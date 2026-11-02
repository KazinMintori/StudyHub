// A finite decision problem, with observation points on the actual calculation.
export const decisionCode = [
  'function chooseRoute(p, loss) {',
  '  let best = null',
  '  for (const route of [',
  "    { name: 'Đường ngắn', outcomes: [[p, 10], [1 - p, loss]] },",
  "    { name: 'Đường vòng', outcomes: [[1, 6]] }",
  '  ]) {',
  '    let score = 0',
  '    for (const [probability, utility] of route.outcomes) {',
  '      score += probability * utility',
  '    }',
  '    if (best === null || score > best.score + 1e-9) {',
  '      best = { name: route.name, score }',
  '    }',
  '  }',
  '  return best',
  '}'
]

export const decisionPresets = [
  { title: 'Đường ngắn có lợi', p: 0.8, loss: 0 },
  { title: 'Ưu tiên đường vòng', p: 0.4, loss: 0 },
  { title: 'Hai phương án bằng nhau', p: 0.6, loss: 0 },
  { title: 'Hậu quả bất lợi lớn hơn', p: 0.8, loss: -20 }
]

export function decisionRoutes(p, loss) {
  if (!Number.isFinite(p) || p < 0 || p > 1 || !Number.isFinite(loss)) {
    throw new RangeError('Xác suất phải thuộc [0, 1] và lợi ích phải hữu hạn.')
  }
  return [
    { name: 'Đường ngắn', outcomes: [[p, 10], [1 - p, loss]] },
    { name: 'Đường vòng', outcomes: [[1, 6]] }
  ]
}

export function chooseRoute(p, loss, observe = () => {}) {
  const routes = decisionRoutes(p, loss)
  let best = null
  const scores = [null, null]
  const emit = (line, phase, routeIndex = null, outcomeIndex = null, score = null, term = null) => {
    observe({ line, phase, routeIndex, outcomeIndex, score, term, scores: [...scores], best: best && { ...best } })
  }
  emit(2, 'start')
  for (const [routeIndex, route] of routes.entries()) {
    emit(3, 'route', routeIndex)
    let score = 0
    emit(7, 'zero', routeIndex, null, score)
    for (const [outcomeIndex, [probability, utility]] of route.outcomes.entries()) {
      const term = probability * utility
      score += term
      emit(9, 'add', routeIndex, outcomeIndex, score, term)
    }
    scores[routeIndex] = score
    emit(11, 'compare', routeIndex, null, score)
    if (best === null || score > best.score + 1e-9) {
      best = { name: route.name, score }
      emit(12, 'replace', routeIndex, null, score)
    } else {
      emit(11, 'keep', routeIndex, null, score)
    }
  }
  emit(15, 'done')
  return best
}

export function traceDecision(p, loss) {
  const frames = []
  chooseRoute(p, loss, frame => frames.push(frame))
  return frames
}

export function codeTokens(line) {
  return line.split(/('(?:[^'\\]|\\.)*'|\b(?:function|let|const|for|of|if|return|null)\b|\b\d+(?:e-\d+)?\b)/g)
    .filter(Boolean).map(text => ({ text, kind: text.startsWith("'") ? 'string' : /^(function|let|const|for|of|if|return|null)$/.test(text) ? 'keyword' : /^\d/.test(text) ? 'number' : '' }))
}
