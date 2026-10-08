<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt } from './svg-drag'

// Lát cắt của tập ma trận tương quan 3×3 (chủ đề 10, Lecture 02). Với ρ₂₃ = c cố định, ma trận
// R = [[1, ρ₁₂, ρ₁₃], [ρ₁₂, 1, c], [ρ₁₃, c, 1]] nửa xác định dương khi và chỉ khi (ρ₁₂, ρ₁₃) nằm trong ellipse
// ρ₁₂² + ρ₁₃² − 2cρ₁₂ρ₁₃ ≤ 1 − c² (đã kiểm bằng Python). Đây là miền khả thi của một LMI theo hai biến.
const c = ref(0.8), pt = ref([0.8, 0.5]), fixRow = ref(true)
// Trị riêng của ma trận đối xứng 3×3 theo công thức lượng giác.
function eig3(A) {
  const p1 = A[0][1] ** 2 + A[0][2] ** 2 + A[1][2] ** 2
  if (p1 < 1e-15) return [A[0][0], A[1][1], A[2][2]].sort((a, b) => a - b)
  const q = (A[0][0] + A[1][1] + A[2][2]) / 3
  const p2 = (A[0][0] - q) ** 2 + (A[1][1] - q) ** 2 + (A[2][2] - q) ** 2 + 2 * p1, p = Math.sqrt(p2 / 6)
  const B = A.map((row, i) => row.map((v, j) => (v - (i === j ? q : 0)) / p))
  const det = B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1]) - B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0]) + B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0])
  const phi = Math.acos(Math.min(1, Math.max(-1, det / 2))) / 3
  const e1 = q + 2 * p * Math.cos(phi), e3 = q + 2 * p * Math.cos(phi + (2 * Math.PI) / 3)
  return [e3, 3 * q - e1 - e3, e1]
}
const R = computed(() => [[1, pt.value[0], pt.value[1]], [pt.value[0], 1, c.value], [pt.value[1], c.value, 1]])
const eigs = computed(() => eig3(R.value))
const psd = computed(() => eigs.value[0] >= -1e-9)
// Khoảng của ρ₁₃ khi ρ₁₂ và ρ₂₃ cố định: ρ₁₂c ± √((1 − ρ₁₂²)(1 − c²)).
const interval = computed(() => {
  const r = pt.value[0], h = Math.sqrt(Math.max(0, (1 - r * r) * (1 - c.value * c.value)))
  return [r * c.value - h, r * c.value + h]
})
const view = ref(makeView({ x0: -1.15, x1: 1.15, y0: -1.15, y1: 1.15, width: 400, height: 400 }))
const svg = ref(null)
const P = (p) => [view.value.sx(p[0]), view.value.sy(p[1])]
const drag = createDragger(svg, view, (_, p) => { pt.value = [Math.max(-1, Math.min(1, p[0])), Math.max(-1, Math.min(1, p[1]))] }, { step: 0.02, snap: 0.01 })
const ellipse = computed(() => {
  const cc = c.value, k = Math.sqrt(1 - cc * cc)
  return Array.from({ length: 181 }, (_, i) => {
    const t = (i / 180) * 2 * Math.PI, a = (k * Math.cos(t)) / Math.sqrt(1 - cc), b = (k * Math.sin(t)) / Math.sqrt(1 + cc)
    return P([(a + b) / Math.SQRT2, (a - b) / Math.SQRT2]).join(',')
  }).join(' ')
})
const area = computed(() => Math.PI * Math.sqrt(1 - c.value * c.value))
</script>

<template>
  <figure class="study-lab" aria-label="Lát cắt của tập ma trận tương quan, miền khả thi của một bất đẳng thức ma trận tuyến tính">
    <p class="lab-title">Những bộ hệ số tương quan có thể xảy ra</p>
    <p class="lab-lead">Ba biến ngẫu nhiên có ma trận tương quan R. Giữ ρ₂₃ cố định, các cặp (ρ₁₂, ρ₁₃) làm R nửa xác định dương lấp đầy một ellipse, nhỏ hơn hẳn hình vuông [−1, 1]². Kéo điểm để xem trị riêng của R.</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Hình vuông các hệ số trong khoảng trừ một tới một và ellipse các cặp hợp lệ" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <rect :x="view.sx(-1)" :y="view.sy(1)" :width="view.sx(1) - view.sx(-1)" :height="view.sy(-1) - view.sy(1)" class="lab-region-soft" style="opacity: 0.3" />
      <line v-for="t in [-1, -0.5, 0, 0.5, 1]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="t in [-1, -0.5, 0, 0.5, 1]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
      <text :x="view.sx(1) - 30" :y="view.sy(0) + 16" class="lab-small">ρ₁₂</text>
      <text :x="view.sx(0) + 6" :y="view.sy(1) + 4" class="lab-small">ρ₁₃</text>
      <polygon :points="ellipse" class="lab-region" />
      <template v-if="fixRow">
        <line :x1="view.sx(pt[0])" :x2="view.sx(pt[0])" y1="0" :y2="view.height" class="lab-guide" />
        <line :x1="view.sx(pt[0])" :x2="view.sx(pt[0])" :y1="view.sy(interval[0])" :y2="view.sy(interval[1])" class="lab-warn" style="stroke-width: 5" />
      </template>
      <circle :cx="P(pt)[0]" :cy="P(pt)[1]" r="9" :class="psd ? 'lab-handle' : 'lab-handle lab-handle-alt'" tabindex="0" role="slider" aria-label="Cặp hệ số tương quan" :aria-valuetext="`ρ₁₂ = ${fmt(pt[0], 2)}, ρ₁₃ = ${fmt(pt[1], 2)}`" @pointerdown="drag.start('p', $event)" @keydown="drag.key('p', pt, $event)" />
    </svg>
    <p class="lab-legend"><span class="legend-accent">cặp hệ số làm R ⪰ 0</span><span class="legend-guide">hình vuông [−1, 1]² (nhạt)</span><span v-if="fixRow" class="legend-warn">các giá trị ρ₁₃ được phép khi ρ₁₂ cố định</span></p>
    <div class="lab-controls">
      <label>ρ₂₃ = {{ fmt(c, 2) }}<input v-model.number="c" type="range" min="-0.98" max="0.98" step="0.01" /></label>
      <label class="lab-check"><input v-model="fixRow" type="checkbox" /> Cố định ρ₁₂ và tìm khoảng của ρ₁₃</label>
    </div>
    <div class="lab-readout" role="status">
      <p>R có hàng (1, {{ fmt(pt[0], 2) }}, {{ fmt(pt[1], 2) }}), ({{ fmt(pt[0], 2) }}, 1, {{ fmt(c, 2) }}), ({{ fmt(pt[1], 2) }}, {{ fmt(c, 2) }}, 1). Trị riêng: {{ eigs.map(e => fmt(e, 3)).join(', ') }}.</p>
      <p v-if="psd" class="is-good">Mọi trị riêng không âm: đây là một ma trận tương quan hợp lệ.</p>
      <p v-else class="is-bad">Có trị riêng âm: không tồn tại ba biến ngẫu nhiên nào có các hệ số tương quan này, dù từng hệ số đều nằm trong [−1, 1].</p>
      <p v-if="fixRow">Với ρ₁₂ = {{ fmt(pt[0], 2) }} và ρ₂₃ = {{ fmt(c, 2) }}, hai bài toán SDP cực tiểu và cực đại ρ₁₃ cho khoảng <span class="is-accent">[{{ fmt(interval[0], 3) }}, {{ fmt(interval[1], 3) }}]</span>.</p>
      <p>Diện tích ellipse là π√(1 − c²) ≈ {{ fmt(area, 3) }}, khoảng {{ fmt((area / 4) * 100, 1) }}% hình vuông.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Đặt ρ₂₃ = 0.8 và kéo điểm tới ρ₁₂ = 0.8. ρ₁₃ nhỏ nhất có thể là bao nhiêu? Kết quả này nói gì về "tính bắc cầu" của tương quan?</li>
        <li>Đưa ρ₂₃ về 0. Ellipse thành hình gì, và điều kiện R ⪰ 0 khi đó đơn giản thành gì?</li>
        <li>Kéo ρ₂₃ gần 1. Ellipse dẹt lại về đường nào, và vì sao?</li>
        <li>Đặt điểm ở góc (0.9, −0.9) với ρ₂₃ = 0.5. Trị riêng nhỏ nhất bằng bao nhiêu?</li>
      </ol>
    </details>
  </figure>
</template>
