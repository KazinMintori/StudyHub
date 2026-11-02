<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const svgLoss = ref(null), svgLikelihood = ref(null), w = ref(1), sigma = ref(0.6)
const optimum = 11 / 14, minimum = 5 / 28
const loss = x => (14*x*x - 22*x + 9)/2
const relative = x => Math.exp(-(loss(x)-minimum)/sigma.value**2)
const lossView = ref(makeView({ x0: 0, x1: 1.5, y0: 0, y1: 5, width: 400, height: 210, pad: 30 }))
const likelihoodView = ref(makeView({ x0: 0, x1: 1.5, y0: 0, y1: 1.1, width: 400, height: 210, pad: 30 }))
const lossDrag = createDragger(svgLoss, lossView, (_, p) => { w.value = p[0] }, { step: 0.02 })
const likelihoodDrag = createDragger(svgLikelihood, likelihoodView, (_, p) => { w.value = p[0] }, { step: 0.02 })
const lossCurve = computed(() => Array.from({ length: 151 }, (_, i) => lossView.value.point([i/100, loss(i/100)]).join(',')).join(' '))
const likelihoodCurve = computed(() => Array.from({ length: 151 }, (_, i) => likelihoodView.value.point([i/100, relative(i/100)]).join(',')).join(' '))
</script>

<template>
  <figure class="study-lab" aria-label="Bình phương tối thiểu và cực đại likelihood có cùng tham số tối ưu">
    <figcaption class="lab-title">Đáy của mất mát trùng đỉnh của likelihood</figcaption>
    <p class="lab-lead">Dùng lại ba quan sát ở phần 1. Kéo chấm trên một trong hai đồ thị theo chiều ngang. Cả hai chấm luôn có cùng w. Đổi σ để thấy độ nhọn thay đổi, còn tham số tối ưu vẫn giữ nguyên.</p>
    <svg ref="svgLoss" viewBox="0 0 400 210" role="group" aria-label="Mất mát f(w) và tham số w kéo được" @pointermove="lossDrag.move" @pointerup="lossDrag.end" @pointercancel="lossDrag.end" @lostpointercapture="lossDrag.end">
      <line x1="30" y1="180" x2="375" y2="180" class="lab-axis" /><text x="30" y="24">Mất mát f(w)</text><text x="366" y="202">w</text>
      <text x="15" y="201">0</text><text :x="lossView.sx(optimum) - 22" y="201">11/14</text><text x="8" :y="lossView.sy(4.5) + 7">4,5</text>
      <line :x1="lossView.sx(optimum)" :x2="lossView.sx(optimum)" y1="35" y2="180" class="lab-guide" /><polyline :points="lossCurve" class="lab-accent" />
      <circle :cx="lossView.sx(w)" :cy="lossView.sy(loss(w))" r="8" class="lab-dot-accent" />
      <circle :cx="lossView.sx(w)" :cy="lossView.sy(loss(w))" r="30" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Trọng số w trên đồ thị mất mát" aria-valuemin="0" aria-valuemax="1.5" :aria-valuenow="w" :aria-valuetext="`w = ${fmt(w)}, f = ${fmt(loss(w))}`" @pointerdown="lossDrag.start('w', $event)" @keydown="lossDrag.key('w', [w, loss(w)], $event)" />
    </svg>
    <svg ref="svgLikelihood" viewBox="0 0 400 210" role="group" aria-label="Likelihood tương đối và cùng tham số w kéo được" @pointermove="likelihoodDrag.move" @pointerup="likelihoodDrag.end" @pointercancel="likelihoodDrag.end" @lostpointercapture="likelihoodDrag.end">
      <line x1="30" y1="180" x2="375" y2="180" class="lab-axis" /><text x="30" y="24">Likelihood L(w)/L(w*)</text><text x="366" y="202">w</text>
      <text x="15" y="201">0</text><text x="8" :y="likelihoodView.sy(1) + 7">1</text><text :x="likelihoodView.sx(optimum) - 22" y="201">11/14</text>
      <line :x1="likelihoodView.sx(optimum)" :x2="likelihoodView.sx(optimum)" y1="35" y2="180" class="lab-guide" /><polyline :points="likelihoodCurve" class="lab-good" />
      <circle :cx="likelihoodView.sx(w)" :cy="likelihoodView.sy(relative(w))" r="8" class="lab-dot-accent" />
      <circle :cx="likelihoodView.sx(w)" :cy="likelihoodView.sy(relative(w))" r="30" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Trọng số w trên đồ thị likelihood" aria-valuemin="0" aria-valuemax="1.5" :aria-valuenow="w" :aria-valuetext="`w = ${fmt(w)}, likelihood tương đối = ${fmt(relative(w))}`" @pointerdown="likelihoodDrag.start('w', $event)" @keydown="likelihoodDrag.key('w', [w, relative(w)], $event)" />
    </svg>
    <details class="lab-tasks lab-alternative"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svgLoss" axes="x" /></details>
    <div class="lab-controls"><label>Độ lệch chuẩn cố định σ = {{ fmt(sigma) }}<input v-model.number="sigma" type="range" min="0.2" max="1.2" step="0.05" /></label></div>
    <div class="lab-buttons"><button type="button" @click="w = optimum">Đưa w về 11/14</button></div>
    <div class="lab-readout" role="status"><p>w = {{ fmt(w, 3) }}, f(w) = {{ fmt(loss(w), 4) }}, L(w)/L(w*) = {{ fmt(relative(w), 4) }}.</p><p>Mức tăng của âm log-likelihood so với tối ưu là [f(w) − f(w*)]/σ² = {{ fmt((loss(w) - minimum)/sigma**2, 4) }}.</p><p>Likelihood là hàm của tham số khi dữ liệu đã cố định. Đường phía dưới được chia cho giá trị đỉnh để dễ so sánh, không phải một mật độ xác suất của w.</p></div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Kéo w xa khỏi đường thẳng đứng nét đứt. Hai giá trị hàm biến đổi theo chiều nào?</li><li>Giảm σ. Vì sao cùng một chênh lệch mất mát làm likelihood tương đối giảm mạnh hơn?</li><li>Bấm đưa w về tối ưu. Kết luận có còn đúng nếu bỏ giả thiết sai số Gauss độc lập và cùng phương sai không?</li></ol></details>
  </figure>
</template>

<style scoped>
svg + svg { margin-top: var(--space-3); }
svg text { font-size: 20px; }
.point-hit { fill: transparent !important; stroke: transparent; }
.point-hit:focus-visible { stroke: var(--vang); }
</style>
