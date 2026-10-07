// Deterministic, deliberately small mathematical models used by MathLab.
export const mix = (a, b, theta) => a.map((x, i) => theta * x + (1 - theta) * b[i])
export const quadratic = ([x, y], kappa = 10) => (x*x + kappa*y*y)/2
export function dualCertificate(lambda, x = 1) {
  if (lambda < 0 || x > 1) throw new RangeError('Certificate requires lambda ≥ 0 and x ≤ 1')
  const primal = (x-2)**2, dual = lambda-lambda**2/4
  return { primal, dual, gap: primal-dual, minimizer: 2-lambda/2 }
}
export function optimizerTrace({ method = 'gd', rate = .15, kappa = 10, steps = 20, start = [2, 2], momentum = .8 } = {}) {
  let x = [...start], velocity = [0,0], sum = [0,0], m = [0,0], v = [0,0]
  const rows = [{ iteration: 0, x: [...x], value: quadratic(x,kappa), gradient: [x[0],kappa*x[1]], m: [...m], v: [...v], sum: [...sum] }]
  for (let t=1;t<=steps;t++) {
    const at = method==='nesterov' ? x.map((z,i)=>z+momentum*velocity[i]) : x
    const gradient = [at[0], kappa*at[1]]
    x=x.map((z,i)=>{
      const g=gradient[i]
      if (method==='newton') return z-g/(i===0?1:kappa)
      if (method==='momentum'||method==='nesterov') { velocity[i]=momentum*velocity[i]-rate*g; return z+velocity[i] }
      if (method==='adagrad') { sum[i]+=g*g; return z-rate*g/(Math.sqrt(sum[i])+1e-8) }
      if (method==='rmsprop') { v[i]=.9*v[i]+.1*g*g; return z-rate*g/(Math.sqrt(v[i])+1e-8) }
      if (method==='adam') {
        m[i]=.9*m[i]+.1*g; v[i]=.999*v[i]+.001*g*g
        return z-rate*(m[i]/(1-.9**t))/(Math.sqrt(v[i]/(1-.999**t))+1e-8)
      }
      return z-rate*g
    })
    rows.push({ iteration:t, x:[...x], value:quadratic(x,kappa), gradient:[...gradient], m:[...m], v:[...v], sum:[...sum] })
  }
  return rows
}
export const lpVertices = [[0,0],[2,0],[2,2],[0,4]]
export function solveSmallLP(c = [3,2]) {
  const values=lpVertices.map(p=>c[0]*p[0]+c[1]*p[1]), best=Math.max(...values)
  return { vertices:lpVertices.map((p,i)=>({ point:p,value:values[i] })), value:best, optimal:lpVertices.filter((_,i)=>Math.abs(values[i]-best)<1e-10) }
}
export const dag = { S:[['A',1],['B',4]], A:[['B',2],['T',5]], B:[['T',1]], T:[] }
export function bellmanTrace(graph = dag, order = ['T','B','A','S'], terminal = 'T', maximize = false) {
  const values = {}, actions = {}, rows=[]
  for (const node of order) {
    if (node===terminal) { values[node]=0; actions[node]=null }
    else {
      const candidates=graph[node].map(([to,cost])=>({ to,value:cost+values[to] }))
      if (!candidates.length || candidates.some(item=>!Number.isFinite(item.value))) throw new Error('Provide a reachable DAG in reverse topological order')
      const optimum=(maximize?Math.max:Math.min)(...candidates.map(c=>c.value)), selected=candidates.find(c=>c.value===optimum)
      values[node]=optimum; actions[node]=selected.to
    }
    rows.push({ node,values:{...values},actions:{...actions} })
  }
  return rows
}
