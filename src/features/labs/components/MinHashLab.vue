<script setup>
import { computed, ref } from 'vue'
import { jaccard, permutations, minHash } from '../services/data-algorithms.mjs'
const choices = ['a', 'b', 'c', 'd', 'e', 'f']
const left = ref(['a', 'b', 'c', 'd']), right = ref(['b', 'c', 'd', 'e']), index = ref(0)
const a = computed(() => new Set(left.value)), b = computed(() => new Set(right.value))
const measure = computed(() => jaccard(a.value, b.value))
const union = computed(() => choices.filter(x => a.value.has(x) || b.value.has(x)))
const orders = computed(() => [...permutations(union.value)])
const selected = computed(() => orders.value[Math.min(index.value, orders.value.length - 1)])
const hashA = computed(() => minHash(a.value, selected.value)), hashB = computed(() => minHash(b.value, selected.value))
const collisions = computed(() => orders.value.filter(p => minHash(a.value, p) === minHash(b.value, p)).length)
const valid = computed(() => a.value.size && b.value.size)
</script>

<template>
  <section class="study-lab minhash-lab" aria-label="Mô phỏng định lý MinHash bằng hoán vị">
    <p class="lab-title">Phần tử đầu tiên quyết định việc trùng chữ ký</p>
    <p class="lab-lead">Chọn hai tập trên vũ trụ a–f. Mô phỏng liệt kê toàn bộ hoán vị của hợp hai tập, nên tỷ lệ trùng được tính chính xác, không qua băm xấp xỉ.</p>
    <div class="lab-pair sets">
      <fieldset><legend>Tập A</legend><label v-for="x in choices" :key="x"><input v-model="left" type="checkbox" :value="x">{{ x }}</label></fieldset>
      <fieldset><legend>Tập B</legend><label v-for="x in choices" :key="x"><input v-model="right" type="checkbox" :value="x">{{ x }}</label></fieldset>
    </div>
    <div v-if="valid">
      <label class="order-control">Hoán vị số {{ Math.min(index + 1, orders.length) }} trong {{ orders.length }}
        <input v-model.number="index" type="range" min="0" :max="orders.length - 1" step="1">
      </label>
      <ol class="permutation" aria-label="Thứ tự hoán vị hiện tại"><li v-for="x in selected" :key="x" :class="{ shared: a.has(x) && b.has(x) }">{{ x }}<small>{{ a.has(x) && b.has(x) ? 'A ∩ B' : a.has(x) ? 'A' : 'B' }}</small></li></ol>
      <div class="lab-readout" role="status" aria-live="polite">
        <p>MinHash(A) = {{ hashA }}, MinHash(B) = {{ hashB }}. Hai chữ ký {{ hashA === hashB ? 'trùng nhau' : 'khác nhau' }}.</p>
        <p>Giao có {{ measure.intersection }} phần tử, hợp có {{ measure.union }} phần tử. Jaccard = {{ measure.intersection }}/{{ measure.union }}.</p>
        <p>Có {{ collisions }}/{{ orders.length }} hoán vị cho chữ ký trùng. Tỷ lệ này bằng Jaccard, xấp xỉ {{ (100 * measure.similarity).toLocaleString('vi-VN', { maximumFractionDigits: 2 }) }}%.</p>
      </div>
    </div>
    <div v-else class="lab-readout" role="status"><p>Chọn ít nhất một phần tử cho mỗi tập để xét định lý MinHash. Quy ước Jaccard cho hai tập rỗng là 1, nhưng tập rỗng không có phần tử đầu tiên để tạo chữ ký.</p></div>
    <details class="lab-tasks"><summary>Thử nghiệm và giải thích</summary><ol>
      <li>Giữ hai tập ban đầu. Chọn một hoán vị có phần tử đầu thuộc giao, rồi một hoán vị có phần tử đầu chỉ thuộc A.</li>
      <li>Tạo hai tập rời nhau. Có hoán vị nào làm hai chữ ký trùng không?</li>
      <li>Cho A là tập con của B. Tại sao mẫu số của xác suất vẫn là kích thước hợp?</li>
    </ol></details>
  </section>
</template>

<style scoped>
.sets { margin-top: var(--space-4); }
fieldset { border: 1px solid var(--rule); border-radius: var(--radius); padding: var(--space-3); display: flex; flex-wrap: wrap; gap: var(--space-2); min-width: 0; }
legend { padding: 0 var(--space-2); }
fieldset label { display: flex; gap: var(--space-2); align-items: center; min-height: 44px; min-width: 44px; }
.order-control { margin-top: var(--space-4); }
.permutation { display: flex; flex-wrap: wrap; gap: var(--space-2); padding: 0; list-style: none; }
.permutation li { display: grid; text-align: center; padding: var(--space-2); min-width: 42px; border: 1px solid var(--rule); border-radius: var(--radius); }
.permutation li.shared { background: var(--tim-soft); border-color: var(--tim); }
.permutation small { font-size: var(--fs-small); }
</style>
