<script setup>
import { computed, nextTick, onMounted, ref, watch } from 'vue'
import { withBase } from 'vitepress'
import {
  createFillSession, fillQuestions, fillResponse, fillQuestionStatus, fillStats, gradeFillQuestion,
  loadFillSession, retryFillQuestion, saveFillSession, setCurrentFillQuestion, setFillAnswer, submitFillQuestion,
} from '../services/fill-session.mjs'

const props = defineProps({ bank: { type: Object, required: true }, courseLink: { type: String, default: '' } })
const session = ref(createFillSession(props.bank))
const hydrated = ref(false), storageFailed = ref(false), submitted = ref(false), listOpen = ref(false)
const announcement = ref(''), heading = ref(null), resultHeading = ref(null), listTrigger = ref(null), root = ref(null)
const questions = computed(()=>fillQuestions(props.bank))
const index = computed(()=>questions.value.findIndex(question=>question.id===session.value.currentId))
const current = computed(()=>questions.value[index.value] || questions.value[0] || null)
const response = computed(()=>fillResponse(session.value,current.value?.id))
const checked = computed(()=>response.value?.checked===true)
const grade = computed(()=>gradeFillQuestion(current.value,response.value?.values))
const stats = computed(()=>fillStats(props.bank,session.value))
const prefix = computed(()=>`fill-${props.bank.id}`)
const backLink = computed(()=>props.courseLink || `/triet-hoc-mac-lenin/on-thi/chuong-${props.bank.chapter}.html`)

function restore() {
  session.value=loadFillSession(props.bank)
  submitted.value=false
  listOpen.value=false
  announcement.value=''
}
onMounted(()=>{restore();hydrated.value=true})
watch(()=>[props.bank.id,props.bank.version],()=>{if(hydrated.value)restore()})
watch(session,value=>{if(hydrated.value)storageFailed.value=!saveFillSession(props.bank,value)},{deep:true,flush:'sync'})

function update(blankIndex,value) {
  session.value=setFillAnswer(props.bank,session.value,current.value.id,blankIndex,value)
}
async function answer() {
  if (!current.value || checked.value) return
  submitted.value=true
  if (!grade.value.complete) {
    const missing=grade.value.results.findIndex(result=>result.empty)
    announcement.value=`Bạn chưa điền ô ${missing+1}.`
    await nextTick()
    root.value?.querySelectorAll('.fill-input')[missing]?.focus()
    return
  }
  session.value=submitFillQuestion(props.bank,session.value,current.value.id)
  announcement.value=grade.value.correct ? 'Chính xác. Các ô đều đúng.' : 'Chưa chính xác. Đáp án cho từng ô ở ngay bên dưới.'
  await nextTick()
  resultHeading.value?.focus({preventScroll:true})
}
async function retry() {
  const firstWrong=grade.value.results.findIndex(result=>!result.correct)
  session.value=retryFillQuestion(props.bank,session.value,current.value.id)
  submitted.value=false
  announcement.value='Đã mở lại câu hỏi. Bạn có thể sửa các ô chưa đúng.'
  await nextTick()
  root.value?.querySelectorAll('.fill-input')[Math.max(0,firstWrong)]?.focus()
}
async function navigate(id) {
  if(!id)return
  session.value=setCurrentFillQuestion(props.bank,session.value,id)
  submitted.value=false
  listOpen.value=false
  announcement.value=''
  await nextTick()
  heading.value?.focus({preventScroll:true})
  heading.value?.scrollIntoView({block:'start',behavior:'instant'})
}
async function closeList() {
  listOpen.value=false
  await nextTick()
  listTrigger.value?.focus()
}
function invalid(blankIndex) {
  return checked.value ? !grade.value.results[blankIndex]?.correct : submitted.value && grade.value.results[blankIndex]?.empty
}
function feedbackId(blankIndex) {
  return `${prefix.value}-${current.value.id}-feedback-${blankIndex}`
}
function keyboard(event) {
  if(event.ctrlKey || event.altKey || event.metaKey || event.target.closest('input,textarea,select') || listOpen.value)return
  if(event.key==='ArrowLeft' && index.value>0){event.preventDefault();navigate(questions.value[index.value-1].id)}
  if(event.key==='ArrowRight' && index.value+1<questions.value.length){event.preventDefault();navigate(questions.value[index.value+1].id)}
}
const statusText = question=>({correct:'Đúng',wrong:'Sai',unanswered:'Chưa làm'}[fillQuestionStatus(question,session.value)])
</script>

<template>
  <section ref="root" class="philosophy-fill vp-doc" @keydown="keyboard">
    <a class="fill-course-link" :href="withBase(backLink)">← Chọn bài ôn thi</a>
    <header class="fill-header">
      <h1>{{ bank.title || 'Điền từ' }}</h1>
      <button ref="listTrigger" class="fill-list-trigger" type="button" :aria-expanded="listOpen" :aria-controls="`${prefix}-list`" @click="listOpen=!listOpen">
        <svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7" /><rect x="14" y="3" width="7" height="7" /><rect x="3" y="14" width="7" height="7" /><rect x="14" y="14" width="7" height="7" /></svg>
        <span>Danh sách câu</span>
      </button>
    </header>
    <div v-if="current" class="fill-progress-row">
      <progress :value="index+1" :max="questions.length" :aria-label="`Câu ${index+1} trên ${questions.length}`" />
      <span class="fill-position">{{ index+1 }}/{{ questions.length }}</span>
      <span class="fill-score is-wrong" :aria-label="`${stats.wrong} câu sai`">✕ {{ stats.wrong }}</span>
      <span class="fill-score is-correct" :aria-label="`${stats.correct} câu đúng`">✓ {{ stats.correct }}</span>
    </div>
    <section v-if="listOpen" :id="`${prefix}-list`" class="fill-list" aria-label="Danh sách câu điền từ" @keydown.esc.prevent="closeList">
      <div class="fill-list-heading"><h2>Danh sách câu</h2><button type="button" @click="closeList">Đóng</button></div>
      <ol>
        <li v-for="(question,position) in questions" :key="question.id">
          <button type="button" :class="[`is-${fillQuestionStatus(question,session)}`,{'is-current':question.id===current?.id}]" :aria-current="question.id===current?.id ? 'step' : undefined" :aria-label="`Câu ${position+1}. ${statusText(question)}`" @click="navigate(question.id)">{{ position+1 }}</button>
        </li>
      </ol>
    </section>
    <p v-if="storageFailed" class="fill-storage" role="status">Trình duyệt chưa lưu được tiến độ. Bạn vẫn có thể làm bài, nhưng lượt này có thể mất khi tải lại trang.</p>
    <p class="fill-sr-only" role="status" aria-live="polite" aria-atomic="true">{{ announcement }}</p>
    <p v-if="!current" class="fill-empty">Chưa có câu điền từ trong bài này.</p>
    <article v-else :key="current.id" class="fill-question">
      <h2 ref="heading" class="fill-question-heading" tabindex="-1">Câu hỏi {{ index+1 }}</h2>
      <p class="fill-instruction">Điền từ hoặc cụm từ thích hợp. Có thể gõ có dấu hoặc không dấu.</p>
      <form :aria-label="`Câu điền từ ${index+1}`" novalidate @submit.prevent="answer">
        <p class="fill-sentence">
          <template v-for="(part,partIndex) in current.parts" :key="partIndex">
            <span>{{ part }}</span><span v-if="partIndex<current.blanks.length" class="fill-inline-field"><input
              :id="`${prefix}-${current.id}-input-${partIndex}`" class="fill-input" type="text" :value="response?.values[partIndex] || ''"
              :aria-label="`Ô ${partIndex+1}. ${current.blanks[partIndex].label || 'Từ hoặc cụm từ cần điền'}`"
              :aria-invalid="invalid(partIndex) ? 'true' : undefined" :aria-describedby="checked || (submitted && grade.results[partIndex]?.empty) ? feedbackId(partIndex) : undefined"
              :class="{'is-correct':checked && grade.results[partIndex]?.correct,'is-wrong':invalid(partIndex)}"
              :readonly="checked" maxlength="160" autocomplete="off" autocapitalize="none" :spellcheck="false" :placeholder="`(${partIndex+1})`"
              @input="update(partIndex,$event.target.value)"
            /></span>
          </template>
        </p>
        <div v-if="submitted && !checked && !grade.complete" class="fill-validation">
          <p v-for="(result,blankIndex) in grade.results" v-show="result.empty" :id="feedbackId(blankIndex)" :key="blankIndex">Bạn chưa điền ô {{ blankIndex+1 }}.</p>
        </div>
        <button v-if="!checked" class="fill-primary" type="submit">Trả lời</button>
      </form>
      <section v-if="checked" class="fill-result" :class="grade.correct ? 'is-correct' : 'is-wrong'" :aria-labelledby="`${prefix}-result-heading`">
        <h3 :id="`${prefix}-result-heading`" ref="resultHeading" tabindex="-1">{{ grade.correct ? 'Chính xác' : 'Chưa chính xác' }}</h3>
        <ul class="fill-answer-list">
          <li v-for="(result,blankIndex) in grade.results" :id="feedbackId(blankIndex)" :key="blankIndex" :class="result.correct ? 'is-correct' : 'is-wrong'">
            <span aria-hidden="true">{{ result.correct ? '✓' : '✕' }}</span><span>Ô {{ blankIndex+1 }}: <strong>{{ result.expected }}</strong><span class="fill-answer-verdict">{{ result.correct ? 'Đúng' : 'Đáp án đúng' }}</span></span>
          </li>
        </ul>
        <p class="fill-explanation">{{ current.explanation }}</p>
        <button v-if="!grade.correct" type="button" @click="retry">Thử lại</button>
      </section>
      <p v-if="stats.total && stats.answered===stats.total" class="fill-complete" role="status">Đã hoàn thành {{ stats.total }} câu: {{ stats.correct }} câu đúng và {{ stats.wrong }} câu cần ôn lại.</p>
      <nav class="fill-navigation" aria-label="Chuyển câu điền từ">
        <span>Đã trả lời {{ stats.answered }}/{{ stats.total }} câu</span>
        <div><button type="button" :disabled="index<=0" @click="navigate(questions[index-1]?.id)">Quay lại</button><button class="fill-primary" type="button" :disabled="index+1>=questions.length" @click="navigate(questions[index+1]?.id)">Tiếp theo</button></div>
      </nav>
    </article>
  </section>
</template>

<style scoped>
.philosophy-fill { width: 100%; max-width: 860px; margin: 0 auto; padding: 16px 20px 48px; box-sizing: border-box; color: var(--ink); font-family: var(--font-ui); }
.philosophy-fill *, .philosophy-fill *::before, .philosophy-fill *::after { box-sizing: border-box; }
.philosophy-fill button { min-height: 44px; padding: 10px 20px; border: 1px solid var(--control); border-radius: 999px; background: var(--sunken); color: var(--ink); font: 600 14px/1.5 var(--font-ui); cursor: pointer; }
.philosophy-fill button:hover:not(:disabled) { border-color: var(--tim); color: var(--tim); background: var(--tim-soft); }
.philosophy-fill button:disabled { opacity: .45; cursor: default; }
.philosophy-fill button:focus-visible, .fill-course-link:focus-visible, .fill-input:focus-visible { outline: 2px solid var(--tim); outline-offset: 3px; }
.philosophy-fill .fill-primary { border-color: var(--tim); background: var(--tim); color: var(--paper); }
.philosophy-fill .fill-primary:hover:not(:disabled) { border-color: var(--tim-hover); background: var(--tim-hover); color: var(--paper); }
.fill-course-link { display: inline-flex; min-height: 44px; align-items: center; color: var(--tim); font-size: 15px; text-decoration: none; }
.fill-header { display: flex; justify-content: space-between; align-items: center; gap: 16px; padding-bottom: 16px; border-bottom: 1px solid var(--rule); }
.fill-header h1 { margin: 0; font: 700 20px/1.3 var(--font-ui); text-wrap: balance; }
.fill-list-trigger { display: inline-flex; align-items: center; gap: 8px; flex-shrink: 0; }
.fill-progress-row { display: flex; gap: 12px; align-items: center; margin: 20px 0 28px; }
.fill-progress-row progress { appearance: none; min-width: 20px; width: 100%; height: 6px; border: 0; border-radius: 999px; overflow: hidden; background: var(--sunken); accent-color: var(--tim); }
.fill-progress-row progress::-webkit-progress-bar { background: var(--sunken); }
.fill-progress-row progress::-webkit-progress-value { background: var(--tim); }
.fill-progress-row progress::-moz-progress-bar { background: var(--tim); }
.fill-position { color: var(--ink-2); font-size: 14px; font-weight: 600; white-space: nowrap; font-variant-numeric: tabular-nums; }
.fill-score { padding: 4px 9px; border-radius: 999px; white-space: nowrap; font-size: 13px; font-weight: 600; }
.fill-score.is-wrong { background: var(--do-soft); color: var(--do); }
.fill-score.is-correct { background: var(--xanh-soft); color: var(--xanh); }
.fill-list { margin-bottom: 24px; padding: 16px; border: 1px solid var(--rule); border-radius: var(--radius-lg); background: var(--canvas); }
.fill-list-heading { display: flex; align-items: center; justify-content: space-between; gap: 12px; }
.fill-list h2 { border: 0; margin: 0; padding: 0; font: 600 16px/1.5 var(--font-ui); }
.fill-list ol { display: grid; grid-template-columns: repeat(auto-fill,minmax(44px,1fr)); gap: 8px; padding: 0 !important; margin: 16px 0 0 !important; list-style: none !important; }
.fill-list li { min-width: 0; margin: 0 !important; list-style: none !important; }
.fill-list li button { width: 100%; padding: 8px; border-radius: var(--radius); }
.fill-list .is-current { outline: 2px solid var(--tim); outline-offset: 2px; }
.fill-list .is-correct { color: var(--xanh); background: var(--xanh-soft); }
.fill-list .is-wrong { color: var(--do); background: var(--do-soft); }
.fill-question-heading { margin: 0 0 12px !important; padding: 0 !important; border: 0 !important; font: 700 18px/1.5 var(--font-ui); scroll-margin-top: calc(var(--vp-nav-height) + 20px); }
.fill-question-heading:focus, .fill-result h3:focus { outline: none; }
.fill-question-heading:focus-visible, .fill-result h3:focus-visible { outline: 2px solid var(--tim); outline-offset: 4px; }
.fill-instruction { margin: 0 0 20px; color: var(--ink-2); font-size: 14px; line-height: 1.7; }
.fill-sentence { margin: 0 0 24px; color: var(--ink); font: 500 17px/2.5 var(--font-ui); overflow-wrap: anywhere; white-space: pre-line; }
.fill-inline-field { display: inline-block; max-width: 100%; margin: 3px 5px; vertical-align: baseline; }
.fill-input { width: 210px; max-width: 100%; min-height: 44px; padding: 8px 12px; border: 1px solid var(--control); border-radius: var(--radius); background: var(--paper); color: var(--ink); font: 500 16px/1.5 var(--font-ui); }
.fill-input::placeholder { color: var(--ink-3); }
.fill-input.is-correct { border-color: var(--xanh); background: var(--xanh-soft); }
.fill-input.is-wrong { border-color: var(--do); background: var(--do-soft); }
.fill-input[readonly] { cursor: default; }
.fill-validation { margin: -8px 0 16px; color: var(--do); font-size: 14px; line-height: 1.7; }
.fill-validation p { margin: 0; }
.fill-result { margin-top: 24px; padding: 20px; border: 1px solid var(--rule); border-radius: var(--radius-lg); background: var(--canvas); }
.fill-result h3 { margin: 0 0 16px; font: 700 17px/1.5 var(--font-ui); color: var(--xanh); }
.fill-result.is-wrong h3 { color: var(--do); }
.fill-answer-list { list-style: none !important; margin: 0 0 16px !important; padding: 0 !important; }
.fill-answer-list li { display: grid; grid-template-columns: 20px minmax(0,1fr); gap: 8px; margin: 0 0 10px !important; overflow-wrap: anywhere; line-height: 1.7; font-size: 15px; }
.fill-answer-list .is-correct > span:first-child { color: var(--xanh); }
.fill-answer-list .is-wrong > span:first-child { color: var(--do); }
.fill-answer-list strong { font-weight: 600; }
.fill-answer-verdict { display: block; color: var(--ink-2); font-size: 13px; }
.fill-explanation { margin: 16px 0; font-size: 15px; line-height: 1.8; overflow-wrap: anywhere; }
.fill-navigation { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-top: 32px; padding-top: 20px; border-top: 1px solid var(--rule); }
.fill-navigation > span { color: var(--ink-3); font-size: 13px; }
.fill-navigation > div { display: flex; gap: 12px; margin-left: auto; }
.fill-navigation button { padding-inline: 24px; }
.fill-storage, .fill-complete { margin: 16px 0; padding: 12px 16px; border-left: 3px solid var(--tim); background: var(--tim-soft); font-size: 14px; line-height: 1.8; }
.fill-empty { margin-top: 24px; color: var(--ink-2); }
.fill-sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; border: 0; }
@media (max-width: 640px) {
  .philosophy-fill { padding: 12px 14px 40px; }
  .fill-header { align-items: flex-start; gap: 12px; }
  .fill-header h1 { font-size: 20px; }
  .fill-list-trigger { padding: 10px !important; }
  .fill-list-trigger > span { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
  .fill-progress-row { gap: 8px; }
  .fill-result { padding: 16px; }
  .fill-sentence { font-size: 16px; }
  .fill-inline-field { max-width: calc(100% - 10px); }
  .fill-input { width: 190px; }
}
</style>
