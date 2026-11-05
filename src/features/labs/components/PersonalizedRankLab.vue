<script setup>
import { computed, ref } from 'vue'
import { pageGraph, personalizedRank } from '../services/data-algorithms.mjs'
const beta = ref(0.8), steps = ref(40), topic = ref('uniform'), dangling = ref(false)
const teleport = computed(() => topic.value === 'A' ? [1, 0, 0, 0] : topic.value === 'C' ? [0, 0, 1, 0] : [0.25, 0.25, 0.25, 0.25])
const result = computed(() => personalizedRank(dangling.value ? [pageGraph[0], pageGraph[1], [], pageGraph[3]] : pageGraph, teleport.value, beta.value, steps.value))
const names = ['A', 'B', 'C', 'D']
const fmt = x => x.toLocaleString('vi-VN', x !== 0 && Math.abs(x) < 0.0001
  ? { notation: 'scientific', maximumFractionDigits: 2 }
  : { maximumFractionDigits: 5 })
</script>

<template>
  <section class="study-lab rank-lab" aria-label="Mô phỏng PageRank cá nhân hóa">
    <p class="lab-title">Cùng mạng liên kết, khác điểm khởi hành</p>
    <p class="lab-lead">Đồ thị A → B, C, D; B → A, D; C → A; D → B, C. Mỗi lần thử bắt đầu từ phân phối đều. Nút cụt luôn phân phối điểm đều đến bốn trang.</p>
    <div class="lab-controls">
      <label>Phân phối nhảy
        <select v-model="topic"><option value="uniform">Đều trên A, B, C, D</option><option value="A">Chỉ nhảy đến A</option><option value="C">Chỉ nhảy đến C</option></select>
      </label>
      <label>Xác suất đi theo liên kết β = {{ fmt(beta) }}
        <input v-model.number="beta" type="range" min="0" max="0.95" step="0.05">
      </label>
      <label>Số vòng lặp = {{ steps }}
        <input v-model.number="steps" type="range" min="0" max="100" step="1">
      </label>
      <label class="lab-check"><input v-model="dangling" type="checkbox">Bỏ cạnh C → A để tạo nút cụt</label>
    </div>
    <div class="rank-bars" aria-label="Điểm của bốn trang">
      <div v-for="(name, i) in names" :key="name" class="rank-row">
        <span>{{ name }}</span><div class="rank-track"><div class="rank-fill" :style="{ width: `${100 * result.rank[i]}%` }" /></div><output>{{ fmt(result.rank[i]) }}</output>
      </div>
    </div>
    <div class="lab-readout" role="status" aria-live="polite">
      <p>Sau {{ steps }} vòng, tổng điểm là {{ fmt(result.rank.reduce((a, b) => a + b, 0)) }}.</p>
      <p v-if="steps && result.delta">Độ thay đổi ở vòng cuối xấp xỉ {{ fmt(result.delta) }}. Cận suy từ mô hình số học lý tưởng xấp xỉ {{ fmt(result.errorBound) }}, chưa cộng sai số làm tròn của máy.</p>
      <p v-else-if="steps">Vòng cuối không đổi ở độ chính xác số thực của máy. Điều này không chứng minh sai số toán học bằng 0.</p>
      <p v-else>Chưa cập nhật. Mỗi trang đang giữ 0,25 điểm.</p>
    </div>
    <details class="lab-tasks"><summary>Thử nghiệm và giải thích</summary><ol>
      <li>Đặt β bằng 0, đổi điểm nhảy rồi giải thích vì sao chỉ cần một vòng để điểm bằng phân phối nhảy.</li>
      <li>Giữ β bằng 0,8, đổi từ A sang C. Phần nào của mạng nhận thêm điểm sau nhiều vòng?</li>
      <li>Bỏ cạnh C → A, chọn nhảy chỉ đến A. Tổng điểm có còn bằng 1 không? Phân biệt quy tắc nút cụt với phân phối nhảy.</li>
      <li>Đặt β bằng 0,95 và giảm số vòng. Độ thay đổi nhỏ đã đủ để kết luận sai số nhỏ đến mức nào?</li>
    </ol></details>
  </section>
</template>

<style scoped>
.rank-bars { display: grid; gap: var(--space-3); margin-top: var(--space-5); }
.rank-row { display: grid; grid-template-columns: 1.2em minmax(0, 1fr) 5.5em; align-items: center; gap: var(--space-2); font-variant-numeric: tabular-nums; }
.rank-track { height: 20px; background: var(--tim-soft); border-radius: var(--radius); }
.rank-fill { height: 100%; background: var(--tim); border-radius: var(--radius); }
.rank-row output { text-align: right; }
</style>
