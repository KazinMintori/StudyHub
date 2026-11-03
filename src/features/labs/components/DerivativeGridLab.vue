<script setup>
import { ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const svg = ref(null)
const x = ref(0.15)
const derivative = t => (t - 0.5) ** 2 - 1 / 16
const grid = [-1, 0, 1]
const view = ref(makeView({ x0: -1.1, x1: 1.1, y0: -0.28, y1: 2.4, width: 400, height: 280, pad: 32 }))
const curve = Array.from({ length: 101 }, (_, i) => {
  const t = i / 50 - 1
  return view.value.point([t, derivative(t)]).join(',')
}).join(' ')
const drag = createDragger(svg, view, (_, [t]) => {
  x.value = Math.max(-1, Math.min(1, t))
}, { step: 0.05, snap: 0.01 })
</script>

<template>
  <figure class="study-lab" aria-label="Kiểm tra đạo hàm trên lưới">
    <figcaption class="lab-title">Ba điểm kiểm tra bỏ sót đoạn đạo hàm âm</figcaption>
    <p class="lab-lead">Ba chấm xanh là các điểm kiểm tra. Kéo chấm vàng qua khoảng giữa 0 và 1 để xem đạo hàm tại một điểm ngoài lưới.</p>
    <svg ref="svg" viewBox="0 0 400 280" role="group" aria-label="Đồ thị đạo hàm và điểm thử kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="30" x2="370" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="34" y2="245" class="lab-grid" />
      <text x="15" y="27">f′(x)</text>
      <text x="375" y="265">x</text>
      <text v-for="t in grid" :key="t" :x="view.sx(t)" y="265" text-anchor="middle">{{ t }}</text>
      <polyline :points="curve" class="lab-accent" />
      <circle v-for="t in grid" :key="t" :cx="view.sx(t)" :cy="view.sy(derivative(t))" r="6" class="lab-dot-good" />
      <line :x1="view.sx(x)" :x2="view.sx(x)" :y1="view.sy(0)" :y2="view.sy(derivative(x))" class="lab-guide" />
      <circle :cx="view.sx(x)" :cy="view.sy(derivative(x))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(x)" :cy="view.sy(derivative(x))" r="31" class="lab-handle grid-hit"
        tabindex="0" role="slider" aria-label="Hoành độ điểm thử" :aria-valuemin="-1" :aria-valuemax="1"
        :aria-valuenow="x" :aria-valuetext="'x = ' + fmt(x)"
        @pointerdown="drag.start('probe', $event)" @keydown="drag.key('probe', [x, derivative(x)], $event)" />
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh điểm thử bằng nút</summary>
      <LabPointControls :svg="svg" axes="x" />
    </details>
    <div class="lab-buttons">
      <button type="button" @click="x = 0">Nút x = 0</button>
      <button type="button" @click="x = 0.5">Giữa x = 0,5</button>
      <button type="button" @click="x = 1">Nút x = 1</button>
    </div>
    <div class="lab-readout" role="status">
      <p>x = {{ fmt(x) }}, f′(x) = {{ fmt(derivative(x), 4) }}.</p>
      <p v-if="derivative(x) < 0">Đạo hàm âm tại điểm này, nên hàm giảm trong một lân cận của điểm thử.</p>
      <p v-else>Đạo hàm không âm tại điểm này. Để kết luận hàm không giảm trên cả đoạn, cần kiểm soát dấu giữa các nút.</p>
    </div>
  </figure>
</template>

<style scoped>
.grid-hit { fill: transparent !important; stroke: transparent; }
.grid-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
