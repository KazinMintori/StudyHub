<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { contourSegments } from './contour.mjs'
import { polyhedronInBox, dot } from './convex-geometry.mjs'

// Một gradient tại x chia mặt phẳng làm hai nửa. Với hàm lồi khả vi, mọi điểm tốt hơn x
// nằm trong nửa {y : ∇f(x)ᵀ(y − x) < 0}, nên nửa còn lại bị loại bỏ chỉ sau một lần tính gradient.
const catalog = {
  quad: { label: 'x₁² + x₁x₂ + 2x₂²', convex: true, f: ([a, b]) => a * a + a * b + 2 * b * b, grad: ([a, b]) => [2 * a + b, a + 4 * b], levels: [0.5, 1.5, 3, 5, 8] },
  lse3: { label: 'log(e^x₁ + e^x₂ + e^(−x₁−x₂))', convex: true, f: ([a, b]) => Math.log(Math.exp(a) + Math.exp(b) + Math.exp(-a - b)), grad: ([a, b]) => { const s = Math.exp(a) + Math.exp(b) + Math.exp(-a - b), r = Math.exp(-a - b) / s; return [Math.exp(a) / s - r, Math.exp(b) / s - r] }, levels: [1.3, 1.8, 2.5, 3.3] },
  bumpy: { label: '0.4(x₁² + x₂²) + cos(2x₁)', convex: false, f: ([a, b]) => 0.4 * (a * a + b * b) + Math.cos(2 * a), grad: ([a, b]) => [0.8 * a - 2 * Math.sin(2 * a), 0.8 * b], levels: [0, 0.5, 1, 2, 3] },
  ring: { label: '(x₁² + x₂² − 2)²', convex: false, f: ([a, b]) => (a * a + b * b - 2) ** 2, grad: ([a, b]) => { const k = 4 * (a * a + b * b - 2); return [k * a, k * b] }, levels: [0.1, 0.5, 1.5, 4] },
  gauss: { label: '−exp(−x₁² − 2x₂²)', convex: false, quasi: true, f: ([a, b]) => -Math.exp(-a * a - 2 * b * b), grad: ([a, b]) => { const e = Math.exp(-a * a - 2 * b * b); return [2 * a * e, 4 * b * e] }, levels: [-0.9, -0.7, -0.5, -0.3, -0.1] }
}
const choice = ref('quad')
const fn = computed(() => catalog[choice.value])
const uid = useId()
const svg = ref(null)
const view = ref(makeView({ x0: -3, x1: 3, y0: -3, y1: 3, width: 360, height: 360 }))
const P = p => view.value.point(p)
const state = ref({ x: [1.5, 1] })
const drag = createDragger(svg, view, (name, value) => { state.value = { ...state.value, [name]: value } }, { step: 0.1, snap: 0.05 })
const x = computed(() => state.value.x)
const fx = computed(() => fn.value.f(x.value))
const g = computed(() => fn.value.grad(x.value))
const gNorm = computed(() => Math.hypot(...g.value))
// degenerate: gradient đúng bằng 0, không còn hướng để vẽ. stationary: gradient nhỏ tới mức coi như bằng 0.
const degenerate = computed(() => gNorm.value < 1e-12)
const stationary = computed(() => gNorm.value < 1e-3)
const box = [-3, 3, -3, 3]
const grid = ({ x0, x1, y0, y1 }) => ({ x0, x1, y0, y1, n: 80 })
const contours = computed(() => fn.value.levels.map(level => contourSegments(fn.value.f, grid(view.value), level)))
const ownLevel = computed(() => contourSegments(fn.value.f, grid(view.value), fx.value))
// Nửa mặt phẳng bị loại: ∇f(x)ᵀ(y − x) ≥ 0, viết thành (−∇f(x))ᵀ y ≤ −∇f(x)ᵀ x.
const unit = computed(() => (degenerate.value ? [0, 0] : [g.value[0] / gNorm.value, g.value[1] / gNorm.value]))
const cutRegion = computed(() => (degenerate.value ? [] : polyhedronInBox([{ a: [-unit.value[0], -unit.value[1]], b: -dot(unit.value, x.value) }], box)))
const cutLine = computed(() => {
  if (degenerate.value) return null
  const u = [-unit.value[1], unit.value[0]]
  return [[x.value[0] - 9 * u[0], x.value[1] - 9 * u[1]], [x.value[0] + 9 * u[0], x.value[1] + 9 * u[1]]]
})
const arrowTip = computed(() => [x.value[0] + 0.9 * unit.value[0], x.value[1] + 0.9 * unit.value[1]])
// Tìm trên lưới những điểm tốt hơn x mà lại nằm trong nửa mặt phẳng bị loại.
const violators = computed(() => {
  if (degenerate.value) return []
  const out = []
  for (let i = 0; i <= 40; i++) for (let j = 0; j <= 40; j++) {
    const y = [-3 + (6 * i) / 40, -3 + (6 * j) / 40]
    if (dot(unit.value, [y[0] - x.value[0], y[1] - x.value[1]]) >= 0 && fn.value.f(y) < fx.value - 1e-6) out.push(y)
  }
  return out
})
const arrow = `${uid}-cut-arrow`
const clip = `${uid}-cut-clip`
</script>

<template>
  <figure class="study-lab" aria-label="Gradient tại một điểm loại bỏ nửa mặt phẳng">
    <p class="lab-title">Một gradient loại bỏ nửa mặt phẳng</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Đường đồng mức, điểm x, gradient tại x và nửa mặt phẳng bị loại" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs>
        <marker :id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="lab-arrow-accent" /></marker>
        <clipPath :id="clip"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath>
      </defs>
      <g :clip-path="`url(#${clip})`">
        <polygon v-if="cutRegion.length" :points="cutRegion.map(p => P(p).join(',')).join(' ')" class="lab-bad-fill" style="stroke: none; opacity: 0.9" />
        <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
        <g v-for="(segs, k) in contours" :key="`c${k}`">
          <line v-for="(s, i) in segs" :key="i" :x1="P(s[0])[0]" :y1="P(s[0])[1]" :x2="P(s[1])[0]" :y2="P(s[1])[1]" class="lab-line" style="stroke-width: 1.2; opacity: 0.55" />
        </g>
        <line v-for="(s, i) in ownLevel" :key="`o${i}`" :x1="P(s[0])[0]" :y1="P(s[0])[1]" :x2="P(s[1])[0]" :y2="P(s[1])[1]" class="lab-warn" />
        <line v-if="cutLine" :x1="P(cutLine[0])[0]" :y1="P(cutLine[0])[1]" :x2="P(cutLine[1])[0]" :y2="P(cutLine[1])[1]" class="lab-guide" />
        <circle v-for="(y, i) in violators" :key="`v${i}`" :cx="P(y)[0]" :cy="P(y)[1]" r="3" class="lab-dot-bad" />
        <line v-if="!degenerate" :x1="P(x)[0]" :y1="P(x)[1]" :x2="P(arrowTip)[0]" :y2="P(arrowTip)[1]" class="lab-accent" :marker-end="`url(#${arrow})`" />
        <circle :cx="P(x)[0]" :cy="P(x)[1]" r="9" class="lab-handle" tabindex="0" role="slider" aria-label="Điểm x" :aria-valuetext="fmtPoint(x)" @pointerdown="drag.start('x', $event)" @keydown="drag.key('x', x, $event)" />
      </g>
    </svg>
    <p class="lab-legend"><span class="legend-warn">đường mức qua x</span><span class="legend-accent">hướng ∇f(x)</span><span class="legend-guide">đường vuông góc với gradient</span><span class="legend-bad">nửa mặt phẳng bị loại</span></p>
    <div class="lab-controls">
      <label>Hàm f = <select v-model="choice"><option v-for="(item, key) in catalog" :key="key" :value="key">{{ item.label }}</option></select></label>
    </div>
    <div class="lab-readout" role="status">
      <p>x = {{ fmtPoint(x) }}, f(x) = {{ fmt(fx, 3) }}, ∇f(x) = {{ fmtPoint(g, 3) }}.</p>
      <p v-if="stationary && fn.convex">Gradient bằng 0 (hoặc gần như bằng 0) tại x. Với hàm lồi, điểm có gradient bằng 0 là một điểm cực tiểu toàn cục.</p>
      <p v-else-if="stationary && fn.quasi" class="is-bad">Gradient gần như bằng 0, dù x còn rất xa điểm cực tiểu tại gốc. Xa gốc, hàm gần như phẳng, giống vùng bão hòa của hàm sigmoid, nên gradient hầu như không còn chỉ đường.</p>
      <p v-else-if="stationary" class="is-bad">Gradient bằng 0 (hoặc gần như bằng 0) tại x, nhưng hàm không lồi nên điều đó không bảo đảm x là cực tiểu. Hãy so f(x) với các đường mức xung quanh.</p>
      <p v-if="!degenerate && violators.length" class="is-bad">Có những điểm tốt hơn x nằm ngay trong nửa mặt phẳng tô đỏ (chấm đỏ). Với hàm không lồi, một gradient không đủ để loại bỏ nửa mặt phẳng.</p>
      <p v-else-if="!degenerate" class="is-good">Mọi điểm y có f(y) &lt; f(x) đều nằm ở phía ∇f(x)ᵀ(y − x) &lt; 0. Chỉ một lần tính gradient đã loại được cả nửa mặt phẳng tô đỏ.</p>
      <p v-if="fn.quasi && !degenerate && !violators.length">Hàm này không lồi, vậy mà phép loại vẫn đúng: điều được dùng thật sự là mọi tập mức dưới của nó đều lồi.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Với hàm bậc hai, kéo x đi khắp khung. Đường nét đứt luôn tiếp xúc với đường mức màu vàng tại x, và đường mức nằm trọn một phía của nó.</li>
        <li>Với (x₁² + x₂² − 2)², đặt x bên trong vòng tròn bán kính √2. Vì sao nửa mặt phẳng bị loại lại chứa những điểm tốt hơn x?</li>
        <li>Với 0.4(x₁² + x₂²) + cos(2x₁), tìm một điểm x có chấm đỏ và một điểm không có.</li>
        <li>Với −exp(−x₁² − 2x₂²), hàm không lồi nhưng không bao giờ có chấm đỏ. Hãy giải thích bằng hình dạng các đường mức.</li>
      </ol>
    </details>
  </figure>
</template>
