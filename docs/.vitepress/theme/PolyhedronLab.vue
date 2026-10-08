<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, fmt, fmtPoint } from './svg-drag'
import { polyhedronInBox, add, scale, sub, dot } from './convex-geometry.mjs'
const clipId = `${useId()}-clip`

// Đa diện {x : aᵢᵀx ≤ bᵢ} trong R²: bật tắt từng ràng buộc, xem đỉnh, tính bị chặn và tính khả thi.
const view = makeView({ x0: -2, x1: 6, y0: -2, y1: 5, width: 440, height: 385 })
const P = p => view.point(p)
const constraints = ref([
  { a: [-1, 0], b: 0, label: 'x₁ ≥ 0', on: true },
  { a: [0, -1], b: 0, label: 'x₂ ≥ 0', on: true },
  { a: [1, 1], b: 4, label: 'x₁ + x₂ ≤ 4', on: true },
  { a: [1, -1], b: 2, label: 'x₁ − x₂ ≤ 2', on: true },
  { a: [-1, 2], b: 5, label: '−x₁ + 2x₂ ≤ 5', on: true },
  { a: [-1, -1], b: -5, label: 'x₁ + x₂ ≥ 5', on: false }
])
const active = computed(() => constraints.value.filter(c => c.on))
const BIG = 1000
const region = computed(() => polyhedronInBox(active.value.map(({ a, b }) => ({ a, b })), [-BIG, BIG, -BIG, BIG]))
const empty = computed(() => region.value.length < 3)
const unbounded = computed(() => region.value.some(p => Math.abs(p[0]) > BIG - 1 || Math.abs(p[1]) > BIG - 1))
const vertices = computed(() => region.value.filter(p => Math.abs(p[0]) < BIG - 1 && Math.abs(p[1]) < BIG - 1)
  .filter((p, i, arr) => arr.findIndex(q => Math.hypot(q[0] - p[0], q[1] - p[1]) < 1e-7) === i))
const drawn = computed(() => polyhedronInBox(active.value.map(({ a, b }) => ({ a, b })), [view.x0, view.x1, view.y0, view.y1]))
// Một đoạn của đường biên mỗi ràng buộc, cắt theo khung nhìn.
function boundaryLine({ a, b }) {
  const n2 = dot(a, a), x0 = scale(b / n2, a), d = [-a[1], a[0]]
  const pts = [-30, 30].map(t => add(x0, scale(t, d)))
  return pts
}
const tight = p => active.value.filter(c => Math.abs(dot(c.a, p) - c.b) < 1e-7).map(c => c.label)
</script>

<template>
  <figure class="study-lab" aria-label="Đa diện là giao của các nửa mặt phẳng">
    <p class="lab-title">Ghép đa diện từ từng nửa mặt phẳng</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Các đường biên của ràng buộc, miền đa diện tô màu và các đỉnh">
      <defs><clipPath :id="clipId"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath></defs>
      <line v-for="x in [-1, 1, 2, 3, 4, 5]" :key="`gx${x}`" :x1="view.sx(x)" :x2="view.sx(x)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="y in [-1, 1, 2, 3, 4]" :key="`gy${y}`" :y1="view.sy(y)" :y2="view.sy(y)" x1="0" :x2="view.width" class="lab-grid" />
      <line :x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :y1="0" :y2="view.height" :x1="view.sx(0)" :x2="view.sx(0)" class="lab-axis" />
      <g :clip-path="`url(#${clipId})`">
        <polygon v-if="drawn.length >= 3" :points="drawn.map(p => P(p).join(',')).join(' ')" class="lab-region" />
        <line v-for="c in active" :key="c.label" :x1="P(boundaryLine(c)[0])[0]" :y1="P(boundaryLine(c)[0])[1]" :x2="P(boundaryLine(c)[1])[0]" :y2="P(boundaryLine(c)[1])[1]" class="lab-guide" />
      </g>
      <g v-for="(v, i) in vertices" :key="i">
        <circle v-if="v[0] >= view.x0 && v[0] <= view.x1 && v[1] >= view.y0 && v[1] <= view.y1" :cx="P(v)[0]" :cy="P(v)[1]" r="6" class="lab-dot-accent" />
        <text v-if="v[0] >= view.x0 && v[0] <= view.x1 && v[1] >= view.y0 && v[1] <= view.y1" :x="P(v)[0] + 8" :y="P(v)[1] - 8" class="lab-small">{{ fmtPoint(v, 1) }}</text>
      </g>
    </svg>
    <div class="lab-controls">
      <label v-for="c in constraints" :key="c.label" class="lab-check"><input v-model="c.on" type="checkbox" /> {{ c.label }}</label>
    </div>
    <div class="lab-readout" role="status">
      <p v-if="empty" class="is-bad">Các ràng buộc đang bật mâu thuẫn nhau: đa diện rỗng. Bài toán tối ưu với miền khả thi này là bất khả thi.</p>
      <template v-else>
        <p>Đa diện là giao của {{ active.length }} nửa mặt phẳng{{ unbounded ? ' và không bị chặn: nó kéo dài ra vô hạn theo ít nhất một hướng.' : ', bị chặn, nên là một đa giác lồi.' }}</p>
        <p v-if="vertices.length">Các đỉnh: <span v-for="(v, i) in vertices" :key="i">{{ fmtPoint(v, 2) }} (chặt: {{ tight(v).join(', ') }}){{ i < vertices.length - 1 ? '; ' : '.' }}</span></p>
        <p v-else>Đa diện không có đỉnh nào: nó chứa trọn một đường thẳng.</p>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Tắt x₁ + x₂ ≤ 4. Đa diện thay đổi thế nào, và nó còn bị chặn không?</li>
        <li>Bật x₁ + x₂ ≥ 5 khi x₁ + x₂ ≤ 4 vẫn bật. Vì sao miền trở thành rỗng?</li>
        <li>Chỉ để lại x₁ − x₂ ≤ 2. Đa diện có đỉnh không?</li>
        <li>Ở mỗi đỉnh, có đúng mấy ràng buộc chặt?</li>
      </ol>
    </details>
  </figure>
</template>
