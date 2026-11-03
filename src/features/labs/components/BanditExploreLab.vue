<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'
const epsilon = ref(0.1), changed = ref(false), seed = ref(7), step = ref(0)
const trace = computed(() => {
  let randomState = seed.value
  const random = () => { randomState = (1664525 * randomState + 1013904223) >>> 0; return randomState / 4294967296 }
  const counts = [0, 0], values = [0, 0], frames = [{ counts: [...counts], values: [...values], total: 0 }]
  let total = 0
  for (let time = 1; time <= 60; time++) {
    const explore = random() < epsilon.value
    const randomAction = random() < 0.5 ? 0 : 1
    const outcome = random()
    const action = explore ? randomAction : Number(values[1] > values[0])
    const redProbability = changed.value && time > 30 ? 0.25 : 0.75
    const reward = action === 0 ? 1 : outcome < redProbability ? 2 : 0
    counts[action]++
    values[action] += (reward - values[action]) / counts[action]
    total += reward
    frames.push({ counts: [...counts], values: [...values], total, time, action, reward, explore, redProbability })
  }
  return frames
})
const frame = computed(() => trace.value[step.value])
watch([epsilon, changed, seed], () => { step.value = 0 })
</script>
<template>
  <section class="math-lab bandit-explore" aria-label="Khám phá và khai thác hai máy">
    <label>Epsilon <select v-model.number="epsilon"><option :value="0">0</option><option :value="0.1">0,1</option><option :value="0.3">0,3</option></select></label>
    <label><input v-model="changed" type="checkbox"> Máy đỏ giảm xác suất thắng sau lượt 30</label>
    <label>Chuỗi ngẫu nhiên <select v-model.number="seed"><option :value="7">7</option><option :value="13">13</option><option :value="29">29</option></select></label>
    <SimulationControls v-model="step" :max="60" :reset-key="[epsilon,changed,seed].join('|')" />
    <div aria-live="polite">
      <p v-if="step">Lượt {{ step }} · {{ frame.explore ? 'Nhánh chọn ngẫu nhiên' : 'Nhánh chọn giá trị ước lượng lớn nhất' }} · Máy {{ frame.action===0?'xanh':'đỏ' }} · Thưởng {{ frame.reward }}.</p>
      <p>Máy xanh nhận 1 chắc chắn. Máy đỏ nhận 2 với xác suất {{ step ? frame.redProbability : 0.75 }}, còn lại nhận 0.</p>
      <p v-for="(count,i) in frame.counts" :key="i">Máy {{ i===0?'xanh':'đỏ' }} · {{ count }} lượt · Trung bình ước lượng {{ frame.values[i].toFixed(3) }}.</p>
      <p>Tổng thưởng {{ frame.total }}.</p>
    </div>
    <p>Khởi tạo hai ước lượng bằng 0 và ưu tiên máy xanh khi hòa. Với epsilon bằng 0, ví dụ này có thể giữ lựa chọn ban đầu. Trung bình mẫu còn chứa dữ liệu cũ khi luật chơi thay đổi.</p>
  </section>
</template>
<style scoped>
label { display:grid;gap:.25rem;margin-block:.75rem; }
</style>
