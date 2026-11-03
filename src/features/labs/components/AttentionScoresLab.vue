<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'
import { attentionStep } from '../services/learning-models.mjs'
const query = ref('balanced'), mask = ref(false), step = ref(0)
const state = computed(() => attentionStep(query.value === 'balanced' ? [1, 1] : [2, 0], mask.value))
const fmt = value => Number.isFinite(value) ? value.toFixed(4) : '−∞'
watch([query, mask], () => { step.value = 0 })
</script>
<template>
  <section class="math-lab attention-scores" aria-label="Tính attention từng bước">
    <label>Truy vấn <select v-model="query"><option value="balanced">q = (1, 1)</option><option value="left">q = (2, 0)</option></select></label>
    <label><input type="checkbox" v-model="mask"> Che vị trí thứ hai</label>
    <p>k₁ = (1, 0), k₂ = (0, 1). v₁ = (1, 0), v₂ = (0, 2).</p>
    <SimulationControls v-model="step" :max="3" :reset-key="query + mask" />
    <div aria-live="polite">
      <p>1. Tích vô hướng {{ state.dots.map(fmt).join(', ') }}.</p>
      <p v-if="step >= 1">2. Chia căn bậc hai của 2 rồi áp dụng mặt nạ {{ state.scores.map(fmt).join(', ') }}.</p>
      <template v-if="step >= 2">
        <p>3. Softmax {{ state.probabilities.map(fmt).join(', ') }}.</p>
        <div v-for="(value,index) in state.probabilities" :key="index" class="attention-bar"><span :style="{width:(100*value)+'%'}"></span><b>Vị trí {{ index+1 }} · {{ (100*value).toFixed(1) }}%</b></div>
      </template>
      <p v-if="step >= 3">4. Tổng có trọng số của hai vector giá trị là ({{ state.result.map(fmt).join(', ') }}).</p>
    </div>
  </section>
</template>
<style scoped>
label { display:grid;gap:.25rem;margin-block:.75rem; }
.attention-bar { position:relative;min-height:36px;border:1px solid var(--vp-c-divider);margin-block:8px; }
.attention-bar span { position:absolute;inset:0 auto 0 0;background:var(--vp-c-brand-soft); }
.attention-bar b { position:relative;padding:8px;font-size:14px;font-weight:400; }
</style>
