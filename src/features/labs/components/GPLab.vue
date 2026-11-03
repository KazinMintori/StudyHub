<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmtPoint, makeView } from '../controllers/svg-drag.js'

const examples = {
  sqrt: { label: '√x₁ + √x₂ ≤ 2', limits: [.04, 4.4], point: [.64, .64],
    endpoints: [[.16, 2.56], [2.56, .16]],
    boundary: x => Math.max(0, 2 - Math.sqrt(x)) ** 2,
    inside: ([x, y]) => Math.sqrt(x) + Math.sqrt(y) <= 2 + 1e-9 },
  mono: { label: 'x₁x₂ = 1', limits: [.2, 5], point: [1, 1],
    endpoints: [[.5, 2], [2, .5]], boundary: x => 1 / x,
    inside: ([x, y]) => Math.abs(x * y - 1) < 1e-9 },
  poster: { label: 'Áp phích có lề', limits: [6, 70], point: [20, 30],
    boundary: x => 600 / x, inside: ([x, y]) => x * y >= 600 - 1e-9 },
}
const mode = ref('sqrt')
const example = computed(() => examples[mode.value])
const point = ref([...examples.sqrt.point])
const originalSvg = ref(null)
const logSvg = ref(null)
const logPoint = computed(() => point.value.map(Math.log))
const make = ([low, high]) => makeView({ x0:low, x1:high, y0:low, y1:high, width:360, height:320, pad:34 })
const originalView = computed(() => make(example.value.limits))
const logView = computed(() => make(example.value.limits.map(Math.log)))
const originalDrag = createDragger(originalSvg, originalView, (_, next) => { point.value = next }, {step:.05})
const logDrag = createDragger(logSvg, logView, (_, next) => { point.value = next.map(Math.exp) }, {step:.05})
function choose(key) {
  mode.value = key
  point.value = [...examples[key].point]
}
const original = { svg: originalSvg, view: originalView, point, drag: originalDrag, transform: p => p }
const logarithmic = { svg: logSvg, view: logView, point: logPoint, drag: logDrag, transform: p => p.map(Math.log) }
const samples = (low, high, fn) => Array.from({length:161}, (_, i) => {
  const x = low + (high-low)*i/160
  return [x, fn(x)]
})
const edge = computed(() => {
  const [low, high] = example.value.limits
  if (mode.value === 'sqrt') return samples(low, (2-Math.sqrt(low))**2, example.value.boundary)
  return samples(mode.value === 'poster' ? 600/high : low, high, example.value.boundary)
})
const region = computed(() => {
  const [low, high] = example.value.limits
  if (mode.value === 'sqrt') return [...edge.value, [low,low]]
  if (mode.value === 'poster') return [...edge.value, [high,high]]
  return []
})
const costEdge = computed(() => mode.value === 'poster' ? samples(864/76-4, 68, x=>864/(x+4)-6) : [])
const paths = computed(() => {
  if (!example.value.endpoints) return [[], []]
  const [p,q] = example.value.endpoints
  const interpolate = (fn) => Array.from({length:81},(_,i)=>p.map((value,j)=>fn(value,q[j],i/80)))
  return [
    interpolate((a,b,t)=>(1-t)*a+t*b),
    interpolate((a,b,t)=>a**(1-t)*b**t),
  ]
})
const points = (values, panel) => values.map(p=>panel.view.value.point(panel.transform(p)).join(',')).join(' ')
const feasible = computed(() => example.value.inside(point.value))
const panels = computed(() => [original, logarithmic].map(panel => ({
  source: panel,
  coordinate: panel.point.value,
  marker: panel.view.value.point(panel.point.value),
  region: points(region.value, panel),
  edge: points(edge.value, panel),
  cost: points(costEdge.value, panel),
  additive: points(paths.value[0], panel),
  geometric: points(paths.value[1], panel),
})))
function bind(panel, element) { panel.source.svg.value = element }
</script>

<template>
 <figure class="study-lab" aria-label="Miền khả thi trong biến gốc và biến logarit">
  <figcaption class="lab-title">Kéo cùng một điểm qua hai hệ tọa độ</figcaption>
  <p class="lab-lead">Kéo chấm tím trong một trong hai hình. Hình kia cập nhật qua logarit hoặc hàm mũ. Hai khung cùng hiển thị một cửa sổ tọa độ dương.</p>
  <div class="lab-pair">
   <svg v-for="(panel,i) in panels" :key="i" :ref="element=>bind(panel,element)" viewBox="0 0 360 320" role="group" :aria-label="i===0?'Tọa độ gốc':'Tọa độ logarit'" @pointermove="panel.source.drag.move" @pointerup="panel.source.drag.end" @pointercancel="panel.source.drag.end" @lostpointercapture="panel.source.drag.end">
    <text x="34" y="25">{{i===0?'Biến gốc x':'Biến y = log x'}}</text>
    <rect x="34" y="34" width="292" height="252" class="frame"/>
    <polygon :points="panel.region" class="lab-region"/>
    <polyline :points="panel.edge" class="boundary"/>
    <polyline :points="panel.cost" class="cost"/>
    <polyline :points="panel.additive" class="additive"/>
    <polyline :points="panel.geometric" class="geometric"/>
    <text x="325" y="309" text-anchor="end">{{i===0?'x₁':'y₁'}}</text>
    <text x="16" y="55">{{i===0?'x₂':'y₂'}}</text>
    <circle :cx="panel.marker[0]" :cy="panel.marker[1]" r="6" class="lab-dot-accent"/>
    <circle :cx="panel.marker[0]" :cy="panel.marker[1]" r="28" class="lab-handle hit" tabindex="0" role="slider" :aria-label="i===0?'Điểm thử trong biến gốc':'Điểm thử trong biến logarit'" :aria-valuetext="fmtPoint(panel.coordinate,4)" @pointerdown="panel.source.drag.start('point',$event)" @keydown="panel.source.drag.key('point',panel.coordinate,$event)"/>
   </svg>
  </div>
  <div class="lab-buttons">
   <button v-for="(item,key) in examples" :key="key" type="button" :aria-pressed="mode===key" @click="choose(key)">{{item.label}}</button>
  </div>
  <div v-if="example.endpoints" class="lab-buttons">
   <button type="button" @click="point=example.endpoints[0].map((v,i)=>(v+example.endpoints[1][i])/2)">Thử trung điểm cộng</button>
   <button type="button" @click="point=example.endpoints[0].map((v,i)=>Math.sqrt(v*example.endpoints[1][i]))">Thử trung bình nhân</button>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút</summary><LabPointControls :svg="originalSvg"/><LabPointControls :svg="logSvg"/></details>
  <p class="lab-legend"><span class="legend-accent">Miền khả thi hoặc đường đẳng thức</span><span v-if="example.endpoints" class="legend-bad">Đoạn thẳng trong biến gốc</span><span v-if="example.endpoints" class="legend-good">Đoạn thẳng trong biến log</span><span v-if="mode==='poster'" class="legend-warn">Biên diện tích giấy 864 cm²</span></p>
  <div class="lab-readout" role="status">
   <p>x = {{fmtPoint(point,4)}}, log x = {{fmtPoint(logPoint,4)}}. {{feasible?'Điểm thỏa ràng buộc.':'Điểm vi phạm ràng buộc.'}}</p>
   <p v-if="example.endpoints">Hai đường nối cùng hai điểm khả thi. Trung điểm của đường xanh trong biến log cho trung bình nhân theo từng tọa độ.</p>
   <p v-else>Miền tím giữ diện tích chữ ít nhất 600 cm². Biên vàng có diện tích giấy 864 cm² và tiếp xúc miền tại (20, 30).</p>
  </div>
 </figure>
</template>

<style scoped>
svg text{font-size:18px;pointer-events:none}
.frame{fill:none;stroke:var(--ink-3);stroke-width:1}
.boundary,.cost,.additive,.geometric{fill:none;stroke-width:1.65}
.boundary{stroke:var(--tim)}
.cost{stroke:var(--vang)}
.additive{stroke:var(--do);stroke-dasharray:5 4}
.geometric{stroke:var(--xanh)}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
