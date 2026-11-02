<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { project3, unprojectPlane } from '../services/foundation-geometry.mjs'

const svg = ref(null), mode = ref('contours'), point = ref([0.8, 0.6]), s1 = ref(1), s2 = ref(0.6), rho = ref(0), yaw = ref(35)
const camera = computed(() => ({ yaw: yaw.value, pitch: 38, scale: 43, origin: [200, 205] }))
const flat = makeView({ x0: -3, x1: 3, y0: -3, y1: 3, width: 400, height: 340, pad: 25 })
const q = ([x, y]) => (x * x / s1.value ** 2 - 2 * rho.value * x * y / (s1.value * s2.value) + y * y / s2.value ** 2) / (1 - rho.value ** 2)
const determinant = computed(() => s1.value ** 2 * s2.value ** 2 * (1 - rho.value ** 2))
const peak = computed(() => 1 / (2 * Math.PI * Math.sqrt(determinant.value)))
const density = p => peak.value * Math.exp(-q(p) / 2)
const P = (p, z = 0) => mode.value === 'surface' ? project3([...p, z * 2 / peak.value], camera.value) : flat.point(p)
const view = computed(() => ({ x0: -2.7, x1: 2.7, y0: -2.7, y1: 2.7, toWorld: (x, y) => mode.value === 'surface' ? unprojectPlane([x, y], 0, camera.value) : flat.toWorld(x, y) }))
const drag = createDragger(svg, view, (_, p) => { point.value = p }, { step: 0.05, snap: 0.01 })
const rings = computed(() => [1, 2, 4].map(level => Array.from({ length: 121 }, (_, i) => {
  const t = i * Math.PI / 60, x = Math.cos(t), y = Math.sin(t)
  return P([Math.sqrt(level) * s1.value * x, Math.sqrt(level) * s2.value * (rho.value * x + Math.sqrt(1 - rho.value ** 2) * y)]).join(',')
}).join(' ')))
const mesh = computed(() => {
  if (mode.value !== 'surface') return []
  const rows = []
  for (let i = 0; i <= 18; i++) for (const axis of [0, 1]) rows.push(Array.from({ length: 49 }, (_, j) => {
    const p = axis === 0 ? [-2.7 + i * 0.3, -2.7 + j * 5.4 / 48] : [-2.7 + j * 5.4 / 48, -2.7 + i * 0.3]
    return P(p, density(p)).join(',')
  }).join(' '))
  return rows
})
</script>

<template>
  <figure class="study-lab" aria-label="Mật độ Gauss hai biến và các ellipse có cùng mật độ">
    <figcaption class="lab-title">Cùng khoảng cách Euclid, mật độ có thể khác nhau</figcaption>
    <p class="lab-lead">Kéo điểm z và thay đổi độ phân tán theo hai trục. Các ellipse là những đường có cùng q(z), nên cũng có cùng mật độ. Hình 3D thêm một trục chiều cao p(z), không thêm một biến ngẫu nhiên thứ ba.</p>
    <div class="lab-buttons" role="group" aria-label="Cách xem mật độ Gauss"><button type="button" :aria-pressed="mode === 'contours'" @click="mode = 'contours'">Đường đồng mật độ</button><button type="button" :aria-pressed="mode === 'surface'" @click="mode = 'surface'">Mặt mật độ trong R³</button></div>
    <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Ellipse mật độ, điểm z kéo được và mặt Gauss khi chọn chế độ 3D" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line :x1="P([-2.9, 0])[0]" :y1="P([-2.9, 0])[1]" :x2="P([2.9, 0])[0]" :y2="P([2.9, 0])[1]" class="lab-axis" /><line :x1="P([0, -2.9])[0]" :y1="P([0, -2.9])[1]" :x2="P([0, 2.9])[0]" :y2="P([0, 2.9])[1]" class="lab-axis" />
      <polyline v-for="(ring, i) in rings" :key="i" :points="ring" :class="i === 0 ? 'lab-accent' : 'lab-guide'" />
      <polyline v-for="(line, i) in mesh" :key="`m${i}`" :points="line" class="lab-line mesh" />
      <text :x="P([2.9, 0])[0] - 10" :y="P([2.9, 0])[1] + 20">z₁</text><text :x="P([0, 2.9])[0] + 8" :y="P([0, 2.9])[1]">z₂</text>
      <template v-if="mode === 'surface'"><line :x1="P(point)[0]" :y1="P(point)[1]" :x2="P(point, density(point))[0]" :y2="P(point, density(point))[1]" class="lab-guide" /><circle :cx="P(point, density(point))[0]" :cy="P(point, density(point))[1]" r="6" class="lab-dot" /><text :x="P([0, 0], peak)[0] + 10" :y="P([0, 0], peak)[1]">p(z)</text></template>
      <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" class="lab-dot-accent" />
      <circle :cx="P(point)[0]" :cy="P(point)[1]" r="30" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Điểm z trên miền đầu vào" :aria-valuetext="fmtPoint(point)" @pointerdown="drag.start('z', $event)" @keydown="drag.key('z', point, $event)" />
    </svg>
    <details class="lab-tasks lab-alternative"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-controls"><label>Độ lệch chuẩn σ₁ = {{ fmt(s1) }}<input v-model.number="s1" type="range" min="0.3" max="1.2" step="0.05" /></label><label>Độ lệch chuẩn σ₂ = {{ fmt(s2) }}<input v-model.number="s2" type="range" min="0.3" max="1.2" step="0.05" /></label><label>Tương quan ρ = {{ fmt(rho) }}<input v-model.number="rho" type="range" min="-0.8" max="0.8" step="0.05" /></label><label v-if="mode === 'surface'">Góc nhìn: {{ yaw }}°<input v-model.number="yaw" type="range" min="-60" max="60" step="5" /></label></div>
    <div class="lab-readout" role="status"><p>z = {{ fmtPoint(point) }}, q(z) = {{ fmt(q(point)) }}, mật độ p(z) = {{ fmt(density(point), 4) }}. Giá trị này là chiều cao mật độ, không phải xác suất tại riêng z.</p><p>det Σ = {{ fmt(determinant, 4) }}, mật độ tại tâm = {{ fmt(peak, 4) }}. Diện tích bên trong đường q(z) = 1 bằng π√det Σ = {{ fmt(Math.PI * Math.sqrt(determinant)) }}.</p><p>Ba đường ứng với q = 1, 2, 4. Trong hai chiều, xác suất bên trong q ≤ c bằng 1 − exp(−c/2), nên q ≤ 1 chứa khoảng 39,35% xác suất. Thang đứng của mặt 3D tự điều chỉnh theo mật độ tại tâm.</p></div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt σ₁ = σ₂ và ρ = 0. Vì sao các đường đồng mật độ là đường tròn?</li><li>Giảm riêng σ₂. Đi cùng một khoảng theo z₁ hay z₂ làm q tăng nhanh hơn?</li><li>Giữ hai độ lệch chuẩn cố định rồi tăng ρ. Vì sao ellipse nghiêng và thu hẹp?</li></ol></details>
  </figure>
</template>

<style scoped>
.mesh { opacity: .45; stroke-width: 1; }
.point-hit { fill: transparent !important; stroke: transparent; }
.point-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 20px; }
</style>
