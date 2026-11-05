import test from 'node:test'
import assert from 'node:assert/strict'
import { pageGraph, personalizedRank, shingles, jaccard, permutations, minHash, matchingBands, candidateProbability } from '../../src/features/labs/services/data-algorithms.mjs'
const close = (a, b) => assert.ok(Math.abs(a - b) < 1e-10, `${a} != ${b}`)

test('personalized PageRank preserves mass including dangling vertices and zero teleport support', () => {
  for (const graph of [pageGraph, [[1], [], []], [[], [], []]]) {
    const v = graph.map((_, i) => i === 0 ? 1 : 0)
    const { rank } = personalizedRank(graph, v, 0.8, 150)
    close(rank.reduce((a, b) => a + b, 0), 1)
    assert.ok(rank.every(x => x >= 0))
  }
  assert.deepEqual(personalizedRank([[0], [1]], [1, 0], 0, 1).rank, [1, 0])
  close(personalizedRank([[0], [1]], [1, 0], 0.8, 150).rank[1], 0)
})

test('fixed dangling policy preserves linearity in teleport and posterior error bound', () => {
  const graph = [[1], [], [0]], a = [1, 0, 0], b = [0, 0, 1]
  const ra = personalizedRank(graph, a, 0.8, 150).rank
  const rb = personalizedRank(graph, b, 0.8, 150).rank
  const mix = personalizedRank(graph, [0.3, 0, 0.7], 0.8, 150).rank
  mix.forEach((x, i) => close(x, 0.3 * ra[i] + 0.7 * rb[i]))
  const early = personalizedRank(graph, a, 0.8, 4)
  assert.ok(early.rank.reduce((s, x, i) => s + Math.abs(x - ra[i]), 0) <= early.errorBound + 1e-12)
})

test('all permutations verify MinHash theorem for every nonempty pair on four elements', () => {
  const universe = ['a', 'b', 'c', 'd'], orders = [...permutations(universe)]
  for (let maskA = 1; maskA < 16; maskA++) for (let maskB = 1; maskB < 16; maskB++) {
    const a = new Set(universe.filter((_, i) => maskA & (1 << i)))
    const b = new Set(universe.filter((_, i) => maskB & (1 << i)))
    const collisions = orders.filter(p => minHash(a, p) === minHash(b, p)).length
    close(collisions / orders.length, jaccard(a, b).similarity)
  }
  assert.equal(minHash(new Set(), universe), null)
  assert.equal(jaccard(new Set(), new Set()).similarity, 1)
})

test('shingles normalize NFC, case and whitespace; count Unicode code points', () => {
  assert.deepEqual(shingles('  A\u0301  B ', 2), new Set(['á ', ' b']))
  assert.deepEqual(shingles('😀a', 1), new Set(['😀', 'a']))
  assert.equal(shingles('a', 2).size, 0)
})

test('banding agrees with exhaustive independent Bernoulli row outcomes', () => {
  for (const s of [0, 0.2, 0.6, 1]) {
    let p = 0
    for (let mask = 0; mask < 16; mask++) {
      const outcomes = Array.from({ length: 4 }, (_, i) => (mask >> i) & 1)
      const weight = outcomes.reduce((v, x) => v * (x ? s : 1 - s), 1)
      if (matchingBands([1, 1, 1, 1], outcomes, 2).some(Boolean)) p += weight
    }
    close(p, candidateProbability(s, 2, 2))
  }
  // Independently calculated with Python Fraction(4, 5).
  close(candidateProbability(0.8, 20, 5), 0.9996439421094793)
  assert.throws(() => matchingBands([1], [1], 2))
  assert.throws(() => personalizedRank([[0]], [1], 1, 10))
})
