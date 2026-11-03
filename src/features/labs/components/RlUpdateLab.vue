<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'

const mode = ref('td')
const step = ref(0)
const alpha = ref(0.5)
const gamma = ref(0.9)
const episode = [
  { state: 'A', action: 'đi', reward: -1, next: 'B' },
  { state: 'B', action: 'thoát', reward: 4, next: 'Kết thúc' }
]
const trace = computed(() => {
  const values = { A: 0, B: 0 }
  const frames = [{ message: 'Bảng ban đầu', values: { ...values } }]
  const counts = { A: 0, B: 0 }
  for (let run = 1; run <= 3; run++) {
    for (const [index, item] of episode.entries()) {
      const old = values[item.state]
      const continuation = item.next === 'Kết thúc' ? 0 : values[item.next]
      let target = item.reward + gamma.value * continuation
      let rate = alpha.value
      if (mode.value === 'mc') {
        target = episode.slice(index).reduce((sum, move, k) => sum + gamma.value ** k * move.reward, 0)
        rate = 1 / ++counts[item.state]
      }
      values[item.state] = old + rate * (target - old)
      frames.push({ ...item, old, target, rate, run, values: { ...values } })
    }
  }
  return frames
})
const frame = computed(() => trace.value[step.value])
const format = n => n.toFixed(3)
watch([mode, alpha, gamma], () => { step.value = 0 })
</script>

<template>
  <section class="math-lab" aria-label="So sánh cập nhật Monte Carlo và TD">
    <label>Phương pháp
      <select v-model="mode"><option value="td">TD(0)</option><option value="mc">Monte Carlo</option></select>
    </label>
    <label>Chiết khấu <select v-model.number="gamma"><option :value="0.9">0,9</option><option :value="1">1</option></select></label>
    <label v-if="mode === 'td'">Tốc độ học <select v-model.number="alpha"><option :value="0.5">0,5</option><option :value="1">1</option></select></label>
    <p>A → B nhận −1. B → Kết thúc nhận 4. Cùng một đoạn được quan sát ba lần.</p>
    <p v-if="mode === 'mc'">Mỗi bước bên dưới xử lý một lượt ghé sau khi đã quan sát hết đoạn.</p>
    <SimulationControls v-model="step" :max="trace.length - 1" :reset-key="[mode, alpha, gamma].join('|')" />
    <div aria-live="polite">
      <p v-if="!step">{{ frame.message }}</p>
      <template v-else>
        <p>Đoạn {{ frame.run }} · {{ frame.state }} → {{ frame.next }} · Thưởng {{ frame.reward }}</p>
        <p>Mục tiêu {{ format(frame.target) }} · Hệ số cập nhật {{ format(frame.rate) }}</p>
        <p>Giá trị mới = {{ format(frame.old) }} + {{ format(frame.rate) }} × ({{ format(frame.target) }} − {{ format(frame.old) }})</p>
      </template>
      <p>V(A) = {{ format(frame.values.A) }} · V(B) = {{ format(frame.values.B) }}</p>
    </div>
  </section>
</template>
