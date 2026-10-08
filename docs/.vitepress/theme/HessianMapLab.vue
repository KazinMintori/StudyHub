<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { contourSegments } from './contour.mjs'
import { eigSym2 } from './convex-geometry.mjs'

// Bản đồ Hessian: tô đỏ những ô mà ∇²f không nửa xác định dương. Hàm hai biến khả vi hai lần
// trên miền lồi là lồi khi và chỉ khi vùng đỏ rỗng. Tại điểm x kéo được, hai vạch là hai hướng riêng,
// dài theo độ lớn của trị riêng, xanh khi cong lên, đỏ khi cong xuống, nét đứt khi độ cong bằng 0.
const catalog = {
  quad: { label: 'x₁² + x₁x₂ + 2x₂²', f: ([a, b]) => a * a + a * b + 2 * b * b, hess: () => [2, 1, 4], levels: [0.5, 1.5, 3, 5, 8] },
  lse: { label: 'log(e^x₁ + e^x₂)', f: ([a, b]) => Math.log(Math.exp(a) + Math.exp(b)), hess: ([a, b]) => { const p = Math.exp(a) / (Math.exp(a) + Math.exp(b)), s = p * (1 - p); return [s, -s, s] }, levels: [-1, 0, 1, 2, 3] },
  qol: { label: 'x₁²/x₂ (x₂ > 0)', f: ([a, b]) => (b > 0 ? (a * a) / b : NaN), hess: ([a, b]) => [2 / b, (-2 * a) / (b * b), (2 * a * a) / b ** 3], dom: ([, b]) => b > 0, levels: [0.25, 1, 2, 4] },
  well: { label: '(x₁² − 1)² + x₂²', f: ([a, b]) => (a * a - 1) ** 2 + b * b, hess: ([a]) => [12 * a * a - 4, 0, 2], levels: [0.2, 0.6, 1, 2, 4] },
  bumpy: { label: '0.4(x₁² + x₂²) + cos(2x₁)', f: ([a, b]) => 0.4 * (a * a + b * b) + Math.cos(2 * a), hess: ([a]) => [0.8 - 4 * Math.cos(2 * a), 0, 0.8], levels: [0, 0.5, 1, 2, 3] },
  saddle: { label: 'x₁² + 3x₁x₂ + x₂²', f: ([a, b]) => a * a + 3 * a * b + b * b, hess: () => [2, 3, 2], levels: [-4, -1, 1, 4] }
}
const choice = ref('well')
const fn = computed(() => catalog[choice.value])
const inDom = p => (fn.value.dom ? fn.value.dom(p) : true)
const uid = useId()
const clip = `${uid}-hess-clip`
const svg = ref(null)
const view = ref(makeView({ x0: -3, x1: 3, y0: -3, y1: 3, width: 360, height: 360 }))
const P = p => view.value.point(p)
const state = ref({ x: [0.3, 1] })
const drag = createDragger(svg, view, (name, value) => { state.value = { ...state.value, [name]: value } }, { step: 0.1, snap: 0.05 })
const x = computed(() => state.value.x)
const contours = computed(() => fn.value.levels.map(level => contourSegments(fn.value.f, { x0: -3, x1: 3, y0: -3, y1: 3, n: 80 }, level)))
const notPsd = ([p, q, r]) => { const tol = 1e-9 * (1 + Math.abs(p * r) + q * q); return p < -tol || r < -tol || p * r - q * q < -tol }
// Gộp các ô đỏ liền nhau trên cùng một hàng thành một hình chữ nhật để giảm số phần tử SVG.
const N = 60
const badRects = computed(() => {
  const h = 6 / N, out = []
  for (let j = 0; j < N; j++) {
    let start = null
    for (let i = 0; i <= N; i++) {
      const c = [-3 + (i + 0.5) * h, -3 + (j + 0.5) * h]
      const bad = i < N && inDom(c) && notPsd(fn.value.hess(c))
      if (bad && start === null) start = i
      if (!bad && start !== null) { out.push({ x0: -3 + start * h, x1: -3 + i * h, y0: -3 + j * h, y1: -3 + (j + 1) * h }); start = null }
    }
  }
  return out
})
const outside = computed(() => {
  if (!fn.value.dom) return []
  const h = 6 / N, out = []
  for (let j = 0; j < N; j++) { const c = [0, -3 + (j + 0.5) * h]; if (!fn.value.dom(c)) out.push({ y0: -3 + j * h, y1: -3 + (j + 1) * h }) }
  return out
})
const here = computed(() => (inDom(x.value) ? fn.value.hess(x.value) : null))
const eig = computed(() => (here.value ? eigSym2(...here.value) : null))
const tol = 1e-6
const sign = l => (l > tol ? 'lab-good' : l < -tol ? 'lab-bad' : 'lab-guide')
const crosses = computed(() => {
  if (!eig.value) return []
  return eig.value.values.map((l, k) => {
    const v = eig.value.vectors[k], s = 0.25 + 0.18 * Math.min(Math.abs(l), 6)
    return { a: [x.value[0] - s * v[0], x.value[1] - s * v[1]], b: [x.value[0] + s * v[0], x.value[1] + s * v[1]], cls: sign(l) }
  })
})
const shape = computed(() => {
  if (!eig.value) return ''
  const [l1, l2] = eig.value.values
  if (l2 > tol) return 'Hessian xác định dương: quanh x, đồ thị cong lên theo mọi hướng, như đáy một cái bát.'
  if (l2 >= -tol && l1 > tol) return `Hessian nửa xác định dương nhưng suy biến: theo hướng ${fmtPoint(eig.value.vectors[1])}, độ cong bằng 0, đồ thị có dạng một cái máng.`
  if (l1 > tol && l2 < -tol) return `Hessian không xác định: cong lên theo hướng ${fmtPoint(eig.value.vectors[0])}, cong xuống theo hướng ${fmtPoint(eig.value.vectors[1])}, như một cái yên ngựa.`
  if (l1 < -tol) return 'Hessian xác định âm: quanh x, đồ thị cong xuống theo mọi hướng, như một cái bát úp.'
  return 'Hessian gần bằng 0 hoặc chỉ cong xuống theo một hướng tại x.'
})
</script>

<template>
  <figure class="study-lab" aria-label="Bản đồ những điểm mà Hessian không nửa xác định dương">
    <p class="lab-title">Tính lồi hỏng ở đâu: bản đồ Hessian</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Đường đồng mức, vùng Hessian không nửa xác định dương và hai hướng riêng tại x" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs><clipPath :id="clip"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath></defs>
      <g :clip-path="`url(#${clip})`">
        <rect v-for="(r, i) in outside" :key="`o${i}`" x="0" :y="view.sy(r.y1)" :width="view.width" :height="view.sy(r.y0) - view.sy(r.y1)" class="lab-grid" style="fill: var(--rule); opacity: 0.5" />
        <rect v-for="(r, i) in badRects" :key="`b${i}`" :x="view.sx(r.x0)" :y="view.sy(r.y1)" :width="view.sx(r.x1) - view.sx(r.x0)" :height="view.sy(r.y0) - view.sy(r.y1) + 0.5" class="lab-bad-fill" style="stroke: none; opacity: 0.9" />
        <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
        <g v-for="(segs, k) in contours" :key="`c${k}`">
          <line v-for="(s, i) in segs" :key="i" :x1="P(s[0])[0]" :y1="P(s[0])[1]" :x2="P(s[1])[0]" :y2="P(s[1])[1]" class="lab-line" style="stroke-width: 1.3; opacity: 0.6" />
        </g>
        <line v-for="(c, i) in crosses" :key="`x${i}`" :x1="P(c.a)[0]" :y1="P(c.a)[1]" :x2="P(c.b)[0]" :y2="P(c.b)[1]" :class="c.cls" style="stroke-width: 4" />
        <circle :cx="P(x)[0]" :cy="P(x)[1]" r="8" class="lab-handle" tabindex="0" role="slider" aria-label="Điểm x" :aria-valuetext="fmtPoint(x)" @pointerdown="drag.start('x', $event)" @keydown="drag.key('x', x, $event)" />
      </g>
    </svg>
    <p class="lab-legend"><span class="legend-bad">vùng Hessian có trị riêng âm</span><span class="legend-good">hướng cong lên</span><span class="legend-guide">hướng có độ cong 0</span></p>
    <div class="lab-controls">
      <label>Hàm f = <select v-model="choice"><option v-for="(item, key) in catalog" :key="key" :value="key">{{ item.label }}</option></select></label>
    </div>
    <div class="lab-readout" role="status">
      <p v-if="!here" class="is-bad">x = {{ fmtPoint(x) }} nằm ngoài miền xác định (phần tô xám).</p>
      <template v-else>
        <p>Tại x = {{ fmtPoint(x) }}: ∇²f(x) = [[{{ fmt(here[0], 2) }}, {{ fmt(here[1], 2) }}], [{{ fmt(here[1], 2) }}, {{ fmt(here[2], 2) }}]], hai trị riêng {{ fmt(eig.values[0], 3) }} và {{ fmt(eig.values[1], 3) }}.</p>
        <p>{{ shape }}</p>
      </template>
      <p v-if="badRects.length" class="is-bad">Trong khung nhìn có những điểm mà Hessian có trị riêng âm (vùng đỏ). Chỉ cần một điểm như vậy, hàm đã không lồi.</p>
      <p v-else class="is-good">Trong khung nhìn, Hessian nửa xác định dương tại mọi điểm của miền xác định, đúng như điều kiện bậc hai đòi hỏi.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Với (x₁² − 1)² + x₂², dải đỏ nằm giữa hai đường thẳng đứng nào? Tính 12x₁² − 4 để kiểm tra.</li>
        <li>Với x₁²/x₂, kéo x đi khắp nửa mặt phẳng trên. Hướng có độ cong bằng 0 luôn chỉ về đâu so với gốc tọa độ?</li>
        <li>Với log(e^x₁ + e^x₂), hướng có độ cong bằng 0 là hướng nào? Kết quả này khớp với điều gì đã thấy ở chủ đề hàm lồi?</li>
        <li>Với x₁² + 3x₁x₂ + x₂², vì sao cả khung đều đỏ dù hai phần tử trên đường chéo của Hessian đều dương?</li>
      </ol>
    </details>
  </figure>
</template>
