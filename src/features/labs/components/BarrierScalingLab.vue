<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, makeView } from '../controllers/svg-drag.js'
import { project3 } from '../services/foundation-geometry.mjs'

const svg = ref(null)
const scale = ref(1)
const matrixSize = ref(2)
const matrixMode = ref(false)
const view = ref(makeView({ x0: 0, x1: 2.5, y0: -1, y1: 1, width: 400, height: 144, pad: 40 }))
const drag = createDragger(svg, view, (_, [x]) => {
  scale.value = Math.max(0.25, Math.min(2, x))
}, { step: 0.05, snap: 0.025 })
const parameter = computed(() => matrixMode.value ? matrixSize.value : 2)
const base = computed(() => matrixMode.value ? -Math.log(matrixSize.value === 2 ? 2 : 6) : -Math.log(0.64))
const change = computed(() => -parameter.value * Math.log(scale.value))
const barrier = computed(() => base.value + change.value)
const camera = { yaw: 30, pitch: 28, scale: 62, origin: [200, 260] }
const project = p => project3(p, camera)
const coordinates = points => points.map(p => project(p).join(',')).join(' ')
const rings = [0.5, 1, 1.5, 2].map(height => coordinates(
  Array.from({ length: 73 }, (_, i) => {
    const angle = i * Math.PI / 36
    return [height * Math.cos(angle), height * Math.sin(angle), height]
  })
))
const rays = [0, Math.PI/2, Math.PI, 3*Math.PI/2].map(angle =>
  coordinates([[0,0,0],[2*Math.cos(angle),2*Math.sin(angle),2]])
)
const point = computed(() => project([0.6*scale.value,0,scale.value]))
</script>

<template>
  <figure class="study-lab" aria-label="Tính đồng bậc logarit của hàm chắn nón">
    <figcaption class="lab-title">Phóng theo một tia làm hàm chắn đổi bao nhiêu?</figcaption>
    <p class="lab-lead">Kéo chấm vàng trên trục hệ số s. Trong nón Lorentz, điểm gốc u = (0,6; 0; 1) được phóng thành su và luôn ở trong nón. Dùng chế độ ma trận để so sánh hệ số của −log det.</p>
    <svg v-if="!matrixMode" viewBox="0 0 400 340" role="img" aria-label="Nón Lorentz ba chiều và điểm được phóng dọc theo tia">
      <polyline v-for="(line,i) in rings" :key="'ring'+i" :points="line" class="scaling-mesh" />
      <polyline v-for="(line,i) in rays" :key="'ray'+i" :points="line" class="scaling-mesh" />
      <line :x1="project([0,0,0])[0]" :y1="project([0,0,0])[1]"
        :x2="project([1.2,0,2])[0]" :y2="project([1.2,0,2])[1]" class="scaling-ray" />
      <circle :cx="point[0]" :cy="point[1]" r="7" class="lab-dot-warn" />
    </svg>
    <div v-else class="scaling-matrix" aria-label="Các phần tử đường chéo của ma trận">
      <p v-for="i in matrixSize" :key="i">Trị riêng thứ {{i}} bằng {{fmt(i*scale,3)}}.</p>
      <p>Ma trận đường chéo có {{matrixSize}} trị riêng dương. Định thức bằng tích các trị riêng.</p>
    </div>
    <svg ref="svg" viewBox="0 0 400 144" role="group" aria-label="Hệ số phóng s kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <text x="13" y="28">Hệ số phóng s</text>
      <line :x1="view.sx(0.25)" :x2="view.sx(2)" y1="72" y2="72" class="lab-axis" />
      <text v-for="s in [0.25,1,2]" :key="s" :x="view.sx(s)" y="119" text-anchor="middle">{{s}}</text>
      <circle :cx="view.sx(scale)" cy="72" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(scale)" cy="72" r="32" class="lab-handle scaling-hit"
        tabindex="0" role="slider" aria-label="Hệ số phóng trong nón" aria-valuemin="0.25" aria-valuemax="2"
        :aria-valuenow="scale" :aria-valuetext="'s = '+fmt(scale,3)"
        @pointerdown="drag.start('scale',$event)" @keydown="drag.key('scale',[scale,0],$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh hệ số bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" @click="matrixMode=false">Nón Lorentz R³</button>
      <button type="button" @click="matrixMode=true; matrixSize=2">Ma trận cỡ 2</button>
      <button type="button" @click="matrixMode=true; matrixSize=3">Ma trận cỡ 3</button>
      <button type="button" @click="scale=0.5">Co một nửa</button>
      <button type="button" @click="scale=2">Phóng gấp đôi</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Tham số ν = {{parameter}}. Hệ số s = {{fmt(scale,3)}}. Giá trị hàm chắn {{fmt(barrier,4)}}.</p>
      <p>Độ thay đổi so với s = 1 là −ν log s = {{fmt(change,4)}}. Co về phía đỉnh nón làm hàm chắn tăng.</p>
    </div>
  </figure>
</template>

<style scoped>
.scaling-mesh { fill: none; stroke: var(--ink-3); stroke-width: 1.1; opacity: 0.65; }
.scaling-ray { stroke: var(--tim); stroke-width: 1.7; }
.scaling-hit { fill: transparent !important; stroke: transparent; }
.scaling-hit:focus-visible { stroke: var(--vang); }
.scaling-matrix { margin-block: var(--space-4); }
svg text { font-size: 19px; pointer-events: none; }
</style>
