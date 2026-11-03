<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const svg = ref(null)
const threshold = ref(-1.5)
const view = ref(makeView({ x0: -3, x1: 2.2, y0: -3, y1: 2.2, width: 400, height: 400, pad: 38 }))
const point = computed(() => [threshold.value / 2, threshold.value / 2])
const polygon = computed(() => [[0,0], [threshold.value,0], [0,threshold.value]]
  .map(coordinates => view.value.point(coordinates).join(',')).join(' '))
const drag = createDragger(svg, view, (_, [x,y]) => {
  threshold.value = Math.max(-2.5, Math.min(2.5, x+y))
}, { step: 0.1, snap: 0.05 })
const line = computed(() => {
  const a = threshold.value
  const left = Math.max(-3, a-2.2)
  const right = Math.min(2.2, a+3)
  return [[left,a-left], [right,a-right]].map(p => view.value.point(p).join(',')).join(' ')
})
</script>

<template>
  <figure class="study-lab" aria-label="Miền nghiệm và chứng chỉ Farkas">
    <figcaption class="lab-title">Kéo đường biên cho tới khi miền nghiệm biến mất</figcaption>
    <p class="lab-lead">Hai điều kiện cố định là x ≤ 0 và y ≤ 0. Kéo chấm vàng để dời đường x + y = a. Điều kiện thứ ba giữ phía x + y ≥ a. Phần xanh là giao của cả ba điều kiện.</p>
    <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Ba biên và điểm kéo ngưỡng a"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <rect :x="view.sx(-3)" :y="view.sy(0)" :width="view.sx(0)-view.sx(-3)"
        :height="view.sy(-3)-view.sy(0)" class="farkas-quadrant" />
      <polygon v-if="threshold < 0" :points="polygon" class="farkas-feasible" />
      <line x1="38" x2="362" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="38" y2="362" class="lab-axis" />
      <text x="370" :y="view.sy(0)+5">x</text>
      <text :x="view.sx(0)+12" y="30">y</text>
      <polyline :points="line" class="farkas-boundary" />
      <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="32" class="lab-handle farkas-hit"
        tabindex="0" role="slider" aria-label="Ngưỡng a của tổng x và y" aria-valuemin="-2.5" aria-valuemax="2.5"
        :aria-valuenow="threshold" :aria-valuetext="'a = ' + fmt(threshold)"
        @pointerdown="drag.start('a',$event)" @keydown="drag.key('a',point,$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh ngưỡng bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" @click="threshold=-1.5">Có miền nghiệm</button>
      <button type="button" @click="threshold=0">Chỉ còn gốc tọa độ</button>
      <button type="button" @click="threshold=1">Hiện chứng chỉ vô nghiệm</button>
    </div>
    <div class="lab-readout" role="status">
      <p>a = {{fmt(threshold)}}. {{threshold<0 ? 'Miền khả thi là tam giác xanh.' : threshold===0 ? 'Nghiệm duy nhất là (0, 0).' : 'Ba điều kiện không có điểm chung.'}}</p>
      <p v-if="threshold>0">Viết điều kiện cuối thành −x − y ≤ −a. Cộng ba bất đẳng thức với hệ số (1, 1, 1) triệt tiêu vế trái. Kết quả 0 ≤ {{fmt(-threshold)}} là mâu thuẫn.</p>
      <p v-else>Gốc tọa độ thỏa cả ba điều kiện. Hệ số (1, 1, 1) vẫn triệt tiêu vế trái, nhưng vế phải −a không âm.</p>
    </div>
  </figure>
</template>

<style scoped>
.farkas-quadrant { fill: var(--tim-soft); }
.farkas-feasible { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.5; }
.farkas-boundary { fill: none; stroke: var(--tim); stroke-width: 1.8; stroke-dasharray: 5 4; }
.farkas-hit { fill: transparent !important; stroke: transparent; }
.farkas-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
