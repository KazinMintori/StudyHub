<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { dot, project3 } from '../services/foundation-geometry.mjs'

const svg = ref(null), w = ref(1), mode = ref('data'), yaw = ref(-20)
const a = [1, 2, 3], b = [1, 2, 2], optimum = 11 / 14
const prediction = computed(() => a.map(v => v * w.value))
const residual = computed(() => prediction.value.map((v, i) => v - b[i]))
const loss = computed(() => dot(residual.value, residual.value) / 2)
const gradient = computed(() => dot(a, residual.value))
const camera = computed(() => ({ yaw: yaw.value, pitch: 30, scale: 47, origin: [200, 242] }))
const P = p => project3(p, camera.value)
const dataPoint = (x, y) => [35 + x * 90, 275 - y * 53]
const handle = computed(() => mode.value === 'data' ? dataPoint(3, 3 * w.value) : P(prediction.value))
const screenView = ref({ x0: 0, x1: 400, y0: -340, y1: 0, toWorld: (x, y) => [x, -y] })
const update = (_, p) => {
  if (mode.value === 'data') w.value = (275 + p[1]) / (53 * 3)
  else { const o = P([0, 0, 0]), end = P(a), d = end.map((v, i) => v - o[i]); w.value = dot([p[0] - o[0], -p[1] - o[1]], d) / dot(d, d) }
  w.value = Math.max(0, Math.min(1.4, w.value))
}
const drag = createDragger(svg, screenView, update, { step: 6 })
</script>

<template>
  <figure class="study-lab" aria-label="Phép nhân ma trận tạo dự đoán trong không gian ba chiều">
    <figcaption class="lab-title">Một tham số w, ba dự đoán cùng chuyển động</figcaption>
    <p class="lab-lead">Kéo chấm tím. Trong biểu đồ dữ liệu, chấm này chỉ trượt theo phương đứng và đổi độ dốc của đường dự đoán. Trong R³, nó là cả vector Aw, chỉ chuyển động trên đường sinh bởi A.</p>
    <div class="lab-buttons" role="group" aria-label="Cách nhìn dữ liệu và dự đoán"><button type="button" :aria-pressed="mode === 'data'" @click="mode = 'data'">Dữ liệu trong mặt phẳng</button><button type="button" :aria-pressed="mode === 'space'" @click="mode = 'space'">Vector dự đoán trong R³</button><button type="button" @click="w = optimum">Tìm w tối ưu</button></div>
    <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Các điểm quan sát, dự đoán và phần dư có thể điều chỉnh trực tiếp" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <template v-if="mode === 'data'">
        <line x1="35" y1="275" x2="365" y2="275" class="lab-axis" /><line x1="35" y1="275" x2="35" y2="20" class="lab-axis" /><text x="345" y="300">aᵢ</text><text x="44" y="30">bᵢ</text>
        <line x1="35" y1="275" :x2="dataPoint(3.2, w * 3.2)[0]" :y2="dataPoint(3.2, w * 3.2)[1]" class="lab-accent" />
        <g v-for="(v, i) in b" :key="i"><line :x1="dataPoint(a[i], v)[0]" :y1="dataPoint(a[i], v)[1]" :x2="dataPoint(a[i], prediction[i])[0]" :y2="dataPoint(a[i], prediction[i])[1]" class="lab-bad" /><circle :cx="dataPoint(a[i], v)[0]" :cy="dataPoint(a[i], v)[1]" r="6" class="lab-dot" /><circle :cx="dataPoint(a[i], prediction[i])[0]" :cy="dataPoint(a[i], prediction[i])[1]" r="5" class="lab-dot-hollow" /><text :x="dataPoint(a[i], 0)[0] - 4" y="299">{{ a[i] }}</text></g>
      </template>
      <template v-else>
        <g v-for="(axis, i) in [[3, 0, 0], [0, 3.5, 0], [0, 0, 4.5]]" :key="i"><line :x1="P([0, 0, 0])[0]" :y1="P([0, 0, 0])[1]" :x2="P(axis)[0]" :y2="P(axis)[1]" class="lab-axis" /><text :x="P(axis)[0] + 5" :y="P(axis)[1]">{{ ['b₁', 'b₂', 'b₃'][i] }}</text></g>
        <line :x1="P([0, 0, 0])[0]" :y1="P([0, 0, 0])[1]" :x2="P(a.map(v => v * 1.5))[0]" :y2="P(a.map(v => v * 1.5))[1]" class="lab-accent" />
        <line :x1="P(b)[0]" :y1="P(b)[1]" :x2="handle[0]" :y2="handle[1]" class="lab-bad" />
        <circle :cx="P(b)[0]" :cy="P(b)[1]" r="6" class="lab-dot" /><text :x="P(b)[0] + 12" :y="P(b)[1] + 18">b</text>
        <circle :cx="P(a.map(v => v * optimum))[0]" :cy="P(a.map(v => v * optimum))[1]" r="6" class="lab-dot-hollow" /><text :x="P(a.map(v => v * optimum))[0] - 38" :y="P(a.map(v => v * optimum))[1] - 12">Aw*</text>
        <text :x="P([0, 0, 0])[0] - 20" :y="P([0, 0, 0])[1] + 20">O</text>
      </template>
      <circle :cx="handle[0]" :cy="handle[1]" r="8" class="lab-dot-accent" />
      <text v-if="mode === 'space'" :x="handle[0] + 12" :y="handle[1] - 10">Aw</text>
      <circle :cx="handle[0]" :cy="handle[1]" r="30" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Dự đoán Aw, điều chỉnh trọng số w" :aria-valuemin="0" :aria-valuemax="1.4" :aria-valuenow="w" :aria-valuetext="`w = ${fmt(w)}, Aw = ${fmtPoint(prediction)}`" @pointerdown="drag.start('w', $event)" @keydown="drag.key('w', [handle[0], -handle[1]], $event)" />
    </svg>
    <details class="lab-tasks lab-alternative"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" :axes="mode === 'data' ? 'y' : 'xy'" /></details>
    <p class="lab-legend"><span class="legend-accent">Dự đoán</span><span>Quan sát b</span><span class="legend-bad">Phần dư Aw − b</span></p>
    <div class="lab-controls"><label>Trọng số w = {{ fmt(w, 3) }}<input v-model.number="w" type="range" min="0" max="1.4" step="0.01" /></label><label v-if="mode === 'space'">Góc nhìn: {{ yaw }}°<input v-model.number="yaw" type="range" min="-40" max="70" step="5" /></label></div>
    <div class="lab-readout" role="status"><p>Aw = {{ fmtPoint(prediction) }}, r = {{ fmtPoint(residual) }}.</p><p>f(w) = ‖r‖₂²/2 = {{ fmt(loss, 4) }}. Gradient Aᵀr = {{ fmt(gradient, 4) }}. {{ Math.abs(gradient) < 1e-8 ? 'Đã đạt cực tiểu.' : gradient > 0 ? 'Giảm w một lượng đủ nhỏ sẽ giảm mất mát.' : 'Tăng w một lượng đủ nhỏ sẽ giảm mất mát.' }}</p><p>Với w* = 11/14, Aᵀr = 0: Phần dư vuông góc với đường các dự đoán. Hình 3D là phép chiếu, nên tính vuông góc cần kiểm bằng tích vô hướng.</p></div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt w = 1. Vì sao hai quan sát đầu không có phần dư?</li><li>Chuyển sang R³. Vì sao ba dự đoán không được chuyển động độc lập?</li><li>Bấm tìm w tối ưu. Vì sao phần dư vẫn khác 0 dù gradient đã bằng 0?</li></ol></details>
  </figure>
</template>

<style scoped>
.point-hit { fill: transparent !important; stroke: transparent; }
.point-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 20px; }
</style>
