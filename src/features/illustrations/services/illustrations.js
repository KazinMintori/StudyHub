export function searchTrace(adjacency, mode = 'bfs') {
  const frontier = ['A'], visited = new Set(), states = [{ frontier: [...frontier], visited: [], current: null }]
  while (frontier.length) {
    const current = mode === 'bfs' ? frontier.shift() : frontier.pop()
    if (visited.has(current)) continue
    visited.add(current)
    const neighbors = (adjacency[current] || []).filter(node => !visited.has(node))
    frontier.push(...(mode === 'bfs' ? neighbors : [...neighbors].reverse()))
    states.push({ frontier: [...frontier], visited: [...visited], current })
  }
  return states
}
export function gradientTrace(start, rate, steps) {
  const trace = [start]
  for (let i = 0; i < steps; i++) trace.push(trace.at(-1) - rate * 2 * trace.at(-1))
  return trace
}
export function bayesCounts(prior, sensitivity, falsePositive, population = 1000) {
  const positives = population * prior, negatives = population - positives
  const truePositive = positives * sensitivity, falseAlarm = negatives * falsePositive
  return { positives, negatives, truePositive, falseAlarm, posterior: truePositive + falseAlarm > 0 ? truePositive / (truePositive + falseAlarm) : null }
}
export function wordCountTrace(text) {
  const words = (text.toLocaleLowerCase('vi').match(/[\p{L}\p{N}]+/gu) || []).slice(0, 30)
  const pairs = words.map(word => [word, 1]), grouped = new Map()
  for (const [word, value] of pairs) grouped.set(word, [...(grouped.get(word) || []), value])
  return { pairs, groups: [...grouped], counts: [...grouped].map(([word, values]) => [word, values.reduce((sum, x) => sum + x, 0)]) }
}
