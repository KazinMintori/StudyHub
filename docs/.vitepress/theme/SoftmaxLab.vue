<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { contourSegments } from './contour.mjs'

// Log-sum-exp với nhiệt độ: lse_β(x) = (1/β) log(e^(βx₁) + e^(βx₂)) là xấp xỉ trơn của max{x₁, x₂},
// với max ≤ lse_β ≤ max + (log 2)/β. Gradient của nó là vector softmax(βx), luôn nằm trong đơn hình.
const beta = ref(1)
const uid = useId()
const clip = `${uid}-soft-clip`, arrow = `${uid}-soft-arrow`
const svg = ref(null)
const view = ref(makeView({ x0: -3, x1: 3, y0: -3, y1: 3, width: 340, height: 340 }))
const P = p => view.value.point(p)
const state = ref({ x: [1, 0.4] })
const drag = createDragger(svg, view, (name, value) => { state.value = { ...state.value, [name]: value } }, { step: 0.1, snap: 0.05 })
const x = computed(() => state.value.x)
// Tính ổn định số: trừ max trước khi lấy mũ.
const lse = (p, b) => { const m = Math.max(p[0], p[1]); return m + Math.log(Math.exp(b * (p[0] - m)) + Math.exp(b * (p[1] - m))) / b }
const softmax = (p, b) => { const m = Math.max(p[0], p[1]), e = [Math.exp(b * (p[0] - m)), Math.exp(b * (p[1] - m))], s = e[0] + e[1]; return [e[0] / s, e[1] / s] }
const levels = [-1, 0, 1, 2]
const smooth = computed(() => levels.map(c => contourSegments(p => lse(p, beta.value), { x0: -3, x1: 3, y0: -3, y1: 3, n: 90 }, c)))
const corners = levels.map(c => [[c, -3], [c, c], [-3, c]].map(P).map(q => q.join(',')).join(' '))
const maxVal = computed(() => Math.max(...x.value))
const lseVal = computed(() => lse(x.value, beta.value))
const w = computed(() => softmax(x.value, beta.value))
const tip = computed(() => [x.value[0] + 1.2 * w.value[0], x.value[1] + 1.2 * w.value[1]])
</script>

<template>
  <figure class="study-lab" aria-label="Log-sum-exp như một phiên bản trơn của hàm max">
    <p class="lab-title">Log-sum-exp: hàm max được làm trơn</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Đường mức của hàm max và của log-sum-exp, cùng gradient softmax tại một điểm" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs>
        <clipPath :id="clip"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath>
        <marker :id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="lab-arrow-accent" /></marker>
      </defs>
      <g :clip-path="`url(#${clip})`">
        <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
        <line :x1="P([-3, -3])[0]" :y1="P([-3, -3])[1]" :x2="P([3, 3])[0]" :y2="P([3, 3])[1]" class="lab-grid" />
        <polyline v-for="(pts, i) in corners" :key="`m${i}`" :points="pts" class="lab-guide" />
        <g v-for="(segs, k) in smooth" :key="`s${k}`">
          <line v-for="(s, i) in segs" :key="i" :x1="P(s[0])[0]" :y1="P(s[0])[1]" :x2="P(s[1])[0]" :y2="P(s[1])[1]" class="lab-warn" />
        </g>
        <line :x1="P(x)[0]" :y1="P(x)[1]" :x2="P(tip)[0]" :y2="P(tip)[1]" class="lab-accent" :marker-end="`url(#${arrow})`" />
        <circle :cx="P(x)[0]" :cy="P(x)[1]" r="8" class="lab-handle" tabindex="0" role="slider" aria-label="Điểm x" :aria-valuetext="fmtPoint(x)" @pointerdown="drag.start('x', $event)" @keydown="drag.key('x', x, $event)" />
      </g>
    </svg>
    <p class="lab-legend"><span class="legend-guide">đường mức của max{x₁, x₂} tại −1, 0, 1, 2</span><span class="legend-warn">đường mức của lse_β</span><span class="legend-accent">gradient = softmax(βx)</span></p>
    <div class="lab-controls">
      <label>β = {{ fmt(beta, 1) }}<input v-model.number="beta" type="range" min="0.5" max="10" step="0.5" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p>Tại x = {{ fmtPoint(x) }}: max{x₁, x₂} = {{ fmt(maxVal, 3) }}, lse_β(x) = {{ fmt(lseVal, 3) }}. Chênh lệch {{ fmt(lseVal - maxVal, 3) }} không vượt (log 2)/β = {{ fmt(Math.log(2) / beta, 3) }}.</p>
      <p>Gradient ∇lse_β(x) = softmax(βx) = {{ fmtPoint(w, 3) }}, hai thành phần không âm và cộng lại bằng 1.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Tăng β từ 0.5 lên 10. Góc của đường mức vàng thay đổi thế nào, và nó tiến dần tới hình gì?</li>
        <li>Đặt x trên đường chéo x₁ = x₂. Chênh lệch giữa lse_β và max lúc này bằng bao nhiêu, và vì sao đó là chênh lệch lớn nhất?</li>
        <li>Kéo x ra xa đường chéo. Mũi tên gradient quay về hướng nào? Với β lớn, softmax trông giống hàm nào?</li>
      </ol>
    </details>
  </figure>
</template>
