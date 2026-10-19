import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile, access } from 'node:fs/promises'
import { chapterPracticeTests, createPracticeBank } from '../../src/features/philosophy/services/practice-tests.mjs'
const readJson = async file => JSON.parse(await readFile(file,'utf8'))

test('chapters divide into balanced tests of at most 60 without a short leftover', () => {
  assert.deepEqual(chapterPracticeTests({id:'chuong-1',chapter:1,count:360}).map(test=>test.count),[60,60,60,60,60,60])
  assert.deepEqual(chapterPracticeTests({id:'chuong-2',chapter:2,count:440}).map(test=>test.count),[55,55,55,55,55,55,55,55])
  assert.deepEqual(chapterPracticeTests({id:'chuong-3',chapter:3,count:450}).map(test=>test.count),[57,57,56,56,56,56,56,56])
  assert.deepEqual(chapterPracticeTests({count:0}),[])
})

test('every original question occurs exactly once in its chapter tests', async () => {
  const ids=[]
  for (const chapter of [1,2,3]) {
    const parent=await readJson(`src/content/courses/triet-hoc-mac-lenin/exam/chuong-${chapter}.json`)
    const covered=[]
    for (const spec of chapterPracticeTests(parent)) {
      const bank=createPracticeBank(parent,spec.testNumber)
      const actual=await readJson(`src/content/courses/triet-hoc-mac-lenin/exam/practice/${spec.id}.json`)
      assert.equal(actual.id,spec.id)
      assert.equal(actual.parentBankId,parent.id)
      assert.equal(actual.questions.length,spec.count)
      for(const [index,question] of actual.questions.entries()) {
        const original=bank.questions[index]
        assert.equal(question.id,original.id)
        assert.deepEqual(question.options,original.options)
        assert.equal(question.prompt,original.prompt)
        assert.equal(question.correctKey,original.correctKey)
        assert(!Object.hasOwn(question,'sourceReference'))
      }
      covered.push(...actual.questions.map(question=>question.id))
      ids.push(actual.id)
      await access(`docs${spec.path}.md`)
    }
    assert.deepEqual(covered,parent.questions.map(question=>question.id))
    assert.equal(new Set(covered).size,parent.questions.length)
  }
  assert.equal(ids.length,22)
  assert.equal(new Set(ids).size,22)
})
