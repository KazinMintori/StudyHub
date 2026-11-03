<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'

const addSubclass = ref(true)
const step = ref(0)
const hierarchy = computed(() => new Map([
  ['Chó', addSubclass.value ? ['Thú'] : []],
  ['Thú', ['Động vật']]
]))
const trace = computed(() => {
  const queue = ['Chó']
  const known = new Set(queue)
  const frames = [{ inferred: [...known], checked: 'Sự thực ban đầu' }]
  while (queue.length) {
    const category = queue.shift()
    for (const parent of hierarchy.value.get(category) ?? []) {
      if (known.has(parent)) continue
      known.add(parent)
      queue.push(parent)
      frames.push({ inferred: [...known], checked: category + ' ⊆ ' + parent })
    }
  }
  frames.push({ inferred: [...known], checked: 'Không còn lớp cha mới' })
  return frames
})
const frame = computed(() => trace.value[Math.min(step.value, trace.value.length - 1)])
watch(addSubclass, () => { step.value = 0 })
</script>

<template>
  <section class="math-lab" aria-label="Suy luận thành viên qua lớp cha">
    <p>Dữ kiện ban đầu là Buster thuộc lớp Chó. Lớp Thú luôn là lớp con của Động vật.</p>
    <label><input v-model="addSubclass" type="checkbox"> Khai báo Chó là lớp con của Thú</label>
    <SimulationControls v-model="step" :max="trace.length - 1" :reset-key="addSubclass" />
    <div aria-live="polite">
      <p>{{ frame.checked }}</p>
      <ul>
        <li v-for="category in frame.inferred" :key="category">Buster thuộc lớp {{ category }}</li>
      </ul>
    </div>
    <p>Kết quả liệt kê các lớp suy ra được từ dữ kiện hiện tại.</p>
  </section>
</template>
