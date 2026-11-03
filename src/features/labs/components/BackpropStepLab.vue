<script setup>
import { computed, ref } from 'vue'
import SimulationControls from './SimulationControls.vue'
import { networkStep } from '../services/learning-models.mjs'
const step = ref(0), iteration = ref(0)
const parameters = ref({ w: 0.4, b: 0.1, v: -0.7, c: 0.2 })
const trace = computed(() => networkStep(parameters.value))
const fmt = value => value.toFixed(5)
function update() { parameters.value = trace.value.after; iteration.value++; step.value = 0 }
function reset() { parameters.value = { w: 0.4, b: 0.1, v: -0.7, c: 0.2 }; iteration.value = 0; step.value = 0 }
</script>
<template>
  <section class="math-lab backprop-step" aria-label="Lan truyền thuận và ngược từng bước">
    <p>Mạng một nút ẩn và một đầu ra sigmoid. Đầu vào 0,6, nhãn 1, hàm mất mát là nửa bình phương sai số.</p>
    <SimulationControls v-model="step" :max="5" :reset-key="iteration" />
    <svg viewBox="0 0 330 100" width="100%" role="img" aria-label="Đầu vào nối đến nút ẩn rồi đến đầu ra">
      <path d="M59 50H141M189 50H271" stroke="currentColor" stroke-width="1.5"/>
      <g v-for="(label,index) in ['x','h','y']" :key="label">
        <circle :cx="35+130*index" cy="50" r="24" fill="var(--vp-c-bg-soft)" stroke="currentColor" stroke-width="1.5"/>
        <text :x="35+130*index" y="56" text-anchor="middle" fill="currentColor">{{ label }}</text>
      </g>
      <text x="100" y="25" text-anchor="middle" fill="currentColor">w</text>
      <text x="230" y="25" text-anchor="middle" fill="currentColor">v</text>
    </svg>
    <div aria-live="polite">
      <p v-if="step >= 0">1. Nút ẩn h = {{ fmt(trace.hidden) }}</p>
      <p v-if="step >= 1">2. Đầu ra y = {{ fmt(trace.output) }}</p>
      <p v-if="step >= 2">3. Mất mát = {{ fmt(trace.loss) }}</p>
      <p v-if="step >= 3">4. Sai số cục bộ đầu ra = {{ fmt(trace.outputDelta) }}</p>
      <p v-if="step >= 4">5. Sai số cục bộ nút ẩn = {{ fmt(trace.hiddenDelta) }}. Giá trị v dùng ở đây là trọng số trước cập nhật.</p>
      <template v-if="step >= 5">
        <p>6. Gradient w = {{ fmt(trace.gradient.w) }}, b = {{ fmt(trace.gradient.b) }}, v = {{ fmt(trace.gradient.v) }}, c = {{ fmt(trace.gradient.c) }}.</p>
        <button type="button" class="study-button" @click="update">Cập nhật với tốc độ học 0,5</button>
      </template>
      <p>Số lần cập nhật {{ iteration }}.</p>
    </div>
    <button type="button" class="study-button" @click="reset">Khôi phục trọng số ban đầu</button>
  </section>
</template>
