import test from 'node:test'
import assert from 'node:assert/strict'
import * as terms from '../../src/features/labs/services/predicate-terms.mjs'
import * as models from '../../src/features/labs/services/predicate-models.mjs'
import * as infer from '../../src/features/labs/services/predicate-inference.mjs'
test('Unification returns a finite shared substitution, including indirect occurs checks',()=>{
 for(const [name,p]of Object.entries(terms.unificationExamples)){
  const a=terms.parseTerm(p.left),b=terms.parseTerm(p.right),t=[...terms.unifySteps(a,b)],result=terms.unify(a,b)
  if(['occurs','indirect','shared'].includes(name)){assert.equal(result,null);assert.ok(['failure','occurs'].includes(t.at(-1).phase))}else{assert.equal(t.at(-1).phase,'success');assert.equal(terms.formatTerm(terms.applyTerm(a,result)),terms.formatTerm(terms.applyTerm(b,result)))}
 }
 assert.deepEqual(terms.formatTheta(terms.unify(terms.parseTerm('Knows(John, ?x)'),terms.parseTerm('Knows(?y, Mother(?y))'))),{'?y':'John','?x':'Mother(John)'})
 assert.equal(terms.unify(terms.parseTerm('f(A)'),terms.parseTerm('g(A)')),null)
 assert.equal(terms.unify(terms.parseTerm('f(A)'),terms.parseTerm('f(A, B)')),null)
 assert.throws(()=>terms.parseTerm('P(x) || process()'));assert.throws(()=>terms.parseTerm('f()'));assert.throws(()=>terms.applyTerm(terms.parseTerm('?x'),{x:terms.parseTerm('f(?x)')}))
})
test('All shallow term pairs produce sound unifiers; a more specific ground solution remains an instance',()=>{
 const strings=['A','B','?x','?y','f(A)','f(B)','f(?x)','g(?x, ?y)','g(A, ?x)','g(?y, B)'],domain=['A','B','f(A)','f(B)'].map(terms.parseTerm)
 for(const sa of strings)for(const sb of strings){const a=terms.parseTerm(sa),b=terms.parseTerm(sb),u=terms.unify(a,b);if(u)assert.equal(terms.formatTerm(terms.applyTerm(a,u)),terms.formatTerm(terms.applyTerm(b,u)))
  for(const x of domain)for(const y of domain){const ground={x,y};if(terms.formatTerm(terms.applyTerm(a,ground))!==terms.formatTerm(terms.applyTerm(b,ground)))continue;assert.notEqual(u,null,sa+' '+sb);for(const [v,t]of Object.entries(u))assert.equal(terms.formatTerm(terms.applyTerm(t,ground)),terms.formatTerm(ground[v]))}
 }
})
test('Quantified relation truth agrees with direct enumeration of every three-object relation',()=>{
 for(let mask=0;mask<512;mask++){
  const m=Array.from({length:3},(_,x)=>Array.from({length:3},(_,y)=>!!(mask>>(x*3+y)&1)))
  const expected={ae:[0,1,2].every(y=>[0,1,2].some(x=>m[x][y])),ea:m.some(row=>row.every(Boolean)),aa:m.every(row=>row.every(Boolean)),ee:m.some(row=>row.some(Boolean))}
  for(const [id,v]of Object.entries(expected))assert.equal([...models.quantifierSteps(m,id)].at(-1).value,v)
  if(expected.ea)assert.equal(expected.ae,true)
 }
 const identity=models.relationPresets.identity.matrix;assert.equal([...models.quantifierSteps(identity,'ae')].at(-1).value,true);assert.equal([...models.quantifierSteps(identity,'ea')].at(-1).value,false)
})
test('Forward chaining and SLD preserve joint substitutions and answer only query variables',()=>{
 for(const name of ['kings','students','shared','backtrack']){const p=infer.predicatePrograms[name],f=[...infer.forwardPredicateSteps(p)].at(-1),s=[...infer.sldPredicateSteps(p)].at(-1);assert.equal(f.phase,'fixedpoint');assert.equal(s.phase,'finished');assert.deepEqual(s.answers,f.answers)}
 assert.deepEqual([...infer.forwardPredicateSteps(infer.predicatePrograms.shared)].at(-1).answers,[])
 assert.equal([...infer.sldPredicateSteps(infer.predicatePrograms.cycle)].at(-1).phase,'budget')
 const t=[...infer.sldPredicateSteps(infer.predicatePrograms.backtrack)];assert.ok(t.some(x=>x.phase==='backtrack'));assert.deepEqual(t.at(-1).answers,[{'?z':'An'}])
  const collisions={facts:['P(An)','Q(Binh)'],rules:[{head:'Pair(?x, ?y)',body:['P(?x)','Q(?y)']}],query:'Pair(?r1_0, ?r1_1)'};assert.deepEqual([...infer.sldPredicateSteps(collisions)].at(-1).answers,[{'?r1_0':'An','?r1_1':'Binh'}])
 assert.equal([...infer.forwardPredicateSteps(infer.predicatePrograms.growing)].at(-1).phase,'budget')
})
test('Function-free unary definite programs agree with a separate ground propositional closure',()=>{
 const rules=[{head:'Q(?x)',body:['P(?x)']},{head:'R(?x)',body:['Q(?x)']},{head:'P(?x)',body:['Q(?x)','R(?x)']}],atoms=['P(A)','P(B)','Q(A)','Q(B)','R(A)','R(B)']
 for(let mask=0;mask<64;mask++){
  const facts=atoms.filter((_,i)=>mask>>i&1),closure=new Set(facts)
  let change=true;while(change){change=false;for(const c of ['A','B'])for(const [body,head]of [[['P'],'Q'],[['Q'],'R'],[['Q','R'],'P']])if(body.every(x=>closure.has(`${x}(${c})`))&&!closure.has(`${head}(${c})`)){closure.add(`${head}(${c})`);change=true}}
  const p={facts,rules,query:'R(?z)'},f=[...infer.forwardPredicateSteps(p)].at(-1);assert.deepEqual(new Set(f.facts),closure)
  const s=[...infer.sldPredicateSteps(p,{maxDepth:8,maxEvents:2000})].at(-1);for(const answer of s.answers)assert.ok(closure.has('R('+answer['?z']+')'))
 }
})
test('Resolution applies a single pivot substitution to both remainders and standardizes apart',()=>{
 const a=infer.parseClause('~P(?x)|Q(?x)'),b=infer.parseClause('P(An)|R(?x)'),r=infer.resolveClauses(a,b,0,0)
 assert.notEqual(r,null);assert.match(infer.formatClause(r.clause),/Q\(An\)/);assert.match(infer.formatClause(r.clause),/R\(\?v0\)/)
 assert.equal(infer.resolveClauses(infer.parseClause('P(?x)'),infer.parseClause('P(An)'),0,0),null)
 for(const name of ['kings','factoring']){const t=[...infer.resolutionPredicateSteps(infer.resolutionExamples[name].clauses)];assert.equal(t.at(-1).phase,'success');assert.equal(t.at(-1).clauses.at(-1).text,'□')}
 const notTaut=[...infer.resolutionPredicateSteps(['P(?x)|~P(?y)'])];assert.ok(notTaut[0].clauses.length);assert.notEqual(notTaut.at(-1).phase,'success')
 const factor=[...infer.resolutionPredicateSteps(infer.resolutionExamples.factoring.clauses)];assert.ok(factor.some(x=>x.phase==='factor'))
})
test('Every displayed ground resolvent is entailed by its parents on all Boolean models',()=>{
 const clauses=['P(A)|Q(A)','~P(A)|R(A)','~Q(A)','~R(A)'],trace=[...infer.resolutionPredicateSteps(clauses)],truth=(text,bits)=>text==='□'?false:text.split(' ∨ ').some(l=>{const neg=l.startsWith('¬'),name=l.replace('¬','');return neg?!bits[name]:bits[name]})
 for(const s of trace)for(const c of s.clauses.filter(c=>c.parents.length))for(let mask=0;mask<8;mask++){
  const bits={'P(A)':!!(mask&1),'Q(A)':!!(mask&2),'R(A)':!!(mask&4)},parents=c.parents.map(id=>s.clauses[id-1]);if(parents.every(p=>truth(p.text,bits)))assert.equal(truth(c.text,bits),true)
 }
 assert.equal(trace.at(-1).phase,'success')
})
test('Finite model and program validation reject unsupported or malformed inputs',()=>{
 assert.throws(()=>[...models.quantifierSteps([])]);assert.throws(()=>[...models.quantifierSteps([[1]])])
 assert.throws(()=>infer.validateProgram({facts:['P(?x)'],rules:[],query:'P(A)'}));assert.throws(()=>infer.validateProgram({facts:['P(A)'],rules:[{head:'Q(?x)',body:['P(A)']}],query:'Q(?x)'}))
 const empty=[...infer.resolutionPredicateSteps(['[]'])];assert.equal(empty.at(-1).phase,'success')
})
