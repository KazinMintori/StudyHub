<script setup>
import { computed, nextTick, onMounted, ref, watch } from 'vue'
import { withBase } from 'vitepress'
import ExamPractice from '../../exam/components/ExamPractice.vue'
import { toExamBank } from '../services/exam-bank.mjs'
import { answerPaper, createPaperSession, loadPaperSession, paperResult, savePaperSession } from '../services/paper-session.mjs'
const props = defineProps({ bank: { type: Object, required: true } })
const session = ref(createPaperSession(props.bank)), hydrated = ref(false), listOpen = ref(false), confirming = ref(false), reviewing = ref(false), storageFailed = ref(false), restarting = ref(false)
const heading = ref(null), status = ref(''), submitTrigger = ref(null), cancelSubmit = ref(null), jumpTrigger = ref(null)
const current = computed(() => props.bank.questions[session.value.index])
const result = computed(() => paperResult(props.bank, session.value))
const reviewBank = computed(() => toExamBank(props.bank))
const prefix = computed(() => `paper-${props.bank.id}`)
function restore() {
  session.value = loadPaperSession(props.bank)
  confirming.value = false; listOpen.value = false; reviewing.value = false; storageFailed.value = false
}
onMounted(() => { restore(); hydrated.value = true })
watch(() => props.bank.id, () => { if (hydrated.value) restore() })
watch(session, value => { if (hydrated.value) storageFailed.value = !savePaperSession(props.bank, value) }, { deep: true })
function choose(key) { session.value = answerPaper(props.bank, session.value, current.value.id, key) }
async function navigate(index) {
  if (index < 0 || index >= props.bank.questions.length) return
  session.value = { ...session.value, index }; listOpen.value = false
  await nextTick(); heading.value?.focus({ preventScroll: true }); heading.value?.scrollIntoView({ block: 'start', behavior: 'instant' })
}
async function requestSubmit(event) { submitTrigger.value = event.currentTarget; confirming.value = true; await nextTick(); cancelSubmit.value?.focus() }
async function cancel() { confirming.value = false; await nextTick(); submitTrigger.value?.focus() }
function submit() {
  session.value = { ...session.value, submitted: true }; confirming.value = false
  status.value = `Đã nộp bài. Đúng ${result.value.correct} trên ${result.value.total} câu.`
}
function restart() {
  session.value = createPaperSession(props.bank); restarting.value = false; reviewing.value = false
  try { sessionStorage.removeItem(`studyhub:philosophy:paper-review:${props.bank.id}`) } catch {}
}
async function closeList() { listOpen.value = false; await nextTick(); jumpTrigger.value?.focus() }
function restoreReview() {
  return { currentQuestionId: props.bank.questions[session.value.index]?.id,
    answers: Object.fromEntries(Object.entries(session.value.answers).map(([id, selectedKey]) => [id, { selectedKey }])) }
}
</script>

<template>
  <div v-if="reviewing" class="paper-review">
    <button class="paper-review-back" type="button" @click="reviewing = false">← Kết quả bài làm</button>
    <ExamPractice :key="bank.id" :bank="reviewBank" :reveal-answers="true" course-link="/triet-hoc-mac-lenin/on-thi/de-thi/" back-link-text="← Danh sách đề thi" :session-key="`studyhub:philosophy:paper-review:${bank.id}`" :restore-state="restoreReview" />
  </div>
  <section v-else class="philosophy-paper" :aria-label="bank.title">
    <a class="paper-back" :href="withBase('/triet-hoc-mac-lenin/on-thi/de-thi/')">← Danh sách đề thi</a>
    <header class="paper-header"><div><p class="paper-eyebrow">Đề luyện tổng hợp · Ba chương</p><h1>{{ bank.title }}</h1></div><span>{{ result.total }} câu</span></header>
    <p class="paper-description">Chọn đáp án và nộp bài để xem điểm cùng lời giải. Bạn có thể đổi lựa chọn trước khi nộp. Tiến độ tự lưu trên trình duyệt.</p>
    <p v-if="storageFailed" role="status" class="paper-storage">Trình duyệt chưa lưu được tiến độ. Hãy giữ trang mở cho đến khi hoàn thành.</p>
    <p class="paper-sr" role="status" aria-live="polite">{{ status }}</p>

    <section v-if="session.submitted" class="paper-result" aria-label="Kết quả bài làm">
      <h2>Đã nộp bài</h2><p class="paper-score">{{ result.score }}<span> / 10 điểm</span></p>
      <dl><div><dt>Đúng</dt><dd>{{ result.correct }}</dd></div><div><dt>Sai</dt><dd>{{ result.wrong }}</dd></div><div><dt>Chưa trả lời</dt><dd>{{ result.unanswered }}</dd></div></dl>
      <p>Mỗi câu được tính điểm như nhau. Câu chưa trả lời không có điểm.</p>
      <button class="paper-primary" type="button" @click="reviewing = true">Xem bài làm và lời giải</button>
      <button type="button" @click="restarting = !restarting">Làm lại đề</button>
      <div v-if="restarting" class="paper-confirm"><p>Lượt mới sẽ bắt đầu với các lựa chọn trống và thay thế bài làm hiện tại.</p><button type="button" @click="restarting = false">Giữ kết quả</button><button type="button" @click="restart">Bắt đầu lượt mới</button></div>
    </section>
    <template v-else>
      <div class="paper-progress"><progress :value="result.answered" :max="result.total" :aria-label="`Đã trả lời ${result.answered} trên ${result.total} câu`" /><span>{{ result.answered }}/{{ result.total }} đã trả lời</span></div>
      <div class="paper-tools"><button ref="jumpTrigger" type="button" :aria-expanded="listOpen" :aria-controls="`${prefix}-list`" @click="listOpen = !listOpen">Danh sách câu</button><button type="button" @click="requestSubmit">Nộp bài</button></div>
      <section v-if="listOpen" :id="`${prefix}-list`" class="paper-list" aria-label="Danh sách câu" @keydown.esc.prevent="closeList">
        <div class="paper-list-heading"><h2>Chọn câu hỏi</h2><button type="button" @click="closeList">Đóng</button></div>
        <ol><li v-for="(question, index) in bank.questions" :key="question.id"><button type="button" :class="{ 'is-answered': session.answers[question.id], 'is-current': index === session.index }" :aria-current="index === session.index ? 'step' : undefined" :aria-label="`Câu ${index + 1}, ${session.answers[question.id] ? 'đã trả lời' : 'chưa trả lời'}`" @click="navigate(index)">{{ index + 1 }}<span v-if="session.answers[question.id]" aria-hidden="true"> ✓</span></button></li></ol>
      </section>
      <section v-if="confirming" class="paper-confirm" aria-label="Xác nhận nộp bài" @keydown.esc.prevent="cancel">
        <h2>Nộp bài này?</h2><p v-if="result.unanswered">Còn {{ result.unanswered }} câu chưa trả lời. Những câu này sẽ không có điểm.</p><p v-else>Bạn đã trả lời đủ {{ result.total }} câu.</p>
        <div><button ref="cancelSubmit" type="button" @click="cancel">Tiếp tục làm</button><button class="paper-primary" type="button" @click="submit">Xác nhận nộp bài</button></div>
      </section>
      <article v-if="current" :key="current.id" class="paper-question">
        <h2 ref="heading" tabindex="-1">Câu {{ session.index + 1 }} / {{ result.total }}</h2>
        <fieldset><legend>{{ current.prompt }}</legend><label v-for="option in current.options" :key="option.key" class="paper-option" :class="{ 'is-selected': session.answers[current.id] === option.key }"><input type="radio" :name="`${prefix}-${current.id}`" :value="option.key" :checked="session.answers[current.id] === option.key" @change="choose(option.key)" /><span>{{ option.key }}.</span><span>{{ option.text }}</span></label></fieldset>
        <nav class="paper-adjacent" aria-label="Chuyển câu"><button type="button" :disabled="session.index === 0" @click="navigate(session.index - 1)">← Quay lại</button><button type="button" :disabled="session.index + 1 === result.total" @click="navigate(session.index + 1)">Tiếp theo →</button></nav>
      </article>
    </template>
  </section>
</template>

<style scoped>
.philosophy-paper,.paper-review{width:100%;max-width:860px;margin:0 auto;padding:var(--space-4) var(--space-5) var(--space-7);box-sizing:border-box;font:var(--fs-ui)/1.8 var(--font-ui);color:var(--ink)}
.philosophy-paper *{box-sizing:border-box}.paper-back{display:inline-flex;min-height:44px;align-items:center;color:var(--tim)}
.paper-header{display:flex;gap:var(--space-4);justify-content:space-between;align-items:center;padding-block:var(--space-4);border-bottom:1px solid var(--rule)}
.paper-header h1{margin:0;font:700 var(--fs-h3)/1.5 var(--font-ui)}.paper-header>span{white-space:nowrap;color:var(--ink-2)}.paper-eyebrow{margin:0;color:var(--ink-3);font-size:var(--fs-small)}.paper-description{color:var(--ink-2)}
.philosophy-paper button,.paper-review-back{min-height:44px;padding:var(--space-2) var(--space-4);border:1px solid var(--control);border-radius:var(--radius-lg);background:var(--paper);color:var(--ink);font:inherit;cursor:pointer}.philosophy-paper button:hover:not(:disabled){border-color:var(--tim);background:var(--tim-soft)}.philosophy-paper button:disabled{opacity:.5;cursor:default}
.philosophy-paper button:focus-visible,.philosophy-paper input:focus-visible,.paper-review-back:focus-visible{outline:2px solid var(--tim);outline-offset:3px}.philosophy-paper .paper-primary{background:var(--tim);color:var(--paper);border-color:var(--tim)}
.paper-progress{display:flex;gap:var(--space-4);align-items:center;margin-top:var(--space-5)}.paper-progress progress{flex:1;min-width:0;height:6px;accent-color:var(--tim)}.paper-progress span{font-size:var(--fs-small);white-space:nowrap}.paper-tools{display:flex;justify-content:space-between;margin-block:var(--space-5)}
.paper-question h2{font-size:var(--fs-lead);scroll-margin-top:100px}.paper-question fieldset{margin:0;padding:0;border:0;min-width:0}.paper-question legend{margin-bottom:var(--space-5);padding:0;font-weight:600;overflow-wrap:anywhere}
.paper-option{display:grid;grid-template-columns:20px 24px minmax(0,1fr);gap:var(--space-3);padding:var(--space-5);margin-block:var(--space-3);border:1px solid var(--rule);border-radius:var(--radius-lg);background:var(--canvas);cursor:pointer;overflow-wrap:anywhere}.paper-option input{width:18px;height:18px;margin:5px 0 0;accent-color:var(--tim)}.paper-option.is-selected{background:var(--tim-soft);border-color:var(--tim)}.paper-option:has(input:focus-visible){outline:2px solid var(--tim);outline-offset:3px}.paper-adjacent{display:flex;justify-content:space-between;gap:var(--space-3);margin-top:var(--space-6);border-top:1px solid var(--rule);padding-top:var(--space-5)}
.paper-list,.paper-confirm,.paper-result{padding:var(--space-5);border:1px solid var(--rule);border-radius:var(--radius-lg);margin-block:var(--space-5);background:var(--canvas)}.paper-list-heading{display:flex;justify-content:space-between;align-items:center;gap:var(--space-3)}.paper-list h2,.paper-confirm h2,.paper-result h2{font-size:var(--fs-lead);margin:0}.paper-list ol{display:grid;grid-template-columns:repeat(auto-fill,minmax(48px,1fr));gap:var(--space-2);padding:0;list-style:none}.paper-list li{margin:0}.paper-list button{width:100%;padding:var(--space-2)}.paper-list button.is-answered{background:var(--tim-soft)}.paper-list button.is-current{outline:2px solid var(--tim)}.paper-confirm>div{display:flex;gap:var(--space-3);justify-content:flex-end;flex-wrap:wrap}
.paper-result dl{display:flex;gap:var(--space-6);flex-wrap:wrap}.paper-result dt{font-size:var(--fs-small);color:var(--ink-2)}.paper-result dd{margin:0;font-size:var(--fs-h3);font-weight:600}.paper-score{font-size:var(--fs-h1);color:var(--tim);margin-block:var(--space-3)}.paper-score span{font-size:var(--fs-ui);color:var(--ink-2)}.paper-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}.paper-storage{border-left:3px solid var(--vang);padding-left:var(--space-3)}
@media(max-width:480px){.philosophy-paper,.paper-review{padding-inline:var(--space-3)}.paper-header{align-items:flex-start}.paper-option{padding:var(--space-4);gap:var(--space-2)}.paper-progress{flex-wrap:wrap}.paper-progress progress{min-width:50%}}
</style>
