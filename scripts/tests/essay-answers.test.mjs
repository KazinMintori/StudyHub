import test from 'node:test'
import assert from 'node:assert/strict'
import {readFile} from 'node:fs/promises'
import {loadEssayAnswers,renderEssayAnswer} from '../build/essay-answers.mjs'
import {createExamMarkdownRenderer} from '../build/exam-markdown.mjs'
import {assertCodePreserved} from '../build/exam-code-integrity.mjs'
import {legacyExplanation,composeLegacySupplement,canonicalPythonBlocks} from '../build/essay-supplements.mjs'

const source=await loadEssayAnswers(process.cwd())
const render=await createExamMarkdownRenderer(process.cwd())
test('All 184 essays keep the current Drive answer first and retain a detailed explanation without grading guides',async()=>{
  let count=0
  for(let i=1;i<=8;i++){
    const n=String(i).padStart(2,'0')
    const bank=JSON.parse(await readFile(`src/content/courses/xu-ly-du-lieu/exam/bai-${n}.json`,'utf8'))
    const ids=bank.questions.filter(q=>q.kind==='essay').map(q=>q.id)
    assert.deepEqual(source.lessons.get(n).items.map(q=>q.id),ids)
    for(const q of bank.questions.filter(q=>q.kind==='essay')){
      const entry=source.questions.get(q.id)
      assert.equal(q.answerHtml,renderEssayAnswer(entry,render),q.id)
      assert(entry.supplementMarkdown?.trim(),`${q.id}: detailed explanation retained`)
      assert(q.answerHtml.startsWith(render(entry.markdown,true)),q.id)
      assertCodePreserved(entry.markdown+'\n\n'+entry.supplementMarkdown,q.answerHtml,q.id)
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
test('Legacy explanations retain code and reasoning but stop before either grading format',()=>{
  for(const heading of ['**Hướng dẫn chấm — 2 điểm**','**Ý bắt buộc và hướng dẫn chấm — 2 điểm**','**Chấm 5 điểm:**']){
    const explanation='Vì khóa tồn tại, giá trị được giữ nguyên.\n\n```python\nx = "a;b"\n```'
    assert.equal(legacyExplanation(explanation+'\n\n'+heading+'\n\n| Ý cần đạt | Điểm |\n|---|---|\n| Đúng | 2 |'),explanation)
  }
  assert(legacyExplanation('```text\n**Chấm 5 điểm:**\n```\n\nPhân tích.').includes('**Chấm 5 điểm:**'))
})
test('An identical code block is not repeated, while its remaining explanation is retained',()=>{
  const main='```python\nx = 1\n```'
  const old='b)\n\n```python\nx = 1\n```\n\nPhép gán tạo liên kết từ tên x tới số nguyên.'
  assert.equal(composeLegacySupplement(main,old),'Phép gán tạo liên kết từ tên x tới số nguyên.')
  const code='```python\nx = 1\n\nprint(x)\n\nx = 2\n```'
  assert.equal(composeLegacySupplement('print(x)',code),code)
  const primary="```python\np = r'\\b[0-9]+\\b'\n```"
  const previous='```python\np=r"\\b[0-9]+\\b"\n```\n\nRanh giới từ giới hạn vị trí khớp.'
  const keys=canonicalPythonBlocks([primary,previous])
  assert.equal(composeLegacySupplement(primary,previous,'',keys),'Ranh giới từ giới hạn vị trí khớp.')
})
