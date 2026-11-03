<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'
const step = ref(0), alpha = ref(0.5)
const samples = [
  ['A','đi',-1,'B'], ['B','an toàn',1,null],
  ['A','đi',-1,'B'], ['B','mạo hiểm',4,null],
  ['A','đi',-1,'B'], ['B','an toàn',1,null],
  ['A','đi',-1,'B'], ['B','mạo hiểm',-2,null]
]
const gamma = 0.9
const trace = computed(() => {
  const q = { A: { đi: 0 }, B: { 'an toàn': 0, 'mạo hiểm': 0 } }
  const snapshot = () => ({ A: { ...q.A }, B: { ...q.B } })
  const frames = [{ q: snapshot() }]
  for (const [state, action, reward, next] of samples) {
    const old = q[state][action]
    const bestNext = next === null ? 0 : Math.max(...Object.values(q[next]))
    const target = reward + gamma * bestNext
    q[state][action] = old + alpha.value * (target - old)
    frames.push({ state, action, reward, next, old, bestNext, target, q: snapshot() })
  }
  return frames
})
const frame = computed(() => trace.value[step.value])
const fmt = n => n.toFixed(3)
watch(alpha, () => { step.value = 0 })
</script>

<template>
  <section class="math-lab" aria-label="Vết cập nhật Q-learning">
    <p>Chiết khấu 0,9. Vết mẫu cố định gồm tám bước chuyển.</p>
    <label>Tốc độ học <select v-model.number="alpha"><option :value="0.5">0,5</option><option :value="1">1</option></select></label>
    <SimulationControls v-model="step" :max="trace.length - 1" :reset-key="alpha" />
    <div aria-live="polite">
      <template v-if="step">
        <p>{{ frame.state }} → {{ frame.next ?? 'Kết thúc' }} · {{ frame.action }} · Thưởng {{ frame.reward }}</p>
        <p>Mục tiêu = {{ frame.reward }} + 0,9 × {{ fmt(frame.bestNext) }} = {{ fmt(frame.target) }}</p>
        <p>Q mới = {{ fmt(frame.old) }} + {{ alpha }} × ({{ fmt(frame.target) }} − {{ fmt(frame.old) }})</p>
      </template>
      <p>Q(A, đi) = {{ fmt(frame.q.A.đi) }}</p>
      <p>Q(B, an toàn) = {{ fmt(frame.q.B['an toàn']) }} · Q(B, mạo hiểm) = {{ fmt(frame.q.B['mạo hiểm']) }}</p>
    </div>
  </section>
</template>
