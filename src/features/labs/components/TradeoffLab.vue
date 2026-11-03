<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint, makeView } from '../controllers/svg-drag.js'
import { clipSegment } from '../services/svg-clipping.mjs'
import { nearestPathWeight, regularizationObjectives, regularizationPoint, regularizationWeights } from '../services/regularization-path.mjs'

const mode = ref('ridge')
const weight = ref(.5)
const objectiveSvg = ref(null)
const parameterSvg = ref(null)
const weightSvg = ref(null)
const objectiveView = makeView({ x0: 0, x1: 32, y0: 0, y1: 2.3, width: 360, height: 320, pad: 35 })
const parameterView = makeView({ x0: -.15, x1: 1.2, y0: -.15, y1: 1.2, width: 360, height: 320, pad: 35 })
const rail = makeView({ x0: 0, x1: 1, y0: 0, y1: 1, width: 360, height: 105, pad: 32 })
const current = computed(() => regularizationPoint(mode.value, weight.value))
const path = computed(() => regularizationWeights.map(value => regularizationPoint(mode.value, value)))
const objectivePoint = row => objectiveView.point([row.error, row.size])
const parameterPoint = row => parameterView.point(row.point)
const objectivePath = computed(() => path.value.map(row => objectivePoint(row).join(',')).join(' '))
const parameterPath = computed(() => path.value.map(row => parameterPoint(row).join(',')).join(' '))
const objectiveDragView = computed(() => ({ x0: 0, x1: 1, y0: 0, y1: 1,
  toWorld: (x, y) => [nearestPathWeight([x, y], path.value, objectivePoint), 0] }))
const parameterDragView = computed(() => ({ x0: 0, x1: 1, y0: 0, y1: 1,
  toWorld: (x, y) => [nearestPathWeight([x, y], path.value, parameterPoint), 0] }))
const update = (_, next) => { weight.value = next[0] }
const objectiveDrag = createDragger(objectiveSvg, objectiveDragView, update, { step: .02 })
const parameterDrag = createDragger(parameterSvg, parameterDragView, update, { step: .02 })
const railView = computed(() => rail)
const weightDrag = createDragger(weightSvg, railView, update, { step: .02 })
const cloud = computed(() => {
  const samples = []
  for (let first = 0; first <= 16; first++) for (let second = 0; second <= 16; second++) {
    const row = regularizationObjectives([-.3 + first / 10, -.3 + second / 10], mode.value)
    if (row.error <= 32 && row.size <= 2.3) samples.push(objectiveView.point([row.error, row.size]))
  }
  return samples
})
const support = computed(() => {
  if (weight.value === 1) return [[0, 0], [32, 0]]
  const { error, size, penalty } = current.value
  if (penalty === 0) return [[error, 0], [error, 2.3]]
  const intercept = error + penalty * size
  return clipSegment([[0, intercept / penalty], [32, (intercept - 32) / penalty]], objectiveView)
})
function choose(penalty, nextMode = mode.value) {
  mode.value = nextMode
  weight.value = penalty === Infinity ? 1 : penalty / (1 + penalty)
}
</script>

<template>
 <figure class="study-lab" aria-label="Đường Pareto và nghiệm ridge hoặc lasso kéo được">
  <figcaption class="lab-title">Một trọng số chọn đồng thời cặp mục tiêu và vector nghiệm</figcaption>
  <p class="lab-lead">Kéo chấm vàng trên một trong hai đường, hoặc kéo trọng số s trên thước. Các điểm trên hình mục tiêu và hình tham số cập nhật cùng nhau. Thước dùng tổng (1 − s)F₁ + sF₂, nên hai đầu s = 0 và s = 1 có ý nghĩa riêng.</p>
  <div class="lab-pair">
   <svg ref="objectiveSvg" viewBox="0 0 360 320" role="group" aria-label="Không gian mục tiêu, đường Pareto và điểm kéo" @pointermove="objectiveDrag.move" @pointerup="objectiveDrag.end" @pointercancel="objectiveDrag.end" @lostpointercapture="objectiveDrag.end">
    <text x="35" y="24">Hai mục tiêu (F₁, F₂)</text>
    <line x1="35" x2="325" y1="285" y2="285" class="lab-axis"/><line x1="35" x2="35" y1="35" y2="285" class="lab-axis"/>
    <circle v-for="(point, index) in cloud" :key="index" :cx="point[0]" :cy="point[1]" r="1.3" class="sample"/>
    <polyline :points="objectivePath" class="frontier"/>
    <line v-if="support" :x1="objectiveView.sx(support[0][0])" :y1="objectiveView.sy(support[0][1])" :x2="objectiveView.sx(support[1][0])" :y2="objectiveView.sy(support[1][1])" class="lab-guide"/>
    <text x="330" y="309">F₁</text><text x="8" y="48">F₂</text>
    <circle :cx="objectivePoint(current)[0]" :cy="objectivePoint(current)[1]" r="6" class="lab-dot-warn"/>
    <circle :cx="objectivePoint(current)[0]" :cy="objectivePoint(current)[1]" r="28" class="lab-handle hit" tabindex="0" role="slider" aria-label="Điểm đang chọn trên đường Pareto" :aria-valuetext="fmt(weight,5)" @pointerdown="objectiveDrag.start('s',$event)" @keydown="objectiveDrag.key('s',[weight,0],$event)"/>
   </svg>
   <svg ref="parameterSvg" viewBox="0 0 360 320" role="group" aria-label="Đường nghiệm trong không gian hai tham số và điểm kéo" @pointermove="parameterDrag.move" @pointerup="parameterDrag.end" @pointercancel="parameterDrag.end" @lostpointercapture="parameterDrag.end">
    <text x="35" y="24">Hai tham số (x₁, x₂)</text>
    <line x1="35" x2="325" :y1="parameterView.sy(0)" :y2="parameterView.sy(0)" class="lab-axis"/><line :x1="parameterView.sx(0)" :x2="parameterView.sx(0)" y1="35" y2="285" class="lab-axis"/>
    <polyline :points="parameterPath" class="solution-path"/>
    <text x="330" y="309">x₁</text><text x="8" y="48">x₂</text>
    <circle :cx="parameterPoint(current)[0]" :cy="parameterPoint(current)[1]" r="6" class="lab-dot-warn"/>
    <circle :cx="parameterPoint(current)[0]" :cy="parameterPoint(current)[1]" r="28" class="lab-handle hit" tabindex="0" role="slider" aria-label="Điểm đang chọn trên đường nghiệm" :aria-valuetext="fmt(weight,5)" @pointerdown="parameterDrag.start('s',$event)" @keydown="parameterDrag.key('s',[weight,0],$event)"/>
   </svg>
  </div>
  <svg ref="weightSvg" viewBox="0 0 360 105" role="group" aria-label="Thước kéo trọng số s" @pointermove="weightDrag.move" @pointerup="weightDrag.end" @pointercancel="weightDrag.end" @lostpointercapture="weightDrag.end">
   <text x="180" y="23" text-anchor="middle">Trọng số s</text><line x1="32" x2="328" y1="54" y2="54" class="lab-axis"/>
   <text x="32" y="94" text-anchor="middle">0</text><text x="328" y="94" text-anchor="middle">1</text>
   <circle :cx="rail.sx(weight)" cy="54" r="6" class="lab-dot-warn"/>
   <circle :cx="rail.sx(weight)" cy="54" r="28" class="lab-handle hit" tabindex="0" role="slider" aria-label="Trọng số s trên thước" :aria-valuetext="fmt(weight,5)" @pointerdown="weightDrag.start('s',$event)" @keydown="weightDrag.key('s',[weight,.5],$event)"/>
  </svg>
  <div class="lab-controls"><label>Đại lượng phạt<select v-model="mode"><option value="ridge">Ridge, F₂ = bình phương chuẩn L₂</option><option value="lasso">Lasso, F₂ = chuẩn L₁</option></select></label></div>
  <div class="lab-buttons"><button type="button" @click="choose(0)">Chỉ cực tiểu sai số</button><button type="button" @click="choose(1)">μ = 1</button><button type="button" @click="choose(86/7,'lasso')">Lasso chạm trục</button><button type="button" @click="choose(38,'lasso')">Lasso bằng 0</button><button type="button" @click="choose(Infinity)">Chỉ cực tiểu độ lớn</button></div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút</summary><LabPointControls :svg="objectiveSvg" axes="x"/><LabPointControls :svg="parameterSvg" axes="x"/><LabPointControls :svg="weightSvg" axes="x"/></details>
  <div class="lab-readout" role="status">
   <p>s = {{fmt(weight,5)}}. x = {{fmtPoint(current.point,5)}}, F₁ = {{fmt(current.error,5)}}, F₂ = {{fmt(current.size,5)}}.</p>
   <p v-if="weight<1">Chia tổng cho 1 − s cho F₁ + μF₂ với μ = {{fmt(current.penalty,5)}}. Đường tựa đi qua cặp mục tiêu đang chọn.</p><p v-else>Trọng số (0, 1) chỉ cực tiểu F₂ và chọn x = (0, 0).</p>
   <p v-if="mode==='lasso'">Với dữ liệu cố định của bài, khi μ ≥ 86/7 thì x₂ = 0, và khi μ ≥ 38 thì cả hai tọa độ bằng 0. Tại ngưỡng, nhiều trọng số có thể cùng chọn một nghiệm.</p>
   <p v-else>Ridge dùng công thức nghiệm của hệ hai biến. Với dữ liệu này, mỗi tọa độ dương khi μ hữu hạn. Các dữ liệu khác vẫn có thể cho một tọa độ bằng 0.</p>
   <p>Chấm nhạt là các mẫu mục tiêu đạt được. Đường biên chỉ vẽ họ nghiệm của bài toán đang xét. Khi kéo, điểm được giữ trên đường và số đọc tính lại từ công thức nghiệm.</p>
  </div>
 </figure>
</template>

<style scoped>
svg text{font-size:18px;pointer-events:none}
.sample{fill:var(--ink-3);opacity:.18}
.frontier,.solution-path{fill:none;stroke-width:1.8}
.frontier{stroke:var(--tim)}
.solution-path{stroke:var(--xanh)}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
