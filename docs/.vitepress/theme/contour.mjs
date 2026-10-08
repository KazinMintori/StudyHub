// Đường đồng mức của hàm hai biến bằng thuật toán marching squares trên lưới đều.
// Trả về các đoạn thẳng [[x1, y1], [x2, y2]] xấp xỉ tập {x : f(x) = level}.
export function contourSegments(f, { x0, x1, y0, y1, n = 60 }, level) {
  const hx = (x1 - x0) / n, hy = (y1 - y0) / n
  const values = []
  for (let j = 0; j <= n; j++) {
    const row = []
    for (let i = 0; i <= n; i++) {
      const v = f([x0 + i * hx, y0 + j * hy])
      row.push(Number.isFinite(v) ? v : NaN)
    }
    values.push(row)
  }
  const segments = []
  const lerp = (pa, pb, va, vb) => {
    const t = (level - va) / (vb - va)
    return [pa[0] + t * (pb[0] - pa[0]), pa[1] + t * (pb[1] - pa[1])]
  }
  for (let j = 0; j < n; j++) {
    for (let i = 0; i < n; i++) {
      const corners = [
        { p: [x0 + i * hx, y0 + j * hy], v: values[j][i] },
        { p: [x0 + (i + 1) * hx, y0 + j * hy], v: values[j][i + 1] },
        { p: [x0 + (i + 1) * hx, y0 + (j + 1) * hy], v: values[j + 1][i + 1] },
        { p: [x0 + i * hx, y0 + (j + 1) * hy], v: values[j + 1][i] }
      ]
      if (corners.some(c => Number.isNaN(c.v))) continue
      const crossings = []
      for (let k = 0; k < 4; k++) {
        const a = corners[k], b = corners[(k + 1) % 4]
        if ((a.v < level) !== (b.v < level)) crossings.push(lerp(a.p, b.p, a.v, b.v))
      }
      if (crossings.length === 2) segments.push(crossings)
      else if (crossings.length === 4) {
        // Ô yên ngựa: dùng giá trị trung bình ở tâm để chọn cách nối.
        const center = (corners[0].v + corners[1].v + corners[2].v + corners[3].v) / 4
        if ((center < level) === (corners[0].v < level)) segments.push([crossings[0], crossings[3]], [crossings[1], crossings[2]])
        else segments.push([crossings[0], crossings[1]], [crossings[2], crossings[3]])
      }
    }
  }
  return segments
}
