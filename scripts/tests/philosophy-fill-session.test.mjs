import test from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { parse, compileScript, compileStyle, compileTemplate } from 'vue/compiler-sfc'
import {
  createFillSession, fillQuestions, fillQuestionStatus, fillResponse, fillStats, fillStorageKey,
  gradeFillQuestion, loadFillSession, normalizeFillAnswer, restoreFillSession, retryFillQuestion,
  saveFillSession, setCurrentFillQuestion, setFillAnswer, submitFillQuestion,
} from '../../src/features/philosophy/services/fill-session.mjs'

const question=(id='F1-001')=>({id,parts:['Vật chất là một phạm trù ',' dùng để chỉ thực tại ','.'],blanks:[{answer:'triết học',label:'Loại phạm trù'},{answer:'khách quan',alternatives:['khách-quan'],label:'Tính chất thực tại'}],explanation:'Vật chất được nhận diện bởi tính tồn tại khách quan, độc lập với ý thức.'})
const bank={version:1,id:'fill-chuong-1',chapter:1,questions:[question(),{...question('F1-002'),parts:['Hoạt động ',' và ',' tạo điều kiện xã hội của ý thức.'],blanks:[{answer:'lao động'},{answer:'ngôn ngữ'}]}]}
const storage=()=>{const values=new Map();return {getItem:key=>values.get(key)??null,setItem:(key,value)=>values.set(key,value),values}}
const draft=(source=bank,id=source.questions[0].id,values=['triết học','khách quan'])=>values.reduce((session,value,index)=>setFillAnswer(source,session,id,index,value),createFillSession(source))

test('normalization accepts Vietnamese accents, decomposed Unicode, spacing, case and punctuation without fuzzy matching',()=>{
  assert.equal(normalizeFillAnswer('  TRIẾT   HỌC! '),'triet hoc')
  assert.equal(normalizeFillAnswer('ý thức'.normalize('NFD')),'y thuc')
  assert.equal(normalizeFillAnswer('LAO ĐỘNG'),'lao dong')
  assert.equal(gradeFillQuestion(question(),['triet hoc','khach quan']).correct,true)
  assert.equal(gradeFillQuestion(question(),['triết học','chủ quan']).correct,false)
  assert.equal(gradeFillQuestion({blanks:[{answer:'ý thức'}]},['thức']).correct,false)
  assert.equal(gradeFillQuestion({blanks:[{answer:'độc lập với ý thức'}]},['không độc lập với ý thức']).correct,false)
  assert.equal(gradeFillQuestion({blanks:[{answer:'lao động và ngôn ngữ'}]},['ngôn ngữ và lao động']).correct,false)
  assert.equal(gradeFillQuestion({blanks:[{answer:'1841'}]},['1842']).correct,false)
})

test('multiple blanks are graded independently and only explicit equivalent answers are accepted',()=>{
  const q={blanks:[{answer:'phủ định biện chứng',alternatives:['sự phủ định biện chứng']},{answer:'ý thức'}]}
  const result=gradeFillQuestion(q,['SỰ PHỦ ĐỊNH BIỆN CHỨNG','vật chất'])
  assert.equal(result.complete,true)
  assert.equal(result.correct,false)
  assert.deepEqual(result.results.map(item=>item.correct),[true,false])
  assert.equal(result.results[1].expected,'ý thức')
  assert.equal(gradeFillQuestion(q,['sự phủ định sạch trơn','ý thức']).correct,false)
})

test('a draft does not count as an answer and empty or punctuation-only fields cannot be submitted',()=>{
  const empty=createFillSession(bank)
  assert.equal(submitFillQuestion(bank,empty,'F1-001'),empty)
  const partial=setFillAnswer(bank,empty,'F1-001',0,'triết học')
  assert.equal(submitFillQuestion(bank,partial,'F1-001'),partial)
  assert.equal(gradeFillQuestion(question(),['triết học','...']).complete,false)
  assert.equal(gradeFillQuestion(question(),null).complete,false)
  assert.deepEqual(fillStats(bank,partial),{total:2,correct:0,wrong:0,answered:0,unanswered:2})
  const complete=draft()
  assert.equal(fillQuestionStatus(question(),complete),'unanswered')
  assert.equal(fillResponse(empty,'F1-001'),null)
})

test('submitting locks a complete answer and derives scoring without mutating drafts',()=>{
  const before=draft()
  const checked=submitFillQuestion(bank,before,'F1-001')
  assert.equal(fillResponse(before,'F1-001').checked,false)
  assert.equal(fillResponse(checked,'F1-001').checked,true)
  assert.equal(fillQuestionStatus(question(),checked),'correct')
  assert.deepEqual(fillStats(bank,checked),{total:2,correct:1,wrong:0,answered:1,unanswered:1})
  assert.equal(setFillAnswer(bank,checked,'F1-001',0,'khác'),checked)
  assert.equal(submitFillQuestion(bank,checked,'F1-001'),checked)
})

test('retry preserves correct fields and clears incorrect fields before a new submission',()=>{
  const checked=submitFillQuestion(bank,draft(bank,'F1-001',['triết học','chủ quan']),'F1-001')
  assert.equal(fillQuestionStatus(question(),checked),'wrong')
  const retry=retryFillQuestion(bank,checked,'F1-001')
  assert.deepEqual(fillResponse(retry,'F1-001'),{values:['triết học',''],checked:false})
  assert.equal(fillStats(bank,retry).answered,0)
  const corrected=submitFillQuestion(bank,setFillAnswer(bank,retry,'F1-001',1,'khách quan'),'F1-001')
  assert.equal(fillQuestionStatus(question(),corrected),'correct')
  assert.deepEqual(fillResponse(retryFillQuestion(bank,corrected,'F1-001'),'F1-001').values,['',''])
})

test('navigation accepts only bank IDs and preserves values and grading',()=>{
  const before=submitFillQuestion(bank,draft(),'F1-001')
  const next=setCurrentFillQuestion(bank,before,'F1-002')
  assert.equal(next.currentId,'F1-002')
  assert.deepEqual(next.responses,before.responses)
  assert.equal(setCurrentFillQuestion(bank,next,'invalid'),next)
  assert.equal(setCurrentFillQuestion(bank,next,'F1-002'),next)
  assert.equal(setFillAnswer(bank,next,'F1-001',-1,'x'),next)
  assert.equal(setFillAnswer(bank,next,'F1-002',2,'x'),next)
})

test('storage restores chapter-isolated drafts, completed answers and current position',()=>{
  const memory=storage(),other={...bank,id:'fill-chuong-2',chapter:2}
  const first=setCurrentFillQuestion(bank,submitFillQuestion(bank,draft(),'F1-001'),'F1-002')
  assert.equal(saveFillSession(bank,first,memory),true)
  assert.deepEqual(loadFillSession(bank,memory),first)
  assert.deepEqual(loadFillSession(other,memory),createFillSession(other))
  saveFillSession(other,draft(other),memory)
  assert.equal(memory.values.size,2)
  assert.notEqual(fillStorageKey(bank),fillStorageKey(other))
  assert.notEqual(fillStorageKey(bank),fillStorageKey({...bank,version:2}))
})

test('restoring rejects corrupt envelopes and recalculates grades against current accepted terms',()=>{
  const complete=submitFillQuestion(bank,draft(),'F1-001')
  for(const raw of ['{bad','[]',null,42,{...complete,bankId:'wrong'},{...complete,version:99},{...complete,bankVersion:99}])assert.deepEqual(restoreFillSession(bank,raw),createFillSession(bank))
  const edited=structuredClone(complete)
  edited.currentId='deleted'
  edited.responses.unknown={values:['x'],checked:true}
  edited.responses['F1-002']={values:[false,''],checked:true}
  edited.responses['F1-001'].correct=true
  const restored=restoreFillSession(bank,edited)
  assert.equal(restored.currentId,'F1-001')
  assert.equal(restored.responses.unknown,undefined)
  assert.deepEqual(restored.responses['F1-002'],{values:['',''],checked:false})
  const changed={...bank,questions:[{...question(),blanks:[{answer:'vật lý'},{answer:'khách quan'}]}]}
  assert.equal(fillQuestionStatus(changed.questions[0],restoreFillSession(changed,complete)),'wrong')
  const long={...complete,responses:{'F1-001':{values:['x'.repeat(500),'y'],checked:false}}}
  assert.equal(restoreFillSession(bank,long).responses['F1-001'].values[0].length,160)
})

test('malformed banks, blocked storage and SSR have usable safe defaults',()=>{
  assert.equal(fillQuestions({...bank,questions:[null,question(),question(),{...question('bad'),parts:['bad']},{...question('bad2'),blanks:[{answer:'   '}]}]}).length,1)
  const empty=createFillSession({id:'empty',questions:[]})
  assert.equal(empty.currentId,null)
  const blocked={getItem(){throw Error('blocked')},setItem(){throw Error('quota')}}
  assert.deepEqual(loadFillSession(bank,blocked),createFillSession(bank))
  assert.equal(saveFillSession(bank,empty,blocked),false)
  assert.deepEqual(loadFillSession(bank),createFillSession(bank))
  assert.equal(saveFillSession(bank,empty),false)
})

test('the fill component compiles for client, SSR and scoped CSS with semantic form controls',()=>{
  const filename='src/features/philosophy/components/PhilosophyFillPractice.vue'
  const source=readFileSync(filename,'utf8')
  const {descriptor,errors}=parse(source,{filename})
  assert.deepEqual(errors,[])
  const script=compileScript(descriptor,{id:'philosophy-fill'})
  for(const ssr of [false,true]) {
    const compiled=compileTemplate({id:'philosophy-fill',filename,source:descriptor.template.content,ssr,ssrCssVars:[],compilerOptions:{bindingMetadata:script.bindings}})
    assert.deepEqual(compiled.errors,[])
  }
  assert.deepEqual(compileStyle({id:'philosophy-fill',filename,source:descriptor.styles[0].content,scoped:true}).errors,[])
  assert.match(source,/@submit\.prevent="answer"/)
  assert.match(source,/:aria-describedby=/)
  assert.match(source,/:aria-invalid=/)
  assert.match(source,/maxlength="160"/)
  assert.doesNotMatch(source,/v-html|PhilosophyNav/)
})
