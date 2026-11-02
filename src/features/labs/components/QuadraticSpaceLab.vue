<script setup>
import { computed, ref, watch } from 'vue'
import LabPointControls from './LabPointControls.vue'
import MathMatrix from '../../../core/math/components/MathMatrix.vue'
import { createDragger, makeView, svgPoint, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { curvatureModel, project3, unprojectPlane } from '../services/foundation-geometry.mjs'

const props = defineProps({ type: { type: String, default: 'curvature' } })
const svg = ref(null), mode = ref('3d'), rotate = ref(false), yaw = ref(35), pitch = ref(30), point = ref([0.65, 0.35])
const parameter = ref(props.type === 'schur' ? 2 : 1), direction = ref(0)
const model = computed(() => curvatureModel(props.type, parameter.value))
const camera = computed(() => ({ yaw: yaw.value, pitch: pitch.value, scale: 70, origin: [200, 180] }))
const flat = makeView({ x0: -1.6, x1: 1.6, y0: -1.6, y1: 1.6, width: 400, height: 340, pad: 26 })
const heightScale = computed(() => 1.3 / Math.max(1, ...[[-1.2, -1.2], [-1.2, 1.2], [1.2, -1.2], [1.2, 1.2]].map(p => Math.abs(model.value.value(p)))))
const P = ([x, y], z = 0) => mode.value === '2d' ? flat.point([x, y]) : project3([x, y, heightScale.value * z], camera.value)
const axisZ = computed(() => 1.6 / heightScale.value)
const view = computed(() => ({ x0: -1.2, x1: 1.2, y0: -1.2, y1: 1.2,
  toWorld: (x, y) => mode.value === '2d' ? flat.toWorld(x, y) : unprojectPlane([x, y], 0, camera.value) }))
const drag = createDragger(svg, view, (_, p) => { point.value = p }, { step: 0.05, snap: 0.01 })
const mesh = computed(() => {
  const lines = []
  for (let i = 0; i <= 12; i++) {
    const fixed = -1.2 + i * 0.2
    for (const axis of [0, 1]) lines.push(Array.from({ length: 33 }, (_, j) => {
      const moving = -1.2 + j * 2.4 / 32, p = axis === 0 ? [fixed, moving] : [moving, fixed]
      return P(p, model.value.value(p)).join(',')
    }).join(' '))
  }
  return lines
})
const d = computed(() => [Math.cos(direction.value * Math.PI / 180), Math.sin(direction.value * Math.PI / 180)])
const curvature = computed(() => { const [a, b, c] = model.value.hessian, [x, y] = d.value; return a * x * x + 2 * b * x * y + c * y * y })
const slice = computed(() => Array.from({ length: 65 }, (_, i) => {
  const s = -1.2 + i * 2.4 / 64, p = d.value.map(v => v * s)
  return P(p, model.value.value(p)).join(',')
}).join(' '))
const sliceScale = computed(() => 58 / Math.max(1, Math.abs(model.value.value(d.value.map(v => v * 1.2)))))
const sliceFlat = computed(() => Array.from({ length: 65 }, (_, i) => {
  const s = -1.2 + i * 2.4 / 64
  return `${200 + s * 95},${91 - model.value.value(d.value.map(v => v * s)) * sliceScale.value}`
}).join(' '))
const tangent = computed(() => model.value.gradient(point.value))
let orbit = null
function startOrbit(event) {
  if (!rotate.value || event.button !== 0 || event.isPrimary === false) return
  const p = svgPoint(svg.value, event)
  if (!p) return
  orbit = { pointer: event.pointerId, target: event.currentTarget, p, yaw: yaw.value, pitch: pitch.value }
  orbit.target.setPointerCapture(event.pointerId)
  event.preventDefault()
}
function move(event) {
  if (!orbit) { drag.move(event); return }
  if (event.pointerId !== orbit.pointer) return
  const p = svgPoint(svg.value, event)
  if (!p) return
  yaw.value = Math.max(-180, Math.min(180, orbit.yaw + (p.x - orbit.p.x) * 0.6))
  pitch.value = Math.max(20, Math.min(65, orbit.pitch + (p.y - orbit.p.y) * 0.3))
}
function end(event) {
  drag.end(event)
  if (!orbit || event.pointerId !== orbit.pointer) return
  const old = orbit; orbit = null
  if (old.target.hasPointerCapture(old.pointer)) old.target.releasePointerCapture(old.pointer)
}
watch(mode, () => { rotate.value = false })
</script>

<template>
  <figure class="study-lab" :aria-label="type === 'schur' ? 'Phần bù Schur qua cực tiểu theo một biến' : 'Độ cong theo hướng của một mặt toàn phương'">
    <figcaption class="lab-title">{{ type === 'schur' ? 'Khử x₁: Theo đáy của từng lát cắt' : 'Độ cong phải được xét theo từng hướng' }}</figcaption>
    <p class="lab-lead">{{ type === 'schur' ? 'Mặt q(x₁, x₂) = x₁² + 2x₁x₂ + c·x₂². Với mỗi x₂ cố định, đáy theo x₁ nằm tại x₁ = −x₂. Giá trị còn lại là (c − 1)x₂².' : 'Mặt f(x₁, x₂) = (x₁² + c·x₂²)/2 nằm trong R³, nhưng đầu vào vẫn chỉ có hai tọa độ. Chọn hướng d để xem đường cắt qua gốc cong lên, cong xuống hay phẳng.' }}</p>
    <div class="lab-buttons" role="group" aria-label="Cách xem mặt hàm">
      <button type="button" :aria-pressed="mode === '3d'" @click="mode = '3d'">Mặt trong R³</button>
      <button type="button" :aria-pressed="mode === '2d'" @click="mode = '2d'">Miền đầu vào R²</button>
      <button v-if="mode === '3d'" type="button" :aria-pressed="rotate" @click="rotate = !rotate">{{ rotate ? 'Xong, kéo điểm' : 'Xoay hình trực tiếp' }}</button>
      <button v-if="type === 'schur'" type="button" @click="point = [-point[1], point[1]]">Lấy đáy theo x₁</button>
    </div>
    <p class="lab-lead">{{ rotate ? 'Vuốt trên hình để đổi góc nhìn. Bấm “Xong, kéo điểm” để trở lại thao tác với điểm.' : 'Kéo chấm tím trên mặt phẳng đáy để đổi đầu vào. Điểm phía trên là giá trị hàm tại đầu vào đó.' }}</p>
    <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Mặt hàm và điểm đầu vào kéo được trên mặt phẳng đáy" :style="{ touchAction: rotate ? 'none' : 'pan-y pinch-zoom' }" @pointerdown="startOrbit" @pointermove="move" @pointerup="end" @pointercancel="end" @lostpointercapture="end">
      <polygon :points="[[-1.2, -1.2], [1.2, -1.2], [1.2, 1.2], [-1.2, 1.2]].map(p => P(p).join(',')).join(' ')" class="lab-region-soft" />
      <line :x1="P([-1.5, 0])[0]" :y1="P([-1.5, 0])[1]" :x2="P([1.5, 0])[0]" :y2="P([1.5, 0])[1]" class="lab-axis" />
      <line :x1="P([0, -1.5])[0]" :y1="P([0, -1.5])[1]" :x2="P([0, 1.5])[0]" :y2="P([0, 1.5])[1]" class="lab-axis" />
      <text :x="P([1.5, 0])[0]" :y="P([1.5, 0])[1] + 20">x₁</text><text :x="P([0, 1.5])[0] - 20" :y="P([0, 1.5])[1] + 20">x₂</text>
      <g v-if="mode === '3d'">
        <polyline v-for="(line, i) in mesh" :key="i" :points="line" class="lab-line surface-grid" />
        <line :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P([0, 0], axisZ)[0]" :y2="P([0, 0], axisZ)[1]" class="lab-axis" /><text :x="P([0, 0], axisZ)[0] + 8" :y="P([0, 0], axisZ)[1]">{{ type === 'schur' ? 'q' : 'f' }}</text>
        <polyline :points="slice" :class="curvature < -1e-8 ? 'lab-bad' : 'lab-good'" />
        <polyline v-if="type === 'schur'" :points="Array.from({ length: 41 }, (_, i) => { const v = -1.2 + i * 2.4 / 40; return P([-v, v], (parameter - 1) * v * v).join(',') }).join(' ')" class="lab-warn" />
        <line :x1="P(point)[0]" :y1="P(point)[1]" :x2="P(point, model.value(point))[0]" :y2="P(point, model.value(point))[1]" class="lab-guide" />
        <circle :cx="P(point, model.value(point))[0]" :cy="P(point, model.value(point))[1]" r="6" class="lab-dot" />
      </g>
      <line :x1="P(d.map(v => -1.2 * v))[0]" :y1="P(d.map(v => -1.2 * v))[1]" :x2="P(d.map(v => 1.2 * v))[0]" :y2="P(d.map(v => 1.2 * v))[1]" class="lab-good" />
      <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" class="lab-dot-accent" />
      <circle v-if="!rotate" :cx="P(point)[0]" :cy="P(point)[1]" r="30" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Đầu vào trên mặt phẳng đáy" :aria-valuetext="fmtPoint(point)" @pointerdown.stop="drag.start('x', $event)" @keydown="drag.key('x', point, $event)" />
    </svg>
    <details class="lab-tasks lab-alternative"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" /></details>
    <p class="lab-legend"><span class="legend-accent">Đầu vào</span><span class="legend-good">Hướng cắt d</span><span v-if="type === 'schur'" class="legend-warn">Đáy x₁ = −x₂</span></p>
    <div class="lab-controls">
      <label>Hệ số c = {{ fmt(parameter) }}<input v-model.number="parameter" type="range" min="-1" max="4" step="0.1" /></label>
      <label>Hướng cắt d: {{ direction }}°<input v-model.number="direction" type="range" min="0" max="180" step="5" /></label>
      <label v-if="mode === '3d'">Góc nhìn ngang: {{ fmt(yaw, 0) }}°<input v-model.number="yaw" type="range" min="-180" max="180" step="5" /></label>
      <label v-if="mode === '3d'">Góc nhìn từ trên: {{ fmt(pitch, 0) }}°<input v-model.number="pitch" type="range" min="20" max="65" step="5" /></label>
    </div>
    <p class="lab-lead">Đường cắt một biến s ↦ {{ type === 'schur' ? 'q(sd)' : 'f(sd)' }}. Cùng một hướng cắt được tô trên hình phía trên.</p>
    <svg viewBox="0 0 400 170" role="img" aria-label="Đồ thị một biến dọc hướng cắt d" class="flat-slice"><line x1="25" y1="91" x2="375" y2="91" class="lab-axis" /><line x1="200" y1="10" x2="200" y2="150" class="lab-axis" /><polyline :points="sliceFlat" :class="curvature < -1e-8 ? 'lab-bad' : 'lab-good'" /><text x="367" y="113">s</text><text x="208" y="25">{{ type === 'schur' ? 'q(sd)' : 'f(sd)' }}</text></svg>
    <div class="lab-readout" role="status">
      <p>Đầu vào {{ fmtPoint(point) }}, giá trị hàm {{ fmt(model.value(point)) }}, gradient {{ fmtPoint(tangent) }}.</p>
      <p>d = {{ fmtPoint(d) }}, dᵀHd = {{ fmt(curvature) }}. {{ curvature > 1e-8 ? 'Đường cắt cong lên.' : curvature < -1e-8 ? 'Đường cắt cong xuống.' : 'Đường cắt này có độ cong bằng 0.' }}</p>
      <template v-if="type === 'schur'"><p>Ma trận của dạng toàn phương là <MathMatrix :rows="[[1, 1], [1, parameter]]" label="Ma trận M của dạng toàn phương" />.</p><p>Phần bù Schur của khối [1] là c − 1 = {{ fmt(parameter - 1) }}. {{ parameter > 1 ? 'Ma trận dương xác định.' : parameter === 1 ? 'Ma trận nửa xác định dương và suy biến.' : 'Ma trận không xác định dấu.' }}</p><p>Giữ x₂ = {{ fmt(point[1]) }}, đáy theo x₁ có giá trị {{ fmt((parameter - 1) * point[1] ** 2) }}. Điểm hiện tại cao hơn đáy {{ fmt((point[0] + point[1]) ** 2) }}.</p></template>
      <p v-else>{{ parameter > 0 ? 'Hessian dương xác định: Mặt cong lên theo mọi hướng khác 0.' : parameter === 0 ? 'Hessian nửa xác định dương: Mặt có một phương phẳng, tạo thành máng.' : 'Hessian không xác định dấu: Mặt có cả hướng cong lên và hướng cong xuống.' }}</p>
      <p>Hình 3D là phép chiếu vuông góc, với thang đứng tự điều chỉnh theo c. Đường cắt phía dưới cũng tự điều chỉnh thang đứng để thấy rõ chiều cong. Đầu vào thuộc R², còn đồ thị (x₁, x₂, f) thuộc R³. Không đo góc hoặc độ dài từ hình chiếu.</p>
    </div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt c = −1 rồi chuyển hướng cắt từ 0° đến 90°. Vì sao dấu độ cong thay đổi?</li><li>{{ type === 'schur' ? 'Đặt c = 1 và hướng cắt 135°. Đường đáy có giá trị nào?' : 'Đặt c = 0 và hướng cắt 90°. Mặt có cực tiểu duy nhất không?' }}</li><li>Xoay hình rồi kiểm tra giá trị hàm. Đại lượng nào đổi và đại lượng nào được giữ nguyên?</li></ol></details>
  </figure>
</template>

<style scoped>
.surface-grid { opacity: .38; stroke-width: 1; }
.flat-slice polyline{stroke-width:2.5}
.point-hit { fill: transparent !important; stroke: transparent; }
.point-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 20px; }
</style>
