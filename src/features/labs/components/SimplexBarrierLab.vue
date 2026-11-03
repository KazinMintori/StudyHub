<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint, makeView } from '../controllers/svg-drag.js'

const svg = ref(null)
const weight = ref(2)
const view = ref(makeView({ x0: -0.1, x1: 1.1, y0: -0.1, y1: 1.1, width: 400, height: 380, pad: 40 }))
const centralX = t => 2 / (t + 3 + Math.sqrt((t + 3) ** 2 - 4 * t))
const center = t => {
  const x = centralX(t)
  return [x, (1 - x) / 2]
}
const point = computed(() => center(weight.value))
const coordinates = rows => rows.map(p => view.value.point(p).join(',')).join(' ')
const triangle = coordinates([[0,0],[1,0],[0,1]])
const path = coordinates([[1/3,1/3],[0,1/2]])
const drag = createDragger(svg, view, (_, [rawX]) => {
  const x = Math.max(centralX(20), Math.min(centralX(0.1), rawX))
  weight.value = 1 / x - 2 / (1 - x)
}, { step: 0.015 })
</script>

<template>
  <figure class="study-lab" aria-label="Đường trung tâm trong đơn hình">
    <figcaption class="lab-title">Kéo điểm trên đường trung tâm</figcaption>
    <p class="lab-lead">Cực tiểu hóa x với x + y + z = 1 và ba tọa độ không âm. Hình vẽ theo x và y, còn z bằng 1 − x − y. Kéo điểm vàng về cạnh xanh để tăng trọng số t của mục tiêu.</p>
    <svg ref="svg" viewBox="0 0 400 380" role="group" aria-label="Đơn hình, cạnh tối ưu và điểm trung tâm kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polygon :points="triangle" class="barrier-simplex" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" :y1="view.sy(0)" :y2="view.sy(1)" class="barrier-optimal" />
      <polyline :points="path" class="barrier-path" />
      <text :x="view.sx(1)-8" :y="view.sy(0)+31">x</text>
      <text :x="view.sx(0)-24" :y="view.sy(1)-9">y</text>
      <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="32" class="lab-handle barrier-hit"
        tabindex="0" role="slider" aria-label="Hoành độ điểm trung tâm"
        :aria-valuemin="centralX(20)" :aria-valuemax="centralX(0.1)"
        :aria-valuenow="point[0]" :aria-valuetext="'x = '+fmt(point[0],4)+', t = '+fmt(weight,3)"
        @pointerdown="drag.start('center',$event)" @keydown="drag.key('center',point,$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button v-for="value in [0.1,2,20]" :key="value" type="button" @click="weight=value">t = {{value}}</button>
    </div>
    <div class="lab-readout" role="status">
      <p>t = {{fmt(weight,3)}}. Điểm trung tâm {{fmtPoint([point[0],point[1],1-point[0]-point[1]],4)}}.</p>
      <p>Mục tiêu còn cách tối ưu {{fmt(point[0],4)}}. Khoảng cách tới cận dưới từ nhân tử đường trung tâm là 3/t = {{fmt(3/weight,4)}}.</p>
      <p>Cả cạnh xanh có giá trị tối ưu bằng 0. Đường trung tâm tiến tới trung điểm của cạnh này.</p>
    </div>
  </figure>
</template>

<style scoped>
.barrier-simplex { fill: var(--tim-soft); stroke: var(--tim); stroke-width: 1.5; }
.barrier-optimal { stroke: var(--xanh); stroke-width: 2.1; }
.barrier-path { fill: none; stroke: var(--tim); stroke-width: 1.8; stroke-dasharray: 5 4; }
.barrier-hit { fill: transparent !important; stroke: transparent; }
.barrier-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
