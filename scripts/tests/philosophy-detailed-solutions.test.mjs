import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { detailedSolution } from '../../src/features/philosophy/services/detailed-solutions.mjs'
import { toExamBank } from '../../src/features/philosophy/services/exam-bank.mjs'
import { cleanQuestionFeedback } from '../../src/features/philosophy/services/quiz-feedback.mjs'

const plain = html => html.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim()

test('All 1250 questions have an authored explanation beyond the short choice feedback', async () => {
  let count = 0
  for (const chapter of [1, 2, 3]) {
    const original = JSON.parse(await readFile(`src/content/courses/triet-hoc-mac-lenin/exam/chuong-${chapter}.json`, 'utf8'))
    const bank = { ...original, questions: original.questions.map(cleanQuestionFeedback) }
    const rendered = toExamBank(bank)
    for (const [index, question] of bank.questions.entries()) {
      const solution = detailedSolution(question.id)
      assert(solution, question.id)
      assert(solution.contexts.length > 0, question.id)
      for (const context of solution.contexts) {
        assert(context?.title && context.paragraphs?.length >= 2, `${question.id} needs a coherent conceptual explanation`)
        assert(context.paragraphs.join(' ').split(/\s+/).length >= 60, `${question.id} has only a terse answer`)
      }
      const full = plain(rendered.questions[index].answerHtml)
      const choices = rendered.questions[index].options.map(option=>plain(option.explanationHtml))
      assert(full.length > Math.max(...choices.map(text=>text.length)) + 150, `${question.id}: Expanded solution must explain more than an option`)
      assert(full.split(/\s+/).length <= 380, `${question.id}: Keep the expanded answer focused`)
      assert(!/Nguồn\s*:|theo (?:sách|giáo trình)|cần đọc kỹ đề|chọn phương án dài nhất/i.test(full), question.id)
      assert(full.includes(`Đáp án ${question.correctKey}.`), question.id)
      for (const distractor of question.distractors) assert(!full.includes(distractor.explanation), `${question.id}: Do not repeat the feedback already shown below each option`)
      count++
    }
  }
  assert.equal(count, 1250)
})

test('Solution assignments contain no duplicate IDs, missing contexts or orphaned question references', async () => {
  const allIds = new Set()
  const specs = [['chuong-1',360],['chuong-2a',220],['chuong-2b',220],['chuong-3',450]]
  for (const [name,count] of specs) {
    const library = JSON.parse(await readFile(`src/content/courses/triet-hoc-mac-lenin/exam/solutions/${name}.json`,'utf8'))
    assert.equal(Object.keys(library.questions).length, count)
    const used = new Set()
    for (const [id,assignment] of Object.entries(library.questions)) {
      assert(!allIds.has(id), id)
      allIds.add(id)
      for (const context of assignment.contextIds) {
        assert(Object.hasOwn(library.contexts,context), `${id}: ${context}`)
        used.add(context)
      }
    }
    assert.equal(used.size,Object.keys(library.contexts).length, `${name}: Remove unused material`)
  }
  assert.equal(allIds.size,1250)
  assert.equal(detailedSolution('missing'),null)
})
