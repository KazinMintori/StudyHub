<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const svg = ref(null)
const lambda = ref(1)
const view = ref(makeView({ x0: -0.35, x1: 4.75, y0: -1.2, y1: 1.45, width: 400, height: 290, pad: 35 }))
const bound = value => value - value ** 2 / 4
const minimizer = computed(() => 2 - lambda.value / 2)
const gap = computed(() => 1 - bound(lambda.value))
const drag = createDragger(svg, view, (_, [x]) => {
  lambda.value = Math.max(0, Math.min(4.5, x))
}, { snap: 0.01, step: 0.05 })
const curve = Array.from({ length: 91 }, (_, index) => {
  const x = index / 20
  return view.value.point([x, bound(x)]).join(',')
}).join(' ')
</script>

<template>
  <figure class="study-lab" aria-label="Cận dưới Lagrange của bài toán một chiều">
    <figcaption class="lab-title">Kéo nhân tử để nâng cận dưới</figcaption>
    <p class="lab-lead">Đường tím cho giá trị nhỏ nhất của L theo x ở mỗi λ. Đường đứt đánh dấu chi phí tối ưu gốc bằng 1. Kéo chấm vàng để xem cận dưới thay đổi.</p>
    <svg ref="svg" viewBox="0 0 400 290" role="group" aria-label="Hàm đối ngẫu và nhân tử lambda kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="35" x2="365" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="36" y2="255" class="lab-axis" />
      <line x1="35" x2="365" :y1="view.sy(1)" :y2="view.sy(1)" class="lab-guide" />
      <text x="13" y="27">g(λ)</text>
      <text x="373" y="265">λ</text>
      <text v-for="x in [0,2,4]" :key="x" :x="view.sx(x)" y="265" text-anchor="middle">{{ x }}</text>
      <polyline :points="curve" class="dual-curve" />
      <line :x1="view.sx(lambda)" :x2="view.sx(lambda)" :y1="view.sy(1)" :y2="view.sy(bound(lambda))" class="lab-guide" />
      <circle :cx="view.sx(lambda)" :cy="view.sy(bound(lambda))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(lambda)" :cy="view.sy(bound(lambda))" r="31" class="lab-handle bound-hit"
        tabindex="0" role="slider" aria-label="Nhân tử lambda" aria-valuemin="0" aria-valuemax="4.5"
        :aria-valuenow="lambda" :aria-valuetext="'λ = ' + fmt(lambda)"
        @pointerdown="drag.start('lambda',$event)" @keydown="drag.key('lambda',[lambda,bound(lambda)],$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh nhân tử bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button v-for="value in [0,1,2,4]" :key="value" type="button" @click="lambda=value">λ = {{value}}</button>
    </div>
    <div class="lab-readout" role="status">
      <p>λ = {{fmt(lambda)}}. Điểm cực tiểu của L là x = {{fmt(minimizer)}}. {{minimizer > 1 ? 'Điểm này vi phạm x ≤ 1.' : 'Điểm này thỏa x ≤ 1.'}}</p>
      <p>Cận dưới g(λ) = {{fmt(bound(lambda),4)}}. Khoảng cách từ cận này tới giá trị tối ưu gốc là {{fmt(gap,4)}}.</p>
    </div>
  </figure>
</template>

<style scoped>
.dual-curve { fill: none; stroke: var(--tim); stroke-width: 1.8; }
.bound-hit { fill: transparent !important; stroke: transparent; }
.bound-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
