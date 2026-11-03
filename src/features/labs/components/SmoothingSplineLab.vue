<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { makeView, createDragger, fmt } from '../controllers/svg-drag.js'
import { smoothNaturalSpline } from '../services/smoothing-spline.mjs'

const initial = [[0, 0], [1, 2.5], [2, 1], [3, 3], [4, 2], [5, 3.5]]
const points = ref(initial)
const penalty = ref(0.25)
const svg = ref(null)
const view = ref(makeView({ x0: -0.3, x1: 5.3, y0: -1.5, y1: 5, width: 400, height: 290, pad: 32 }))
const drag = createDragger(svg, view, (name, [, y]) => {
  points.value = points.value.map(([x, observed], i) =>
    [x, i === Number(name) ? Math.max(-0.5, Math.min(4, y)) : observed]
  )
}, { step: 0.1, snap: 0.1 })
const fit = computed(() => smoothNaturalSpline(points.value, penalty.value))
const curve = computed(() => Array.from({ length: 151 }, (_, i) => {
  const x = i / 30
  return view.value.point([x, fit.value.evaluate(x)]).join(',')
}).join(' '))
const error = computed(() => points.value.reduce((sum, [, y], i) =>
  sum + (fit.value.values[i] - y) ** 2, 0))
const levels = [
  { value: 0, label: 'Nội suy' },
  { value: 0.05, label: 'Phạt nhẹ' },
  { value: 0.25, label: 'Phạt vừa' },
  { value: 2, label: 'Phạt mạnh' },
  { value: Infinity, label: 'Giới hạn đường thẳng' }
]
</script>

<template>
  <figure class="study-lab" aria-label="Làm mượt bằng spline bậc ba tự nhiên">
    <figcaption class="lab-title">Từ đường nội suy đến đường hồi quy</figcaption>
    <p class="lab-lead">Kéo các điểm vàng theo chiều dọc. Đường tím đi qua các nút đã hiệu chỉnh. Đoạn nét đứt nối giá trị đo với giá trị khớp tại cùng hoành độ.</p>
    <svg ref="svg" viewBox="0 0 400 290" role="group" aria-label="Đường spline và sáu điểm đo có thể kéo"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="30" x2="370" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line x1="30" x2="30" y1="34" y2="248" class="lab-axis" />
      <text x="368" y="274">x</text>
      <text x="12" y="29">y</text>
      <g v-for="y in [0, 2, 4]" :key="y">
        <line v-if="y" x1="30" x2="370" :y1="view.sy(y)" :y2="view.sy(y)" class="lab-grid" />
        <text x="12" :y="view.sy(y) + 5">{{ y }}</text>
      </g>
      <g v-for="([x, y], i) in points" :key="x">
        <line :x1="view.sx(x)" :x2="view.sx(x)" :y1="view.sy(y)" :y2="view.sy(fit.values[i])" class="lab-guide" />
        <text :x="view.sx(x)" y="274" text-anchor="middle">{{ x }}</text>
      </g>
      <polyline :points="curve" class="lab-accent" />
      <g v-for="([x, y], i) in points" :key="i">
        <circle :cx="view.sx(x)" :cy="view.sy(y)" r="6" class="lab-dot-warn" />
        <circle :cx="view.sx(x)" :cy="view.sy(y)" r="30" class="lab-handle spline-hit" tabindex="0" role="slider"
          :aria-label="`Điểm đo tại x bằng ${x}`" :aria-valuemin="-0.5" :aria-valuemax="4"
          :aria-valuenow="y" :aria-valuetext="'y = ' + fmt(y)" aria-orientation="vertical"
          @pointerdown="drag.start(String(i), $event)" @keydown="drag.key(String(i), [x, y], $event)" />
      </g>
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh điểm bằng nút</summary>
      <LabPointControls :svg="svg" axes="y" />
    </details>
    <div class="lab-buttons">
      <button v-for="level in levels" :key="level.value" type="button" :aria-pressed="penalty === level.value"
        @click="penalty = level.value">{{ level.label }}</button>
      <button type="button" @click="points = initial">Đặt lại điểm</button>
    </div>
    <div class="lab-readout" role="status">
      <p v-if="penalty === Infinity">Giới hạn khi λ tăng vô hạn là đường hồi quy bình phương tối thiểu.</p>
      <p v-else>Mức phạt λ = {{ fmt(penalty) }}.</p>
      <p>Tổng bình phương phần dư {{ fmt(error, 3) }}. Tích phân bình phương đạo hàm bậc hai {{ fmt(fit.roughness, 3) }}.</p>
    </div>
  </figure>
</template>

<style scoped>
.spline-hit { fill: transparent !important; stroke: transparent; }
.spline-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
