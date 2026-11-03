<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const initial = [1, 5, 4]
const counts = ref(initial)
const step = ref(0)
const svg = ref(null)
const view = ref(makeView({ x0: 0.4, x1: 3.6, y0: 0, y1: 8.5, width: 400, height: 290, pad: 38 }))
const drag = createDragger(svg, view, (name, [, y]) => {
  counts.value = counts.value.map((count, index) => index === Number(name) ? Math.max(1, Math.min(8, y)) : count)
  step.value = 0
}, { snap: 1, step: 1 })

const history = computed(() => {
  let blocks = counts.value.map((count, index) => ({ first: index + 1, last: index + 1, total: count, size: 1 }))
  const stages = [blocks]
  let violation = blocks.findIndex((block, i) => i < blocks.length - 1 &&
    block.total * blocks[i + 1].size < blocks[i + 1].total * block.size)
  while (violation !== -1) {
    const [left, right] = blocks.slice(violation, violation + 2)
    const merged = { first: left.first, last: right.last, total: left.total + right.total, size: left.size + right.size }
    blocks = [...blocks.slice(0, violation), merged, ...blocks.slice(violation + 2)]
    stages.push(blocks)
    violation = blocks.findIndex((block, i) => i < blocks.length - 1 &&
      block.total * blocks[i + 1].size < blocks[i + 1].total * block.size)
  }
  return stages
})
const blocks = computed(() => history.value[step.value])
const mass = computed(() => {
  const total = counts.value.reduce((sum, count) => sum + count, 0)
  return blocks.value.flatMap(block => Array(block.size).fill(block.total / block.size / total))
})
</script>

<template>
  <figure class="study-lab" aria-label="Gộp các khối kề vi phạm thứ tự không tăng">
    <figcaption class="lab-title">Gộp khối để khôi phục thứ tự</figcaption>
    <p class="lab-lead">Kéo chấm vàng để đổi số đếm. Sau đó bấm Gộp khối kế tiếp. Mỗi thanh tím bao trùm một khối và có độ cao bằng số đếm trung bình của khối.</p>
    <svg ref="svg" viewBox="0 0 400 290" role="group" aria-label="Ba số đếm kéo được và các khối đang gộp"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <text x="13" y="25">Số đếm</text>
      <line x1="38" x2="362" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <g v-for="value in [2, 4, 6, 8]" :key="value">
        <line x1="38" x2="362" :y1="view.sy(value)" :y2="view.sy(value)" class="lab-grid" />
        <text x="13" :y="view.sy(value) + 6">{{ value }}</text>
      </g>
      <rect v-for="block in blocks" :key="block.first" :x="view.sx(block.first - 0.37)"
        :width="view.sx(block.last + 0.37) - view.sx(block.first - 0.37)"
        :y="view.sy(block.total / block.size)" :height="view.sy(0) - view.sy(block.total / block.size)" class="count-block" />
      <g v-for="(count, index) in counts" :key="index">
        <text :x="view.sx(index + 1)" y="277" text-anchor="middle">{{ index + 1 }}</text>
        <circle :cx="view.sx(index + 1)" :cy="view.sy(count)" r="6" class="lab-dot-warn" />
        <circle :cx="view.sx(index + 1)" :cy="view.sy(count)" r="31" class="lab-handle count-hit" tabindex="0"
          role="slider" :aria-label="'Số đếm trạng thái ' + (index + 1)" aria-valuemin="1" aria-valuemax="8"
          :aria-valuenow="count" :aria-valuetext="'Số đếm ' + count" aria-orientation="vertical"
          @pointerdown="drag.start(String(index), $event)" @keydown="drag.key(String(index), [index + 1, count], $event)" />
      </g>
    </svg>
    <details class="lab-tasks">
      <summary>Điều chỉnh số đếm bằng nút</summary>
      <LabPointControls :svg="svg" axes="y" />
    </details>
    <div class="lab-buttons">
      <button type="button" :disabled="step === history.length - 1" @click="step++">Gộp khối kế tiếp</button>
      <button type="button" @click="step = history.length - 1">Tới nghiệm</button>
      <button type="button" @click="counts = initial; step = 0">Về ví dụ (1, 5, 4)</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Đã gộp {{ step }} lần. Xác suất hiện tại ({{ mass.map(p => fmt(p, 4)).join(', ') }}).</p>
      <p v-if="step < history.length - 1">Còn một cặp khối kề có trung bình tăng. Gộp cặp đó để sửa vi phạm.</p>
      <p v-else>Trung bình các khối đã không tăng. Sau chuẩn hóa, ta được phân phối đơn điệu tối đa hóa log-likelihood.</p>
    </div>
  </figure>
</template>

<style scoped>
.count-block { fill: var(--tim-soft); stroke: var(--tim); stroke-width: 1.4; }
.count-hit { fill: transparent !important; stroke: transparent; }
.count-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
