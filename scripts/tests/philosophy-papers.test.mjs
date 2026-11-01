import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { createPaperSession, answerPaper, restorePaperSession, paperResult, loadPaperSession, savePaperSession } from '../../src/features/philosophy/services/paper-session.mjs'
const bank={id:'test',questions:[{id:'q1',correctKey:'A'},{id:'q2',correctKey:'B'}]}
test('Mock papers defer grading until submission, allow answer changes and refuse changes afterward',()=>{
 const blank=createPaperSession(bank)
 let session=answerPaper(bank,blank,'q1','B')
 assert.deepEqual(blank.answers,{})
 session=answerPaper(bank,session,'q1','A')
 assert.deepEqual(paperResult(bank,session),{total:2,answered:1,correct:1,wrong:0,unanswered:1,score:5})
 session={...session,submitted:true}
 assert.equal(answerPaper(bank,session,'q2','B'),session)
 assert.equal(answerPaper(bank,blank,'unknown','A'),blank)
})
test('Paper persistence rejects corrupt state, rescoring uses current keys, and storage errors are safe',()=>{
 assert.deepEqual(restorePaperSession(bank,'{bad'),createPaperSession(bank))
 assert.deepEqual(restorePaperSession(bank,{version:1,bankId:'other',answers:{q1:'A'}}),createPaperSession(bank))
 const restored=restorePaperSession(bank,{version:1,bankId:'test',answers:{q1:'B',q2:'Z',unknown:'A'},index:99,submitted:true})
 assert.equal(restored.index,1);assert.deepEqual(restored.answers,{q1:'B'});assert.equal(paperResult(bank,restored).score,0)
 const broken={getItem(){throw Error('blocked')},setItem(){throw Error('quota')}}
 assert.deepEqual(loadPaperSession(bank,broken),createPaperSession(bank));assert.equal(savePaperSession(bank,restored,broken),false)
})
test('21 mixed papers cover all 1250 original IDs exactly once and every paper includes all chapters',async()=>{
 const catalog=JSON.parse(await readFile('src/content/courses/triet-hoc-mac-lenin/exam/papers/catalog.json','utf8'))
 assert.equal(catalog.papers.length,21)
 const ids=[]
 for(const paper of catalog.papers){
  const bank=JSON.parse(await readFile(`src/content/courses/triet-hoc-mac-lenin/exam/papers/${paper.id}.json`,'utf8'))
  assert(bank.questions.length>=59&&bank.questions.length<=60)
  assert.equal(bank.kind,'generated')
  assert(paper.chapterCounts.every(count=>count>0))
  ids.push(...bank.questions.map(question=>question.id))
 }
 assert.equal(ids.length,1250);assert.equal(new Set(ids).size,1250)
})
