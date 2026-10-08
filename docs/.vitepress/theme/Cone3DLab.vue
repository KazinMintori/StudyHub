<script setup>
import { computed, ref } from 'vue'
import { fmt } from './svg-drag'
import { isPsd2 } from './convex-geometry.mjs'

// Khung dây của hai nón trong R³ dưới phép chiếu vuông góc có thể xoay quanh trục đứng.
// type="soc": nón bậc hai {(x₁, x₂, t) : sqrt(x₁² + x₂²) ≤ t}.
// type="psd": biên nón PSD trong S², vẽ theo tọa độ (x, y, z) của ma trận [[x, y], [y, z]].
const props = defineProps({ type: { type: String, default: 'soc' } })
const yaw = ref(35), pitch = ref(22)
const W = 420, H = 330, S = 120
// Hệ trục vẽ (a, b, c): a, b nằm ngang, c thẳng đứng.
function project([a, b, c]) {
  const ya = (yaw.value * Math.PI) / 180, pi = (pitch.value * Math.PI) / 180
  const a1 = a * Math.cos(ya) - b * Math.sin(ya), b1 = a * Math.sin(ya) + b * Math.cos(ya)
  const y = c * Math.cos(pi) - b1 * Math.sin(pi)
  return [W / 2 + S * a1, H * 0.78 - S * y]
}
const path = pts => pts.map(project).map(p => p.join(',')).join(' ')
// Tham số hóa biên. SOC: (s cos t, s sin t, s). PSD: x = s(1 + cos t), y = s sin t, z = s(1 − cos t) thỏa xz = y².
// Với nón PSD, phép đổi trục trực chuẩn a = (x − z)/√2, b = y, c = (x + z)/√2 dựng trục của nón thẳng đứng mà không làm méo hình.
const toDrawPsd = ([x, y, z]) => [(x - z) / Math.SQRT2, y, (x + z) / Math.SQRT2]
function surfacePoint(s, t) {
  if (props.type === 'soc') return [s * Math.cos(t), s * Math.sin(t), s]
  return toDrawPsd([s * (1 + Math.cos(t)), s * Math.sin(t), s * (1 - Math.cos(t))])
}
const levels = [0.25, 0.5, 0.75, 1]
const rings = computed(() => levels.map(s => Array.from({ length: 73 }, (_, i) => surfacePoint(s, (2 * Math.PI * i) / 72))))
const rays = computed(() => Array.from({ length: 12 }, (_, i) => [surfacePoint(0, 0), surfacePoint(1.15, (2 * Math.PI * i) / 12)]))
const axisPts = computed(() => props.type === 'soc'
  ? [{ to: [1.4, 0, 0], name: 'x₁' }, { to: [0, 1.4, 0], name: 'x₂' }, { to: [0, 0, 1.35], name: 't' }]
  : [{ to: toDrawPsd([1.3, 0, 0]), name: 'x' }, { to: toDrawPsd([0, 1.3, 0]), name: 'y' }, { to: toDrawPsd([0, 0, 1.3]), name: 'z' }])
// Điểm thử: SOC dùng (x₁, x₂, t); PSD dùng (x, y, z) của ma trận.
const q1 = ref(0.4), q2 = ref(0.3), q3 = ref(0.7)
const testPoint = computed(() => props.type === 'soc' ? [q1.value, q2.value, q3.value] : toDrawPsd([q1.value, q2.value, q3.value]))
const inside = computed(() => props.type === 'soc' ? Math.hypot(q1.value, q2.value) <= q3.value + 1e-9 : isPsd2(q1.value, q2.value, q3.value))
const names = computed(() => props.type === 'soc' ? ['x₁', 'x₂', 't'] : ['x', 'y', 'z'])
</script>

<template>
  <figure class="study-lab" :aria-label="type === 'soc' ? 'Nón bậc hai trong không gian ba chiều' : 'Nón các ma trận nửa xác định dương cỡ 2'">
    <p class="lab-title">{{ type === 'soc' ? 'Nón bậc hai (nón kem) trong R³' : 'Nón PSD trong S²: ma trận [[x, y], [y, z]]' }}</p>
    <svg :viewBox="`0 0 ${W} ${H}`" role="img" :aria-label="type === 'soc' ? 'Khung dây của nón bậc hai và một điểm thử' : 'Khung dây của biên nón nửa xác định dương và một điểm thử'">
      <g v-for="axis in axisPts" :key="axis.name">
        <line :x1="project([0, 0, 0])[0]" :y1="project([0, 0, 0])[1]" :x2="project(axis.to)[0]" :y2="project(axis.to)[1]" class="lab-axis" />
        <text :x="project(axis.to)[0] + 6" :y="project(axis.to)[1] + 4" class="lab-small">{{ axis.name }}</text>
      </g>
      <polyline v-for="(ray, i) in rays" :key="`r${i}`" :points="path(ray)" class="lab-guide" />
      <polyline v-for="(ring, i) in rings" :key="`c${i}`" :points="path(ring)" :class="i === rings.length - 1 ? 'lab-accent' : 'lab-line'" />
      <line :x1="project(testPoint)[0]" :y1="project(testPoint)[1]" :x2="project([testPoint[0], testPoint[1], 0])[0]" :y2="project([testPoint[0], testPoint[1], 0])[1]" class="lab-guide" />
      <circle :cx="project(testPoint)[0]" :cy="project(testPoint)[1]" r="7" :class="inside ? 'lab-dot-accent' : 'lab-dot-bad'" />
    </svg>
    <div class="lab-controls">
      <label>Xoay quanh trục đứng: {{ yaw }}°<input v-model.number="yaw" type="range" min="-180" max="180" step="5" /></label>
      <label>Góc nhìn từ trên: {{ pitch }}°<input v-model.number="pitch" type="range" min="0" max="60" step="2" /></label>
      <label>{{ names[0] }} = {{ fmt(q1) }}<input v-model.number="q1" type="range" :min="type === 'soc' ? -1 : -0.5" max="1.5" step="0.05" /></label>
      <label>{{ names[1] }} = {{ fmt(q2) }}<input v-model.number="q2" type="range" min="-1" max="1" step="0.05" /></label>
      <label>{{ names[2] }} = {{ fmt(q3) }}<input v-model.number="q3" type="range" :min="type === 'soc' ? 0 : -0.5" max="1.5" step="0.05" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p v-if="type === 'soc'">‖(x₁, x₂)‖₂ = {{ fmt(Math.hypot(q1, q2)) }} và t = {{ fmt(q3) }}, nên điểm <span :class="inside ? 'is-good' : 'is-bad'">{{ inside ? 'thuộc' : 'không thuộc' }}</span> nón. Mỗi vòng tròn là một lát cắt t = hằng số, chính là một quả cầu Euclid bán kính t.</p>
      <p v-else>Ma trận [[{{ fmt(q1) }}, {{ fmt(q2) }}], [{{ fmt(q2) }}, {{ fmt(q3) }}]] có x ≥ 0: {{ q1 >= 0 ? 'đúng' : 'sai' }}, z ≥ 0: {{ q3 >= 0 ? 'đúng' : 'sai' }}, xz − y² = {{ fmt(q1 * q3 - q2 * q2) }}. Vậy ma trận <span :class="inside ? 'is-good' : 'is-bad'">{{ inside ? 'nửa xác định dương' : 'không nửa xác định dương' }}</span>.</p>
      <p class="lab-small">Hình vẽ bằng phép chiếu vuông góc, không có phối cảnh, nên chỉ để hình dung hình dạng. Các kết luận trong khung này được tính từ tọa độ, không đọc từ hình.</p>
    </div>
  </figure>
</template>
