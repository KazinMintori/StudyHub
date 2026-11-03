export const detectorObservations = [
  { observation: 1, signal: 0.1, noise: 0.5 },
  { observation: 2, signal: 0.3, noise: 0.4 },
  { observation: 3, signal: 0.6, noise: 0.1 }
]

const likelihoodOrder = detectorObservations.map((_, i) => i).sort((a, b) => {
  const first = detectorObservations[a]
  const second = detectorObservations[b]
  return second.signal * first.noise - first.signal * second.noise
})

export function detectorRates(rule) {
  return detectorObservations.reduce(({ falseAlarm, detection }, row, i) => ({
    falseAlarm: falseAlarm + rule[i] * row.noise,
    detection: detection + rule[i] * row.signal
  }), { falseAlarm: 0, detection: 0 })
}

// For these data each observation has positive probability under noise.
export function detectorAtFalseAlarm(budget) {
  let remaining = Math.min(1, Math.max(0, budget))
  const rule = detectorObservations.map(() => 0)
  for (const i of likelihoodOrder) {
    const { noise } = detectorObservations[i]
    const allocation = Math.min(remaining, noise)
    rule[i] = allocation / noise
    remaining -= allocation
  }
  return { rule, ...detectorRates(rule) }
}

export const rocBudgets = likelihoodOrder.reduce((prefixes, i) =>
  [...prefixes, prefixes.at(-1) + detectorObservations[i].noise], [0])

export const minimaxDetector = (() => {
  const rightIndex = rocBudgets.findIndex(budget => {
    const { falseAlarm, detection } = detectorAtFalseAlarm(budget)
    return falseAlarm + detection >= 1
  })
  const left = detectorAtFalseAlarm(rocBudgets[rightIndex - 1])
  const right = detectorAtFalseAlarm(rocBudgets[rightIndex])
  const residual = row => row.falseAlarm + row.detection - 1
  const fraction = -residual(left) / (residual(right) - residual(left))
  return detectorAtFalseAlarm(left.falseAlarm + fraction * (right.falseAlarm - left.falseAlarm))
})()
