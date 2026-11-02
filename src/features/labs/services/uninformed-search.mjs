import { searchCode, idsCode } from './uninformed-search-code.mjs'
export { searchCode, idsCode }

export const searchExamples = [
  { id: 'weighted', title: 'Ít bước khác ít chi phí', graph: { S: [['A',1],['B',4]], A: [['B',2],['C',5]], B: [['C',1]], C: [['G',3]], G: [] }, start:'S', goal:'G' },
  { id: 'unit', title: 'Mọi cạnh cùng chi phí', graph: { S: [['A',1],['B',1]], A: [['B',1],['C',1]], B: [['C',1]], C: [['G',1]], G: [] }, start:'S', goal:'G' },
  { id: 'early', title: 'Đích đắt xuất hiện sớm', graph: { S: [['G',10],['A',1]], A: [['G',1]], G: [] }, start:'S', goal:'G' },
  { id: 'beyond', title: 'Còn nhánh sau khi tới đích', graph: { S:[['A',1],['G',2],['B',7]], A:[['G',1]], B:[['C',1]], C:[], G:[] }, start:'S', goal:'G' },
  { id: 'cycle', title: 'Có chu trình', graph: { S:[['A',1]], A:[['S',1],['B',1]], B:[['A',1],['G',1]], G:[] }, start:'S', goal:'G' },
  { id: 'unreachable', title: 'Không có đường tới đích', graph: { S:[['A',1]], A:[['S',1],['B',1]], B:[], G:[] }, start:'S', goal:'G' },
  { id: 'initial', title: 'Bắt đầu đã là đích', graph: { S:[['A',1]], A:[] }, start:'S', goal:'S' }
]

// The displayed program is the executed generator, with instrumentation hidden
// only at the UI boundary. Every yielded snapshot is a real operation.
export function* graphSearch(graph, start, goal, mode) {
  const weighted = mode === 'ucs' || mode === 'dijkstra'
  let serial = 0
  const nodes = [{ id:serial++, state:start, parent:null, g:0, depth:0 }]
  let frontier = [0]
  const discovered = new Set([start]), settled = new Set(), best = new Map([[start,0]])
  const pathTo = id => { const path=[]; for(let n=nodes[id];n;n=nodes[n.parent])path.unshift(n.state); return path }
  const snap = (phase, current=null, edge=null, result=null) => ({ phase, current, edge, result, frontier:frontier.map(id=>({...nodes[id]})), settled:[...settled], discovered:[...discovered], best:Object.fromEntries(best), nodes:nodes.map(n=>({...n})), path:current===null?[]:pathTo(current), limit:null })
  yield snap('start')
  while (frontier.length) {
    if (weighted) frontier.sort((a,b)=>nodes[a].g-nodes[b].g || a-b)
    const id = mode === 'dfs' ? frontier.pop() : frontier.shift()
    const node = nodes[id]
    yield snap('take', id)
    if (weighted && (node.g > best.get(node.state) || settled.has(node.state))) { yield snap('stale',id); continue }
    if (node.state === goal && mode !== 'dijkstra') { yield snap('success',id,null,{path:pathTo(id),cost:node.g,depth:node.depth}); return }
    settled.add(node.state)
    yield snap('expand',id)
    const edges = [...graph[node.state]]
    if (mode === 'dfs') edges.reverse()
    for (const [next, weight] of edges) {
      const g = node.g + weight
      yield snap('consider',id,[node.state,next])
      if (weighted ? g >= (best.get(next) ?? Infinity) : discovered.has(next)) { yield snap('skip',id,[node.state,next]); continue }
      discovered.add(next)
      best.set(next,g)
      const child = { id:serial++, state:next, parent:id, g, depth:node.depth+1 }
      nodes.push(child)
      frontier.push(child.id)
      yield snap('insert',id,[node.state,next])
    }
  }
  if (mode === 'dijkstra') {
    const target = nodes.filter(n=>n.state===goal && n.g===best.get(goal))[0]
    const distances = Object.fromEntries(Object.keys(graph).map(v=>[v,best.get(v)??Infinity]))
    yield snap('complete',target?.id??null,null,{path:target?pathTo(target.id):[],cost:target?.g??Infinity,depth:target?.depth??null,distances})
  } else yield snap('failure')
}

export function* iterativeSearch(graph, start, goal) {
  let serial=0
  const nodes=[]
  for(let limit=0;limit<Object.keys(graph).length;limit++) {
    const root={id:serial++,state:start,parent:null,g:0,depth:0,path:[start]}
    nodes.push(root)
    const frontier=[root], expanded=[]
    let cutoff=false
    const snap=(phase,node=null,edge=null,result=null)=>({phase,current:node?.id??null,edge,result,frontier:frontier.map(n=>({...n})),settled:[...expanded],discovered:[],best:{},nodes:nodes.map(n=>({...n})),path:node?.path??[],limit})
    yield snap('iteration')
    while(frontier.length) {
      const node=frontier.pop()
      yield snap('take',node)
      if(node.state===goal){yield snap('success',node,null,{path:node.path,cost:node.g,depth:node.depth});return}
      const children=graph[node.state].filter(([v])=>!node.path.includes(v))
      if(node.depth===limit){if(children.length){cutoff=true;yield snap('cutoff',node)}continue}
      expanded.push(node.state)
      yield snap('expand',node)
      for(const [next,weight] of [...children].reverse()){
        const child={id:serial++,state:next,parent:node.id,g:node.g+weight,depth:node.depth+1,path:[...node.path,next]}
        nodes.push(child);frontier.push(child)
        yield snap('insert',node,[node.state,next])
      }
    }
    if(!cutoff){yield snap('failure');return}
  }
  yield {phase:'failure',current:null,edge:null,result:null,frontier:[],settled:[],discovered:[],best:{},nodes,path:[],limit:Object.keys(graph).length-1}
}

export function traceUninformed(graph, start, goal, mode='bfs') {
  if(!['bfs','dfs','ucs','ids','dijkstra'].includes(mode))throw Error('Chiến lược không hợp lệ')
  if(!Object.hasOwn(graph,start)||!Object.hasOwn(graph,goal))throw Error('Thiếu trạng thái đầu hoặc đích')
  for(const edges of Object.values(graph))for(const [v,w] of edges)if(!Object.hasOwn(graph,v)||!Number.isFinite(w)||w<0)throw Error('Cạnh phải tới đỉnh đã khai báo và có chi phí không âm')
  const frames=[]
  for(const frame of (mode==='ids'?iterativeSearch(graph,start,goal):graphSearch(graph,start,goal,mode))){
    frames.push(frame)
    if(frames.length>=1000 && !['success','failure','complete'].includes(frame.phase)){frames.push({...frame,phase:'budget',result:null});break}
  }
  return frames
}

export function activeSearchLine(phase,mode) {
  const lines=mode==='ids'?idsCode:searchCode
  const needle={start:'let frontier = [0]',iteration:'for(let limit=0',take:mode==='ids'?'const node=frontier.pop()':'const id = mode',stale:'if (weighted &&',success:mode==='ids'?'if(node.state===goal)':'if (node.state === goal',expand:mode==='ids'?'expanded.push(node.state)':'settled.add(node.state)',consider:'const g = node.g + weight',skip:'if (weighted ?',insert:mode==='ids'?'nodes.push(child);frontier.push(child)':'frontier.push(child.id)',cutoff:'if(node.depth===limit)',complete:'const distances = Object.fromEntries',failure:"yield snap('failure'"}[phase]
  return Math.max(0,lines.findIndex(line=>line.includes(needle)))
}
