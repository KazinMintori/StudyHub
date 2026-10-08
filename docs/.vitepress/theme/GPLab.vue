<script setup>
import { computed, ref } from 'vue'
import { makeView, fmt, fmtPoint } from './svg-drag'

// Quy hoạch hình học (chủ đề 9, Lecture 02): cùng một tập, nhìn trong biến x > 0 và trong biến y = log x.
// Đoạn thẳng trong biến y ứng với đường "trung bình nhân" x(θ) = p^{1−θ} q^θ trong biến x.
// Ba tập tự đặt: √x₁ + √x₂ ≤ 2 (không lồi theo x), x₁x₂ = 1 (đường cong theo x, đường thẳng theo log x),
// và bài toán áp phích: phần chữ w·h ≥ 600 với tập mức (w + 4)(h + 6) ≤ 864 của hàm mục tiêu.
const presets = {
  sqrt: {
    label: '√x₁ + √x₂ ≤ 2',
    xr: [0, 4.4], yr: [0, 4.4], lr: [-3.2, 1.9],
    p: [0.16, 2.56], q: [2.56, 0.16],
    inside: (x) => Math.sqrt(x[0]) + Math.sqrt(x[1]) <= 2 + 1e-12,
    // biên: x = (s², (2 − s)²), 0 ≤ s ≤ 2
    edge: (s) => [s * s, (2 - s) * (2 - s)], sRange: [0, 2], closeX: [[0, 0]]
  },
  mono: {
    label: 'x₁x₂ = 1',
    xr: [0, 4.4], yr: [0, 4.4], lr: [-2.2, 2.2],
    p: [0.5, 2], q: [2, 0.5],
    inside: (x) => Math.abs(x[0] * x[1] - 1) < 1e-9,
    edge: (s) => [s, 1 / s], sRange: [0.23, 4.4], closeX: null
  },
  poster: {
    label: 'áp phích: wh ≥ 600, (w + 4)(h + 6) ≤ 864',
    xr: [0, 62], yr: [0, 62], lr: [1.5, 4.2],
    p: null, q: null,
    inside: (x) => x[0] * x[1] >= 600 - 1e-9,
    edge: (s) => [s, 600 / s], sRange: [9.7, 62], closeX: [[62, 62], [9.7, 62]]
  }
}
const key = ref('sqrt'), showPath = ref(true)
const pr = computed(() => presets[key.value])
const vx = computed(() => makeView({ x0: pr.value.xr[0], x1: pr.value.xr[1], y0: pr.value.yr[0], y1: pr.value.yr[1], width: 230, height: 230 }))
const vl = computed(() => makeView({ x0: pr.value.lr[0], x1: pr.value.lr[1], y0: pr.value.lr[0], y1: pr.value.lr[1], width: 230, height: 230 }))
const PX = (p) => [vx.value.sx(p[0]), vx.value.sy(p[1])]
const PL = (p) => [vl.value.sx(p[0]), vl.value.sy(p[1])]
const lg = (p) => [Math.log(p[0]), Math.log(p[1])]
const samples = (n) => Array.from({ length: n + 1 }, (_, i) => i / n)
const edgeX = computed(() => samples(240).map(t => pr.value.edge(pr.value.sRange[0] + t * (pr.value.sRange[1] - pr.value.sRange[0]))))
const regionX = computed(() => (pr.value.closeX ? [...edgeX.value, ...pr.value.closeX] : null))
// Trong biến log, biên là ảnh log của cùng đường cong. Tập được đóng lại bằng góc của khung nhìn.
const edgeL = computed(() => edgeX.value.filter(p => p[0] > 0 && p[1] > 0).map(lg).filter(p => p.every(Number.isFinite)))
const regionL = computed(() => {
  const L = pr.value.lr
  if (key.value === 'sqrt') return [...edgeL.value.filter(p => p[0] >= L[0] - 1 && p[1] >= L[0] - 1), [L[0] - 1, L[0] - 1]]
  if (key.value === 'poster') return [...edgeL.value, [L[1] + 1, L[1] + 1]]
  return null
})
// Tập mức (w + 4)(h + 6) ≤ 864 của bài toán áp phích: dưới đường h = 864/(w + 4) − 6.
const levelX = computed(() => (key.value === 'poster' ? samples(200).map(t => { const w = 0.5 + t * 61; return [w, 864 / (w + 4) - 6] }).filter(p => p[1] > 0) : []))
const levelL = computed(() => levelX.value.map(lg))
const OPT = [20, 30]
const geoPath = (p, q) => samples(60).map(t => [p[0] ** (1 - t) * q[0] ** t, p[1] ** (1 - t) * q[1] ** t])
const linePath = (p, q) => samples(60).map(t => [p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])])
const pts = (arr, P) => arr.map(p => P(p).join(',')).join(' ')
const mid = computed(() => (pr.value.p ? [(pr.value.p[0] + pr.value.q[0]) / 2, (pr.value.p[1] + pr.value.q[1]) / 2] : null))
const gmean = computed(() => (pr.value.p ? [Math.sqrt(pr.value.p[0] * pr.value.q[0]), Math.sqrt(pr.value.p[1] * pr.value.q[1])] : null))
const ok = (x) => pr.value.inside(x)
</script>

<template>
  <figure class="study-lab" aria-label="Một tập trong biến x và trong biến log x">
    <p class="lab-title">Đổi sang thang logarit</p>
    <p class="lab-lead">Bên trái là tập trong biến gốc x, bên phải là cùng tập ấy sau phép đổi biến y = log x. Đoạn thẳng nối hai điểm bên phải ứng với đường trung bình nhân bên trái.</p>
    <div class="lab-pair">
      <svg :viewBox="`0 0 ${vx.width} ${vx.height}`" role="img" aria-label="Tập trong biến gốc x">
        <line x1="0" :x2="vx.width" :y1="vx.sy(0)" :y2="vx.sy(0)" class="lab-axis" />
        <line :x1="vx.sx(0)" :x2="vx.sx(0)" y1="0" :y2="vx.height" class="lab-axis" />
        <text x="8" y="16" class="lab-small">biến x</text>
        <polygon v-if="regionX" :points="pts(regionX, PX)" class="lab-region" />
        <polyline :points="pts(edgeX, PX)" class="lab-accent" style="stroke-width: 2.5" />
        <polyline v-if="levelX.length" :points="pts(levelX, PX)" class="lab-warn" />
        <circle v-if="key === 'poster'" :cx="PX(OPT)[0]" :cy="PX(OPT)[1]" r="6" class="lab-dot-warn" />
        <template v-if="pr.p">
          <polyline :points="pts(linePath(pr.p, pr.q), PX)" class="lab-bad" style="stroke-width: 2" />
          <polyline v-if="showPath" :points="pts(geoPath(pr.p, pr.q), PX)" class="lab-good" style="stroke-width: 2.5" />
          <circle :cx="PX(mid)[0]" :cy="PX(mid)[1]" r="5" :class="ok(mid) ? 'lab-dot' : 'lab-dot-bad'" />
          <circle :cx="PX(gmean)[0]" :cy="PX(gmean)[1]" r="5" class="lab-dot-warn" />
          <circle :cx="PX(pr.p)[0]" :cy="PX(pr.p)[1]" r="5" class="lab-dot" /><circle :cx="PX(pr.q)[0]" :cy="PX(pr.q)[1]" r="5" class="lab-dot" />
        </template>
      </svg>
      <svg :viewBox="`0 0 ${vl.width} ${vl.height}`" role="img" aria-label="Cùng tập trong biến y bằng log x">
        <line x1="0" :x2="vl.width" :y1="vl.sy(0)" :y2="vl.sy(0)" class="lab-axis" />
        <line :x1="vl.sx(0)" :x2="vl.sx(0)" y1="0" :y2="vl.height" class="lab-axis" />
        <text x="8" y="16" class="lab-small">biến y = log x</text>
        <polygon v-if="regionL" :points="pts(regionL, PL)" class="lab-region" />
        <polyline :points="pts(edgeL, PL)" class="lab-accent" style="stroke-width: 2.5" />
        <polyline v-if="levelL.length" :points="pts(levelL, PL)" class="lab-warn" />
        <circle v-if="key === 'poster'" :cx="PL(lg(OPT))[0]" :cy="PL(lg(OPT))[1]" r="6" class="lab-dot-warn" />
        <template v-if="pr.p">
          <polyline :points="pts(linePath(pr.p, pr.q).map(lg), PL)" class="lab-bad" style="stroke-width: 2" />
          <polyline v-if="showPath" :points="pts(geoPath(pr.p, pr.q).map(lg), PL)" class="lab-good" style="stroke-width: 2.5" />
          <circle :cx="PL(lg(gmean))[0]" :cy="PL(lg(gmean))[1]" r="5" class="lab-dot-warn" />
          <circle :cx="PL(lg(pr.p))[0]" :cy="PL(lg(pr.p))[1]" r="5" class="lab-dot" /><circle :cx="PL(lg(pr.q))[0]" :cy="PL(lg(pr.q))[1]" r="5" class="lab-dot" />
        </template>
      </svg>
    </div>
    <p class="lab-legend"><span class="legend-accent">tập (hoặc biên của tập)</span><span v-if="pr.p" class="legend-bad">đoạn thẳng trong biến x</span><span v-if="pr.p && showPath" class="legend-good">đoạn thẳng trong biến log x</span><span v-if="key === 'poster'" class="legend-warn">tập mức của hàm mục tiêu và nghiệm</span></p>
    <div class="lab-controls">
      <label>Tập<select v-model="key"><option v-for="(s, k) in presets" :key="k" :value="k">{{ s.label }}</option></select></label>
      <label v-if="pr.p" class="lab-check"><input v-model="showPath" type="checkbox" /> Hiện đường trung bình nhân</label>
    </div>
    <div class="lab-readout" role="status">
      <template v-if="pr.p">
        <p>Hai điểm p = {{ fmtPoint(pr.p) }} và q = {{ fmtPoint(pr.q) }} đều thuộc tập.</p>
        <p :class="ok(mid) ? '' : 'is-bad'">Trung điểm cộng {{ fmtPoint(mid) }} {{ ok(mid) ? 'thuộc tập' : 'không thuộc tập' }}: trong biến x, tập {{ ok(mid) ? 'có thể lồi' : 'không lồi' }}.</p>
        <p class="is-good">Trung bình nhân {{ fmtPoint(gmean) }} thuộc tập. Nó là trung điểm của đoạn thẳng trong biến log x, nơi tập là lồi.</p>
      </template>
      <template v-else>
        <p>Ràng buộc wh ≥ 600 trở thành nửa mặt phẳng log w + log h ≥ log 600. Tập mức (w + 4)(h + 6) ≤ 864 không lồi trong biến (w, h) nhưng lồi trong biến log.</p>
        <p class="is-accent">Nghiệm (w, h) = (20, 30), diện tích giấy 864 cm²: tập mức chạm ràng buộc tại đúng một điểm.</p>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Với tập √x₁ + √x₂ ≤ 2, vì sao đoạn thẳng đỏ đi ra ngoài tập, còn đường xanh thì không?</li>
        <li>Với x₁x₂ = 1, tập là một đường cong trong biến x. Trong biến log x nó trở thành gì, và vì sao ràng buộc đẳng thức monomial là "affine trá hình"?</li>
        <li>Với bài toán áp phích, so sánh hình dạng tập mức của hàm mục tiêu ở hai bên. Bên nào cho thấy bài toán là lồi?</li>
      </ol>
    </details>
  </figure>
</template>
