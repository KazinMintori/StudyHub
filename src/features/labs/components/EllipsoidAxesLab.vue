<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'
import { project3 } from '../services/foundation-geometry.mjs'

const svg = ref(null)
const radii = ref([1.8, 1])
const third = ref(1)
const space = ref(false)
const view = ref(makeView({ x0: -3.1, x1: 3.1, y0: -3.1, y1: 3.1, width: 400, height: 400, pad: 32 }))
const drag = createDragger(svg, view, (name, point) => {
  const axis = Number(name)
  radii.value = radii.value.map((value, i) => i === axis ? Math.max(0.6, Math.min(2.5, point[axis])) : value)
}, { step: 0.05, snap: 0.025 })
const determinant = computed(() => radii.value[0] * radii.value[1] * (space.value ? third.value : 1))
const camera = { yaw: 30, pitch: 25, scale: 52, origin: [200, 197] }
const poly = points => points.map(point => project3(point, camera).join(',')).join(' ')
const mesh = computed(() => {
  const [a, b] = radii.value
  const c = third.value
  const rings = [-Math.PI/4, 0, Math.PI/4].map(latitude =>
    Array.from({ length: 73 }, (_, i) => {
      const angle = Math.PI * i / 36
      return [a * Math.cos(latitude) * Math.cos(angle), b * Math.cos(latitude) * Math.sin(angle), c * Math.sin(latitude)]
    })
  )
  const meridians = [0, Math.PI/3, 2*Math.PI/3].map(longitude =>
    Array.from({ length: 73 }, (_, i) => {
      const angle = Math.PI * i / 36
      return [a * Math.cos(angle) * Math.cos(longitude), b * Math.cos(angle) * Math.sin(longitude), c * Math.sin(angle)]
    })
  )
  return [...rings, ...meridians].map(poly)
})
</script>

<template>
  <figure class="study-lab" aria-label="Các bán trục và hai cách tham số hóa ellipsoid">
    <figcaption class="lab-title">B kéo giãn quả cầu, A đưa nó trở về quả cầu</figcaption>
    <p class="lab-lead">Kéo hai điểm trên đường elip để đổi bán trục. Đường tròn đứt có bán kính 1. Với B đường chéo, mỗi tọa độ được nhân với bán trục tương ứng.</p>
    <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Elip với hai bán trục kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="32" x2="368" y1="200" y2="200" class="lab-axis" />
      <line x1="200" x2="200" y1="32" y2="368" class="lab-axis" />
      <circle cx="200" cy="200" :r="view.sx(1)-view.sx(0)" class="unit-circle" />
      <ellipse cx="200" cy="200" :rx="view.sx(radii[0])-view.sx(0)" :ry="view.sy(0)-view.sy(radii[1])" class="axes-ellipse" />
      <text x="369" y="223">x₁</text>
      <text x="211" y="29">x₂</text>
      <g v-for="(radius, axis) in radii" :key="axis">
        <circle :cx="view.sx(axis === 0 ? radius : 0)" :cy="view.sy(axis === 1 ? radius : 0)" r="7" class="lab-dot-warn" />
        <circle :cx="view.sx(axis === 0 ? radius : 0)" :cy="view.sy(axis === 1 ? radius : 0)" r="31" class="lab-handle axes-hit"
          tabindex="0" role="slider" :aria-label="'Bán trục ' + (axis+1)" aria-valuemin="0.6" aria-valuemax="2.5"
          :aria-valuenow="radius" :aria-valuetext="'Bán trục ' + fmt(radius,3)"
          :aria-orientation="axis === 0 ? 'horizontal' : 'vertical'"
          @pointerdown="drag.start(String(axis), $event)"
          @keydown="drag.key(String(axis), axis === 0 ? [radius,0] : [0,radius], $event)" />
      </g>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bán trục bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" @click="radii=[1,1]">Quả cầu đơn vị</button>
      <button type="button" @click="radii=[2,1]">Kéo trục ngang gấp đôi</button>
      <button type="button" :aria-pressed="space" @click="space=!space">Mở sang R³</button>
    </div>
    <template v-if="space">
      <svg viewBox="0 0 400 370" role="img" aria-label="Lưới thưa trên ellipsoid ba chiều">
        <polyline v-for="(line,i) in mesh" :key="i" :points="line" class="axes-mesh" />
      </svg>
      <div class="lab-buttons">
        <button v-for="radius in [0.6,1,2]" :key="radius" type="button" :aria-pressed="third === radius" @click="third=radius">Bán trục 3 = {{ radius }}</button>
      </div>
    </template>
    <div class="lab-readout" role="status">
      <p>B có các phần tử đường chéo {{ fmt(radii[0],3) }}, {{ fmt(radii[1],3) }}{{ space ? ', ' + fmt(third,3) : '' }}. A = B⁻¹ có các phần tử nghịch đảo.</p>
      <p>P = B² có các phần tử đường chéo là bình phương bán trục. Định thức B = {{ fmt(determinant,3) }}, cũng là tỉ số thể tích so với quả cầu đơn vị cùng số chiều.</p>
    </div>
  </figure>
</template>

<style scoped>
.unit-circle { fill: none; stroke: var(--ink-3); stroke-width: 1.4; stroke-dasharray: 5 4; }
.axes-ellipse { fill: none; stroke: var(--tim); stroke-width: 1.8; }
.axes-mesh { fill: none; stroke: var(--tim); stroke-width: 1.3; }
.axes-hit { fill: transparent !important; stroke: transparent; }
.axes-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
