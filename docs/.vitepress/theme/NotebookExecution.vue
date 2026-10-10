<script setup>
const cells = [
  { id: 1, count: 1, code: 'x = 10', tone: 'purple' },
  { id: 2, count: 4, code: 'print(x)', output: '20', tone: 'amber' },
  { id: 3, count: 3, code: 'x = x + 5', tone: 'green' }
]
const history = [
  { count: 1, cell: 1, code: 'x = 10', state: 'x = 10', text: 'Gán giá trị ban đầu.', tone: 'purple' },
  { count: 2, cell: 3, code: 'x = x + 5', state: 'x = 15', text: 'Cộng 5 vào giá trị 10.', tone: 'green' },
  { count: 3, cell: 3, code: 'x = x + 5', state: 'x = 20', text: 'Chạy lại ô 3, cộng thêm 5.', tone: 'green' },
  { count: 4, cell: 2, code: 'print(x)', state: 'x = 20', text: 'In ra 20. Giá trị x không đổi.', tone: 'amber' }
]
</script>

<template>
  <figure class="notebook-execution">
    <figcaption>Một notebook, hai thứ tự</figcaption>
    <div class="notebook-execution__panels">
      <section class="notebook-execution__panel">
        <h4>Vị trí trong tài liệu</h4>
        <p class="notebook-execution__intro">Ba ô được hiển thị từ trên xuống dưới. Nhãn ghi lần thực thi gần nhất của mỗi ô.</p>
        <div class="notebook-execution__cells">
          <div v-for="cell in cells" :key="cell.id" class="notebook-execution__card" :class="`notebook-execution__${cell.tone}`">
            <div class="notebook-execution__label"><strong>Ô {{ cell.id }}</strong><code>In [{{ cell.count }}]</code></div>
            <code class="notebook-execution__code">{{ cell.code }}</code>
            <div v-if="cell.output" class="notebook-execution__output"><span>Đầu ra của print</span><code>{{ cell.output }}</code></div>
          </div>
        </div>
      </section>
      <section class="notebook-execution__panel">
        <h4>Thứ tự thực thi</h4>
        <p class="notebook-execution__intro">Kernel đã nhận bốn lần chạy. Ô 3 được chạy hai lần trước khi chạy ô 2.</p>
        <ol class="notebook-execution__history">
          <li v-for="step in history" :key="step.count" class="notebook-execution__card" :class="`notebook-execution__${step.tone}`">
            <div class="notebook-execution__label"><strong>Lần {{ step.count }} · Ô {{ step.cell }}</strong><code>In [{{ step.count }}]</code></div>
            <code class="notebook-execution__code">{{ step.code }}</code>
            <div class="notebook-execution__state"><span>RAM sau lần chạy</span><code>{{ step.state }}</code></div>
            <p>{{ step.text }}</p>
          </li>
        </ol>
      </section>
    </div>
  </figure>
</template>

<style scoped>
.notebook-execution { margin: var(--space-6) 0; padding: var(--space-4) 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); background: var(--paper); color: var(--ink); font: var(--fs-ui)/1.65 var(--font-ui); min-width: 0; }
.notebook-execution > figcaption { margin: 0 0 var(--space-5); font: 600 var(--fs-lead)/1.5 var(--font-ui); }
.notebook-execution__panels { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-5); align-items: start; }
.notebook-execution__panel { min-width: 0; }
.notebook-execution .notebook-execution__panel h4 { margin: 0; font: 600 var(--fs-ui)/1.6 var(--font-ui); }
.notebook-execution .notebook-execution__intro { margin: var(--space-2) 0 var(--space-4); color: var(--ink-2); font: var(--fs-small)/1.7 var(--font-ui); }
.notebook-execution__cells { display: grid; gap: var(--space-4); }
.notebook-execution .notebook-execution__history { display: grid; gap: var(--space-4); list-style: none; margin: 0; padding: 0; }
.notebook-execution__purple { --cell-accent: var(--tim); --cell-bg: var(--tim-soft); }
.notebook-execution__green { --cell-accent: var(--xanh); --cell-bg: var(--xanh-soft); }
.notebook-execution__amber { --cell-accent: var(--vang); --cell-bg: var(--vang-soft); }
.notebook-execution .notebook-execution__card { min-width: 0; margin: 0; padding: var(--space-3); border: 1px solid var(--rule); border-left: 3px solid var(--cell-accent); border-radius: var(--radius); background: var(--cell-bg); }
.notebook-execution .notebook-execution__history .notebook-execution__card { padding-block: var(--space-2); border: 0; border-left: 2px solid var(--cell-accent); border-radius: 0; background: transparent; }
.notebook-execution .notebook-execution__history .notebook-execution__code { padding: 0; background: transparent; }
.notebook-execution__label { display: flex; align-items: baseline; flex-wrap: wrap; justify-content: space-between; gap: var(--space-2); color: var(--cell-accent); }
.notebook-execution__label strong { font-weight: 600; }
.notebook-execution code { font: var(--fs-small)/1.7 var(--font-code); background: transparent; padding: 0; color: inherit; white-space: pre-wrap; overflow-wrap: anywhere; }
.notebook-execution .notebook-execution__code { display: block; margin-top: var(--space-2); padding: var(--space-2); background: var(--paper); color: var(--ink); border-radius: var(--radius-sm); }
.notebook-execution__output, .notebook-execution__state { display: flex; align-items: baseline; flex-wrap: wrap; gap: var(--space-2); margin-top: var(--space-2); font-size: var(--fs-small); }
.notebook-execution__output { padding-top: var(--space-2); border-top: 1px solid var(--rule); }
.notebook-execution__output span, .notebook-execution__state span { color: var(--ink-2); }
.notebook-execution .notebook-execution__card p { margin: var(--space-1) 0 0; font: var(--fs-small)/1.7 var(--font-ui); }
.notebook-execution .notebook-execution__takeaway { margin: var(--space-5) 0 0; padding-top: var(--space-4); border-top: 1px solid var(--rule); color: var(--ink-2); font: var(--fs-small)/1.7 var(--font-ui); }
@media (max-width: 600px) {
  .notebook-execution__panels { grid-template-columns: minmax(0, 1fr); }
}
@media print { .notebook-execution__card { break-inside: avoid; } }
</style>
