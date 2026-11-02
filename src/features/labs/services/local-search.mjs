// All positions and rows used by the engine are zero based.
export function seededRandom(seed = 1) {
  let value = Number(seed) >>> 0
  return () => {
    value = (Math.imul(value, 1664525) + 1013904223) >>> 0
    return value / 4294967296
  }
}
export const landscapes = {
  valley: { title: 'Hai thung lũng', costs: [8, 4, 2, 5, 7, 3, 1, 0, 4], start: 1 },
  plateau: { title: 'Miền bằng có lối ra', costs: [6, 3, 3, 3, 1, 0, 4], start: 1 },
  trap: { title: 'Danh sách tabu làm tắc lối', costs: [0, 2, 1], start: 1 }
}
export function validateLandscape(costs) {
  if (!Array.isArray(costs) || costs.length < 3 || costs.length > 20 || costs.some(x => !Number.isFinite(x) || Math.abs(x) > 10000)) throw Error('Nhập từ 3 đến 20 chi phí hữu hạn, trị tuyệt đối không quá 10000.')
  return costs.slice()
}
export function* landscapeSteps({ costs, start = 1, mode = 'hill', seed = 7, temperature = 4, cooling = .9, tenure = 3, width = 2, budget = 30 }) {
  validateLandscape(costs)
  if (!Number.isInteger(start) || start < 0 || start >= costs.length) throw Error('Vị trí bắt đầu không hợp lệ.')
  if (!['hill', 'anneal', 'tabu', 'beam'].includes(mode)) throw Error('Thuật toán không hợp lệ.')
  if (!(temperature > 0 && cooling > 0 && cooling < 1)) throw Error('Cần nhiệt độ dương và tốc độ làm nguội trong khoảng 0 đến 1.')
  if (!Number.isInteger(budget) || budget < 1 || budget > 200 || !Number.isInteger(tenure) || tenure < 1 || tenure > 10 || !Number.isInteger(width) || width < 1 || width > 5) throw Error('Tham số vượt giới hạn mô phỏng.')
  const random = seededRandom(seed), neighbors = x => [x - 1, x + 1].filter(y => y >= 0 && y < costs.length)
  const rank = (a, b) => costs[a] - costs[b] || a - b
  let current = start, best = start, visited = [start], tabu = [start], beam = [...new Set([start, costs.length - 1, 0, Math.floor(costs.length / 2), costs.length - 2])].slice(0, width)
  if (mode === 'beam') best = beam.slice().sort(rank)[0]
  const snap = (phase, extra = {}) => ({ phase, mode, current, best, visited: visited.slice(), tabu: tabu.slice(), beam: beam.slice(), ...extra })
  yield snap('start')
  for (let iteration = 0; iteration < budget; iteration++) {
    if (mode === 'beam') {
      const candidates = [...new Set(beam.flatMap(neighbors))].sort(rank)
      yield snap('pool', { candidates, iteration })
      beam = candidates.slice(0, width)
      current = beam[0]
      if (costs[current] < costs[best]) best = current
      visited.push(current)
      yield snap('select', { candidates, iteration })
      continue
    }
    const candidates = neighbors(current).sort(rank)
    yield snap('neighbors', { candidates, iteration })
    let next, probability = 1, draw = null, accepted = true, T = null
    if (mode === 'hill') {
      next = candidates[0]
      if (costs[next] >= costs[current]) { yield snap('local', { candidates, iteration }); return }
    } else if (mode === 'anneal') {
      T = temperature * cooling ** iteration
      next = candidates[Math.floor(random() * candidates.length)]
      const delta = costs[next] - costs[current]
      probability = delta <= 0 ? 1 : Math.exp(-delta / T)
      draw = random()
      accepted = draw < probability
      yield snap('probability', { next, delta, probability, draw, accepted, T, iteration })
    } else {
      const allowed = candidates.filter(x => !tabu.includes(x) || costs[x] < costs[best])
      if (!allowed.length) { yield snap('blocked', { candidates, iteration }); return }
      next = allowed[0]
      yield snap('admissible', { next, candidates, aspiration: tabu.includes(next), iteration })
    }
    if (accepted) {
      current = next
      visited.push(current)
      if (costs[current] < costs[best]) best = current
      if (mode === 'tabu') tabu = [...tabu, current].slice(-tenure)
    }
    yield snap(accepted ? 'move' : 'reject', { next, probability, draw, T, iteration })
  }
  yield snap('budget', { iteration: budget })
}
export function queenConflicts(rows) {
  let result = 0
  for (let i = 0; i < rows.length; i++) for (let j = i + 1; j < rows.length; j++) {
    if (rows[i] === rows[j] || Math.abs(rows[i] - rows[j]) === j - i) result++
  }
  return result
}
export function queenNeighbors(rows) {
  const result = []
  for (let column = 0; column < rows.length; column++) for (let row = 0; row < rows.length; row++) {
    if (row === rows[column]) continue
    const next = rows.slice(); next[column] = row
    result.push({ rows: next, column, row, cost: queenConflicts(next) })
  }
  return result.sort((a, b) => a.cost - b.cost || a.column - b.column || a.row - b.row)
}
export function* queenSteps({ rows, mode = 'hill', seed = 7, budget = 100 }) {
  if (!Array.isArray(rows) || rows.length < 4 || rows.length > 10 || rows.some(x => !Number.isInteger(x) || x < 0 || x >= rows.length)) throw Error('Bàn cờ có 4 đến 10 cột. Mỗi hàng phải nằm trong bàn cờ.')
  if (!['hill', 'minconflicts', 'anneal'].includes(mode) || !Number.isInteger(budget) || budget < 1 || budget > 200) throw Error('Tham số tìm kiếm không hợp lệ.')
  const random = seededRandom(seed)
  let current = rows.slice(), best = rows.slice()
  const snap = (phase, extra = {}) => ({ phase, rows: current.slice(), best: best.slice(), cost: queenConflicts(current), bestCost: queenConflicts(best), ...extra })
  yield snap('start')
  for (let iteration = 0; iteration < budget; iteration++) {
    if (queenConflicts(current) === 0) { yield snap('success'); return }
    let candidates = queenNeighbors(current), next
    if (mode === 'minconflicts') {
      const columns = current.map((_, i) => i).filter(i => current.some((r, j) => j !== i && (r === current[i] || Math.abs(r - current[i]) === Math.abs(j - i))))
      const column = columns[Math.floor(random() * columns.length)]
      candidates = candidates.filter(x => x.column === column)
      // Include staying in the current row as a legal min-conflicts tie.
      candidates.push({ rows: current.slice(), column, row: current[column], cost: queenConflicts(current) })
      const minimum = Math.min(...candidates.map(x => x.cost)), ties = candidates.filter(x => x.cost === minimum)
      next = ties[Math.floor(random() * ties.length)]
    } else next = mode === 'hill' ? candidates[0] : candidates[Math.floor(random() * candidates.length)]
    yield snap('candidate', { next, iteration })
    if (mode === 'hill' && next.cost >= queenConflicts(current)) { yield snap('local', { next }); return }
    const T = 3 * .97 ** iteration, delta = next.cost - queenConflicts(current)
    const probability = delta <= 0 ? 1 : Math.exp(-delta / T), draw = mode === 'anneal' ? random() : 0
    const accepted = mode !== 'anneal' || draw < probability
    if (accepted) current = next.rows.slice()
    if (queenConflicts(current) < queenConflicts(best)) best = current.slice()
    yield snap(accepted ? 'move' : 'reject', { next, iteration, T, delta, probability, draw })
  }
  yield snap(queenConflicts(current) === 0 ? 'success' : 'budget')
}
export const tourExamples = {
  cross: { title: 'Bốn thành phố, đường đi giao nhau', points: [[0, 0], [4, 0], [4, 3], [0, 3]], tour: [0, 2, 1, 3] },
  six: { title: 'Sáu thành phố', points: [[0, 0], [4, 0], [6, 3], [4, 6], [0, 6], [-2, 3]], tour: [0, 3, 1, 4, 2, 5] }
}
export function tourLength(points, tour) {
  return tour.reduce((sum, v, i) => { const w = tour[(i + 1) % tour.length]; return sum + Math.hypot(points[v][0] - points[w][0], points[v][1] - points[w][1]) }, 0)
}
export function twoOpt(tour, i, j) {
  if (!(0 <= i && i + 1 < j && j < tour.length) || i === 0 && j === tour.length - 1) throw Error('Hai cạnh phải không kề nhau trên chu trình.')
  return [...tour.slice(0, i + 1), ...tour.slice(i + 1, j + 1).reverse(), ...tour.slice(j + 1)]
}
export function* twoOptSteps({ points, tour }) {
  if (!Array.isArray(points) || points.length < 4 || points.length > 12 || points.some(p => !Array.isArray(p) || p.length !== 2 || p.some(x => !Number.isFinite(x) || Math.abs(x) > 1000)) || !Array.isArray(tour) || tour.length !== points.length || new Set(tour).size !== points.length || tour.some(x => !Number.isInteger(x) || x < 0 || x >= points.length)) throw Error('Cần 4 đến 12 điểm và một hoán vị đủ các chỉ số thành phố.')
  let current = tour.slice()
  const snap = (phase, extra = {}) => ({ phase, tour: current.slice(), cost: tourLength(points, current), ...extra })
  yield snap('start')
  for (let round = 0; round < 50; round++) {
    let improved = false
    scan: for (let i = 0; i < current.length; i++) for (let j = i + 2; j < current.length; j++) {
      if (i === 0 && j === current.length - 1) continue
      const next = twoOpt(current, i, j), nextCost = tourLength(points, next), delta = nextCost - tourLength(points, current)
      yield snap('candidate', { next, nextCost, delta, i, j })
      if (delta < -1e-10) {
        current = next; improved = true
        yield snap('move', { i, j, delta })
        break scan
      }
      // First improvement restarts the scan from the next round.
    }
    if (!improved) { yield snap('local'); return }
  }
  yield snap('budget')
}
export function orderCrossover(a, b, left, right) {
  if (a.length !== b.length || new Set(a).size !== a.length || new Set(b).size !== b.length || a.some(x => !b.includes(x)) || !Number.isInteger(left) || !Number.isInteger(right) || left < 0 || left >= right || right > a.length) throw Error('OX cần hai hoán vị cùng tập gene và đoạn hợp lệ.')
  const child = Array(a.length).fill(null)
  child.splice(left, right - left, ...a.slice(left, right))
  let position = right % a.length
  for (const gene of [...b.slice(right), ...b.slice(0, right)]) if (!child.includes(gene)) {
    child[position] = gene; position = (position + 1) % a.length
  }
  return child
}
export const initialPopulation = ['24748552', '32752411', '24415124', '32543213'].map(s => [...s].map(x => Number(x) - 1))
export function* geneticSteps({ seed = 7, mutation = .08, elitism = true, generations = 8 } = {}) {
  if (!(mutation >= 0 && mutation <= 1) || !Number.isInteger(generations) || generations < 1 || generations > 30) throw Error('Tham số di truyền không hợp lệ.')
  const random = seededRandom(seed), fitness = q => 28 - queenConflicts(q)
  let population = initialPopulation.map(x => x.slice()), best = population.slice().sort((a, b) => fitness(b) - fitness(a))[0].slice()
  const snap = (phase, extra = {}) => ({ phase, population: population.map(x => x.slice()), fitness: population.map(fitness), best: best.slice(), bestFitness: fitness(best), ...extra })
  yield snap('start')
  for (let generation = 0; generation < generations; generation++) {
    const scores = population.map(fitness), total = scores.reduce((a, b) => a + b, 0)
    const probabilities = scores.map(x => total ? x / total : 1 / population.length)
    yield snap('evaluate', { generation, probabilities })
    const select = () => { const u = random(); let sum = 0; for (let i = 0; i < population.length; i++) { sum += probabilities[i]; if (u < sum) return i } return population.length - 1 }
    const children = []
    if (elitism) children.push(population.slice().sort((a, b) => fitness(b) - fitness(a))[0].slice())
    while (children.length < population.length) {
      const a = select(), b = select(), cut = 1 + Math.floor(random() * 7)
      const child = [...population[a].slice(0, cut), ...population[b].slice(cut)], before = child.slice(), changes = []
      yield snap('crossover', { generation, parents: [a, b], cut, child: child.slice(), probabilities })
      for (let i = 0; i < child.length; i++) if (random() < mutation) {
        const old = child[i], value = Math.floor(random() * 7)
        child[i] = value >= old ? value + 1 : value; changes.push(i)
      }
      yield snap('mutation', { generation, before, child: child.slice(), changes, probabilities })
      children.push(child)
    }
    population = children
    for (const individual of population) if (fitness(individual) > fitness(best)) best = individual.slice()
    yield snap('replace', { generation })
  }
  yield snap('budget')
}
