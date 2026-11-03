<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'
import { clipSegment } from '../services/svg-clipping.mjs'

const graph = ref(null), rail = ref(null)
const quadratic = ref(true), sample = ref(0.5), slope = ref(1)
const bounds = { x0: -2.6, x1: 2.6, y0: -1.7, y1: 3.8 }
const view = ref(makeView({ ...bounds, width: 400, height: 310, pad: 35 }))
const slopeView = ref(makeView({ x0: -1.9, x1: 1.9, y0: -1, y1: 1, width: 400, height: 144, pad: 40 }))
const f = x => quadratic.value ? x*x/2 : Math.abs(x)
const finite = computed(() => quadratic.value || Math.abs(slope.value) <= 1)
const conjugate = computed(() => quadratic.value ? slope.value**2/2 : finite.value ? 0 : Infinity)
const gap = computed(() => f(sample.value) + conjugate.value - sample.value*slope.value)
const contact = computed(() => quadratic.value ? slope.value : 0)
const graphDrag = createDragger(graph, view, (_, [x]) => {
  sample.value = Math.max(-2.4, Math.min(2.4, x))
}, { step: 0.05, snap: 0.01 })
const railDrag = createDragger(rail, slopeView, (_, [x]) => {
  slope.value = Math.max(-1.6, Math.min(1.6, x))
}, { step: 0.05, snap: 0.01 })
const coordinates = list => list.map(p => view.value.point(p).join(',')).join(' ')
const curve = computed(() => coordinates(Array.from({ length: 97 }, (_, i) => {
  const x = (i - 48) / 20
  return [x, f(x)]
})))
const support = computed(() => {
  if (!finite.value) return ''
  const segment = clipSegment([-2.6, 2.6].map(x => [x, slope.value*x-conjugate.value]), bounds)
  return segment ? coordinates(segment) : ''
})
</script>

<template>
  <figure class="study-lab" aria-label="Đường đỡ Fenchel và khoảng cách Fenchel–Young">
    <figcaption class="lab-title">Kéo độ dốc của đường đỡ</figcaption>
    <p class="lab-lead">Kéo chấm tím ở trục độ dốc. Đường xanh nằm thấp hơn hoặc chạm đồ thị f. Kéo chấm vàng trên đồ thị để xem độ chênh giữa f và đường xanh.</p>
    <svg ref="graph" viewBox="0 0 400 310" role="group" aria-label="Đồ thị hàm lồi, đường đỡ và điểm thử kéo được"
      @pointermove="graphDrag.move" @pointerup="graphDrag.end" @pointercancel="graphDrag.end" @lostpointercapture="graphDrag.end">
      <line x1="35" x2="365" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="35" y2="275" class="lab-axis" />
      <text x="15" y="28">f(x)</text><text x="370" :y="view.sy(0)+25">x</text>
      <polyline :points="curve" class="fenchel-curve" />
      <polyline v-if="support" :points="support" class="fenchel-support" />
      <circle v-if="finite" :cx="view.sx(contact)" :cy="view.sy(f(contact))" r="5" class="lab-dot-good" />
      <circle :cx="view.sx(sample)" :cy="view.sy(f(sample))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(sample)" :cy="view.sy(f(sample))" r="32" class="lab-handle fenchel-hit"
        tabindex="0" role="slider" aria-label="Hoành độ điểm thử" aria-valuemin="-2.4" aria-valuemax="2.4"
        :aria-valuenow="sample" :aria-valuetext="'x = '+fmt(sample)"
        @pointerdown="graphDrag.start('point',$event)" @keydown="graphDrag.key('point',[sample,f(sample)],$event)" />
    </svg>
    <svg ref="rail" viewBox="0 0 400 144" role="group" aria-label="Độ dốc y kéo được"
      @pointermove="railDrag.move" @pointerup="railDrag.end" @pointercancel="railDrag.end" @lostpointercapture="railDrag.end">
      <text x="13" y="28">Độ dốc y</text>
      <line :x1="slopeView.sx(-1.6)" :x2="slopeView.sx(1.6)" y1="72" y2="72" class="lab-axis" />
      <text v-for="v in [-1,0,1]" :key="v" :x="slopeView.sx(v)" y="115" text-anchor="middle">{{v}}</text>
      <circle :cx="slopeView.sx(slope)" cy="72" r="7" class="lab-dot-accent" />
      <circle :cx="slopeView.sx(slope)" cy="72" r="32" class="lab-handle fenchel-hit"
        tabindex="0" role="slider" aria-label="Độ dốc của đường đỡ" aria-valuemin="-1.6" aria-valuemax="1.6"
        :aria-valuenow="slope" :aria-valuetext="'y = '+fmt(slope)"
        @pointerdown="railDrag.start('slope',$event)" @keydown="railDrag.key('slope',[slope,0],$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút</summary><LabPointControls :svg="graph" axes="x" /><LabPointControls :svg="rail" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="quadratic" @click="quadratic=true">Bình phương</button>
      <button type="button" :aria-pressed="!quadratic" @click="quadratic=false">Trị tuyệt đối</button>
      <button type="button" @click="slope=1.5">Độ dốc 1,5</button>
      <button type="button" @click="slope=1">Độ dốc 1</button>
      <button v-if="finite" type="button" @click="sample=contact">Đưa x về điểm chạm</button>
    </div>
    <div class="lab-readout" role="status">
      <p>x = {{fmt(sample)}}, y = {{fmt(slope)}}.</p>
      <p v-if="finite">f*(y) = {{fmt(conjugate,4)}}. Độ chênh Fenchel–Young bằng {{fmt(gap,4)}}. Khi độ chênh bằng 0, điểm thử nằm trên đường đỡ.</p>
      <p v-else>f*(y) = +∞. Với f(x) = |x|, độ dốc có trị tuyệt đối lớn hơn 1 khiến yx − f(x) tăng vô hạn theo một hướng.</p>
      <p v-if="!quadratic && Math.abs(slope) === 1">Ở độ dốc này, đường đỡ trùng với cả một nhánh của đồ thị.</p>
    </div>
  </figure>
</template>

<style scoped>
.fenchel-curve, .fenchel-support { fill: none; stroke-width: 1.8; }
.fenchel-curve { stroke: var(--tim); }
.fenchel-support { stroke: var(--xanh); stroke-dasharray: 5 4; }
.fenchel-hit { fill: transparent !important; stroke: transparent; }
.fenchel-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
figure > svg + svg { margin-top: var(--space-3); }
</style>
