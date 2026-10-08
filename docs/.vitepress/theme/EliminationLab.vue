<script setup>
import { computed, ref } from 'vue'
import { makeView, fmt, fmtPoint } from './svg-drag'

// Khử một ràng buộc đẳng thức tuyến tính (ví dụ tự đặt của chủ đề 2, Lecture 02).
// f(x) = (x₁ − 2)² + 2(x₂ − 1)², ràng buộc aᵀx = b với a = (cos θ, sin θ).
// Mọi điểm trên đường viết được thành x = x₀ + z·d, x₀ = b·a, d = (−sin θ, cos θ), nên bài toán
// hai biến có ràng buộc trở thành bài toán một biến z không ràng buộc: g(z) = f(x₀ + z d).
const C = [2, 1], Dg = [1, 2]
const f = (p) => Dg[0] * (p[0] - C[0]) ** 2 + Dg[1] * (p[1] - C[1]) ** 2
const deg = ref(45), b = ref(0.71), z = ref(-1.2)
const showGrad = ref(true)
const th = computed(() => (deg.value * Math.PI) / 180)
const a = computed(() => [Math.cos(th.value), Math.sin(th.value)])
const d = computed(() => [-Math.sin(th.value), Math.cos(th.value)])
const x0 = computed(() => [b.value * a.value[0], b.value * a.value[1]])
const at = (t) => [x0.value[0] + t * d.value[0], x0.value[1] + t * d.value[1]]
const g = (t) => f(at(t))
// g là parabol theo z: z* = dᵀD(c − x₀) / dᵀDd.
const zStar = computed(() => {
  const dd = d.value, xx = x0.value
  return (Dg[0] * dd[0] * (C[0] - xx[0]) + Dg[1] * dd[1] * (C[1] - xx[1])) / (Dg[0] * dd[0] ** 2 + Dg[1] * dd[1] ** 2)
})
const xStar = computed(() => at(zStar.value))
const fStar = computed(() => f(xStar.value))
const grad = computed(() => [2 * Dg[0] * (xStar.value[0] - C[0]), 2 * Dg[1] * (xStar.value[1] - C[1])])
const nu = computed(() => grad.value[0] * a.value[0] + grad.value[1] * a.value[1])
const cur = computed(() => at(z.value))

const view = makeView({ x0: -1.5, x1: 4.5, y0: -2, y1: 3.48, width: 460, height: 420 })
const P = (p) => [view.sx(p[0]), view.sy(p[1])]
const ellipse = (L) => Array.from({ length: 121 }, (_, i) => {
  const t = (i / 120) * 2 * Math.PI
  return P([C[0] + Math.sqrt(L / Dg[0]) * Math.cos(t), C[1] + Math.sqrt(L / Dg[1]) * Math.sin(t)]).join(',')
}).join(' ')
const levels = [0.5, 1.5, 3, 5, 8, 12]
const lineEnds = computed(() => [P(at(-8)), P(at(8))])
// Đồ thị nhỏ của g(z) trên đoạn z ∈ [−4, 4].
const Z = [-4, 4]
const gView = computed(() => {
  const ys = Array.from({ length: 161 }, (_, i) => g(Z[0] + (i / 160) * (Z[1] - Z[0])))
  const lo = Math.min(...ys), hi = Math.min(Math.max(...ys), lo + 30)
  return makeView({ x0: Z[0], x1: Z[1], y0: lo - 0.08 * (hi - lo), y1: hi, width: 460, height: 150 })
})
const gCurve = computed(() => Array.from({ length: 161 }, (_, i) => {
  const t = Z[0] + (i / 160) * (Z[1] - Z[0])
  return `${gView.value.sx(t)},${gView.value.sy(Math.min(gView.value.y1, g(t)))}`
}).join(' '))
const arrowEnd = computed(() => {
  const s = 0.18, gr = grad.value
  return [xStar.value[0] + s * gr[0], xStar.value[1] + s * gr[1]]
})
</script>

<template>
  <figure class="study-lab" aria-label="Khử một ràng buộc đẳng thức tuyến tính bằng cách tham số hóa đường thẳng">
    <p class="lab-title">Đi dọc ràng buộc thay vì giữ ràng buộc</p>
    <p class="lab-lead">Các đường ellipse là đường mức của f. Mọi điểm khả thi nằm trên đường thẳng aᵀx = b và được mô tả bởi một số duy nhất z, nên bài toán còn lại chỉ là cực tiểu một parabol theo z.</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Đường mức ellipse của f, đường ràng buộc, điểm x theo tham số z và điểm tối ưu nơi đường mức tiếp xúc ràng buộc">
      <line v-for="t in [-1, 0, 1, 2, 3, 4]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="t in [-2, -1, 0, 1, 2, 3]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
      <polyline v-for="L in levels" :key="L" :points="ellipse(L)" class="lab-line" style="stroke-width: 1.2; opacity: 0.5" />
      <polyline :points="ellipse(fStar)" class="lab-warn" />
      <line :x1="lineEnds[0][0]" :y1="lineEnds[0][1]" :x2="lineEnds[1][0]" :y2="lineEnds[1][1]" class="lab-accent" style="stroke-width: 2.5" />
      <circle :cx="P(C)[0]" :cy="P(C)[1]" r="4" class="lab-dot" />
      <circle :cx="P(x0)[0]" :cy="P(x0)[1]" r="5" class="lab-dot-hollow" />
      <text :x="P(x0)[0] + 8" :y="P(x0)[1] + 16" class="lab-small">x₀</text>
      <line v-if="showGrad" :x1="P(xStar)[0]" :y1="P(xStar)[1]" :x2="P(arrowEnd)[0]" :y2="P(arrowEnd)[1]" class="lab-bad" style="stroke-width: 2.5" />
      <circle :cx="P(xStar)[0]" :cy="P(xStar)[1]" r="6" class="lab-dot-warn" />
      <circle :cx="P(cur)[0]" :cy="P(cur)[1]" r="7" class="lab-dot-accent" />
      <text :x="P(cur)[0] + 10" :y="P(cur)[1] - 8" class="lab-small">x(z)</text>
    </svg>
    <svg :viewBox="`0 0 ${gView.width} ${gView.height}`" role="img" aria-label="Đồ thị g theo z, một parabol" style="margin-top: var(--space-3)">
      <line :x1="gView.sx(0)" :x2="gView.sx(0)" y1="0" :y2="gView.height" class="lab-axis" />
      <text x="8" y="16" class="lab-small">g(z) = f(x₀ + z d)</text>
      <text v-for="t in [-4, -2, 2, 4]" :key="`zt${t}`" :x="gView.sx(t) - 6" :y="gView.height - 6" class="lab-small">{{ t }}</text>
      <polyline :points="gCurve" class="lab-line" />
      <circle :cx="gView.sx(zStar)" :cy="gView.sy(fStar)" r="5" class="lab-dot-warn" />
      <circle v-if="z >= Z[0] && z <= Z[1]" :cx="gView.sx(z)" :cy="gView.sy(Math.min(gView.y1, g(z)))" r="7" class="lab-dot-accent" />
    </svg>
    <p class="lab-legend"><span class="legend-accent">đường ràng buộc và điểm x(z)</span><span class="legend-warn">đường mức qua nghiệm</span><span v-if="showGrad" class="legend-bad">gradient tại nghiệm</span></p>
    <div class="lab-controls">
      <label>Góc của pháp tuyến a: {{ deg }}°<input v-model.number="deg" type="range" min="0" max="179" step="1" /></label>
      <label>Vế phải b = {{ fmt(b, 2) }}<input v-model.number="b" type="range" min="-1.5" max="2.5" step="0.01" /></label>
      <label>Tham số z = {{ fmt(z, 2) }}<input v-model.number="z" type="range" min="-4" max="4" step="0.01" /></label>
      <label class="lab-check"><input v-model="showGrad" type="checkbox" /> Hiện gradient tại nghiệm</label>
    </div>
    <div class="lab-readout" role="status">
      <p>a = {{ fmtPoint(a) }}, x₀ = {{ fmtPoint(x0) }}, d = {{ fmtPoint(d) }}. Điểm x(z) = {{ fmtPoint(cur) }} cho g(z) = {{ fmt(g(z), 3) }}.</p>
      <p>Cực tiểu của parabol: z* = {{ fmt(zStar, 3) }}, nên x* = {{ fmtPoint(xStar, 3) }} và f(x*) = <span class="is-accent">{{ fmt(fStar, 3) }}</span>.</p>
      <p>Tại x*, ∇f = {{ fmtPoint(grad, 3) }} = ν·a với ν = {{ fmt(nu, 3) }}: gradient vuông góc với đường ràng buộc, nên đường mức tiếp xúc với nó.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo z cho tới khi chấm tím trùng chấm vàng. Lúc đó đồ thị g(z) ở dưới có gì đặc biệt?</li>
        <li>Đặt góc 45° và b ≈ 0.71, tức ràng buộc x₁ + x₂ = 1. So x* với kết quả tính tay (2/3, 1/3).</li>
        <li>Đổi b để đường thẳng đi qua tâm (2, 1) của các ellipse. Khi đó ν bằng bao nhiêu, và vì sao?</li>
        <li>Xoay góc mà giữ b. Gradient tại nghiệm có bao giờ không vuông góc với đường ràng buộc không?</li>
      </ol>
    </details>
  </figure>
</template>
