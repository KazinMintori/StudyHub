<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { contourSegments } from './contour.mjs'
import { eigSym2 } from './convex-geometry.mjs'
const clipId = `${useId()}-clip`

// Hàm hai biến: bên trái là các đường đồng mức và một đường thẳng x + tv, bên phải là g(t) = f(x + tv).
// Một hàm lồi khi và chỉ khi mọi hàm hạn chế g như vậy là lồi.
const catalog = {
  quad: { label: 'x₁² + x₁x₂ + 2x₂²', f: ([a, b]) => a * a + a * b + 2 * b * b, levels: [0.5, 1.5, 3, 5, 8], hess: () => [2, 1, 4] },
  saddle: { label: 'x₁² − x₂²', f: ([a, b]) => a * a - b * b, levels: [-4, -2, -0.5, 0.5, 2, 4], hess: () => [2, 0, -2] },
  lse: { label: 'log(e^x₁ + e^x₂)', f: ([a, b]) => Math.log(Math.exp(a) + Math.exp(b)), levels: [-1, 0, 1, 2, 3], hess: ([a, b]) => { const p = Math.exp(a) / (Math.exp(a) + Math.exp(b)); return [p * (1 - p), -p * (1 - p), p * (1 - p)] } },
  qol: { label: 'x₁²/x₂ (x₂ > 0)', f: ([a, b]) => (b > 0 ? (a * a) / b : NaN), levels: [0.25, 1, 2, 4], hess: ([a, b]) => (b > 0 ? [2 / b, -2 * a / (b * b), 2 * a * a / b ** 3] : null) },
  bumpy: { label: '0.4(x₁² + x₂²) + cos(2x₁)', f: ([a, b]) => 0.4 * (a * a + b * b) + Math.cos(2 * a), levels: [0, 0.5, 1, 2, 3], hess: ([a]) => [0.8 - 4 * Math.cos(2 * a), 0, 0.8] }
}
const choice = ref('quad')
const fn = computed(() => catalog[choice.value])
const svg = ref(null)
const left = ref(makeView({ x0: -3, x1: 3, y0: -3, y1: 3, width: 300, height: 300 }))
const L = p => left.value.point(p)
const base = ref({ x: [0.5, 1] })
const angle = ref(30)
const drag = createDragger(svg, left, (name, value) => { base.value = { ...base.value, [name]: value } }, { step: 0.1, snap: 0.05 })
const dir = computed(() => [Math.cos((angle.value * Math.PI) / 180), Math.sin((angle.value * Math.PI) / 180)])
const contours = computed(() => fn.value.levels.map(level => ({ level, segs: contourSegments(fn.value.f, { x0: -3, x1: 3, y0: -3, y1: 3, n: 70 }, level) })))
const pointAt = t => [base.value.x[0] + t * dir.value[0], base.value.x[1] + t * dir.value[1]]
const g = t => fn.value.f(pointAt(t))
const T = 3
const samples = computed(() => Array.from({ length: 241 }, (_, i) => { const t = -T + (2 * T * i) / 240; return { t, v: g(t) } }))
const finite = computed(() => samples.value.filter(s => Number.isFinite(s.v)))
const gRange = computed(() => { const vs = finite.value.map(s => s.v); if (!vs.length) return [0, 1]; const lo = Math.min(...vs), hi = Math.max(...vs); return lo === hi ? [lo - 1, hi + 1] : [lo, hi] })
const sx = t => 330 + ((t + T) / (2 * T)) * 280
const sy = v => 285 - ((v - gRange.value[0]) / (gRange.value[1] - gRange.value[0])) * 260
const gPath = computed(() => {
  const segs = [[]]
  for (const s of samples.value) { if (!Number.isFinite(s.v)) { if (segs.at(-1).length) segs.push([]); continue } segs.at(-1).push(`${sx(s.t)},${sy(s.v)}`) }
  return segs.filter(s => s.length > 1).map(s => s.join(' '))
})
// Kiểm tra lồi của g bằng sai phân bậc hai trên lưới (chỉ là phép thử trên khung nhìn, không phải chứng minh).
const concaveSpots = computed(() => {
  const out = [], s = samples.value
  for (let i = 1; i < s.length - 1; i++) {
    const [a, b, c] = [s[i - 1].v, s[i].v, s[i + 1].v]
    if ([a, b, c].every(Number.isFinite) && a - 2 * b + c < -1e-9) out.push(s[i])
  }
  return out
})
const hessian = computed(() => fn.value.hess(base.value.x))
const curvatureAlong = computed(() => { const h = hessian.value; if (!h) return null; const [p, q, r] = h, [u, v] = dir.value; return p * u * u + 2 * q * u * v + r * v * v })
const eig = computed(() => (hessian.value ? eigSym2(...hessian.value).values : null))
const lineEnds = computed(() => [pointAt(-T), pointAt(T)])
</script>

<template>
  <figure class="study-lab" aria-label="Hàm hai biến hạn chế lên một đường thẳng">
    <p class="lab-title">Lồi trên mọi đường thẳng</p>
    <svg ref="svg" viewBox="0 0 620 300" role="img" aria-label="Bên trái các đường đồng mức và một đường thẳng, bên phải đồ thị của hàm hạn chế" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs><clipPath :id="clipId"><rect x="0" y="0" width="300" height="300" /></clipPath></defs>
      <g :clip-path="`url(#${clipId})`">
        <line x1="0" x2="300" :y1="left.sy(0)" :y2="left.sy(0)" class="lab-axis" /><line :x1="left.sx(0)" :x2="left.sx(0)" y1="0" y2="300" class="lab-axis" />
        <g v-for="(c, k) in contours" :key="c.level">
          <line v-for="(seg, i) in c.segs" :key="i" :x1="L(seg[0])[0]" :y1="L(seg[0])[1]" :x2="L(seg[1])[0]" :y2="L(seg[1])[1]" :class="c.level < 0 ? 'lab-warn' : 'lab-line'" :style="`stroke-width: 1.4; opacity: ${0.45 + 0.1 * k}`" />
        </g>
        <line :x1="L(lineEnds[0])[0]" :y1="L(lineEnds[0])[1]" :x2="L(lineEnds[1])[0]" :y2="L(lineEnds[1])[1]" class="lab-accent" />
        <circle :cx="L(base.x)[0]" :cy="L(base.x)[1]" r="9" class="lab-handle" tabindex="0" role="slider" aria-label="Điểm gốc x của đường thẳng" @pointerdown="drag.start('x', $event)" @keydown="drag.key('x', base.x, $event)" />
      </g>
      <rect x="320" y="10" width="300" height="285" class="lab-region-soft" style="opacity: 0.25" />
      <line x1="330" x2="610" :y1="sy(Math.min(Math.max(0, gRange[0]), gRange[1]))" :y2="sy(Math.min(Math.max(0, gRange[0]), gRange[1]))" class="lab-axis" />
      <line :x1="sx(0)" :x2="sx(0)" y1="15" y2="290" class="lab-guide" />
      <polyline v-for="(seg, i) in gPath" :key="`g${i}`" :points="seg" class="lab-accent" />
      <circle v-for="(s, i) in concaveSpots" :key="`c${i}`" :cx="sx(s.t)" :cy="sy(s.v)" r="2.5" class="lab-dot-bad" />
      <text x="595" y="296" class="lab-small">t</text>
      <text x="334" y="26" class="lab-small">g(t) = f(x + tv)</text>
    </svg>
    <div class="lab-controls">
      <label>Hàm f = <select v-model="choice"><option v-for="(item, key) in catalog" :key="key" :value="key">{{ item.label }}</option></select></label>
      <label>Hướng v: {{ angle }}°<input v-model.number="angle" type="range" min="0" max="180" step="2" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p>Đường thẳng đi qua x = {{ fmtPoint(base.x) }} theo hướng v = {{ fmtPoint(dir) }}. Đồ thị bên phải là g(t) = f(x + tv) với −3 ≤ t ≤ 3{{ finite.length < samples.length ? ', đứt quãng ở chỗ đường thẳng ra khỏi miền xác định' : '' }}.</p>
      <p v-if="concaveSpots.length" class="is-bad">Trên đường thẳng này, g có chỗ cong xuống (các chấm đỏ). Một đường thẳng như vậy là đủ để kết luận f không lồi.</p>
      <p v-else class="is-good">Trên đường thẳng này, g cong lên ở mọi điểm của khung nhìn.</p>
      <p v-if="hessian">Tại x, Hessian có hai trị riêng {{ fmt(eig[0], 3) }} và {{ fmt(eig[1], 3) }}, còn độ cong theo hướng v là vᵀ∇²f(x)v = {{ fmt(curvatureAlong, 3) }} = g''(0).</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Với x₁² − x₂², xoay hướng v từ 0° tới 90°. Ở góc nào g đổi từ cong lên sang cong xuống?</li>
        <li>Với log-sum-exp, đặt v theo hướng (1, 1), tức 45°. Đồ thị g có dạng gì, và vì sao độ cong bằng 0?</li>
        <li>Với hàm có cos(2x₁), tìm một điểm và một hướng làm g cong xuống, dù hàm trông như một cái bát.</li>
        <li>Với x₁²/x₂, kéo đường thẳng cắt qua trục x₂ = 0. Đồ thị g bị đứt ở đâu?</li>
      </ol>
    </details>
  </figure>
</template>
