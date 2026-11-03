import { leastSquaresLine } from './fitting.mjs'
import { solveLinearSystem } from './lp-models-geometry.mjs'

// The lab keeps at least three distinct knots in increasing order.
export function smoothNaturalSpline(points, penalty) {
  const knots = points.map(([x]) => x)
  const observed = points.map(([, y]) => y)
  const widths = knots.slice(1).map((x, index) => x - knots[index])
  const inner = points.length - 2

  if (penalty === Infinity) {
    const line = leastSquaresLine(points)
    const values = knots.map(x => line.a * x + line.c)
    return { values, roughness: 0, evaluate: x => line.a * x + line.c }
  }

  // Each column maps knot values to the change in adjacent secant slopes.
  const columns = Array.from({ length: inner }, (_, j) =>
    knots.map((_, i) => {
      if (i === j) return 1 / widths[j]
      if (i === j + 1) return -1 / widths[j] - 1 / widths[j + 1]
      if (i === j + 2) return 1 / widths[j + 1]
      return 0
    })
  )
  const dot = (a, b) => a.reduce((sum, value, i) => sum + value * b[i], 0)
  const mass = columns.map((_, i) => columns.map((_, j) => {
    if (i === j) return (widths[i] + widths[i + 1]) / 3
    return Math.abs(i - j) === 1 ? widths[Math.max(i, j)] / 6 : 0
  }))
  // Eliminating the fitted values gives (R + λ QᵀQ)m = Qᵀy.
  const system = mass.map((row, i) =>
    row.map((value, j) => value + penalty * dot(columns[i], columns[j]))
  )
  const innerCurvature = solveLinearSystem(system, columns.map(column => dot(column, observed)))
  const curvature = [0, ...innerCurvature, 0]
  const values = observed.map((y, i) =>
    y - penalty * columns.reduce((sum, column, j) => sum + column[i] * innerCurvature[j], 0)
  )
  const roughness = dot(innerCurvature, mass.map(row => dot(row, innerCurvature)))

  function evaluate(x) {
    const right = knots.findIndex(knot => knot >= x)
    const i = right === -1 ? widths.length - 1 : Math.max(0, right - 1)
    const width = widths[i]
    const t = (x - knots[i]) / width
    const left = 1 - t
    return left * values[i] + t * values[i + 1]
      + (width ** 2 / 6) * (
        (left ** 3 - left) * curvature[i] + (t ** 3 - t) * curvature[i + 1]
      )
  }

  return { values, roughness, evaluate }
}
