import test from 'node:test'
import assert from 'node:assert/strict'
import {searchExamples,traceUninformed,searchCode,idsCode,graphSearch,iterativeSearch} from '../../src/features/labs/services/uninformed-search.mjs'
test('readable production code matches the executable generators before bundling',()=>{
 assert.equal(searchCode.join('\n'),graphSearch.toString())
 assert.equal(idsCode.join('\n'),iterativeSearch.toString())
})
test('visualization budget is not mistaken for proof of no solution',()=>{
 const names=['S','A','B','C','D','E','F','G']
 const g=Object.fromEntries(names.map(u=>[u,u==='G'?[]:names.filter(v=>v!==u&&v!=='G').map(v=>[v,1])]))
 const trace=traceUninformed(g,'S','G','ids')
 assert.equal(trace.at(-1).phase,'budget');assert.equal(trace.at(-1).result,null)
 assert.equal(trace.length,1001)
})
test('weighted examples distinguish fewest edges and least total cost',()=>{
 const e=searchExamples[0]
 for(const m of ['bfs','dfs','ids'])assert.deepEqual(traceUninformed(e.graph,e.start,e.goal,m).at(-1).result,{path:['S','A','C','G'],cost:9,depth:3})
 assert.deepEqual(traceUninformed(e.graph,e.start,e.goal,'ucs').at(-1).result,{path:['S','A','B','C','G'],cost:7,depth:4})
})
test('first generated goal is not the UCS answer; zero edges work',()=>{
 const e=searchExamples[2]
 assert.equal(traceUninformed(e.graph,e.start,e.goal,'bfs').at(-1).result.cost,10)
 assert.equal(traceUninformed(e.graph,e.start,e.goal,'ucs').at(-1).result.cost,2)
 assert.equal(traceUninformed({S:[['A',0],['G',3]],A:[['S',0],['G',1]],G:[]},'S','G','ucs').at(-1).result.cost,1)
})
test('Dijkstra shares the UCS prefix, then continues to settle remaining distances',()=>{
 const e=searchExamples.find(e=>e.id==='beyond')
 const ucs=traceUninformed(e.graph,e.start,e.goal,'ucs'),dijkstra=traceUninformed(e.graph,e.start,e.goal,'dijkstra')
 assert.deepEqual(dijkstra.slice(0,ucs.length-1),ucs.slice(0,-1))
 assert.equal(ucs.at(-1).result.cost,2)
 assert.equal(ucs.at(-1).best.C,undefined)
 assert.equal(dijkstra.at(-1).phase,'complete')
 assert.deepEqual(dijkstra.at(-1).result.distances,{S:0,A:1,B:7,C:8,G:2})
 assert.deepEqual(dijkstra.at(-1).result.path,['S','G'])
 const disconnected=searchExamples.find(e=>e.id==='unreachable')
 assert.equal(traceUninformed(disconnected.graph,'S','G','dijkstra').at(-1).result.distances.G,Infinity)
})
test('all modes terminate on cycles, failure, and initial goal; snapshots replay independently',()=>{
 for(const e of searchExamples)for(const mode of ['bfs','dfs','ucs','ids']){
  const trace=traceUninformed(e.graph,e.start,e.goal,mode),end=trace.at(-1)
  assert.ok(['success','failure'].includes(end.phase));assert.ok(trace.length<500)
  if(e.id==='unreachable')assert.equal(end.phase,'failure')
  if(e.id==='initial')assert.deepEqual(end.result,{path:['S'],cost:0,depth:0})
  assert.deepEqual(trace,traceUninformed(e.graph,e.start,e.goal,mode))
 }
})
test('UCS costs and BFS/IDS depths agree with independent solvers on 50 small graphs',()=>{
 let seed=25;const rand=()=>{seed=(seed*1664525+1013904223)>>>0;return seed/2**32}
 for(let k=0;k<50;k++){
  const g=Object.fromEntries(['S','A','B','C','G'].map(v=>[v,[]]))
  for(const u of Object.keys(g))for(const v of Object.keys(g))if(u!==v&&rand()<.3)g[u].push([v,Math.floor(rand()*6)])
  const d=Object.fromEntries(Object.keys(g).map(v=>[v,v==='S'?0:Infinity]))
  for(let j=0;j<4;j++)for(const [u,edges] of Object.entries(g))for(const [v,w]of edges)d[v]=Math.min(d[v],d[u]+w)
  const end=traceUninformed(g,'S','G','ucs').at(-1)
  assert.equal(end.result?.cost??Infinity,d.G)
  const all=traceUninformed(g,'S','G','dijkstra').at(-1).result.distances
  assert.deepEqual(all,d)
  const queue=[['S',0]],seen=new Set(['S']);let depth=Infinity
  while(queue.length){const [u,k]=queue.shift();if(u==='G'){depth=k;break}for(const[v]of g[u])if(!seen.has(v)){seen.add(v);queue.push([v,k+1])}}
  assert.equal(traceUninformed(g,'S','G','bfs').at(-1).result?.depth??Infinity,depth)
  assert.equal(traceUninformed(g,'S','G','ids').at(-1).result?.depth??Infinity,depth)
 }
})
