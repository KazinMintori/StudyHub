<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint, makeView } from '../controllers/svg-drag.js'
import { clipPolyline } from '../services/svg-clipping.mjs'

const svg = ref(null)
const point = ref([2, 1])
const sigma = ref(0.5)
const target = ref(1)
const lastStep = ref(null)
const bounds = { x0: -0.25, x1: 3.65, y0: -0.2, y1: 1.95 }
const view = ref(makeView({ ...bounds, width: 400, height: 350, pad: 38 }))
const dualResidual = computed(() => 1 - point.value[1])
const product = computed(() => point.value[0] * point.value[1])
const centeringResidual = computed(() => product.value - target.value)
const direction = computed(() => [
  (target.value - point.value[0]) / point.value[1],
  1 - point.value[1]
])
const coordinates = points => points.map(p => view.value.point(p).join(',')).join(' ')
const centralCurve = computed(() => {
  if (!target.value) return []
  const samples = Array.from({ length: 151 }, (_, i) => {
    const x = 0.01 + i * 3.59 / 150
    return [x, target.value / x]
  })
  return clipPolyline(samples, bounds).map(coordinates)
})
function chooseTarget() {
  target.value = sigma.value * point.value[0] * point.value[1]
  lastStep.value = null
}
function reset(position) {
  point.value = position
  chooseTarget()
}
const drag = createDragger(svg, view, (_, [x, lambda]) => {
  reset([Math.max(1e-8, Math.min(3.2, x)), Math.max(0.2, Math.min(1.6, lambda))])
}, { step: 0.05 })

function findStep() {
  const [x, lambda] = point.value
  const [dx, dlambda] = direction.value
  const originalResidual = Math.hypot(1 - lambda, x * lambda - target.value)
  if (originalResidual < 1e-12) return null
  const positiveLimit = Math.min(
    1,
    dx < 0 ? -x / dx : Infinity,
    dlambda < 0 ? -lambda / dlambda : Infinity
  )
  let step = Math.min(0.8, 0.99 * positiveLimit)
  for (let iteration = 0; iteration < 40; iteration++) {
    const trial = [x + step * dx, lambda + step * dlambda]
    const residual = Math.hypot(1 - trial[1], trial[0] * trial[1] - target.value)
    if (trial.every(value => value > 0) && residual <= (1 - 0.1 * step) * originalResidual) {
      return { point: trial, step }
    }
    step /= 2
  }
  return null
}
const preview = computed(findStep)
function takeStep() {
  const next = preview.value
  if (!next) return
  point.value = next.point
  lastStep.value = next.step
}
</script>

<template>
  <figure class="study-lab" aria-label="Phần dư và bước primal-dual của bài toán một biến">
    <figcaption class="lab-title">Tích bù trừ dương chưa đủ để là khoảng cách đối ngẫu</figcaption>
    <p class="lab-lead">Cực tiểu hóa x với x ≥ 0. Kéo điểm vàng trong miền x, λ dương. Đường xanh nét đứt là λ = 1, nơi gradient Lagrange bằng 0. Đường tím liền là xλ = η. Đoạn vàng chấm dẫn tới điểm của bước thử tiếp theo.</p>
    <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Điểm primal-dual kéo được, đường dừng và đường tích bù trừ"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="38" x2="362" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="38" y2="312" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(3.5)" :y1="view.sy(1)" :y2="view.sy(1)" class="primal-dual-stationary" />
      <polyline v-for="(curve,i) in centralCurve" :key="i" :points="curve" class="primal-dual-central" />
      <template v-if="preview">
        <line :x1="view.sx(point[0])" :y1="view.sy(point[1])" :x2="view.sx(preview.point[0])" :y2="view.sy(preview.point[1])" class="primal-dual-preview" />
        <circle :cx="view.sx(preview.point[0])" :cy="view.sy(preview.point[1])" r="5" class="primal-dual-next" />
      </template>
      <text x="13" y="28">λ</text><text x="372" y="333">x</text>
      <text :x="view.sx(0)-20" :y="view.sy(1)+5">1</text>
      <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="32" class="lab-handle primal-dual-hit"
        tabindex="0" role="slider" aria-label="Điểm x và lambda của bước primal-dual" :aria-valuetext="fmtPoint(point,4)"
        @pointerdown="drag.start('point',$event)" @keydown="drag.key('point',point,$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh hai biến bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" @click="sigma=0.5; reset([2,1])">Ví dụ (2, 1)</button>
      <button type="button" @click="reset([2,0.5])">Thử λ = 0,5</button>
      <button type="button" @click="takeStep">Đi một bước</button>
      <button type="button" @click="chooseTarget">Đặt lại mục tiêu η</button>
      <button type="button" @click="sigma=0; chooseTarget()">Đích bù trừ bằng 0</button>
    </div>
    <div class="lab-readout" role="status">
      <p>(x, λ) = {{fmtPoint(point,4)}}. Tích xλ = {{fmt(product,4)}}, mục tiêu η = {{fmt(target,4)}}.</p>
      <p>Phần dư đối ngẫu {{fmt(dualResidual,4)}}. Phần dư bù trừ {{fmt(centeringResidual,4)}}. Hướng Newton {{fmtPoint(direction,4)}}.</p>
      <p v-if="lastStep !== null">Bước vừa dùng s = {{fmt(lastStep,4)}}. Mục tiêu η giữ cố định trong bước này.</p>
      <p v-if="preview">Bước thử tiếp theo s = {{fmt(preview.step,4)}} tới {{fmtPoint(preview.point,4)}}. Bấm đặt lại mục tiêu để giảm η theo tích hiện tại.</p>
      <p v-if="point[1]===1">Lagrangian có infimum g = 0. Khoảng cách đối ngẫu bằng xλ = {{fmt(product,4)}}.</p>
      <p v-else>Lagrangian bằng (1 − λ)x và có infimum −∞ trên trục số. Tích xλ hiện tại là đại lượng đại diện cho bù trừ.</p>
    </div>
  </figure>
</template>

<style scoped>
.primal-dual-central, .primal-dual-stationary { fill: none; stroke-width: 1.7; }
.primal-dual-central { stroke: var(--tim); }
.primal-dual-stationary { stroke: var(--xanh); stroke-dasharray: 5 4; }
.primal-dual-preview { stroke: var(--vang); stroke-width: 1.7; stroke-dasharray: 2 4; }
.primal-dual-next { stroke: var(--vang); stroke-width: 1.7; fill: var(--paper); }
.primal-dual-hit { fill: transparent !important; stroke: transparent; }
.primal-dual-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
