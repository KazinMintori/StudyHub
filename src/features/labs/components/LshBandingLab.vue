<script setup>
import { computed, ref } from 'vue'
import { candidateProbability, permutationSample, minHash, matchingBands, jaccard } from '../services/data-algorithms.mjs'
const bands = ref(20), rows = ref(5), similarity = ref(0.8), threshold = ref(0.7)
const probability = computed(() => candidateProbability(similarity.value, bands.value, rows.value))
const half = computed(() => (1 - 2 ** (-1 / bands.value)) ** (1 / rows.value))
const heuristic = computed(() => bands.value ** (-1 / rows.value))
const points = computed(() => Array.from({ length: 101 }, (_, i) => `${45 + 3 * i},${230 - 190 * candidateProbability(i / 100, bands.value, rows.value)}`).join(' '))
const universe = ['a', 'b', 'c', 'd', 'e', 'f']
const a = new Set(['a', 'b', 'c', 'd']), b = new Set(['b', 'c', 'd', 'e'])
const example = computed(() => {
  const orders = permutationSample(universe, bands.value * rows.value)
  const sa = orders.map(p => minHash(a, p)), sb = orders.map(p => minHash(b, p))
  return { matches: matchingBands(sa, sb, rows.value), sa, sb }
})
const actual = jaccard(a, b).similarity
const fmt = x => x.toLocaleString('vi-VN', { maximumFractionDigits: 4 })
</script>

<template>
  <section class="study-lab lsh-lab" aria-label="Mô phỏng phân dải MinHash và xác suất ứng viên">
    <p class="lab-title">Điều chỉnh dải để thay đổi xác suất giữ cặp</p>
    <p class="lab-lead">Đường cong giả sử các hàng MinHash độc lập và không có va chạm phụ khi băm dải. Cặp minh họa bên dưới dùng một mẫu hoán vị với hạt giống cố định, nên không thay thế chứng minh xác suất.</p>
    <div class="lab-controls">
      <label>Số dải b = {{ bands }}<input v-model.number="bands" type="range" min="1" max="30" step="1"></label>
      <label>Số hàng mỗi dải r = {{ rows }}<input v-model.number="rows" type="range" min="1" max="10" step="1"></label>
      <label>Độ tương đồng s = {{ fmt(similarity) }}<input v-model.number="similarity" type="range" min="0" max="1" step="0.01"></label>
      <label>Ngưỡng xác minh τ = {{ fmt(threshold) }}<input v-model.number="threshold" type="range" min="0" max="1" step="0.05"></label>
    </div>
    <svg viewBox="0 0 380 285" role="img" aria-label="Xác suất thành ứng viên theo độ tương đồng từ 0 đến 1">
      <line x1="45" y1="230" x2="345" y2="230" class="lab-axis"/><line x1="45" y1="40" x2="45" y2="230" class="lab-axis"/>
      <line x1="45" y1="135" x2="345" y2="135" class="lab-guide"/>
      <polyline :points="points" class="lab-accent"/>
      <circle :cx="45 + 300 * similarity" :cy="230 - 190 * probability" r="5" class="lab-dot-accent"/>
      <text x="15" y="44">1</text><text x="7" y="140">0,5</text><text x="20" y="235">0</text>
      <text x="43" y="253">0</text><text x="338" y="253">1</text>
      <text x="55" y="23">Xác suất thành ứng viên</text><text x="124" y="276">Độ tương đồng s</text>
    </svg>
    <div class="lab-readout" role="status" aria-live="polite">
      <p>Chữ ký có {{ bands * rows }} hàng. Với s = {{ fmt(similarity) }}, xác suất ứng viên xấp xỉ {{ fmt(probability) }}.</p>
      <p>Mốc xác suất 1/2 có s xấp xỉ {{ fmt(half) }}. Mốc gần đúng b mũ (−1/r) xấp xỉ {{ fmt(heuristic) }}.</p>
    </div>
    <p>Cặp A = {a, b, c, d} và B = {b, c, d, e} có Jaccard bằng 0,6. Mỗi ô thể hiện một dải của mẫu chữ ký cố định.</p>
    <div class="band-grid" aria-label="Các dải trùng hoặc khác"><span v-for="(match, i) in example.matches" :key="i" :class="{ match }">{{ i + 1 }}: {{ match ? 'Trùng' : 'Khác' }}</span></div>
    <div class="lab-readout" role="status" aria-live="polite">
      <p>Có {{ example.matches.filter(Boolean).length }} dải trùng. {{ example.matches.some(Boolean) ? 'Cặp được đưa sang bước xác minh.' : 'Cặp bị bỏ qua, không được xác minh.' }}</p>
      <p v-if="example.matches.some(Boolean)">Kiểm tra Jaccard chính xác với τ = {{ fmt(threshold) }}: {{ actual >= threshold ? 'Giữ cặp vì 0,6 ≥ τ.' : 'Loại cặp vì 0,6 < τ.' }}</p>
      <p v-else-if="actual >= threshold">Với ngưỡng đã chọn, đây là một cặp đạt yêu cầu bị bỏ sót trong mẫu này.</p>
    </div>
    <details class="lab-tasks"><summary>Thử nghiệm và giải thích</summary><ol>
      <li>Giữ r cố định, tăng b. Xác suất giữ cặp thay đổi thế nào, và chữ ký dài thêm bao nhiêu hàng?</li>
      <li>So sánh b = 20, r = 5 với b = 10, r = 10. Cả hai có 100 hàng, nhưng có cùng đường cong không?</li>
      <li>Đổi ngưỡng xác minh. Tại sao đường cong tạo ứng viên giữ nguyên?</li>
    </ol></details>
  </section>
</template>

<style scoped>
.lsh-lab svg { margin-top: var(--space-4); }
.band-grid { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.band-grid span { border: 1px solid var(--rule); border-radius: var(--radius); padding: var(--space-2); font-size: var(--fs-small); }
.band-grid span.match { background: var(--tim-soft); border-color: var(--tim); }
</style>
