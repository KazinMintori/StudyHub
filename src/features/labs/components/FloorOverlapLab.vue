<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt, fmtPoint } from '../controllers/svg-drag.js'

const svg = ref(null)
const offset = ref([2,0])
const view = ref(makeView({ x0: -4.2, x1: 4.2, y0: -3.4, y1: 3.4, width: 400, height: 335, pad: 24 }))
const drag = createDragger(svg, view, (_, [x,y]) => {
  offset.value = [Math.max(-3,Math.min(3,x)), Math.max(-2.4,Math.min(2.4,y))]
}, { step: 0.1, snap: 0.05 })
const width = computed(() => Math.max(0, 2-Math.abs(offset.value[0])))
const height = computed(() => Math.max(0, 2-Math.abs(offset.value[1])))
const area = computed(() => width.value * height.value)
</script>

<template>
  <figure class="study-lab" aria-label="Hai hình vuông và tính không lồi của ràng buộc">
    <figcaption class="lab-title">Hai vị trí hợp lệ, trung điểm chồng lấn</figcaption>
    <p class="lab-lead">Khối xanh đứng yên. Kéo tâm khối tím để thay độ dời. Hai khối có thể chạm cạnh hoặc chạm góc, miễn phần trong của chúng rời nhau.</p>
    <svg ref="svg" viewBox="0 0 400 335" role="group" aria-label="Hai khối cạnh 2 và tâm khối tím kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="24" x2="376" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="24" y2="310" class="lab-axis" />
      <rect :x="view.sx(-1)" :y="view.sy(1)" :width="view.sx(1)-view.sx(-1)" :height="view.sy(-1)-view.sy(1)" class="fixed-square" />
      <rect :x="view.sx(offset[0]-1)" :y="view.sy(offset[1]+1)"
        :width="view.sx(1)-view.sx(-1)" :height="view.sy(-1)-view.sy(1)" class="moving-square" />
      <rect v-if="area > 0" :x="view.sx(Math.max(-1,offset[0]-1))" :y="view.sy(Math.min(1,offset[1]+1))"
        :width="view.sx(width)-view.sx(0)" :height="view.sy(0)-view.sy(height)" class="overlap-square" />
      <circle :cx="view.sx(offset[0])" :cy="view.sy(offset[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(offset[0])" :cy="view.sy(offset[1])" r="31" class="lab-handle floor-hit"
        tabindex="0" role="slider" aria-label="Tâm khối di động" :aria-valuetext="fmtPoint(offset)"
        @pointerdown="drag.start('offset', $event)" @keydown="drag.key('offset', offset, $event)" />
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh tâm bằng nút</summary>
      <LabPointControls :svg="svg" />
    </details>
    <div class="lab-buttons">
      <button type="button" @click="offset = [-2,0]">Chạm cạnh trái</button>
      <button type="button" @click="offset = [2,0]">Chạm cạnh phải</button>
      <button type="button" @click="offset = [0,0]">Thử trung điểm</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Độ dời {{ fmtPoint(offset) }}. Diện tích giao {{ fmt(area) }}.</p>
      <p v-if="area > 0">Cả hai độ dời theo trục đều có trị tuyệt đối nhỏ hơn 2. Hai phần trong giao nhau.</p>
      <p v-else>Ít nhất một độ dời theo trục có trị tuyệt đối từ 2 trở lên. Hai phần trong rời nhau.</p>
    </div>
  </figure>
</template>

<style scoped>
.fixed-square { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.5; }
.moving-square { fill: var(--tim-soft); stroke: var(--tim); stroke-width: 1.5; }
.overlap-square { fill: var(--do-soft); stroke: var(--do); stroke-width: 1.5; }
.floor-hit { fill: transparent !important; stroke: transparent; }
.floor-hit:focus-visible { stroke: var(--vang); }
</style>
