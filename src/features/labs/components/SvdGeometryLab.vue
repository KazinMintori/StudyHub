<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { norm2, svdStages } from '../services/foundation-geometry.mjs'

const svg = ref(null), point = ref([0.8, 0.6]), stage = ref(3), minor = ref(0.7)
const view = ref(makeView({ x0: -2, x1: 2, y0: -2, y1: 2, width: 360, height: 360, pad: 25 }))
const P = p => view.value.point(p)
const transform = p => svdStages(p, [1.6, minor.value])[stage.value]
const result = computed(() => transform(point.value))
const circle = computed(() => Array.from({ length: 121 }, (_, i) => {
  const t = i * Math.PI / 60
  return P(transform([Math.cos(t), Math.sin(t)])).join(',')
}).join(' '))
const drag = createDragger(svg, view, (_, p) => { point.value = norm2(p) > 1 ? p.map(v => v / norm2(p)) : p }, { step: 0.05 })
const names = ['Đầu vào x', '1. Quay bằng Vᵀ', '2. Co giãn bằng Σ', '3. Quay bằng U']
</script>

<template>
  <figure class="study-lab" aria-label="Ba bước hình học của phân tích SVD">
    <figcaption class="lab-title">Từ đĩa tròn đến ellipse qua ba phép biến đổi</figcaption>
    <p class="lab-lead">Kéo đầu mút x trong hình “Đầu vào”. Chọn từng bước rồi quan sát hình kết quả để theo dõi cùng vector. Hai phép quay giữ độ dài, còn Σ thay đổi độ dài theo từng trục.</p>
    <div class="lab-buttons" role="group" aria-label="Bước biến đổi">
      <button v-for="(name, i) in names" :key="i" type="button" :aria-pressed="stage === i" @click="stage = i">{{ name }}</button>
    </div>
    <div class="lab-pair svd-pair">
      <svg ref="svg" viewBox="0 0 360 360" role="group" aria-label="Đĩa đơn vị và vector đầu vào kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
        <line x1="20" y1="180" x2="340" y2="180" class="lab-axis" /><line x1="180" y1="20" x2="180" y2="340" class="lab-axis" />
        <circle cx="180" cy="180" :r="P([1, 0])[0] - 180" class="lab-region" />
        <line x1="180" y1="180" :x2="P(point)[0]" :y2="P(point)[1]" class="lab-accent" />
        <text x="24" y="32">Đầu vào x</text><text x="319" y="201">x₁</text><text x="190" y="29">x₂</text>
        <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" class="lab-dot-accent" pointer-events="none" />
        <circle :cx="P(point)[0]" :cy="P(point)[1]" r="30" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Vector đầu vào x" :aria-valuetext="fmtPoint(point)" @pointerdown="drag.start('x', $event)" @keydown="drag.key('x', point, $event)" />
      </svg>
      <svg viewBox="0 0 360 360" role="img" :aria-label="names[stage] + ' và ảnh của đĩa đơn vị'">
        <line x1="20" y1="180" x2="340" y2="180" class="lab-axis" /><line x1="180" y1="20" x2="180" y2="340" class="lab-axis" />
        <polyline :points="circle" class="lab-region" />
        <line v-for="(axis, i) in [[1, 0], [0, 1]]" :key="i" x1="180" y1="180" :x2="P(transform(axis))[0]" :y2="P(transform(axis))[1]" class="lab-guide" />
        <line x1="180" y1="180" :x2="P(result)[0]" :y2="P(result)[1]" class="lab-good" />
        <circle :cx="P(result)[0]" :cy="P(result)[1]" r="8" class="lab-dot" />
        <text x="24" y="32">{{ ['x', 'Vᵀx', 'ΣVᵀx', 'Ax = UΣVᵀx'][stage] }}</text>
      </svg>
    </div>
    <details class="lab-tasks lab-alternative"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-controls"><label>Giá trị kỳ dị σ₂ = {{ fmt(minor) }}<input v-model.number="minor" type="range" min="0" max="1.6" step="0.05" /></label></div>
    <div class="lab-readout" role="status">
      <p>x = {{ fmtPoint(point) }}, kết quả = {{ fmtPoint(result) }}. Độ dài thay đổi từ {{ fmt(norm2(point)) }} thành {{ fmt(norm2(result)) }}.</p>
      <p>σ₁ = 1,60, σ₂ = {{ fmt(minor) }}. Chuẩn phổ của A bằng 1,60. {{ minor === 0 ? 'A có hạng 1: Đĩa tròn bị ép thành đoạn thẳng. A không khả nghịch.' : `Số điều kiện κ₂(A) = ${fmt(1.6 / minor)}.` }}</p>
      <p>Vᵀ quay −30°, Σ co giãn theo hai trục, U quay +30°. Hình đường biên là ảnh của toàn bộ đường tròn đơn vị, không chỉ là quỹ đạo của điểm đang kéo.</p>
    </div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol>
      <li>Chọn bước quay thứ nhất. Vì sao điểm vẫn nằm trong đĩa đơn vị?</li>
      <li>Đặt σ₂ = 0 rồi kéo x. Những đầu vào khác nhau nào cho cùng đầu ra?</li>
      <li>Đặt σ₂ = σ₁. Ảnh của đĩa tròn có còn bị kéo dài theo một hướng riêng không?</li>
    </ol></details>
  </figure>
</template>

<style scoped>
.svd-pair { margin-top: var(--space-4); }
.point-hit { fill: transparent !important; stroke: transparent; }
.point-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 20px; }
</style>
