import {adversarialCode} from './adversarial-code.mjs'
export {adversarialCode}
export const adversarialExamples=[
 {id:'classic',title:'Ba nhánh Minimax · Giá trị 3',tree:[[3,12,8],[2,4,6],[14,5,2]]},
 {id:'small',title:'Cắt một lá · Giá trị 8',tree:[[10,8],[4,50]]},
 {id:'deep',title:'Cắt ở cả MAX và MIN · Giá trị 10',tree:[[[10,6],[100,8]],[[1,2],[20,4]]]},
 {id:'hidden',title:'Giá trị trả về chỉ là cận',tree:[[[10,6],[100,150]],[[1,2],[20,4]]]},
 {id:'equal',title:'Hòa điểm và cắt khi bằng nhau',tree:[[5,5],[5,9]]},
 {id:'negative',title:'Mọi lợi ích đều âm',tree:[[-3,-8],[-4,-2]]},
 {id:'horizon',title:'Ước lượng nông đảo lựa chọn',tree:[{eval:5,children:[-10,-8]},{eval:4,children:[1,2]}]},
 {id:'opponent',title:'An toàn hoặc kỳ vọng cao',tree:[[10,10],[9,100]]}
]
export function createGameTree(input){
 const nodes=[]
 function visit(t,id='R',depth=0,parent=null){
  if(depth>4||nodes.length>=45)throw Error('Bộ xem hỗ trợ tối đa 45 nút và 4 tầng hành động.')
  const leaf=typeof t==='number',list=Array.isArray(t)?t:t?.children
  if(leaf&&!Number.isFinite(t))throw Error('Lợi ích lá phải là số hữu hạn.')
  if(!leaf&&(!Array.isArray(list)||list.length<1||list.length>3))throw Error('Mỗi nút trong cần từ 1 đến 3 nút con.')
  const node={id,parent,depth,type:leaf?'LEAF':depth%2?'MIN':'MAX',utility:leaf?t:null,eval:leaf?t:Array.isArray(t)?0:t.eval??0,children:[]}
  if(!Number.isFinite(node.eval))throw Error('Điểm đánh giá phải là số hữu hạn.')
  nodes.push(node)
  if(!leaf)list.forEach((c,i)=>node.children.push(visit(c,id+(i+1),depth+1,id).id))
  return node
 }
 const root=visit(input);return {root:root.id,nodes}
}
export function exactGameValue(tree,id=tree.root,depth=Infinity){
 const n=tree.nodes.find(n=>n.id===id)
 if(n.type==='LEAF')return n.utility
 if(depth===0)return n.eval
 const values=n.children.map(c=>exactGameValue(tree,c,depth-1))
 return n.type==='MAX'?Math.max(...values):Math.min(...values)
}

// The executed generator is also the code displayed by AdversarialTreeLab.
export function* adversarialSearch(tree, pruning=true, depthLimit=Infinity, order='original'){
 const byId=new Map(tree.nodes.map(n=>[n.id,n]))
 const records={},stack=[],pruned=new Set(),evaluated=[]
 let visits=0,result=null
 const snap=(phase,id=null,child=null)=>({
  phase,id,child,visits,result:result?{...result}:null,
  records:Object.fromEntries(Object.entries(records).map(([k,v])=>[k,{...v}])),
  stack:stack.map(f=>({...f})),pruned:[...pruned],evaluated:[...evaluated]
 })
 const markPruned=id=>{
  pruned.add(id)
  for(const c of byId.get(id).children)markPruned(c)
 }
 function* search(id,alpha,beta,remaining){
  const node=byId.get(id),alphaIn=alpha,betaIn=beta
  const maximizing=node.type==='MAX'
  const frame={id,alpha,beta,value:maximizing?-Infinity:Infinity}
  stack.push(frame);visits++
  records[id]={status:'entered'}
  yield snap('enter',id)
  if(node.type==='LEAF'||remaining===0){
   const value=node.type==='LEAF'?node.utility:node.eval
   records[id]={status:node.type==='LEAF'?'terminal':'cutoff',value,bound:'exact'}
   evaluated.push(id);frame.value=value
   yield snap(node.type==='LEAF'?'terminal':'cutoff',id)
   stack.pop()
   return {value,move:null,bound:'exact'}
  }
  let value=maximizing?-Infinity:Infinity,move=null
  const intervals=[]
  let children=[...node.children]
  if(order==='reverse')children.reverse()
  for(let i=0;i<children.length;i++){
   const child=children[i]
   yield snap('choose',id,child)
   const answer=yield* search(child,alpha,beta,remaining-1)
   intervals.push({
    low:answer.bound==='upper'?-Infinity:answer.value,
    high:answer.bound==='lower'?Infinity:answer.value
   })
   if(move===null||(maximizing?answer.value>value:answer.value<value)){
    value=answer.value;move=child
   }
   if(pruning){
    if(maximizing)alpha=Math.max(alpha,value)
    else beta=Math.min(beta,value)
   }
   Object.assign(frame,{alpha,beta,value})
   const lows=intervals.map(x=>x.low),highs=intervals.map(x=>x.high)
   const pending=i+1<children.length
   const low=maximizing?Math.max(...lows):pending?-Infinity:Math.min(...lows)
   const high=maximizing?(pending?Infinity:Math.max(...highs)):Math.min(...highs)
   records[id]={status:'partial',value,move,bound:'interval',low,high}
   yield snap('update',id,child)
   if(pruning&&alpha>=beta){
    for(const c of children.slice(i+1))markPruned(c)
    if(i+1<children.length)yield snap('prune',id)
    break
   }
  }
  const bound=!pruning?'exact':value<=alphaIn?'upper':value>=betaIn?'lower':'exact'
  records[id]={status:'returned',value,move,bound}
  yield snap('return',id)
  stack.pop()
  return {value,move,bound}
 }
 result=yield* search(tree.root,-Infinity,Infinity,depthLimit)
 yield snap('complete',tree.root)
}
export function traceAdversarial(tree,mode='alphabeta',depth=Infinity,order='original',budget=1800){
 if(!['minimax','alphabeta'].includes(mode)||!['original','reverse'].includes(order)||!(depth===Infinity||Number.isInteger(depth)&&depth>=0&&depth<=4))throw Error('Cài đặt tìm kiếm không hợp lệ.')
 const frames=[]
 for(const f of adversarialSearch(tree,mode==='alphabeta',depth,order)){
  frames.push(f)
  if(frames.length>=budget){frames.push({...f,phase:'budget',result:null});break}
 }
 return frames
}
export function adversarialLine(phase){
 const needle={enter:"yield snap('enter'",terminal:"yield snap(node.type",cutoff:"yield snap(node.type",choose:"yield snap('choose'",update:'Object.assign(frame',prune:'for(const c of children.slice',return:'records[id]={status:\'returned\'',complete:'result=yield* search',budget:'for(let i=0;'}[phase]
 return Math.max(0,adversarialCode.findIndex(s=>s.includes(needle||'yield snap')))
}
