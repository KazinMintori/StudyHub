<script setup>
import { computed } from 'vue'
import { dataDiagrams } from './data-diagrams.mjs'

const props = defineProps({ name: { type: String, required: true } })
const diagram = computed(() => dataDiagrams[props.name])
</script>

<template>
  <figure v-if="diagram" class="data-diagram" :class="[`data-diagram--${diagram.layout || 'flow'}`, `data-diagram--${name}`]">
    <figcaption class="data-diagram__heading">{{ diagram.title }}</figcaption>
    <code v-if="diagram.code" class="data-diagram__code data-diagram__shared-code">{{ diagram.code }}</code>

    <template v-if="diagram.layout === 'effort'">
      <div class="data-diagram__ratio" role="img" aria-label="Minh họa tỷ lệ thời gian: Xử lý dữ liệu khoảng 80%, mô hình khoảng 20%.">
        <span>≈ 80%</span><span>≈ 20%</span>
      </div>
      <div class="data-diagram__effort">
        <div class="data-diagram__preparation">
          <strong>Xử lý dữ liệu</strong>
          <div class="data-diagram__chips">
            <span v-for="(step, i) in diagram.steps" :key="step" class="data-diagram__chip" :class="`data-diagram__tone-${i % 4}`">{{ step }}</span>
          </div>
        </div>
        <div class="data-diagram__model"><strong>Mô hình</strong><span>≈ 20% thời gian</span></div>
      </div>
    </template>

    <div v-if="diagram.intro" class="data-diagram__intro">{{ diagram.intro }}</div>
    <div v-if="diagram.groups" class="data-diagram__chips data-diagram__groups">
      <span v-for="(group, i) in diagram.groups" :key="group" class="data-diagram__chip" :class="`data-diagram__tone-${i % 4}`">{{ group }}</span>
    </div>

    <div v-if="diagram.items" class="data-diagram__items">
      <section v-for="(item, i) in diagram.items" :key="item.title" class="data-diagram__card" :class="`data-diagram__tone-${item.tone ?? i % 4}`">
        <div class="data-diagram__card-heading">
          <span class="data-diagram__number">{{ item.label || String(i + 1).padStart(2, '0') }}</span>
          <strong>{{ item.title }}</strong>
        </div>
        <code v-if="item.code" class="data-diagram__code">{{ item.code }}</code>
        <p v-if="item.text" class="data-diagram__text">{{ item.text }}</p>
        <dl v-if="item.fields" class="data-diagram__fields">
          <div v-for="field in item.fields" :key="field.label">
            <dt>{{ field.label }}</dt>
            <dd><code v-if="field.code" class="data-diagram__code">{{ field.code }}</code><span v-if="field.text">{{ field.text }}</span></dd>
          </div>
        </dl>
        <ul v-if="item.lines" class="data-diagram__lines">
          <li v-for="line in item.lines" :key="line">{{ line }}</li>
        </ul>
        <div v-if="item.channel" class="data-diagram__channel">{{ item.channel }}</div>
        <table v-if="item.rows" class="data-diagram__table">
          <thead><tr><th v-for="column in item.columns" :key="column" scope="col">{{ column }}</th></tr></thead>
          <tbody><tr v-for="(row, r) in item.rows" :key="r"><td v-for="(value, c) in row" :key="c" :data-label="item.columns[c]">{{ value }}</td></tr></tbody>
        </table>
        <div v-if="item.bars" class="data-diagram__chart" role="img" :aria-label="item.chartLabel">
          <div class="data-diagram__chart-top">Thang đo: {{ item.min }}–{{ item.max }}%</div>
          <div class="data-diagram__bars">
            <div v-for="(value, b) in item.bars" :key="b" class="data-diagram__bar-column">
              <span>{{ value }}%</span>
              <div class="data-diagram__bar-track"><div class="data-diagram__bar" :style="{ height: `${(value - item.min) / (item.max - item.min) * 100}%` }"></div></div>
              <span>{{ ['A', 'B', 'C'][b] }}</span>
            </div>
          </div>
          <div class="data-diagram__chart-bottom">Gốc trục: {{ item.min }}%</div>
        </div>
      </section>
    </div>

    <div v-if="diagram.memory" class="data-diagram__memory">
      <div class="data-diagram__connector" aria-hidden="true">↓</div>
      <strong>Data buffer · Vùng nhớ C liên tục</strong>
      <div class="data-diagram__memory-rows">
        <div v-for="(row, i) in diagram.memory" :key="i" class="data-diagram__memory-row" :class="`data-diagram__tone-${i}`">
          <div><span v-for="(value, c) in row" :key="c">{{ value }}</span></div>
          <span>Hàng {{ i }}</span>
        </div>
      </div>
    </div>
    <div v-if="diagram.result" class="data-diagram__result"><strong>{{ diagram.result.title }}</strong><span>{{ diagram.result.text }}</span></div>
    <p v-if="diagram.caption" class="data-diagram__caption">{{ diagram.caption }}</p>
  </figure>
</template>

<style scoped>
.data-diagram {
  margin: var(--space-6) 0;
  padding: var(--space-5);
  border: 1px solid var(--rule);
  border-radius: var(--radius-lg);
  background: var(--paper);
  color: var(--ink);
  font: var(--fs-ui)/1.65 var(--font-ui);
  min-width: 0;
}
.data-diagram .data-diagram__heading { margin: 0 0 var(--space-4); color: var(--ink); font: 600 var(--fs-lead)/1.5 var(--font-ui); text-align: left; }
.data-diagram__tone-0 { --diagram-accent: var(--tim); --diagram-soft: var(--tim-soft); }
.data-diagram__tone-1 { --diagram-accent: var(--xanh); --diagram-soft: var(--xanh-soft); }
.data-diagram__tone-2 { --diagram-accent: var(--vang); --diagram-soft: var(--vang-soft); }
.data-diagram__tone-3 { --diagram-accent: var(--do); --diagram-soft: var(--do-soft); }
.data-diagram__items { display: grid; gap: var(--space-5); }
.data-diagram--compare .data-diagram__items { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-4); }
.data-diagram__card { position: relative; min-width: 0; padding: var(--space-4); border: 1px solid var(--rule); border-left: 3px solid var(--diagram-accent); border-radius: var(--radius); background: var(--diagram-soft); }
.data-diagram--flow .data-diagram__card + .data-diagram__card::before { content: '↓'; position: absolute; top: -27px; left: 24px; color: var(--ink-3); line-height: 24px; }
.data-diagram--exchange .data-diagram__card + .data-diagram__card::before { content: '↕'; position: absolute; top: -27px; left: 24px; color: var(--ink-3); line-height: 24px; }
.data-diagram__channel { margin-top: var(--space-3); padding-top: var(--space-2); border-top: 1px solid var(--rule); color: var(--diagram-accent); font-weight: 600; }
.data-diagram .data-diagram__fields { margin: var(--space-3) 0 0; }
.data-diagram__fields > div + div { margin-top: var(--space-3); }
.data-diagram__fields dt { color: var(--diagram-accent); font-weight: 600; }
.data-diagram__fields dd { margin: var(--space-1) 0 0; }
.data-diagram--jupyter, .data-diagram--notebook-file-formats { padding: var(--space-4) 0; border: 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); border-radius: 0; }
.data-diagram--jupyter .data-diagram__number { display: none; }
.data-diagram--notebook-file-formats .data-diagram__items { align-items: start; }
.data-diagram__card-heading { display: flex; align-items: baseline; gap: var(--space-3); color: var(--diagram-accent); }
.data-diagram__number { flex-shrink: 0; font: 600 var(--fs-meta)/1.5 var(--font-ui); }
.data-diagram__card-heading strong { font-weight: 600; overflow-wrap: anywhere; }
.data-diagram .data-diagram__code { display: block; margin-top: var(--space-2); padding: var(--space-2) var(--space-3); border-radius: var(--radius-sm); background: var(--paper); color: var(--ink); font: var(--fs-small)/1.7 var(--font-code); white-space: pre-wrap; overflow-wrap: anywhere; }
.data-diagram .data-diagram__shared-code { margin: 0 0 var(--space-4); padding: var(--space-4); border: 1px solid var(--rule); background: var(--canvas); }
.data-diagram .data-diagram__text { margin: var(--space-2) 0 0; font: inherit; }
.data-diagram .data-diagram__lines { margin: var(--space-2) 0 0; padding-left: var(--space-4); font: inherit; }
.data-diagram .data-diagram__lines li { margin: var(--space-1) 0; }
.data-diagram__intro, .data-diagram__result { padding: var(--space-3) var(--space-4); border-radius: var(--radius); background: var(--canvas); border: 1px solid var(--rule); }
.data-diagram__intro { margin-bottom: var(--space-4); font-weight: 600; }
.data-diagram__result { margin-top: var(--space-4); }
.data-diagram__result strong, .data-diagram__result span { display: block; }
.data-diagram .data-diagram__caption { margin: var(--space-4) 0 0; color: var(--ink-2); font: var(--fs-small)/1.7 var(--font-ui); }
.data-diagram__chips { display: flex; flex-wrap: wrap; gap: var(--space-2); margin-top: var(--space-3); }
.data-diagram__groups { margin: 0 0 var(--space-4); }
.data-diagram__chip { padding: var(--space-1) var(--space-3); border: 1px solid var(--diagram-accent); border-radius: var(--radius-sm); color: var(--diagram-accent); background: var(--diagram-soft); font-size: var(--fs-small); }
.data-diagram__ratio { display: grid; grid-template-columns: 4fr 1fr; min-height: 52px; border-radius: var(--radius); overflow: hidden; }
.data-diagram__ratio span { display: flex; align-items: center; justify-content: center; padding: var(--space-2); font-weight: 700; color: var(--paper); background: var(--tim); }
.data-diagram__ratio span + span { color: var(--paper); background: var(--xanh); border-left: 3px solid var(--paper); }
.data-diagram__effort { display: grid; grid-template-columns: minmax(0, 4fr) minmax(0, 1fr); gap: var(--space-4); margin-top: var(--space-4); }
.data-diagram__model { display: flex; flex-direction: column; gap: var(--space-2); color: var(--xanh); }
.data-diagram__model span { font-size: var(--fs-small); }
.data-diagram .data-diagram__table { display: table; width: 100%; margin: var(--space-3) 0 0; border-collapse: collapse; font: var(--fs-small)/1.6 var(--font-ui); }
.data-diagram .data-diagram__table :is(th, td) { padding: var(--space-2); border: 0; border-bottom: 1px solid var(--rule); text-align: left; overflow-wrap: anywhere; }
.data-diagram .data-diagram__table th { color: var(--diagram-accent); font-weight: 600; }
.data-diagram .data-diagram__table tr { background: transparent; border: 0; }
.data-diagram .data-diagram__table tbody tr:last-child td { border-bottom: 0; }
.data-diagram__memory { margin-top: var(--space-3); text-align: center; }
.data-diagram__connector { color: var(--ink-3); margin-bottom: var(--space-2); }
.data-diagram__memory-rows { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: var(--space-2); margin-top: var(--space-3); }
.data-diagram__memory-row > div { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid var(--diagram-accent); border-radius: var(--radius-sm); background: var(--diagram-soft); color: var(--diagram-accent); }
.data-diagram__memory-row > div > span { padding: var(--space-2) 0; font: var(--fs-small)/1.5 var(--font-code); }
.data-diagram__memory-row > div > span + span { border-left: 1px solid var(--diagram-accent); }
.data-diagram__memory-row > span { color: var(--diagram-accent); font-size: var(--fs-small); }
.data-diagram__chart { margin-top: var(--space-3); font-size: var(--fs-small); }
.data-diagram__chart-top, .data-diagram__chart-bottom { color: var(--ink-2); }
.data-diagram__bars { display: flex; gap: var(--space-3); }
.data-diagram__bar-column { display: flex; flex: 1; min-width: 0; flex-direction: column; align-items: center; }
.data-diagram__bar-column > span:first-child { padding: var(--space-2) 0; }
.data-diagram__bar-track { display: flex; align-items: end; height: 140px; width: 70%; }
.data-diagram__bar { width: 100%; background: var(--diagram-accent); border-radius: var(--radius-sm) var(--radius-sm) 0 0; }
.data-diagram__bar-column > span:last-child { width: 100%; border-top: 2px solid var(--ink-2); text-align: center; }
@media (max-width: 600px) {
  .data-diagram { padding: var(--space-4); }
  .data-diagram--compare .data-diagram__items, .data-diagram__effort { grid-template-columns: minmax(0, 1fr); }
  .data-diagram__model { flex-direction: row; flex-wrap: wrap; align-items: baseline; }
  .data-diagram__ratio span { padding-inline: var(--space-1); font-size: var(--fs-small); white-space: nowrap; }
  .data-diagram__memory-rows { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .data-diagram .data-diagram__table thead { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
  .data-diagram .data-diagram__table :is(tbody, tr, td) { display: block; }
  .data-diagram .data-diagram__table tbody tr { padding: var(--space-2) 0; border-bottom: 1px solid var(--rule); }
  .data-diagram .data-diagram__table tbody td { padding: var(--space-1) 0; border: 0; }
  .data-diagram__table td::before { content: attr(data-label) ': '; color: var(--ink-2); font-weight: 600; }
}
@media print { .data-diagram { break-inside: avoid; } }
</style>
