<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'

// Khoảng cách giữa hai đa giác lồi (chủ đề 7, Lecture 02): QP cực tiểu ‖x₁ − x₂‖² với x₁ ∈ P₁, x₂ ∈ P₂.
// Trong mặt phẳng, nghiệm của QP được tính đúng bằng hình học: nếu hai đa giác rời nhau (kiểm bằng trục tách),
// cặp điểm gần nhất là một đỉnh của đa giác này và điểm gần nhất trên một cạnh của đa giác kia.
const P1 = [[0.5, 0.5], [2.5, 0.8], [2.0, 2.6], [0.6, 2.0]]
const SHAPE2 = [[-0.8, -0.6], [0.9, -0.4], [0.6, 0.9], [-0.7, 0.7]]
const c2 = ref([4.5, 2.2])
const P2 = computed(() => SHAPE2.map(([a, b]) => [c2.value[0] + a, c2.value[1] + b]))
const sub = (a, b) => [a[0] - b[0], a[1] - b[1]]
const dot = (a, b) => a[0] * b[0] + a[1] * b[1]
const closestOnSeg = (p, a, b) => {
  const ab = sub(b, a), t = Math.min(1, Math.max(0, dot(sub(p, a), ab) / dot(ab, ab)))
  return [a[0] + t * ab[0], a[1] + t * ab[1]]
}
const separated = (A, B) => {
  for (const poly of [A, B]) for (let i = 0; i < poly.length; i++) {
    const e = sub(poly[(i + 1) % poly.length], poly[i]), n = [-e[1], e[0]]
    const pa = A.map(p => dot(n, p)), pb = B.map(p => dot(n, p))
    if (Math.max(...pa) < Math.min(...pb) || Math.max(...pb) < Math.min(...pa)) return true
  }
  return false
}
const result = computed(() => {
  const A = P1, B = P2.value
  if (!separated(A, B)) return { d: 0 }
  let best = { d: Infinity }
  const scan = (V, W, flip) => {
    for (const v of V) for (let i = 0; i < W.length; i++) {
      const q = closestOnSeg(v, W[i], W[(i + 1) % W.length]), d = Math.hypot(...sub(v, q))
      if (d < best.d) best = { d, x1: flip ? q : v, x2: flip ? v : q }
    }
  }
  scan(A, B, false); scan(B, A, true)
  return best
})
// Đường trung trực của đoạn nối hai điểm gần nhất là một siêu phẳng tách hai đa giác.
const bisector = computed(() => {
  const r = result.value
  if (!r.x1) return null
  const m = [(r.x1[0] + r.x2[0]) / 2, (r.x1[1] + r.x2[1]) / 2], d = sub(r.x2, r.x1), t = [-d[1], d[0]], L = 20 / Math.hypot(...t)
  return [[m[0] - L * t[0], m[1] - L * t[1]], [m[0] + L * t[0], m[1] + L * t[1]]]
})
const view = ref(makeView({ x0: -0.5, x1: 6.5, y0: -0.5, y1: 4.5, width: 460, height: 329 }))
const svg = ref(null)
const P = (p) => [view.value.sx(p[0]), view.value.sy(p[1])]
const drag = createDragger(svg, view, (_, p) => { c2.value = p }, { step: 0.1, snap: 0.05 })
</script>

<template>
  <figure class="study-lab" aria-label="Khoảng cách giữa hai đa giác lồi là nghiệm của một quy hoạch toàn phương">
    <p class="lab-title">Hai điểm gần nhau nhất của hai đa giác</p>
    <p class="lab-lead">Kéo đa giác bên phải. Cặp điểm gần nhau nhất là nghiệm của một QP bốn biến, và đường trung trực của đoạn nối chúng tách hai đa giác.</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Hai đa giác, đoạn nối hai điểm gần nhất và đường thẳng tách" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <line v-for="t in [0, 1, 2, 3, 4, 5, 6]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="t in [0, 1, 2, 3, 4]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line v-if="bisector" :x1="P(bisector[0])[0]" :y1="P(bisector[0])[1]" :x2="P(bisector[1])[0]" :y2="P(bisector[1])[1]" class="lab-guide" />
      <polygon :points="P1.map(p => P(p).join(',')).join(' ')" class="lab-region" />
      <polygon :points="P2.map(p => P(p).join(',')).join(' ')" :class="result.d === 0 ? 'lab-bad-fill' : 'lab-good-fill'" style="opacity: 0.85" />
      <template v-if="result.x1">
        <line :x1="P(result.x1)[0]" :y1="P(result.x1)[1]" :x2="P(result.x2)[0]" :y2="P(result.x2)[1]" class="lab-warn" />
        <circle :cx="P(result.x1)[0]" :cy="P(result.x1)[1]" r="6" class="lab-dot-warn" />
        <circle :cx="P(result.x2)[0]" :cy="P(result.x2)[1]" r="6" class="lab-dot-warn" />
      </template>
      <text :x="P([1.2, 1.4])[0]" :y="P([1.2, 1.4])[1]" class="lab-small">P₁</text>
      <circle :cx="P(c2)[0]" :cy="P(c2)[1]" r="10" class="lab-handle" tabindex="0" role="slider" aria-label="Kéo đa giác P₂" :aria-valuetext="`tâm ${fmtPoint(c2)}`" @pointerdown="drag.start('c2', $event)" @keydown="drag.key('c2', c2, $event)" />
      <text :x="P(c2)[0] + 12" :y="P(c2)[1] - 10" class="lab-small">P₂</text>
    </svg>
    <p class="lab-legend"><span class="legend-accent">P₁</span><span class="legend-good">P₂ (rời P₁)</span><span class="legend-bad">P₂ chồng lên P₁</span><span class="legend-warn">đoạn ngắn nhất</span><span class="legend-guide">đường thẳng tách</span></p>
    <div class="lab-readout" role="status">
      <p>QP: cực tiểu ‖x₁ − x₂‖² với x₁ ∈ P₁ và x₂ ∈ P₂, gồm 4 biến và 8 bất đẳng thức tuyến tính.</p>
      <p v-if="result.d === 0" class="is-bad">Hai đa giác giao nhau: giá trị tối ưu bằng 0, và mọi điểm chung đều cho x₁ = x₂ tối ưu.</p>
      <template v-else>
        <p>Khoảng cách <span class="is-accent">{{ fmt(result.d, 3) }}</span>, đạt tại x₁ = {{ fmtPoint(result.x1) }} và x₂ = {{ fmtPoint(result.x2) }}.</p>
        <p>Đường trung trực của đoạn x₁x₂ tách hẳn hai đa giác: đây là một siêu phẳng tách, dựng được từ nghiệm của QP.</p>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo P₂ quanh P₁. Cặp điểm gần nhất khi thì là hai đỉnh, khi thì là một đỉnh và một điểm giữa cạnh. Khi nào xảy ra trường hợp nào?</li>
        <li>Khi điểm gần nhất nằm giữa một cạnh, đoạn ngắn nhất tạo với cạnh ấy góc bao nhiêu?</li>
        <li>Kéo hai đa giác cho chạm nhau. Nghiệm của QP còn duy nhất không?</li>
        <li>Kéo P₂ dọc một đường thẳng đi ngang qua P₁ và theo dõi khoảng cách. Vì sao khoảng cách, xem như hàm của vị trí P₂, là một hàm lồi?</li>
      </ol>
    </details>
  </figure>
</template>
