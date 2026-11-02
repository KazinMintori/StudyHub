import test from 'node:test'
import assert from 'node:assert/strict'
import {parseFormula,evaluateFormula,allModels,analyzeKnowledge,convertCnf,modelExamples,normalizeClause} from '../../src/features/labs/services/propositional-logic.mjs'
import {hornExamples,forwardChaining,sldResolution,resolutionRefutation,forwardCode,sldCode,resolutionCode,traceHorn,traceResolution,validateHorn,resolutionExamples} from '../../src/features/labs/services/propositional-inference.mjs'
test('Displayed programs are exact executable generators',()=>{
 for(const [code,fn] of [[forwardCode,forwardChaining],[sldCode,sldResolution],[resolutionCode,resolutionRefutation]])assert.deepEqual(code,fn.toString().split('\n'))
})
test('Parser respects connectives and rejects malformed or executable input',()=>{
 assert.equal(evaluateFormula(parseFormula('P -> Q -> R'),{P:true,Q:true,R:false}),false)
 assert.equal(evaluateFormula(parseFormula('P | Q & !R'),{P:true,Q:false,R:true}),true)
 assert.deepEqual(parseFormula('¬P ∨ (Q ⇒ R)'),parseFormula('!P | (Q -> R)'))
 for(const s of ['','P &','(P','P) Q','P; fetch("x")','P + Q'])assert.throws(()=>parseFormula(s))
})
test('Entailment distinguishes countermodels, unknown, negation and inconsistency',()=>{
 const d=analyzeKnowledge(['A','B -> C','A -> (B | C)'],'C')
 assert.equal(d.modelCount,2);assert.equal(d.entails,true)
 assert.deepEqual(d.rows.filter(r=>r.kb).map(r=>r.model),[{A:true,B:false,C:true},{A:true,B:true,C:true}])
 assert.equal(analyzeKnowledge(['A','B -> C','A -> (B | C)'],'B').status,'unknown')
 assert.equal(analyzeKnowledge(['P','!P'],'Q').status,'inconsistent')
 assert.equal(analyzeKnowledge(['!P'],'P').status,'negated')
 assert.equal(analyzeKnowledge(['P -> Q','Q'],'P').status,'unknown')
 assert.equal(analyzeKnowledge(['P'],'R').status,'unknown')
 assert.throws(()=>analyzeKnowledge(['A & B & C & D & E & F & G'],'A'))
})
test('CNF transformations preserve every valuation on seeded formula trees',()=>{
 let seed=87;const rand=()=>{seed=(seed*1664525+1013904223)>>>0;return seed/2**32}
 const expression=d=>d===0?['P','Q','R','TRUE','FALSE'][Math.floor(rand()*5)]:rand()<.25?'!('+expression(d-1)+')':'('+expression(d-1)+[' & ',' | ',' -> ',' <-> '][Math.floor(rand()*4)]+expression(d-1)+')'
 for(let i=0;i<100;i++){const d=convertCnf(expression(2));assert.ok(d.equivalent);assert.ok(d.rows.every(r=>r.before===r.after))}
 const d=convertCnf('P <-> (Q & R)');assert.deepEqual(d.clauses,[['!P','Q'],['!P','R'],['!Q','!R','P']])
 assert.deepEqual(convertCnf('TRUE').clauses,[]);assert.deepEqual(convertCnf('FALSE').clauses,[[]])
 assert.deepEqual(convertCnf('P | !P').clauses,[]);assert.equal(normalizeClause(['P','!P']),null)
})
test('Forward trace uses indexed counts, duplicate guards, and AND premises',()=>{
 const frames=traceHorn(hornExamples[0]),last=frames.at(-1)
 assert.equal(last.phase,'success');assert.deepEqual(last.inferred,['A','B','L','M','P','Q']);assert.ok(last.agenda.includes('L'))
 const l=frames.find(f=>f.phase==='infer'&&f.current==='L');assert.equal(l.count[1],2)
 assert.equal(traceHorn(hornExamples.find(e=>e.id==='and')).at(-1).phase,'unknown')
 assert.equal(traceHorn(hornExamples.find(e=>e.id==='cycle')).at(-1).phase,'unknown')
 const e={facts:['A'],rules:[{body:['A','A'],head:'Q'}],query:'Q'};assert.equal(validateHorn(e).rules[0].body.length,1);assert.equal(traceHorn(e).at(-1).phase,'success')
 assert.equal(traceHorn(hornExamples[0],'forward',3).at(-1).phase,'budget')
 assert.equal(frames[0].inferred.length,0);assert.deepEqual(frames[0].agenda,['A','B'])
})
test('SLD backtracks from loops and empty goals prove success',()=>{
 const f=traceHorn(hornExamples.find(e=>e.id==='backtrack'),'sld')
 assert.ok(f.some(f=>f.phase==='loop'));assert.ok(f.some(f=>f.phase==='backtrack'));assert.equal(f.at(-1).phase,'success');assert.deepEqual(f.at(-1).goals,[])
 assert.equal(traceHorn(hornExamples[0],'sld').at(-1).phase,'success')
 assert.equal(traceHorn(hornExamples.find(e=>e.id==='practice'),'sld').at(-1).phase,'success')
})
test('Both Horn methods match independent model entailment on every two-atom definite KB',()=>{
 const atoms=['P','Q'],bodies=[[],['P'],['Q'],['P','Q']],pool=atoms.flatMap(head=>bodies.map(body=>({body,head})))
 for(let mask=0;mask<256;mask++)for(const query of atoms){
  const rules=pool.filter((_,i)=>mask&(1<<i)),e={facts:[],rules,query}
  const models=[{P:false,Q:false},{P:false,Q:true},{P:true,Q:false},{P:true,Q:true}].filter(m=>rules.every(r=>!r.body.every(x=>m[x])||m[r.head]))
  const truth=models.every(m=>m[query])
  for(const mode of ['forward','sld'])assert.equal(traceHorn(e,mode).at(-1).phase==='success',truth)
 }
})
test('Resolution agrees with truth on all two-atom clause sets; each derived clause is sound',()=>{
 const pool=[]
 for(const p of [0,1,-1])for(const q of [0,1,-1])pool.push([...(p?[p===1?'P':'!P']:[]),...(q?[q===1?'Q':'!Q']:[])])
 const models=[{P:false,Q:false},{P:false,Q:true},{P:true,Q:false},{P:true,Q:true}],value=(c,m)=>c.some(l=>l[0]==='!'?!m[l.slice(1)]:m[l])
 for(let mask=0;mask<512;mask++){
  const clauses=pool.filter((_,i)=>mask&(1<<i))
  for(const query of ['P','!P']){
   const truth=models.filter(m=>clauses.every(c=>value(c,m))).every(m=>value([query],m))
   const frames=traceResolution({clauses,query}),last=frames.at(-1)
   assert.notEqual(last.phase,'budget');assert.equal(last.phase==='success',truth)
   for(const c of last.clauses.filter(c=>c.parents)){
    const parents=c.parents.map(id=>last.clauses.find(x=>x.id===id))
    assert.ok(models.filter(m=>parents.every(p=>value(p.literals,m))).every(m=>value(c.literals,m)))
   }
  }
 }
 const multi=traceResolution(resolutionExamples.find(e=>e.id==='multipivot'));assert.equal(multi.at(-1).phase,'saturated');assert.ok(!multi.at(-1).clauses.some(c=>!c.literals.length))
 assert.equal(traceResolution(resolutionExamples[0],1).at(-1).phase,'budget')
 assert.equal(traceResolution({clauses:[[]],query:'P'}).at(-1).phase,'success')
})
