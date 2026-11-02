import {normalizeCnf,normalizeClause,negateLiteral,allModels} from './propositional-logic.mjs'
import {forwardCode,sldCode,resolutionCode} from './propositional-code.mjs'
export {forwardCode,sldCode,resolutionCode}
export const hornExamples=[
 {id:'source',title:'Đồ thị AND trong slide',facts:['A','B'],rules:[{body:['P'],head:'Q'},{body:['L','M'],head:'P'},{body:['B','L'],head:'M'},{body:['A','P'],head:'L'},{body:['A','B'],head:'L'}],query:'Q'},
 {id:'cycle',title:'Chu trình chưa có sự thực làm điểm tựa',facts:[],rules:[{body:['P'],head:'Q'},{body:['Q'],head:'P'}],query:'Q'},
 {id:'backtrack',title:'Nhánh vòng lặp đứng trước lời giải',facts:['A'],rules:[{body:['Q'],head:'Q'},{body:['A'],head:'Q'}],query:'Q'},
 {id:'and',title:'Thiếu một tiền đề của luật AND',facts:['A'],rules:[{body:['A','B'],head:'Q'}],query:'Q'},
 {id:'fact',title:'Truy vấn đã là sự thực',facts:['Q'],rules:[],query:'Q'},
 {id:'practice',title:'Bài thực hành mười luật',facts:['A','B'],rules:[{body:['A'],head:'C'},{body:['B'],head:'D'},{body:['C','D'],head:'E'},{body:['E'],head:'F'},{body:['F'],head:'G'},{body:['A','D'],head:'H'},{body:['H','C'],head:'I'},{body:['I'],head:'J'},{body:['J','G'],head:'K'},{body:['K'],head:'Q'}],query:'Q'}
]
export function validateHorn(e){
 const atom=s=>typeof s==='string'&&/^[A-Za-z][A-Za-z0-9_]{0,7}$/.test(s)
 if(!e||!Array.isArray(e.facts)||!Array.isArray(e.rules)||e.facts.length>12||e.rules.length>16||!atom(e.query)||e.facts.some(x=>!atom(x)))throw Error('Cần facts, rules và query là ký hiệu nguyên tử hợp lệ. Tối đa 16 luật.')
 const rules=e.rules.map((r,i)=>{if(!r||!atom(r.head)||!Array.isArray(r.body)||r.body.length>8||r.body.some(x=>!atom(x)))throw Error('Mỗi luật có head là một ký hiệu và body là mảng tối đa 8 ký hiệu.');return {id:'r'+(i+1),body:[...new Set(r.body)],head:r.head}})
 const symbols=[...new Set([...e.facts,e.query,...rules.flatMap(r=>[r.head,...r.body])])].sort()
 if(symbols.length>12)throw Error('Tối đa 12 ký hiệu trong bộ xem suy luận.')
 return {facts:[...new Set(e.facts)],rules,query:e.query,symbols}
}
export function* forwardChaining(example){
 const {facts,rules,query}=validateHorn(example)
 const agenda=[...facts],inferred=new Set(),count=rules.map(r=>r.body.length),index=new Map()
 rules.forEach((r,i)=>r.body.forEach(p=>{if(!index.has(p))index.set(p,[]);index.get(p).push(i)}))
 rules.forEach(r=>{if(!r.body.length)agenda.push(r.head)})
 const snap=(phase,current=null,rule=null)=>({phase,current,rule,agenda:[...agenda],inferred:[...inferred],count:[...count]})
 yield snap('start')
 while(agenda.length){
  const p=agenda.shift()
  yield snap('take',p)
  if(inferred.has(p)){yield snap('duplicate',p);continue}
  inferred.add(p)
  yield snap('infer',p)
  if(p===query){yield snap('success',p);return}
  for(const i of index.get(p)||[]){
   count[i]--
   yield snap('count',p,rules[i].id)
   if(count[i]===0){agenda.push(rules[i].head);yield snap('fire',p,rules[i].id)}
  }
 }
 yield snap('unknown')
}
export function* sldResolution(example){
 const {facts,rules,query}=validateHorn(example)
 const clauses=[...rules,...facts.map((head,i)=>({id:'f'+(i+1),body:[],head}))]
 const stack=[],active=new Set()
 const snap=(phase,goals,rule=null)=>({phase,goals:[...goals],rule,stack:stack.map(s=>({...s}))})
 function* solve(goals){
  yield snap('goal',goals)
  if(!goals.length){yield snap('success',goals);return true}
  const key=[...new Set(goals)].sort().join('&')
  if(active.has(key)){yield snap('loop',goals);return false}
  active.add(key)
  const selected=goals[0]
  for(const rule of clauses.filter(c=>c.head===selected)){
   const next=[...new Set([...rule.body,...goals.slice(1)])]
   stack.push({selected,rule:rule.id,goals:goals.join(', ')})
   yield snap('resolve',next,rule.id)
   if(yield* solve(next)){active.delete(key);return true}
   stack.pop()
   yield snap('backtrack',goals,rule.id)
  }
  active.delete(key)
  yield snap('deadend',goals)
  return false
 }
 const proven=yield* solve([query])
 if(!proven)yield snap('unknown',[query])
}
export function traceHorn(example,mode='forward',budget=1000){
 const frames=[],generator=mode==='sld'?sldResolution(example):forwardChaining(example)
 for(const f of generator){frames.push(f);if(frames.length>=budget){frames.push({...f,phase:'budget'});break}}
 return frames
}
export const resolutionExamples=[
 {id:'rain',title:'Modus ponens bằng phản chứng',clauses:[['P'],['!P','Q']],query:'Q'},
 {id:'wumpus',title:'Không có gió, không có hố liền kề',clauses:[['!Q','B'],['!B','P','Q'],['!P','B'],['!B']],query:'!P'},
 {id:'unknown',title:'Chưa đủ tri thức cho Q',clauses:[['!P','Q']],query:'Q'},
 {id:'multipivot',title:'Không được khử hai cặp cùng lúc',clauses:[['P','Q'],['!P','!Q']],query:'R'},
 {id:'inconsistent',title:'Cơ sở tri thức đã mâu thuẫn',clauses:[['P'],['!P']],query:'Q'}
]
export function validateResolution(e){
 const literal=x=>typeof x==='string'&&/^!?[A-Za-z][A-Za-z0-9_]{0,7}$/.test(x)
 if(!e||!Array.isArray(e.clauses)||e.clauses.length>16||!literal(e.query)||e.clauses.some(c=>!Array.isArray(c)||c.length>8||c.some(x=>!literal(x))))throw Error('Nhập tối đa 16 clause, mỗi clause là mảng literal. Truy vấn là một literal.')
 const symbols=[...new Set([...e.clauses.flat(),e.query].map(x=>x.replace('!','')))].sort()
 if(symbols.length>6)throw Error('Hợp giải trong bộ xem hỗ trợ tối đa 6 ký hiệu.')
 return {clauses:normalizeCnf(e.clauses),query:e.query,symbols}
}
export function resolutionDiagnostic(e){
 const {clauses,query,symbols}=validateResolution(e),truth=(l,m)=>l.startsWith('!')?!m[l.slice(1)]:m[l]
 const models=allModels(symbols).filter(m=>clauses.every(c=>c.some(l=>truth(l,m))))
 return {consistent:models.length>0,models:models.length,entails:models.every(m=>truth(query,m)),counter:models.find(m=>!truth(query,m))||null}
}
export function* resolutionRefutation(example,maxClauses=80){
 const input=validateResolution(example)
 const clauses=input.clauses.map((literals,i)=>({id:'c'+(i+1),literals,parents:null,pivot:null}))
 const negative=[negateLiteral(input.query)],seen=new Set(clauses.map(c=>c.literals.join('|')))
 if(!seen.has(negative.join('|'))){clauses.push({id:'c'+(clauses.length+1),literals:negative,parents:null,pivot:null,negatedQuery:true});seen.add(negative.join('|'))}
 const snap=(phase,parents=null,pivot=null,candidate=null)=>({phase,parents,pivot,candidate,clauses:clauses.map(c=>({...c,literals:[...c.literals]}))})
 yield snap('start')
 if(clauses.some(c=>!c.literals.length)){yield snap('success');return}
 for(let i=0;i<clauses.length;i++)for(let j=0;j<i;j++){
  const a=clauses[i],b=clauses[j]
  for(const literal of a.literals){
   if(!b.literals.includes(negateLiteral(literal)))continue
   const parents=[a.id,b.id],pivot=literal.replace('!','')
   const candidate=normalizeClause([...a.literals.filter(x=>x!==literal),...b.literals.filter(x=>x!==negateLiteral(literal))])
   yield snap('resolve',parents,pivot,candidate)
   if(candidate===null){yield snap('tautology',parents,pivot);continue}
   const key=candidate.join('|')
   if(seen.has(key)){yield snap('duplicate',parents,pivot,candidate);continue}
   if(clauses.length>=maxClauses){yield snap('budget',parents,pivot,candidate);return}
   seen.add(key)
   clauses.push({id:'c'+(clauses.length+1),literals:candidate,parents,pivot})
   yield snap('add',parents,pivot,candidate)
   if(!candidate.length){yield snap('success',parents,pivot,candidate);return}
  }
 }
 yield snap('saturated')
}
export function traceResolution(e,budget=1500,maxClauses=80){const frames=[];for(const f of resolutionRefutation(e,maxClauses)){frames.push(f);if(frames.length>=budget){frames.push({...f,phase:'budget'});break}}return frames}
