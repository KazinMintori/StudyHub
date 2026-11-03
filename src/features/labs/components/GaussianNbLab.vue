<script setup>
import { computed, ref } from 'vue'
const x = ref(5), sigma = ref(1), prior = ref(0.5)
const density = (value, mean) => Math.exp(-(((value - mean) / sigma.value) ** 2) / 2) / (sigma.value * Math.sqrt(2 * Math.PI))
const curve = mean => Array.from({length:101},(_,i) => (i?'L':'M') + (25+30*i/10) + ',' + (160-300*density(i/10,mean))).join(' ')
const scores = computed(() => [prior.value*density(x.value,3),(1-prior.value)*density(x.value,7)])
const posterior = computed(() => scores.value[0]/(scores.value[0]+scores.value[1]))
</script>
<template>
  <section class="math-lab gaussian-nb" aria-label="Likelihood Gaussian và hậu nghiệm">
    <label>Giá trị x {{ x }} <input type="range" v-model.number="x" min="0" max="10" step="0.5"></label>
    <label>Độ lệch chuẩn chung <select v-model.number="sigma"><option :value="1">1</option><option :value="2">2</option></select></label>
    <label>Tiên nghiệm nhãn A <select v-model.number="prior"><option :value="0.5">0,5</option><option :value="0.8">0,8</option></select></label>
    <svg viewBox="0 0 350 190" width="100%" role="img" aria-label="Hai đường mật độ Gaussian có trung bình 3 và 7">
      <path d="M25 160H325" stroke="currentColor" fill="none"/>
      <path :d="curve(3)" stroke="var(--vp-c-brand-1)" stroke-width="1.8" fill="none"/>
      <path :d="curve(7)" stroke="var(--vp-c-tip-1)" stroke-width="1.8" fill="none"/>
      <path :d="'M'+(25+30*x)+',12 V160'" stroke="currentColor" stroke-dasharray="3 3" fill="none"/>
      <text x="115" y="183" text-anchor="middle" fill="currentColor">A · μ = 3</text>
      <text x="235" y="183" text-anchor="middle" fill="currentColor">B · μ = 7</text>
    </svg>
    <p aria-live="polite">Mật độ tại x theo A {{ density(x,3).toFixed(4) }}, theo B {{ density(x,7).toFixed(4) }}. Hậu nghiệm A {{ (100*posterior).toFixed(1) }}%.</p>
    <p>Đường cong biểu diễn mật độ có điều kiện. Hậu nghiệm còn sử dụng tiên nghiệm của từng nhãn.</p>
  </section>
</template>
<style scoped>
label { display:grid;gap:.25rem;margin-block:.75rem; }
</style>
