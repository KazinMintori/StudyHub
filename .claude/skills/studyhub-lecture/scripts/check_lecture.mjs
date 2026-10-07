#!/usr/bin/env node
// Kiểm tra một bài giảng StudyHub đã tích hợp đúng với catalog, Kiến thức nền, Wiki và hình.
// Chỉ kiểm cấu trúc; không đánh giá nội dung, giọng văn hay hiển thị.
//
//   node .claude/skills/studyhub-lecture/scripts/check_lecture.mjs toan-cho-ai/bai-02-tap-loi
//   node .claude/skills/studyhub-lecture/scripts/check_lecture.mjs --all
//   Tùy chọn: --root <repo>  --json
//
// Exit code: 0 không có lỗi (có thể còn cảnh báo), 1 có lỗi, 2 sai cách dùng / không đọc được repo.
import { readFile, access } from 'node:fs/promises'
import path from 'node:path'
import { pathToFileURL } from 'node:url'

const args = process.argv.slice(2)
const flag = name => { const i = args.indexOf(name); if (i < 0) return null; const v = args[i + 1]; args.splice(i, 2); return v }
const has = name => { const i = args.indexOf(name); if (i < 0) return false; args.splice(i, 1); return true }
const asJson = has('--json'), all = has('--all')
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
  console.error('Cách dùng: check_lecture.mjs <course-id>/<slug> [...] | --all  [--root <repo>] [--json]')
  process.exit(2)
}

const load = rel => import(pathToFileURL(path.join(root, rel)).href)
let courseCatalog, concepts, wikiGroups, wikiDetails, relatedConcepts, lectureSlides
try {
  ;({ courseCatalog } = await load('docs/.vitepress/course-catalog.mjs'))
  try { ;({ lectureSlides } = await load('docs/.vitepress/lecture-model.mjs')) } catch { /* repo thử có thể không có */ }
  ;({ concepts } = await load('docs/.vitepress/concepts.mjs'))
  ;({ wikiGroups, wikiDetails, relatedConcepts } = await load('docs/.vitepress/wiki-content.mjs'))
} catch (error) {
  console.error(`Không nạp được catalog/concepts/wiki-content: ${error.message}`)
  process.exit(2)
}

let illustrationTypes = null
try {
  const vue = await readFile(path.join(root, 'docs/.vitepress/theme/CodeIllustration.vue'), 'utf8')
  illustrationTypes = new Set([...vue.matchAll(/type\s*===?\s*'([\w-]+)'/g)].map(m => m[1]))
} catch { /* component có thể không tồn tại trong repo thử */ }

const report = []
const add = (level, where, code, message) => report.push({ level, where, code, message })
const LATEX = /\\[a-zA-Z]+|\$[^$]+\$/
const MARKUP = /\*\*[^*]+\*\*|\$[^$]+\$|\\[a-zA-Z]+/

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
    for (const [field, value] of [['title', s.title], ['formula', s.formula], ['example', s.example], ...(s.bullets || []).map((b, k) => [`bullets[${k}]`, b])])
      if (typeof value === 'string' && LATEX.test(value)) add('error', sw, 'SLIDE_LATEX', `${field} chứa LaTeX/$…$; chuỗi slide hiển thị nguyên văn, dùng Unicode.`)
  })

  for (const id of lesson.prerequisites || []) {
    const pw = `${where} prerequisite "${id}"`
    if (!concepts[id]) { add('error', pw, 'PREREQ_NOT_IN_CONCEPTS', 'Không có trong concepts.mjs.'); continue }
    if (!wikiGroups.some(g => g.ids.includes(id))) add('error', pw, 'PREREQ_NOT_IN_GROUP', 'Không thuộc nhóm nào trong wikiGroups.')
    if (!wikiDetails[id]) add('error', pw, 'PREREQ_NO_DETAILS', 'Thiếu wikiDetails.')
    if (!await exists(path.join(root, `docs/wiki/${id}.md`))) add('warning', pw, 'WIKI_FILE_MISSING', 'Chưa có docs/wiki/<id>.md; chạy npm run sync:courses rồi biên tập file.')
    const t = concepts[id]
    for (const field of ['definition', 'example', 'use', 'question', 'answer'])
      if (typeof t[field] === 'string' && MARKUP.test(t[field])) add('warning', pw, 'CONCEPT_MARKUP', `concepts.${field} chứa Markdown/LaTeX; tab Kiến thức nền hiển thị văn bản thuần.`)
  }

  // Nội dung Markdown
  const lines = proseLines(source).filter(l => l.n > front.bodyStart)
  const stack = [], smallSvgs = []
  let lastClosed = null
  for (const { n, raw } of lines) {
    const line = raw.trim()
    if (/^#\s/.test(line)) add('warning', `${rel}:${n}`, 'EXTRA_H1', 'Notes có H1; header trang đã có tiêu đề từ catalog.')
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
    for (const m of raw.matchAll(/\]\(\/wiki\/([\w-]+)(?:\.md|\.html)?(?:#[^)]*)?\)/g))
      if (!concepts[m[1]]) add('error', `${rel}:${n}`, 'WIKI_LINK_BROKEN', `Link tới /wiki/${m[1]} nhưng không có thuật ngữ này.`)
    for (const m of raw.matchAll(/\]\(\/([\w-]+)\/bai-giang\/([\w-]+?)(?:\.md|\.html)?(?:#[^)]*)?\)/g)) {
      const other = courseCatalog.find(c => c.id === m[1])
      if (!other || !other.lessons.some(l => l.slug === m[2])) add('error', `${rel}:${n}`, 'LECTURE_LINK_BROKEN', `Link tới bài /${m[1]}/bai-giang/${m[2]} không có trong catalog.`)
    }
  }
  if (smallSvgs.length) {
    const worst = smallSvgs.reduce((a, b) => (b.phonePx < a.phonePx ? b : a))
    add('warning', where, 'SVG_SMALL_TEXT', `${smallSvgs.length} hình SVG có chữ < 12 đơn vị; nhỏ nhất ở ${worst.file}: ${Math.min(...worst.sizes)} → khoảng ${worst.phonePx.toFixed(1)}px trên màn hình 375px. Site có lightbox để phóng to, nhưng nhãn cần đọc để hiểu bài nên đọc được ngay; xem lại ở bề rộng điện thoại. Ví dụ: ${smallSvgs.slice(0, 3).map(x => x.file).join(', ')}${smallSvgs.length > 3 ? ', …' : ''}.`)
  }
  for (const open of stack) add('error', `${rel}:${open.n}`, 'CONTAINER_UNCLOSED', `::: ${open.name} chưa được đóng.`)
  const exercises = lines.filter(l => /^:{3,}\s*exercise\b/.test(l.raw.trim())).length
  const solutions = lines.filter(l => /^:{3,}\s*solution\b/.test(l.raw.trim())).length
  if (exercises && solutions < exercises) add('warning', where, 'EXERCISE_WITHOUT_SOLUTION', `${exercises} bài tập nhưng chỉ ${solutions} lời giải gập.`)
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
if (asJson) console.log(JSON.stringify({ checked: targets.map(([c, l]) => `${c.id}/${l.slug}`), errors, warnings, notes }, null, 2))
else {
  const label = { error: 'LỖI   ', warning: 'CẢNH BÁO', note: 'GHI CHÚ' }
  // Với --all, ghi chú chỉ được đếm để danh sách không bị ngập.
  for (const r of report) if (!(all && r.level === 'note')) console.log(`${label[r.level]} [${r.code}] ${r.where}: ${r.message}`)
  console.log(`\nĐã kiểm ${targets.length} bài: ${errors.length} lỗi, ${warnings.length} cảnh báo, ${notes.length} ghi chú${all && notes.length ? ' (ẩn; xem bằng --json hoặc kiểm từng bài)' : ''}. Chỉ kiểm cấu trúc — nội dung, giọng và hiển thị vẫn cần đọc và xem trang.`)
}
process.exit(errors.length ? 1 : 0)
