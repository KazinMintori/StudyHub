import test from 'node:test'
import assert from 'node:assert/strict'
import { contourSegments } from '../../docs/.vitepress/theme/contour.mjs'

test('Contour of a circle stays on the circle', () => {
  const segs = contourSegments(([x, y]) => x * x + y * y, { x0: -2, x1: 2, y0: -2, y1: 2, n: 80 }, 1)
  assert(segs.length > 50)
  for (const seg of segs) for (const [x, y] of seg) assert(Math.abs(Math.hypot(x, y) - 1) < 0.01)
})

test('Undefined values are skipped and saddle cells produce two segments', () => {
  const half = contourSegments(([x, y]) => (y > 0 ? x * x / y : NaN), { x0: -2, x1: 2, y0: -1, y1: 2, n: 40 }, 1)
  for (const seg of half) for (const [, y] of seg) assert(y >= 0)
  const saddle = contourSegments(([x, y]) => x * y, { x0: -1, x1: 1, y0: -1, y1: 1, n: 20 }, 0.25)
  for (const seg of saddle) for (const [x, y] of seg) assert(Math.abs(x * y - 0.25) < 0.02)
})
