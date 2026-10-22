import test from 'node:test'
import assert from 'node:assert/strict'
import { matchesWikiQuery, conceptUsageIndex, conceptSummary } from './wiki-discovery.mjs'
test('Vietnamese search supports unaccented words and requires every word', () => {
  const term = { name: 'Xác suất có điều kiện', aliases: ['conditional probability'], definition: 'Cập nhật theo bằng chứng.' }
  assert(matchesWikiQuery(term, 'xac suat dieu kien'))
  assert(matchesWikiQuery(term, 'conditional'))
  assert(!matchesWikiQuery(term, 'xac suat ma tran'))
})
test('A concept is counted once per lecture even when listed in both roles', () => {
  const index = conceptUsageIndex([{ lessons: [{ prerequisites: ['a'], supportingConcepts: ['a', 'b'] }, { prerequisites: ['a'] }] }])
  assert.equal(index.get('a'), 2)
  assert.equal(index.get('b'), 1)
})
test('Discovery summaries do not expose multiline display notation', () => {
  assert.equal(conceptSummary('Một định nghĩa.\n\n$$x=y$$'), 'Một định nghĩa.')
  assert(conceptSummary('Một từ '.repeat(60)).length <= 220)
})
test('A summary never cuts a TeX segment in half', () => {
  const summary = conceptSummary('Một từ '.repeat(30) + '$x_1+x_2+x_3+x_4+x_5+x_6+x_7+x_8+x_9+x_{10}$')
  assert.equal((summary.match(/\$/g) || []).length % 2, 0)
})
