<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, makeView } from '../controllers/svg-drag.js'
import { clipPolyline } from '../services/svg-clipping.mjs'

const svg = ref(null)
const start = ref(1.4)
const bounds = { x0: -2.2, x1: 2.2, y0: -0.55, y1: 6.8 }
const view = ref(makeView({ ...bounds, width: 400, height: 340, pad: 34 }))
const f = x => x ** 2 / 2 + x ** 4 / 4
const gradient = computed(() => start.value + start.value ** 3)
const hessian = computed(() => 1 + 3 * start.value ** 2)
const next = computed(() => start.value - gradient.value / hessian.value)
const predictedDrop = computed(() => gradient.value ** 2 / (2 * hessian.value))
const actualDrop = computed(() => f(start.value) - f(next.value))
const model = x => {
  const displacement = x - start.value
  return f(start.value) + gradient.value * displacement + hessian.value * displacement ** 2 / 2
}
const samples = Array.from({ length: 129 }, (_, i) => (i - 64) / 32)
const coordinates = points => points.map(p => view.value.point(p).join(',')).join(' ')
const objective = coordinates(samples.map(x => [x, f(x)]))
const modelPaths = computed(() => clipPolyline(samples.map(x => [x, model(x)]), bounds).map(coordinates))
const drag = createDragger(svg, view, (_, [x]) => {
  start.value = Math.max(-1.9, Math.min(1.9, x))
}, { step: 0.05, snap: 0.01 })
</script>

<template>
  <figure class="study-lab" aria-label="Mô hình bậc hai của một bước Newton">
    <figcaption class="lab-title">Mức giảm dự đoán và mức giảm thực</figcaption>
    <p class="lab-lead">Kéo điểm vàng trên đồ thị tím của hàm mục tiêu. Đường xanh là mô hình Taylor bậc hai tại điểm đó. Hoành độ thấp nhất của đường xanh cho bước Newton đầy đủ.</p>
    <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Hàm mục tiêu, mô hình Newton và điểm bắt đầu kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="34" x2="366" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="34" y2="306" class="lab-axis" />
      <text x="13" y="27">Giá trị</text><text x="371" y="326">x</text>
      <polyline :points="objective" class="newton-objective" />
      <polyline v-for="(path,i) in modelPaths" :key="i" :points="path" class="newton-model" />
      <line :x1="view.sx(next)" :x2="view.sx(next)" :y1="view.sy(model(next))" :y2="view.sy(f(next))" class="lab-guide" />
      <circle :cx="view.sx(next)" :cy="view.sy(model(next))" r="5" class="lab-dot-good" />
      <circle :cx="view.sx(next)" :cy="view.sy(f(next))" r="5" class="lab-dot-accent" />
      <circle :cx="view.sx(start)" :cy="view.sy(f(start))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(start)" :cy="view.sy(f(start))" r="31" class="lab-handle newton-hit"
        tabindex="0" role="slider" aria-label="Điểm bắt đầu Newton" aria-valuemin="-1.9" aria-valuemax="1.9"
        :aria-valuenow="start" :aria-valuetext="'x = '+fmt(start,3)"
        @pointerdown="drag.start('start',$event)" @keydown="drag.key('start',[start,f(start)],$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm bắt đầu bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" @click="start=next">Đi một bước Newton</button>
      <button type="button" @click="start=1.4">Bắt đầu ở 1,4</button>
      <button type="button" @click="start=0">Đặt tại nghiệm</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Điểm bắt đầu {{fmt(start,3)}}. Điểm thử sau bước Newton {{fmt(next,3)}}.</p>
      <p>Mô hình dự đoán giảm {{fmt(predictedDrop,5)}}. Mục tiêu thực giảm {{fmt(actualDrop,5)}}. Đoạn đứng nối hai giá trị tại cùng điểm thử.</p>
    </div>
  </figure>
</template>

<style scoped>
.newton-objective, .newton-model { fill: none; stroke-width: 1.8; }
.newton-objective { stroke: var(--tim); }
.newton-model { stroke: var(--xanh); stroke-dasharray: 5 4; }
.newton-hit { fill: transparent !important; stroke: transparent; }
.newton-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
