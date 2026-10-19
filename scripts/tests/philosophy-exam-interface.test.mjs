import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { toExamBank } from '../../src/features/philosophy/services/exam-bank.mjs'
import { cleanQuestionFeedback } from '../../src/features/philosophy/services/quiz-feedback.mjs'

test('The shared exam adapter retains every prompt, option and individual explanation', async () => {
  for (const chapter of [1, 2]) {
    const bank = JSON.parse(await readFile(`src/content/courses/triet-hoc-mac-lenin/exam/chuong-${chapter}.json`, 'utf8'))
    bank.questions = bank.questions.map(cleanQuestionFeedback)
    const adapted = toExamBank(bank)
    assert.equal(adapted.questions.length, bank.questions.length)
    for (const [index, question] of bank.questions.entries()) {
      const result = adapted.questions[index]
      assert.equal(result.id, question.id)
      assert.equal(result.correctKey, question.correctKey)
      assert.equal(result.options.length, 4)
      for (const option of result.options) assert(option.explanationHtml, `${question.id}-${option.key} must retain its explanation`)
    }
  }
})

test('Plain question text cannot inject markup into the shared renderer', () => {
  const bank = toExamBank({ id: 'test', questions: [{ id: 'q', prompt: '<img src=x onerror=alert(1)> & "text"', correctKey: 'A', explanation: '<script>bad()</script>', options: [{ key: 'A', text: '<b>literal</b>' }] }] })
  assert(bank.questions[0].promptHtml.includes('&lt;img'))
  assert(!bank.questions[0].promptHtml.includes('<img'))
  assert.equal(bank.questions[0].options[0].html, '<p>&lt;b&gt;literal&lt;/b&gt;</p>')
  assert(!bank.questions[0].options[0].explanationHtml.includes('<script>'))
})

test('All philosophy tests use the same page layout as Data Processing', async () => {
  for (const [chapter,count] of [[1,6],[2,8]]) for (let number=1; number<=count; number++) {
    const page=await readFile(`docs/triet-hoc-mac-lenin/on-thi/chuong-${chapter}/bai-${number}.md`, 'utf8')
    assert.match(page, /layout: page/)
    assert.match(page, /sidebar: false/)
    assert.doesNotMatch(page, /PhilosophyPracticeLinks/)
  }
  for (const file of ['PhilosophyHeader.vue','PhilosophyCourse.vue']) {
    const source=await readFile(`src/features/philosophy/components/${file}`,'utf8')
    assert.doesNotMatch(source, /PhilosophyNav/)
  }
})
