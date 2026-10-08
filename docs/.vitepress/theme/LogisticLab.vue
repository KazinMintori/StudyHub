<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { contourSegments } from './contour.mjs'
import { eigSym2 } from './convex-geometry.mjs'

// Hồi quy logistic một biến: p(u) = σ(a·u + b). Bên trái là đường mức của hàm mất mát trung bình
// L(a, b) = (1/m) Σ log(1 + exp(−sᵢ(a·uᵢ + b))) + (λ/2)(a² + b²), với sᵢ = ±1, một hàm lồi theo (a, b).
// Bên phải là dữ liệu và đường cong xác suất ứng với điểm (a, b) đang chọn.
const u = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
const datasets = {
  overlap: { label: 'hai lớp chồng lấn', y: [0, 0, 1, 0, 1, 0, 1, 1] },
  separable: { label: 'tách được bởi một ngưỡng', y: [0, 0, 0, 0, 1, 1, 1, 1] }
}
const dKey = ref('overlap'), lam = ref(0)
const y = computed(() => datasets[dKey.value].y)
const softplus = t => (t > 0 ? t + Math.log1p(Math.exp(-t)) : Math.log1p(Math.exp(t)))
const sigma = t => 1 / (1 + Math.exp(-t))
const L = ([a, b]) => u.reduce((acc, ui, i) => acc + softplus(-(2 * y.value[i] - 1) * (a * ui + b)), 0) / u.length + (lam.value / 2) * (a * a + b * b)
const grad = ([a, b]) => {
  let ga = 0, gb = 0
  u.forEach((ui, i) => { const s = 2 * y.value[i] - 1, w = -s * sigma(-s * (a * ui + b)); ga += w * ui; gb += w })
  return [ga / u.length + lam.value * a, gb / u.length + lam.value * b]
}
const hess = ([a, b]) => {
  let p = 0, q = 0, r = 0
  u.forEach(ui => { const s = sigma(a * ui + b), w = s * (1 - s); p += w * ui * ui; q += w * ui; r += w })
  return [p / u.length + lam.value, q / u.length, r / u.length + lam.value]
}
// Newton có tìm kiếm quay lui, xuất phát từ 0. Với dữ liệu tách được và λ = 0, dãy chạy mãi ra xa.
const solution = computed(() => {
  let th = [0, 0]
  for (let k = 0; k < 60; k++) {
    const g = grad(th), [p, q, r] = hess(th), det = p * r - q * q
    if (Math.hypot(...g) < 1e-10 || det < 1e-14) break
    const d = [-(r * g[0] - q * g[1]) / det, -(-q * g[0] + p * g[1]) / det]
    let t = 1
    while (L([th[0] + t * d[0], th[1] + t * d[1]]) > L(th) + 0.25 * t * (g[0] * d[0] + g[1] * d[1]) && t > 1e-10) t /= 2
    th = [th[0] + t * d[0], th[1] + t * d[1]]
  }
  return th
})
const finite = computed(() => Math.hypot(...solution.value) < 40)
const uid = useId()
const clip = `${uid}-log-clip`
const svg = ref(null)
const left = ref(makeView({ x0: -1, x1: 7, y0: -17, y1: 3, width: 300, height: 300 }))
const PL = p => left.value.point(p)
const state = ref({ th: [2, -3] })
const drag = createDragger(svg, left, (name, value) => { state.value = { ...state.value, [name]: value } }, { step: 0.2, snap: 0.05 })
const th = computed(() => state.value.th)
const levels = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.2, 2]
const contours = computed(() => levels.map(c => ({ c, segs: contourSegments(L, { x0: -1, x1: 7, y0: -17, y1: 3, n: 70 }, c) })))
const right = makeView({ x0: 0, x1: 4.5, y0: -0.08, y1: 1.08, width: 300, height: 300 })
const curve = computed(() => Array.from({ length: 121 }, (_, i) => { const s = (4.5 * i) / 120; return `${320 + right.sx(s)},${right.sy(sigma(th.value[0] * s + th.value[1]))}` }).join(' '))
const eig = computed(() => eigSym2(...hess(th.value)).values)
const line = s => `${PL(s[0])[0]},${PL(s[0])[1]} ${PL(s[1])[0]},${PL(s[1])[1]}`
</script>

<template>
  <figure class="study-lab" aria-label="Hàm mất mát của hồi quy logistic theo hai tham số">
    <p class="lab-title">Hồi quy logistic: một cái bát theo tham số (a, b)</p>
    <svg ref="svg" viewBox="0 0 620 300" role="img" aria-label="Bên trái đường mức của hàm mất mát theo a và b, bên phải dữ liệu và đường cong xác suất" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs><clipPath :id="clip"><rect x="0" y="0" width="300" height="300" /></clipPath></defs>
      <g :clip-path="`url(#${clip})`">
        <line x1="0" x2="300" :y1="left.sy(0)" :y2="left.sy(0)" class="lab-axis" /><line :x1="left.sx(0)" :x2="left.sx(0)" y1="0" y2="300" class="lab-axis" />
        <g v-for="(lv, k) in contours" :key="`c${k}`"><polyline v-for="(s, i) in lv.segs" :key="i" :points="line(s)" class="lab-line" :style="`stroke-width: 1.2; opacity: ${0.35 + 0.05 * k}`" /></g>
        <circle v-if="finite" :cx="PL(solution)[0]" :cy="PL(solution)[1]" r="7" class="lab-dot-hollow" />
        <circle :cx="PL(th)[0]" :cy="PL(th)[1]" r="8" class="lab-handle" tabindex="0" role="slider" aria-label="Tham số (a, b)" :aria-valuetext="fmtPoint(th)" @pointerdown="drag.start('th', $event)" @keydown="drag.key('th', th, $event)" />
        <text x="290" :y="left.sy(0) - 6" class="lab-small" text-anchor="end">a</text>
        <text :x="left.sx(0) + 6" y="14" class="lab-small">b</text>
      </g>
      <g>
        <rect x="320" y="0" width="300" height="300" class="lab-region-soft" style="opacity: 0.25" />
        <line x1="320" x2="620" :y1="right.sy(0)" :y2="right.sy(0)" class="lab-axis" /><line x1="320" x2="620" :y1="right.sy(1)" :y2="right.sy(1)" class="lab-grid" />
        <line x1="320" x2="620" :y1="right.sy(0.5)" :y2="right.sy(0.5)" class="lab-guide" />
        <polyline :points="curve" class="lab-accent" />
        <circle v-for="(ui, i) in u" :key="`d${i}`" :cx="320 + right.sx(ui)" :cy="right.sy(y[i])" r="6" :class="y[i] ? 'lab-dot-accent' : 'lab-dot'" />
        <text x="326" y="16" class="lab-small">p(u) = σ(a·u + b)</text>
        <text x="612" :y="right.sy(0) + 16" class="lab-small" text-anchor="end">u</text>
      </g>
    </svg>
    <div class="lab-controls">
      <label>Dữ liệu <select v-model="dKey"><option v-for="(item, key) in datasets" :key="key" :value="key">{{ item.label }}</option></select></label>
      <label>Điều chuẩn λ = {{ fmt(lam, 2) }}<input v-model.number="lam" type="range" min="0" max="0.3" step="0.01" /></label>
    </div>
    <div class="lab-buttons"><button type="button" :disabled="!finite" @click="state = { th: solution }">Đặt (a, b) vào nghiệm</button></div>
    <div class="lab-readout" role="status">
      <p>Tại (a, b) = {{ fmtPoint(th) }}: L = {{ fmt(L(th), 4) }}. Hessian có trị riêng {{ fmt(eig[0], 4) }} và {{ fmt(eig[1], 4) }}, cả hai không âm ở mọi điểm.</p>
      <p v-if="finite" class="is-good">Nghiệm (vòng tròn rỗng): (a, b) ≈ {{ fmtPoint(solution, 3) }} với L ≈ {{ fmt(L(solution), 4) }}.</p>
      <p v-else class="is-bad">Không có nghiệm hữu hạn: dữ liệu tách được và λ = 0, nên L giảm mãi về 0 khi (a, b) chạy ra xa theo hướng làm ngưỡng −b/a nằm giữa hai lớp. Tăng λ một chút để thấy nghiệm xuất hiện.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Với dữ liệu chồng lấn, kéo (a, b) quanh khung. Các đường mức có dạng gì, và có "thung lũng" thứ hai nào không?</li>
        <li>Chuyển sang dữ liệu tách được với λ = 0. Kéo (a, b) theo hướng (1, −2.25) và xem L thay đổi thế nào.</li>
        <li>Tăng λ từ 0 lên 0.3 với cả hai bộ dữ liệu. Nghiệm dịch chuyển về đâu, và đường cong xác suất bên phải dốc hơn hay thoải hơn?</li>
      </ol>
    </details>
  </figure>
</template>
