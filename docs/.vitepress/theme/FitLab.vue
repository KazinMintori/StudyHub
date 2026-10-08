<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt } from './svg-drag'
import { leastSquaresLine, l1Line, chebyshevLine, lossL1, lossL2, lossLinf } from './fitting.mjs'

// Năm điểm dữ liệu kéo được; ba đường thẳng tối ưu theo ba tiêu chí khác nhau.
const svg = ref(null)
const view = ref(makeView({ x0: -0.5, x1: 4.5, y0: -1, y1: 8, width: 440, height: 330 }))
const points = ref([[0, 0.5], [1, 1.5], [2, 1.8], [3, 3.2], [4, 7]])
const drag = createDragger(svg, view, (name, value) => {
  const i = Number(name)
  points.value = points.value.map((p, j) => (j === i ? [p[0], value[1]] : p)) // chỉ cho kéo theo phương đứng
}, { step: 0.1, snap: 0.1 })
const show = ref({ l2: true, l1: true, linf: false })
const residualsOf = ref('l2')

const fits = computed(() => {
  const pts = points.value
  const l2 = leastSquaresLine(pts), l1 = l1Line(pts), linf = chebyshevLine(pts)
  return [
    { key: 'l2', name: 'Bình phương tối thiểu', line: l2, cls: 'lab-accent' },
    { key: 'l1', name: 'Tổng trị tuyệt đối (ℓ₁)', line: l1, cls: 'lab-good' },
    { key: 'linf', name: 'Sai số lớn nhất (ℓ∞)', line: linf, cls: 'lab-warn' }
  ].filter(f => f.line)
})
const ends = line => [[view.value.x0, line.a * view.value.x0 + line.c], [view.value.x1, line.a * view.value.x1 + line.c]]
const P = p => view.value.point(p)
const residualLine = computed(() => fits.value.find(f => f.key === residualsOf.value)?.line)
</script>

<template>
  <figure class="study-lab" aria-label="So sánh ba cách khớp đường thẳng">
    <p class="lab-title">Ba tiêu chí, ba đường thẳng</p>
    <p class="lab-lead">Kéo các điểm theo chiều dọc. Đường tím cực tiểu tổng bình phương phần dư, đường xanh cực tiểu tổng trị tuyệt đối, đường vàng cực tiểu phần dư lớn nhất.</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Năm điểm dữ liệu và các đường khớp" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <line v-for="x in [0, 1, 2, 3, 4]" :key="`gx${x}`" :x1="view.sx(x)" :x2="view.sx(x)" y1="0" :y2="view.height" :class="x === 0 ? 'lab-axis' : 'lab-grid'" />
      <line v-for="y in [0, 2, 4, 6, 8]" :key="`gy${y}`" :y1="view.sy(y)" :y2="view.sy(y)" x1="0" :x2="view.width" :class="y === 0 ? 'lab-axis' : 'lab-grid'" />
      <text v-for="x in [1, 2, 3, 4]" :key="`tx${x}`" :x="view.sx(x) - 4" :y="view.sy(0) + 18" class="lab-small">{{ x }}</text>
      <text v-for="y in [2, 4, 6]" :key="`ty${y}`" :x="view.sx(0) - 16" :y="view.sy(y) + 5" class="lab-small">{{ y }}</text>
      <g v-if="residualLine">
        <line v-for="(p, i) in points" :key="`r${i}`" :x1="P(p)[0]" :y1="P(p)[1]" :x2="P(p)[0]" :y2="P([p[0], residualLine.a * p[0] + residualLine.c])[1]" class="lab-guide" />
      </g>
      <template v-for="f in fits" :key="f.key">
        <line v-if="show[f.key]" :x1="P(ends(f.line)[0])[0]" :y1="P(ends(f.line)[0])[1]" :x2="P(ends(f.line)[1])[0]" :y2="P(ends(f.line)[1])[1]" :class="f.cls" />
      </template>
      <circle v-for="(p, i) in points" :key="i" :cx="P(p)[0]" :cy="P(p)[1]" r="9" class="lab-handle" tabindex="0" role="slider" :aria-label="`Điểm dữ liệu thứ ${i + 1}, kéo theo chiều dọc`" @pointerdown="drag.start(String(i), $event)" @keydown="drag.key(String(i), p, $event)" />
    </svg>
    <div class="lab-controls">
      <label class="lab-check"><input v-model="show.l2" type="checkbox" /> Đường bình phương tối thiểu</label>
      <label class="lab-check"><input v-model="show.l1" type="checkbox" /> Đường ℓ₁</label>
      <label class="lab-check"><input v-model="show.linf" type="checkbox" /> Đường ℓ∞</label>
      <label>Vẽ phần dư của
        <select v-model="residualsOf"><option value="l2">đường bình phương tối thiểu</option><option value="l1">đường ℓ₁</option><option value="linf">đường ℓ∞</option></select>
      </label>
    </div>
    <div class="lab-readout" role="status">
      <p v-for="f in fits" :key="f.key"><span :class="f.key === 'l2' ? 'is-accent' : f.key === 'l1' ? 'is-good' : ''">{{ f.name }}:</span> y = {{ fmt(f.line.a) }}t {{ f.line.c < 0 ? '−' : '+' }} {{ fmt(Math.abs(f.line.c)) }}. Tổng bình phương {{ fmt(lossL2(points, f.line)) }}, tổng trị tuyệt đối {{ fmt(lossL1(points, f.line)) }}, sai số lớn nhất {{ fmt(lossLinf(points, f.line)) }}.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Đọc bảng số: mỗi đường thắng đúng ở tiêu chí mà nó tối ưu, nhưng thua ở hai tiêu chí kia.</li>
        <li>Kéo điểm cuối lên thật cao. Đường nào bị kéo theo nhiều nhất, đường nào gần như không đổi?</li>
        <li>Đặt năm điểm thẳng hàng. Ba đường có trùng nhau không? Vì sao?</li>
      </ol>
    </details>
  </figure>
</template>
