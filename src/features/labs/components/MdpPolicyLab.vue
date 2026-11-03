<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'
import { tinyModel, policyIterations, actionValue } from '../services/mdp-model.mjs'
const gamma = ref(0.9), step = ref(0)
const model = tinyModel()
const trace = computed(() => policyIterations(model, gamma.value))
const frame = computed(() => trace.value[step.value])
watch(gamma, () => { step.value = 0 })
</script>
<template>
  <section class="math-lab mdp-policy" aria-label="Đánh giá và cải tiến chính sách MDP">
    <p>Một trạng thái đang sống có hai lựa chọn. Ở lại nhận 1 rồi trở về chính nó. Thoát nhận 3 rồi kết thúc.</p>
    <label>Chiết khấu <select v-model.number="gamma"><option :value="0.5">0,5</option><option :value="0.9">0,9</option></select></label>
    <SimulationControls v-model="step" :max="trace.length - 1" :reset-key="gamma" />
    <div aria-live="polite">
      <h4>{{ frame.phase }}</h4>
      <p>Chính sách hiện tại {{ frame.policy.alive === 'stay' ? 'Ở lại' : 'Thoát' }}.</p>
      <p>Giá trị đã đánh giá {{ frame.values.alive.toFixed(4) }}.</p>
      <p>Q ở lại {{ actionValue(model, 'alive', 'stay', frame.values, gamma).toFixed(4) }}. Q thoát 3.</p>
      <p v-if="frame.phase === 'Cải tiến'">Bảng giá trị còn thuộc chính sách vừa đánh giá. Bước tiếp theo sẽ đánh giá chính sách mới.</p>
    </div>
  </section>
</template>
