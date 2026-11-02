<script setup>
import { computed, ref, watch } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { dot, leastNormExample, project3 } from '../services/foundation-geometry.mjs'

const props=defineProps({initialDimension:{type:Number,default:3}})
const svg = ref(null), dimension = ref(props.initialDimension), t = ref(0.8), yaw = ref(35)
const example = computed(() => leastNormExample(dimension.value, t.value))
const camera = computed(() => ({ yaw: yaw.value, pitch: 28, scale: 51, origin: [205, 233] }))
const P = p => dimension.value === 2 ? [180 + 55 * p[0], 225 - 55 * p[1]] : project3(p, camera.value)
const linePoint = s => example.value.closest.map((v, i) => v + s * example.value.kernel[i])
const p0 = computed(() => P(example.value.closest)), p1 = computed(() => P(linePoint(1)))
const screenView = ref({ x0: 0, x1: 400, y0: -340, y1: 0, toWorld: (x, y) => [x, -y] })
const setFromScreen = (_, p) => {
  const direction = p1.value.map((v, i) => v - p0.value[i]), offset = p.map((v, i) => v - p0.value[i])
  t.value = Math.max(-1.2, Math.min(1.2, dot(offset, direction) / dot(direction, direction)))
}
const drag = createDragger(svg, screenView, (name, p) => setFromScreen(name, [p[0], -p[1]]), { step: 5 })
watch(dimension, () => { t.value = 0.8 })
const axes = computed(() => dimension.value === 2 ? [{ p: [2.8, 0], name: 'x₁' }, { p: [0, 3.4], name: 'x₂' }] : [{ p: [2.8, 0, 0], name: 'x₁' }, { p: [0, 3.4, 0], name: 'x₂' }, { p: [0, 0, 3.4], name: 'x₃' }])
const origin = computed(() => P(dimension.value === 2 ? [0, 0] : [0, 0, 0]))
</script>

<template>
  <figure class="study-lab" aria-label="Nghiệm chuẩn nhỏ nhất là hình chiếu của gốc lên đường nghiệm">
    <figcaption class="lab-title">Cùng thỏa Ax = b, nhưng độ dài khác nhau</figcaption>
    <p class="lab-lead">Kéo điểm x dọc đường nghiệm. Đoạn từ gốc O đến x* vuông góc với đường này. Hai ràng buộc trong R³ có thể để lại cả một đường nghiệm, chứ không phải chỉ một điểm.</p>
    <div class="lab-buttons" role="group" aria-label="Số chiều của ví dụ">
      <button type="button" :aria-pressed="dimension === 2" @click="dimension = 2">R²: Một đường thẳng</button>
      <button type="button" :aria-pressed="dimension === 3" @click="dimension = 3">R³: Giao hai mặt phẳng</button>
      <button type="button" @click="t = 0">Đưa về nghiệm chuẩn nhỏ nhất</button>
    </div>
    <p class="lab-lead">{{ dimension === 2 ? 'Ràng buộc x₁ + 2x₂ = 2. Phương tự do là (2, −1).' : 'Ràng buộc x₁ + x₂ = 2 và x₂ + x₃ = 4. Phương tự do là (1, −1, 1).' }}</p>
    <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Đường nghiệm, gốc O, nghiệm gần gốc nhất x* và điểm x kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <template v-if="dimension === 2">
        <circle cx="180" cy="225" :r="55 * Math.sqrt(0.8)" class="lab-good" />
        <polygon :points="[[1, 0], [0, 1], [-1, 0], [0, -1]].map(p => P(p).join(',')).join(' ')" class="lab-warn norm-diamond" />
        <circle :cx="P([0, 1])[0]" :cy="P([0, 1])[1]" r="6" class="lab-dot-warn" />
        <text x="105" y="148">Nghiệm L₁</text>
      </template>
      <polygon v-if="dimension === 3" :points="[[1.6, 0.4, -0.2], [1.6, 0.4, 3.3], [-0.5, 2.5, 3.3], [-0.5, 2.5, -0.2]].map(p => P(p).join(',')).join(' ')" class="lab-region-soft" />
      <polygon v-if="dimension === 3" :points="[[-1.2, 0.7, 3.3], [1.8, 0.7, 3.3], [1.8, 2.8, 1.2], [-1.2, 2.8, 1.2]].map(p => P(p).join(',')).join(' ')" class="lab-good-fill plane" />
      <g v-for="axis in axes" :key="axis.name"><line :x1="origin[0]" :y1="origin[1]" :x2="P(axis.p)[0]" :y2="P(axis.p)[1]" class="lab-axis" /><text :x="P(axis.p)[0] + 4" :y="P(axis.p)[1] - 6">{{ axis.name }}</text></g>
      <line :x1="P(linePoint(-1.4))[0]" :y1="P(linePoint(-1.4))[1]" :x2="P(linePoint(1.4))[0]" :y2="P(linePoint(1.4))[1]" class="lab-accent" />
      <line :x1="origin[0]" :y1="origin[1]" :x2="P(example.x)[0]" :y2="P(example.x)[1]" class="lab-line" />
      <line :x1="origin[0]" :y1="origin[1]" :x2="p0[0]" :y2="p0[1]" class="lab-good" />
      <circle :cx="origin[0]" :cy="origin[1]" r="4" class="lab-dot" /><text :x="origin[0] - 20" :y="origin[1] + 18">O</text>
      <circle :cx="p0[0]" :cy="p0[1]" r="6" class="lab-dot-hollow" /><text :x="p0[0] + (dimension === 2 ? 10 : -23)" :y="p0[1] + (dimension === 2 ? 21 : -15)">x*</text>
      <circle :cx="P(example.x)[0]" :cy="P(example.x)[1]" r="8" class="lab-dot-accent" /><text :x="P(example.x)[0] + 11" :y="P(example.x)[1] + 16">x</text>
      <circle :cx="P(example.x)[0]" :cy="P(example.x)[1]" r="30" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Nghiệm x trên đường nghiệm" :aria-valuemin="-1.2" :aria-valuemax="1.2" :aria-valuenow="t" :aria-valuetext="`t = ${fmt(t)}, x = ${fmtPoint(example.x)}`" @pointerdown="drag.start('x', $event)" @keydown="drag.key('x', [P(example.x)[0], -P(example.x)[1]], $event)" />
    </svg>
    <details class="lab-tasks lab-alternative"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" /></details>
    <p v-if="dimension === 2" class="lab-legend"><span class="legend-good">Quả cầu Euclid tiếp xúc tại x*</span><span class="legend-warn">Quả cầu L₁ tiếp xúc tại (0; 1)</span></p>
    <div class="lab-controls"><label>Vị trí t = {{ fmt(t) }}<input v-model.number="t" type="range" min="-1.2" max="1.2" step="0.05" /></label><label v-if="dimension === 3">Góc nhìn quanh trục x₃: {{ yaw }}°<input v-model.number="yaw" type="range" min="-70" max="70" step="5" /></label></div>
    <div class="lab-readout" role="status">
      <p>x* = {{ fmtPoint(example.closest) }}, x = x* + t·{{ fmtPoint(example.kernel, 0) }} = {{ fmtPoint(example.x) }}.</p>
      <p>‖x‖₂² = {{ fmt(example.minimum) }} + {{ fmt(example.extra) }} = {{ fmt(example.squared) }}. Phần tăng thêm là ‖t·z‖₂² và luôn không âm.</p>
      <p>Ax − b = {{ fmtPoint(example.residual) }}. Tích vô hướng x*ᵀz = {{ fmt(dot(example.closest, example.kernel)) }}: x* vuông góc với mọi hướng tự do.</p>
      <p v-if="dimension === 2">Chuẩn L₁ của x = {{ fmt(example.x.reduce((s, v) => s + Math.abs(v), 0)) }}. Nghiệm nhỏ nhất theo L₁ là (0; 1), có chuẩn bằng 1, khác với nghiệm nhỏ nhất theo Euclid (0,4; 0,8).</p>
      <p v-if="dimension === 3">Hai mảnh mặt phẳng chỉ biểu diễn một phần của hai ràng buộc vô hạn. Góc vuông trong không gian có thể không hiện thành góc vuông trên hình chiếu. Xoay hình không thay đổi tọa độ và độ dài tính được.</p>
    </div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đưa t về 0. Vì sao x* vẫn thỏa cả hai ràng buộc?</li><li>So sánh t và −t. Vì sao hai nghiệm có cùng chuẩn?</li><li>Đổi từ R² sang R³. Trong hai ví dụ, số chiều của không gian nghiệm đều bằng n − m = 1.</li></ol></details>
  </figure>
</template>

<style scoped>
.plane { opacity: .22; }
.norm-diamond { fill: none; }
.point-hit { fill: transparent !important; stroke: transparent; }
.point-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 20px; }
</style>
