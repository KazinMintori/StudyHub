<script setup>
import { computed, ref } from 'vue'
import { makeView, fmt, fmtPoint } from './svg-drag'
import { add, scale, fromEigen, sqrtPsd2, matVec2, ellipseBoundary } from './convex-geometry.mjs'

// Ellipsoid {x : (x − c)ᵀP⁻¹(x − c) ≤ 1} với P = R diag(λ₁, λ₂) Rᵀ, và ảnh c + Au của đường tròn đơn vị với A = P^{1/2}.
const view = makeView({ x0: -4.5, x1: 4.5, y0: -3.4, y1: 3.4, width: 440, height: 332 })
const P2 = p => view.point(p)
const l1 = ref(4), l2 = ref(1), phi = ref(30), ang = ref(20)
const center = [0, 0]
const Pm = computed(() => fromEigen(l1.value, l2.value, (phi.value * Math.PI) / 180))
const A = computed(() => sqrtPsd2(Pm.value))
const boundary = computed(() => ellipseBoundary(Pm.value, center, 120))
const unitCircle = Array.from({ length: 120 }, (_, i) => [Math.cos((2 * Math.PI * i) / 120), Math.sin((2 * Math.PI * i) / 120)])
const u = computed(() => [Math.cos((ang.value * Math.PI) / 180), Math.sin((ang.value * Math.PI) / 180)])
const image = computed(() => add(center, matVec2(A.value, u.value)))
const axes = computed(() => {
  const t = (phi.value * Math.PI) / 180, v1 = [Math.cos(t), Math.sin(t)], v2 = [-Math.sin(t), Math.cos(t)]
  return [scale(Math.sqrt(l1.value), v1), scale(Math.sqrt(l2.value), v2)]
})
const degenerate = computed(() => l2.value === 0 || l1.value === 0)
const quadForm = computed(() => {
  if (degenerate.value) return null
  const [[p, q], [, r]] = Pm.value, det = p * r - q * q, d = image.value
  return (r * d[0] * d[0] - 2 * q * d[0] * d[1] + p * d[1] * d[1]) / det
})
const area = computed(() => Math.PI * Math.sqrt(l1.value * l2.value))
</script>

<template>
  <figure class="study-lab" aria-label="Ellipsoid sinh bởi một ma trận đối xứng xác định dương">
    <p class="lab-title">Ma trận P vẽ ra một ellipsoid</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Ellipse, hai bán trục theo vector riêng của P, đường tròn đơn vị nét đứt và ảnh của một điểm trên đường tròn">
      <line v-for="x in [-4, -3, -2, -1, 1, 2, 3, 4]" :key="`gx${x}`" :x1="view.sx(x)" :x2="view.sx(x)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="y in [-3, -2, -1, 1, 2, 3]" :key="`gy${y}`" :y1="view.sy(y)" :y2="view.sy(y)" x1="0" :x2="view.width" class="lab-grid" />
      <line :x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :y1="0" :y2="view.height" :x1="view.sx(0)" :x2="view.sx(0)" class="lab-axis" />
      <polygon :points="boundary.map(p => P2(p).join(',')).join(' ')" class="lab-region" />
      <polygon :points="unitCircle.map(p => P2(p).join(',')).join(' ')" class="lab-guide" />
      <line v-for="(ax, i) in axes" :key="`ax${i}`" :x1="P2(center)[0]" :y1="P2(center)[1]" :x2="P2(ax)[0]" :y2="P2(ax)[1]" :class="i === 0 ? 'lab-accent' : 'lab-good'" />
      <line :x1="P2(u)[0]" :y1="P2(u)[1]" :x2="P2(image)[0]" :y2="P2(image)[1]" class="lab-guide" />
      <circle :cx="P2(u)[0]" :cy="P2(u)[1]" r="6" class="lab-dot-hollow" />
      <circle :cx="P2(image)[0]" :cy="P2(image)[1]" r="7" class="lab-dot-warn" />
      <text :x="P2(u)[0] + 8" :y="P2(u)[1] - 8" class="lab-small">u</text>
      <text :x="P2(image)[0] + 8" :y="P2(image)[1] - 8">Au</text>
    </svg>
    <div class="lab-controls">
      <label>λ₁ = {{ fmt(l1, 2) }}<input v-model.number="l1" type="range" min="0" max="5" step="0.25" /></label>
      <label>λ₂ = {{ fmt(l2, 2) }}<input v-model.number="l2" type="range" min="0" max="5" step="0.25" /></label>
      <label>Góc quay của trục thứ nhất: {{ phi }}°<input v-model.number="phi" type="range" min="0" max="180" step="5" /></label>
      <label>Điểm u trên đường tròn đơn vị: {{ ang }}°<input v-model.number="ang" type="range" min="0" max="360" step="5" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p>P = [[{{ fmt(Pm[0][0]) }}, {{ fmt(Pm[0][1]) }}], [{{ fmt(Pm[1][0]) }}, {{ fmt(Pm[1][1]) }}]], hai trị riêng {{ fmt(l1) }} và {{ fmt(l2) }}, nên hai bán trục dài <span class="is-accent">√λ₁ = {{ fmt(Math.sqrt(l1)) }}</span> và <span class="is-good">√λ₂ = {{ fmt(Math.sqrt(l2)) }}</span>.</p>
      <p>A = P^(1/2) biến u = {{ fmtPoint(u) }} thành Au = {{ fmtPoint(image) }}. <template v-if="quadForm !== null">Kiểm tra: (Au)ᵀP⁻¹(Au) = {{ fmt(quadForm, 4) }}, nên ảnh của đường tròn đơn vị nằm đúng trên biên ellipsoid.</template></p>
      <p v-if="degenerate" class="is-bad">Một trị riêng bằng 0: P chỉ nửa xác định dương, P⁻¹ không tồn tại. Ảnh của hình tròn đơn vị bị ép thành một đoạn thẳng, gọi là ellipsoid suy biến, có chiều affine bằng hạng của A.</p>
      <p v-else>Diện tích ellipse = π√(λ₁λ₂) = π√(det P) ≈ {{ fmt(area) }}, gấp √(det P) = {{ fmt(Math.sqrt(l1 * l2)) }} lần diện tích hình tròn đơn vị.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Đặt λ₁ = λ₂. Ellipse trở thành hình gì, và góc quay còn ảnh hưởng không?</li>
        <li>Giữ λ₁ = 4, λ₂ = 1 và quay góc. Các phần tử của P thay đổi, nhưng bán trục thì sao?</li>
        <li>Kéo λ₂ về 0 và quan sát ellipse bị dẹt lại.</li>
        <li>Cho u chạy một vòng. Điểm Au chạy hết biên ellipse mấy vòng?</li>
      </ol>
    </details>
  </figure>
</template>
