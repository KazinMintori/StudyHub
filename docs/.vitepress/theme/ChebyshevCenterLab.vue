<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'

// Tâm Chebyshev của đa giác {x : aᵢᵀx ≤ bᵢ} (chủ đề 5, Lecture 02): cực đại r với aᵢᵀx_c + r‖aᵢ‖ ≤ bᵢ.
// LP ba biến (x_c, r) được giải đúng bằng cách xét mọi bộ ba ràng buộc chặt: nghiệm của LP có giá trị hữu hạn
// luôn đạt tại một đỉnh, và mỗi đỉnh của miền khả thi trong R³ là giao của ba mặt.
const DEFAULT = [
  { a: [-1, 0], b: 0 }, { a: [0, -1], b: 0 }, { a: [1, 2], b: 8 }, { a: [3, 1], b: 12 }, { a: [-1, 1], b: 3 }
]
const cons = ref(DEFAULT.map(c => ({ ...c })))
const showCentroid = ref(false)
const norm = (a) => Math.hypot(a[0], a[1])
const dot = (u, v) => u[0] * v[0] + u[1] * v[1]

function solve3(M, rhs) {
  const det = (m) => m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
  const D = det(M)
  if (Math.abs(D) < 1e-10) return null
  return [0, 1, 2].map(k => det(M.map((row, i) => row.map((v, j) => (j === k ? rhs[i] : v)))) / D)
}
const center = computed(() => {
  const C = cons.value
  let best = null
  for (let i = 0; i < C.length; i++) for (let j = i + 1; j < C.length; j++) for (let k = j + 1; k < C.length; k++) {
    const rows = [C[i], C[j], C[k]]
    const sol = solve3(rows.map(c => [c.a[0], c.a[1], norm(c.a)]), rows.map(c => c.b))
    if (!sol || sol[2] < -1e-9) continue
    const ok = C.every(c => dot(c.a, sol) + sol[2] * norm(c.a) <= c.b + 1e-7)
    if (ok && (!best || sol[2] > best.r + 1e-12)) best = { x: [sol[0], sol[1]], r: sol[2] }
  }
  return best
})
const active = computed(() => {
  const s = center.value
  if (!s) return []
  return cons.value.map((c, i) => (Math.abs(dot(c.a, s.x) + s.r * norm(c.a) - c.b) < 1e-6 ? i : -1)).filter(i => i >= 0)
})
// Đa giác khả thi: cắt một hình vuông lớn bởi từng nửa mặt phẳng (thuật toán Sutherland–Hodgman).
const polygon = computed(() => {
  let poly = [[-10, -10], [10, -10], [10, 10], [-10, 10]]
  for (const c of cons.value) {
    const out = [], val = (p) => dot(c.a, p) - c.b
    for (let i = 0; i < poly.length; i++) {
      const p = poly[i], q = poly[(i + 1) % poly.length], vp = val(p), vq = val(q)
      if (vp <= 0) out.push(p)
      if ((vp < 0 && vq > 0) || (vp > 0 && vq < 0)) { const t = vp / (vp - vq); out.push([p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])]) }
    }
    poly = out
    if (!poly.length) break
  }
  return poly
})
const centroid = computed(() => {
  const V = polygon.value
  if (V.length < 3) return null
  let A = 0, cx = 0, cy = 0
  for (let i = 0; i < V.length; i++) {
    const [x0, y0] = V[i], [x1, y1] = V[(i + 1) % V.length], cr = x0 * y1 - x1 * y0
    A += cr; cx += (x0 + x1) * cr; cy += (y0 + y1) * cr
  }
  return Math.abs(A) < 1e-12 ? null : { x: [cx / (3 * A), cy / (3 * A)], area: Math.abs(A) / 2 }
})

const view = ref(makeView({ x0: -1, x1: 5, y0: -1, y1: 4.6, width: 460, height: 429 }))
const svg = ref(null)
const P = (p) => [view.value.sx(p[0]), view.value.sy(p[1])]
// Tay nắm của ràng buộc i: chân đường vuông góc hạ từ tâm (hoặc từ điểm tham chiếu) xuống cạnh i.
const ref0 = computed(() => (center.value ? center.value.x : [1.5, 1.5]))
const handle = (i) => {
  const c = cons.value[i], n2 = dot(c.a, c.a), s = (c.b - dot(c.a, ref0.value)) / n2
  return [ref0.value[0] + s * c.a[0], ref0.value[1] + s * c.a[1]]
}
const drag = createDragger(svg, view, (name, p) => {
  const i = Number(name.slice(1)), c = cons.value[i]
  cons.value = cons.value.map((cc, k) => (k === i ? { ...cc, b: Math.round(dot(c.a, p) * 100) / 100 } : cc))
}, { step: 0.1 })
const lineEnds = (c) => {
  const n2 = dot(c.a, c.a), base = [(c.b * c.a[0]) / n2, (c.b * c.a[1]) / n2], t = [-c.a[1], c.a[0]], L = 30 / Math.sqrt(n2)
  return [P([base[0] - L * t[0], base[1] - L * t[1]]), P([base[0] + L * t[0], base[1] + L * t[1]])]
}
// Viết ràng buộc thành chữ: bỏ hệ số 0, không viết hệ số ±1.
const label = (c) => {
  const parts = [[c.a[0], 'x₁'], [c.a[1], 'x₂']].filter(([k]) => k !== 0)
  const text = parts.map(([k, name], i) => {
    const mag = Math.abs(k) === 1 ? name : `${Math.abs(k)}${name}`
    return i === 0 ? (k < 0 ? `−${mag}` : mag) : (k < 0 ? ` − ${mag}` : ` + ${mag}`)
  }).join('')
  return `${text} ≤ ${fmt(c.b, 2)}`
}
</script>

<template>
  <figure class="study-lab" aria-label="Tâm Chebyshev của một đa giác">
    <p class="lab-title">Hình tròn lớn nhất nằm trong đa giác</p>
    <p class="lab-lead">Kéo các chấm tròn để dịch từng cạnh song song với chính nó. Hình tròn lớn nhất nằm trong đa giác là nghiệm của một LP ba biến: hai tọa độ của tâm và bán kính.</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Đa giác khả thi, các đường ràng buộc, hình tròn lớn nhất và tâm Chebyshev" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <line v-for="t in [0, 1, 2, 3, 4]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="t in [0, 1, 2, 3, 4]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line v-for="(c, i) in cons" :key="`l${i}`" :x1="lineEnds(c)[0][0]" :y1="lineEnds(c)[0][1]" :x2="lineEnds(c)[1][0]" :y2="lineEnds(c)[1][1]" :class="active.includes(i) ? 'lab-warn' : 'lab-guide'" />
      <polygon v-if="polygon.length >= 3" :points="polygon.map(p => P(p).join(',')).join(' ')" class="lab-region" />
      <template v-if="center">
        <circle :cx="P(center.x)[0]" :cy="P(center.x)[1]" :r="center.r * (view.sx(1) - view.sx(0))" class="lab-good-fill" style="opacity: 0.75" />
        <circle :cx="P(center.x)[0]" :cy="P(center.x)[1]" r="5" class="lab-dot" />
      </template>
      <circle v-if="showCentroid && centroid" :cx="P(centroid.x)[0]" :cy="P(centroid.x)[1]" r="6" class="lab-dot-hollow" />
      <circle v-for="(c, i) in cons" :key="`h${i}`" :cx="P(handle(i))[0]" :cy="P(handle(i))[1]" r="9" class="lab-handle" tabindex="0" role="slider" :aria-label="`Cạnh ${i + 1}: ${label(c)}`" :aria-valuetext="`b = ${fmt(c.b, 2)}`" @pointerdown="drag.start(`c${i}`, $event)" @keydown="drag.key(`c${i}`, handle(i), $event)" />
    </svg>
    <p class="lab-legend"><span class="legend-accent">đa giác khả thi</span><span class="legend-good">hình tròn lớn nhất</span><span class="legend-warn">ràng buộc chặt</span><span class="legend-guide">ràng buộc còn dư</span></p>
    <div class="lab-controls">
      <label class="lab-check"><input v-model="showCentroid" type="checkbox" /> Hiện trọng tâm của đa giác</label>
    </div>
    <div class="lab-buttons"><button type="button" @click="cons = DEFAULT.map(c => ({ ...c }))">Khôi phục đa giác ban đầu</button></div>
    <div class="lab-readout" role="status">
      <p v-if="!center" class="is-bad">Các ràng buộc mâu thuẫn: đa giác rỗng, LP bất khả thi.</p>
      <template v-else>
        <p>Tâm Chebyshev x_c = {{ fmtPoint(center.x, 3) }}, bán kính r = <span class="is-accent">{{ fmt(center.r, 3) }}</span>.</p>
        <p>Ràng buộc chặt: {{ active.map(i => `(${i + 1}) ${label(cons[i])}`).join(', ') }}. Hình tròn tiếp xúc đúng các cạnh này, còn các cạnh khác có thể dịch mà không đổi nghiệm, chừng nào chúng chưa chạm hình tròn.</p>
        <p v-if="showCentroid && centroid">Trọng tâm diện tích {{ fmtPoint(centroid.x, 3) }} nói chung khác tâm Chebyshev: tâm Chebyshev là điểm nằm sâu nhất, xa biên nhất, chứ không phải điểm cân bằng của diện tích.</p>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Đếm số cạnh mà hình tròn chạm. Vì sao trong mặt phẳng, thường có đúng ba cạnh chạm?</li>
        <li>Kéo một cạnh đang màu xám (còn dư) vào trong. Nghiệm có đổi không cho tới khi cạnh ấy chạm hình tròn?</li>
        <li>Kéo hai cạnh (3) và (4) ra xa. Hình tròn lớn lên tới đâu, và từ lúc nào ràng buộc (5) bắt đầu chặt?</li>
        <li>Bật trọng tâm. Tìm một hình dạng làm trọng tâm và tâm Chebyshev cách xa nhau.</li>
      </ol>
    </details>
  </figure>
</template>
