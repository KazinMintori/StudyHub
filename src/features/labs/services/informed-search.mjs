import { informedCode } from './informed-search-code.mjs'
export { informedCode }

export const informedExamples = [
  { id:'weighted', title:'Greedy chọn 8, A* chọn 7', graph:{S:[['A',1],['B',4]],A:[['B',2],['C',5]],B:[['C',1]],C:[['G',3]],G:[]}, h:{S:5,A:4,B:3,C:2,G:0}, start:'S',goal:'G' },
  { id:'slides', title:'Ví dụ A* trong slide', graph:{S:[['a',1]],a:[['b',1],['d',3],['e',8]],b:[['c',1]],c:[],d:[['G',2]],e:[['d',1]],G:[]}, h:{S:6,a:5,b:6,c:7,d:2,e:1,G:0}, start:'S',goal:'G' },
  { id:'early', title:'Đích xuất hiện trước lời giải tốt', graph:{S:[['A',2],['B',2]],A:[['G',2]],B:[['G',3]],G:[]}, h:{S:3,A:2,B:1,G:0},start:'S',goal:'G' },
  { id:'overestimate', title:'Ước lượng quá cao', graph:{S:[['A',1],['G',5]],A:[['G',3]],G:[]},h:{S:7,A:6,G:0},start:'S',goal:'G' },
  { id:'reopen', title:'Chấp nhận được nhưng chưa nhất quán', graph:{S:[['A',1],['B',1]],A:[['C',1]],B:[['C',2]],C:[['G',3]],G:[]},h:{S:2,A:4,B:1,C:1,G:0},start:'S',goal:'G' },
  { id:'consistent', title:'Cùng đồ thị, heuristic nhất quán', graph:{S:[['A',1],['B',1]],A:[['C',1]],B:[['C',2]],C:[['G',3]],G:[]},h:{S:2,A:4,B:1,C:3,G:0},start:'S',goal:'G' },
  { id:'unreachable', title:'Chu trình và đích không tới được', graph:{S:[['A',0]],A:[['S',0],['B',1]],B:[],G:[]},h:{S:2,A:1,B:1,G:0},start:'S',goal:'G' },
  { id:'initial', title:'Trạng thái đầu đã là đích', graph:{S:[['A',1]],A:[]},h:{S:0,A:1},start:'S',goal:'S' }
]

// This generator is both the algorithm and the source shown in the lab.
export function* informedSearch(graph, h, start, goal, mode='astar', reopen=true) {
  const priority = n => mode === 'ucs' ? n.g
    : mode === 'greedy' ? n.h : n.g + n.h
  const nodes = [{
    id:0, state:start, g:0, h:h[start], parent:null, depth:0
  }]
  let frontier = [0]
  const best = new Map([[start,0]])
  const closed = new Set()
  const pathTo = id => {
    const path = []
    for (let n=nodes[id]; n; n=nodes[n.parent]) {
      path.unshift(n.state)
    }
    return path
  }
  const snap = (phase,current=null,edge=null,result=null) => ({
    phase, current, edge, result,
    frontier:frontier.map(id=>({
      ...nodes[id], f:priority(nodes[id])
    })),
    nodes:nodes.map(n=>({...n,f:priority(n)})),
    closed:[...closed],
    best:Object.fromEntries(best),
    path:current===null ? [] : pathTo(current)
  })
  yield snap('start')
  while (frontier.length) {
    frontier.sort((a,b)=>priority(nodes[a])-priority(nodes[b]) || a-b)
    const id = frontier.shift()
    const node = nodes[id]
    yield snap('take',id)
    if (node.g !== best.get(node.state) || closed.has(node.state)) {
      yield snap('stale',id)
      continue
    }
    if (node.state === goal) {
      yield snap('success',id,null,{
        path:pathTo(id), cost:node.g, depth:node.depth
      })
      return
    }
    closed.add(node.state)
    yield snap('expand',id)
    for (const [next,cost] of graph[node.state]) {
      const g = node.g + cost
      yield snap('consider',id,[node.state,next])
      if (g >= (best.get(next) ?? Infinity)) {
        yield snap('skip',id,[node.state,next])
        continue
      }
      if (closed.has(next) && (mode === 'greedy' || !reopen)) {
        yield snap('blocked',id,[node.state,next])
        continue
      }
      best.set(next,g)
      const wasClosed = closed.delete(next)
      const child = {
        id:nodes.length, state:next, g, h:h[next],
        parent:id, depth:node.depth+1
      }
      nodes.push(child)
      frontier.push(child.id)
      yield snap(wasClosed?'reopen':'insert',id,[node.state,next])
    }
  }
  yield snap('failure')
}

export function traceInformed(example, mode='astar', reopen=true, budget=1200) {
  if(!['ucs','greedy','astar'].includes(mode))throw Error('Chiến lược không hợp lệ.')
  validateInformed(example)
  const frames=[]
  for(const frame of informedSearch(example.graph,example.h,example.start,example.goal,mode,reopen)) {
    frames.push(frame)
    if(frames.length>=budget){frames.push({...frame,phase:'budget',result:null});break}
  }
  return frames
}

export function validateInformed({graph,h,start,goal}) {
  if(!graph || typeof graph!=='object' || Array.isArray(graph))throw Error('Đồ thị phải là một đối tượng danh sách kề.')
  const ids=Object.keys(graph)
  if(ids.length<1 || ids.length>8 || !ids.includes(start) || !ids.includes(goal))throw Error('Cần từ 1 đến 8 trạng thái, có trạng thái đầu và đích.')
  if(ids.some(v=>!/^\w{1,4}$/.test(v)))throw Error('Tên trạng thái gồm 1–4 chữ cái Latin, chữ số hoặc dấu gạch dưới.')
  if(!h || typeof h!=='object' || ids.some(v=>!Number.isFinite(h[v]) || h[v]<0 || h[v]>1000000))throw Error('Mỗi trạng thái cần một heuristic không âm, hữu hạn và không quá 1.000.000.')
  if(h[goal]!==0)throw Error('Heuristic tại đích phải bằng 0 trong mô hình này.')
  for(const [v,edges] of Object.entries(graph)) {
    if(!Array.isArray(edges) || edges.length>8)throw Error('Mỗi danh sách kề chứa tối đa 8 cạnh.')
    for(const e of edges)if(!Array.isArray(e)||e.length!==2||!ids.includes(e[0])||e[0]===v||!Number.isFinite(e[1])||e[1]<0||e[1]>1000000)throw Error('Cạnh cần đỉnh tới hợp lệ khác đỉnh nguồn và chi phí từ 0 đến 1.000.000.')
  }
  return true
}

// Independent reverse Bellman relaxation: diagnostic only, never guides search.
export function inspectHeuristic({graph,h,goal}) {
  const ids=Object.keys(graph), exact=Object.fromEntries(ids.map(v=>[v,v===goal?0:Infinity]))
  for(let i=1;i<ids.length;i++)for(const [v,edges] of Object.entries(graph))for(const [u,c] of edges)exact[v]=Math.min(exact[v],c+exact[u])
  const over=ids.filter(v=>h[v]>exact[v])
  const violations=Object.entries(graph).flatMap(([v,edges])=>edges.filter(([u,c])=>h[v]>c+h[u]).map(([u,c])=>({from:v,to:u,cost:c,left:h[v],right:c+h[u]})))
  return {exact,over,violations,admissible:over.length===0,consistent:violations.length===0&&h[goal]===0}
}

export function informedLine(phase) {
  const needles={start:"yield snap('start')",take:"yield snap('take'",stale:'node.g !== best',success:'node.state === goal',expand:'closed.add',consider:"yield snap('consider'",skip:'g >= (best',blocked:'closed.has(next)',insert:'frontier.push',reopen:'const wasClosed',failure:"yield snap('failure')",budget:'while (frontier.length)'}
  return Math.max(0,informedCode.findIndex(s=>s.includes(needles[phase]||'yield snap')))
}
