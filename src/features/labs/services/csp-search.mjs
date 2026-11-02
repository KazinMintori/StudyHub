const copyDomains = domains => Object.fromEntries(Object.entries(domains).map(([k, v]) => [k, v.slice()]))
export const australiaEdges = [['WA', 'NT'], ['WA', 'SA'], ['NT', 'SA'], ['NT', 'Q'], ['SA', 'Q'], ['SA', 'NSW'], ['SA', 'V'], ['Q', 'NSW'], ['NSW', 'V']]
export function colorCsp(variables, edges, colors = ['Đỏ', 'Lá', 'Lam']) {
  return { variables, domains: Object.fromEntries(variables.map(v => [v, colors.slice()])), constraints: edges.map(([a, b]) => ({ a, b, relation: 'ne' })) }
}
export function queenCsp(n = 4) {
  return { variables: Array.from({ length: n }, (_, i) => `Q${i + 1}`), domains: Object.fromEntries(Array.from({ length: n }, (_, i) => [`Q${i + 1}`, Array.from({ length: n }, (_, j) => j + 1)])), constraints: Array.from({ length: n }, (_, i) => Array.from({ length: n - i - 1 }, (_, k) => ({ a: `Q${i + 1}`, b: `Q${i + k + 2}`, relation: 'queen', distance: k + 1 }))).flat() }
}
export const cspPresets = {
  australia: { title: 'Tô màu bản đồ Úc', create: () => colorCsp(['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T'], australiaEdges) },
  triangle: { title: 'Tam giác hai màu vô nghiệm', create: () => colorCsp(['A', 'B', 'C'], [['A', 'B'], ['B', 'C'], ['A', 'C']], ['Đỏ', 'Lam']) },
  forward: { title: 'FC chưa thấy mâu thuẫn sau A = Đỏ', create: () => { const p = colorCsp(['A', 'B', 'C'], [['A', 'B'], ['B', 'C'], ['A', 'C']], ['Đỏ', 'Lam']); p.domains.A = ['Đỏ']; return p } },
  chain: { title: 'Chuỗi A < B < C', create: () => ({ variables: ['A', 'B', 'C'], domains: { A: [1, 2, 3], B: [1, 2, 3], C: [1, 2, 3] }, constraints: [{ a: 'A', b: 'B', relation: 'lt' }, { a: 'B', b: 'C', relation: 'lt' }] }) },
  queens: { title: 'Bốn quân hậu', create: () => queenCsp(4) },
  crossword: { title: 'Ô chữ ba vị trí', create: () => ({ variables: ['N1','D1','N2'], domains: { N1: ['BAN','CAN','LAM'], D1: ['BAO','CAO','LAM'], N2: ['NON','NAM','MAN'] }, constraints: [{ a: 'N1', b: 'D1', relation: 'letter', positions: [0,0] }, { a: 'D1', b: 'N2', relation: 'letter', positions: [2,1] }] }) },
  tree: { title: 'Cây sáu biến', create: () => colorCsp(['A', 'B', 'C', 'D', 'E', 'F'], [['A', 'B'], ['B', 'C'], ['B', 'D'], ['D', 'E'], ['D', 'F']], [1, 2]) }
}
export function validateCsp(problem) {
  const { variables, domains, constraints } = problem || {}
  if (!Array.isArray(variables) || !variables.length || variables.length > 25 || new Set(variables).size !== variables.length || variables.some(x => typeof x !== 'string' || !/^[A-Za-z][A-Za-z0-9_]{0,11}$/.test(x))) throw Error('Cần 1 đến 25 tên biến khác nhau, bắt đầu bằng chữ và dài tối đa 12 ký tự.')
  if (!domains || variables.some(v => !Array.isArray(domains[v]) || domains[v].length > 9 || new Set(domains[v]).size !== domains[v].length || domains[v].some(x => !(typeof x === 'string' && x.length <= 20 || typeof x === 'number' && Number.isFinite(x))))) throw Error('Mỗi miền có tối đa 9 giá trị chuỗi hoặc số hữu hạn khác nhau.')
  if (!Array.isArray(constraints) || constraints.length > 120 || constraints.some(c => !variables.includes(c.a) || !variables.includes(c.b) || c.a === c.b || !['ne', 'lt', 'eq', 'queen', 'letter'].includes(c.relation) || ['lt','queen'].includes(c.relation) && [...domains[c.a],...domains[c.b]].some(x=>typeof x!=='number') || c.relation === 'queen' && (!Number.isInteger(c.distance) || c.distance < 1) || c.relation === 'letter' && (!Array.isArray(c.positions) || c.positions.length !== 2 || c.positions.some((x,i) => !Number.isInteger(x) || x < 0 || domains[i===0?c.a:c.b].some(v=>typeof v !== 'string' || x>=v.length))))) throw Error('Ràng buộc nhị phân không hợp lệ. lt và queen cần miền số. letter cần hai chỉ số ký tự hợp lệ.')
  return { variables: variables.slice(), domains: copyDomains(Object.fromEntries(variables.map(v => [v, domains[v]]))), constraints: constraints.map(c => ({ ...c })) }
}
export function satisfies(c, a, b) {
  if (c.relation === 'letter') return a[c.positions[0]] === b[c.positions[1]]
  if (c.relation === 'lt') return a < b
  if (c.relation === 'eq') return a === b
  if (c.relation === 'queen') return a !== b && Math.abs(a - b) !== c.distance
  return a !== b
}
export function compatible(problem, a, av, b, bv) {
  return problem.constraints.every(c => c.a === a && c.b === b ? satisfies(c, av, bv) : c.a === b && c.b === a ? satisfies(c, bv, av) : true)
}
export function neighborsOf(problem, v) {
  return problem.variables.filter(w => w !== v && problem.constraints.some(c => c.a === v && c.b === w || c.b === v && c.a === w))
}
export function isSolution(problem, assignment) {
  return problem.variables.every(v => Object.hasOwn(assignment, v) && problem.domains[v].includes(assignment[v])) && problem.constraints.every(c => satisfies(c, assignment[c.a], assignment[c.b]))
}
export function revise(problem, domains, a, b) {
  const removed = domains[a].filter(av => !domains[b].some(bv => compatible(problem, a, av, b, bv)))
  domains[a] = domains[a].filter(x => !removed.includes(x))
  return removed
}
export function* ac3Steps(problem, options = {}) {
  const p = validateCsp(problem), domains = options.domains || copyDomains(p.domains)
  let queue = (options.queue || p.variables.flatMap(a => neighborsOf(p, a).map(b => [a, b]))).map(x => x.slice()), revisions = 0
  const snap = (phase, extra = {}) => ({ phase, domains: copyDomains(domains), queue: queue.map(x => x.slice()), revisions, ...extra })
  yield snap('start')
  if (p.variables.some(v => !domains[v].length)) { yield snap('failure'); return false }
  while (queue.length) {
    const [a, b] = queue.shift()
    yield snap('arc', { arc: [a, b] })
    const removed = revise(p, domains, a, b); revisions++
    yield snap('revise', { arc: [a, b], removed })
    if (removed.length) {
      if (!domains[a].length) { yield snap('failure', { arc: [a, b], removed }); return false }
      for (const k of neighborsOf(p, a)) if (k !== b && !queue.some(([x, y]) => x === k && y === a)) queue.push([k, a])
      yield snap('enqueue', { arc: [a, b], removed })
    }
  }
  yield snap('consistent')
  return true
}
export function* backtrackingSteps(problem, { filtering = 'mac', variableOrder = 'mrv', valueOrder = 'lcv', budget = 2000 } = {}) {
  const p = validateCsp(problem)
  if (!['none', 'fc', 'mac'].includes(filtering) || !['fixed', 'mrv'].includes(variableOrder) || !['fixed', 'lcv'].includes(valueOrder) || !Number.isInteger(budget) || budget < 1 || budget > 10000) throw Error('Tham số quay lui không hợp lệ.')
  let domains = copyDomains(p.domains), assignment = {}, attempts = 0, prunes = 0, revisions = 0, interrupted = false
  const snap = (phase, extra = {}) => ({ phase, domains: copyDomains(domains), assignment: { ...assignment }, attempts, prunes, revisions, depth: Object.keys(assignment).length, ...extra })
  const legal = v => domains[v].filter(value => Object.entries(assignment).every(([a, av]) => compatible(p, v, value, a, av)))
  yield snap('start')
  function* search() {
    if (p.variables.every(v => Object.hasOwn(assignment, v))) { yield snap('success'); return { ...assignment } }
    if (attempts >= budget) { interrupted = true; yield snap('budget'); return null }
    const remaining = p.variables.filter(v => !Object.hasOwn(assignment, v))
    const degree = v => neighborsOf(p, v).filter(w => remaining.includes(w)).length
    if (variableOrder === 'mrv') remaining.sort((a, b) => legal(a).length - legal(b).length || degree(b) - degree(a) || p.variables.indexOf(a) - p.variables.indexOf(b))
    const variable = remaining[0], values = legal(variable)
    const losses = value => neighborsOf(p, variable).filter(v => !Object.hasOwn(assignment, v)).reduce((sum, v) => sum + legal(v).filter(vv => !compatible(p, variable, value, v, vv)).length, 0)
    if (valueOrder === 'lcv') values.sort((a, b) => losses(a) - losses(b) || domains[variable].indexOf(a) - domains[variable].indexOf(b))
    yield snap('choose', { variable, values: values.slice(), choices: remaining.map(v => ({ variable: v, remaining: legal(v).length, degree: degree(v) })) })
    for (const value of values) {
      if (attempts >= budget) { interrupted = true; yield snap('budget'); return null }
      const saved = copyDomains(domains)
      assignment[variable] = value; domains[variable] = [value]; attempts++
      yield snap('assign', { variable, value })
      let feasible = true
      if (filtering === 'fc') for (const v of neighborsOf(p, variable).filter(v => !Object.hasOwn(assignment, v))) {
        const removed = domains[v].filter(x => !compatible(p, variable, value, v, x))
        domains[v] = domains[v].filter(x => !removed.includes(x)); prunes += removed.length
        yield snap('filter', { variable: v, source: variable, removed })
        if (!domains[v].length) { feasible = false; yield snap('wipeout', { variable: v }); break }
      }
      if (filtering === 'mac') {
        const iterator = ac3Steps(p, { domains })
        let event = iterator.next()
        while (!event.done) {
          if (event.value.phase === 'revise') { revisions++; prunes += event.value.removed.length }
          yield snap('propagate', { propagation: event.value })
          event = iterator.next()
        }
        feasible = event.value
      }
      if (feasible) { const result = yield* search(); if (result) return result }
      domains = saved; delete assignment[variable]
      yield snap('backtrack', { variable, value })
      if (interrupted) return null
    }
    return null
  }
  const solution = yield* search()
  if (!solution) yield snap(interrupted ? 'budget' : 'failure')
  return solution
}
export function* treeCspSteps(problem) {
  const p = validateCsp(problem), domains = copyDomains(p.domains), root = p.variables[0], parent = { [root]: null }, order = [root], assignment = {}
  for (let i = 0; i < order.length; i++) for (const v of neighborsOf(p, order[i])) {
    if (v === parent[order[i]]) continue
    if (Object.hasOwn(parent, v)) throw Error('Thuật toán cây cần đồ thị liên thông không có chu trình.')
    parent[v] = order[i]; order.push(v)
  }
  if (order.length !== p.variables.length) throw Error('Đồ thị có nhiều thành phần. Hãy giải riêng từng cây.')
  const snap = (phase, extra = {}) => ({ phase, domains: copyDomains(domains), assignment: { ...assignment }, order: order.slice(), parent: { ...parent }, ...extra })
  yield snap('start')
  if (p.variables.some(v => !domains[v].length)) { yield snap('failure'); return null }
  for (let i = order.length - 1; i > 0; i--) {
    const child = order[i], a = parent[child], removed = revise(p, domains, a, child)
    yield snap('revise', { arc: [a, child], removed })
    if (!domains[a].length) { yield snap('failure'); return null }
  }
  for (const v of order) {
    const value = domains[v].find(x => parent[v] === null || compatible(p, parent[v], assignment[parent[v]], v, x))
    if (value === undefined) { yield snap('failure'); return null }
    assignment[v] = value
    yield snap('assign', { variable: v, value })
  }
  yield snap('success')
  return assignment
}
