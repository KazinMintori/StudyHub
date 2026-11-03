export const sigmoid = value => 1 / (1 + Math.exp(-value))

export function networkStep({ w = 0.4, b = 0.1, v = -0.7, c = 0.2 } = {}, rate = 0.5) {
  const x = 0.6, target = 1
  const hidden = sigmoid(w * x + b)
  const output = sigmoid(v * hidden + c)
  const loss = (output - target) ** 2 / 2
  const outputDelta = (output - target) * output * (1 - output)
  const hiddenDelta = outputDelta * v * hidden * (1 - hidden)
  const gradient = { w: hiddenDelta * x, b: hiddenDelta, v: outputDelta * hidden, c: outputDelta }
  const before = { w, b, v, c }
  const after = Object.fromEntries(Object.entries(before).map(([name, value]) => [name, value - rate * gradient[name]]))
  return { x, target, hidden, output, loss, outputDelta, hiddenDelta, gradient, before, after }
}

export function attentionStep(query = [1, 1], maskSecond = false) {
  const keys = [[1, 0], [0, 1]], values = [[1, 0], [0, 2]]
  const dots = keys.map(key => query.reduce((sum, value, index) => sum + value * key[index], 0))
  const scores = dots.map((dot, index) => maskSecond && index === 1 ? -Infinity : dot / Math.sqrt(2))
  const peak = Math.max(...scores)
  const weights = scores.map(score => Math.exp(score - peak))
  const total = weights.reduce((sum, weight) => sum + weight, 0)
  const probabilities = weights.map(weight => weight / total)
  const result = [0, 1].map(dimension => values.reduce(
    (sum, value, index) => sum + probabilities[index] * value[dimension], 0))
  return { query, keys, values, dots, scores, probabilities, result }
}

export function beamSteps(width = 2) {
  const branches = {
    '': [['A', 0.6], ['B', 0.4]],
    A: [['x', 0.6], ['y', 0.4]],
    B: [['z', 1]],
    'A x': [['EOS', 0.5], ['w', 0.5]],
    'A y': [['EOS', 1]],
    'B z': [['EOS', 1]],
    'A x w': [['EOS', 1]]
  }
  let beams = [{ tokens: [], log: 0, ended: false }]
  const frames = [{ kept: beams, removed: [] }]
  for (let depth = 0; depth < 4; depth++) {
    const candidates = beams.flatMap(beam => beam.ended ? [beam] : (branches[beam.tokens.join(' ')] ?? []).map(([token, probability]) => ({
      tokens: [...beam.tokens, token], log: beam.log + Math.log(probability), ended: token === 'EOS'
    })))
    candidates.sort((a, b) => b.log - a.log)
    beams = candidates.slice(0, width)
    frames.push({ kept: beams, removed: candidates.slice(width) })
    if (beams.every(beam => beam.ended)) break
  }
  return frames
}
