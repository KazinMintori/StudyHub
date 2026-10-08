#!/usr/bin/env node
// Kiểm tra một bài giảng StudyHub đã tích hợp đúng với catalog, Kiến thức nền, Wiki và hình.
// Bài nhiều lớp (lesson.topicGroups) còn được kiểm từng trang chủ đề trong bai-giang/<slug>/.
// Chỉ kiểm cấu trúc; không đánh giá nội dung, giọng văn hay hiển thị.
//
//   node .claude/skills/studyhub-lecture/scripts/check_lecture.mjs toan-cho-ai/bai-02-tap-loi
//   node .claude/skills/studyhub-lecture/scripts/check_lecture.mjs --all
//   Tùy chọn: --root <repo>  --json  --no-math (bỏ phép đo bề rộng công thức inline)
//
// Exit code: 0 không có lỗi (có thể còn cảnh báo), 1 có lỗi, 2 sai cách dùng / không đọc được repo.
import { readFile, readdir, access } from 'node:fs/promises'
import { createRequire } from 'node:module'
import path from 'node:path'
import { pathToFileURL } from 'node:url'

const args = process.argv.slice(2)
const flag = name => { const i = args.indexOf(name); if (i < 0) return null; const v = args[i + 1]; args.splice(i, 2); return v }
const has = name => { const i = args.indexOf(name); if (i < 0) return false; args.splice(i, 1); return true }
const asJson = has('--json'), all = has('--all'), noMath = has('--no-math')
let root = flag('--root')

const exists = async file => { try { await access(file); return true } catch { return false } }
async function findRoot(start) {
  let dir = path.resolve(start)
  while (true) {
    if (await exists(path.join(dir, 'docs/.vitepress/course-catalog.mjs'))) return dir
    const parent = path.dirname(dir)
    if (parent === dir) return null
    dir = parent
  }
}
root = root ? path.resolve(root) : await findRoot(process.cwd())
if (!root || !await exists(path.join(root, 'docs/.vitepress/course-catalog.mjs'))) {
  console.error('Không tìm thấy repo StudyHub (cần docs/.vitepress/course-catalog.mjs). Dùng --root <đường dẫn>.')
  process.exit(2)
}
if (!all && !args.length) {
  console.error('Cách dùng: check_lecture.mjs <course-id>/<slug> [...] | --all  [--root <repo>] [--json] [--no-math]')
  process.exit(2)
}

const load = rel => import(pathToFileURL(path.join(root, rel)).href)
let courseCatalog, concepts, wikiGroups, wikiDetails, relatedConcepts, lectureSlides, lessonTopicsFn
try {
  ;({ courseCatalog } = await load('docs/.vitepress/course-catalog.mjs'))
  try { ;({ lectureSlides, lessonTopics: lessonTopicsFn } = await load('docs/.vitepress/lecture-model.mjs')) } catch { /* repo thử có thể không có */ }
  ;({ concepts } = await load('docs/.vitepress/concepts.mjs'))
  ;({ wikiGroups, wikiDetails, relatedConcepts } = await load('docs/.vitepress/wiki-content.mjs'))
} catch (error) {
  console.error(`Không nạp được catalog/concepts/wiki-content: ${error.message}`)
  process.exit(2)
}
// Cùng thứ tự đọc với site: các nhóm chủ đề trải phẳng theo catalog.
const lessonTopics = lesson => (lessonTopicsFn ? lessonTopicsFn(lesson)
  : (lesson?.topicGroups || []).flatMap((group, groupIndex) => (group.topics || []).map(topic => ({ ...topic, group: group.title, groupIndex }))))

let illustrationTypes = null
try {
  const vue = await readFile(path.join(root, 'docs/.vitepress/theme/CodeIllustration.vue'), 'utf8')
  illustrationTypes = new Set([...vue.matchAll(/type\s*===?\s*'([\w-]+)'/g)].map(m => m[1]))
} catch { /* component có thể không tồn tại trong repo thử */ }

// Đo bề rộng công thức inline bằng chính markdown-it-mathjax3 của site, nếu repo đã cài.
// Công thức inline không xuống dòng được; rộng hơn khoảng 38ex là tràn ngang ở màn hình 375px.
const INLINE_MATH_LIMIT_EX = 38
let measureInline = null
if (!noMath) {
  try {
    const require = createRequire(path.join(root, 'package.json'))
    const MarkdownIt = require('markdown-it')
    const mathjax = require('markdown-it-mathjax3')
    const md = new MarkdownIt({ html: true }).use(mathjax.default || mathjax)
    const cache = new Map()
    measureInline = tex => {
      if (!cache.has(tex)) { const w = /width="([\d.]+)ex"/.exec(md.renderInline(`$${tex}$`)); cache.set(tex, w ? Number(w[1]) : 0) }
      return cache.get(tex)
    }
  } catch { /* repo thử không có node_modules: bỏ qua phép đo */ }
}

const report = []
const add = (level, where, code, message) => report.push({ level, where, code, message })
const LATEX = /\\[a-zA-Z]+|\$[^$]+\$/
const MARKUP = /\*\*[^*]+\*\*|\$[^$]+\$|\\[a-zA-Z]+/
let rendersMathText = false
try {
  const panels = await readFile(path.join(root, 'docs/.vitepress/theme/LecturePanels.vue'), 'utf8')
  rendersMathText = panels.includes('<MathText') && await exists(path.join(root, 'docs/.vitepress/theme/MathText.vue'))
} catch { /* Older repositories and test fixtures still use plain text. */ }
const outsideMath = value => value.replace(/\$\$[\s\S]*?\$\$|\$[^$\n]+\$/g, '')
function checkMathText(value, where, field) {
  const plain = outsideMath(value)
  if (plain.includes('$')) add('error', where, 'MATH_DELIMITER', `${field} có dấu $ không được ghép cặp.`)
  if (/\\[a-zA-Z]+/.test(plain)) add('error', where, 'SLIDE_LATEX', `${field} có lệnh TeX ngoài $…$ hoặc $$…$$.`)
}

function parseFrontmatter(source) {
  const match = source.match(/^﻿?---\r?\n([\s\S]*?)\r?\n---\r?\n/)
  if (!match) return null
  const data = {}
  for (const line of match[1].split(/\r?\n/)) {
    const kv = line.match(/^([A-Za-z_][\w-]*):\s*(.*)$/)
    if (!kv) continue
    let [, key, value] = kv
    value = value.trim()
    if (value.startsWith('[')) {
      try { data[key] = JSON.parse(value) } catch {
        data[key] = value.replace(/^\[|\]$/g, '').split(',').map(s => s.trim().replace(/^['"]|['"]$/g, '')).filter(Boolean)
      }
    } else if (/^".*"$/.test(value)) {
      try { data[key] = JSON.parse(value) } catch { data[key] = value.slice(1, -1) }
    } else data[key] = value.replace(/^'|'$/g, '')
  }
  return { data, bodyStart: match[0].split('\n').length - 1 }
}

// Trả về các dòng ngoài code fence, kèm số dòng (1-based).
function proseLines(source) {
  const out = []; let fence = null
  source.split(/\r?\n/).forEach((raw, i) => {
    const m = raw.trim().match(/^(`{3,}|~{3,})/)
    if (m) {
      if (!fence) fence = m[1]
      else if (m[1][0] === fence[0] && m[1].length >= fence.length) fence = null
      return
    }
    if (!fence) out.push({ n: i + 1, raw })
  })
  return out
}

const sameList = (a, b) => Array.isArray(a) && Array.isArray(b) && a.length === b.length && a.every((x, i) => x === b[i])

// Phần thân Markdown của một trang Notes hoặc một trang chủ đề.
async function checkBody({ source, front, rel, file, where, smallSvgs }) {
  const lines = proseLines(source).filter(l => l.n > front.bodyStart)
  const stack = []
  let lastClosed = null
  for (const { n, raw } of lines) {
    const line = raw.trim()
    if (/^#\s/.test(line)) add('warning', `${rel}:${n}`, 'EXTRA_H1', 'Trang có H1; header trang đã có tiêu đề từ catalog.')
    const open = line.match(/^(:{3,})\s*([A-Za-z][\w-]*)/)
    const close = line.match(/^(:{3,})\s*$/)
    if (open) {
      // Lời giải gập phải đi ngay sau đề (hoặc gợi ý), chỉ cách nhau bởi dòng trống.
      if (open[2] === 'solution' && !(lastClosed && ['exercise', 'hint'].includes(lastClosed)))
        add('warning', `${rel}:${n}`, 'SOLUTION_WITHOUT_EXERCISE', '::: solution không đứng ngay sau ::: exercise/hint.')
      stack.push({ marker: open[1], name: open[2], n })
      lastClosed = null
    } else if (close) {
      const top = stack[stack.length - 1]
      if (!top) add('error', `${rel}:${n}`, 'CONTAINER_UNBALANCED', 'Dòng ::: đóng mà không có container mở.')
      else if (close[1].length === top.marker.length) { stack.pop(); lastClosed = top.name }
    } else if (line) lastClosed = null
    for (const m of raw.matchAll(/!\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)|<img[^>]+src="([^"]+)"/g)) {
      const target = (m[1] || m[2]).split(/[?#]/)[0]
      if (/^(https?:)?\/\//.test(target) || target.startsWith('data:')) continue
      const candidates = target.startsWith('/')
        ? [path.join(root, 'docs/public', target), path.join(root, 'docs', target), path.join(root, target)]
        : [path.join(path.dirname(file), decodeURI(target))]
      let found = false
      for (const c of candidates) if (await exists(c)) { found = true; if (c.endsWith('.svg')) await checkSvg(c, `${rel}:${n}`, smallSvgs) }
      if (!found) add('error', `${rel}:${n}`, 'IMAGE_MISSING', `Không tìm thấy hình ${target}.`)
    }
    for (const m of raw.matchAll(/<CodeIllustration\s+type="([\w-]+)"/g))
      if (illustrationTypes && !illustrationTypes.has(m[1])) add('error', `${rel}:${n}`, 'ILLUSTRATION_TYPE', `CodeIllustration type="${m[1]}" chưa được hỗ trợ (có: ${[...illustrationTypes].join(', ')}).`)
    // Mô phỏng tương tác: theme/index.js đăng ký mọi file theme/*Lab.vue theo tên file.
    for (const m of raw.matchAll(/<([A-Z]\w*Lab)\b/g))
      if (!await exists(path.join(root, 'docs/.vitepress/theme', `${m[1]}.vue`))) add('error', `${rel}:${n}`, 'LAB_MISSING', `Không có component docs/.vitepress/theme/${m[1]}.vue.`)
    for (const m of raw.matchAll(/\]\(\/wiki\/([\w-]+)(?:\.md|\.html)?(?:#[^)]*)?\)/g))
      if (!concepts[m[1]]) add('error', `${rel}:${n}`, 'WIKI_LINK_BROKEN', `Link tới /wiki/${m[1]} nhưng không có thuật ngữ này.`)
    for (const m of raw.matchAll(/\]\(\/([\w-]+)\/bai-giang\/([\w-]+?)(?:\.md|\.html)?(?:#[^)]*)?\)/g)) {
      const other = courseCatalog.find(c => c.id === m[1])
      if (!other || !other.lessons.some(l => l.slug === m[2])) add('error', `${rel}:${n}`, 'LECTURE_LINK_BROKEN', `Link tới bài /${m[1]}/bai-giang/${m[2]} không có trong catalog.`)
    }
    // Link tương đối tới một trang khác của site phải trỏ tới file có thật.
    for (const m of raw.matchAll(/\]\((\.{1,2}\/[^)\s#]+?\.(?:md|html))(?:#[^)]*)?\)/g)) {
      const target = path.join(path.dirname(file), decodeURI(m[1]).replace(/\.html$/, '.md'))
      if (!await exists(target)) add('error', `${rel}:${n}`, 'RELATIVE_LINK_BROKEN', `Link ${m[1]} không trỏ tới file nào.`)
    }
    if (measureInline) {
      const plain = raw.replace(/\$\$[^$]*\$\$/g, '')
      for (const m of plain.matchAll(/(?<![\\$])\$(?!\$)([^$\n]+?)\$(?!\$)/g)) {
        const width = measureInline(m[1])
        if (width > INLINE_MATH_LIMIT_EX) add('warning', `${rel}:${n}`, 'INLINE_MATH_WIDE', `Công thức inline rộng ${width.toFixed(1)}ex (> ${INLINE_MATH_LIMIT_EX}ex) sẽ tràn ngang trên điện thoại; chuyển thành công thức hiển thị $$…$$ hoặc tách nhỏ: $${m[1].slice(0, 60)}${m[1].length > 60 ? '…' : ''}$.`)
      }
    }
  }
  for (const open of stack) add('error', `${rel}:${open.n}`, 'CONTAINER_UNCLOSED', `::: ${open.name} chưa được đóng.`)
  const exercises = lines.filter(l => /^:{3,}\s*exercise\b/.test(l.raw.trim())).length
  const solutions = lines.filter(l => /^:{3,}\s*solution\b/.test(l.raw.trim())).length
  if (exercises && solutions < exercises) add('warning', where, 'EXERCISE_WITHOUT_SOLUTION', `${exercises} bài tập nhưng chỉ ${solutions} lời giải gập.`)
}

function reportSmallSvgs(where, smallSvgs) {
  if (!smallSvgs.length) return
  const worst = smallSvgs.reduce((a, b) => (b.phonePx < a.phonePx ? b : a))
  add('warning', where, 'SVG_SMALL_TEXT', `${smallSvgs.length} hình SVG có chữ < 12 đơn vị; nhỏ nhất ở ${worst.file}: ${Math.min(...worst.sizes)} → khoảng ${worst.phonePx.toFixed(1)}px trên màn hình 375px. Site có lightbox để phóng to, nhưng nhãn cần đọc để hiểu bài nên đọc được ngay; xem lại ở bề rộng điện thoại. Ví dụ: ${smallSvgs.slice(0, 3).map(x => x.file).join(', ')}${smallSvgs.length > 3 ? ', …' : ''}.`)
}

let topicCount = 0
async function checkLesson(course, lesson) {
  const rel = `docs/${course.id}/bai-giang/${lesson.slug}.md`
  const where = `${course.id}/${lesson.slug}`
  const file = path.join(root, rel)
  if (!await exists(file)) { add('error', where, 'NOTES_MISSING', `Không có file ${rel}.`); return }
  const source = await readFile(file, 'utf8')
  const front = parseFrontmatter(source)
  if (!front) { add('error', where, 'FRONTMATTER_MISSING', 'File Notes thiếu frontmatter YAML.'); return }
  const fm = front.data
  if (fm.course !== course.id) add('error', where, 'FRONTMATTER_COURSE', `course: "${fm.course}" phải là "${course.id}".`)
  if (fm.lecture !== lesson.slug) add('error', where, 'FRONTMATTER_LECTURE', `lecture: "${fm.lecture}" phải trùng slug "${lesson.slug}".`)
  if (fm.section !== 'lecture') add('error', where, 'FRONTMATTER_SECTION', 'Cần section: lecture.')
  if (fm.title !== lesson.title) add('warning', where, 'TITLE_MISMATCH', `title trong frontmatter ("${fm.title}") khác catalog ("${lesson.title}"); header trang lấy từ catalog.`)
  if (!sameList(fm.prerequisites, lesson.prerequisites)) add('warning', where, 'PREREQ_MISMATCH', `prerequisites trong frontmatter ${JSON.stringify(fm.prerequisites)} khác catalog ${JSON.stringify(lesson.prerequisites)}; tab Kiến thức nền dùng catalog.`)
  if (fm.lessonStatus !== lesson.status) add('error', where, 'STATUS_MISMATCH', `lessonStatus "${fm.lessonStatus}" khác status catalog "${lesson.status}".`)
  if (!fm.description) add('note', where, 'NO_DESCRIPTION', 'Thiếu description (dùng cho tìm kiếm và thẻ trang).')

  if (course.parts && !course.parts.some(p => (p.lessons || []).includes(lesson.slug)))
    add('error', where, 'NOT_IN_PARTS', 'Slug không có trong course.parts → bài không hiện trong sidebar.')
  // Dùng đúng hàm của site (có slide dự phòng viết cứng cho vài bài); repo thử thì lọc theo note.
  const slides = lectureSlides ? lectureSlides(course, lesson) : (course.slides || []).filter(s => s.note === lesson.slug)
  if (lesson.status === 'ready' && !slides.length) add('error', where, 'READY_WITHOUT_SLIDES', 'Bài ready nhưng catalog chưa có slide nào note trỏ tới bài.')
  slides.forEach((s, i) => {
    const sw = `${where} slide ${i + 1} "${s.title}"`
    if (!Array.isArray(s.bullets) || !s.bullets.length) add('error', sw, 'SLIDE_NO_BULLETS', 'Slide không có bullet.')
    else if (s.bullets.length > 5) add('warning', sw, 'SLIDE_TOO_DENSE', `${s.bullets.length} bullet; slide catalog là bản ôn ngắn (2–4 ý).`)
    for (const [field, value] of [['title', s.title], ['formula', s.formula], ['example', s.example], ...(s.bullets || []).map((b, k) => [`bullets[${k}]`, b])]) {
      if (typeof value !== 'string') continue
      if (rendersMathText) checkMathText(value, sw, field)
      else if (LATEX.test(value)) add('error', sw, 'SLIDE_LATEX', `${field} chứa LaTeX/$…$; chuỗi slide hiển thị nguyên văn, dùng Unicode.`)
    }
  })

  const prerequisiteSet = new Set(lesson.prerequisites || [])
  for (const id of lesson.supportingConcepts || [])
    if (prerequisiteSet.has(id)) add('warning', `${where} supporting concept "${id}"`, 'CONCEPT_IN_BOTH_LISTS', 'Khái niệm xuất hiện ở cả prerequisites và supportingConcepts; chỉ giữ trong nhóm đúng vai trò.')
  for (const [kind, ids] of [['prerequisite', lesson.prerequisites || []], ['supporting concept', lesson.supportingConcepts || []]]) for (const id of ids) {
    const pw = `${where} ${kind} "${id}"`
    const code = kind === 'prerequisite' ? 'PREREQ' : 'SUPPORT'
    if (!concepts[id]) { add('error', pw, `${code}_NOT_IN_CONCEPTS`, 'Không có trong concepts.mjs.'); continue }
    if (!wikiGroups.some(g => g.ids.includes(id))) add('error', pw, `${code}_NOT_IN_GROUP`, 'Không thuộc nhóm nào trong wikiGroups.')
    if (!wikiDetails[id]) add('error', pw, `${code}_NO_DETAILS`, 'Thiếu wikiDetails.')
    if (!await exists(path.join(root, `docs/wiki/${id}.md`))) add('warning', pw, 'WIKI_FILE_MISSING', 'Chưa có docs/wiki/<id>.md; chạy npm run sync:courses rồi biên tập file.')
    const t = concepts[id]
    for (const field of ['definition', 'example', 'use', 'question', 'answer']) {
      if (typeof t[field] !== 'string') continue
      if (rendersMathText) {
        checkMathText(t[field], pw, `concepts.${field}`)
        if (/\*\*[^*]+\*\*/.test(outsideMath(t[field]))) add('warning', pw, 'CONCEPT_MARKUP', `concepts.${field} chứa Markdown; MathText chỉ hỗ trợ văn bản và công thức TeX.`)
      } else if (MARKUP.test(t[field])) add('warning', pw, 'CONCEPT_MARKUP', `concepts.${field} chứa Markdown/LaTeX; tab Kiến thức nền hiển thị văn bản thuần.`)
    }
  }

  const smallSvgs = []
  await checkBody({ source, front, rel, file, where, smallSvgs })
  const topics = lessonTopics(lesson)
  if (topics.length && !/<TopicMap\b/.test(source)) add('warning', where, 'HUB_NO_TOPIC_MAP', 'Bài có các trang chủ đề nhưng trang chương không đặt <TopicMap />; người học khó thấy bản đồ chủ đề.')
  for (const topic of topics) await checkTopic(course, lesson, topic, smallSvgs)
  if (topics.length) {
    // File chủ đề nằm trong thư mục nhưng không có trong catalog sẽ không có thanh điều hướng, tiến độ hay sidebar.
    const dir = path.join(root, `docs/${course.id}/bai-giang/${lesson.slug}`)
    let names = []
    try { names = (await readdir(dir, { withFileTypes: true })).filter(d => d.isFile() && d.name.endsWith('.md')).map(d => d.name.replace(/\.md$/, '')) } catch { /* thư mục chưa có */ }
    for (const name of names) if (!topics.some(t => t.slug === name)) add('warning', `${where}/${name}`, 'TOPIC_ORPHAN', `File chủ đề ${name}.md không có trong topicGroups của catalog.`)
  }
  reportSmallSvgs(where, smallSvgs)
}

async function checkTopic(course, lesson, topic, smallSvgs) {
  topicCount++
  const rel = `docs/${course.id}/bai-giang/${lesson.slug}/${topic.slug}.md`
  const where = `${course.id}/${lesson.slug}/${topic.slug}`
  const file = path.join(root, rel)
  if (!await exists(file)) { add('error', where, 'TOPIC_MISSING', `Catalog khai báo chủ đề nhưng không có file ${rel}.`); return }
  const source = await readFile(file, 'utf8')
  const front = parseFrontmatter(source)
  if (!front) { add('error', where, 'FRONTMATTER_MISSING', 'File chủ đề thiếu frontmatter YAML.'); return }
  const fm = front.data
  if (fm.course !== course.id) add('error', where, 'FRONTMATTER_COURSE', `course: "${fm.course}" phải là "${course.id}".`)
  if (fm.lecture !== lesson.slug) add('error', where, 'FRONTMATTER_LECTURE', `lecture: "${fm.lecture}" phải là "${lesson.slug}".`)
  if (fm.topic !== topic.slug) add('error', where, 'FRONTMATTER_TOPIC', `topic: "${fm.topic}" phải trùng slug "${topic.slug}".`)
  if (fm.section !== 'topic') add('error', where, 'FRONTMATTER_SECTION', 'Trang chủ đề cần section: topic.')
  if (fm.title !== topic.title) add('warning', where, 'TOPIC_TITLE_MISMATCH', `title ("${fm.title}") khác catalog ("${topic.title}"); header, thanh điều hướng và sidebar lấy từ catalog.`)
  if (!fm.description) add('note', where, 'NO_DESCRIPTION', 'Thiếu description (dùng cho tìm kiếm và thẻ trang).')
  await checkBody({ source, front, rel, file, where, smallSvgs })
}

const checkedSvgs = new Set()
async function checkSvg(file, where, smallSvgs) {
  if (checkedSvgs.has(file)) return
  checkedSvgs.add(file)
  const svg = await readFile(file, 'utf8')
  if (!/viewBox=/.test(svg)) add('warning', where, 'SVG_NO_VIEWBOX', `${path.relative(root, file)} không có viewBox; hình khó co giãn trên điện thoại.`)
  const small = [...svg.matchAll(/font-size(?:=|:\s*)["']?(\d+(?:\.\d+)?)/g)].map(m => +m[1]).filter(v => v < 12)
  // Cỡ chữ hiển thị ≈ font-size × (bề rộng khung ~343px ở điện thoại 375px) / bề rộng viewBox.
  const vb = svg.match(/viewBox=["']\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)/)
  const width = vb ? +vb[1] : 680
  if (small.length) smallSvgs.push({ file: path.basename(file), sizes: small, phonePx: Math.min(...small) * 343 / width })
}

async function checkSite() {
  const ids = Object.keys(concepts)
  const grouped = wikiGroups.flatMap(g => g.ids)
  for (const id of grouped) if (!concepts[id]) add('error', `wikiGroups`, 'GROUP_UNKNOWN_ID', `"${id}" có trong wikiGroups nhưng không có trong concepts.`)
  const seen = new Set()
  for (const id of grouped) { if (seen.has(id)) add('error', 'wikiGroups', 'GROUP_DUPLICATE', `"${id}" xuất hiện ở nhiều nhóm.`); seen.add(id) }
  for (const id of ids) {
    if (!seen.has(id)) add('error', `concepts "${id}"`, 'CONCEPT_NO_GROUP', 'Không thuộc nhóm nào trong wikiGroups.')
    if (!wikiDetails[id]) add('error', `concepts "${id}"`, 'CONCEPT_NO_DETAILS', 'Thiếu wikiDetails.')
    try { for (const other of relatedConcepts(id)) if (!concepts[other] || other === id) add('error', `concepts "${id}"`, 'BAD_RELATED', `Thuật ngữ liên quan "${other}" không hợp lệ.`) }
    catch (error) { add('error', `concepts "${id}"`, 'RELATED_THROWS', `relatedConcepts lỗi: ${error.message}`) }
  }
  for (const course of courseCatalog) {
    for (const part of course.parts || []) for (const slug of part.lessons || [])
      if (!course.lessons.some(l => l.slug === slug)) add('error', `${course.id} parts`, 'PART_UNKNOWN_LESSON', `"${slug}" có trong parts nhưng không có trong lessons.`)
    for (const s of course.slides || [])
      if (!course.lessons.some(l => l.slug === s.note)) add('error', `${course.id} slide "${s.title}"`, 'SLIDE_UNKNOWN_NOTE', `note "${s.note}" không trỏ tới bài nào.`)
    for (const lesson of course.lessons) {
      const slugs = lessonTopics(lesson).map(t => t.slug)
      for (const [i, slug] of slugs.entries()) {
        if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug)) add('error', `${course.id}/${lesson.slug}`, 'TOPIC_SLUG', `Slug chủ đề "${slug}" phải gồm chữ thường không dấu, số và gạch nối.`)
        if (slugs.indexOf(slug) !== i) add('error', `${course.id}/${lesson.slug}`, 'TOPIC_DUPLICATE', `Slug chủ đề "${slug}" lặp lại trong topicGroups.`)
      }
    }
  }
}

const targets = []
if (all) {
  for (const course of courseCatalog) for (const lesson of course.lessons) targets.push([course, lesson])
  await checkSite()
} else {
  for (const arg of args) {
    const [courseId, slug] = arg.replace(/\.md$/, '').replace(/^docs\//, '').replace('/bai-giang/', '/').split('/')
    const course = courseCatalog.find(c => c.id === courseId)
    if (!course) { add('error', arg, 'UNKNOWN_COURSE', `Không có môn "${courseId}" trong catalog.`); continue }
    const lesson = course.lessons.find(l => l.slug === slug)
    if (!lesson) { add('error', arg, 'LESSON_NOT_IN_CATALOG', `Chưa khai báo lesson('${slug}', …) trong catalog của môn ${courseId}.`); continue }
    targets.push([course, lesson])
  }
}
for (const [course, lesson] of targets) await checkLesson(course, lesson)

const errors = report.filter(r => r.level === 'error'), warnings = report.filter(r => r.level === 'warning'), notes = report.filter(r => r.level === 'note')
if (asJson) console.log(JSON.stringify({ checked: targets.map(([c, l]) => `${c.id}/${l.slug}`), topics: topicCount, errors, warnings, notes }, null, 2))
else {
  const label = { error: 'LỖI   ', warning: 'CẢNH BÁO', note: 'GHI CHÚ' }
  // Với --all, ghi chú chỉ được đếm để danh sách không bị ngập.
  for (const r of report) if (!(all && r.level === 'note')) console.log(`${label[r.level]} [${r.code}] ${r.where}: ${r.message}`)
  console.log(`\nĐã kiểm ${targets.length} bài${topicCount ? ` và ${topicCount} trang chủ đề` : ''}: ${errors.length} lỗi, ${warnings.length} cảnh báo, ${notes.length} ghi chú${all && notes.length ? ' (ẩn; xem bằng --json hoặc kiểm từng bài)' : ''}. ${measureInline ? '' : 'Không đo bề rộng công thức (thiếu markdown-it-mathjax3 hoặc có --no-math). '}Chỉ kiểm cấu trúc — nội dung, giọng và hiển thị vẫn cần đọc và xem trang.`)
}
process.exit(errors.length ? 1 : 0)
