<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { project3 } from '../services/foundation-geometry.mjs'

const svg = ref(null)
const point = ref([1.6, 1])
const showSurface = ref(false)
const view = ref(makeView({ x0: -0.3, x1: 3.3, y0: -0.45, y1: 4.45, width: 400, height: 325, pad: 42 }))
const value = (x, lambda) => (x - 2) ** 2 + lambda * (x - 1)
const drag = createDragger(svg, view, (_, [x, lambda]) => {
  point.value = [Math.max(0, Math.min(3, x)), Math.max(0, Math.min(4, lambda))]
}, { step: 0.1, snap: 0.05 })

const camera = { yaw: 26, pitch: 30, scale: 52, origin: [200, 208] }
const lift = ([x, lambda]) => project3([x - 1.5, lambda - 2, (value(x, lambda) - 1) / 4], camera)
const path = points => points.map(p => lift(p).join(',')).join(' ')
const xSamples = Array.from({ length: 41 }, (_, i) => 3 * i / 40)
const lambdaSamples = Array.from({ length: 41 }, (_, i) => i / 10)
const mesh = [
  ...[0, 1, 3, 4].map(lambda => path(xSamples.map(x => [x, lambda]))),
  ...[0, 0.5, 1.5, 2, 2.5, 3].map(x => path(lambdaSamples.map(lambda => [x, lambda])))
]
const xSlice = path(xSamples.map(x => [x, 2]))
const lambdaSlice = path(lambdaSamples.map(lambda => [1, lambda]))
const liftedPoint = computed(() => lift(point.value))
</script>

<template>
  <figure class="study-lab" aria-label="Điểm yên ngựa của Lagrangian">
    <figcaption class="lab-title">Giữ một biến để thấy hai vai trò khác nhau</figcaption>
    <p class="lab-lead">Kéo điểm vàng trong mặt phẳng (x, λ). Đường tím ứng với λ = 2 và đường xanh ứng với x = 1. Mở mặt 3D để xem giá trị L ở độ cao tương ứng.</p>
    <svg ref="svg" viewBox="0 0 400 325" role="group" aria-label="Mặt phẳng hai biến với điểm thử kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line :x1="view.sx(0)" :x2="view.sx(3)" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" :y1="view.sy(0)" :y2="view.sy(4)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(3)" :y1="view.sy(2)" :y2="view.sy(2)" class="saddle-x" />
      <line :x1="view.sx(1)" :x2="view.sx(1)" :y1="view.sy(0)" :y2="view.sy(4)" class="saddle-lambda" />
      <text x="17" y="30">λ</text><text x="364" y="303">x</text>
      <text :x="view.sx(1)" y="312" text-anchor="middle">1</text>
      <text x="27" :y="view.sy(2)+5">2</text>
      <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="32" class="lab-handle saddle-hit"
        tabindex="0" role="slider" aria-label="Điểm thử x và lambda" :aria-valuetext="fmtPoint(point)"
        @pointerdown="drag.start('point',$event)" @keydown="drag.key('point',point,$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm thử bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" @click="point=[1,2]">Điểm yên ngựa</button>
      <button type="button" @click="point=[2,2]">Dọc lát λ = 2</button>
      <button type="button" @click="point=[1,4]">Dọc lát x = 1</button>
      <button type="button" :aria-pressed="showSurface" @click="showSurface=!showSurface">Xem mặt trong R³</button>
    </div>
    <template v-if="showSurface">
      <svg viewBox="0 0 400 340" role="img" aria-label="Mặt Lagrangian, hai lát cắt và điểm đang chọn">
        <polyline v-for="(line,i) in mesh" :key="i" :points="line" class="saddle-mesh" />
        <polyline :points="xSlice" class="saddle-x" />
        <polyline :points="lambdaSlice" class="saddle-lambda" />
        <circle :cx="liftedPoint[0]" :cy="liftedPoint[1]" r="7" class="lab-dot-warn" />
      </svg>
      <p>Độ cao biểu diễn L, với tỉ lệ nén cố định để thấy cả hai lát. Hình giữ nguyên góc nhìn khi kéo điểm.</p>
    </template>
    <div class="lab-readout" role="status">
      <p>(x, λ) = {{fmtPoint(point)}}. L = {{fmt(value(...point),4)}}.</p>
      <p>Lát tím λ = 2 có L = 1 + (x − 1)² và thấp nhất tại x = 1. Lát xanh x = 1 có L = 1 với mọi λ không âm, nên λ = 2 cũng là một điểm cực đại trên lát này.</p>
    </div>
  </figure>
</template>

<style scoped>
.saddle-mesh, .saddle-x, .saddle-lambda { fill: none; stroke-width: 1.5; }
.saddle-mesh { stroke: var(--ink-3); opacity: 0.55; }
.saddle-x { stroke: var(--tim); }
.saddle-lambda { stroke: var(--xanh); stroke-dasharray: 5 4; }
.saddle-hit { fill: transparent !important; stroke: transparent; }
.saddle-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
