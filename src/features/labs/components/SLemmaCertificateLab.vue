<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt, fmtPoint } from '../controllers/svg-drag.js'

const svg = ref(null)
const sample = ref([0.65, 0.45])
const certificate = ref(2)
const view = ref(makeView({ x0: -1.9, x1: 1.9, y0: -1.9, y1: 1.9, width: 400, height: 400, pad: 39 }))
const drag = createDragger(svg, view, (_, p) => { sample.value = p }, { step: 0.05, snap: 0.025 })
const f1 = computed(() => sample.value[0]**2 + sample.value[1]**2 - 1)
const f0 = computed(() => 2*sample.value[0]**2 + sample.value[1]**2 - 2)
const slack = computed(() => certificate.value*f1.value - f0.value)
const valid = computed(() => certificate.value === 2)
</script>

<template>
  <figure class="study-lab" aria-label="Chứng chỉ bổ đề S cho đĩa và elip">
    <figcaption class="lab-title">Một hệ số chứng nhận cả miền</figcaption>
    <p class="lab-lead">Đĩa tím là F₁ ≤ 0. Elip xanh là F₀ ≤ 0. Kéo điểm vàng qua hai đường biên, rồi đổi λ để kiểm điều kiện mạnh hơn là λF₁ − F₀ không âm ở mọi điểm.</p>
    <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Đĩa nằm trong elip và điểm thử kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="39" x2="361" y1="200" y2="200" class="lab-axis" />
      <line x1="200" x2="200" y1="39" y2="361" class="lab-axis" />
      <ellipse cx="200" cy="200" :rx="view.sx(1)-200" :ry="200-view.sy(Math.SQRT2)" class="slemma-ellipse" />
      <circle cx="200" cy="200" :r="view.sx(1)-200" class="slemma-disk" />
      <text x="371" y="222">x</text><text x="212" y="30">y</text>
      <circle :cx="view.sx(sample[0])" :cy="view.sy(sample[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(sample[0])" :cy="view.sy(sample[1])" r="32" class="lab-handle slemma-hit"
        tabindex="0" role="slider" aria-label="Điểm thử chứng chỉ bổ đề S" :aria-valuetext="fmtPoint(sample)"
        @pointerdown="drag.start('sample',$event)" @keydown="drag.key('sample',sample,$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm thử bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button v-for="value in [1,2,3]" :key="value" type="button" :aria-pressed="certificate===value" @click="certificate=value">Chọn λ = {{value}}</button>
      <button type="button" @click="sample=certificate<2 ? [1.5,0] : [0,0]">Thử điểm kiểm chứng</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Điểm {{fmtPoint(sample)}}. F₁ = {{fmt(f1,3)}}, F₀ = {{fmt(f0,3)}}. Với λ = {{certificate}}, hiệu λF₁ − F₀ = {{fmt(slack,3)}}.</p>
      <p v-if="valid">Với λ = 2, hiệu bằng y² trên toàn mặt phẳng. Vì vậy, mọi điểm có F₁ ≤ 0 đều có F₀ ≤ 0.</p>
      <p v-else-if="certificate<2">Với λ = 1, điểm (1,5; 0) cho hiệu âm. Hệ số này chưa phải chứng chỉ.</p>
      <p v-else>Với λ = 3, gốc tọa độ cho hiệu âm. Hệ số này chưa phải chứng chỉ.</p>
    </div>
  </figure>
</template>

<style scoped>
.slemma-ellipse { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.7; }
.slemma-disk { fill: var(--tim-soft); stroke: var(--tim); stroke-width: 1.5; }
.slemma-hit { fill: transparent !important; stroke: transparent; }
.slemma-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
