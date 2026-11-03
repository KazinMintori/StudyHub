<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'
import { gridModel, directions, valueIterations, actionValue, greedyAction } from '../services/mdp-model.mjs'
const noise = ref(0.2), living = ref(0), gamma = ref(0.9), convention = ref('exit')
const step = ref(0), selected = ref('2,2'), action = ref('E')
const model = computed(() => gridModel({ noise: noise.value, living: living.value, convention: convention.value }))
const key = computed(() => [noise.value, living.value, gamma.value, convention.value].join('|'))
const frames = computed(() => valueIterations(model.value, gamma.value, 100))
const frame = computed(() => frames.value[step.value])
const previous = computed(() => frames.value[Math.max(0, step.value - 1)].values)
const terms = computed(() => model.value.transitions[selected.value]?.[action.value] ?? [])
const cells = computed(() => {
  const result = []
  for (let y = 2; y >= 0; y--) {
    for (let x = 0; x < 4; x++) result.push({ id: x + ',' + y, wall: x === 1 && y === 1 })
  }
  return result
})
const format = value => Number(value).toFixed(4)
function arrow(id) {
  const best = greedyAction(model.value, id, frame.value.values, gamma.value)
  return best === 'exit' ? 'Thoát' : directions.find(item => item.id === best)?.label ?? 'Kết thúc'
}
watch(key, () => { step.value = 0 })
</script>

<template>
  <section class="math-lab mdp-grid" aria-label="Lặp giá trị MDP trên lưới">
    <div class="mdp-settings">
      <label>Nhiễu
        <select v-model.number="noise"><option :value="0">0</option><option :value="0.2">0,2</option><option :value="0.5">0,5</option></select>
      </label>
      <label>Chiết khấu
        <select v-model.number="gamma"><option :value="0.5">0,5</option><option :value="0.9">0,9</option><option :value="0.99">0,99</option></select>
      </label>
      <label>Thưởng mỗi bước
        <select v-model.number="living"><option :value="0">0</option><option :value="-0.03">−0,03</option><option :value="-0.4">−0,4</option><option :value="-2">−2</option></select>
      </label>
      <label>Nhận thưởng ±1
        <select v-model="convention"><option value="exit">Khi thoát từ ô đặc biệt</option><option value="entry">Ngay khi vào ô đặc biệt</option></select>
      </label>
    </div>
    <SimulationControls v-model="step" :max="100" :reset-key="key" label="Vòng lặp" />
    <div class="mdp-cells" role="group" aria-label="Giá trị và hành động tham lam theo bảng hiện tại">
      <template v-for="cell in cells" :key="cell.id">
        <div v-if="cell.wall" class="mdp-wall" aria-label="Tường">Tường</div>
        <button v-else type="button" :aria-pressed="selected === cell.id" :disabled="!model.actions[cell.id].length" @click="selected = cell.id; action = model.actions[cell.id][0]">
          <small>({{ cell.id }})</small>
          <strong>{{ format(frame.values[cell.id]) }}</strong>
          <span>{{ arrow(cell.id) }}</span>
        </button>
      </template>
    </div>
    <p aria-live="polite">Vòng {{ step }}. Chênh lệch với vòng trước {{ format(frame.delta) }}.</p>
    <label>Hành động tại ({{ selected }})
      <select v-model="action"><option v-for="id in model.actions[selected]" :key="id" :value="id">{{ directions.find(item => item.id === id)?.label ?? 'Thoát' }}</option></select>
    </label>
    <p>Phép cập nhật dùng bảng của vòng {{ Math.max(0, step - 1) }}. Các mũi tên trong lưới được trích từ bảng vòng {{ step }}.</p>
    <ol class="mdp-terms">
      <li v-for="term in terms" :key="term.next">
        Đến {{ term.next }} với xác suất {{ format(term.probability) }}.
        <code>{{ format(term.probability) }} × ({{ term.reward }} + {{ gamma }} × {{ format(previous[term.next]) }}) = {{ format(term.probability * (term.reward + gamma * previous[term.next])) }}</code>
      </li>
    </ol>
    <p v-if="terms.length">Tổng cho hành động này {{ format(actionValue(model, selected, action, previous, gamma)) }}.</p>
    <p>Vòng 0 là bảng khởi tạo. Khi nhận thưởng lúc vào ô, giá trị ô kết thúc bằng 0 vì thưởng đã được tính trên cạnh đi vào.</p>
  </section>
</template>

<style scoped>
.mdp-settings { display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.75rem; }
label { display:grid;gap:.3rem; }
.mdp-cells { display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:5px;margin-block:1rem; }
.mdp-cells button,.mdp-wall { min-width:0;min-height:92px;border:1px solid var(--vp-c-divider);border-radius:6px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:5px; }
.mdp-cells button { background:var(--vp-c-bg-soft);color:var(--vp-c-text-1);cursor:pointer; }
.mdp-cells button[aria-pressed="true"] { outline:2px solid var(--vp-c-brand-1); }
.mdp-cells strong { font-size:clamp(12px,3vw,16px);font-variant-numeric:tabular-nums; }
.mdp-wall { background:var(--vp-c-divider); }
.mdp-terms code { display:block;white-space:normal;overflow-wrap:anywhere; }
</style>
