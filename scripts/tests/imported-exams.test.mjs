import test from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { createHash } from 'node:crypto'
import { assertCodePreserved, htmlCodeText, renderedCodeLiterals } from '../build/exam-code-integrity.mjs'
import { acceptedQuizKeys, createExamSessionState, recordQuizAnswer, recordQuizReview, reconcileStoredAnswers, calculateSessionStats } from '../../src/features/exam/services/exam-session.mjs'

const load = file => JSON.parse(readFileSync(file, 'utf8'))
const source = load('raw_materials/xu-ly-du-lieu/exam-papers/source.json')
const catalog = load('src/content/courses/xu-ly-du-lieu/de-thi/catalog.json')
const coverage = load('raw_materials/xu-ly-du-lieu/exam-papers/render-coverage.json')
const banks = catalog.map(exam => load(`src/content/courses/xu-ly-du-lieu/de-thi/${exam.id}.json`))
const clean = text => htmlCodeText(text).replace(/\s+/g, ' ').trim()
const sha = object => createHash('sha256').update(JSON.stringify(object)).digest('hex')

test('Five papers contain every source question, choice and unchanged code block', () => {
  assert.deepEqual(banks.map(bank => bank.code), ['047', '045', '046', '030', '001'])
  assert.deepEqual(banks.map(bank => bank.title), ['Đề 1', 'Đề 2', 'Đề 3', 'Đề 4', 'Đề 5'])
  let questions = 0, choices = 0, blocks = 0
  for (const [i, bank] of banks.entries()) {
    assert.equal(bank.questions.length, 26)
    assert.equal(bank.questions.filter(q => q.kind === 'quiz').length, 20)
    assert.equal(bank.questions.filter(q => q.kind === 'essay').length, 6)
    assert.equal(coverage[i].sourceSha256, sha(source.exams[i]))
    assert.equal(coverage[i].renderedSha256, sha(bank))
    for (const [j, q] of bank.questions.entries()) {
      const original = source.exams[i].questions[j]
      assert.equal(q.sourceNumber, j + 1)
      assert.equal(q.id, original.id)
      assert.ok(q.answerHtml.includes('Đáp án') && clean(q.answerHtml).length > 200, `${q.id}: detailed solution`)
      assert.ok(!/ZXQKEEP|data-mjx-error|<merror\b/.test(q.answerHtml), q.id)
      for (const svg of q.answerHtml.matchAll(/<svg[^>]*width="([0-9.]+)ex"/g)) {
        assert.ok(Number(svg[1]) <= 30, `${q.id}: equation fits a narrow solution panel`)
      }
      const codes = original.items.filter(item => item.kind === 'code').map(item => item.text.replace(/\r\n?/g, '\n').replace(/\n$/, ''))
      assert.deepEqual(renderedCodeLiterals(q.promptHtml).blocks, codes, q.id)
      for (const prose of original.items.filter(item => item.kind === 'prose')) {
        assert.ok(clean(q.promptHtml).includes(prose.text.replace(/\s+/g, ' ').trim()), `${q.id}: verbatim prose`)
      }
      const originals = original.items.filter(item => item.kind === 'choice')
      assert.equal(q.options.length, originals.length)
      for (const [k, option] of q.options.entries()) {
        assert.equal(option.key, originals[k].label)
        assert.equal(clean(option.html), originals[k].text.replace(/\s+/g, ' ').trim(), `${q.id}/${option.key}`)
      }
      assertCodePreserved(original.solutionMarkdown, q.answerHtml, `${q.id}: solution`)
      questions++; choices += originals.length; blocks += codes.length
    }
  }
  assert.equal(questions, 130)
  assert.equal(choices, 400)
  assert.equal(blocks, 94)
})

test('Invalid source questions are reviewable without an invented grade', () => {
  const bank = banks[3]
  assert.deepEqual(bank.questions.filter(q => q.grading === 'manual').map(q => q.sourceNumber), [4,5,7,8,9,10,11,12,18])
  const session = createExamSessionState()
  const q = bank.questions[3]
  assert.deepEqual(acceptedQuizKeys(q), [])
  assert.equal(recordQuizAnswer(session, q, 'A'), null)
  recordQuizReview(session, q)
  assert.equal(session.answers[q.id].isCorrect, null)
  assert.equal(calculateSessionStats(session, bank.questions).wrongCount, 0)
  assert.equal(reconcileStoredAnswers(bank.questions, session.answers)[q.id].isCorrect, null)
  recordQuizAnswer(session, bank.questions[12], 'C')
  recordQuizAnswer(session, bank.questions[16], 'C')
  const stats = calculateSessionStats(session, bank.questions)
  assert.equal(stats.correctCount, 2)
  assert.equal(stats.wrongCount, 0)
  assert.equal(stats.scorePercentage, Math.round(2 / 11 * 100))
  assert.equal(reconcileStoredAnswers(bank.questions, session.answers)[bank.questions[12].id].isCorrect, true)
})

test('Reviewed source variants and independent page storage keys stay explicit', () => {
  assert.equal(banks[1].questions[19].correctKey, 'A')
  assert.equal(banks[2].questions[17].correctKey, 'C')
  assert.ok(renderedCodeLiterals(banks[2].questions[23].promptHtml).blocks.some(text => text.includes('r"\\b(\\d+)m2\\b"')))
  assert.ok(banks[2].questions[7].reviewNoteHtml.includes('Copy-on-Write'))
  const keys = banks.map((bank, i) => {
    const page = readFileSync(`docs/xu-ly-du-lieu/de-thi/de-${i+1}.md`, 'utf8')
    assert.ok(page.includes('ExamPractice'))
    return page.match(/session-key="([^"]+)"/)[1]
  })
  assert.equal(new Set(keys).size, 5)
  const pdf = readFileSync('docs/public/materials/xu-ly-du-lieu/de-thi/5-de-130-cau-loi-giai.pdf')
  assert.equal(pdf.subarray(0,5).toString(), '%PDF-')
  assert.ok(pdf.length > 500000)
})
