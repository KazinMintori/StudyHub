<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt, fmtPoint } from '../controllers/svg-drag.js'

const svg = ref(null)
const probe = ref([0.22, 0.43])
const copies = ref(1)
const inradius = 1 / (2 + Math.SQRT2)
const analytic = computed(() => [copies.value/(copies.value+2), 1/(copies.value+2)])
const view = ref(makeView({ x0: -0.18, x1: 1.18, y0: -0.18, y1: 1.18, width: 400, height: 400, pad: 38 }))
const drag = createDragger(svg, view, (_, [x,y]) => {
  const px = Math.max(0.02,x), py = Math.max(0.02,y)
  const scale = Math.max(1,(px+py-0.04)/0.94)
  probe.value = [0.02+(px-0.02)/scale,0.02+(py-0.02)/scale]
}, { step: 0.025 })
const barrier = ([x,y]) => -copies.value*Math.log(x) - Math.log(y) - Math.log(1-x-y)
const barrierGradient = computed(() => {
  const [x,y] = probe.value
  const inv = 1/(1-x-y)
  return [inv-copies.value/x,inv-1/y]
})
const outline = [[0,0],[1,0],[0,1]].map(p=>view.value.point(p).join(',')).join(' ')
</script>

<template>
  <figure class="study-lab" aria-label="Tâm giải tích và tâm Chebyshev của tam giác">
    <figcaption class="lab-title">Cùng một tam giác, tâm giải tích có thể đổi</figcaption>
    <p class="lab-lead">Kéo điểm thử màu vàng để đọc hàm chắn. Thêm bản sao của cạnh x₁ = 0 để đổi hàm chắn trong khi tam giác và đường tròn nội tiếp giữ nguyên.</p>
    <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Tam giác, hai tâm và điểm thử kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polygon :points="outline" class="center-triangle" />
      <circle :cx="view.sx(inradius)" :cy="view.sy(inradius)" :r="view.sx(inradius)-view.sx(0)" class="center-circle" />
      <line v-if="copies>1" :x1="view.sx(0)" :x2="view.sx(0)" :y1="view.sy(0)" :y2="view.sy(1)" class="lab-guide" />
      <text :x="view.sx(1)+12" :y="view.sy(0)+14">x₁</text>
      <text :x="view.sx(0)-26" :y="view.sy(1)-9">x₂</text>
      <circle :cx="view.sx(inradius)" :cy="view.sy(inradius)" r="4" class="lab-dot-good" />
      <circle :cx="view.sx(analytic[0])" :cy="view.sy(analytic[1])" r="5" class="lab-dot-accent" />
      <circle :cx="view.sx(probe[0])" :cy="view.sy(probe[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(probe[0])" :cy="view.sy(probe[1])" r="31" class="lab-handle center-hit"
        tabindex="0" role="slider" aria-label="Điểm thử của hàm chắn" :aria-valuetext="fmtPoint(probe,3)"
        @pointerdown="drag.start('probe', $event)" @keydown="drag.key('probe', probe, $event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm thử bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" @click="copies=1">Mỗi cạnh một lần</button>
      <button type="button" @click="copies=2">Lặp cạnh trái</button>
      <button type="button" @click="probe=analytic">Đưa điểm thử tới tâm giải tích</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Tâm xanh của đường tròn nội tiếp {{ fmtPoint([inradius,inradius],4) }}. Tâm giải tích màu tím {{ fmtPoint(analytic,4) }}.</p>
      <p>Điểm thử {{ fmtPoint(probe,4) }}. Giá trị hàm chắn {{ fmt(barrier(probe),4) }}, gradient {{ fmtPoint(barrierGradient,3) }}.</p>
    </div>
  </figure>
</template>

<style scoped>
.center-triangle { fill: var(--paper); stroke: var(--ink-3); stroke-width: 1.4; }
.center-circle { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.4; }
.center-hit { fill: transparent !important; stroke: transparent; }
.center-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
