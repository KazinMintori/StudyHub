<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const logSvg = ref(null), densitySvg = ref(null)
const threshold = ref(2), tilt = ref(0.8)
const logView = ref(makeView({ x0: -0.25, x1: 4.3, y0: -5.1, y1: 13, width: 400, height: 290, pad: 36 }))
const densityView = ref(makeView({ x0: -4.5, x1: 7.5, y0: -0.04, y1: 0.46, width: 400, height: 245, pad: 36 }))
const logBound = lambda => lambda ** 2 / 2 - lambda * threshold.value
const bestTilt = computed(() => Math.max(0, threshold.value))
const trialBound = computed(() => Math.min(1, Math.exp(logBound(tilt.value))))
const bestBound = computed(() => Math.exp(logBound(bestTilt.value)))
const density = (x, mean) => Math.exp(-((x - mean) ** 2) / 2) / Math.sqrt(2 * Math.PI)
const trace = (view, f, from, to) => Array.from({ length: 141 }, (_, i) => {
  const x = from + (to - from) * i / 140
  return view.point([x, f(x)]).join(',')
}).join(' ')
const logCurve = computed(() => trace(logView.value, logBound, 0, 4))
const original = trace(densityView.value, x => density(x, 0), -4, 7)
const shifted = computed(() => trace(densityView.value, x => density(x, tilt.value), -4, 7))
const dragTilt = createDragger(logSvg, logView, (_, [x]) => {
  tilt.value = Math.max(0, Math.min(4, x))
}, { snap: 0.01, step: 0.05 })
const dragThreshold = createDragger(densitySvg, densityView, (_, [x]) => {
  threshold.value = Math.max(-1, Math.min(3, x))
}, { snap: 0.01, step: 0.05 })
</script>

<template>
  <figure class="study-lab" aria-label="Tối ưu tham số của cận Chernoff chuẩn">
    <figcaption class="lab-title">Tìm điểm thấp nhất của log-cận Chernoff</figcaption>
    <p class="lab-lead">Kéo chấm vàng trên parabol để đổi λ. Kéo chấm ở trục hoành của hình dưới để đổi ngưỡng đuôi t. Chấm xanh là giá trị λ tối ưu trên miền không âm.</p>
    <svg ref="logSvg" viewBox="0 0 400 290" role="group" aria-label="Parabol log-cận với tham số lambda kéo được"
      @pointermove="dragTilt.move" @pointerup="dragTilt.end" @pointercancel="dragTilt.end" @lostpointercapture="dragTilt.end">
      <line x1="34" x2="366" :y1="logView.sy(0)" :y2="logView.sy(0)" class="lab-axis" />
      <line :x1="logView.sx(0)" :x2="logView.sx(0)" y1="35" y2="253" class="lab-axis" />
      <text x="13" y="27">Log-cận</text>
      <text x="375" y="270">λ</text>
      <text v-for="x in [0, 2, 4]" :key="x" :x="logView.sx(x)" y="270" text-anchor="middle">{{ x }}</text>
      <polyline :points="logCurve" class="lab-accent" />
      <circle :cx="logView.sx(bestTilt)" :cy="logView.sy(logBound(bestTilt))" r="6" class="lab-dot-good" />
      <circle :cx="logView.sx(tilt)" :cy="logView.sy(logBound(tilt))" r="7" class="lab-dot-warn" />
      <circle :cx="logView.sx(tilt)" :cy="logView.sy(logBound(tilt))" r="31" class="lab-handle chernoff-hit"
        tabindex="0" role="slider" aria-label="Tham số lambda" aria-valuemin="0" aria-valuemax="4"
        :aria-valuenow="tilt" :aria-valuetext="'λ = ' + fmt(tilt)"
        @pointerdown="dragTilt.start('tilt', $event)" @keydown="dragTilt.key('tilt', [tilt,logBound(tilt)], $event)" />
    </svg>
    <svg ref="densitySvg" viewBox="0 0 400 245" role="group" aria-label="Hai mật độ chuẩn và ngưỡng đuôi kéo được"
      @pointermove="dragThreshold.move" @pointerup="dragThreshold.end" @pointercancel="dragThreshold.end" @lostpointercapture="dragThreshold.end">
      <line x1="36" x2="364" :y1="densityView.sy(0)" :y2="densityView.sy(0)" class="lab-axis" />
      <line :x1="densityView.sx(threshold)" :x2="densityView.sx(threshold)" y1="38" :y2="densityView.sy(0)" class="lab-guide" />
      <text x="13" y="27">Mật độ</text>
      <text x="371" y="231">x</text>
      <text v-for="x in [-4, 0, 4, 7]" :key="x" :x="densityView.sx(x)" y="231" text-anchor="middle">{{ x }}</text>
      <polyline :points="original" class="lab-accent" />
      <polyline :points="shifted" class="lab-good density-tilt" />
      <circle :cx="densityView.sx(threshold)" :cy="densityView.sy(0)" r="7" class="lab-dot-warn" />
      <circle :cx="densityView.sx(threshold)" :cy="densityView.sy(0)" r="31" class="lab-handle chernoff-hit"
        tabindex="0" role="slider" aria-label="Ngưỡng đuôi phải" aria-valuemin="-1" aria-valuemax="3"
        :aria-valuenow="threshold" :aria-valuetext="'t = ' + fmt(threshold)"
        @pointerdown="dragThreshold.start('threshold', $event)" @keydown="dragThreshold.key('threshold', [threshold,0], $event)" />
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh các điểm bằng nút</summary>
      <LabPointControls :svg="logSvg" axes="x" />
      <LabPointControls :svg="densitySvg" axes="x" />
    </details>
    <div class="lab-buttons">
      <button type="button" @click="tilt = bestTilt">Đưa λ về tối ưu</button>
      <button type="button" @click="threshold = 2; tilt = 0.8">Thử t = 2</button>
      <button type="button" @click="threshold = -1; tilt = 0">Thử t = −1</button>
    </div>
    <div class="lab-readout" role="status">
      <p>t = {{ fmt(threshold) }}, λ = {{ fmt(tilt) }}. Cận thử sau khi chặn ở 1 là {{ fmt(trialBound, 4) }}. Cận tối ưu trong họ này là {{ fmt(bestBound, 4) }} tại λ = {{ fmt(bestTilt) }}.</p>
      <p>Đường tím dưới là mật độ chuẩn ban đầu. Nét xanh đứt là mật độ sau khi nghiêng theo hàm mũ, có kỳ vọng λ và phương sai vẫn bằng 1.</p>
    </div>
  </figure>
</template>

<style scoped>
.chernoff-hit { fill: transparent !important; stroke: transparent; }
.chernoff-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
svg .density-tilt { stroke-width: 1.7; stroke-dasharray: 5 4; }
figure > svg + svg { margin-top: var(--space-3); }
</style>
