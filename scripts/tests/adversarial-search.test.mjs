import test from 'node:test'
import assert from 'node:assert/strict'
import {readFile} from 'node:fs/promises'
import {adversarialExamples,createGameTree,exactGameValue,adversarialSearch,adversarialCode,traceAdversarial} from '../../src/features/labs/services/adversarial-search.mjs'
import {winningLines,ticTacToeTerminal,ticTacToeEvaluate,ticTacToeExamples,analyzeTicTacToe,reachableTicTacToe,validateTicTacToe} from '../../src/features/labs/services/tic-tac-toe.mjs'
import {ticTacToeCode} from '../../src/features/labs/services/tic-tac-toe-code.mjs'
const get=id=>createGameTree(adversarialExamples.find(e=>e.id===id).tree)
test('Executed code and displayed source are identical',()=>assert.deepEqual(adversarialCode,adversarialSearch.toString().split('\n')))
test('Displayed tic-tac-toe code matches the executable module',async()=>assert.equal(ticTacToeCode.join('\n'),await readFile(new URL('../../src/features/labs/services/tic-tac-toe.mjs',import.meta.url),'utf8')))
test('Source trees preserve root values and show genuine pruning counts',()=>{
 for(const [id,value,mm,ab] of [['classic',3,9,7],['small',8,4,3],['deep',10,8,5],['hidden',10,8,5],['equal',5,4,3],['negative',-4,4,4]]){
  const tree=get(id),m=traceAdversarial(tree,'minimax').at(-1),a=traceAdversarial(tree).at(-1)
  assert.equal(m.result.value,value);assert.equal(a.result.value,value);assert.equal(m.evaluated.length,mm);assert.equal(a.evaluated.length,ab)
 }
 const f=traceAdversarial(get('hidden')).at(-1)
 assert.deepEqual(f.records.R12,{status:'returned',value:100,move:'R121',bound:'lower'})
 assert.equal(exactGameValue(get('hidden'),'R12'),150)
 assert.ok(f.pruned.includes('R122'));assert.ok(!f.records.R122)
})
test('Cutoff estimates are distinct from terminal utility and can reverse action',()=>{
 const t=get('horizon'),one=traceAdversarial(t,'alphabeta',1).at(-1),two=traceAdversarial(t,'alphabeta',2).at(-1)
 assert.equal(one.result.move,'R1');assert.equal(one.result.value,5)
 assert.equal(two.result.move,'R2');assert.equal(two.result.value,1)
 assert.equal(one.records.R1.status,'cutoff');assert.equal(two.records.R11.status,'terminal')
 const terminal=createGameTree(-8);assert.equal(traceAdversarial(terminal,'alphabeta',0).at(-1).result.value,-8)
 assert.equal(traceAdversarial(t,'alphabeta',Infinity,'original',3).at(-1).phase,'budget')
})
test('Random trees match independent recursive oracle, and every displayed bound is valid',()=>{
 let seed=183;const rand=()=>{seed=(seed*1664525+1013904223)>>>0;return seed/2**32}
 const build=(d)=>d===0||rand()<.2?Math.floor(rand()*41)-20:Array.from({length:rand()<.6?2:3},()=>build(d-1))
 const oracle=(x,max=true,d=Infinity)=>typeof x==='number'?x:d===0?0:(max?Math.max:Math.min)(...x.map(c=>oracle(c,!max,d-1)))
 for(let k=0;k<150;k++){
  let raw=build(3),tree
  try{tree=createGameTree(raw)}catch{continue}
  for(const order of ['original','reverse'])for(const depth of [0,1,2,Infinity]){
   const frames=traceAdversarial(tree,'alphabeta',depth,order),end=frames.at(-1)
   assert.equal(end.result.value,oracle(raw,true,depth))
   for(const f of frames)for(const [id,r] of Object.entries(f.records)){
    if(r.value===undefined)continue
    const n=tree.nodes.find(n=>n.id===id),remaining=depth===Infinity?Infinity:depth-n.depth,truth=exactGameValue(tree,id,remaining)
    if(r.bound==='exact')assert.equal(r.value,truth)
    if(r.bound==='lower')assert.ok(r.value<=truth)
    if(r.bound==='upper')assert.ok(r.value>=truth)
    if(r.bound==='interval')assert.ok(r.low<=truth&&truth<=r.high)
   }
   for(const id of end.pruned)assert.ok(!end.records[id])
  }
 }
})
test('Snapshots are immutable and malformed trees are rejected',()=>{
 const f=traceAdversarial(get('deep'));assert.deepEqual(f[0].pruned,[]);assert.equal(Object.keys(f[0].records).length,1)
 assert.throws(()=>createGameTree([]));assert.throws(()=>createGameTree([NaN,2]));assert.throws(()=>createGameTree([1,2,3,4]))
})
// Independent retrograde oracle: No production terminal/evaluation routines.
const memo=new Map()
function oracleBoard(b){
 const key=b.join('');if(memo.has(key))return memo.get(key)
 const lines=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
 for(const [i,j,k]of lines)if(b[i]!=='.'&&b[i]===b[j]&&b[j]===b[k])return b[i]==='X'?100:-100
 if(!b.includes('.'))return 0
 const x=b.filter(v=>v==='X').length,o=b.filter(v=>v==='O').length,values=[]
 for(let i=0;i<9;i++)if(b[i]==='.'){const a=[...b];a[i]=x===o?'X':'O';values.push(oracleBoard(a))}
 const v=x===o?Math.max(...values):Math.min(...values);memo.set(key,v);return v
}
test('All 5478 reachable tic-tac-toe boards agree with an independent game oracle',()=>{
 const states=reachableTicTacToe();assert.equal(states.size,5478)
 let terminal=0
 for(const b of states.values()){
  const actual=analyzeTicTacToe(b),expected=oracleBoard(b.map(v=>v||'.'))
  assert.equal(actual.value,expected)
  if(actual.terminal.done){terminal++;assert.equal(actual.bestMove,null)}
  else{
   assert.equal(b[actual.bestMove],'')
   assert.ok(actual.moves.some(m=>m.move===actual.bestMove&&m.value===expected))
  }
 }
 assert.equal(terminal,958)
})
test('Minimax and alpha–beta score every root action equally at multiple depths',()=>{
 const boards=[...reachableTicTacToe().values()]
 for(let i=0;i<boards.length;i+=53)for(const d of [1,2,9]){
  const a=analyzeTicTacToe(boards[i],'alphabeta',d),m=analyzeTicTacToe(boards[i],'minimax',d)
  assert.deepEqual(a.moves,m.moves);assert.equal(a.value,m.value);assert.equal(a.bestMove,m.bestMove)
 }
 const block=ticTacToeExamples.find(e=>e.id==='block');assert.equal(analyzeTicTacToe(block.board).bestMove,2)
 const win=ticTacToeExamples.find(e=>e.id==='win');assert.equal(analyzeTicTacToe(win.board).bestMove,2)
 assert.equal(ticTacToeEvaluate(['X','X','X','O','O','','','',''],[0,0]),100)
 assert.throws(()=>validateTicTacToe(['O','','','','','','','','']))
 assert.throws(()=>validateTicTacToe(['X','X','X','O','O','O','','','']))
})
