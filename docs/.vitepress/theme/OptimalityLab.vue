<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { contourSegments } from './contour.mjs'
import { clipPolygon, closestOnSegment, insideConvexPolygon, dot, sub, add, scale } from './convex-geometry.mjs'

// Điều kiện tối ưu (4.21): x tối ưu khi và chỉ khi ∇f(x)ᵀ(y − x) ≥ 0 với mọi y khả thi.
// Vùng tô đỏ là các điểm khả thi y với ∇f(x)ᵀ(y − x) < 0: đi về phía chúng, f giảm ngay từ đầu.
// x tối ưu đúng khi vùng này rỗng, tức đường thẳng vuông góc với gradient tựa vào đa giác tại x.
const poly = [[-2, -1.5], [1.5, -2], [2.2, 0.5], [0.5, 2], [-1.8, 1]] // lồi, ngược chiều kim đồng hồ
const Q = [[1, 0.4], [0.4, 2]]
const uid = useId()
const clip = `${uid}-opt-clip`, arrow = `${uid}-opt-arrow`
const svg = ref(null)
const view = ref(makeView({ x0: -3, x1: 3.5, y0: -2.75, y1: 3.25, width: 360, height: 332 }))
const P = p => view.value.point(p)
const project = p => {
  if (insideConvexPolygon(p, poly)) return p
  let best = null
  poly.forEach((a, i) => { const c = closestOnSegment(p, a, poly[(i + 1) % poly.length]); if (!best || c.distance < best.distance) best = c })
  return best.point
}
const state = ref({ x: [0.2, -0.4], c: [2.6, 2.2] })
const drag = createDragger(svg, view, (name, value) => {
  state.value = { ...state.value, [name]: name === 'x' ? project(value) : value }
}, { step: 0.1, snap: 0.05 })
const x = computed(() => state.value.x), c = computed(() => state.value.c)
const Qv = v => [Q[0][0] * v[0] + Q[0][1] * v[1], Q[1][0] * v[0] + Q[1][1] * v[1]]
const f = y => { const d = sub(y, c.value); return dot(d, Qv(d)) }
const grad = y => scale(2, Qv(sub(y, c.value)))
const g = computed(() => grad(x.value))
const gNorm = computed(() => Math.hypot(...g.value))
const fx = computed(() => f(x.value))
// Hàm tuyến tính nhỏ nhất tại một đỉnh của đa giác.
const worst = computed(() => Math.min(...poly.map(v => dot(g.value, sub(v, x.value)))))
// Sai số tương đối nhỏ để điểm nghiệm tính bằng lặp vẫn được nhận là tối ưu.
const optimal = computed(() => worst.value >= -1e-3 * (1 + gNorm.value))
const improving = computed(() => (gNorm.value < 1e-12 ? [] : clipPolygon(poly, g.value, dot(g.value, x.value))))
// Nghiệm thật: phương pháp gradient có chiếu với bước 1/L.
const xStar = computed(() => {
  let y = project(c.value)
  for (let k = 0; k < 400; k++) y = project(sub(y, scale(0.2, grad(y))))
  return y
})
const box = computed(() => ({ x0: view.value.x0, x1: view.value.x1, y0: view.value.y0, y1: view.value.y1, n: 70 }))
const levels = computed(() => [0.5, 2, 4.5, 8, 12.5].map(l => contourSegments(f, box.value, l)))
const ownLevel = computed(() => contourSegments(f, box.value, fx.value))
const support = computed(() => {
  if (gNorm.value < 1e-12) return null
  const u = [-g.value[1] / gNorm.value, g.value[0] / gNorm.value]
  return [add(x.value, scale(-9, u)), add(x.value, scale(9, u))]
})
const tip = computed(() => (gNorm.value < 1e-12 ? x.value : add(x.value, scale(-0.9 / gNorm.value, g.value))))
const step = 0.2
const pgPoint = computed(() => project(sub(x.value, scale(step, g.value))))
const pgMove = computed(() => Math.hypot(...sub(pgPoint.value, x.value)))
const line = s => `${P(s[0])[0]},${P(s[0])[1]} ${P(s[1])[0]},${P(s[1])[1]}`
</script>

<template>
  <figure class="study-lab" aria-label="Điều kiện tối ưu bậc nhất trên một đa giác">
    <p class="lab-title">Khi nào không còn hướng khả thi nào làm f giảm</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Đa giác khả thi, đường mức của f, điểm x, hướng ngược gradient và vùng các điểm khả thi tốt hơn theo bậc nhất" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs>
        <clipPath :id="clip"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath>
        <marker :id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="lab-arrow-accent" /></marker>
      </defs>
      <g :clip-path="`url(#${clip})`">
        <polygon :points="poly.map(p => P(p).join(',')).join(' ')" class="lab-region" />
        <polygon v-if="improving.length > 2" :points="improving.map(p => P(p).join(',')).join(' ')" class="lab-bad-fill" style="stroke: none; opacity: 0.9" />
        <g v-for="(segs, k) in levels" :key="`l${k}`"><polyline v-for="(s, i) in segs" :key="i" :points="line(s)" class="lab-line" style="stroke-width: 1.1; opacity: 0.5" /></g>
        <polyline v-for="(s, i) in ownLevel" :key="`o${i}`" :points="line(s)" class="lab-warn" />
        <line v-if="support" :x1="P(support[0])[0]" :y1="P(support[0])[1]" :x2="P(support[1])[0]" :y2="P(support[1])[1]" class="lab-guide" />
        <line v-if="gNorm > 1e-12" :x1="P(x)[0]" :y1="P(x)[1]" :x2="P(tip)[0]" :y2="P(tip)[1]" class="lab-accent" :marker-end="`url(#${arrow})`" />
        <circle :cx="P(xStar)[0]" :cy="P(xStar)[1]" r="7" class="lab-dot-hollow" />
        <circle :cx="P(c)[0]" :cy="P(c)[1]" r="7" class="lab-handle lab-handle-alt" tabindex="0" role="slider" aria-label="Tâm c của hàm mục tiêu" :aria-valuetext="fmtPoint(c)" @pointerdown="drag.start('c', $event)" @keydown="drag.key('c', c, $event)" />
        <circle :cx="P(x)[0]" :cy="P(x)[1]" r="8" class="lab-handle" tabindex="0" role="slider" aria-label="Điểm khả thi x" :aria-valuetext="fmtPoint(x)" @pointerdown="drag.start('x', $event)" @keydown="drag.key('x', x, $event)" />
      </g>
    </svg>
    <p class="lab-legend"><span class="legend-accent">hướng −∇f(x)</span><span class="legend-warn">đường mức qua x</span><span class="legend-bad">điểm khả thi tốt hơn theo bậc nhất</span><span class="legend-guide">đường vuông góc với gradient</span></p>
    <div class="lab-buttons">
      <button type="button" @click="state = { ...state, x: xStar }">Đặt x vào nghiệm</button>
      <button type="button" @click="state = { ...state, x: pgPoint }">Đi một bước gradient có chiếu</button>
    </div>
    <div class="lab-readout" role="status">
      <p>f(y) = (y − c)ᵀQ(y − c) với c = {{ fmtPoint(c) }} (chấm vàng, kéo được). Tại x = {{ fmtPoint(x) }}: f(x) = {{ fmt(fx, 3) }}, ∇f(x) = {{ fmtPoint(g, 2) }}.</p>
      <p>Giá trị nhỏ nhất của ∇f(x)ᵀ(y − x) trên đa giác là {{ fmt(worst, 3) }}, đạt tại một đỉnh.</p>
      <p v-if="optimal" class="is-good">Không còn điểm khả thi nào làm ∇f(x)ᵀ(y − x) âm: x tối ưu, và đường nét đứt tựa vào đa giác tại x.</p>
      <p v-else class="is-bad">Đi từ x về phía bất kỳ điểm nào trong vùng đỏ, f giảm ngay từ đầu, nên x chưa tối ưu. Nghiệm thật là vòng tròn rỗng tại {{ fmtPoint(xStar) }}.</p>
      <p>Một bước gradient có chiếu với độ dài bước {{ step }} đưa x tới {{ fmtPoint(pgPoint) }}, cách x một khoảng {{ fmt(pgMove, 3) }}{{ pgMove < 1e-3 ? ': x là điểm bất động, đúng như điều kiện tối ưu dự báo' : '' }}.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo x dọc theo biên đa giác tới vòng tròn rỗng. Vùng đỏ co lại thế nào, và đường mức vàng nằm ra sao so với đa giác lúc vùng đỏ biến mất?</li>
        <li>Kéo tâm c vào bên trong đa giác. Nghiệm nằm ở đâu, và điều kiện tối ưu trở thành gì?</li>
        <li>Đặt c sao cho nghiệm rơi đúng vào một đỉnh của đa giác. Lúc đó hướng −∇f(x) nằm trong vùng nào?</li>
      </ol>
    </details>
  </figure>
</template>
