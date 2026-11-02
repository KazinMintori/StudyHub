import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile, access } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { fillQuestions, gradeFillQuestion } from '../../src/features/philosophy/services/fill-session.mjs'
test('All three chapters contain 40 complete fill questions with accepted terms, explanations and working routes',async()=>{
 const seen=new Set()
 for(const chapter of [1,2,3]){
  const bank=JSON.parse(await readFile(`src/content/courses/triet-hoc-mac-lenin/exam/fill/chuong-${chapter}.json`,'utf8'))
  assert.equal(fillQuestions(bank).length,40)
  for(const question of bank.questions){
   assert(!seen.has(question.id));seen.add(question.id)
   assert.equal(question.parts.length,question.blanks.length+1)
   assert(question.explanation.split(/\s+/).length>=30)
   assert(gradeFillQuestion(question,question.blanks.map(blank=>blank.answer)).correct)
   assert(!gradeFillQuestion(question,question.blanks.map(()=> 'không đúng')).correct)
   for(const [index,blank] of question.blanks.entries()) for(const alias of blank.alternatives||[]){
    const values=question.blanks.map(item=>item.answer);values[index]=alias
    assert(gradeFillQuestion(question,values).correct)
   }
  }
  await access(`docs/triet-hoc-mac-lenin/on-thi/chuong-${chapter}/dien-tu.md`)
 }
 assert.equal(seen.size,120)
})
test('The supplied DOCX is preserved byte for byte and its fill examples are assigned to chapter II',async()=>{
 const manifest=JSON.parse(await readFile('raw_materials/triet-hoc-mac-lenin/assessment-inputs/manifest.json','utf8'))
 assert.equal(createHash('sha256').update(await readFile(manifest.file)).digest('hex'),manifest.sha256)
 const bank=JSON.parse(await readFile('src/content/courses/triet-hoc-mac-lenin/exam/fill/chuong-2.json','utf8'))
 for(const id of ['F2-001','F2-007','F2-033','F2-034'])assert(bank.questions.find(question=>question.id===id).sourceIds.includes('user-docx-2026-11-02'))
})
test('External reference cards keep provenance and include verified links without claiming all are official exams',async()=>{
 const references=JSON.parse(await readFile('src/content/courses/triet-hoc-mac-lenin/exam/papers/references.json','utf8'))
 assert(references.items.length>=10)
 assert.equal(new Set(references.items.map(item=>item.id)).size,references.items.length)
 for(const item of references.items){assert(item.verified);assert(new URL(item.url).protocol==='https:');assert(item.description)}
 assert(references.items.some(item=>item.institution.includes('HUST')))
 for(const item of references.items.filter(item=>item.institution.includes('PTIT')))assert.equal(item.provenance,'student-collection')
})
