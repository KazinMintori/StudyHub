<script setup>
import { computed, ref, useId, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'
import { decisionCode, decisionPresets, decisionRoutes, traceDecision, codeTokens } from '../services/agent-decision.mjs'

const probability = ref(80), loss = ref(0), step = ref(0), outcome = ref(null), copied = ref(false), resetVersion = ref(0)
const marker = `decision-${useId().replace(/[^a-zA-Z0-9_-]/g, '')}`
const p = computed(() => probability.value / 100)
const routes = computed(() => decisionRoutes(p.value, loss.value))
const frames = computed(() => traceDecision(p.value, loss.value))
const frame = computed(() => frames.value[Math.min(step.value, frames.value.length - 1)])
const complete = computed(() => frame.value.phase === 'done')
const resetKey = computed(() => `${probability.value}:${loss.value}:${resetVersion.value}`)
const lines = decisionCode.map(codeTokens)
const format = value => new Intl.NumberFormat('vi-VN', { maximumFractionDigits: 2 }).format(value)
const message = computed(() => {
  const f = frame.value, route = routes.value[f.routeIndex]
  if (f.phase === 'start') return 'Chưa xét phương án nào. Tác tử chỉ biết mô hình và các xác suất, chưa biết kết quả thực tế.'
  if (f.phase === 'route') return `Bắt đầu xét ${route.name.toLocaleLowerCase('vi')}. Các phương án được duyệt theo thứ tự cố định.`
  if (f.phase === 'zero') return 'Đặt tổng lợi ích kỳ vọng của phương án đang xét bằng 0 trước khi cộng các kết quả.'
  if (f.phase === 'add') {
    const [chance, utility] = route.outcomes[f.outcomeIndex]
    return `Cộng ${format(chance)} × ${format(utility)} = ${format(f.term)} điểm. Tổng tạm thời là ${format(f.score)} điểm. Đây là đóng góp có trọng số, không phải kết quả đã xảy ra.`
  }
  if (f.phase === 'compare') return `Đã tính xong ${route.name.toLocaleLowerCase('vi')}: ${format(f.score)} điểm. Tiếp theo so sánh với phương án tốt nhất đang giữ.`
  if (f.phase === 'replace') return `Giữ ${f.best.name.toLocaleLowerCase('vi')} làm phương án tốt nhất tạm thời với ${format(f.best.score)} điểm.`
  if (f.phase === 'keep') return Math.abs(f.score - f.best.score) < 1e-9
    ? 'Hai điểm kỳ vọng bằng nhau. Quy tắc phá hòa giữ phương án được xét trước, nên vẫn giữ đường ngắn.'
    : `Phương án vừa xét có điểm thấp hơn. Tiếp tục giữ ${f.best.name.toLocaleLowerCase('vi')}.`
  return `Đã xét hết hai phương án. Chọn ${f.best.name.toLocaleLowerCase('vi')} với lợi ích kỳ vọng ${format(f.best.score)} điểm theo mô hình hiện tại.`
})
const realized = computed(() => {
  if (!complete.value || outcome.value === null) return null
  return frame.value.best.name === 'Đường vòng' ? 6 : outcome.value === 'good' ? 10 : loss.value
})
watch(resetKey, () => { step.value = 0; outcome.value = null })
watch(step, () => { outcome.value = null })
function preset(item) { probability.value = item.p * 100; loss.value = item.loss; resetVersion.value++; step.value = 0; outcome.value = null }
async function copyCode() {
  try { await navigator.clipboard.writeText(decisionCode.join('\n')); copied.value = true }
  catch { copied.value = false }
}
</script>

<template>
  <figure class="study-lab agent-decision" aria-label="Mô phỏng quyết định giao hàng dưới sự không chắc chắn">
    <figcaption class="lab-title">Một quyết định, hai phương án</figcaption>
    <p class="lab-lead">Thay xác suất hoặc hậu quả, rồi theo dõi cách tác tử tính và so sánh lợi ích kỳ vọng. Điểm biểu thị lợi ích trong mô hình, không phải thời gian di chuyển.</p>
    <div class="decision-presets" role="group" aria-label="Các trường hợp mẫu">
      <button v-for="item in decisionPresets" :key="item.title" type="button" @click="preset(item)">{{ item.title }}</button>
    </div>
    <div class="decision-inputs">
      <label>Xác suất thuận lợi của đường ngắn: {{ probability }}%
        <input v-model.number="probability" type="range" min="0" max="100" step="1" aria-label="Xác suất thuận lợi của đường ngắn">
      </label>
      <label>Điểm khi đường ngắn bất lợi: {{ loss }}
        <input v-model.number="loss" type="range" min="-20" max="0" step="1" aria-label="Lợi ích của đường ngắn khi bất lợi">
      </label>
    </div>
    <SimulationControls v-model="step" :max="frames.length - 1" :reset-key="resetKey" />
    <p class="decision-explanation" role="status" aria-live="polite">{{ message }}</p>
    <div class="decision-workbench">
      <div class="decision-model">
        <div v-for="(route, r) in routes" :key="route.name" class="route-model" :class="{ examining: frame.routeIndex === r }">
          <h4>{{ route.name }} <span v-if="frame.routeIndex === r">· Đang xét</span></h4>
          <svg v-if="r === 0" viewBox="0 0 340 145" role="img" aria-label="Đường ngắn có hai kết quả: Thuận lợi được 10 điểm, bất lợi nhận điểm đã chọn">
            <defs><marker :id="marker" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M1 1 9 5 1 9" /></marker></defs>
            <path d="M38 72 C90 72 95 35 146 35 M38 72 C90 72 95 110 146 110" :marker-end="`url(#${marker})`" />
            <circle cx="27" cy="72" r="10" />
            <text x="80" y="26">{{ format(p) }}</text><text x="80" y="134">{{ format(1 - p) }}</text>
            <rect x="150" y="15" width="181" height="40" rx="6" :class="{ 'active-outcome': frame.routeIndex === 0 && frame.outcomeIndex === 0 }" />
            <rect x="150" y="90" width="181" height="40" rx="6" :class="{ 'active-outcome': frame.routeIndex === 0 && frame.outcomeIndex === 1 }" />
            <text x="240" y="41" text-anchor="middle">Thuận lợi: 10 điểm</text>
            <text x="240" y="116" text-anchor="middle">Bất lợi: {{ loss }} điểm</text>
          </svg>
          <p v-else class="detour-model">Một kết quả chắc chắn: 6 điểm.</p>
          <p class="route-score">Kỳ vọng đã tính: <strong>{{ frame.scores[r] === null ? 'Chưa hoàn tất' : `${format(frame.scores[r])} điểm` }}</strong></p>
        </div>
        <dl class="decision-state">
          <div><dt>Tổng đang cộng</dt><dd>{{ frame.score === null ? 'Chưa tính' : `${format(frame.score)} điểm` }}</dd></div>
          <div><dt>{{ complete ? 'Quyết định' : 'Tốt nhất tạm thời' }}</dt><dd>{{ frame.best ? `${frame.best.name} · ${format(frame.best.score)} điểm` : 'Chưa có' }}</dd></div>
        </dl>
      </div>
      <div class="decision-editor">
        <div class="editor-bar"><span>JavaScript · Chọn phương án</span><button type="button" @click="copyCode">{{ copied ? 'Đã chép' : 'Chép mã' }}</button></div>
        <pre aria-label="Mã JavaScript với dòng tương ứng bước đang xét"><code><span v-for="(tokens, i) in lines" :key="i" class="code-row" :class="{ current: frame.line === i + 1 }" :aria-current="frame.line === i + 1 ? 'step' : undefined"><span class="line-number" aria-hidden="true">{{ i + 1 }}</span><span class="line-content"><span v-for="(token, t) in tokens" :key="t" :class="token.kind">{{ token.text }}</span></span></span></code></pre>
        <p class="code-note">Dòng được tô chỉ thao tác tương ứng với bước đang xét. Khi điểm bằng nhau, phép so sánh giữ phương án trước. Ngưỡng nhỏ trong mã tránh sai khác do số thực.</p>
      </div>
    </div>
    <section v-if="complete" class="decision-outcome" aria-label="Phân biệt quyết định và kết quả thực tế">
      <h4>Sau khi đã chọn, kết quả nào xảy ra?</h4>
      <p>Chọn một kết quả để đối chiếu. Thao tác này minh họa các khả năng trong mô hình, không lấy mẫu ngẫu nhiên và không thay đổi quyết định vừa tính.</p>
      <div class="outcome-buttons">
        <template v-if="frame.best.name === 'Đường ngắn'">
          <button type="button" :disabled="p === 0" @click="outcome = 'good'">Kết quả thuận lợi</button>
          <button type="button" :disabled="p === 1" @click="outcome = 'bad'">Kết quả bất lợi</button>
        </template>
        <button v-else type="button" @click="outcome = 'certain'">Xem kết quả đường vòng</button>
      </div>
      <p v-if="realized !== null" role="status">Kết quả lần này: <strong>{{ format(realized) }} điểm</strong>. Tác tử đã chọn bằng thông tin có trước kết quả. Một lần bất lợi chưa đủ bác bỏ tính hợp lý của quyết định theo mô hình đó.</p>
    </section>
    <details class="lab-tasks"><summary>Thử thay đổi và giải thích</summary>
      <ol><li>Giữ điểm bất lợi bằng 0. Tìm xác suất tại đó hai phương án có cùng kỳ vọng.</li><li>Giữ xác suất bằng 80%, đổi điểm bất lợi từ 0 xuống −20. Điều gì khiến quyết định đổi?</li><li>Ở mẫu đường ngắn có lợi, chạy đến cuối rồi chọn kết quả bất lợi. Phân biệt điều tác tử biết khi chọn với điều bạn biết sau đó.</li></ol>
    </details>
  </figure>
</template>

<style scoped>
.agent-decision { min-width: 0; }
.decision-presets, .outcome-buttons { display: flex; flex-wrap: wrap; gap: 8px; }
.agent-decision button { min-height: 44px; padding: 8px 12px; border: 1px solid var(--control); border-radius: var(--radius); background: var(--paper); color: var(--ink); font: inherit; font-size: var(--fs-small); cursor: pointer; }
.agent-decision button:hover:not(:disabled) { border-color: var(--tim); background: var(--tim-soft); }
.agent-decision button:disabled { opacity: .5; cursor: default; }
.agent-decision :is(button, input):focus-visible { outline: 3px solid var(--tim); outline-offset: 3px; }
.decision-inputs { display: grid; gap: 16px; margin-top: 20px; }
.decision-inputs label { display: grid; gap: 6px; font-size: var(--fs-small); line-height: 1.6; }
.decision-inputs input { width: 100%; min-height: 44px; accent-color: var(--tim); }
.decision-explanation { min-height: 5em; padding: 14px; border-left: 3px solid var(--tim); background: var(--tim-soft); font-size: var(--fs-ui); line-height: 1.7; }
.decision-workbench { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr); gap: 16px; align-items: start; }
.decision-model, .decision-editor { min-width: 0; }
.route-model { margin-bottom: 12px; padding: 12px; border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper); }
.route-model.examining { border-color: var(--tim); }
.agent-decision h4 { margin: 0 0 8px; font: 600 var(--fs-ui)/1.5 var(--font-ui); }
.route-model h4 span { color: var(--tim); font-weight: 400; }
.route-model svg { border: 0; margin: 0; max-height: none; border-radius: 0; }
.route-model svg :is(path, circle, rect) { fill: var(--paper); stroke: var(--ink-2); stroke-width: 1.4; }
.route-model svg > path { fill: none; }
.route-model svg marker path { fill: none; stroke: var(--ink-2); stroke-width: 1.4; }
.route-model svg text { fill: var(--ink); font: 16px var(--font-ui); }
.route-model svg .active-outcome { fill: var(--tim-soft); stroke: var(--tim); stroke-width: 2; }
.detour-model, .route-score { font-size: var(--fs-small); line-height: 1.7; margin: 8px 0 0; }
.decision-state { margin: 0; font-size: var(--fs-small); }
.decision-state > div { padding: 10px 0; border-bottom: 1px solid var(--rule); }
.decision-state dt { color: var(--ink-2); }
.decision-state dd { margin: 3px 0 0; font-weight: 600; }
.decision-editor { border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper); overflow: hidden; }
.editor-bar { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 6px; padding: 8px 12px; border-bottom: 1px solid var(--rule); font-size: var(--fs-small); }
.decision-editor pre { margin: 0; padding: 12px 0; background: var(--paper); color: var(--ink); overflow: visible; font: 12px/1.8 var(--font-code); }
.decision-editor code { font: inherit; }
.code-row { display: grid; grid-template-columns: 3ch minmax(0, 1fr); padding: 2px 10px; border-left: 3px solid transparent; }
.code-row.current { border-left-color: var(--tim); background: var(--tim-soft); }
.line-number { user-select: none; color: var(--ink-2); padding-right: 8px; text-align: right; }
.line-content { white-space: pre-wrap; overflow-wrap: anywhere; }
.keyword { color: var(--tim); font-weight: 600; }
.string { color: var(--xanh); }
.number { color: var(--do); }
.code-note { margin: 0; padding: 12px; border-top: 1px solid var(--rule); font-size: var(--fs-small); line-height: 1.6; }
.decision-outcome { margin-top: 20px; padding-top: 16px; border-top: 1px solid var(--rule); font-size: var(--fs-small); line-height: 1.7; }
@media (max-width: 960px) { .decision-workbench { grid-template-columns: minmax(0, 1fr); } .decision-editor pre { font-size: 13px; } }
@media (max-width: 480px) { .agent-decision { margin-inline: 0; padding: 12px; } .decision-presets { display: grid; grid-template-columns: 1fr 1fr; } .decision-presets button { text-align: left; padding: 8px; } .route-model { padding: 8px; } .decision-explanation { min-height: 0; } }
</style>
