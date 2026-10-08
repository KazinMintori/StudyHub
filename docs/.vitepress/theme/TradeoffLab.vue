<script setup>
import { computed, ref } from 'vue'
import { makeView, fmt, fmtPoint } from './svg-drag'

// Đường đánh đổi của bình phương tối thiểu có điều chuẩn (ví dụ tự đặt của chủ đề 12, Lecture 02).
// Dữ liệu A (4×2), b. Hai mục tiêu F₁ = ‖Ax − b‖², F₂ = ‖x‖₂² (ridge) hoặc ‖x‖₁ (lasso).
// Vô hướng hóa với trọng số (1, μ): ridge có nghiệm đóng x(μ) = (AᵀA + μI)⁻¹Aᵀb; lasso giải bằng hạ theo
// tọa độ với ngưỡng mềm, khởi động từ nghiệm của μ trước. Đã đối chiếu với Python (x₂ về 0 tại μ = 86/7).
const A = [[1, 2], [2, 1], [1, 1], [3, 1]], b = [3, 1, 2, 4]
const mode = ref('ridge'), logMu = ref(0.5)
const mu = computed(() => 10 ** logMu.value)
const F1 = (x) => A.reduce((s, row, i) => s + (row[0] * x[0] + row[1] * x[1] - b[i]) ** 2, 0)
const F2 = (x, m) => (m === 'ridge' ? x[0] * x[0] + x[1] * x[1] : Math.abs(x[0]) + Math.abs(x[1]))
const AtA = [[15, 8], [8, 7]], Atb = [19, 13]
const ridge = (m) => {
  const a = AtA[0][0] + m, d = AtA[1][1] + m, c = AtA[0][1], det = a * d - c * c
  return [(d * Atb[0] - c * Atb[1]) / det, (a * Atb[1] - c * Atb[0]) / det]
}
const soft = (z, t) => Math.sign(z) * Math.max(Math.abs(z) - t, 0)
const lasso = (m, start = [0, 0]) => {
  const x = [...start]
  for (let it = 0; it < 400; it++) for (let j = 0; j < 2; j++) {
    let rho = 0, nn = 0
    for (let i = 0; i < 4; i++) { const r = b[i] - A[i][0] * x[0] - A[i][1] * x[1] + A[i][j] * x[j]; rho += A[i][j] * r; nn += A[i][j] ** 2 }
    x[j] = soft(rho, m / 2) / nn
  }
  return x
}
const LOGS = Array.from({ length: 161 }, (_, i) => -2 + (4.5 * i) / 160)
const path = computed(() => {
  let prev = [0, 0]
  return LOGS.map(l => {
    const m = 10 ** l, x = mode.value === 'ridge' ? ridge(m) : (prev = lasso(m, prev))
    return { x, f1: F1(x), f2: F2(x, mode.value) }
  })
})
const cur = computed(() => {
  const x = mode.value === 'ridge' ? ridge(mu.value) : lasso(mu.value, [0.7, 1])
  return { x, f1: F1(x), f2: F2(x, mode.value) }
})
// Đám mây các giá trị đạt được: (F₁, F₂) tại một lưới điểm x.
const cloud = computed(() => {
  const pts = []
  for (let i = 0; i <= 26; i++) for (let j = 0; j <= 26; j++) {
    const x = [-0.4 + (1.6 * i) / 26, -0.4 + (1.8 * j) / 26]
    pts.push([F1(x), F2(x, mode.value)])
  }
  return pts
})
const ov = computed(() => makeView({ x0: 0, x1: 32, y0: 0, y1: mode.value === 'ridge' ? 2.2 : 2.1, width: 230, height: 230 }))
const pv = makeView({ x0: -0.15, x1: 1.15, y0: -0.15, y1: 1.15, width: 230, height: 230 })
const PO = (p) => [ov.value.sx(p[0]), ov.value.sy(p[1])]
const PP = (p) => [pv.sx(p[0]), pv.sy(p[1])]
// Đường tựa: F₁ + μF₂ = hằng số, tiếp xúc với tập giá trị đạt được tại điểm Pareto.
const support = computed(() => {
  const c = cur.value.f1 + mu.value * cur.value.f2
  return [PO([0, c / mu.value]), PO([c, 0])]
})
const zeroNote = computed(() => (mode.value === 'lasso' ? cur.value.x.map((v, i) => (Math.abs(v) < 1e-9 ? i + 1 : 0)).filter(Boolean) : []))
</script>

<template>
  <figure class="study-lab" aria-label="Đường đánh đổi giữa sai số khớp và độ lớn tham số">
    <p class="lab-title">Đánh đổi giữa khớp dữ liệu và giữ tham số nhỏ</p>
    <p class="lab-lead">Bên trái là không gian mục tiêu: mỗi chấm nhạt là cặp (F₁, F₂) của một điểm x. Đường đậm là đường đánh đổi Pareto. Bên phải là đường đi của nghiệm x(μ) khi trọng số μ thay đổi.</p>
    <div class="lab-pair">
      <svg :viewBox="`0 0 ${ov.width} ${ov.height}`" role="img" aria-label="Tập giá trị mục tiêu đạt được, đường Pareto và đường tựa">
        <line x1="0" :x2="ov.width" :y1="ov.sy(0)" :y2="ov.sy(0)" class="lab-axis" />
        <line :x1="ov.sx(0)" :x2="ov.sx(0)" y1="0" :y2="ov.height" class="lab-axis" />
        <text :x="ov.width - 70" :y="ov.sy(0) - 6" class="lab-small">F₁ = ‖Ax − b‖²</text>
        <text x="6" y="14" class="lab-small">{{ mode === 'ridge' ? 'F₂ = ‖x‖²' : 'F₂ = ‖x‖₁' }}</text>
        <circle v-for="(p, i) in cloud" :key="i" :cx="PO(p)[0]" :cy="PO(p)[1]" r="1.6" class="lab-dot" style="opacity: 0.25" />
        <polyline :points="path.map(q => PO([q.f1, q.f2]).join(',')).join(' ')" class="lab-accent" />
        <line :x1="support[0][0]" :y1="support[0][1]" :x2="support[1][0]" :y2="support[1][1]" class="lab-guide" />
        <circle :cx="PO([cur.f1, cur.f2])[0]" :cy="PO([cur.f1, cur.f2])[1]" r="6" class="lab-dot-warn" />
      </svg>
      <svg :viewBox="`0 0 ${pv.width} ${pv.height}`" role="img" aria-label="Đường đi của nghiệm theo trọng số trong không gian tham số">
        <line x1="0" :x2="pv.width" :y1="pv.sy(0)" :y2="pv.sy(0)" class="lab-axis" />
        <line :x1="pv.sx(0)" :x2="pv.sx(0)" y1="0" :y2="pv.height" class="lab-axis" />
        <text :x="pv.width - 22" :y="pv.sy(0) - 6" class="lab-small">x₁</text>
        <text :x="pv.sx(0) + 6" y="14" class="lab-small">x₂</text>
        <polyline :points="path.map(q => PP(q.x).join(',')).join(' ')" class="lab-good" style="stroke-width: 2.5" />
        <circle :cx="PP(path[0].x)[0]" :cy="PP(path[0].x)[1]" r="4" class="lab-dot" />
        <circle :cx="PP([0, 0])[0]" :cy="PP([0, 0])[1]" r="4" class="lab-dot" />
        <circle :cx="PP(cur.x)[0]" :cy="PP(cur.x)[1]" r="6" class="lab-dot-warn" />
      </svg>
    </div>
    <p class="lab-legend"><span class="legend-accent">đường đánh đổi</span><span class="legend-guide">đường tựa F₁ + μF₂ = hằng số</span><span class="legend-good">đường đi của x(μ)</span><span class="legend-warn">nghiệm hiện tại</span></p>
    <div class="lab-controls">
      <label>Trọng số μ = {{ fmt(mu, mu < 1 ? 3 : 2) }}<input v-model.number="logMu" type="range" min="-2" max="2.5" step="0.01" /></label>
      <label>Mục tiêu thứ hai<select v-model="mode"><option value="ridge">‖x‖₂² (ridge)</option><option value="lasso">‖x‖₁ (lasso)</option></select></label>
    </div>
    <div class="lab-readout" role="status">
      <p>x(μ) = {{ fmtPoint(cur.x, 4) }}, F₁ = {{ fmt(cur.f1, 3) }}, F₂ = {{ fmt(cur.f2, 3) }}.</p>
      <p>Đường tựa có hệ số góc −1/μ = {{ fmt(-1 / mu, 3) }}: quanh điểm này, giảm F₂ một đơn vị phải trả khoảng {{ fmt(mu, 2) }} đơn vị F₁.</p>
      <p v-if="zeroNote.length" class="is-accent">Thành phần x{{ zeroNote.join(', x') }} bằng đúng 0: chuẩn ℓ₁ cho nghiệm thưa.</p>
      <p v-else-if="mode === 'ridge'">Với ridge, các thành phần co dần về 0 nhưng không bao giờ bằng đúng 0 khi μ hữu hạn.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo μ từ nhỏ đến lớn. Hai đầu của đường đánh đổi ứng với nghiệm nào?</li>
        <li>Đường tựa luôn chạm đám mây giá trị ở đúng một điểm của đường đánh đổi, và cả đám mây nằm về một phía. Vì sao?</li>
        <li>Đổi sang lasso. Với μ khoảng 12.3 trở lên, x₂ bằng đúng 0. Trong khi đó x₁ có luôn giảm khi μ tăng không?</li>
        <li>So hai đường đi bên phải: đường của ridge cong mềm, đường của lasso gãy khúc và chạm trục. Điều này gợi ý gì về việc chọn đặc trưng?</li>
      </ol>
    </details>
  </figure>
</template>
