import assert from 'node:assert/strict'
import {readFile} from 'node:fs/promises'
import {fileURLToPath} from 'node:url'
import path from 'node:path'
import {createHash} from 'node:crypto'
import {assertCodePreserved} from './build/exam-code-integrity.mjs'

const hash=value=>createHash('sha256').update(value).digest('hex')
export async function verifyDataExamAdditions(root=fileURLToPath(new URL('../',import.meta.url))) {
  const base=path.join(root,'raw_materials/xu-ly-du-lieu/exam')
  const read=async file=>JSON.parse(await readFile(file,'utf8'))
  const manifest=await read(path.join(base,'additions-20261106.json'))
  const renderAudit=await read(path.join(base,'additions-render-coverage.json'))
  const catalog=await read(path.join(root,'src/content/courses/xu-ly-du-lieu/exam/catalog.json'))
  const ids=new Set()
  for(const source of manifest.lessons) {
    const bank=await read(path.join(base,`banks/bai-${source.lesson}.json`))
    const review=await read(path.join(base,`reviews/bai-${source.lesson}.json`))
    const compiled=await read(path.join(root,`src/content/courses/xu-ly-du-lieu/exam/bai-${source.lesson}.json`))
    const audit=renderAudit.find(item=>item.lesson===source.lesson)
    assert(!('assumptionsHtml'in compiled))
    assert.equal(bank.questions.length,90)
    assert.equal(review.items.length,90)
    assert.deepEqual(bank.questions.map(q=>q.id),source.sourceQuestionIds)
    assert.deepEqual(compiled.questions.map(q=>q.id),source.sourceQuestionIds)
    assert.deepEqual(audit.renderedQuestionIds,source.sourceQuestionIds)
    assert.equal(audit.inputSha256,hash(JSON.stringify({bank,review})))
    assert.equal(audit.contentSha256,hash(JSON.stringify(compiled)))
    for(const file of source.files) {
      const bytes=await readFile(path.join(base,'source',file.file))
      assert.equal(bytes.length,file.bytes)
      assert.equal(hash(bytes),file.sha256)
    }
    for(const[qIndex,question]of bank.questions.entries()) {
      const output=compiled.questions[qIndex],item=review.items.find(x=>x.id===question.id)
      assert(!ids.has(question.id));ids.add(question.id)
      assert(['confirmed','corrected'].includes(item.verdict),`${question.id}: unresolved`)
      assertCodePreserved(question.promptMarkdown,output.promptHtml,question.id)
      assert.equal(output.options.length,question.kind==='quiz'?4:0)
      assert(!/Hướng dẫn chấm|Chấm điểm|Kỹ năng:|Mức dự kiến|Thời gian.*giây/.test(output.answerHtml),question.id)
      assert(!/[\x00-\x08\x0b\x0c\x0e-\x1f\ufffd]/.test(output.promptHtml+output.answerHtml),question.id)
      if(question.kind==='quiz') {
        assert.equal(output.correctKey,item.correctKey||question.correctKey)
        for(const[index,option]of output.options.entries()) {
          assert.equal(option.key,'ABCD'[index])
          assertCodePreserved(question.options[index].markdown,option.html,`${question.id}/${option.key}`)
          assert(output.answerHtml.includes(`Phương án ${option.key}`),question.id)
          assert(item.optionExplanations[option.key].length>=45,`${question.id}/${option.key}: substantive feedback`)
        }
      } else {
        assert.equal(output.correctKey,null)
        assertCodePreserved(question.answerMarkdown,output.answerHtml,`${question.id}: primary answer retained`)
        assert(item.supplementMarkdown?.length>=100,`${question.id}: detailed explanation`)
      }
    }
    const entry=catalog.find(x=>x.lesson===source.lesson)
    assert.deepEqual([entry.total,entry.quiz,entry.essay],[90,60,30])
    assert((await readFile(path.join(root,`docs/xu-ly-du-lieu/on-thi/bai-${source.lesson}.md`),'utf8')).includes('<ExamPractice :bank="bank" />'))
  }
  assert.equal(ids.size,180)
  const total=catalog.reduce((sum,x)=>sum+x.total,0)
  assert.equal(total,728)
  return {questions:ids.size,quiz:120,essay:60,total}
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))console.log('PASS',await verifyDataExamAdditions())
