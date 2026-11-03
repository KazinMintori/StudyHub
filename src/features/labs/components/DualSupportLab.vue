<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, makeView } from '../controllers/svg-drag.js'
import { clipSegment } from '../services/svg-clipping.mjs'

const svg = ref(null)
const multiplier = ref(1)
const bounds = { x0: -1.15, x1: 2.1, y0: -0.65, y1: 4.5 }
const view = ref(makeView({ ...bounds, width: 400, height: 350, pad: 37 }))
const u = computed(() => 1 - multiplier.value / 2)
const dual = computed(() => multiplier.value - multiplier.value ** 2 / 4)
const lower = value => Math.max(0, 1 - value) ** 2
const coords = points => points.map(point => view.value.point(point).join(',')).join(' ')
const boundary = Array.from({ length: 109 }, (_, i) => {
  const x = -1.1 + i * 3.15 / 108
  return [x, lower(x)]
})
const upperSet = coords([...boundary, [2.05, 4.5], [-1.1, 4.5]])
const supportingLine = computed(() => {
  const segment = clipSegment([bounds.x0, bounds.x1].map(x => [x, dual.value - multiplier.value * x]), bounds)
  return segment ? coords(segment) : ''
})
const drag = createDragger(svg, view, (_, [x]) => {
  multiplier.value = Math.max(0, Math.min(4, 2 * (1 - x)))
}, { step: 0.05, snap: 0.025 })
</script>

<template>
  <figure class="study-lab" aria-label="Tập trên và đường tựa của bài toán đối ngẫu">
    <figcaption class="lab-title">Đọc cận dưới ở giao điểm với trục tung</figcaption>
    <p class="lab-lead">Vùng tím là phần tập trên nằm trong khung. Kéo chấm vàng dọc biên dưới. Đường xanh đi qua chấm vàng với độ dốc −λ. Giao điểm của đường xanh với trục tung cho cận dưới g(λ).</p>
    <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Tập trên, đường tựa và điểm tiếp xúc kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polygon :points="upperSet" class="dual-upper" />
      <line x1="37" x2="363" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="37" y2="313" class="lab-axis" />
      <text :x="view.sx(0)+10" y="27">t</text>
      <text x="373" :y="view.sy(0)+8">u</text>
      <text x="279" y="85">Tập trên A</text>
      <polyline :points="coords(boundary)" class="dual-edge" />
      <polyline :points="supportingLine" class="dual-support" />
      <circle :cx="view.sx(0)" :cy="view.sy(1)" r="5" class="lab-dot-accent" />
      <circle :cx="view.sx(0)" :cy="view.sy(dual)" r="4" class="lab-dot-good" />
      <circle :cx="view.sx(u)" :cy="view.sy(lower(u))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(u)" :cy="view.sy(lower(u))" r="31" class="lab-handle dual-support-hit"
        tabindex="0" role="slider" aria-label="Hoành độ điểm tựa" aria-valuemin="-1" aria-valuemax="1"
        :aria-valuenow="u" :aria-valuetext="'u = ' + fmt(u)"
        @pointerdown="drag.start('contact',$event)" @keydown="drag.key('contact',[u,lower(u)],$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm tựa bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button v-for="value in [0,1,2,4]" :key="value" type="button" @click="multiplier=value">Đường tựa λ = {{value}}</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Điểm tựa có u = {{fmt(u)}}. Nhân tử λ = {{fmt(multiplier)}} và tung độ cắt trục g(λ) = {{fmt(dual,4)}}.</p>
      <p>Điểm tím trên trục tung có giá trị p* = 1. {{multiplier===2 ? 'Đường tựa đi qua điểm này.' : 'Đường tựa cắt trục tung ở phía dưới điểm này.'}}</p>
    </div>
  </figure>
</template>

<style scoped>
.dual-upper { fill: var(--tim-soft); }
.dual-edge, .dual-support { fill: none; stroke-width: 1.7; }
.dual-edge { stroke: var(--tim); }
.dual-support { stroke: var(--xanh); stroke-dasharray: 5 4; }
.dual-support-hit { fill: transparent !important; stroke: transparent; }
.dual-support-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
