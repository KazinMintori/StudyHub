export const puzzleGoal=[0,1,2,3,4,5,6,7,8]
export const puzzleExamples=[
  {id:'source',title:'Ví dụ trong slide · Manhattan 18',board:[7,2,4,5,0,6,8,3,1]},
  {id:'small',title:'Bài nhỏ để tự chạy',board:[1,4,2,3,0,5,6,7,8]},
  {id:'goal',title:'Đã ở đích',board:[...puzzleGoal]},
  {id:'impossible',title:'Đổi chỗ hai ô số · Không giải được',board:[0,2,1,3,4,5,6,7,8]}
]
export function validatePuzzle(board){if(!Array.isArray(board)||board.length!==9||new Set(board).size!==9||board.some(v=>!Number.isInteger(v)||v<0||v>8))throw Error('Cần đúng 9 số từ 0 đến 8, mỗi số xuất hiện một lần. Số 0 là ô trống.');return true}
export function puzzleParts(board){return Array.from({length:8},(_,i)=>{const tile=i+1,pos=board.indexOf(tile),row=Math.floor(pos/3),col=pos%3,goalRow=Math.floor(tile/3),goalCol=tile%3;return {tile,row,col,goalRow,goalCol,vertical:Math.abs(row-goalRow),horizontal:Math.abs(col-goalCol),distance:Math.abs(row-goalRow)+Math.abs(col-goalCol),misplaced:pos===tile?0:1}})}
export function puzzleHeuristic(board,mode='manhattan'){if(mode==='zero')return 0;return puzzleParts(board).reduce((s,p)=>s+(mode==='misplaced'?p.misplaced:p.distance),0)}
export function puzzleSolvable(board){const a=board.filter(Boolean);let inversions=0;for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++)if(a[i]>a[j])inversions++;return inversions%2===0}
export function puzzleNeighbors(board){const blank=board.indexOf(0),r=Math.floor(blank/3),c=blank%3,out=[];for(const [dr,dc] of [[-1,0],[0,1],[1,0],[0,-1]]){const nr=r+dr,nc=c+dc;if(nr<0||nr>2||nc<0||nc>2)continue;const n=[...board],i=nr*3+nc;[n[blank],n[i]]=[n[i],n[blank]];out.push(n)}return out}
// Stable binary min-heap: lower f, then earlier insertion.
class MinHeap{
  data=[]
  less(a,b){return a.f<b.f||(a.f===b.f&&a.id<b.id)}
  push(n){const a=this.data;a.push(n);let i=a.length-1;while(i>0){const p=(i-1)>>1;if(!this.less(a[i],a[p]))break;[a[i],a[p]]=[a[p],a[i]];i=p}}
  pop(){const a=this.data,first=a[0],last=a.pop();if(a.length){a[0]=last;let i=0;while(true){let j=i,left=i*2+1,right=left+1;if(left<a.length&&this.less(a[left],a[j]))j=left;if(right<a.length&&this.less(a[right],a[j]))j=right;if(j===i)break;[a[i],a[j]]=[a[j],a[i]];i=j}}return first}
}
export function solvePuzzle(board,mode='manhattan',budget=20000){
  validatePuzzle(board)
  if(!['zero','misplaced','manhattan'].includes(mode))throw Error('Heuristic không hợp lệ.')
  if(!puzzleSolvable(board))return {status:'unsolvable',path:[],expanded:0,generated:0}
  const goal=puzzleGoal.join(''),start=board.join(''),best=new Map([[start,0]]),parents=new Map(),boards=new Map([[start,[...board]]]),q=new MinHeap()
  let serial=0,expanded=0,generated=1,peak=1
  q.push({key:start,g:0,f:puzzleHeuristic(board,mode),id:serial++})
  while(q.data.length){
    const n=q.pop();if(n.g!==best.get(n.key))continue
    if(n.key===goal){const path=[];for(let k=n.key;k!==undefined;k=parents.get(k))path.unshift(boards.get(k));return {status:'success',path,cost:n.g,expanded,generated,peak}}
    if(expanded>=budget)return {status:'budget',path:[],expanded,generated,peak}
    expanded++
    for(const next of puzzleNeighbors(boards.get(n.key))){
      const key=next.join(''),g=n.g+1
      if(g>=(best.get(key)??Infinity))continue
      best.set(key,g);parents.set(key,n.key);boards.set(key,next)
      q.push({key,g,f:g+puzzleHeuristic(next,mode),id:serial++});generated++
    }
    peak=Math.max(peak,q.data.length)
  }
  return {status:'failure',path:[],expanded,generated,peak}
}
