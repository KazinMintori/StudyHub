<script setup>
import { computed, ref } from 'vue'
import { makeView, fmt, fmtPoint } from './svg-drag'

// LP bền vững (ví dụ tự đặt của chủ đề 8, Lecture 02): cực đại x₁ + 2x₂ với aᵢᵀx ≤ bᵢ, trong đó mỗi aᵢ chỉ biết
// thuộc hình tròn tâm āᵢ bán kính ρ. Ràng buộc bền vững āᵢᵀx + ρ‖x‖₂ ≤ bᵢ là ràng buộc nón bậc hai.
// Gốc tọa độ nằm trong miền (mọi bᵢ > 0), nên miền bền vững hình sao theo gốc: theo hướng đơn vị u, điểm biên
// cách gốc s(u) = min bᵢ/(āᵢᵀu + ρ) trên các i có āᵢᵀu + ρ > 0. Nghiệm tìm bằng cách quét u rồi tinh chỉnh.
const A = [[1, 0], [0, 1], [1, 1], [-1, 0], [0, -1]], B = [3, 2, 4, 1, 1], C = [1, 2]
const rho = ref(0.2)
const dot = (u, v) => u[0] * v[0] + u[1] * v[1]
const radius = (u, r) => {
  let s = Infinity
  for (let i = 0; i < A.length; i++) { const d = dot(A[i], u) + r; if (d > 1e-12) s = Math.min(s, B[i] / d) }
  return s
}
const dir = (t) => [Math.cos(t), Math.sin(t)]
const boundary = (r) => Array.from({ length: 721 }, (_, k) => { const u = dir((k / 720) * 2 * Math.PI), s = radius(u, r); return [s * u[0], s * u[1]] })
const optimum = (r) => {
  const val = (t) => { const u = dir(t); return radius(u, r) * dot(C, u) }
  let bt = 0, bv = -Infinity
  for (let k = 0; k < 3600; k++) { const t = (k / 3600) * 2 * Math.PI, v = val(t); if (v > bv) { bv = v; bt = t } }
  // Tinh chỉnh bằng tìm kiếm tỉ lệ vàng quanh góc tốt nhất (hàm theo góc có một đỉnh ở đây).
  let lo = bt - (2 * Math.PI) / 3600, hi = bt + (2 * Math.PI) / 3600
  for (let k = 0; k < 60; k++) { const m1 = lo + (hi - lo) * 0.382, m2 = lo + (hi - lo) * 0.618; if (val(m1) < val(m2)) lo = m1; else hi = m2 }
  const t = (lo + hi) / 2, u = dir(t), s = radius(u, r)
  return { x: [s * u[0], s * u[1]], value: val(t) }
}
const nominal = { x: [2, 2], value: 6 }
const robust = computed(() => optimum(rho.value))
const active = computed(() => {
  const x = robust.value.x, n = Math.hypot(...x)
  return A.map((a, i) => (Math.abs(dot(a, x) + rho.value * n - B[i]) < 2e-3 ? i : -1)).filter(i => i >= 0)
})
const worstViolation = computed(() => {
  const n = Math.hypot(...nominal.x)
  return Math.max(...A.map((a, i) => dot(a, nominal.x) + rho.value * n - B[i]))
})
const view = makeView({ x0: -1.6, x1: 3.6, y0: -1.6, y1: 2.6, width: 460, height: 372 })
const P = (p) => [view.sx(p[0]), view.sy(p[1])]
const pts = (arr) => arr.map(p => P(p).join(',')).join(' ')
const nominalPoly = boundary(0)
const robustPoly = computed(() => boundary(rho.value))
const label = (i) => ['x₁ ≤ 3', 'x₂ ≤ 2', 'x₁ + x₂ ≤ 4', '−x₁ ≤ 1', '−x₂ ≤ 1'][i]
</script>

<template>
  <figure class="study-lab" aria-label="LP bền vững với hệ số bất định trong hình tròn">
    <p class="lab-title">Cái giá của việc an toàn với mọi hệ số</p>
    <p class="lab-lead">Miền nhạt là miền khả thi khi các hệ số aᵢ được biết chính xác. Khi mỗi aᵢ chỉ biết nằm trong một hình tròn bán kính ρ, các điểm phải thỏa ràng buộc với mọi hệ số có thể, và miền khả thi co lại thành miền tô đậm có biên cong.</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Miền khả thi danh nghĩa, miền khả thi bền vững, nghiệm danh nghĩa và nghiệm bền vững">
      <line v-for="t in [-1, 0, 1, 2, 3]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="t in [-1, 0, 1, 2]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
      <polygon :points="pts(nominalPoly)" class="lab-region-soft" style="opacity: 0.45" />
      <polygon :points="pts(robustPoly)" class="lab-region" />
      <circle :cx="P(nominal.x)[0]" :cy="P(nominal.x)[1]" r="6" class="lab-dot-hollow" />
      <text :x="P(nominal.x)[0] + 8" :y="P(nominal.x)[1] - 8" class="lab-small">danh nghĩa</text>
      <circle :cx="P(robust.x)[0]" :cy="P(robust.x)[1]" r="7" class="lab-dot-warn" />
      <line :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P([0.45, 0.9])[0]" :y2="P([0.45, 0.9])[1]" class="lab-accent" />
      <text :x="P([0.45, 0.9])[0] + 6" :y="P([0.45, 0.9])[1]" class="lab-small">c</text>
    </svg>
    <p class="lab-legend"><span class="legend-accent">miền bền vững, hướng c</span><span class="legend-warn">nghiệm bền vững</span><span class="legend-guide">miền danh nghĩa (nhạt)</span></p>
    <div class="lab-controls">
      <label>Bán kính bất định ρ = {{ fmt(rho, 2) }}<input v-model.number="rho" type="range" min="0" max="0.6" step="0.01" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p>Nghiệm danh nghĩa (ρ = 0): (2, 2), giá trị x₁ + 2x₂ = 6.</p>
      <p>Nghiệm bền vững: x = {{ fmtPoint(robust.x, 3) }}, giá trị <span class="is-accent">{{ fmt(robust.value, 3) }}</span>, thấp hơn {{ fmt(nominal.value - robust.value, 3) }} so với danh nghĩa. Ràng buộc chặt: {{ active.map(label).join(', ') || 'không có' }}.</p>
      <p v-if="rho > 0" :class="worstViolation > 1e-9 ? 'is-bad' : ''">Nếu vẫn dùng nghiệm danh nghĩa (2, 2), trong trường hợp xấu nhất có ràng buộc bị vượt {{ fmt(worstViolation, 3) }}, vì số hạng ρ‖x‖₂ = {{ fmt(rho * Math.hypot(2, 2), 3) }}.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Tăng ρ từ 0. Miền bền vững co lại về phía nào nhiều nhất, và vì sao các điểm gần gốc tọa độ ít bị ảnh hưởng?</li>
        <li>Đặt ρ = 0.2 và kiểm tra nghiệm (2, 1.5) bằng tay: hai ràng buộc chặt cho phương trình nào?</li>
        <li>Biên của miền bền vững cong. Vì sao một ràng buộc vốn tuyến tính lại cho biên cong?</li>
        <li>Giá trị tối ưu giảm khi ρ tăng. Đó là cái giá của sự an toàn. Với ρ = 0.5, cái giá ấy là bao nhiêu phần trăm?</li>
      </ol>
    </details>
  </figure>
</template>
