import { mkdir, readFile, writeFile } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'
import path from 'node:path'
import { createMarkdownRenderer } from 'vitepress'
import { configureStudyMarkdown } from './markdown-presentation.mjs'
import { examProsePlugin } from './exam-prose.mjs'
import { assertCodePreserved } from './exam-code-integrity.mjs'

const root = fileURLToPath(new URL('../../', import.meta.url))
const source = path.join(root, 'raw_materials/xu-ly-du-lieu/exam')
const output = path.join(root, 'src/content/courses/xu-ly-du-lieu/exam')
const draft = process.argv.includes('--draft')
const questionContext = JSON.parse(await readFile(path.join(source, 'question-context.json'), 'utf8'))
const md = await createMarkdownRenderer(path.join(root, 'docs'), {
  html: true, math: true, lineNumbers: false,
  config: renderer => { configureStudyMarkdown(renderer, { base: '/' }); renderer.use(examProsePlugin) }
})
// HTML tags discussed in programming questions are data, not author-supplied
// interface markup. MathJax emits its DOM through its own renderer rules.
md.renderer.rules.html_inline = (tokens, index) => md.utils.escapeHtml(tokens[index].content)
md.renderer.rules.html_block = (tokens, index) => md.utils.escapeHtml(tokens[index].content)
const titles = ['Tổng quan, công cụ và tình huống học tập', 'Python cơ bản cho xử lý dữ liệu',
  'NumPy, mảng và tính toán trên mảng', 'Làm quen với pandas',
  'Series, DataFrame và tổng hợp theo nhóm', 'Kết nối và truy xuất dữ liệu ngoài',
  'Làm sạch chuỗi và biểu thức chính quy', 'Xử lý dữ liệu thời gian']

// Local references in the supplied answer notes are citations, not web routes.
function readableLinks(text) {
  return text.replace(/\[([^\]]+)\]\(<?[A-Z]:[/\\][^\n]*?>?\)/g, '$1')
}
function sourceMarkdown(text) {
  // All unquoted dollar signs in these supplied banks are currency or regex
  // characters. Protect them while leaving code text and indentation intact.
  return text.replace(/(^```[^\n]*\n[\s\S]*?^```[ \t]*$)|(`+)([\s\S]*?)\2|\\\$|[$<>]/gm,
    match => ({'$':'\\$', '<':'&lt;', '>':'&gt;'})[match] || match)
}
function render(text = '', literalDollars = false) {
  text = text.replace(/^```python-error[ \t]*$/gm, '```python')
  let html
  try { html = md.render(readableLinks(literalDollars ? sourceMarkdown(text) : text), { relativePath: 'xu-ly-du-lieu/on-thi/index.md' }) }
  catch (error) { throw new Error(`Exam Markdown failed near: ${text.slice(0,300)}`, {cause:error}) }
  if (/data-mjx-error|<merror\b/.test(html)) throw new Error(`Invalid exam math near: ${text.slice(0,300)}`)
  // The shared renderer targets compiled Vue templates. Here the result is
  // already HTML for an outer v-html, so nested Vue bindings must be expanded.
  const entities = {quot:'"', amp:'&', lt:'<', gt:'>'}
  return html.replace(/<a\b[^>]*class="header-anchor"[^>]*>[\s\S]*?<\/a>/g, '')
  .replace(/<(span|div) class="static-math" v-html="([^"]*)"><\/\1>/g, (_, tag, expression) => {
    const json = expression.replace(/&(quot|amp|lt|gt);/g, (_, name) => entities[name])
    return `<${tag} class="static-math">${JSON.parse(json)}</${tag}>`
  }).replace(/<script\b[\s\S]*?<\/script>/gi, '')
}
// Keep the complete downloaded answers in raw_materials. These lines are the
// source author's editing/checking metadata, rather than steps of a solution.
// In particular, an old claim of execution must not stand in for our review.
function solutionBody(text) {
  let fence = false
  return text.split('\n').filter(line => {
    if (/^```/.test(line)) { fence = !fence; return true }
    return fence || !/^\*\*(?:Kiểm chứng|Đối chiếu|Đọc lại|Mục tiêu|Hồ sơ câu|Nhãn|Sai lầm(?: được)? kiểm tra|Kiến thức\/bẫy):\*\*/.test(line)
  }).join('\n').replace(/\n{3,}/g, '\n\n').trim()
}

await mkdir(output, { recursive: true })
const catalog = []
const audit = []
for (let number = 1; number <= 8; number++) {
  const lesson = String(number).padStart(2, '0')
  const bank = JSON.parse(await readFile(path.join(source, `banks/bai-${lesson}.json`), 'utf8'))
  let review
  try { review = JSON.parse(await readFile(path.join(source, `reviews/bai-${lesson}.json`), 'utf8')) }
  catch (error) { if (!draft) throw error }
  const reviews = new Map((review?.items || []).map(item => [item.id, item]))
  let detailed
  try { detailed = JSON.parse(await readFile(path.join(source, `detailed-solutions/bai-${lesson}.json`), 'utf8')) }
  catch (error) { if (!draft) throw error }
  const fullSolutions = new Map((detailed?.items || []).map(item => [item.id, item.markdown]))
  if (!draft && reviews.size !== bank.questions.length) throw new Error(`Incomplete review: ${lesson}`)
  const questions = bank.questions.map(question => {
    const checked = reviews.get(question.id)
    if (!draft && !checked) throw new Error(`Missing review ${question.id}`)
    const correctKey = checked?.correctKey || question.correctKey
    const options = question.options.map(option => {
      const explanation = checked?.optionExplanations?.[option.key]
      if (!draft && !explanation?.trim()) throw new Error(`Missing explanation ${question.id}/${option.key}`)
      const html = render(option.markdown, true)
      assertCodePreserved(option.markdown, html, `${question.id}/${option.key}`)
      return { key: option.key, html, explanationHtml: render(explanation || '', true) }
    })
    const extra = question.kind === 'quiz'
      ? (fullSolutions.get(question.id) || checked?.explanationMarkdown || '')
      : (checked?.explanationMarkdown || '')
    if (!draft && question.kind === 'quiz') {
      if (!fullSolutions.has(question.id)) throw new Error(`Missing detailed solution ${question.id}`)
      for (const key of ['A','B','C','D']) {
        if (!extra.includes(`### Phương án ${key}`)) throw new Error(`Missing detailed option ${question.id}/${key}`)
      }
    }
    const changedKey = question.kind === 'quiz' && correctKey !== question.correctKey
    const correction = changedKey ? `Đáp án đã đối chiếu là ${correctKey}. Tệp đáp án ghi ${question.correctKey}.\n\n` : ''
    const solution = question.kind === 'quiz' && extra.trim()
      ? render(correction) + render(extra)
      : render(correction + solutionBody(question.answerMarkdown), true) + (extra ? render(extra) : '')
    return {
      id: question.id, kind: question.kind, group: question.group,
      promptHtml: (questionContext[question.id] ? render(questionContext[question.id]) : '') + render(question.promptMarkdown, true), options,
      correctKey: question.kind === 'quiz' ? correctKey : null,
      answerHtml: solution,
    }
  })
  const compiled = { lesson, title: titles[number - 1], questions }
  await writeFile(path.join(output, `bai-${lesson}.json`), JSON.stringify(compiled, null, 2) + '\n')
  const counts = { total: questions.length, quiz: questions.filter(q => q.kind === 'quiz').length, essay: questions.filter(q => q.kind === 'essay').length }
  catalog.push({ lesson, title: compiled.title, ...counts })
  audit.push({ lesson, sourceQuestionIds: bank.questions.map(q => q.id), renderedQuestionIds: questions.map(q => q.id),
    inputSha256: createHash('sha256').update(JSON.stringify({bank,review,detailed,questionContext})).digest('hex'),
    reviewed: reviews.size, contentSha256: createHash('sha256').update(JSON.stringify(compiled)).digest('hex') })
}
await writeFile(path.join(output, 'catalog.json'), JSON.stringify(catalog, null, 2) + '\n')
await writeFile(path.join(source, 'render-coverage.json'), JSON.stringify(audit, null, 2) + '\n')
console.log(`Rendered ${catalog.reduce((n, row) => n + row.total, 0)} questions in 8 banks${draft ? ' (draft: pending review)' : ' with reviewed keys and explanations'}.`)
