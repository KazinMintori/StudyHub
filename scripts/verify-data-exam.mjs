import assert from 'node:assert/strict'
import { readFile, readdir } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'
import path from 'node:path'
import { buildThemeConfig } from '../src/features/course/services/build-navigation.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
const directory = path.join(root, 'raw_materials/xu-ly-du-lieu/exam')
const read = async file => JSON.parse(await readFile(file, 'utf8'))
const draft = process.argv.includes('--draft')
const manifest = await read(path.join(directory, 'source-manifest.json'))
assert.equal(manifest.length, 18)
for (const item of manifest) {
  const bytes = await readFile(path.join(directory, 'source', item.file))
  assert.equal(bytes.length, item.bytes, `${item.file}: complete download`)
  assert.equal(createHash('sha256').update(bytes).digest('hex'), item.sha256, `${item.file}: source preserved`)
}
const expected = [60, 60, 72, 60, 72, 72, 80, 72]
const coverage = await read(path.join(directory, 'coverage.json'))
const rendered = await read(path.join(directory, 'render-coverage.json'))
const context = await read(path.join(directory, 'question-context.json'))
let total = 0, quiz = 0, essay = 0
const ids = new Set()
for (let number = 1; number <= 8; number++) {
  const lesson = String(number).padStart(2, '0')
  const bank = await read(path.join(directory, `banks/bai-${lesson}.json`))
  const compiled = await read(path.join(root, `src/content/courses/xu-ly-du-lieu/exam/bai-${lesson}.json`))
  assert(!('assumptionsHtml' in compiled), 'No general assumptions panel')
  assert.equal(bank.questions.length, expected[number - 1])
  assert.equal(compiled.questions.length, expected[number - 1])
  assert.deepEqual(coverage[number - 1].sourceQuestionIds, coverage[number - 1].importedQuestionIds)
  assert.deepEqual(rendered[number - 1].sourceQuestionIds, rendered[number - 1].renderedQuestionIds)
  assert.equal(createHash('sha256').update(JSON.stringify(compiled)).digest('hex'), rendered[number - 1].contentSha256, 'Compiled content agrees with render audit')
  assert.deepEqual(compiled.questions.map(q => q.id), bank.questions.map(q => q.id))
  // Check the original documents too, independently of the importer's saved
  // coverage report. Every source heading must have exactly one rendered ID.
  const sourceQuestions = await readFile(path.join(directory, 'source', bank.questions[0].source.questionFile), 'utf8')
  const sourceAnswers = await readFile(path.join(directory, 'source', bank.questions[0].source.answerFile), 'utf8')
  const headingIds = text => [...text.matchAll(/^#{2,5}\s+(B\d+-(?:MR|R)?\d+)\b/gm)].map(match => match[1])
  assert.deepEqual(headingIds(sourceQuestions), bank.questions.map(q => q.id), `${lesson}: all original question headings`)
  assert.deepEqual(headingIds(sourceAnswers), bank.questions.map(q => q.id), `${lesson}: all original answer headings`)
  let reviewed
  let detailedSolutions
  if (!draft) {
    const review = await read(path.join(directory, `reviews/bai-${lesson}.json`))
    assert.equal(review.items.length, expected[number - 1])
    reviewed = new Map(review.items.map(item => [item.id, item]))
    assert.equal(reviewed.size, expected[number - 1], 'No duplicate review IDs')
    const details = await read(path.join(directory, `detailed-solutions/bai-${lesson}.json`))
    const inputsHash = createHash('sha256').update(JSON.stringify({bank,review,detailed:details,questionContext:context})).digest('hex')
    assert.equal(rendered[number - 1].inputSha256, inputsHash, `${lesson}: rendered bank must be regenerated after any source, feedback, solution or context change`)
    detailedSolutions = new Map(details.items.map(item => [item.id, item.markdown]))
    const quizIds = bank.questions.filter(q => q.kind === 'quiz').map(q => q.id)
    assert.equal(detailedSolutions.size, details.items.length, 'No duplicate detailed solutions')
    assert.deepEqual([...detailedSolutions.keys()].sort(), quizIds.sort(), 'Every quiz has a complete solution')
  }
  for (const [index, question] of bank.questions.entries()) {
    assert(!ids.has(question.id), `Duplicate question: ${question.id}`)
    ids.add(question.id)
    const output = compiled.questions[index]
    assert(question.promptMarkdown.trim(), `${question.id}: prompt`)
    assert(question.answerMarkdown.trim(), `${question.id}: original answer`)
    assert(output.promptHtml.trim(), `${question.id}: rendered prompt`)
    assert(output.answerHtml.trim(), `${question.id}: rendered solution`)
    assert.equal(createHash('sha256').update(question.answerMarkdown).digest('hex'), question.source.answerSha256)
    assert(!/<script\b/i.test(output.promptHtml + output.answerHtml))
    const review = reviewed?.get(question.id)
    if (!draft) {
      assert(review, `${question.id}: reviewed`)
      assert(review.verification?.method?.trim(), `${question.id}: verification method`)
      assert(review.verification?.evidence?.trim(), `${question.id}: verification evidence`)
      assert.equal(output.correctKey, review.correctKey, `${question.id}: rendered key matches independent review`)
    }
    if (question.kind === 'quiz') {
      quiz++
      assert.deepEqual(question.options.map(o => o.key), ['A','B','C','D'])
      assert.deepEqual(output.options.map(o => o.key), ['A','B','C','D'])
      assert(['A','B','C','D'].includes(output.correctKey))
      if (!draft) {
        const solution = detailedSolutions.get(question.id)
        assert(!/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(solution), `${question.id}: no corrupted escape/control characters`)
        const conclusion = solution.match(/Phương án\s+([A-D])\s+(?:là\s+)?(?:đáp án\s+)?đúng/)
        assert(conclusion, `${question.id}: explicit answer conclusion`)
        assert.equal(conclusion[1], output.correctKey, `${question.id}: detailed conclusion agrees with verified key`)
        if (output.correctKey !== question.correctKey) {
          const checks = review.verification.independentChecks
          assert(Array.isArray(checks) && checks.length >= 2, `${question.id}: changed key requires multiple independent checks`)
          assert(new Set(checks.map(check => check.method)).size >= 2, `${question.id}: distinct verification methods`)
          assert(checks.every(check => check.result && check.correctKey === output.correctKey), `${question.id}: independent checks must agree`)
        }
        const sections = [...solution.matchAll(/^### Phương án ([A-D])\s*\n([\s\S]*?)(?=^### |$(?![\s\S]))/gm)]
        assert.deepEqual(sections.map(section => section[1]), ['A','B','C','D'], `${question.id}: separate detailed A–D reasoning`)
        for (const key of ['A','B','C','D']) assert(new RegExp(`<h3\\b[^>]*>\\s*Phương án ${key}\\s*</h3>`).test(output.answerHtml), `${question.id}/${key}: expanded explanation rendered as an actual section`)
        for (const section of sections) assert(section[2].trim().split(/\s+/).length >= 18, `${question.id}/${section[1]}: detailed reasoning rather than a label`)
        for (const option of output.options) {
          const brief = review.optionExplanations?.[option.key]?.trim()
          assert(brief, `${question.id}/${option.key}: explanation`)
          assert.equal((brief.match(/`/g) || []).length % 2, 0, `${question.id}/${option.key}: balanced inline-code delimiters`)
          assert(option.explanationHtml.trim(), `${question.id}/${option.key}: visible explanation`)
        }
      }
    } else {
      essay++
      assert.equal(question.kind, 'essay')
      assert.equal(output.correctKey, null)
      assert.equal(output.options.length, 0)
    }
    total++
  }
  const source = await readFile(path.join(root, `docs/xu-ly-du-lieu/on-thi/bai-${lesson}.md`), 'utf8')
  assert(source.includes('<ExamPractice :bank="bank" />'))
}
assert.equal(total, 548)
assert.equal(quiz, 364)
assert.equal(essay, 184)
assert.equal([...ids].filter(id => /^B7-R\d+$/.test(id)).length, 20)
assert.equal([...ids].filter(id => /-MR\d+$/.test(id)).length, 48)
for (const [id, text] of Object.entries(context)) { assert(ids.has(id)); assert(text.trim()) }
const navigation = buildThemeConfig({courseCatalog:[{id:'xu-ly-du-lieu',name:'Dữ liệu',lessons:[]}],wikiGroups:[],concepts:{}})
assert.deepEqual(navigation.sidebar['/xu-ly-du-lieu/'][0].items.map(item=>item.text), ['Tổng quan môn học','Bài tập ôn luyện','Ôn thi','Bài tập lớn'])
const ordinary = buildThemeConfig({courseCatalog:[{id:'other',name:'Khác',lessons:[]}],wikiGroups:[],concepts:{}})
assert(!ordinary.sidebar['/other/'][0].items.some(item=>item.text==='Ôn thi'))
console.log(`PASS ${total} questions: ${quiz} quiz, ${essay} essays; source coverage, IDs, choices and navigation${draft ? ' (review pending)' : ', reviewed-key consistency and explanation structure'}. This structural check does not prove every answer.`)
