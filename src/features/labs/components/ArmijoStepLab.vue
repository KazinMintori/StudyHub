<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, makeView } from '../controllers/svg-drag.js'

const svg = ref(null)
const step = ref(1)
const directionScale = ref(4)
const alpha = 0.2
const view = ref(makeView({ x0: -0.08, x1: 1.12, y0: -1.05, y1: 4.45, width: 400, height: 350, pad: 36 }))
const lossChange = t => directionScale.value * t * (directionScale.value * t / 2 - 1)
const armijoLine = t => -alpha * directionScale.value * t
const accepted = computed(() => lossChange(step.value) <= armijoLine(step.value) + 1e-10)
const limit = computed(() => Math.min(1, 2 * (1 - alpha) / directionScale.value))
const points = rows => rows.map(p => view.value.point(p).join(',')).join(' ')
const curve = computed(() => points(Array.from({ length: 101 }, (_, i) => [i / 100, lossChange(i / 100)])))
const drag = createDragger(svg, view, (_, [t]) => {
  step.value = Math.max(0.01, Math.min(1, t))
}, { step: 0.05, snap: 0.01 })

function setDirectionScale(value) {
  directionScale.value = value
  step.value = 1
}
</script>

<template>
  <figure class="study-lab" aria-label="Bước thử và điều kiện giảm đủ Armijo">
    <figcaption class="lab-title">Bước thử có giảm đủ hay không?</figcaption>
    <p class="lab-lead">Bắt đầu ở x = 1 với f(x) = x²/2 và hướng d = −k. Kéo điểm vàng để đổi bước t. Đường tím là độ thay đổi mục tiêu, còn đường xanh là mức Armijo cho phép.</p>
    <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Độ giảm mục tiêu, đường Armijo và bước thử kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="36" x2="364" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="36" y2="314" class="lab-axis" />
      <text x="13" y="27">Độ thay đổi</text><text x="374" y="332">t</text>
      <text v-for="t in [0,0.5,1]" :key="t" :x="view.sx(t)" y="332" text-anchor="middle">{{t}}</text>
      <polyline :points="curve" class="armijo-curve" />
      <polyline :points="points([[0,0],[1,armijoLine(1)]])" class="armijo-limit" />
      <line :x1="view.sx(step)" :x2="view.sx(step)" :y1="view.sy(lossChange(step))" :y2="view.sy(armijoLine(step))" class="lab-guide" />
      <circle :cx="view.sx(step)" :cy="view.sy(lossChange(step))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(step)" :cy="view.sy(lossChange(step))" r="31" class="lab-handle armijo-hit"
        tabindex="0" role="slider" aria-label="Độ dài bước thử" aria-valuemin="0.01" aria-valuemax="1"
        :aria-valuenow="step" :aria-valuetext="'t = '+fmt(step,4)"
        @pointerdown="drag.start('step',$event)" @keydown="drag.key('step',[step,lossChange(step)],$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bước bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" @click="setDirectionScale(1)">Hướng d = −1</button>
      <button type="button" @click="setDirectionScale(4)">Hướng d = −4</button>
      <button type="button" @click="step=1">Thử lại t = 1</button>
      <button type="button" :disabled="accepted" @click="step/=2">Giảm bước còn một nửa</button>
    </div>
    <div class="lab-readout" role="status">
      <p>t = {{fmt(step,4)}}. Độ thay đổi thực {{fmt(lossChange(step),4)}}. Mức Armijo {{fmt(armijoLine(step),4)}}.</p>
      <p>{{accepted ? 'Chấp nhận bước này.' : 'Bước chưa giảm đủ. Hãy thử co bước.'}} Trong khung, các bước dương đến {{fmt(limit,4)}} đều được chấp nhận.</p>
    </div>
  </figure>
</template>

<style scoped>
.armijo-curve, .armijo-limit { fill: none; stroke-width: 1.8; }
.armijo-curve { stroke: var(--tim); }
.armijo-limit { stroke: var(--xanh); stroke-dasharray: 5 4; }
.armijo-hit { fill: transparent !important; stroke: transparent; }
.armijo-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
