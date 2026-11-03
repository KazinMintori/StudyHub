<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'

const alpha = ref(1)
const input = ref('ưu đãi họp')
const step = ref(0)
const vocabulary = ['ưu', 'đãi', 'họp']
const classes = [
  { label: 'Thư rác', prior: 0.5, counts: [3, 2, 0] },
  { label: 'Thư thường', prior: 0.5, counts: [0, 1, 4] }
]
const words = computed(() => input.value.toLowerCase().trim().split(/\s+/).filter(Boolean).slice(0, 24))
const known = computed(() => words.value.filter(word => vocabulary.includes(word)))
const ignored = computed(() => words.value.filter(word => !vocabulary.includes(word)))
const scores = computed(() => classes.map(row => {
  const denominator = row.counts.reduce((a, b) => a + b, 0) + vocabulary.length * alpha.value
  const terms = known.value.slice(0, step.value).map(word => {
    const probability = (row.counts[vocabulary.indexOf(word)] + alpha.value) / denominator
    return { word, probability }
  })
  const score = terms.reduce((sum, term) => sum + Math.log(term.probability), Math.log(row.prior))
  return { ...row, denominator, terms, score }
}))
const posterior = computed(() => {
  const peak = Math.max(...scores.value.map(row => row.score))
  if (!Number.isFinite(peak)) return null
  const weights = scores.value.map(row => Math.exp(row.score - peak))
  const total = weights.reduce((a, b) => a + b, 0)
  return weights.map(weight => weight / total)
})
watch([alpha, input], () => { step.value = 0 })
</script>

<template>
  <section class="math-lab" aria-label="Vết phân loại thư bằng Naive Bayes">
    <p>Từ vựng huấn luyện gồm ba token: ưu, đãi, họp. Hai nhãn có cùng xác suất tiên nghiệm.</p>
    <label>Thư cần phân loại <input v-model="input" maxlength="240" /></label>
    <label>Làm trơn <select v-model.number="alpha"><option :value="0">0</option><option :value="1">1</option><option :value="2">2</option></select></label>
    <p v-if="ignored.length">Bỏ qua token ngoài từ vựng: {{ ignored.join(', ') }}.</p>
    <SimulationControls v-model="step" :max="known.length" :reset-key="input + '|' + alpha" label="Token" />
    <div aria-live="polite">
      <article v-for="(row, index) in scores" :key="row.label">
        <h4>{{ row.label }}</h4>
        <p>Số đếm theo thứ tự từ vựng: {{ row.counts.join(', ') }}. Mẫu số {{ row.denominator }}.</p>
        <ul><li v-for="(term, i) in row.terms" :key="i">{{ term.word }} · Xác suất {{ term.probability.toFixed(4) }}</li></ul>
        <p>Điểm log {{ row.score.toFixed(4) }}. <span v-if="posterior">Hậu nghiệm theo tiền tố đang xét {{ (100 * posterior[index]).toFixed(1) }}%.</span></p>
      </article>
      <p v-if="!posterior">Cả hai nhãn đều có điểm bằng 0 trên thang xác suất. Không chuẩn hóa được, hãy thử làm trơn.</p>
    </div>
  </section>
</template>

<style scoped>
label { display: grid; gap: .25rem; margin-block: .75rem; }
input { min-width: 0; }
</style>
