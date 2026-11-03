<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'

const image = [[1,1,2,4],[5,6,7,8],[3,2,1,0],[1,2,3,4]]
const kernel = [[-1,1],[-1,1]]
const mode = ref('conv')
const step = ref(0)
const stride = computed(() => mode.value === 'conv' ? 1 : 2)
const positions = computed(() => {
  const list = []
  for (let row = 0; row < 3; row += stride.value) {
    for (let col = 0; col < 3; col += stride.value) {
      const patch = image.slice(row,row+2).flatMap(line => line.slice(col,col+2))
      const terms = patch.map((value,i) => value * kernel.flat()[i])
      list.push({row,col,patch,terms,value:mode.value === 'conv' ? terms.reduce((a,b)=>a+b,0) : Math.max(...patch)})
    }
  }
  return list
})
const current = computed(() => positions.value[Math.min(step.value,positions.value.length-1)])
watch(mode, () => { step.value = 0 })
</script>

<template>
  <section class="math-lab" aria-label="Cửa sổ trượt CNN">
    <label>Phép tính
      <select v-model="mode"><option value="conv">Tích chập CNN</option><option value="pool">Max pooling</option></select>
    </label>
    <p>Cửa sổ 2 × 2, bước trượt {{ stride }}, không đệm biên.</p>
    <SimulationControls v-model="step" :max="positions.length-1" :reset-key="mode" />
    <div class="matrix" aria-label="Ma trận đầu vào">
      <template v-for="(line,r) in image" :key="r">
        <span v-for="(value,c) in line" :key="c" :class="{selected:r>=current.row && r<current.row+2 && c>=current.col && c<current.col+2}">{{ value }}</span>
      </template>
    </div>
    <p aria-live="polite">
      Cửa sổ ({{ current.row }}, {{ current.col }}), đánh số từ 0.
      {{ mode==='conv' ? 'Nhân theo bộ lọc (−1, 1, −1, 1) rồi cộng: ' + current.terms.join(', ') : 'Lấy lớn nhất trong: ' + current.patch.join(', ') }}.
      Kết quả <strong>{{ current.value }}</strong>.
    </p>
    <div class="matrix output" :style="{gridTemplateColumns:'repeat('+(mode==='conv'?3:2)+', 1fr)'}" aria-label="Ma trận đầu ra">
      <span v-for="(position,i) in positions" :key="i" :class="{selected:i===step}">{{ i<=step ? position.value : '·' }}</span>
    </div>
  </section>
</template>

<style scoped>
.matrix { display:grid;grid-template-columns:repeat(4,1fr);gap:4px;max-width:15rem;margin-block:1rem; }
.matrix span { display:grid;place-items:center;min-height:40px;border:1px solid var(--vp-c-divider);border-radius:4px; }
.selected { outline:2px solid var(--vp-c-brand-1);outline-offset:-2px;background:var(--vp-c-bg-soft); }
</style>
