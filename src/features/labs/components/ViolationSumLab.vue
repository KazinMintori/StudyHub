<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, makeView } from '../controllers/svg-drag.js'

const svg = ref(null)
const trial = ref(2)
const view = ref(makeView({ x0: -0.4, x1: 4.4, y0: -0.45, y1: 3.7, width: 400, height: 310, pad: 37 }))
const violations = computed(() => [Math.max(0, 3-trial.value), Math.max(0, trial.value-1)])
const total = x => Math.max(0,3-x) + Math.max(0,x-1)
const coordinates = points => points.map(p=>view.value.point(p).join(',')).join(' ')
const curve = coordinates([[0,3],[1,2],[3,2],[4,3]])
const drag = createDragger(svg, view, (_, [x]) => {
  trial.value = Math.max(0,Math.min(4,x))
}, { step: 0.1, snap: 0.05 })
</script>

<template>
  <figure class="study-lab" aria-label="Các nghiệm tối ưu của tổng độ vi phạm">
    <figcaption class="lab-title">Cùng tổng vi phạm, nhiều cách phân bổ phần vi phạm</figcaption>
    <p class="lab-lead">Ta muốn đồng thời x ≥ 3 và x ≤ 1. Kéo điểm vàng dọc đồ thị tổng độ vi phạm. Mọi x từ 1 đến 3 cho cùng tổng nhỏ nhất, còn từng phần vi phạm thay đổi.</p>
    <svg ref="svg" viewBox="0 0 400 310" role="group" aria-label="Tổng độ vi phạm và điểm thử kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="37" x2="363" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="37" y2="273" class="lab-axis" />
      <text x="13" y="28">Tổng vi phạm</text><text x="372" y="297">x</text>
      <text v-for="x in [0,1,2,3,4]" :key="x" :x="view.sx(x)" y="297" text-anchor="middle">{{x}}</text>
      <polyline :points="curve" class="sum-curve" />
      <line :x1="view.sx(1)" :x2="view.sx(3)" :y1="view.sy(2)" :y2="view.sy(2)" class="sum-minimum" />
      <circle :cx="view.sx(trial)" :cy="view.sy(total(trial))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(trial)" :cy="view.sy(total(trial))" r="32" class="lab-handle sum-hit"
        tabindex="0" role="slider" aria-label="Vị trí thử tổng độ vi phạm" aria-valuemin="0" aria-valuemax="4"
        :aria-valuenow="trial" :aria-valuetext="'x = '+fmt(trial)"
        @pointerdown="drag.start('trial',$event)" @keydown="drag.key('trial',[trial,total(trial)],$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh vị trí bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button v-for="x in [1,2,3]" :key="x" type="button" @click="trial=x">Thử x = {{x}}</button>
    </div>
    <div class="lab-readout" role="status">
      <p>x = {{fmt(trial)}}. Vi phạm x ≥ 3 là {{fmt(violations[0])}}. Vi phạm x ≤ 1 là {{fmt(violations[1])}}.</p>
      <p>Tổng {{fmt(total(trial))}}. {{trial>=1&&trial<=3 ? 'Điểm thử là một nghiệm tối ưu của bài toán phụ.' : 'Tổng tại điểm thử còn lớn hơn giá trị tối ưu 2.'}}</p>
    </div>
  </figure>
</template>

<style scoped>
.sum-curve { fill: none; stroke: var(--tim); stroke-width: 1.8; }
.sum-minimum { stroke: var(--xanh); stroke-width: 2.2; }
.sum-hit { fill: transparent !important; stroke: transparent; }
.sum-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
