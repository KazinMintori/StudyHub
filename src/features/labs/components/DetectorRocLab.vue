<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'
import { detectorAtFalseAlarm, detectorObservations, minimaxDetector, rocBudgets } from '../services/detector-roc.mjs'
import { planeBoxSection, project3 } from '../services/foundation-geometry.mjs'

const svg = ref(null)
const budget = ref(0.2)
const showRules = ref(false)
const view = ref(makeView({ x0: -0.05, x1: 1.06, y0: -0.07, y1: 1.07, width: 400, height: 335, pad: 34 }))
const active = computed(() => detectorAtFalseAlarm(budget.value))
const drag = createDragger(svg, view, (_, [value]) => {
  budget.value = Math.min(1, Math.max(0, value))
}, { step: 0.02, snap: 0.001 })
const position = ({ falseAlarm, detection }) => view.value.point([falseAlarm, detection])
const upper = rocBudgets.map(a => position(detectorAtFalseAlarm(a)))
const lower = upper.slice(1, -1).map(([x, y]) =>
  [view.value.sx(0) + view.value.sx(1) - x, view.value.sy(0) + view.value.sy(1) - y]
)
const coordinates = points => points.map(point => point.join(',')).join(' ')
const percentage = value => fmt(100 * value, 2) + '%'
const optimum = computed(() => position(active.value))
const noise = detectorObservations.map(row => row.noise)
const vertices = Array.from({ length: 8 }, (_, i) => [1, 2, 4].map(bit => Number(Boolean(i & bit))))
const edges = vertices.flatMap((_, i) => [1, 2, 4].filter(bit => !(i & bit)).map(bit => [i, i | bit]))
const camera = { yaw: 30, pitch: 26, scale: 132, origin: [200, 160] }
const ruleProjection = rule => project3(rule.map(value => value - 0.5), camera)
const ruleVertices = vertices.map(ruleProjection)
const rulePoint = computed(() => ruleProjection(active.value.rule))
const cut = computed(() => planeBoxSection(noise, budget.value - 0.5, 0.5).map(point => project3(point, camera)))
const axes = [
  { label: 'T₁₁', end: ruleProjection([1.24, 0, 0]), dx: 4, dy: 13 },
  { label: 'T₁₂', end: ruleProjection([0, 1.24, 0]), dx: -32, dy: 13 },
  { label: 'T₁₃', end: ruleProjection([0, 0, 1.24]), dx: 5, dy: -6 }
]
</script>

<template>
  <figure class="study-lab" aria-label="Biên ROC của bộ phát hiện ba trạng thái">
    <figcaption class="lab-title">Đánh đổi giữa báo động giả và phát hiện đúng</figcaption>
    <p class="lab-lead">Kéo điểm vàng trên biên trên. Mỗi vị trí cho xác suất phát hiện lớn nhất với ngân sách báo động giả tương ứng. Miền tô nhạt gồm các cặp xác suất mà quy tắc ngẫu nhiên hóa có thể đạt được.</p>
    <svg ref="svg" viewBox="0 0 400 335" role="group" aria-label="Miền ROC và điểm tối ưu kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polygon :points="coordinates([...upper, ...lower])" class="roc-region" />
      <line :x1="view.sx(0)" :x2="view.sx(1)" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" :y1="view.sy(0)" :y2="view.sy(1)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(1)" :y1="view.sy(1)" :y2="view.sy(0)" class="lab-guide" />
      <polyline :points="coordinates(upper)" class="lab-accent" />
      <text x="10" y="29">Pđ</text>
      <text x="360" :y="view.sy(0) + 5">Pbg</text>
      <text v-for="t in [0, 0.5, 1]" :key="t" :x="view.sx(t)" y="320" text-anchor="middle">{{ t }}</text>
      <text v-for="t in [0.5, 1]" :key="t" x="11" :y="view.sy(t) + 5">{{ t }}</text>
      <circle :cx="optimum[0]" :cy="optimum[1]" r="7" class="lab-dot-warn" />
      <circle :cx="optimum[0]" :cy="optimum[1]" r="31" class="lab-handle roc-hit" tabindex="0" role="slider"
        aria-label="Ngân sách xác suất báo động giả" :aria-valuemin="0" :aria-valuemax="1" :aria-valuenow="budget"
        :aria-valuetext="'Báo động giả ' + percentage(budget)"
        @pointerdown="drag.start('budget', $event)" @keydown="drag.key('budget', [budget, active.detection], $event)" />
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh ngân sách bằng nút</summary>
      <LabPointControls :svg="svg" axes="x" />
    </details>
    <div class="lab-buttons">
      <button type="button" @click="budget = 0.1">Dùng hết nhóm 3</button>
      <button type="button" @click="budget = 0.2">Báo động giả 20%</button>
      <button type="button" @click="budget = minimaxDetector.falseAlarm">Hai lỗi bằng nhau</button>
      <button type="button" :aria-pressed="showRules" @click="showRules = !showRules">Xem khối quyết định R³</button>
    </div>
    <template v-if="showRules">
      <svg viewBox="0 0 400 290" role="img" aria-label="Khối xác suất quyết định, mặt cắt theo ngân sách và quy tắc tối ưu">
        <polygon v-if="cut.length >= 3" :points="coordinates(cut)" class="roc-cut" />
        <line v-for="([a, b], index) in edges" :key="index"
          :x1="ruleVertices[a][0]" :y1="ruleVertices[a][1]" :x2="ruleVertices[b][0]" :y2="ruleVertices[b][1]" class="lab-axis" />
        <g v-for="{ label, end, dx, dy } in axes" :key="label">
          <line :x1="ruleVertices[0][0]" :y1="ruleVertices[0][1]" :x2="end[0]" :y2="end[1]" class="lab-guide" />
          <text :x="end[0] + dx" :y="end[1] + dy">{{ label }}</text>
        </g>
        <circle :cx="rulePoint[0]" :cy="rulePoint[1]" r="7" class="lab-dot-warn" />
      </svg>
      <p>Mỗi điểm trong khối là một bộ ba xác suất báo có tín hiệu. Mặt tím gồm các bộ ba dùng đúng ngân sách. Chấm vàng là bộ ba tối ưu của điểm đang chọn trên ROC.</p>
    </template>
    <div class="lab-readout" role="status">
      <p>Pbg báo động giả {{ percentage(active.falseAlarm) }}. Pđ phát hiện đúng {{ percentage(active.detection) }}. Bỏ sót {{ percentage(1 - active.detection) }}.</p>
      <p>Đường đứt là tập các cặp có xác suất báo động giả bằng xác suất bỏ sót.</p>
      <ul>
        <li v-for="(row, i) in detectorObservations" :key="row.observation">
          Quan sát {{ row.observation }}. Báo có tín hiệu với xác suất {{ percentage(active.rule[i]) }}.
        </li>
      </ul>
    </div>
  </figure>
</template>

<style scoped>
.roc-region { fill: var(--tim-soft); stroke: var(--ink-3); stroke-width: 1.2; }
.roc-cut { fill: var(--tim-soft); stroke: var(--tim); stroke-width: 1.2; }
.roc-hit { fill: transparent !important; stroke: transparent; }
.roc-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 18px; pointer-events: none; }
</style>
