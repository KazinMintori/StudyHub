<script setup>
import { computed, ref, useId } from 'vue'
import { makeView } from './svg-drag'

// Thử quy tắc hợp hàm f(x) = h(g(x)). Quy tắc chỉ là điều kiện đủ: lab so sánh điều quy tắc
// dự đoán với hình dạng thật của f trên khung nhìn (kiểm bằng sai phân bậc hai trên lưới).
// mono: chiều đơn điệu của mở rộng giá trị h̃ trên toàn trục số ('inc', 'dec' hoặc 'none').
const hs = {
  exp: { label: 'eᵘ', f: u => Math.exp(u), dom: () => true, curv: 'convex', mono: 'inc', note: 'lồi và không giảm' },
  sq: { label: 'u²', f: u => u * u, dom: () => true, curv: 'convex', mono: 'none', note: 'lồi nhưng không đơn điệu' },
  sqplus: { label: 'max{u, 0}²', f: u => Math.max(u, 0) ** 2, dom: () => true, curv: 'convex', mono: 'inc', note: 'lồi và không giảm' },
  inv: { label: '1/u (u > 0)', f: u => 1 / u, dom: u => u > 0, curv: 'convex', mono: 'dec', note: 'lồi, mở rộng giá trị không tăng' },
  neglog: { label: '−log u (u > 0)', f: u => -Math.log(u), dom: u => u > 0, curv: 'convex', mono: 'dec', note: 'lồi, mở rộng giá trị không tăng' },
  pow32: { label: 'u^(3/2) (u ≥ 0)', f: u => u ** 1.5, dom: u => u >= 0, curv: 'convex', mono: 'none', note: 'lồi và tăng trên miền của nó, nhưng mở rộng giá trị không đơn điệu' },
  log: { label: 'log u (u > 0)', f: u => Math.log(u), dom: u => u > 0, curv: 'concave', mono: 'inc', note: 'lõm, mở rộng giá trị không giảm' },
  sqrt: { label: '√u (u ≥ 0)', f: u => Math.sqrt(u), dom: u => u >= 0, curv: 'concave', mono: 'inc', note: 'lõm, mở rộng giá trị không giảm' }
}
const gs = {
  sq: { label: 'x²', f: x => x * x, curv: 'convex' },
  abs: { label: '|x|', f: x => Math.abs(x), curv: 'convex' },
  sqm1: { label: 'x² − 1', f: x => x * x - 1, curv: 'convex' },
  exp: { label: 'eˣ', f: x => Math.exp(x), curv: 'convex' },
  lin: { label: '2x + 1', f: x => 2 * x + 1, curv: 'affine' },
  cap: { label: '4 − x²', f: x => 4 - x * x, curv: 'concave' },
  tent: { label: '3 − |x|', f: x => 3 - Math.abs(x), curv: 'concave' }
}
const hKey = ref('exp'), gKey = ref('sq')
const h = computed(() => hs[hKey.value]), g = computed(() => gs[gKey.value])
const clip = `${useId()}-comp-clip`
const N = 400, X0 = -2.5, X1 = 2.5
const samples = computed(() => Array.from({ length: N + 1 }, (_, i) => {
  const x = X0 + ((X1 - X0) * i) / N, u = g.value.f(x)
  return { x, v: h.value.dom(u) ? h.value.f(u) : NaN }
}))
const finite = computed(() => samples.value.filter(s => Number.isFinite(s.v)))
// Miền của f trên khung có liền một khoảng không?
const domainPieces = computed(() => {
  let pieces = 0, inside = false
  for (const s of samples.value) { const ok = Number.isFinite(s.v); if (ok && !inside) pieces++; inside = ok }
  return pieces
})
const actual = computed(() => {
  if (!finite.value.length) return 'empty'
  if (domainPieces.value > 1) return 'baddomain'
  let pos = false, neg = false
  const s = samples.value
  for (let i = 1; i < s.length - 1; i++) {
    const [a, b, c] = [s[i - 1].v, s[i].v, s[i + 1].v]
    if (![a, b, c].every(Number.isFinite)) continue
    const d = a - 2 * b + c, scale = 1e-9 * (1 + Math.abs(a) + Math.abs(b) + Math.abs(c))
    if (d > scale) pos = true
    if (d < -scale) neg = true
  }
  if (pos && neg) return 'neither'
  if (neg) return 'concave'
  if (pos) return 'convex'
  return 'affine'
})
const predicted = computed(() => {
  const H = h.value, G = g.value.curv
  if (G === 'affine') return { verdict: H.curv, rule: `hợp của hàm ${H.curv === 'convex' ? 'lồi' : 'lõm'} với một hàm affine, không cần điều kiện đơn điệu` }
  if (H.curv === 'convex' && H.mono === 'inc' && G === 'convex') return { verdict: 'convex', rule: 'h lồi, h̃ không giảm, g lồi' }
  if (H.curv === 'convex' && H.mono === 'dec' && G === 'concave') return { verdict: 'convex', rule: 'h lồi, h̃ không tăng, g lõm' }
  if (H.curv === 'concave' && H.mono === 'inc' && G === 'concave') return { verdict: 'concave', rule: 'h lõm, h̃ không giảm, g lõm' }
  if (H.curv === 'concave' && H.mono === 'dec' && G === 'convex') return { verdict: 'concave', rule: 'h lõm, h̃ không tăng, g lồi' }
  return { verdict: null, rule: 'không quy tắc nào trong bốn quy tắc áp dụng được' }
})
const words = { convex: 'lồi', concave: 'lõm', affine: 'affine', neither: 'không lồi cũng không lõm', baddomain: 'không lồi vì miền xác định bị tách rời', empty: 'không xác định ở đâu trên khung nhìn' }
const yRange = computed(() => {
  const vs = finite.value.map(s => s.v).sort((a, b) => a - b)
  if (!vs.length) return [0, 1]
  const lo = vs[0], hi = vs[Math.floor(0.97 * (vs.length - 1))]
  return hi - lo < 1e-9 ? [lo - 1, hi + 1] : [lo - 0.08 * (hi - lo), hi + 0.08 * (hi - lo)]
})
const view = computed(() => makeView({ x0: X0, x1: X1, y0: yRange.value[0], y1: yRange.value[1], width: 440, height: 260 }))
const path = computed(() => {
  const segs = [[]]
  for (const s of samples.value) { if (!Number.isFinite(s.v)) { if (segs.at(-1).length) segs.push([]); continue } segs.at(-1).push(`${view.value.sx(s.x)},${view.value.sy(s.v)}`) }
  return segs.filter(s => s.length > 1).map(s => s.join(' '))
})
const agree = computed(() => predicted.value.verdict === null || predicted.value.verdict === actual.value || (actual.value === 'affine'))
</script>

<template>
  <figure class="study-lab" aria-label="Thử các quy tắc hợp hàm">
    <p class="lab-title">Quy tắc hợp hàm: dự đoán và thực tế</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" :aria-label="`Đồ thị của h(g(x)) với h = ${h.label}, g = ${g.label}`">
      <defs><clipPath :id="clip"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath></defs>
      <g :clip-path="`url(#${clip})`">
        <line v-if="yRange[0] < 0 && yRange[1] > 0" x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
        <line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
        <polyline v-for="(seg, i) in path" :key="i" :points="seg" class="lab-accent" />
      </g>
    </svg>
    <div class="lab-controls">
      <label>Hàm ngoài h(u) = <select v-model="hKey"><option v-for="(item, key) in hs" :key="key" :value="key">{{ item.label }}</option></select></label>
      <label>Hàm trong g(x) = <select v-model="gKey"><option v-for="(item, key) in gs" :key="key" :value="key">{{ item.label }}</option></select></label>
    </div>
    <div class="lab-readout" role="status">
      <p>f(x) = h(g(x)), trong đó h {{ h.note }}, còn g {{ g.curv === 'convex' ? 'lồi' : g.curv === 'concave' ? 'lõm' : 'affine' }}.</p>
      <p>Quy tắc: {{ predicted.rule }}<span v-if="predicted.verdict">, nên dự đoán f <strong>{{ words[predicted.verdict] }}</strong></span>.</p>
      <p :class="actual === 'convex' || actual === 'concave' || actual === 'affine' ? 'is-good' : 'is-bad'">Thực tế trên đoạn [−2.5, 2.5]: f {{ words[actual] }}.</p>
      <p v-if="predicted.verdict === null && (actual === 'convex' || actual === 'concave')">Không quy tắc nào áp dụng, vậy mà f vẫn {{ words[actual] }}. Quy tắc hợp hàm là điều kiện đủ, không phải điều kiện cần.</p>
      <p v-if="!agree" class="is-bad">Dự đoán và thực tế không khớp. Hãy kiểm tra lại giả thiết của quy tắc.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Chọn h = u² và g = x² − 1. Hàm hợp có dạng gì, và giả thiết nào của quy tắc bị vi phạm?</li>
        <li>Giữ h = u², đổi g thành |x|. Không quy tắc nào áp dụng, nhưng f có lồi không? Vì sao?</li>
        <li>Chọn h = u^(3/2) và g = x² − 1. Hàm h lồi và tăng trên miền của nó, g lồi, vậy mà f không lồi. Chuyện gì xảy ra với miền xác định của f?</li>
        <li>Tìm một cặp (h, g) mà quy tắc dự đoán hàm lõm.</li>
      </ol>
    </details>
  </figure>
</template>
