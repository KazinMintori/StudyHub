// Pure, deterministic models shared by the three data-algorithm labs.
export const pageGraph = [[1, 2, 3], [0, 3], [0], [1, 2]]

export function personalizedRank(graph, teleport, beta = 0.8, steps = 40) {
  const n = graph.length
  if (!n || teleport.length !== n || !teleport.every(x => Number.isFinite(x) && x >= 0) ||
      Math.abs(teleport.reduce((a, b) => a + b, 0) - 1) > 1e-12 ||
      !(beta >= 0 && beta < 1) || !Number.isInteger(steps) || steps < 0 ||
      !graph.every(row => row.every(i => Number.isInteger(i) && i >= 0 && i < n))) throw Error('Invalid PageRank parameters')
  let rank = Array(n).fill(1 / n), delta = 0
  for (let t = 0; t < steps; t++) {
    const next = teleport.map(x => (1 - beta) * x)
    graph.forEach((targets, j) => {
      // Fixed uniform dangling policy makes S independent of teleport.
      if (!targets.length) next.forEach((_, i) => { next[i] += beta * rank[j] / n })
      else targets.forEach(i => { next[i] += beta * rank[j] / targets.length })
    })
    delta = next.reduce((sum, x, i) => sum + Math.abs(x - rank[i]), 0)
    rank = next
  }
  return { rank, delta, errorBound: steps ? beta * delta / (1 - beta) : null }
}

export function shingles(text, k) {
  if (!Number.isInteger(k) || k < 1) throw Error('Invalid shingle length')
  const chars = Array.from(text.normalize('NFC').toLocaleLowerCase('vi').trim().replace(/\s+/gu, ' '))
  return new Set(Array.from({ length: Math.max(0, chars.length - k + 1) }, (_, i) => chars.slice(i, i + k).join('')))
}

export function jaccard(a, b) {
  let intersection = 0
  for (const item of a) if (b.has(item)) intersection++
  const union = a.size + b.size - intersection
  return { intersection, union, similarity: union ? intersection / union : 1 }
}

export function* permutations(items) {
  if (!items.length) { yield []; return }
  for (let i = 0; i < items.length; i++) {
    for (const tail of permutations([...items.slice(0, i), ...items.slice(i + 1)])) yield [items[i], ...tail]
  }
}

export function minHash(set, permutation) {
  return permutation.find(item => set.has(item)) ?? null
}

// A fixed seed is for reproducible teaching, not a claim of cryptographic randomness.
export function permutationSample(universe, count, seed = 20261105) {
  let state = seed >>> 0
  const random = () => {
    state = (Math.imul(1664525, state) + 1013904223) >>> 0
    return state / 4294967296
  }
  return Array.from({ length: count }, () => {
    const order = [...universe]
    for (let i = order.length - 1; i > 0; i--) {
      const j = Math.floor(random() * (i + 1))
      ;[order[i], order[j]] = [order[j], order[i]]
    }
    return order
  })
}

export function candidateProbability(s, bands, rows) {
  if (!(s >= 0 && s <= 1) || !Number.isInteger(bands) || bands < 1 || !Number.isInteger(rows) || rows < 1) throw Error('Invalid LSH parameters')
  if (s === 0) return 0
  if (s === 1) return 1
  return -Math.expm1(bands * Math.log1p(-(s ** rows)))
}

export function matchingBands(a, b, rows) {
  if (a.length !== b.length || !Number.isInteger(rows) || rows < 1 || a.length % rows) throw Error('Invalid band signatures')
  return Array.from({ length: a.length / rows }, (_, band) => {
    const start = band * rows
    return a.slice(start, start + rows).every((x, offset) => x === b[start + offset])
  })
}
