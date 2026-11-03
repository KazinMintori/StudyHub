<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'
const mode = ref('gcd'), step = ref(0)
const trace = computed(() => {
  if (mode.value === 'gcd') {
    const frames = []
    let a = 10, b = 15
    while (b !== 0) {
      const remainder = a % b
      frames.push({ call: 'gcd(' + a + ', ' + b + ', G)', operation: a + ' mod ' + b + ' = ' + remainder, returned: 'G chưa có giá trị' })
      a = b
      b = remainder
    }
    frames.push({ call: 'gcd(' + a + ', 0, G)', operation: 'Khớp trường hợp cơ sở', returned: 'G = ' + a })
    return frames
  }
  const list = [2, 3, 5, 7]
  return list.map((_, index) => ({
    call: 'findLast([' + list.slice(index).join(', ') + '], X)',
    operation: index === list.length - 1 ? 'Danh sách một phần tử, khớp trường hợp cơ sở' : 'Bỏ đầu danh sách rồi gọi trên đuôi',
    returned: index === list.length - 1 ? 'X = 7 truyền về mọi lời gọi đang chờ' : 'X chưa có giá trị'
  }))
})
const frame = computed(() => trace.value[step.value])
watch(mode, () => { step.value = 0 })
</script>
<template>
  <section class="math-lab prolog-recursion" aria-label="Truy vết đệ quy Prolog">
    <label>Ví dụ <select v-model="mode"><option value="gcd">Euclid</option><option value="last">Phần tử cuối danh sách</option></select></label>
    <SimulationControls v-model="step" :max="trace.length - 1" :reset-key="mode" />
    <div aria-live="polite">
      <pre><code>{{ frame.call }}</code></pre>
      <p>{{ frame.operation }}</p>
      <p>{{ frame.returned }}</p>
    </div>
  </section>
</template>
