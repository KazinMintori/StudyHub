<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const svg = ref(null)
const middle = ref(0)
const showSurface = ref(false)
const chordHeight = 4 / 3
const slopes = computed(() => [middle.value - 1, (2 - middle.value) / 2])
const feasible = computed(() => middle.value <= chordHeight)
const samples = computed(() => [[0, 1], [1, middle.value], [3, 2]])
const view = ref(makeView({ x0: -0.25, x1: 3.35, y0: -0.85, y1: 2.7, width: 400, height: 290, pad: 34 }))
const point = coordinates => view.value.point(coordinates).join(',')
const drag = createDragger(svg, view, (_, [, y]) => {
  middle.value = Math.max(-0.25, Math.min(2.5, y))
}, { step: 0.05, snap: 0.01 })

const project = ([x, z, y]) => [72 + 76 * x + 32 * z, 194 + 9 * x - 23 * z - 42 * y]
const axisOrigin = project([0, -1, -0.25])
const axes = [
  { label: 'x', end: project([3.25, -1, -0.25]), dx: 7, dy: 3 },
  { label: 'z', end: project([0, 1.2, -0.25]), dx: -12, dy: 32 },
  { label: 'y', end: project([0, -1, 2]), dx: -12, dy: -6 }
]
const surfaceHeight = (x, z) => {
  const [left, right] = slopes.value
  return middle.value + Math.max(left * (x - 1), right * (x - 1)) + Math.abs(z)
}
const surfaceFaces = computed(() => [[0, 1], [1, 3]].flatMap(([left, right]) =>
  [[0, 1], [-1, 0]].map(([near, far]) =>
    [[left, near], [right, near], [right, far], [left, far]]
      .map(([x, z]) => project([x, z, surfaceHeight(x, z)]).join(',')).join(' ')
  )
))
const centerSection = computed(() => samples.value.map(([x, y]) => project([x, 0, y]).join(',')).join(' '))
</script>

<template>
  <figure class="study-lab" aria-label="Điều kiện nội suy lồi và mặt nâng">
    <figcaption class="lab-title">Kéo điểm giữa qua dây cung</figcaption>
    <p class="lab-lead">Đường đứt nối hai điểm cố định. Kéo điểm vàng theo chiều dọc để xem khi nào hai hệ số góc có thể tạo thành một hàm lồi đi qua cả ba điểm.</p>
    <svg ref="svg" viewBox="0 0 400 290" role="group" aria-label="Ba điểm nội suy, điểm giữa có thể kéo"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="32" x2="369" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="36" y2="252" class="lab-axis" />
      <text x="17" y="29">y</text>
      <text x="372" y="273">x</text>
      <text v-for="x in [0, 1, 3]" :key="x" :x="view.sx(x)" y="273" text-anchor="middle">{{ x }}</text>
      <polyline :points="[point([0, 1]), point([3, 2])].join(' ')" class="lab-guide" />
      <polyline v-if="feasible" :points="samples.map(point).join(' ')" class="lab-accent" />
      <line v-else :x1="view.sx(1)" :x2="view.sx(1)" :y1="view.sy(chordHeight)" :y2="view.sy(middle)" class="lab-warn" />
      <circle v-for="([x, y], index) in samples" :key="x" :cx="view.sx(x)" :cy="view.sy(y)"
        r="6" :class="index === 1 ? 'lab-dot-warn' : 'lab-dot-good'" />
      <circle :cx="view.sx(1)" :cy="view.sy(middle)" r="31" class="lab-handle interpolation-hit"
        tabindex="0" role="slider" aria-label="Độ cao điểm nội suy ở giữa"
        :aria-valuemin="-0.25" :aria-valuemax="2.5" :aria-valuenow="middle"
        :aria-valuetext="'y = ' + fmt(middle, 3)" aria-orientation="vertical"
        @pointerdown="drag.start('middle', $event)" @keydown="drag.key('middle', [1, middle], $event)" />
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh điểm giữa bằng nút</summary>
      <LabPointControls :svg="svg" axes="y" />
    </details>
    <div class="lab-buttons">
      <button type="button" @click="middle = 0">Dưới dây cung</button>
      <button type="button" @click="middle = chordHeight">Trên dây cung</button>
      <button type="button" @click="middle = 1.75">Cao hơn dây cung</button>
      <button type="button" :aria-pressed="showSurface" @click="showSurface = !showSurface">Xem mặt trong R³</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Độ cao điểm giữa {{ fmt(middle, 3) }}. Hệ số góc bên trái {{ fmt(slopes[0], 3) }}, bên phải {{ fmt(slopes[1], 3) }}.</p>
      <p v-if="feasible">Hệ số góc không giảm. Đường tím là đồ thị của giá trị lớn nhất trong hai hàm affine kéo dài từ hai đoạn thẳng.</p>
      <p v-else>Điểm giữa cao hơn dây cung. Bất đẳng thức lồi tại hoành độ 1 bị vi phạm, nên ba điểm này không thể cùng thuộc đồ thị của một hàm lồi.</p>
    </div>
    <template v-if="showSurface">
      <svg v-if="feasible" viewBox="0 0 400 275" role="img" aria-label="Bốn mảnh mặt phẳng ghép thành đồ thị lồi của hai biến">
        <g v-for="{ label, end, dx, dy } in axes" :key="label">
          <line :x1="axisOrigin[0]" :y1="axisOrigin[1]" :x2="end[0]" :y2="end[1]" class="lab-axis" />
          <text :x="end[0] + dx" :y="end[1] + dy">{{ label }}</text>
        </g>
        <polygon v-for="(face, i) in surfaceFaces" :key="i" :points="face" class="interpolation-face" :class="{ 'far-face': i % 2 === 0 }" />
        <polyline :points="centerSection" class="lab-accent" />
      </svg>
      <p v-if="feasible">Mặt ghép là đồ thị của g(x, z) = f(x) + |z|. Mỗi lát z cố định là đường f nâng lên một đoạn |z|. Đường tím là lát z = 0.</p>
      <p v-else>Mặt nâng chỉ hiển thị khi có một hàm lồi nội suy để làm lát z = 0.</p>
    </template>
  </figure>
</template>

<style scoped>
.interpolation-hit { fill: transparent !important; stroke: transparent; }
.interpolation-hit:focus-visible { stroke: var(--vang); }
.interpolation-face { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.5; }
.far-face { fill: var(--paper); }
svg text { font-size: 19px; pointer-events: none; }
</style>
