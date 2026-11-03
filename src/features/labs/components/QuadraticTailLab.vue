<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { project3 } from '../services/foundation-geometry.mjs'

const svg = ref(null)
const sample = ref([0.5, 0.25])
const showSurface = ref(false)
const view = ref(makeView({ x0: -2.6, x1: 2.6, y0: -2, y1: 2, width: 400, height: 320, pad: 32 }))
const value = ([x,y]) => x*x/4 + y*y
const level = computed(() => value(sample.value))
const drag = createDragger(svg, view, (_, p) => { sample.value = p }, { step: 0.1, snap: 0.05 })
const camera = { yaw: 25, pitch: 26, scale: 48, origin: [200, 199] }
const project = p => project3(p, camera)
const rim = (radius, height) => Array.from({ length: 73 }, (_, i) => {
  const angle = i * Math.PI / 36
  return project([2 * radius * Math.cos(angle), radius * Math.sin(angle), height])
})
const stringify = points => points.map(p => p.join(',')).join(' ')
const slices = [0.25, 0.5, 0.75, 1.25].map(radius => stringify(rim(radius, radius ** 2)))
const generators = Array.from({ length: 8 }, (_, i) => {
  const angle = i * Math.PI / 4
  return stringify(Array.from({ length: 31 }, (_, j) => {
    const r = j / 24
    return project([2*r*Math.cos(angle), r*Math.sin(angle), r*r])
  }))
})
const liftedPoint = computed(() => project([...sample.value, level.value]))
</script>

<template>
  <figure class="study-lab" aria-label="Ellipsoid an toàn và hàm chặn toàn phương">
    <figcaption class="lab-title">Đường mức 1 chia miền an toàn và miền nguy hiểm</figcaption>
    <p class="lab-lead">Kéo điểm vàng qua biên. Ta dùng f(x, y) = x²/4 + y² để chặn hàm chỉ thị của biến cố ở ngoài hoặc trên biên elip.</p>
    <svg ref="svg" viewBox="0 0 400 320" role="group" aria-label="Elip an toàn và điểm thử kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <ellipse :cx="view.sx(0)" :cy="view.sy(0)" :rx="view.sx(2)-view.sx(0)" :ry="view.sy(0)-view.sy(1)" class="tail-ellipse" />
      <line x1="32" x2="368" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="32" y2="288" class="lab-axis" />
      <text x="370" y="153">x</text>
      <text x="211" y="29">y</text>
      <circle :cx="view.sx(sample[0])" :cy="view.sy(sample[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(sample[0])" :cy="view.sy(sample[1])" r="31" class="lab-handle tail-hit"
        tabindex="0" role="slider" aria-label="Điểm thử trong mặt phẳng" :aria-valuetext="fmtPoint(sample)"
        @pointerdown="drag.start('sample', $event)" @keydown="drag.key('sample', sample, $event)" />
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh điểm thử bằng nút</summary>
      <LabPointControls :svg="svg" />
    </details>
    <div class="lab-buttons">
      <button type="button" @click="sample = [0,0]">Tâm elip</button>
      <button type="button" @click="sample = [2,0]">Biên elip</button>
      <button type="button" @click="sample = [2.2,0]">Ngoài elip</button>
      <button type="button" :aria-pressed="showSurface" @click="showSurface = !showSurface">Xem mặt chặn trong R³</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Điểm {{ fmtPoint(sample) }} có f = {{ fmt(level, 3) }}. Hàm chỉ thị bằng {{ level >= 1 ? 1 : 0 }}.</p>
      <p>Với elip này, g = f − 1. Trong bổ đề S ta có thể chọn λ = 1, vì f − 1 − λg bằng 0 khắp nơi.</p>
    </div>
    <template v-if="showSurface">
      <svg viewBox="0 0 400 295" role="img" aria-label="Mặt parabol, đường mức một và điểm được nâng lên">
        <polyline v-for="(line, i) in generators" :key="'ray'+i" :points="line" class="tail-mesh" />
        <polyline v-for="(line, i) in slices" :key="'slice'+i" :points="line" class="tail-mesh" />
        <polyline :points="stringify(rim(1, 1))" class="tail-level" />
        <circle v-if="level <= 1.5625" :cx="liftedPoint[0]" :cy="liftedPoint[1]" r="6" class="lab-dot-warn" />
      </svg>
      <p>Đường xanh trên mặt có độ cao 1. Hình vẽ mặt đến độ cao 1,5625. {{ level > 1.5625 ? 'Điểm đang chọn nằm cao hơn phần được vẽ.' : 'Chấm vàng là điểm đang chọn, nâng lên độ cao f.' }}</p>
    </template>
  </figure>
</template>

<style scoped>
.tail-ellipse { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.5; }
.tail-mesh, .tail-level { fill: none; stroke-width: 1.3; }
.tail-mesh { stroke: var(--tim); opacity: 0.65; }
.tail-level { stroke: var(--xanh); stroke-width: 2; }
.tail-hit { fill: transparent !important; stroke: transparent; }
.tail-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
