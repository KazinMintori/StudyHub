<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint, makeView } from '../controllers/svg-drag.js'

const svg = ref(null)
const gradient = ref([1.5, 0.75])
const norm = ref('l2')
const view = ref(makeView({ x0: -2.3, x1: 2.3, y0: -2.3, y1: 2.3, width: 400, height: 400, pad: 35 }))
const drag = createDragger(svg, view, (_, p) => {
  gradient.value = p.map(value => Math.max(-2, Math.min(2, value)))
}, { step: 0.1, snap: 0.05 })
const direction = computed(() => {
  const [gx, gy] = gradient.value
  const length = Math.hypot(gx, gy)
  if (!length) return [0, 0]
  if (norm.value === 'l2') return [-gx / length, -gy / length]
  if (norm.value === 'linf') return [-Math.sign(gx), -Math.sign(gy)]
  return Math.abs(gx) >= Math.abs(gy) ? [-Math.sign(gx), 0] : [0, -Math.sign(gy)]
})
const derivative = computed(() => gradient.value[0] * direction.value[0] + gradient.value[1] * direction.value[1])
const tied = computed(() => {
  const [gx, gy] = gradient.value
  if (norm.value !== 'l1' || !gx || Math.abs(gx) !== Math.abs(gy)) return ''
  return [[-Math.sign(gx), 0], [0, -Math.sign(gy)]].map(p => view.value.point(p).join(',')).join(' ')
})
const box = computed(() => {
  const vertices = norm.value === 'l1'
    ? [[1,0],[0,1],[-1,0],[0,-1]]
    : [[1,1],[-1,1],[-1,-1],[1,-1]]
  return vertices.map(p => view.value.point(p).join(',')).join(' ')
})
</script>

<template>
  <figure class="study-lab" aria-label="Hướng dốc nhất theo ba chuẩn">
    <figcaption class="lab-title">Cùng một gradient, ba cách đo bước</figcaption>
    <p class="lab-lead">Kéo chấm vàng để đổi đầu vector gradient. Vùng tím chứa các bước có chuẩn không quá 1. Điểm xanh cho một bước đạt đạo hàm định hướng nhỏ nhất trong vùng đó.</p>
    <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Quả cầu đơn vị và đầu gradient kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="35" x2="365" y1="200" y2="200" class="lab-axis" />
      <line x1="200" x2="200" y1="35" y2="365" class="lab-axis" />
      <text x="364" y="224">v₁</text><text x="212" y="29">v₂</text>
      <circle v-if="norm==='l2'" cx="200" cy="200" :r="view.sx(1)-200" class="descent-ball" />
      <polygon v-else :points="box" class="descent-ball" />
      <polyline v-if="tied" :points="tied" class="descent-edge" />
      <line x1="200" y1="200" :x2="view.sx(gradient[0])" :y2="view.sy(gradient[1])" class="descent-gradient" />
      <line x1="200" y1="200" :x2="view.sx(direction[0])" :y2="view.sy(direction[1])" class="descent-edge" />
      <circle :cx="view.sx(direction[0])" :cy="view.sy(direction[1])" r="6" class="lab-dot-good" />
      <circle :cx="view.sx(gradient[0])" :cy="view.sy(gradient[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(gradient[0])" :cy="view.sy(gradient[1])" r="31" class="lab-handle descent-hit"
        tabindex="0" role="slider" aria-label="Hai thành phần gradient" :aria-valuetext="fmtPoint(gradient)"
        @pointerdown="drag.start('gradient',$event)" @keydown="drag.key('gradient',gradient,$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh gradient bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button v-for="[key,label] in [['l2','Chuẩn ℓ₂'],['l1','Chuẩn ℓ₁'],['linf','Chuẩn ℓ∞']]" :key="key"
        type="button" :aria-pressed="norm===key" @click="norm=key">{{label}}</button>
      <button type="button" @click="gradient=[1,1]">Hai thành phần bằng nhau</button>
      <button type="button" @click="gradient=[1,0]">Một thành phần bằng 0</button>
      <button type="button" @click="gradient=[0,0]">Gradient bằng 0</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Gradient {{fmtPoint(gradient)}}. Bước được chọn {{fmtPoint(direction)}}. Đạo hàm định hướng {{fmt(derivative,4)}}.</p>
      <p v-if="gradient.every(value=>value===0)">Mọi bước trong vùng đều có đạo hàm định hướng bằng 0.</p>
      <p v-else-if="tied">Mọi điểm trên cạnh xanh đều đạt cùng giá trị nhỏ nhất.</p>
      <p v-else-if="norm==='linf'&&gradient.some(value=>value===0)">Tọa độ có thành phần gradient bằng 0 có thể chọn tùy ý từ −1 đến 1. Hình chọn 0.</p>
    </div>
  </figure>
</template>

<style scoped>
.descent-ball { fill: var(--tim-soft); stroke: var(--tim); stroke-width: 1.6; }
.descent-edge { fill: none; stroke: var(--xanh); stroke-width: 2; }
.descent-gradient { stroke: var(--vang); stroke-width: 1.8; }
.descent-hit { fill: transparent !important; stroke: transparent; }
.descent-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
