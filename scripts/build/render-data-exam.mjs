import { mkdir, readFile, writeFile } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'
import path from 'node:path'
import { createExamMarkdownRenderer } from './exam-markdown.mjs'
import { loadEssayAnswers, renderEssayAnswer } from './essay-answers.mjs'
import { assertCodePreserved } from './exam-code-integrity.mjs'

const root = fileURLToPath(new URL('../../', import.meta.url))
const source = path.join(root, 'raw_materials/xu-ly-du-lieu/exam')
const output = path.join(root, 'src/content/courses/xu-ly-du-lieu/exam')
const draft = process.argv.includes('--draft')
const questionContext = JSON.parse(await readFile(path.join(source, 'question-context.json'), 'utf8'))
const render = await createExamMarkdownRenderer(root)
const essays = await loadEssayAnswers(root)
const essaysOnly = process.argv.includes('--essays-only')
const priorAudit = essaysOnly ? JSON.parse(await readFile(path.join(source, 'render-coverage.json'), 'utf8')) : []
const titles = ['Tổng quan, công cụ và tình huống học tập', 'Python cơ bản cho xử lý dữ liệu',
  'NumPy, mảng và tính toán trên mảng', 'Làm quen với pandas',
  'Series, DataFrame và tổng hợp theo nhóm', 'Kết nối và truy xuất dữ liệu ngoài',
  'Làm sạch chuỗi và biểu thức chính quy', 'Xử lý dữ liệu thời gian']

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
  if (essaysOnly) {
    const compiled = JSON.parse(await readFile(path.join(output, `bai-${lesson}.json`), 'utf8'))
    for (const question of compiled.questions) {
      if (question.kind === 'essay') question.answerHtml = renderEssayAnswer(essays.questions.get(question.id), render)
    }
    await writeFile(path.join(output, `bai-${lesson}.json`), JSON.stringify(compiled, null, 2) + '\n')
    const prior = priorAudit.find(item => item.lesson === lesson)
    audit.push({...prior, essayInputSha256: essays.lessons.get(lesson).inputSha256,
      contentSha256: createHash('sha256').update(JSON.stringify(compiled)).digest('hex')})
    continue
  }
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
      : renderEssayAnswer(essays.questions.get(question.id), render)
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
    reviewed: reviews.size, essayInputSha256: essays.lessons.get(lesson).inputSha256, contentSha256: createHash('sha256').update(JSON.stringify(compiled)).digest('hex') })
}
if (!essaysOnly) await writeFile(path.join(output, 'catalog.json'), JSON.stringify(catalog, null, 2) + '\n')
await writeFile(path.join(source, 'render-coverage.json'), JSON.stringify(audit, null, 2) + '\n')
console.log(essaysOnly ? 'Updated all 184 essay answers; prompts and quiz content preserved.' : `Rendered ${catalog.reduce((n, row) => n + row.total, 0)} questions in 8 banks with current essay answers.`)
