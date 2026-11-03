<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt, fmtPoint } from '../controllers/svg-drag.js'

const svg = ref(null), position = ref([1, 1]), extra = ref(false)
const view = ref(makeView({ x0: -0.45, x1: 4.45, y0: -0.5, y1: 3.6, width: 400, height: 320, pad: 30 }))
const drag = createDragger(svg, view, (_, [x, y]) => {
  position.value = [Math.min(4, Math.max(0, x)), Math.min(3, Math.max(0, y))]
}, { step: 0.1, snap: 0.05 })
const terminals = computed(() => [
  { name: 'A', x: 0, y: 0, weight: 2 },
  { name: 'B', x: 4, y: 0, weight: 3 },
  ...(extra.value ? [{ name: 'D', x: 2, y: 3, weight: 4 }] : [])
])
const length = ({ x, y }) => Math.abs(x - position.value[0]) + Math.abs(y - position.value[1])
const cost = computed(() => terminals.value.reduce((sum, item) => sum + item.weight * length(item), 0))
const optimal = computed(() => extra.value ? [2, 0] : [4, 0])
const polyline = points => points.map(p => view.value.point(p).join(',')).join(' ')
</script>

<template>
  <figure class="study-lab" aria-label="Tối ưu dây nối Manhattan giữa các đầu nối">
    <figcaption class="lab-title">Kéo đầu nối C để so sánh tổng độ dài</figcaption>
    <p class="lab-lead">Mỗi dây chỉ đi ngang và dọc. Kéo điểm vàng để đổi vị trí C. Hình này dùng đầu nối dạng điểm, theo mô hình định vị sơ bộ.</p>
    <svg ref="svg" viewBox="0 0 400 320" role="group" aria-label="Các đầu nối cố định và điểm C kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <rect :x="view.sx(0)" :y="view.sy(3)" :width="view.sx(4)-view.sx(0)" :height="view.sy(0)-view.sy(3)" class="wire-box" />
      <g v-for="(item, index) in terminals" :key="item.name">
        <polyline :points="polyline([[item.x,item.y],[item.x,position[1]],position])"
          class="wire-path" :class="'wire-' + index" />
        <circle :cx="view.sx(item.x)" :cy="view.sy(item.y)" r="5" class="lab-dot-accent" />
        <text :x="view.sx(item.x)" :y="view.sy(item.y)+(item.y ? -17 : 25)" text-anchor="middle">{{ item.name }}</text>
      </g>
      <circle :cx="view.sx(position[0])" :cy="view.sy(position[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(position[0])" :cy="view.sy(position[1])" r="31" class="lab-handle wire-hit"
        tabindex="0" role="slider" aria-label="Đầu nối C" :aria-valuetext="fmtPoint(position)"
        @pointerdown="drag.start('point', $event)" @keydown="drag.key('point', position, $event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh C bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="extra" @click="extra = !extra">Thêm hoặc bỏ D</button>
      <button type="button" @click="position = optimal">Đưa C đến điểm tối ưu</button>
    </div>
    <div class="lab-readout" role="status">
      <p>C tại {{ fmtPoint(position) }}. Tổng chi phí có trọng số {{ fmt(cost) }}.</p>
      <p v-for="item in terminals" :key="item.name">Dây tới {{ item.name }} dài {{ fmt(length(item)) }}, trọng số {{ item.weight }}.</p>
      <p>Vị trí tối ưu {{ fmtPoint(optimal) }} có chi phí {{ extra ? 22 : 8 }}.</p>
    </div>
  </figure>
</template>

<style scoped>
.wire-box { fill: var(--paper); stroke: var(--ink-3); stroke-width: 1.2; }
.wire-path { fill: none; stroke: var(--tim); stroke-width: 1.5; }
.wire-1 { stroke: var(--xanh); stroke-dasharray: 5 4; }
.wire-2 { stroke: var(--do); stroke-dasharray: 2 4; }
.wire-hit { fill: transparent !important; stroke: transparent; }
.wire-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
