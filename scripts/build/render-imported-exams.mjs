import { readFile, writeFile, mkdir } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createHash } from 'node:crypto'
import { createExamMarkdownRenderer } from './exam-markdown.mjs'
import { assertCodePreserved } from './exam-code-integrity.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..')
const sourcePath = path.join(root, 'raw_materials/xu-ly-du-lieu/exam-papers/source.json')
const source = JSON.parse(await readFile(sourcePath, 'utf8'))
const metadata = JSON.parse(await readFile(path.join(path.dirname(sourcePath), 'metadata.json'), 'utf8'))
const output = path.join(root, 'src/content/courses/xu-ly-du-lieu/de-thi')
await mkdir(output, { recursive: true })
const render = await createExamMarkdownRenderer(root)
const renderOriginal = await createExamMarkdownRenderer(root, { preserveProse: true })
const escapeProse = text => text.replace(/\\/g, '\\\\').replace(/[`*_{}[\]#$]/g, '\\$&')
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
const itemMarkdown = item => item.kind === 'code'
  ? `\`\`\`python\n${item.text}\n\`\`\`` : escapeProse(item.text)
const catalog = []
const coverage = []
for (const exam of source.exams) {
  const meta = metadata[exam.code]
  if(!meta || !['official','practice'].includes(meta.examType)) throw new Error(`Missing exam metadata: ${exam.code}`)
  if(meta.examDate && (!/^\d{4}-\d{2}-\d{2}$/.test(meta.examDate) || new Date(meta.examDate).toISOString().slice(0,10)!==meta.examDate)) throw new Error(`Invalid exam date: ${exam.code}`)
  const examTypeLabel = meta.examType === 'official' ? 'Đề chính thức' : 'Đề luyện tập'
  const academicTerm = `Học kỳ ${meta.semester}, năm học ${meta.academicYear}`
  const examDateLabel = meta.examDate ? meta.examDate.split('-').reverse().join('/') : ''
  const paperInfo = {...meta, examTypeLabel, academicTerm, examDateLabel}
  const questions = exam.questions.map(q => {
    const promptItems = q.items.filter(x => x.kind !== 'choice')
    const promptMarkdown = promptItems.map(itemMarkdown).join('\n\n')
    const promptHtml = renderOriginal(promptMarkdown)
    assertCodePreserved(promptMarkdown, promptHtml, `${q.id}/prompt`)
    const summary = render(q.answerSummaryMarkdown)
    const answerHtml = render(q.solutionMarkdown)
    assertCodePreserved(q.solutionMarkdown, answerHtml, `${q.id}/solution`)
    const options = q.items.filter(x => x.kind === 'choice').map(option => ({
      key: option.label,
      html: renderOriginal(escapeProse(option.text)),
      explanationHtml: q.grading === 'manual'
        ? ''
        : render(q.correctKeys.includes(option.label) ? 'Phương án đúng.' : 'Phương án này không phù hợp với kết quả đã kiểm chứng.') + summary,
    }))
    return {
      id: q.id, kind: q.kind, sourceNumber: q.n, group: `${q.points} điểm`,
      promptHtml, options, correctKey: q.correctKey, correctKeys: q.correctKeys,
      grading: q.grading, reviewNoteHtml: q.reviewNote ? renderOriginal(escapeProse(q.reviewNote)) : '', answerHtml,
    }
  })
  const bank = { id: exam.id, title: exam.title, code: exam.code, ...paperInfo, questions }
  await writeFile(path.join(output, `${exam.id}.json`), JSON.stringify(bank, null, 2) + '\n')
  catalog.push({ id: exam.id, slug: exam.id, title: exam.title, number: exam.number, code: exam.code,
    ...paperInfo, description: `${examTypeLabel} · Mã đề ${exam.code} · ${academicTerm}${examDateLabel ? ` · Ngày thi: ${examDateLabel}` : ''}`, total: questions.length, quiz: 20, essay: 6 })
  coverage.push({ id: exam.id, questions: questions.map(q => q.id),
    sourceSha256: createHash('sha256').update(JSON.stringify(exam)).digest('hex'),
    metadataSha256: createHash('sha256').update(JSON.stringify(meta)).digest('hex'),
    renderedSha256: createHash('sha256').update(JSON.stringify(bank)).digest('hex') })
  console.log(`Rendered ${exam.title} (${exam.code}): ${questions.length} questions`)
}
await writeFile(path.join(output, 'catalog.json'), JSON.stringify(catalog, null, 2) + '\n')
await writeFile(path.join(root, 'raw_materials/xu-ly-du-lieu/exam-papers/render-coverage.json'), JSON.stringify(coverage, null, 2) + '\n')
