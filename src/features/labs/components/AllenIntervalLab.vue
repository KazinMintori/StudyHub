<script setup>
import { computed, ref } from 'vue'
const start = ref(2)
const length = ref(3)
const fixedStart = 5
const fixedEnd = 9
const end = computed(() => start.value + length.value)
const relation = computed(() => {
  const a = start.value, b = end.value, c = fixedStart, d = fixedEnd
  if (b < c) return 'Đứng trước'
  if (b === c) return 'Tiếp giáp bên trái'
  if (a > d) return 'Đứng sau'
  if (a === d) return 'Tiếp giáp bên phải'
  if (a === c && b === d) return 'Trùng nhau'
  if (a === c) return b < d ? 'Cùng đầu, I ngắn hơn' : 'Cùng đầu, I dài hơn'
  if (b === d) return a > c ? 'Cùng cuối, I ngắn hơn' : 'Cùng cuối, I dài hơn'
  if (a < c) return b < d ? 'Chồng lấn từ trái' : 'I chứa J'
  return b < d ? 'I nằm trong J' : 'Chồng lấn từ phải'
})
const x = t => 25 + t * 17
</script>

<template>
  <section class="math-lab" aria-label="Quan hệ giữa hai khoảng thời gian">
    <label>Điểm đầu I {{ start }} <input v-model.number="start" type="range" min="0" max="12"></label>
    <label>Độ dài I {{ length }} <input v-model.number="length" type="range" min="1" max="5"></label>
    <svg viewBox="0 0 330 118" width="100%" role="img" :aria-label="'Khoảng I từ ' + start + ' đến ' + end + ', khoảng J từ 5 đến 9'">
      <path d="M25 101 H314" stroke="currentColor" stroke-width="1"/>
      <g v-for="t in [0, 5, 9, 17]" :key="t">
        <path :d="'M'+x(t)+' 94 V103'" stroke="currentColor"/>
        <text :x="x(t)" y="116" text-anchor="middle" fill="currentColor" font-size="13">{{ t }}</text>
      </g>
      <text x="5" y="34" fill="currentColor">I</text>
      <text x="5" y="72" fill="currentColor">J</text>
      <rect :x="x(start)" y="21" :width="x(end)-x(start)" height="16" rx="3" fill="var(--lam)"/>
      <rect :x="x(fixedStart)" y="59" :width="x(fixedEnd)-x(fixedStart)" height="16" rx="3" fill="var(--ngoc)"/>
    </svg>
    <p aria-live="polite"><strong>{{ relation }}</strong> · I [{{ start }}, {{ end }}], J [5, 9]</p>
  </section>
</template>

<style scoped>
label { display: grid; gap: .25rem; margin-block: .75rem; }
svg { display: block; max-width: 540px; }
</style>
