<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const svg = ref(null)
const threshold = ref(1.5)
const shift = ref(1.25)
const view = ref(makeView({ x0: -3.35, x1: 3.6, y0: -0.35, y1: 2.5, width: 400, height: 300, pad: 35 }))
const drag = createDragger(svg, view, (name, [x]) => {
  if (name === 'threshold') threshold.value = Math.min(2.8, Math.max(0.6, x))
  else shift.value = Math.min(2.5, Math.max(0.05, -x))
}, { step: 0.05, snap: 0.01 })
const expectation = computed(() => (1 + shift.value ** 2) / (threshold.value + shift.value) ** 2)
const optimalShift = computed(() => 1 / threshold.value)
const best = computed(() => 1 / (1 + threshold.value ** 2))
const point = coordinates => view.value.point(coordinates).join(',')
const curve = computed(() => {
  const a = threshold.value, u = shift.value, radius = (a + u) * Math.sqrt(2.3)
  const from = Math.max(-3.2, -u - radius), to = Math.min(3.45, -u + radius)
  return Array.from({ length: 121 }, (_, i) => {
    const x = from + (to - from) * i / 120
    return point([x, ((x + u) / (a + u)) ** 2])
  }).join(' ')
})
</script>

<template>
  <figure class="study-lab" aria-label="Parabol chứng minh bất đẳng thức Cantelli">
    <figcaption class="lab-title">Dịch đỉnh parabol để giảm kỳ vọng của hàm chặn</figcaption>
    <p class="lab-lead">Giữ kỳ vọng của X bằng 0 và phương sai bằng 1. Kéo chấm vàng để đổi ngưỡng a hoặc kéo chấm xanh để đổi đỉnh −u. Parabol tím luôn chặn trên hàm chỉ thị nét đứt.</p>
    <svg ref="svg" viewBox="0 0 400 300" role="group" aria-label="Ngưỡng đuôi và đỉnh parabol kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <rect :x="view.sx(threshold)" y="35" :width="view.sx(3.45)-view.sx(threshold)"
        :height="view.sy(0)-35" class="cantelli-tail" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="35" :y2="view.sy(0)" class="lab-axis" />
      <line x1="32" x2="370" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <polyline :points="[point([-3.2, 0]), point([threshold, 0])].join(' ')" class="lab-guide" />
      <polyline :points="[point([threshold, 1]), point([3.45, 1])].join(' ')" class="lab-guide" />
      <circle :cx="view.sx(threshold)" :cy="view.sy(0)" r="4" class="cantelli-open" />
      <polyline :points="curve" class="lab-accent" />
      <text x="15" y="28">Giá trị</text>
      <text x="373" y="280">x</text>
      <text v-for="t in [-3, 0, 3]" :key="t" :x="view.sx(t)" y="280" text-anchor="middle">{{ t }}</text>
      <g v-for="{ name, x, y, label, color, min, max } in [
        { name: 'threshold', x: threshold, y: 1, label: 'Ngưỡng a', color: 'lab-dot-warn', min: 0.6, max: 2.8 },
        { name: 'vertex', x: -shift, y: 0, label: 'Hoành độ đỉnh', color: 'lab-dot-good', min: -2.5, max: -0.05 }
      ]" :key="name">
        <circle :cx="view.sx(x)" :cy="view.sy(y)" r="7" :class="color" />
        <circle :cx="view.sx(x)" :cy="view.sy(y)" r="31" class="lab-handle cantelli-hit"
          tabindex="0" role="slider" :aria-label="label" :aria-valuemin="min" :aria-valuemax="max"
          :aria-valuenow="x" :aria-valuetext="label + ' ' + fmt(x)"
          @pointerdown="drag.start(name, $event)" @keydown="drag.key(name, [x,y], $event)" />
      </g>
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh các điểm bằng nút</summary>
      <LabPointControls :svg="svg" axes="x" />
    </details>
    <div class="lab-buttons">
      <button type="button" @click="shift = optimalShift">Đặt đỉnh tại −1/a</button>
      <button type="button" @click="threshold = 2; shift = 0.5">Ví dụ a = 2</button>
    </div>
    <div class="lab-readout" role="status">
      <p>a = {{ fmt(threshold) }}, u = {{ fmt(shift, 3) }}. Kỳ vọng của parabol {{ fmt(expectation, 4) }}.</p>
      <p>Giá trị nhỏ nhất là {{ fmt(best, 4) }} khi u = 1/a. Cận đạt được bởi phân phối hai điểm đặt xác suất {{ fmt(best, 4) }} tại a và phần còn lại tại −1/a.</p>
    </div>
  </figure>
</template>

<style scoped>
.cantelli-tail { fill: var(--vang-soft); }
.cantelli-open { fill: var(--paper); stroke: var(--ink-2); stroke-width: 1.4; }
.cantelli-hit { fill: transparent !important; stroke: transparent; }
.cantelli-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
