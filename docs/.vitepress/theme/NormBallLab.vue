<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { pNorm, pBallBoundary } from './convex-geometry.mjs'

// Quả cầu đơn vị {x : ||x||_p <= 1} trong R² khi p thay đổi; p < 1 không còn là chuẩn.
const svg = ref(null)
const view = ref(makeView({ x0: -1.6, x1: 1.6, y0: -1.25, y1: 1.25, width: 420, height: 328 }))
const P = p => view.value.point(p)
const exponent = ref(1.5), infinite = ref(false)
const p = computed(() => (infinite.value ? Infinity : exponent.value))
const pt = ref({ x: [0.7, 0.45] })
const drag = createDragger(svg, view, (name, value) => { pt.value = { ...pt.value, [name]: value } }, { step: 0.05, snap: 0.01 })
const ball = computed(() => pBallBoundary(p.value, 240))
const refs = [1, 2, Infinity].map(q => ({ q, pts: pBallBoundary(q, 120) }))
const nonConvex = computed(() => p.value < 1)
const mid = [0.5, 0.5]
const midNorm = computed(() => pNorm(mid, p.value))
const label = q => (q === Infinity ? '∞' : String(q))
</script>

<template>
  <figure class="study-lab" aria-label="Quả cầu đơn vị của chuẩn p">
    <p class="lab-title">Quả cầu đơn vị của ‖x‖ₚ khi p thay đổi</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Biên của tập ‖x‖ₚ ≤ 1, ba đường tham chiếu p = 1, 2, vô cùng và một điểm thử" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <line :x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :y1="0" :y2="view.height" :x1="view.sx(0)" :x2="view.sx(0)" class="lab-axis" />
      <polygon v-for="r in refs" :key="r.q" :points="r.pts.map(q => P(q).join(',')).join(' ')" class="lab-guide" />
      <polygon :points="ball.map(q => P(q).join(',')).join(' ')" class="lab-region" />
      <template v-if="nonConvex">
        <line :x1="P([1, 0])[0]" :y1="P([1, 0])[1]" :x2="P([0, 1])[0]" :y2="P([0, 1])[1]" class="lab-bad" />
        <circle :cx="P(mid)[0]" :cy="P(mid)[1]" r="6" class="lab-dot-bad" />
        <circle :cx="P([1, 0])[0]" :cy="P([1, 0])[1]" r="5" class="lab-dot" /><circle :cx="P([0, 1])[0]" :cy="P([0, 1])[1]" r="5" class="lab-dot" />
      </template>
      <text :x="P([1, 0])[0] + 6" :y="P([1, 0])[1] + 18" class="lab-small">1</text>
      <text :x="P([0, 1])[0] + 6" :y="P([0, 1])[1] - 6" class="lab-small">1</text>
      <circle :cx="P(pt.x)[0]" :cy="P(pt.x)[1]" r="9" class="lab-handle lab-handle-alt" tabindex="0" role="slider" aria-label="Điểm thử x" @pointerdown="drag.start('x', $event)" @keydown="drag.key('x', pt.x, $event)" />
      <text :x="P(pt.x)[0] + 12" :y="P(pt.x)[1] - 8">x</text>
    </svg>
    <div class="lab-controls">
      <label>p = {{ infinite ? '∞' : fmt(exponent, 2) }}<input v-model.number="exponent" type="range" min="0.5" max="8" step="0.05" :disabled="infinite" /></label>
      <label class="lab-check"><input v-model="infinite" type="checkbox" /> Lấy p = ∞</label>
    </div>
    <div class="lab-readout" role="status">
      <p>Với x = {{ fmtPoint(pt.x) }}: ‖x‖₁ = {{ fmt(pNorm(pt.x, 1)) }}, ‖x‖₂ = {{ fmt(pNorm(pt.x, 2)) }}, ‖x‖∞ = {{ fmt(pNorm(pt.x, Infinity)) }}, còn ‖x‖ₚ = <span class="is-accent">{{ fmt(pNorm(pt.x, p)) }}</span>. Điểm x {{ pNorm(pt.x, p) <= 1 + 1e-9 ? 'thuộc' : 'không thuộc' }} vùng tô.</p>
      <p v-if="nonConvex" class="is-bad">Với p = {{ fmt(exponent, 2) }} &lt; 1, hai điểm (1, 0) và (0, 1) thuộc tập, nhưng trung điểm (0.5, 0.5) cho giá trị {{ fmt(midNorm, 3) }} &gt; 1. Tập không lồi, nên biểu thức này không phải một chuẩn: bất đẳng thức tam giác bị vi phạm.</p>
      <p v-else>Với p ≥ 1, tập là lồi và đối xứng qua gốc. Ba đường nét đứt là quả cầu đơn vị của p = 1, 2 và ∞ để so sánh.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo p từ 1 lên 8. Hình thoi dần biến thành hình gì?</li>
        <li>Kéo p xuống dưới 1. Chỗ nào của tập bị "lõm" vào?</li>
        <li>Đặt x = (0.6, 0.6). Điểm này thuộc quả cầu của chuẩn nào trong ba chuẩn tham chiếu?</li>
      </ol>
    </details>
  </figure>
</template>
