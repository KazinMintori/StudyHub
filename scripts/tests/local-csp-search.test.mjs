import test from 'node:test'
import assert from 'node:assert/strict'
import * as local from '../../src/features/labs/services/local-search.mjs'
import * as csp from '../../src/features/labs/services/csp-search.mjs'
function solutions(p){const result=[];function visit(i,a){if(i===p.variables.length){if(csp.isSolution(p,a))result.push({...a});return}const v=p.variables[i];for(const x of p.domains[v]){a[v]=x;visit(i+1,a)}delete a[v]}visit(0,{});return result}
test('Queen objective counts attacking pairs once on all four-queen configurations',()=>{
 for(let i=0;i<256;i++){const q=Array.from({length:4},(_,j)=>Math.floor(i/4**j)%4);let attacks=0;for(let a=0;a<4;a++)for(let b=a+1;b<4;b++)if(q[a]===q[b]||Math.abs(q[a]-q[b])===b-a)attacks++;assert.equal(local.queenConflicts(q),attacks);assert.equal(local.queenNeighbors(q).length,12)}
 for(const mode of ['hill','anneal','minconflicts']){const input={rows:[0,1,2,3],mode,seed:7},a=[...local.queenSteps(input)],b=[...local.queenSteps(input)];assert.deepEqual(a,b);for(const x of a){assert.equal(x.cost,local.queenConflicts(x.rows));assert.ok(x.bestCost<=x.cost)}if(a.at(-1).phase==='success')assert.equal(a.at(-1).cost,0)}
})
test('Local landscape uses the stated acceptance, tabu and common successor pool',()=>{
 const p=local.landscapes.valley
 const hill=[...local.landscapeSteps({...p})];assert.equal(hill.at(-1).phase,'local');assert.equal(hill.at(-1).current,2)
 const anneal=[...local.landscapeSteps({...p,mode:'anneal'})];for(const s of anneal.filter(s=>s.phase==='probability')){assert.equal(s.probability,s.delta<=0?1:Math.exp(-s.delta/s.T));assert.equal(s.accepted,s.draw<s.probability)}
 const tabu=[...local.landscapeSteps({...p,mode:'tabu',tenure:3})];assert.ok(tabu.every(x=>x.tabu.length<=3));for(const x of tabu.filter(x=>x.phase==='admissible'))assert.ok(!x.tabu.includes(x.next)||p.costs[x.next]<p.costs[x.best])
 const beam=[...local.landscapeSteps({...p,mode:'beam',width:2})];for(let i=1;i<beam.length;i++)if(beam[i].phase==='select')assert.deepEqual(beam[i].beam,beam[i-1].candidates.slice(0,2))
 assert.throws(()=>[...local.landscapeSteps({costs:[1,NaN,3]})]);assert.throws(()=>[...local.landscapeSteps({...p,temperature:0})]);assert.throws(()=>[...local.landscapeSteps({...p,budget:1e8})])
})
test('2-opt preserves tours, accepts only strict improvements and reaches a local optimum',()=>{
 for(const p of Object.values(local.tourExamples)){
  const t=[...local.twoOptSteps(p)];for(const s of t){assert.deepEqual(s.tour.slice().sort((a,b)=>a-b),p.tour.slice().sort((a,b)=>a-b));assert.ok(Math.abs(s.cost-local.tourLength(p.points,s.tour))<1e-9);if(s.next)assert.ok(Math.abs(s.delta-(local.tourLength(p.points,s.next)-s.cost))<1e-9)}
  const final=t.at(-1);assert.equal(final.phase,'local');for(let i=0;i<final.tour.length;i++)for(let j=i+2;j<final.tour.length;j++){if(!i&&j===final.tour.length-1)continue;assert.ok(local.tourLength(p.points,local.twoOpt(final.tour,i,j))>=final.cost-1e-9)}
 }
 const t=[...local.twoOptSteps(local.tourExamples.cross)];assert.equal(t[0].cost,16);assert.equal(t.at(-1).cost,14)
})
test('Genetic selection normalizes fitness and elitism preserves the population best',()=>{
 for(const elitism of [false,true])for(const seed of [1,7,42]){
  const t=[...local.geneticSteps({elitism,seed})];assert.deepEqual(t[0].fitness,[24,23,20,11]);let best=0,previous=0
  for(const s of t){assert.ok(s.bestFitness>=best);best=s.bestFitness;for(const q of s.population)assert.ok(q.length===8&&q.every(x=>x>=0&&x<8));if(s.probabilities)assert.ok(Math.abs(s.probabilities.reduce((a,b)=>a+b,0)-1)<1e-12);if(s.phase==='replace'){if(elitism)assert.ok(Math.max(...s.fitness)>=previous);previous=Math.max(...s.fitness)}}
 }
 const a=[3,5,7,2,1,6,4,8],b=[2,5,7,6,8,1,3,4];assert.deepEqual(local.orderCrossover(a,b,2,6),[5,8,7,2,1,6,3,4])
 for(let l=0;l<8;l++)for(let r=l+1;r<=8;r++){const x=local.orderCrossover(a,b,l,r);assert.deepEqual(x.slice(l,r),a.slice(l,r));assert.deepEqual(x.slice().sort(),a.slice().sort())}
})
test('Backtracking variants agree with exhaustive assignments on every four-node two-color graph',()=>{
 const edges=[['A','B'],['A','C'],['A','D'],['B','C'],['B','D'],['C','D']]
 for(let mask=0;mask<64;mask++){
  const p=csp.colorCsp(['A','B','C','D'],edges.filter((_,i)=>mask>>i&1),[1,2]),sol=solutions(p),baseline=JSON.stringify(p)
  for(const filtering of ['none','fc','mac'])for(const variableOrder of ['fixed','mrv'])for(const valueOrder of ['fixed','lcv']){
   const t=[...csp.backtrackingSteps(p,{filtering,variableOrder,valueOrder})],last=t.at(-1);assert.equal(last.phase,sol.length?'success':'failure');if(sol.length)assert.ok(csp.isSolution(p,last.assignment));assert.equal(JSON.stringify(p),baseline)
   for(const s of t)for(const solution of sol)if(Object.entries(s.assignment).every(([v,x])=>solution[v]===x))for(const v of p.variables)assert.ok(s.domains[v].includes(solution[v]))
  }
 }
})
test('AC-3 preserves every solution; arc consistency alone does not solve the two-color triangle',()=>{
 for(const preset of Object.values(csp.cspPresets)){
  const p=preset.create(),sol=solutions(p),t=[...csp.ac3Steps(p)]
  for(const s of t)for(const solution of sol)for(const v of p.variables)assert.ok(s.domains[v].includes(solution[v]))
 }
 const p=csp.cspPresets.triangle.create(),t=[...csp.ac3Steps(p)];assert.equal(solutions(p).length,0);assert.equal(t.at(-1).phase,'consistent');assert.deepEqual(t.at(-1).domains,p.domains)
 const chain=[...csp.ac3Steps(csp.cspPresets.chain.create())];assert.deepEqual(chain.at(-1).domains,{A:[1],B:[2],C:[3]});assert.equal(chain.find(x=>x.phase==='revise').arc[0],'A')
 const fc=[...csp.backtrackingSteps(csp.cspPresets.forward.create(),{filtering:'fc',variableOrder:'fixed',valueOrder:'fixed'})];assert.ok(fc.some(s=>s.phase==='filter'&&s.domains.B.length===1&&s.domains.C.length===1))
})
test('Tree solver is complete on finite trees and refuses cycles or disconnected input',()=>{
 for(const name of ['chain','tree']){const p=csp.cspPresets[name].create(),t=[...csp.treeCspSteps(p)];assert.equal(t.at(-1).phase,'success');assert.ok(csp.isSolution(p,t.at(-1).assignment))}
 const p=csp.cspPresets.chain.create();p.domains.C=[1];assert.equal([...csp.treeCspSteps(p)].at(-1).phase,'failure')
 assert.throws(()=>[...csp.treeCspSteps(csp.cspPresets.triangle.create())]);assert.throws(()=>[...csp.treeCspSteps(csp.cspPresets.australia.create())])
 const one={variables:['A'],domains:{A:[0]},constraints:[]};assert.equal([...csp.treeCspSteps(one)].at(-1).assignment.A,0)
})
test('Input and budget failures are distinct from an unsatisfiability proof',()=>{
 const p=csp.cspPresets.australia.create(),last=[...csp.backtrackingSteps(p,{budget:1})].at(-1);assert.equal(last.phase,'budget');assert.deepEqual(last.assignment,{})
 assert.throws(()=>csp.validateCsp({...p,variables:['A','A']}));assert.throws(()=>csp.validateCsp({...p,constraints:[{a:'WA',b:'BAD',relation:'ne'}]}))
 const empty={variables:['A'],domains:{A:[]},constraints:[]};assert.equal([...csp.ac3Steps(empty)].at(-1).phase,'failure');assert.equal([...csp.backtrackingSteps(empty)].at(-1).phase,'failure')
 assert.equal(solutions(csp.cspPresets.australia.create()).length,18);assert.equal(solutions(csp.queenCsp(4)).length,2)
})
test('Crossword crossings prune candidates using character positions and preserve both solutions',()=>{
 const p=csp.cspPresets.crossword.create(),sol=solutions(p);assert.equal(sol.length,2)
 for(const method of ['none','fc','mac']){const result=[...csp.backtrackingSteps(p,{filtering:method})].at(-1);assert.equal(result.phase,'success');assert.ok(csp.isSolution(p,result.assignment))}
 const last=[...csp.ac3Steps(p)].at(-1);assert.deepEqual(last.domains.N1,['BAN','CAN']);assert.deepEqual(last.domains.D1,['BAO','CAO']);assert.deepEqual(last.domains.N2,['NON'])
 const bad=structuredClone(p);bad.constraints[0].positions=[9,0];assert.throws(()=>csp.validateCsp(bad))
 const wrong=csp.cspPresets.chain.create();wrong.domains.A=['x'];assert.throws(()=>csp.validateCsp(wrong))
})
