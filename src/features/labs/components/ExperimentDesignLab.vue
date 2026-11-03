<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { closestOnSegment, insideConvexPolygon } from '../services/convex-geometry.mjs'
import { clipPolyline } from '../services/svg-clipping.mjs'

const svg = ref(null)
const allocation = ref([1 / 3, 1 / 3])
const triangle = [[0,0], [1,0], [0,1]]
const simplex = ref(makeView({ x0: -0.1, x1: 1.1, y0: -0.1, y1: 1.1, width: 400, height: 300, pad: 45 }))
const viewport = { x0: -4, x1: 4, y0: -3.1, y1: 3.1 }
const errors = makeView({ ...viewport, width: 400, height: 310, pad: 34 })
const points = (view, list) => list.map(p => view.point(p).join(',')).join(' ')
const drag = createDragger(svg, simplex, (_, p) => {
  if (insideConvexPolygon(p, triangle)) allocation.value = p
  else allocation.value = triangle.map((start, i) => closestOnSegment(p, start, triangle[(i + 1) % 3]))
    .sort((a,b) => a.distance-b.distance)[0].point
}, { step: 0.025 })
const weights = computed(() => [...allocation.value, Math.max(0, 1 - allocation.value[0] - allocation.value[1])])
const design = computed(() => {
  const [a,b,c] = weights.value
  const det = a*b+a*c+b*c
  const trace = 1+c
  const gap = Math.hypot(a-b, 2*c)
  const max = (trace+gap)/2
  const min = det/max
  return { det, min, max, trace, angle: Math.atan2(2*c,a-b)/2 }
})
const ellipse = computed(() => {
  const { min,max,angle } = design.value
  const cs = Math.cos(angle), sn = Math.sin(angle)
  if (min < 1e-10) {
    const r = 1 / Math.sqrt(max)
    const boundaries = [-r,r].map(d => [[d*cs+12*sn,d*sn-12*cs],[d*cs-12*sn,d*sn+12*cs]])
    return boundaries.flatMap(line => clipPolyline(line,viewport))
  }
  const samples = Array.from({length:241}, (_, i) => {
    const t = Math.PI*i/120
    const u = Math.cos(t)/Math.sqrt(max), v = Math.sin(t)/Math.sqrt(min)
    return [u*cs-v*sn,u*sn+v*cs]
  })
  return clipPolyline(samples,viewport)
})
const optimumA = 2/(3+Math.sqrt(3))
</script>

<template>
  <figure class="study-lab" aria-label="Thiết kế thí nghiệm và elip sai số chuẩn hóa">
    <figcaption class="lab-title">Đổi ngân sách đo, đổi hình dạng của elip sai số</figcaption>
    <p class="lab-lead">Kéo điểm vàng trong tam giác. Hai tọa độ là phần ngân sách dành cho hướng ngang và hướng dọc. Phần còn lại dành cho hướng chéo.</p>
    <svg ref="svg" viewBox="0 0 400 300" role="group" aria-label="Đơn hình ba trọng số và phân bổ kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polygon :points="points(simplex,triangle)" class="design-simplex" />
      <text :x="simplex.sx(0)-10" :y="simplex.sy(0)+33">λ₃ = 1</text>
      <text :x="simplex.sx(1)-25" :y="simplex.sy(0)+33">λ₁ = 1</text>
      <text :x="simplex.sx(0)-10" :y="simplex.sy(1)-21">λ₂ = 1</text>
      <circle :cx="simplex.sx(allocation[0])" :cy="simplex.sy(allocation[1])" r="7" class="lab-dot-warn" />
      <circle :cx="simplex.sx(allocation[0])" :cy="simplex.sy(allocation[1])" r="31" class="lab-handle design-hit"
        tabindex="0" role="slider" aria-label="Phân bổ ngân sách cho ba hướng đo" :aria-valuetext="fmtPoint(weights,4)"
        @pointerdown="drag.start('allocation', $event)" @keydown="drag.key('allocation', allocation, $event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh phân bổ bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" @click="allocation = [1/3,1/3]">Tối ưu D</button>
      <button type="button" @click="allocation = [optimumA,optimumA]">Tối ưu A</button>
      <button type="button" @click="allocation = [0.5,0.5]">Tối ưu E</button>
      <button type="button" @click="allocation = [1,0]">Chỉ đo ngang</button>
    </div>
    <svg viewBox="0 0 400 310" role="img" aria-label="Miền sai số chuẩn hóa trong hệ trục cố định">
      <line x1="34" x2="366" y1="155" y2="155" class="lab-axis" />
      <line x1="200" x2="200" y1="35" y2="275" class="lab-axis" />
      <text x="365" y="179">e₁</text>
      <text x="209" y="28">e₂</text>
      <polyline v-for="(line,i) in ellipse" :key="i" :points="points(errors,line)" class="design-boundary" />
    </svg>
    <div class="lab-readout" role="status">
      <p>Phân bổ {{ fmtPoint(weights,4) }}. Định thức {{ fmt(design.det,4) }}. Trị riêng nhỏ nhất {{ fmt(design.min,4) }}.</p>
      <p v-if="design.min >= 1e-10">Vết nghịch đảo {{ fmt(design.trace/design.det,4) }}. Bán trục dài nhất {{ fmt(1/Math.sqrt(design.min),4) }}. Hình giữ nguyên thang đo khi đổi phân bổ và có thể cắt phần elip vượt khung.</p>
      <p v-else>Ma trận suy biến. Mức 1 tạo thành hai đường thẳng song song. Miền ở giữa kéo dài vô hạn theo hướng mà phép đo không nhận biết được.</p>
    </div>
  </figure>
</template>

<style scoped>
.design-simplex { fill: var(--tim-soft); stroke: var(--tim); stroke-width: 1.4; }
.design-boundary { fill: none; stroke: var(--xanh); stroke-width: 1.8; }
.design-hit { fill: transparent !important; stroke: transparent; }
.design-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
