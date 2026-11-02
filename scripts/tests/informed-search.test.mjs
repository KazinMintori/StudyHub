import test from 'node:test'
import assert from 'node:assert/strict'
import {informedExamples,informedSearch,informedCode,traceInformed,inspectHeuristic,validateInformed,informedLine} from '../../src/features/labs/services/informed-search.mjs'
import {puzzleGoal,puzzleExamples,puzzleParts,puzzleHeuristic,puzzleNeighbors,solvePuzzle,validatePuzzle} from '../../src/features/labs/services/heuristic-puzzle.mjs'
const example=id=>informedExamples.find(e=>e.id===id)
const last=(e,m='astar',r=true)=>traceInformed(e,m,r).at(-1)
test('Displayed code is the exact executable generator, with stable highlighted lines',()=>{
  assert.deepEqual(informedCode,informedSearch.toString().split('\n'))
  for(const p of ['start','take','stale','expand','consider','skip','blocked','insert','reopen','success','failure','budget'])assert.ok(informedLine(p)>=0&&informedLine(p)<informedCode.length)
})
test('Concrete traces distinguish priorities and handle source examples',()=>{
  assert.equal(last(example('weighted'),'ucs').result.cost,7)
  assert.equal(last(example('weighted'),'greedy').result.cost,8)
  assert.equal(last(example('weighted')).result.cost,7)
  assert.deepEqual(last(example('weighted')).result.path,['S','A','B','C','G'])
  assert.equal(last(example('slides')).result.cost,6)
  const frames=traceInformed(example('early'))
  const firstGoal=frames.find(f=>f.phase==='insert'&&f.frontier.some(n=>n.state==='G'))
  assert.equal(firstGoal.frontier.find(n=>n.state==='G').g,5)
  assert.equal(frames.at(-1).result.cost,4)
  assert.equal(last(example('overestimate')).result.cost,5)
  assert.equal(inspectHeuristic(example('overestimate')).exact.S,4)
})
test('Admissible inconsistent h needs reopening and can produce decreasing f',()=>{
  const e=example('reopen'),a=inspectHeuristic(e)
  assert.equal(a.admissible,true);assert.equal(a.consistent,false)
  assert.equal(last(e,'astar',false).result.cost,6)
  const trace=traceInformed(e)
  assert.equal(trace.at(-1).result.cost,5)
  assert.equal(trace.filter(f=>f.phase==='reopen').length,1)
  assert.deepEqual(trace.filter(f=>f.phase==='expand').map(f=>f.nodes[f.current].f),[2,2,4,5,3])
  const fixed=example('consistent')
  assert.equal(inspectHeuristic(fixed).consistent,true)
  assert.equal(last(fixed,'astar',false).result.cost,5)
})
test('Zero heuristic matches UCS, snapshots are immutable, failure and budget differ',()=>{
  for(const e of informedExamples){
    const z={...e,h:Object.fromEntries(Object.keys(e.graph).map(v=>[v,0]))}
    assert.deepEqual(traceInformed(z),traceInformed(z,'ucs'))
  }
  const t=traceInformed(example('weighted'));assert.equal(t[0].frontier.length,1);assert.deepEqual(t[0].closed,[]);assert.equal(t[0].nodes.length,1)
  assert.equal(last(example('unreachable')).phase,'failure')
  assert.equal(traceInformed(example('weighted'),'astar',true,3).at(-1).phase,'budget')
  assert.equal(last(example('initial')).result.cost,0)
})
test('A* with reopening agrees with independent Bellman-Ford on seeded graphs',()=>{
  let seed=12541;const rand=()=>{seed=(seed*1664525+1013904223)>>>0;return seed/2**32}
  for(let trial=0;trial<80;trial++){
    const ids=['S','A','B','C','D','G'],graph=Object.fromEntries(ids.map(v=>[v,[]]))
    for(const v of ids)for(const u of ids)if(v!==u&&rand()<.28)graph[v].push([u,Math.floor(rand()*6)])
    const d=Object.fromEntries(ids.map(v=>[v,v==='S'?0:Infinity]))
    for(let k=1;k<ids.length;k++)for(const [v,edges] of Object.entries(graph))for(const [u,w] of edges)d[u]=Math.min(d[u],d[v]+w)
    const trueH=Object.fromEntries(ids.map(v=>[v,v==='G'?0:Infinity]))
    // Synchronous reverse Bellman is intentionally separate from the search implementation.
    for(let k=1;k<ids.length;k++){const old={...trueH};for(const [v,edges] of Object.entries(graph))for(const [u,w] of edges)trueH[v]=Math.min(trueH[v],w+old[u])}
    const h=Object.fromEntries(ids.map(v=>[v,Number.isFinite(trueH[v])?Math.floor(rand()*(trueH[v]+1)):0]));h.G=0
    const end=last({graph,h,start:'S',goal:'G'})
    assert.notEqual(end.phase,'budget')
    if(Number.isFinite(d.G))assert.equal(end.result.cost,d.G)
    else assert.equal(end.phase,'failure')
  }
})
test('Input validation rejects malformed data without accepting executable input',()=>{
  assert.throws(()=>validateInformed({...example('weighted'),h:{}}))
  assert.throws(()=>validateInformed({...example('weighted'),h:{...example('weighted').h,G:1}}))
  assert.throws(()=>validateInformed({...example('weighted'),graph:{S:[['G',-1]],G:[]}}))
  assert.throws(()=>validatePuzzle([0,1,1,3,4,5,6,7,8]))
})
test('Puzzle excludes blank, has verified h=8/18, solution 26 and parity detection',()=>{
  const b=puzzleExamples[0].board
  assert.equal(puzzleHeuristic(b,'misplaced'),8);assert.equal(puzzleHeuristic(b),18)
  assert.deepEqual(puzzleParts(b).map(p=>p.distance),[3,1,2,2,2,3,3,2])
  const r=solvePuzzle(b);assert.equal(r.cost,26);assert.equal(r.path.length,27)
  assert.deepEqual(r.path.at(-1),puzzleGoal)
  for(let i=1;i<r.path.length;i++)assert.ok(puzzleNeighbors(r.path[i-1]).some(a=>a.join('')===r.path[i].join('')))
  assert.equal(solvePuzzle(puzzleExamples[3].board).status,'unsolvable')
  assert.equal(solvePuzzle(b,'zero',3).status,'budget')
})
test('Puzzle A* and all heuristic inequalities match independent breadth-first distances',()=>{
  const queue=[[...puzzleGoal]],distance=new Map([[puzzleGoal.join(''),0]])
  for(let i=0;i<queue.length;i++){
    const s=queue[i],d=distance.get(s.join(''))
    for(const t of puzzleNeighbors(s)){
      assert.ok(puzzleHeuristic(s)<=1+puzzleHeuristic(t))
      assert.ok(puzzleHeuristic(s,'misplaced')<=1+puzzleHeuristic(t,'misplaced'))
      if(d<9&&!distance.has(t.join(''))){distance.set(t.join(''),d+1);queue.push(t)}
    }
    assert.ok(puzzleHeuristic(s,'misplaced')<=puzzleHeuristic(s))
    assert.ok(puzzleHeuristic(s)<=d)
  }
  for(let i=0;i<queue.length;i+=19)for(const m of ['zero','misplaced','manhattan'])assert.equal(solvePuzzle(queue[i],m).cost,distance.get(queue[i].join('')))
})
