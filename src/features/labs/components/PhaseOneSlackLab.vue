<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, makeView } from '../controllers/svg-drag.js'
import { clipPolyline } from '../services/svg-clipping.mjs'

const svg = ref(null)
const threshold = ref(-2)
const exponential = ref(false)
const trial = ref(0.75)
const minimumX = computed(() => exponential.value ? -1 : -2)
const bounds = { x0: -3.3, x1: 4.5, y0: -2, y1: 4.6 }
const view = ref(makeView({ ...bounds, width: 400, height: 330, pad: 36 }))
const slack = x => exponential.value ? Math.exp(-x) : Math.max(x, threshold.value - x)
const coordinates = points => points.map(p => view.value.point(p).join(',')).join(' ')
const curve = computed(() => {
  const samples = Array.from({ length: 157 }, (_, i) => {
    const x = bounds.x0 + i * (bounds.x1 - bounds.x0) / 156
    return [x, slack(x)]
  })
  return clipPolyline(samples, bounds).map(coordinates)
})
const drag = createDragger(svg, view, (_, [x]) => {
  trial.value = Math.max(minimumX.value, Math.min(4, x))
}, { step: 0.1, snap: 0.05 })
const optimal = computed(() => threshold.value / 2)

function choose(value) {
  threshold.value = value
  exponential.value = false
}
</script>

<template>
  <figure class="study-lab" aria-label="Giá trị biến bù Pha I và tính khả thi">
    <figcaption class="lab-title">Dấu của giá trị Pha I nói điều gì?</figcaption>
    <p class="lab-lead">Với hai điều kiện x ≤ 0 và x ≥ a, biến bù nhỏ nhất tại x là max(x, a − x). Kéo chấm vàng trên đồ thị để thử một x cụ thể, rồi đổi a để so sánh ba trường hợp.</p>
    <svg ref="svg" viewBox="0 0 400 330" role="group" aria-label="Đồ thị mức nới lỏng và điểm thử kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="36" x2="364" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="36" y2="294" class="lab-axis" />
      <text x="13" y="28">Biến bù s</text><text x="371" y="313">x</text>
      <text v-for="x in [-2,0,2,4]" :key="x" :x="view.sx(x)" y="313" text-anchor="middle">{{x}}</text>
      <polyline v-for="(path,i) in curve" :key="i" :points="path" class="phase-curve" />
      <circle :cx="view.sx(trial)" :cy="view.sy(slack(trial))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(trial)" :cy="view.sy(slack(trial))" r="32" class="lab-handle phase-hit" tabindex="0"
        role="slider" aria-label="Hoành độ thử cho Pha I" :aria-valuemin="minimumX" aria-valuemax="4"
        :aria-valuenow="trial" :aria-valuetext="'x = ' + fmt(trial)"
        @pointerdown="drag.start('trial',$event)" @keydown="drag.key('trial',[trial,slack(trial)],$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm thử bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" @click="choose(-2)">a = −2</button>
      <button type="button" @click="choose(0)">a = 0</button>
      <button type="button" @click="choose(2)">a = 2</button>
      <button v-if="!exponential" type="button" @click="trial=optimal">Đưa x về cực tiểu</button>
      <button type="button" @click="exponential=true; trial=1">Ví dụ không đạt infimum</button>
    </div>
    <div class="lab-readout" role="status">
      <p>x = {{fmt(trial)}}. Biến bù nhỏ nhất tại điểm thử {{fmt(slack(trial),4)}}.</p>
      <p v-if="exponential">Ví dụ này chỉ có điều kiện e⁻ˣ ≤ 0. Pha I có infimum bằng 0, nhưng mọi x hữu hạn đều cho biến bù dương. Bài toán gốc vô nghiệm.</p>
      <p v-else-if="threshold<0">Giá trị tối ưu {{fmt(optimal)}} đạt tại x = {{fmt(optimal)}}. Có điểm khả thi ngặt cho cả hai bất đẳng thức.</p>
      <p v-else-if="threshold===0">Giá trị tối ưu 0 đạt tại x = 0. Bài toán gốc có một điểm khả thi và mọi điểm đều không thể thỏa hai bất đẳng thức ngặt.</p>
      <p v-else>Giá trị tối ưu {{fmt(optimal)}} dương. Không có x nào thỏa đồng thời x ≤ 0 và x ≥ {{threshold}}.</p>
    </div>
  </figure>
</template>

<style scoped>
.phase-curve { fill: none; stroke: var(--tim); stroke-width: 1.8; }
.phase-hit { fill: transparent !important; stroke: transparent; }
.phase-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
