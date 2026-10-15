// Khớp đường thẳng y = a t + c theo ba tiêu chí, tính chính xác cho số điểm nhỏ.
// Dùng trong mô phỏng của chủ đề "Bình phương tối thiểu và quy hoạch tuyến tính".

// Bình phương tối thiểu: giải hệ phương trình chuẩn 2x2.
export function leastSquaresLine(points) {
  const n = points.length
  const st = points.reduce((s, [t]) => s + t, 0), sy = points.reduce((s, [, y]) => s + y, 0)
  const stt = points.reduce((s, [t]) => s + t * t, 0), sty = points.reduce((s, [t, y]) => s + t * y, 0)
  const det = stt * n - st * st
  if (Math.abs(det) < 1e-12) return null
  const a = (sty * n - st * sy) / det
  const c = (stt * sy - st * sty) / det
  return { a, c }
}

export const residuals = (points, { a, c }) => points.map(([t, y]) => a * t + c - y)
export const lossL2 = (points, line) => residuals(points, line).reduce((s, r) => s + r * r, 0)
export const lossL1 = (points, line) => residuals(points, line).reduce((s, r) => s + Math.abs(r), 0)
export const lossLinf = (points, line) => Math.max(...residuals(points, line).map(Math.abs))

// Tổng trị tuyệt đối: bài toán LP này luôn có một nghiệm đi qua ít nhất hai điểm dữ liệu
// (một đỉnh của miền khả thi), nên duyệt mọi đường thẳng qua hai điểm có hoành độ khác nhau là đủ.
export function l1Line(points) {
  let best = null
  for (let i = 0; i < points.length; i++) for (let j = i + 1; j < points.length; j++) {
    const [t1, y1] = points[i], [t2, y2] = points[j]
    if (Math.abs(t2 - t1) < 1e-12) continue
    const a = (y2 - y1) / (t2 - t1), line = { a, c: y1 - a * t1 }
    const loss = lossL1(points, line)
    if (!best || loss < best.loss - 1e-12) best = { ...line, loss }
  }
  return best
}

// Sai số lớn nhất (xấp xỉ Chebyshev): minimize τ với −τ ≤ a t_i + c − y_i ≤ τ.
// Nghiệm đạt tại một đỉnh của đa diện trong R^3, xác định bởi ba ràng buộc chặt.
function solve3(M, v) {
  const det = m => m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
  const d = det(M)
  if (Math.abs(d) < 1e-12) return null
  return [0, 1, 2].map(k => det(M.map((row, i) => row.map((x, j) => (j === k ? v[i] : x)))) / d)
}
export function chebyshevLine(points) {
  // Mỗi ràng buộc có dạng s (a t + c − y) − τ ≤ 0 với s = ±1, tức hàng [s t, s, −1] và vế phải s y.
  const rows = points.flatMap(([t, y]) => [1, -1].map(s => ({ coef: [s * t, s, -1], rhs: s * y })))
  let best = null
  for (let i = 0; i < rows.length; i++) for (let j = i + 1; j < rows.length; j++) for (let k = j + 1; k < rows.length; k++) {
    const sol = solve3([rows[i].coef, rows[j].coef, rows[k].coef], [rows[i].rhs, rows[j].rhs, rows[k].rhs])
    if (!sol) continue
    const [a, c, tau] = sol
    if (rows.some(r => r.coef[0] * a + r.coef[1] * c + r.coef[2] * tau > r.rhs + 1e-9)) continue
    if (!best || tau < best.loss - 1e-12) best = { a, c, loss: tau }
  }
  return best
}
