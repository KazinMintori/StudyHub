import test from 'node:test'
import assert from 'node:assert/strict'
import { leastSquaresLine, l1Line, chebyshevLine, lossL1, lossL2, lossLinf, residuals } from '../../docs/.vitepress/theme/fitting.mjs'
const near = (a, b, tolerance = 1e-9) => assert(Math.abs(a - b) <= tolerance, `${a} != ${b}`)

test('Least squares solves the normal equations and leaves residuals orthogonal to the columns', () => {
  const pts = [[0, 1], [1, 2], [2, 4]]
  const line = leastSquaresLine(pts)
  near(line.a, 1.5); near(line.c, 5 / 6)
  const r = residuals(pts, line)
  near(r.reduce((s, v) => s + v, 0), 0); near(r.reduce((s, v, i) => s + v * pts[i][0], 0), 0)
  near(lossL2(pts, line), 1 / 6)
  assert.equal(leastSquaresLine([[1, 1], [1, 2]]), null)
})

test('l1 and Chebyshev fits are optimal against a fine search', () => {
  const pts = [[0, 0.5], [1, 1.5], [2, 1.8], [3, 3.2], [4, 7]]
  const l1 = l1Line(pts), cheb = chebyshevLine(pts)
  // Tìm kiếm lưới độc lập không được tốt hơn nghiệm chính xác.
  let bestL1 = Infinity, bestLinf = Infinity
  for (let a = -1; a <= 4; a += 0.01) for (let c = -3; c <= 4; c += 0.01) {
    bestL1 = Math.min(bestL1, lossL1(pts, { a, c })); bestLinf = Math.min(bestLinf, lossLinf(pts, { a, c }))
  }
  assert(l1.loss <= bestL1 + 1e-9 && cheb.loss <= bestLinf + 1e-9)
  // Đối chiếu với scipy.optimize.linprog (HiGHS): tổng trị tuyệt đối nhỏ nhất bằng 3.5, đạt bởi nhiều đường
  // (chẳng hạn a = 0.9 hoặc a = 1 với c = 0.5), còn Chebyshev cho (1.625, −0.5875) với τ = 1.0875.
  near(l1.loss, 3.5); near(lossL1(pts, { a: 0.9, c: 0.5 }), 3.5); near(lossL1(pts, { a: 1, c: 0.5 }), 3.5)
  near(cheb.a, 1.625); near(cheb.c, -0.5875); near(cheb.loss, 1.0875)
  near(cheb.loss, lossLinf(pts, cheb))
  // Ngoại lai kéo đường bình phương tối thiểu nhiều hơn đường l1.
  const ls = leastSquaresLine(pts)
  assert(ls.a > l1.a)
})
