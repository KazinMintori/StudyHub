<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const svg = ref(null)
const height = ref(2.4)
const limit = Math.sqrt(8)
const view = ref(makeView({ x0: -0.6, x1: 6.8, y0: -0.6, y1: 3.7, width: 400, height: 265, pad: 26 }))
const left = computed(() => 4 / height.value)
const width = computed(() => 12 / height.value)
const drag = createDragger(svg, view, (_, [, y]) => {
  height.value = Math.max(2, Math.min(limit, y))
}, { step: 0.05, snap: 0.01 })
</script>

<template>
  <figure class="study-lab" aria-label="Mặt bằng hai khối với một lát cắt dọc">
    <figcaption class="lab-title">Nhiều hình dạng có cùng diện tích bao</figcaption>
    <p class="lab-lead">Kéo chấm vàng lên xuống để đổi chiều cao chung. Hai khối giữ diện tích 4 và 8 nên cùng hẹp lại khi chiều cao tăng. Đường giữa hai khối là lát cắt dọc.</p>
    <svg ref="svg" viewBox="0 0 400 265" role="group" aria-label="Hai khối và chiều cao chung có thể kéo"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <rect :x="view.sx(0)" :y="view.sy(height)" :width="view.sx(left)-view.sx(0)"
        :height="view.sy(0)-view.sy(height)" class="left-block" />
      <rect :x="view.sx(left)" :y="view.sy(height)" :width="view.sx(width)-view.sx(left)"
        :height="view.sy(0)-view.sy(height)" class="right-block" />
      <text :x="view.sx(left/2)" :y="view.sy(height/2)+6" text-anchor="middle">A · 4</text>
      <text :x="view.sx((left+width)/2)" :y="view.sy(height/2)+6" text-anchor="middle">B · 8</text>
      <line :x1="view.sx(left)" :x2="view.sx(left)" :y1="view.sy(height)" :y2="view.sy(0)" class="lab-guide" />
      <circle :cx="view.sx(left)" :cy="view.sy(height)" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(left)" :cy="view.sy(height)" r="31" class="lab-handle slicing-hit"
        tabindex="0" role="slider" aria-label="Chiều cao chung" aria-valuemin="2" :aria-valuemax="limit"
        :aria-valuenow="height" :aria-valuetext="'H = ' + fmt(height, 3)" aria-orientation="vertical"
        @pointerdown="drag.start('height', $event)" @keydown="drag.key('height', [left,height], $event)" />
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh chiều cao bằng nút</summary>
      <LabPointControls :svg="svg" axes="y" />
    </details>
    <div class="lab-buttons">
      <button type="button" @click="height = 2">H = 2</button>
      <button type="button" @click="height = 2.5">H = 2,5</button>
      <button type="button" @click="height = limit">H = √8</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Chiều rộng A {{ fmt(left, 3) }}, B {{ fmt(width-left, 3) }}. Khung bao rộng {{ fmt(width, 3) }} và cao {{ fmt(height, 3) }}.</p>
      <p>Tỉ lệ cao/rộng của A là {{ fmt(height/left, 3) }}, của B là {{ fmt(height/(width-left), 3) }}. Cả hai nằm từ 0,5 đến 2.</p>
      <p>Diện tích khung bao {{ fmt(width*height) }}. Mỗi chiều cao trong khoảng này cho một nghiệm tối ưu.</p>
    </div>
  </figure>
</template>

<style scoped>
.left-block { fill: var(--tim-soft); stroke: var(--tim); stroke-width: 1.3; }
.right-block { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.3; }
.slicing-hit { fill: transparent !important; stroke: transparent; }
.slicing-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 21px; pointer-events: none; }
</style>
