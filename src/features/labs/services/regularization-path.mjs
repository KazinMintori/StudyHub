import { closestOnSegment } from './convex-geometry.mjs'

const design = [[1, 2], [2, 1], [1, 1], [3, 1]]
const targets = [3, 1, 2, 4]

export function regularizationPoint(mode, weight) {
  let point
  const penalty = weight === 1 ? Infinity : weight / (1 - weight)
  if (weight === 1) {
    point = [0, 0]
  } else if (mode === 'ridge') {
    const first = 15 + penalty
    const second = 7 + penalty
    const determinant = first * second - 64
    point = [(19 * second - 104) / determinant, (13 * first - 152) / determinant]
  } else if (penalty <= 86 / 7) {
    point = [(29 + penalty / 2) / 41, (43 - 7 * penalty / 2) / 41]
  } else {
    point = [Math.max(0, (19 - penalty / 2) / 15), 0]
  }
  const objectives = regularizationObjectives(point, mode)
  return { point, penalty, weight, ...objectives }
}

export function regularizationObjectives(point, mode) {
  const error = design.reduce((sum, row, index) => {
    const residual = row[0] * point[0] + row[1] * point[1] - targets[index]
    return sum + residual * residual
  }, 0)
  const size = mode === 'ridge'
    ? point[0] ** 2 + point[1] ** 2
    : Math.abs(point[0]) + Math.abs(point[1])
  return { error, size }
}

export const regularizationWeights = [
  0,
  ...Array.from({ length: 181 }, (_, index) => {
    const penalty = 10 ** (-3 + index / 30)
    return penalty / (1 + penalty)
  }),
  1,
]

export function nearestPathWeight(screenPoint, path, project) {
  let closest = { distance: Infinity, weight: 0 }
  for (let index = 1; index < path.length; index++) {
    const previous = path[index - 1]
    const next = path[index]
    const segment = closestOnSegment(screenPoint, project(previous), project(next))
    if (segment.distance < closest.distance) {
      closest = {
        distance: segment.distance,
        weight: previous.weight + segment.t * (next.weight - previous.weight),
      }
    }
  }
  return closest.weight
}
