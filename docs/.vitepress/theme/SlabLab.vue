<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { polyhedronInBox } from './convex-geometry.mjs'
const clipId = `${useId()}-clip`

// Ví dụ 2.8 với m = 2: S = {x ∈ R² : |x₁ cos t + x₂ cos 2t| ≤ 1 với mọi |t| ≤ π/3}.
// Hình trái: các dải {x : |x₁ cos t + x₂ cos 2t| ≤ 1} và giao của chúng. Hình phải: đa thức p_x(t) của điểm x đang chọn.
const svg = ref(null)
const view = ref(makeView({ x0: -2.2, x1: 2.2, y0: -2.2, y1: 2.2, width: 300, height: 300 }))
const P = p => view.value.point(p)
const pt = ref({ x: [0.5, 0.5] })
const drag = createDragger(svg, view, (name, value) => { pt.value = { ...pt.value, [name]: value } }, { step: 0.05, snap: 0.05 })
const showCount = ref(10)
const tMax = Math.PI / 3
const fine = Array.from({ length: 121 }, (_, k) => (k / 120) * tMax)
const coef = t => [Math.cos(t), Math.cos(2 * t)]
// Giao của 121 dải: xấp xỉ S từ bên ngoài, đủ mịn để vẽ.
const region = computed(() => polyhedronInBox(fine.flatMap(t => { const a = coef(t); return [{ a, b: 1 }, { a: [-a[0], -a[1]], b: 1 }] }), [view.value.x0, view.value.x1, view.value.y0, view.value.y1]))
const shown = computed(() => Array.from({ length: showCount.value }, (_, k) => (showCount.value === 1 ? 0 : (k / (showCount.value - 1)) * tMax)))
function slabLines(t) {
  const [c1, c2] = coef(t), n2 = c1 * c1 + c2 * c2, d = [-c2, c1]
  return [1, -1].map(side => { const base = [(side * c1) / n2, (side * c2) / n2]; return [[base[0] - 9 * d[0], base[1] - 9 * d[1]], [base[0] + 9 * d[0], base[1] + 9 * d[1]]] })
}
const px = t => pt.value.x[0] * Math.cos(t) + pt.value.x[1] * Math.cos(2 * t)
const worst = computed(() => fine.reduce((best, t) => (Math.abs(px(t)) > Math.abs(px(best)) ? t : best), 0))
const inS = computed(() => Math.abs(px(worst.value)) <= 1 + 1e-9)
// Khung bên phải: t từ 0 tới π, p từ −2.5 tới 2.5.
const plot = { x: 320, w: 300, h: 300 }
const sxT = t => plot.x + (t / Math.PI) * plot.w
const syP = v => plot.h / 2 - (v / 2.5) * (plot.h / 2 - 10)
const curve = computed(() => Array.from({ length: 121 }, (_, k) => { const t = (k / 120) * Math.PI; return `${sxT(t)},${syP(Math.max(-2.5, Math.min(2.5, px(t))))}` }).join(' '))
</script>

<template>
  <figure class="study-lab" aria-label="Giao vô hạn các dải trong ví dụ đa thức lượng giác">
    <p class="lab-title">Mỗi giá trị t cho một dải, và S là giao của tất cả</p>
    <svg ref="svg" viewBox="0 0 640 300" role="img" aria-label="Bên trái các dải và tập S, bên phải đồ thị đa thức lượng giác của điểm đang chọn" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs><clipPath :id="clipId"><rect x="0" y="0" width="300" height="300" /></clipPath></defs>
      <g :clip-path="`url(#${clipId})`">
        <line :x1="0" x2="300" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" y2="300" class="lab-axis" />
        <polygon v-if="region.length >= 3" :points="region.map(p => P(p).join(',')).join(' ')" class="lab-region" />
        <g v-for="t in shown" :key="t">
          <line v-for="(seg, i) in slabLines(t)" :key="i" :x1="P(seg[0])[0]" :y1="P(seg[0])[1]" :x2="P(seg[1])[0]" :y2="P(seg[1])[1]" class="lab-guide" />
        </g>
        <circle :cx="P(pt.x)[0]" :cy="P(pt.x)[1]" r="8" :class="inS ? 'lab-handle' : 'lab-handle lab-handle-alt'" tabindex="0" role="slider" aria-label="Điểm x = (x₁, x₂)" @pointerdown="drag.start('x', $event)" @keydown="drag.key('x', pt.x, $event)" />
      </g>
      <text x="8" y="18" class="lab-small">x₂</text><text x="280" :y="view.sy(0) - 6" class="lab-small">x₁</text>
      <rect :x="plot.x" y="0" :width="plot.w" :height="plot.h" class="lab-region-soft" style="opacity: 0.25" />
      <rect :x="sxT(0)" :y="syP(1)" :width="sxT(tMax) - sxT(0)" :height="syP(-1) - syP(1)" class="lab-region-soft" />
      <line :x1="plot.x" :x2="plot.x + plot.w" :y1="syP(0)" :y2="syP(0)" class="lab-axis" />
      <line :x1="plot.x" :x2="plot.x + plot.w" :y1="syP(1)" :y2="syP(1)" class="lab-guide" />
      <line :x1="plot.x" :x2="plot.x + plot.w" :y1="syP(-1)" :y2="syP(-1)" class="lab-guide" />
      <line :x1="sxT(tMax)" :x2="sxT(tMax)" y1="0" y2="300" class="lab-guide" />
      <polyline :points="curve" :class="inS ? 'lab-accent' : 'lab-bad'" />
      <circle :cx="sxT(worst)" :cy="syP(Math.max(-2.5, Math.min(2.5, px(worst))))" r="5" class="lab-dot-warn" />
      <text :x="sxT(tMax) + 4" y="16" class="lab-small">t = π/3</text>
      <text :x="plot.x + plot.w - 18" :y="syP(0) + 16" class="lab-small">π</text>
      <text :x="plot.x + 4" :y="syP(1) - 4" class="lab-small">1</text>
      <text :x="plot.x + 4" :y="syP(-1) + 14" class="lab-small">−1</text>
    </svg>
    <div class="lab-controls">
      <label>Số dải được vẽ: {{ showCount }}<input v-model.number="showCount" type="range" min="1" max="20" step="1" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p>x = {{ fmtPoint(pt.x) }} cho p_x(t) = {{ fmt(pt.x[0]) }}cos t + {{ fmt(pt.x[1]) }}cos 2t. Trên đoạn |t| ≤ π/3, giá trị tuyệt đối lớn nhất là {{ fmt(Math.abs(px(worst)), 3) }}, đạt tại t ≈ {{ fmt(worst, 3) }}.</p>
      <p v-if="inS"><span class="is-good">x thuộc S:</span> đồ thị nằm trong dải [−1, 1] trên toàn đoạn được tô.</p>
      <p v-else><span class="is-bad">x không thuộc S:</span> đồ thị vượt ra khỏi dải [−1, 1] tại điểm vàng, nên x vi phạm ràng buộc ứng với t đó.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Tăng số dải từ 1 lên 20 và quan sát giao của chúng hình thành dần.</li>
        <li>Kéo x tới (1, 1). Đồ thị vượt ngưỡng ở đâu?</li>
        <li>Đặt x ở hai điểm khác nhau trong S, rồi ở trung điểm của chúng. Đa thức của trung điểm có quan hệ gì với hai đa thức kia?</li>
      </ol>
    </details>
  </figure>
</template>
