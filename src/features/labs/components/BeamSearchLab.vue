<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'
import { beamSteps } from '../services/learning-models.mjs'
const width = ref(1), step = ref(0)
const trace = computed(() => beamSteps(width.value))
const frame = computed(() => trace.value[step.value])
watch(width, () => { step.value = 0 })
</script>
<template>
  <section class="math-lab beam-search" aria-label="Truy vết beam search">
    <label>Độ rộng beam <select v-model.number="width"><option :value="1">1 · Tham lam</option><option :value="2">2</option><option :value="3">3</option></select></label>
    <p>Ở gốc, A có xác suất 0,6 và B có xác suất 0,4. Sau A là x (0,6) hoặc y (0,4), sau B là z (1). Sau A x, EOS và w cùng có xác suất 0,5. Các tiền tố còn lại kết thúc bằng EOS với xác suất 1.</p>
    <SimulationControls v-model="step" :max="trace.length - 1" :reset-key="width" />
    <div aria-live="polite">
      <h4>Giữ lại</h4>
      <p v-for="(beam,i) in frame.kept" :key="i">{{ beam.tokens.join(' ') || 'Tiền tố rỗng' }} · Tích xác suất {{ Math.exp(beam.log).toFixed(3) }} · Điểm log {{ beam.log.toFixed(3) }}</p>
      <h4 v-if="frame.removed.length">Loại khỏi beam</h4>
      <p v-for="(beam,i) in frame.removed" :key="i">{{ beam.tokens.join(' ') }} · {{ Math.exp(beam.log).toFixed(3) }}</p>
    </div>
    <p>Ví dụ dùng điểm log chưa chuẩn hóa độ dài và tập chuyển đã cho. Độ rộng hữu hạn có thể loại bỏ tiền tố của câu tốt hơn.</p>
  </section>
</template>
