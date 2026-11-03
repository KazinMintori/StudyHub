<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const svg = ref(null)
const mean = ref(0.2)
const view = ref(makeView({ x0: -1, x1: 1, y0: 0, y1: 1, width: 400, height: 290, pad: 56 }))
const middleMass = computed(() => (Math.sqrt(4 - 3 * mean.value ** 2) - 1) / 3)
const mass = computed(() => [
  (1 - middleMass.value - mean.value) / 2,
  middleMass.value,
  (1 - middleMass.value + mean.value) / 2
])
const entropy = computed(() => -mass.value.reduce((sum, p) => sum + (p > 0 ? p * Math.log(p) : 0), 0))
const vertices = [[-1, 0], [0, 1], [1, 0]].map(p => view.value.point(p).join(',')).join(' ')
const drag = createDragger(svg, view, (_, [value]) => { mean.value = value }, { step: 0.05, snap: 0.01 })
</script>

<template>
  <figure class="study-lab" aria-label="Phân phối cực đại entropy trên đơn hình xác suất">
    <figcaption class="lab-title">Thay kỳ vọng, đổi lát cắt của đơn hình</figcaption>
    <p class="lab-lead">Mỗi điểm trong tam giác là một phân phối trên ba giá trị −1, 0 và 1. Kéo điểm vàng sang trái hoặc phải để đổi kỳ vọng. Đoạn xanh gồm mọi phân phối có kỳ vọng đang chọn.</p>
    <svg ref="svg" viewBox="0 0 400 290" role="group" aria-label="Đơn hình xác suất và điểm cực đại entropy kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polygon :points="vertices" class="entropy-triangle" />
      <line :x1="view.sx(mean)" :x2="view.sx(mean)" :y1="view.sy(0)" :y2="view.sy(1 - Math.abs(mean))" class="lab-good" />
      <text x="56" y="266" text-anchor="middle">p₁ = 1</text>
      <text x="200" y="35" text-anchor="middle">p₂ = 1</text>
      <text x="344" y="266" text-anchor="middle">p₃ = 1</text>
      <circle :cx="view.sx(mean)" :cy="view.sy(middleMass)" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(mean)" :cy="view.sy(middleMass)" r="31" class="lab-handle entropy-hit"
        tabindex="0" role="slider" aria-label="Kỳ vọng của X" :aria-valuemin="-1" :aria-valuemax="1"
        :aria-valuenow="mean" :aria-valuetext="'Kỳ vọng ' + fmt(mean)"
        @pointerdown="drag.start('mean', $event)" @keydown="drag.key('mean', [mean, middleMass], $event)" />
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh kỳ vọng bằng nút</summary>
      <LabPointControls :svg="svg" axes="x" />
    </details>
    <div class="lab-buttons">
      <button type="button" @click="mean = -1">Biên trái</button>
      <button type="button" @click="mean = 0">Phân phối đều</button>
      <button type="button" @click="mean = 0.2">Ví dụ kỳ vọng 0,2</button>
      <button type="button" @click="mean = 1">Biên phải</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Kỳ vọng {{ fmt(mean) }}. Phân phối cực đại entropy ({{ mass.map(p => fmt(p, 4)).join(', ') }}).</p>
      <p>Entropy {{ fmt(entropy, 4) }} nat.</p>
      <p v-if="Math.abs(mean) === 1">Ở biên, chỉ một phân phối thỏa điều kiện. Toàn bộ khối lượng dồn vào một giá trị.</p>
      <p v-else>Điểm vàng đạt entropy lớn nhất trên lát này. Cả ba xác suất đều dương.</p>
    </div>
  </figure>
</template>

<style scoped>
.entropy-triangle { fill: var(--tim-soft); stroke: var(--ink-3); stroke-width: 1.3; }
.entropy-hit { fill: transparent !important; stroke: transparent; }
.entropy-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
svg .lab-good { stroke-width: 1.5; }
</style>
