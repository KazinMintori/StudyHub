<script setup>
import { computed, ref } from 'vue'
import { makeView, fmt } from './svg-drag'

// Cực tiểu trị riêng lớn nhất (chủ đề 11, Lecture 02): A(x) = [[x, ε], [ε, 1 − x]].
// Hai trị riêng là 1/2 ± √((x − 1/2)² + ε²). Hàm λ_max lồi theo x vì là giá trị lớn nhất của họ hàm tuyến tính
// uᵀA(x)u với ‖u‖ = 1. Khi ε = 0 hai trị riêng cắt nhau và λ_max có một góc nhọn, khi ε > 0 chúng "tránh" nhau.
// Bài toán cực tiểu λ_max(A(x)) là SDP: cực tiểu t với tI − A(x) ⪰ 0.
const eps = ref(0.3), x = ref(0)
const lam = (xx, e) => { const r = Math.sqrt((xx - 0.5) ** 2 + e * e); return [0.5 - r, 0.5 + r] }
const cur = computed(() => lam(x.value, eps.value))
const view = computed(() => makeView({ x0: -1, x1: 2, y0: -1.3, y1: 2.3, width: 460, height: 300 }))
const P = (p) => [view.value.sx(p[0]), view.value.sy(p[1])]
const xs = Array.from({ length: 301 }, (_, i) => -1 + (3 * i) / 300)
const curve = (k) => xs.map(xx => P([xx, lam(xx, eps.value)[k]]).join(',')).join(' ')
// Đường tiếp tuyến dưới (dưới đạo hàm) của λ_max tại x hiện tại: λ_max(y) ≥ λ_max(x) + g(y − x) với g = u₁ᵀA₁u₁.
const slope = computed(() => {
  const r = Math.sqrt((x.value - 0.5) ** 2 + eps.value ** 2)
  return r < 1e-12 ? 0 : (x.value - 0.5) / r
})
const tangent = computed(() => {
  const y0 = cur.value[1], g = slope.value
  return [P([-1, y0 + g * (-1 - x.value)]), P([2, y0 + g * (2 - x.value)])]
})
</script>

<template>
  <figure class="study-lab" aria-label="Trị riêng lớn nhất của một ma trận phụ thuộc affine vào một tham số">
    <p class="lab-title">Trị riêng lớn nhất là một hàm lồi</p>
    <p class="lab-lead">Hai đường cong là hai trị riêng của A(x) = [[x, ε], [ε, 1 − x]] theo x. Đường phía trên, λ_max, là hàm lồi, và cực tiểu nó là một bài toán SDP. Kéo ε về 0 để thấy chuyện gì xảy ra khi hai trị riêng chạm nhau.</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Hai trị riêng theo tham số x, trị riêng lớn nhất và tiếp tuyến của nó">
      <line v-for="t in [-1, 0, 1, 2]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="t in [-1, 0, 1, 2]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <text v-for="t in [-1, 1, 2]" :key="`tx${t}`" :x="view.sx(t) + 4" :y="view.sy(0) + 16" class="lab-small">{{ t }}</text>
      <polyline :points="curve(0)" class="lab-line" style="opacity: 0.6" />
      <line :x1="tangent[0][0]" :y1="tangent[0][1]" :x2="tangent[1][0]" :y2="tangent[1][1]" class="lab-guide" />
      <polyline :points="curve(1)" class="lab-accent" />
      <circle :cx="P([0.5, 0.5 + eps])[0]" :cy="P([0.5, 0.5 + eps])[1]" r="6" class="lab-dot-warn" />
      <circle :cx="P([x, cur[1]])[0]" :cy="P([x, cur[1]])[1]" r="7" class="lab-dot-accent" />
      <circle :cx="P([x, cur[0]])[0]" :cy="P([x, cur[0]])[1]" r="5" class="lab-dot" />
    </svg>
    <p class="lab-legend"><span class="legend-accent">λ_max(A(x))</span><span class="legend-guide">tiếp tuyến dưới tại x</span><span class="legend-warn">cực tiểu của λ_max</span></p>
    <div class="lab-controls">
      <label>x = {{ fmt(x, 2) }}<input v-model.number="x" type="range" min="-1" max="2" step="0.01" /></label>
      <label>Phần tử ngoài đường chéo ε = {{ fmt(eps, 2) }}<input v-model.number="eps" type="range" min="0" max="0.8" step="0.01" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p>A(x) có hai trị riêng {{ fmt(cur[0], 3) }} và <span class="is-accent">{{ fmt(cur[1], 3) }}</span>.</p>
      <p>Giá trị nhỏ nhất của λ_max là 1/2 + ε = {{ fmt(0.5 + eps, 3) }}, đạt tại x = 1/2. SDP tương ứng: cực tiểu t với tI − A(x) ⪰ 0.</p>
      <p v-if="eps < 0.005 && Math.abs(x - 0.5) < 0.006" class="is-bad">Tại đây hai trị riêng bằng nhau và λ_max = max(x, 1 − x) có góc nhọn: không có đạo hàm, mọi độ dốc trong [−1, 1] đều cho một tiếp tuyến dưới.</p>
      <p v-else>Độ dốc của λ_max tại x là {{ fmt(slope, 3) }}, và tiếp tuyến nét đứt nằm dưới toàn bộ đường cong, đúng như với mọi hàm lồi.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo x qua lại với ε = 0.3. Hai trị riêng có bao giờ bằng nhau không? Khoảng cách nhỏ nhất giữa chúng là bao nhiêu?</li>
        <li>Đặt ε = 0. Hai đường bây giờ là hai đường thẳng nào, và λ_max có dạng gì tại x = 1/2?</li>
        <li>Đường λ_min ở dưới là hàm lõm. Vì sao, và cực đại λ_min có là bài toán lồi không?</li>
        <li>Tiếp tuyến nét đứt luôn nằm dưới λ_max. Điều đó nói gì về tính lồi?</li>
      </ol>
    </details>
  </figure>
</template>
