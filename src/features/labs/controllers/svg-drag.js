// Kéo điểm trong SVG bằng chuột, chạm hoặc bàn phím. Không chạm tới window khi dựng trang tĩnh.
export function svgPoint(svg, event) {
  const matrix = svg.getScreenCTM()
  if (!matrix) return null
  const point = svg.createSVGPoint()
  point.x = event.clientX
  point.y = event.clientY
  return point.matrixTransform(matrix.inverse())
}

// view: { x0, x1, y0, y1, width, height, pad } ánh xạ hệ tọa độ toán học sang tọa độ SVG (trục y hướng lên).
export function makeView({ x0, x1, y0, y1, width = 400, height = 300, pad = 0 }) {
  const sx = x => pad + ((x - x0) / (x1 - x0)) * (width - 2 * pad)
  const sy = y => height - pad - ((y - y0) / (y1 - y0)) * (height - 2 * pad)
  const wx = px => x0 + ((px - pad) / (width - 2 * pad)) * (x1 - x0)
  const wy = py => y0 + ((height - pad - py) / (height - 2 * pad)) * (y1 - y0)
  const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v))
  return { x0, x1, y0, y1, width, height, sx, sy, wx, wy, point: p => [sx(p[0]), sy(p[1])], toWorld: (px, py) => [clamp(wx(px), x0, x1), clamp(wy(py), y0, y1)] }
}

// onMove(name, worldPoint) được gọi khi một tay nắm được kéo; step là bước di chuyển bằng phím mũi tên.
export function createDragger(svgRef, view, onMove, { step = 0.1, snap = 0 } = {}) {
  let active = null
  const round = v => (snap ? Math.round(v / snap) * snap : v)
  return {
    start(name, event) {
      active = name
      event.currentTarget?.setPointerCapture?.(event.pointerId)
      event.preventDefault()
    },
    move(event) {
      if (!active || !svgRef.value) return
      const p = svgPoint(svgRef.value, event)
      if (!p) return
      const [x, y] = view.value.toWorld(p.x, p.y)
      onMove(active, [round(x), round(y)])
    },
    end() { active = null },
    key(name, current, event) {
      const moves = { ArrowLeft: [-step, 0], ArrowRight: [step, 0], ArrowUp: [0, step], ArrowDown: [0, -step] }
      const d = moves[event.key]
      if (!d) return
      event.preventDefault()
      const v = view.value
      onMove(name, [Math.min(v.x1, Math.max(v.x0, round(current[0] + d[0]))), Math.min(v.y1, Math.max(v.y0, round(current[1] + d[1])))])
    }
  }
}

export const fmt = (x, digits = 2) => {
  if (!Number.isFinite(x)) return '—'
  const v = Math.abs(x) < 5 * 10 ** -(digits + 1) ? 0 : x
  return v.toFixed(digits).replace('-', '−')
}
export const fmtPoint = (p, digits = 2) => `(${p.map(v => fmt(v, digits)).join(', ')})`
