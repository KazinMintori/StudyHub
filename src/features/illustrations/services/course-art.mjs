// Pure helpers for the course illustrations. Every motif is drawn in a
// 160 × 120 view box; colours come from CSS tokens (see illustrations.css).

export const COURSE_MOTIFS = {
  'bieu-dien-tri-thuc': { motif: 'tree', tone: 'tim' },
  'toan-cho-ai': { motif: 'contour', tone: 'lam' },
  'xac-suat-thong-ke': { motif: 'bell', tone: 'hong' },
  'xu-ly-du-lieu': { motif: 'table-chart', tone: 'ngoc' },
  'vat-ly-1': { motif: 'pendulum', tone: 'cam' },
  'vat-ly-2': { motif: 'field', tone: 'vang' },
  'giai-thuat-du-lieu': { motif: 'network', tone: 'xanh' },
  dsa: { motif: 'structures', tone: 'tim' },
  'discrete-math': { motif: 'venn', tone: 'lam' },
  'triet-hoc-mac-lenin': { motif: 'book-spiral', tone: 'do' }
}

// Older course records describe their interactive illustration by name.
const ILLUSTRATION_MOTIFS = { search: 'tree', gradient: 'contour', bayes: 'bell', broadcast: 'table-chart', field: 'field', mapreduce: 'network' }

export function resolveCourseArt(course) {
  const id = typeof course === 'string' ? course : course?.id
  if (COURSE_MOTIFS[id]) return COURSE_MOTIFS[id]
  const motif = ILLUSTRATION_MOTIFS[course?.illustration]
  return { motif: motif || 'books', tone: 'tim' }
}

const round = value => Math.round(value * 10) / 10

/** Smooth path through sampled points of f on [x0, x1]. */
export function samplePath(f, x0, x1, steps = 48) {
  const points = Array.from({ length: steps + 1 }, (_, i) => {
    const x = x0 + (x1 - x0) * i / steps
    return `${round(x)},${round(f(x))}`
  })
  return `M${points[0]} L${points.slice(1).join(' ')}`
}

export const bellCurve = (mean, sigma, top, base) => x => base - (base - top) * Math.exp(-((x - mean) ** 2) / (2 * sigma ** 2))

/** Histogram bars whose heights follow the same normal curve. */
export function bellBars({ count = 9, x0 = 22, width = 11, gap = 2, base = 100, peak = 62, sigma = 1.6 } = {}) {
  const middle = (count - 1) / 2
  return Array.from({ length: count }, (_, i) => {
    const k = i - middle
    const height = round(peak * Math.exp(-(k * k) / (2 * sigma * sigma)))
    return { x: x0 + i * (width + gap), y: round(base - height), width, height, core: Math.abs(k) <= 1 }
  })
}

/** Archimedean spiral starting at (cx, cy). */
export function spiralPath(cx, cy, turns = 2.25, growth = 3.1, steps = 90) {
  const points = []
  for (let i = 0; i <= steps; i++) {
    const angle = (turns * 2 * Math.PI * i) / steps
    const radius = growth * angle
    points.push(`${round(cx + radius * Math.cos(angle - Math.PI / 2))},${round(cy + radius * Math.sin(angle - Math.PI / 2) * 0.62)}`)
  }
  return `M${points[0]} L${points.slice(1).join(' ')}`
}

/** Line from the edge of one node to the edge of another, with an arrow head. */
export function arrowBetween(from, to, gap = 2) {
  const dx = to.x - from.x, dy = to.y - from.y
  const length = Math.hypot(dx, dy) || 1
  const ux = dx / length, uy = dy / length
  const start = { x: from.x + ux * (from.r + gap), y: from.y + uy * (from.r + gap) }
  const tip = { x: to.x - ux * (to.r + gap), y: to.y - uy * (to.r + gap) }
  const size = 5.5
  const back = { x: tip.x - ux * size, y: tip.y - uy * size }
  const left = { x: back.x - uy * size * 0.55, y: back.y + ux * size * 0.55 }
  const right = { x: back.x + uy * size * 0.55, y: back.y - ux * size * 0.55 }
  return {
    line: `M${round(start.x)},${round(start.y)} L${round(back.x)},${round(back.y)}`,
    head: `M${round(tip.x)},${round(tip.y)} L${round(left.x)},${round(left.y)} L${round(right.x)},${round(right.y)} Z`
  }
}
