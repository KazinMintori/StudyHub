import test from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { cleanQuestionFeedback, cleanQuizFeedback } from '../../src/features/philosophy/services/quiz-feedback.mjs'

const banks = [1, 2, 3].map(chapter => JSON.parse(readFileSync(new URL(`../../src/content/courses/triet-hoc-mac-lenin/exam/chuong-${chapter}.json`, import.meta.url), 'utf8')))
const questions = banks.flatMap(bank => bank.questions)
const feedback = question => [question.explanation, ...(question.takeaway ? [question.takeaway] : []), ...question.distractors.map(item => item.explanation)]
const sourceNarration = /nguồn(?!\s+(?:gốc|lực|lý luận|tri thức)\b)|giáo trình|bản nguồn|tham chiếu(?:\s*:| tài liệu)|(?:trang|PDF|tr\.)\s*\d|đối chiếu\s*:|kiến thức\s*:|dữ kiện(?:\/cách hiểu)? quyết định|(?:vì vậy|do đó)\s+chọn\s+[ABCD](?=$|[\s.:])|→\s*chọn/iu

test('authoring labels become knowledge and a substantive distinction', () => {
  const result = cleanQuizFeedback('Nguồn: Vật chất tồn tại khách quan → đối chiếu: Cảm giác phản ánh hiện thực, không tạo ra hiện thực. → chọn D.')
  assert.equal(result, 'Vật chất tồn tại khách quan. Cảm giác phản ánh hiện thực, không tạo ra hiện thực.')
  assert.equal(cleanQuizFeedback('Dữ kiện/cách hiểu quyết định: Biết một phần chưa phải biết hết. → kiến thức: Nhận thức là quá trình phát triển → chọn C.'), 'Nhận thức là quá trình phát triển. Biết một phần chưa phải biết hết.')
  assert.equal(cleanQuizFeedback('Nguồn nêu vật chất tồn tại khách quan.'), 'Vật chất tồn tại khách quan.')
})

test('selection boilerplate and page citations disappear without deleting philosophical terms', () => {
  const result = cleanQuizFeedback('Nguồn phân biệt hai quan hệ; nguồn gốc ý thức gắn với bộ óc. Vì vậy chọn A: Nguồn gốc ý thức có cơ sở tự nhiên và xã hội.')
  assert.match(result, /Nguồn gốc ý thức có cơ sở tự nhiên và xã hội/)
  assert.match(result, /Nguồn gốc ý thức gắn với bộ óc/)
  assert.doesNotMatch(result, sourceNarration)
  assert.equal(cleanQuizFeedback('Nguồn lực vật chất cần được sử dụng phù hợp. Nguồn gốc vận động nằm trong hiện thực.'), 'Nguồn lực vật chất cần được sử dụng phù hợp. Nguồn gốc vận động nằm trong hiện thực.')
  assert.equal(cleanQuizFeedback('Nguồn: **Triết học có tính hệ thống** → đối chiếu: Đúng nội dung trang 5. → chọn A.'), 'Triết học có tính hệ thống.')
})

test('all 1250 questions retain their identity, exact question text, options and scoring', () => {
  assert.equal(questions.length, 1250)
  for (const question of questions) {
    const snapshot = structuredClone(question)
    const result = cleanQuestionFeedback(question)
    assert.notEqual(result, question)
    assert.deepEqual(question, snapshot, `${question.id}: canonical object must not be mutated`)
    assert.equal(result.id, question.id)
    assert.equal(result.prompt, question.prompt)
    assert.deepEqual(result.options, question.options)
    assert.equal(result.correctKey, question.correctKey)
    const withoutFeedback = value => Object.fromEntries(Object.entries(value).filter(([key]) => !['explanation', 'distractors', 'takeaway'].includes(key)))
    assert.deepEqual(withoutFeedback(result), withoutFeedback(question), question.id)
    assert.deepEqual(result.distractors.map(item => item.key), question.distractors.map(item => item.key), question.id)
  }
})

test('every explanation, takeaway and three distractor reasons remain substantive student prose', () => {
  for (const question of questions) {
    const result = cleanQuestionFeedback(question)
    assert.equal(result.distractors.length, 3, question.id)
    assert.equal(new Set(result.distractors.map(item => item.key)).size, 3, question.id)
    assert.ok(result.distractors.every(item => item.key !== result.correctKey), question.id)
    for (const value of feedback(result)) {
      assert.ok(value.length >= 8, `${question.id}: feedback cannot disappear`)
      assert.match(value, /\p{L}/u)
      assert.doesNotMatch(value, sourceNarration, `${question.id}: ${value}`)
      assert.doesNotMatch(value, /^(?:Đáp án|Chọn|Phương án đúng)\s*[ABCD][.!]?$/iu)
      assert.doesNotMatch(value, /\*\*|```|\[[^\]]+\]\([^)]+\)|→|\uE000|\[object Object\]|undefined|\s+[,.]|\.{2,}|:\s*\p{Ll}/u, `${question.id}: ${value}`)
    }
    assert.deepEqual(cleanQuestionFeedback(result), result, `${question.id}: repeated rendering must not damage prose`)
  }
})

test('reviewed purely editorial feedback explains the actual concept', () => {
  const byId = id => cleanQuestionFeedback(questions.find(question => question.id === id))
  assert.match(byId('CH010').explanation, /bản chất.*nhân sinh quan/u)
  assert.match(byId('CH001').explanation, /phương Đông và phương Tây/u)
  assert.doesNotMatch(byId('CH001').explanation, /khớp/u)
  assert.match(byId('Q022').explanation, /quan hệ vật chất.*duy vật lịch sử/u)
  assert.match(byId('Q339').explanation, /cơ sở nội tại.*giữ lại và cải tạo/u)
  assert.match(byId('Q415').takeaway, /phản ánh đầy đủ.*biết trọn vẹn/u)
  assert.match(byId('CIII-010').explanation, /không có nghĩa.*chưa có quy tắc/u)
  assert.match(byId('CIII-254').explanation, /thị trường.*liên kết kinh tế/u)
  assert.equal(cleanQuizFeedback(null), '')
  assert.equal(cleanQuestionFeedback(null), null)
})
