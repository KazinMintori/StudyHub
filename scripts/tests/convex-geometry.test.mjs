import test from 'node:test'
import assert from 'node:assert/strict'
import {
  combination, barycentric, convexHull, insideConvexPolygon, insidePolygon, polyhedronInBox,
  eigSym2, isPsd2, isPd2, fromEigen, sqrtPsd2, matVec2, ellipseBoundary, pNorm, pBallBoundary,
  segmentOutside, separateDisks, closestPolygons, polygonsIntersect, perspective, perspectiveWeight,
  minimalIndices, minimumIndex, weightedMinimizers, dualOfPlanarCone, inDualCone, dot, sub, norm2
} from '../../docs/.vitepress/theme/convex-geometry.mjs'

const near = (a, b, tolerance = 1e-9) => assert(Math.abs(a - b) <= tolerance, `${a} != ${b}`)
const nearVec = (u, v, tolerance = 1e-9) => u.forEach((x, i) => near(x, v[i], tolerance))

test('Affine combinations and barycentric coordinates agree', () => {
  const a = [0, 0], b = [4, 0], c = [0, 3]
  nearVec(combination([a, b, c], [0.25, 0.25, 0.5]), [1, 1.5])
  nearVec(barycentric([1, 1.5], a, b, c), [0.25, 0.25, 0.5])
  // Một điểm ngoài tam giác có ít nhất một tọa độ âm nhưng tổng vẫn bằng 1.
  const w = barycentric([5, 2], a, b, c)
  near(w.reduce((s, x) => s + x, 0), 1)
  assert(Math.min(...w) < 0)
  assert.equal(barycentric([1, 1], [0, 0], [1, 1], [2, 2]), null)
})

test('Convex hull drops interior points and returns counter-clockwise vertices', () => {
  const hull = convexHull([[0, 0], [2, 0], [2, 2], [0, 2], [1, 1], [1, 0]])
  assert.deepEqual(hull, [[0, 0], [2, 0], [2, 2], [0, 2]])
  assert(insideConvexPolygon([1, 1], hull) && insideConvexPolygon([2, 1], hull) && !insideConvexPolygon([3, 1], hull))
  // Hình sao năm cánh không lồi: tâm ở trong, đầu một cánh ở trong, điểm giữa hai đầu cánh có thể ra ngoài.
  const star = Array.from({ length: 10 }, (_, i) => { const r = i % 2 ? 0.4 : 1, t = Math.PI / 2 + i * Math.PI / 5; return [r * Math.cos(t), r * Math.sin(t)] })
  assert(insidePolygon([0, 0], star))
  assert(!insidePolygon([0.5 * (star[0][0] + star[2][0]), 0.5 * (star[0][1] + star[2][1])], star))
})

test('Clipping by halfspaces reproduces the vertices of a small polyhedron', () => {
  // x >= 0, y >= 0, x + y <= 5, 2x + y <= 8 có các đỉnh (0,0), (4,0), (3,2), (0,5).
  const poly = polyhedronInBox([{ a: [-1, 0], b: 0 }, { a: [0, -1], b: 0 }, { a: [1, 1], b: 5 }, { a: [2, 1], b: 8 }])
  const keys = new Set(poly.map(p => p.map(v => Math.round(v * 1e9) / 1e9).join(',')))
  for (const v of ['0,0', '4,0', '3,2', '0,5']) assert(keys.has(v), v)
  assert.equal(polyhedronInBox([{ a: [1, 0], b: -1 }, { a: [-1, 0], b: -1 }]).length, 0)
})

test('Symmetric 2x2 eigen-decomposition, PSD tests and matrix square root', () => {
  const { values, vectors } = eigSym2(2, 1, 2)
  nearVec(values, [3, 1]); near(Math.abs(dot(vectors[0], [1, 1])) / Math.SQRT2, 1)
  assert(isPsd2(1, -1, 1) && !isPd2(1, -1, 1) && !isPsd2(1, 2, 1) && isPd2(2, 1, 2))
  const P = fromEigen(4, 1, Math.PI / 6), A = sqrtPsd2(P)
  const AA = [[A[0][0] * A[0][0] + A[0][1] * A[1][0], A[0][0] * A[0][1] + A[0][1] * A[1][1]], [A[1][0] * A[0][0] + A[1][1] * A[1][0], A[1][0] * A[0][1] + A[1][1] * A[1][1]]]
  nearVec(AA[0], P[0]); nearVec(AA[1], P[1])
  // Mọi điểm biên thỏa (x - c)^T P^{-1} (x - c) = 1.
  const det = P[0][0] * P[1][1] - P[0][1] ** 2, Pinv = [[P[1][1] / det, -P[0][1] / det], [-P[0][1] / det, P[0][0] / det]]
  for (const x of ellipseBoundary(P, [1, -1], 24)) { const d = sub(x, [1, -1]); near(dot(d, matVec2(Pinv, d)), 1, 1e-9) }
  // Bán trục bằng căn bậc hai trị riêng: điểm xa tâm nhất cách tâm 2.
  near(Math.max(...ellipseBoundary(P, [0, 0], 720).map(norm2)), 2, 1e-4)
})

test('l_p balls: values, boundary and the failure of convexity for p < 1', () => {
  near(pNorm([3, -4], 1), 7); near(pNorm([3, -4], 2), 5); near(pNorm([3, -4], Infinity), 4)
  for (const p of [0.5, 1, 2, 3]) for (const x of pBallBoundary(p, 36)) near(pNorm(x, p), 1, 1e-9)
  // Với p = 1/2, hai điểm (1,0) và (0,1) thuộc quả cầu nhưng trung điểm thì không: ||(1/2,1/2)||_{1/2} = 2.
  near(pNorm([0.5, 0.5], 0.5), 2)
  const inHalf = x => pNorm(x, 0.5) <= 1 + 1e-12
  assert(segmentOutside(inHalf, [1, 0], [0, 1]).length > 0)
  assert.equal(segmentOutside(x => pNorm(x, 1) <= 1 + 1e-12, [1, 0], [0, 1]).length, 0)
})

test('Separating two disks and two polygons', () => {
  const s = separateDisks([0, 0], 1, [4, 0], 1)
  assert(s.disjoint); nearVec(s.p, [1, 0]); nearVec(s.q, [3, 0]); near(s.b / s.a[0], 2)
  assert(!separateDisks([0, 0], 2, [3, 0], 1.5).disjoint)
  const P = [[0, 0], [1, 0], [1, 1], [0, 1]], Q = [[3, 0], [4, 0], [4, 1], [3, 1]]
  near(closestPolygons(P, Q).distance, 2)
  assert(!polygonsIntersect(P, Q) && polygonsIntersect(P, [[0.5, 0.5], [2, 0.5], [2, 2]]))
})

test('Perspective keeps segments but changes their parameter', () => {
  near(perspective([2, 2]), 1); near(perspective([3, 3]), 1); assert.throws(() => perspective([1, 0]))
  // u = (0,1), v = (4,2): theta = 1/2 cho mu = 1/3 và ảnh của trung điểm là 4/3.
  near(perspectiveWeight(0.5, 1, 2), 1 / 3)
  near(perspective([2, 1.5]), 4 / 3)
  for (let i = 0; i <= 10; i++) { const mu = perspectiveWeight(i / 10, 1, 2); assert(mu >= 0 && mu <= 1) }
})

test('Minimum, minimal elements and weighted scalarization', () => {
  const pts = [[1, 6], [2, 4], [4, 2], [3, 6], [5, 4]]
  assert.deepEqual(minimalIndices(pts), [0, 1, 2]); assert.equal(minimumIndex(pts), -1)
  assert.equal(minimumIndex([[1, 2], [2, 3], [1, 5]]), 0)
  assert.deepEqual(weightedMinimizers(pts, [3, 1]), [0])
  assert.deepEqual(weightedMinimizers(pts, [3, 2]), [1])
  assert.deepEqual(weightedMinimizers(pts, [1, 3]), [2])
})

test('Dual of a planar cone', () => {
  const [n1, n2] = dualOfPlanarCone([1, 0], [1, 1])
  // K = cone{(1,0),(1,1)} cho K* = {y : y1 >= 0, y1 + y2 >= 0}, sinh bởi (0,1) và (1,-1).
  near(dot(n1, [1, 0]), 0); near(dot(n2, [1, 1]), 0)
  assert(inDualCone(n1, [[1, 0], [1, 1]]) && inDualCone(n2, [[1, 0], [1, 1]]))
  assert(inDualCone([1, 0], [[1, 0], [1, 1]]) && !inDualCone([-1, 2], [[1, 0], [1, 1]]))
})
