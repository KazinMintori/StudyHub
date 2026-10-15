// Hàm hình học thuần, không phụ thuộc trình duyệt, dùng chung cho các mô phỏng của chương tập lồi và hàm lồi.
// Mọi phép tính ở đây được kiểm tra trong scripts/tests/convex-geometry.test.mjs.

export const add = (a, b) => a.map((x, i) => x + b[i])
export const sub = (a, b) => a.map((x, i) => x - b[i])
export const scale = (s, a) => a.map(x => s * x)
export const dot = (a, b) => a.reduce((sum, x, i) => sum + x * b[i], 0)
export const norm2 = a => Math.sqrt(dot(a, a))
export const cross2 = (a, b) => a[0] * b[1] - a[1] * b[0]
export const lerp = (a, b, theta) => add(scale(theta, a), scale(1 - theta, b))

// Tổ hợp tuyến tính sum_i w_i p_i. Khi tổng trọng số bằng 1 thì đây là một tổ hợp affine.
export function combination(points, weights) {
  return points.reduce((acc, p, i) => add(acc, scale(weights[i], p)), points[0].map(() => 0))
}

// Tọa độ trọng tâm (barycentric) của p theo tam giác a, b, c: p = t1 a + t2 b + t3 c, t1 + t2 + t3 = 1.
export function barycentric(p, a, b, c) {
  const det = cross2(sub(b, a), sub(c, a))
  if (Math.abs(det) < 1e-12) return null
  const t2 = cross2(sub(p, a), sub(c, a)) / det
  const t3 = cross2(sub(b, a), sub(p, a)) / det
  return [1 - t2 - t3, t2, t3]
}

// Bao lồi theo thuật toán monotone chain, trả về các đỉnh theo chiều ngược kim đồng hồ.
export function convexHull(points) {
  const pts = [...new Map(points.map(p => [`${p[0]},${p[1]}`, p])).values()].sort((p, q) => p[0] - q[0] || p[1] - q[1])
  if (pts.length <= 2) return pts
  const half = list => {
    const out = []
    for (const p of list) {
      while (out.length >= 2 && cross2(sub(out.at(-1), out.at(-2)), sub(p, out.at(-2))) <= 1e-12) out.pop()
      out.push(p)
    }
    return out
  }
  const lower = half(pts), upper = half([...pts].reverse())
  return [...lower.slice(0, -1), ...upper.slice(0, -1)]
}

// Đa giác lồi theo chiều ngược kim đồng hồ: p ở trong (kể cả biên) khi nằm bên trái mọi cạnh.
export function insideConvexPolygon(p, poly, tolerance = 1e-9) {
  if (poly.length < 3) return false
  return poly.every((a, i) => cross2(sub(poly[(i + 1) % poly.length], a), sub(p, a)) >= -tolerance)
}

// Đa giác bất kỳ, dùng tia ngang (ray casting).
export function insidePolygon(p, poly) {
  let inside = false
  for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {
    const [xi, yi] = poly[i], [xj, yj] = poly[j]
    if ((yi > p[1]) !== (yj > p[1]) && p[0] < ((xj - xi) * (p[1] - yi)) / (yj - yi) + xi) inside = !inside
  }
  return inside
}

// Cắt đa giác bởi nửa mặt phẳng a^T x <= b (Sutherland–Hodgman). Dùng để vẽ đa diện trong một khung hữu hạn.
export function clipPolygon(poly, a, b) {
  const out = []
  const value = p => dot(a, p) - b
  for (let i = 0; i < poly.length; i++) {
    const p = poly[i], q = poly[(i + 1) % poly.length]
    const vp = value(p), vq = value(q)
    if (vp <= 1e-12) out.push(p)
    if ((vp < -1e-12 && vq > 1e-12) || (vp > 1e-12 && vq < -1e-12)) {
      const t = vp / (vp - vq)
      out.push(add(p, scale(t, sub(q, p))))
    }
  }
  return out
}
export function polyhedronInBox(halfspaces, box = [-10, 10, -10, 10]) {
  const [x0, x1, y0, y1] = box
  let poly = [[x0, y0], [x1, y0], [x1, y1], [x0, y1]]
  for (const { a, b } of halfspaces) { poly = clipPolygon(poly, a, b); if (!poly.length) break }
  return poly
}

// Trị riêng và vector riêng của ma trận đối xứng 2x2 [[p, q], [q, r]], trị riêng giảm dần.
export function eigSym2(p, q, r) {
  const mean = (p + r) / 2, radius = Math.hypot((p - r) / 2, q)
  const l1 = mean + radius, l2 = mean - radius
  let v1
  if (Math.abs(q) > 1e-14) v1 = [l1 - r, q]
  else v1 = p >= r ? [1, 0] : [0, 1]
  const n = norm2(v1)
  v1 = scale(1 / n, v1)
  return { values: [l1, l2], vectors: [v1, [-v1[1], v1[0]]] }
}
export const isPsd2 = (p, q, r, tolerance = 1e-12) => p >= -tolerance && r >= -tolerance && p * r - q * q >= -tolerance
export const isPd2 = (p, q, r) => p > 0 && p * r - q * q > 0

// Ma trận P = R diag(l1, l2) R^T với R là phép quay góc phi. Trả về [[p, q], [q, r]].
export function fromEigen(l1, l2, phi) {
  const c = Math.cos(phi), s = Math.sin(phi)
  return [[l1 * c * c + l2 * s * s, (l1 - l2) * c * s], [(l1 - l2) * c * s, l1 * s * s + l2 * c * c]]
}
// Căn bậc hai đối xứng P^{1/2} của ma trận PSD 2x2.
export function sqrtPsd2(P) {
  const { values, vectors } = eigSym2(P[0][0], P[0][1], P[1][1])
  const s = values.map(v => Math.sqrt(Math.max(v, 0)))
  const [u, w] = vectors
  return [[s[0] * u[0] * u[0] + s[1] * w[0] * w[0], s[0] * u[0] * u[1] + s[1] * w[0] * w[1]],
          [s[0] * u[1] * u[0] + s[1] * w[1] * w[0], s[0] * u[1] * u[1] + s[1] * w[1] * w[1]]]
}
export const matVec2 = (M, v) => [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]]
// Biên ellipsoid {x : (x - c)^T P^{-1} (x - c) <= 1} = {c + P^{1/2} u : ||u|| <= 1}.
export function ellipseBoundary(P, center = [0, 0], n = 96) {
  const A = sqrtPsd2(P)
  return Array.from({ length: n }, (_, i) => {
    const t = (2 * Math.PI * i) / n
    return add(center, matVec2(A, [Math.cos(t), Math.sin(t)]))
  })
}

// Chuẩn l_p trong R^n (p >= 1 là chuẩn; 0 < p < 1 vẫn tính được biểu thức nhưng không phải chuẩn).
export function pNorm(x, p) {
  if (p === Infinity) return Math.max(...x.map(Math.abs))
  return Math.pow(x.reduce((s, v) => s + Math.pow(Math.abs(v), p), 0), 1 / p)
}
// Biên tập {x in R^2 : ||x||_p <= 1}: đi theo hướng góc t và co về độ dài 1/||(cos t, sin t)||_p.
export function pBallBoundary(p, n = 180) {
  return Array.from({ length: n }, (_, i) => {
    const t = (2 * Math.PI * i) / n
    const d = [Math.cos(t), Math.sin(t)]
    return scale(1 / pNorm(d, p), d)
  })
}

// Đoạn [a, b] có nằm trong tập không? inside là hàm thành viên. Trả về các tham số t trong [0, 1] bị lọt ra ngoài.
export function segmentOutside(inside, a, b, samples = 200) {
  const out = []
  for (let i = 0; i <= samples; i++) {
    const t = i / samples
    if (!inside(add(a, scale(t, sub(b, a))))) out.push(t)
  }
  return out
}

// Hai hình tròn: nếu rời nhau, cặp điểm gần nhất nằm trên đường nối tâm và siêu phẳng trung trực của cặp đó tách hai hình.
export function separateDisks(c1, r1, c2, r2) {
  const d = sub(c2, c1), dist = norm2(d)
  if (dist <= r1 + r2 || dist < 1e-12) return { disjoint: false, gap: dist - r1 - r2 }
  const u = scale(1 / dist, d)
  const p = add(c1, scale(r1, u)), q = sub(c2, scale(r2, u))
  const a = sub(q, p), b = (dot(q, q) - dot(p, p)) / 2
  return { disjoint: true, gap: dist - r1 - r2, p, q, a, b }
}

// Khoảng cách từ điểm tới đoạn thẳng và điểm gần nhất trên đoạn.
export function closestOnSegment(x, a, b) {
  const d = sub(b, a), len2 = dot(d, d)
  const t = len2 < 1e-15 ? 0 : Math.min(1, Math.max(0, dot(sub(x, a), d) / len2))
  const point = add(a, scale(t, d))
  return { point, t, distance: norm2(sub(x, point)) }
}
// Cặp điểm gần nhất giữa hai đa giác lồi rời nhau (đủ dùng cho đa giác nhỏ trong mô phỏng).
export function closestPolygons(P, Q) {
  let best = { distance: Infinity }
  const consider = (x, poly, xFromP) => {
    for (let i = 0; i < poly.length; i++) {
      const c = closestOnSegment(x, poly[i], poly[(i + 1) % poly.length])
      if (c.distance < best.distance) best = xFromP ? { p: x, q: c.point, distance: c.distance } : { p: c.point, q: x, distance: c.distance }
    }
  }
  P.forEach(x => consider(x, Q, true))
  Q.forEach(x => consider(x, P, false))
  return best
}
export function polygonsIntersect(P, Q) {
  if (P.some(p => insideConvexPolygon(p, Q)) || Q.some(q => insideConvexPolygon(q, P))) return true
  const segmentsCross = (a, b, c, d) => {
    const o = (p, q, r) => Math.sign(cross2(sub(q, p), sub(r, p)))
    return o(a, b, c) * o(a, b, d) < 0 && o(c, d, a) * o(c, d, b) < 0
  }
  return P.some((a, i) => Q.some((c, j) => segmentsCross(a, P[(i + 1) % P.length], c, Q[(j + 1) % Q.length])))
}

// Phép phối cảnh P(z, t) = z / t trên miền t > 0, và trọng số mới mu của ảnh một điểm trên đoạn.
export const perspective = ([z, t]) => { if (!(t > 0)) throw new RangeError('Perspective needs t > 0'); return z / t }
export const perspectiveWeight = (theta, t1, t2) => (theta * t1) / (theta * t1 + (1 - theta) * t2)

// Thứ tự theo từng thành phần trong R^2 (nón R^2_+): x <= y khi y - x thuộc nón.
export const precedes = (x, y) => x.every((v, i) => v <= y[i] + 1e-12)
export const minimalIndices = points => points.map((x, i) => i).filter(i => !points.some((y, j) => j !== i && precedes(y, points[i]) && !precedes(points[i], y)))
export const minimumIndex = points => points.findIndex(x => points.every(y => precedes(x, y)))
// Phần tử của tập hữu hạn làm lambda^T z nhỏ nhất (có thể nhiều phần tử cùng đạt).
export function weightedMinimizers(points, lambda) {
  const values = points.map(p => dot(lambda, p)), best = Math.min(...values)
  return values.map((v, i) => [v, i]).filter(([v]) => Math.abs(v - best) < 1e-9).map(([, i]) => i)
}

// Nón sinh bởi hai vector trong R^2 và nón đối ngẫu của nó, mô tả bằng góc (radian) của hai tia biên.
export const angleOf = v => Math.atan2(v[1], v[0])
export function dualOfPlanarCone(v1, v2) {
  // Với nón nhọn sinh bởi v1, v2 (góc giữa chúng < pi), K* sinh bởi hai pháp tuyến hướng vào trong.
  const turn = cross2(v1, v2) >= 0 ? 1 : -1
  const n1 = turn > 0 ? [-v1[1], v1[0]] : [v1[1], -v1[0]]
  const n2 = turn > 0 ? [v2[1], -v2[0]] : [-v2[1], v2[0]]
  return [n1, n2]
}
export const inDualCone = (y, generators) => generators.every(g => dot(y, g) >= -1e-12)
