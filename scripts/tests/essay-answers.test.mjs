import test from 'node:test'
import assert from 'node:assert/strict'
import {readFile} from 'node:fs/promises'
import {loadEssayAnswers,renderEssayAnswer} from '../build/essay-answers.mjs'
import {createExamMarkdownRenderer} from '../build/exam-markdown.mjs'
import {assertCodePreserved} from '../build/exam-code-integrity.mjs'

const source=await loadEssayAnswers(process.cwd())
const render=await createExamMarkdownRenderer(process.cwd())
test('All 184 essays use the complete new Drive answer and have no grading guide or old appendix',async()=>{
  let count=0
  for(let i=1;i<=8;i++){
    const n=String(i).padStart(2,'0')
    const bank=JSON.parse(await readFile(`src/content/courses/xu-ly-du-lieu/exam/bai-${n}.json`,'utf8'))
    const ids=bank.questions.filter(q=>q.kind==='essay').map(q=>q.id)
    assert.deepEqual(source.lessons.get(n).items.map(q=>q.id),ids)
    for(const q of bank.questions.filter(q=>q.kind==='essay')){
      const entry=source.questions.get(q.id)
      assert.equal(q.answerHtml,renderEssayAnswer(entry,render),q.id)
      assertCodePreserved(entry.markdown,q.answerHtml,q.id)
      assert(!/hướng dẫn chấm|ý cần đạt|điểm tối đa|rubric|kiến thức bổ sung|giải thích chuyên sâu/i.test(q.answerHtml),q.id)
      count++
    }
  }
  assert.equal(count,184)
})
test('An optional explanation follows the primary answer as ordinary paragraphs',()=>{
  const entry={markdown:'Kết quả là `0`.',supplementMarkdown:'Giá trị 0 vẫn được giữ vì phép lọc kiểm tra `is not None`.'}
  const result=renderEssayAnswer(entry,render)
  assert(result.startsWith(render(entry.markdown,true)))
  assert(result.endsWith(render(entry.supplementMarkdown,true)))
  assert(!result.includes('<h'))
})
test('The common renderer preserves HTML entities, regex syntax and semicolons in code',()=>{
  const markdown='Kết quả: `[g for g in gam if g >= 0]`.\n\n```python\nx = "a;b"\np = r"\\b[0-9]+\\b"\n```'
  assertCodePreserved(markdown,render(markdown,true),'literal regression')
})
