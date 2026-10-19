<script setup>
import { computed, nextTick, onMounted, ref, watch } from 'vue'
import MathText from '../../../core/math/components/MathText.vue'
import {
  answerQuizQuestion, attemptQuestions, createQuizSession, filterQuizQuestions, historyStats,
  loadQuizSession, nextUnansweredId, questionStatus, quizQuestions, quizResponse, quizStats,
  restartQuizSession, saveQuizSession, setQuizQuestion,
} from '../services/quiz-session.mjs'

const props = defineProps({ bank: { type: Object, required: true } })
const session = ref(createQuizSession(props.bank))
const hydrated = ref(false)
const storageFailed = ref(false)
const announcement = ref('')
const listOpen = ref(false)
const historyOpen = ref(false)
const filter = ref('all')
const search = ref('')
const group = ref('')
const listPage = ref(0)
const pendingRestart = ref(null)
const questionHeading = ref(null)
const resultHeading = ref(null)
const cancelRestart = ref(null)
const restartTrigger = ref(null)
const listTrigger = ref(null)
const pageSize = 40
const filters = [{ key: 'all', label: 'Tất cả' }, { key: 'unanswered', label: 'Chưa làm' }, { key: 'wrong', label: 'Câu sai' }]
const questions = computed(() => attemptQuestions(props.bank, session.value))
const stats = computed(() => quizStats(props.bank, session.value))
const currentIndex = computed(() => questions.value.findIndex(question => question.id === session.value.attempt.currentId))
const current = computed(() => questions.value[currentIndex.value] || null)
const response = computed(() => quizResponse(session.value, current.value?.id))
const checked = computed(() => response.value?.checked === true)
const correct = computed(() => checked.value && response.value.selectedKey === current.value?.correctKey)
const correctOption = computed(() => current.value?.options.find(option => option.key === current.value.correctKey))
const options = computed(() => [...(current.value?.options || [])].sort((a, b) => a.key.localeCompare(b.key)))
const wrongExplanations = computed(() => (current.value?.distractors || []).filter(item => item.key !== current.value.correctKey).sort((a, b) => a.key.localeCompare(b.key)))
const nextUnanswered = computed(() => nextUnansweredId(props.bank, session.value))
const groups = computed(() => [...new Map(questions.value.filter(question => question.group).map(question => [question.group, question.groupTitle || question.group])).entries()].map(([id, title]) => ({ id, title })))
const filtered = computed(() => filterQuizQuestions(props.bank, session.value, filter.value, search.value, group.value))
const pageCount = computed(() => Math.max(1, Math.ceil(filtered.value.length / pageSize)))
const visibleList = computed(() => filtered.value.slice(listPage.value * pageSize, (listPage.value + 1) * pageSize))
const listRange = computed(() => filtered.value.length ? `${listPage.value * pageSize + 1}–${Math.min((listPage.value + 1) * pageSize, filtered.value.length)}` : '0')
const history = computed(() => historyStats(props.bank, session.value))
const hasSelections = computed(() => Object.keys(session.value.attempt.responses).length > 0)
const scopeSize = computed(() => pendingRestart.value === 'wrong' ? stats.value.wrong : quizQuestions(props.bank).length)
const prefix = computed(() => `philosophy-quiz-${props.bank.id}`)
function restore() {
  session.value = loadQuizSession(props.bank)
  storageFailed.value = false
  listOpen.value = false
  historyOpen.value = false
  pendingRestart.value = null
  filter.value = 'all'
  search.value = ''
  group.value = ''
  announcement.value = ''
}

onMounted(() => { restore(); hydrated.value = true })
watch(() => [props.bank.id, props.bank.schemaVersion], () => { if (hydrated.value) restore() })
watch(session, value => {
  if (hydrated.value) storageFailed.value = !saveQuizSession(props.bank, value)
}, { deep: true, flush: 'sync' })
watch([filter, search, group], () => { listPage.value = 0 })
watch(pageCount, count => { listPage.value = Math.min(listPage.value, count - 1) })

async function select(key) {
  if (!current.value || checked.value) return
  const previous = session.value
  session.value = answerQuizQuestion(props.bank, session.value, current.value.id, key)
  if (session.value === previous) return
  announcement.value = `${current.value.id}. ${correct.value ? 'Chính xác.' : 'Chưa chính xác.'} Đáp án đúng: ${current.value.correctKey}. Phần giải thích ở ngay bên dưới.`
  await nextTick()
  resultHeading.value?.focus({ preventScroll: true })
}

async function navigate(id, closeList = false) {
  if (!id) return
  session.value = setQuizQuestion(props.bank, session.value, id)
  announcement.value = ''
  pendingRestart.value = null
  if (closeList) listOpen.value = false
  await nextTick()
  questionHeading.value?.focus({ preventScroll: true })
  questionHeading.value?.scrollIntoView({ block: 'start', behavior: 'instant' })
}

async function requestRestart(mode, trigger) {
  restartTrigger.value = trigger
  pendingRestart.value = mode
  await nextTick()
  cancelRestart.value?.focus()
}

async function dismissRestart() {
  pendingRestart.value = null
  await nextTick()
  restartTrigger.value?.focus()
}

async function restart() {
  session.value = restartQuizSession(props.bank, session.value, pendingRestart.value)
  pendingRestart.value = null
  listOpen.value = false
  filter.value = 'all'
  search.value = ''
  group.value = ''
  announcement.value = `Đã bắt đầu lượt ${session.value.attempt.number} với ${stats.value.total} câu.`
  await nextTick()
  questionHeading.value?.focus({ preventScroll: true })
  questionHeading.value?.scrollIntoView({ block: 'start', behavior: 'instant' })
}

function statusLabel(question) {
  return { correct: 'Đúng', wrong: 'Sai', unanswered: 'Chưa làm' }[questionStatus(question, session.value)]
}

async function closeList() {
  listOpen.value = false
  await nextTick()
  listTrigger.value?.focus()
}
</script>

<template>
  <section class="philosophy-quiz" :aria-label="bank.title || 'Luyện trắc nghiệm'">
    <p class="quiz-instruction">Chọn một phương án để xem đáp án và lời giải.</p>
    <p v-if="session.attempt.mode === 'wrong'" class="quiz-round">Lượt {{ session.attempt.number }} · Luyện lại {{ stats.total }} câu sai</p>

    <dl class="quiz-stats" aria-label="Tiến độ lượt hiện tại">
      <div><dt>Đã trả lời</dt><dd>{{ stats.answered }}<span> / {{ stats.total }}</span></dd></div>
      <div class="quiz-stat-correct"><dt>Đúng</dt><dd>{{ stats.correct }}</dd></div>
      <div class="quiz-stat-wrong"><dt>Sai</dt><dd>{{ stats.wrong }}</dd></div>
      <div><dt>Chưa làm</dt><dd>{{ stats.unanswered }}</dd></div>
    </dl>
    <progress class="quiz-progress" :value="stats.answered" :max="Math.max(stats.total, 1)" :aria-label="`Đã trả lời ${stats.answered} trên ${stats.total} câu`" />

    <div class="quiz-tools">
      <button ref="listTrigger" type="button" :aria-expanded="listOpen" :aria-controls="`${prefix}-list`" @click="listOpen = !listOpen">{{ listOpen ? 'Ẩn danh sách câu' : 'Danh sách câu' }}</button>
      <button type="button" :disabled="!stats.wrong" @click="requestRestart('wrong', $event.currentTarget)">Làm lại câu sai<span v-if="stats.wrong"> ({{ stats.wrong }})</span></button>
      <button type="button" :disabled="!hasSelections" @click="requestRestart('all', $event.currentTarget)">Làm lại</button>
    </div>

    <section v-if="pendingRestart" class="quiz-confirm" :aria-labelledby="`${prefix}-confirm-title`" @keydown.esc.prevent="dismissRestart">
      <h2 :id="`${prefix}-confirm-title`">{{ pendingRestart === 'wrong' ? 'Luyện lại các câu sai?' : 'Bắt đầu lại bài này?' }}</h2>
      <p>Lượt mới gồm {{ scopeSize }} câu và bắt đầu với các lựa chọn trống. Lượt hiện tại được giữ trong lịch sử. Tiến độ bài khác vẫn được giữ.</p>
      <div class="quiz-confirm-actions">
        <button ref="cancelRestart" type="button" @click="dismissRestart">Hủy</button>
        <button class="quiz-primary" type="button" @click="restart">{{ pendingRestart === 'wrong' ? 'Bắt đầu luyện lại' : 'Bắt đầu lại' }}</button>
      </div>
    </section>

    <section v-if="listOpen" :id="`${prefix}-list`" class="quiz-list" :aria-labelledby="`${prefix}-list-title`" @keydown.esc="closeList">
      <div class="quiz-list-heading"><h2 :id="`${prefix}-list-title`">Danh sách câu</h2><button type="button" @click="closeList">Đóng</button></div>
      <div class="quiz-filters" role="group" aria-label="Lọc danh sách câu">
        <button v-for="item in filters" :key="item.key" type="button" :aria-pressed="filter === item.key" @click="filter = item.key">{{ item.label }}</button>
      </div>
      <label v-if="groups.length > 1" class="quiz-search" :for="`${prefix}-group`"><span>Nội dung</span><select :id="`${prefix}-group`" v-model="group"><option value="">Tất cả nội dung</option><option v-for="item in groups" :key="item.id" :value="item.id">{{ item.title }}</option></select></label>
      <label class="quiz-search" :for="`${prefix}-search`"><span>Tìm theo mã câu</span><input :id="`${prefix}-search`" v-model="search" type="search" autocomplete="off" spellcheck="false" placeholder="Nhập mã câu" /></label>
      <p class="quiz-list-count">{{ filtered.length }} câu<span v-if="filtered.length > pageSize"> · Hiển thị {{ listRange }}</span></p>
      <p v-if="!filtered.length" class="quiz-empty">{{ search ? 'Không tìm thấy mã câu phù hợp.' : filter === 'wrong' ? 'Chưa có câu sai trong nội dung đang chọn.' : filter === 'unanswered' ? 'Bạn đã làm hết các câu trong nội dung đang chọn.' : 'Không có câu phù hợp với bộ lọc.' }}</p>
      <ol v-else class="quiz-question-grid">
        <li v-for="question in visibleList" :key="question.id">
          <button type="button" :class="[`is-${questionStatus(question, session)}`, { 'is-current': question.id === current?.id }]" :aria-current="question.id === current?.id ? 'step' : undefined" :aria-label="`${question.id}. ${statusLabel(question)}`" @click="navigate(question.id, true)">
            <span>{{ question.id }}</span><small>{{ statusLabel(question) }}</small>
          </button>
        </li>
      </ol>
      <nav v-if="pageCount > 1" class="quiz-list-pages" aria-label="Trang danh sách câu">
        <button type="button" :disabled="listPage === 0" @click="listPage--">Trang trước</button><span>{{ listPage + 1 }} / {{ pageCount }}</span><button type="button" :disabled="listPage + 1 >= pageCount" @click="listPage++">Trang sau</button>
      </nav>
    </section>

    <p v-if="storageFailed" class="quiz-storage-note" role="status">Trình duyệt chưa lưu được tiến độ. Bạn vẫn có thể làm bài, nhưng lượt này có thể mất khi tải lại trang.</p>
    <p class="quiz-sr-only" role="status" aria-live="polite" aria-atomic="true">{{ announcement }}</p>

    <p v-if="!current" class="quiz-empty">Chưa có câu hỏi để luyện tập trong bài này.</p>
    <article v-else :key="current.id" class="quiz-question" :aria-labelledby="`${prefix}-question`">
      <h2 :id="`${prefix}-question`" ref="questionHeading" class="quiz-question-position" tabindex="-1"><span>Câu {{ currentIndex + 1 }} / {{ questions.length }}</span><span class="quiz-question-id">{{ current.id }}</span></h2>
        <fieldset class="quiz-choices" :disabled="checked">
          <legend><MathText :text="current.prompt" /></legend>
          <label v-for="option in options" :key="option.key" class="quiz-option" :class="{ 'is-selected': response?.selectedKey === option.key, 'is-correct': checked && option.key === current.correctKey, 'is-wrong': checked && response?.selectedKey === option.key && option.key !== current.correctKey, 'is-locked': checked }">
            <input type="radio" :name="`${prefix}-${current.id}`" :value="option.key" :checked="response?.selectedKey === option.key" @change="select(option.key)" />
            <span class="quiz-option-key">{{ option.key }}</span>
            <span class="quiz-option-body"><MathText :text="option.text" /><span v-if="checked && option.key === current.correctKey" class="quiz-option-verdict">{{ response?.selectedKey === option.key ? 'Bạn chọn · Đúng' : 'Đáp án đúng' }}</span><span v-else-if="checked && response?.selectedKey === option.key" class="quiz-option-verdict">Bạn chọn · Sai</span></span>
          </label>
        </fieldset>

      <section v-if="checked" class="quiz-result" :class="correct ? 'is-correct' : 'is-wrong'" :aria-labelledby="`${prefix}-result`">
        <h3 :id="`${prefix}-result`" ref="resultHeading" tabindex="-1">{{ correct ? 'Chính xác' : 'Chưa chính xác' }}</h3>
        <p class="quiz-correct-answer"><strong>Đáp án đúng: {{ current.correctKey }}.</strong> <MathText :text="correctOption?.text || ''" /></p>
        <MathText class="quiz-explanation" :text="current.explanation" as="p" />
        <template v-if="wrongExplanations.length">
          <h4>Vì sao các phương án còn lại chưa đúng</h4>
          <ul class="quiz-distractors"><li v-for="item in wrongExplanations" :key="item.key"><strong>{{ item.key }}.</strong><MathText :text="item.explanation" as="p" /></li></ul>
        </template>
        <MathText v-if="current.takeaway" class="quiz-takeaway" :text="current.takeaway" as="p" />
      </section>

      <div v-if="stats.answered === stats.total && stats.total" class="quiz-complete" role="status"><strong>Đã hoàn thành lượt này.</strong><span>{{ stats.correct }} câu đúng, {{ stats.wrong }} câu sai. {{ stats.wrong ? 'Bạn có thể luyện lại các câu sai ở phía trên.' : 'Bạn đã trả lời đúng toàn bộ các câu trong lượt.' }}</span></div>
      <nav class="quiz-navigation" aria-label="Chuyển câu hỏi">
        <div class="quiz-adjacent"><button type="button" :disabled="currentIndex <= 0" @click="navigate(questions[currentIndex - 1]?.id)"><span aria-hidden="true">← </span>Câu trước</button><button type="button" :disabled="currentIndex + 1 >= questions.length" @click="navigate(questions[currentIndex + 1]?.id)">Câu sau<span aria-hidden="true"> →</span></button></div>
        <button class="quiz-next-unanswered" type="button" :disabled="!nextUnanswered" @click="navigate(nextUnanswered)">Câu chưa làm tiếp theo<span aria-hidden="true"> →</span></button>
      </nav>
    </article>

    <section v-if="history.length" class="quiz-history">
      <button type="button" :aria-expanded="historyOpen" :aria-controls="`${prefix}-history`" @click="historyOpen = !historyOpen">{{ historyOpen ? 'Ẩn lịch sử' : 'Lịch sử luyện tập' }} ({{ history.length }} lượt)</button>
      <ol v-if="historyOpen" :id="`${prefix}-history`"><li v-for="attempt in history" :key="attempt.number"><strong>Lượt {{ attempt.number }}{{ attempt.mode === 'wrong' ? ' · Câu sai' : '' }}</strong><span>{{ attempt.answered }}/{{ attempt.total }} câu đã trả lời · Đúng {{ attempt.correct }} · Sai {{ attempt.wrong }}</span></li></ol>
    </section>
  </section>
</template>

<style scoped>
.philosophy-quiz { width: 100%; max-width: 800px; min-width: 0; margin-inline: auto; color: var(--ink); font-family: var(--font-ui); }
.philosophy-quiz *, .philosophy-quiz *::before, .philosophy-quiz *::after { box-sizing: border-box; }
.philosophy-quiz p { margin: 0; }
.philosophy-quiz button { min-height: 44px; font: inherit; cursor: pointer; }
.philosophy-quiz button { padding: var(--space-2) var(--space-4); border: 1px solid var(--control); border-radius: var(--radius); background: var(--paper); color: var(--ink-2); line-height: 1.5; transition: background var(--motion-fast) var(--ease), border-color var(--motion-fast) var(--ease); }
.philosophy-quiz button:not(:disabled):hover { border-color: var(--tim); color: var(--tim); background: var(--tim-soft); }
.philosophy-quiz button:not(:disabled):active { background: var(--sunken); }
.philosophy-quiz button:disabled { color: var(--ink-3); border-color: var(--rule); background: var(--canvas); cursor: default; }
.philosophy-quiz button:focus-visible, .philosophy-quiz input:focus-visible, .philosophy-quiz select:focus-visible { outline: 2px solid var(--tim); outline-offset: 3px; }
.philosophy-quiz .quiz-primary { background: var(--tim); color: var(--paper); border-color: var(--tim); font-weight: 600; }
.philosophy-quiz .quiz-primary:not(:disabled):hover { background: var(--tim-hover); color: var(--paper); border-color: var(--tim-hover); }
.philosophy-quiz .quiz-primary:disabled { background: var(--sunken); border-color: var(--rule); color: var(--ink-3); }
.quiz-instruction { color: var(--ink-2); font-size: var(--fs-ui); line-height: 1.8; }
.quiz-round { margin-top: var(--space-3) !important; color: var(--tim); font-size: var(--fs-small); }
.quiz-stats { display: grid; grid-template-columns: 1.4fr repeat(3, 1fr); gap: var(--space-2); margin: var(--space-5) 0 var(--space-3); }
.quiz-stats > div { min-width: 0; }
.quiz-stats dt { font-size: var(--fs-small); color: var(--ink-3); line-height: 1.6; }
.quiz-stats dd { margin: var(--space-1) 0 0; font-size: var(--fs-h3); font-weight: 600; line-height: 1.4; font-variant-numeric: tabular-nums; }
.quiz-stats dd span { color: var(--ink-3); font-size: var(--fs-small); font-weight: 400; }
.quiz-stat-correct dd { color: var(--xanh); }
.quiz-stat-wrong dd { color: var(--do); }
.quiz-progress { appearance: none; display: block; width: 100%; height: 5px; overflow: hidden; border: 0; border-radius: var(--radius-sm); background: var(--sunken); accent-color: var(--tim); }
.quiz-progress::-webkit-progress-bar { background: var(--sunken); }
.quiz-progress::-webkit-progress-value { background: var(--tim); }
.quiz-progress::-moz-progress-bar { background: var(--tim); }
.quiz-tools { display: flex; flex-wrap: wrap; gap: var(--space-2); margin: var(--space-5) 0; font-size: var(--fs-small); }
.quiz-confirm, .quiz-list { margin: var(--space-5) 0; padding: var(--space-5); border: 1px solid var(--rule); border-radius: var(--radius-lg); background: var(--canvas); }
.quiz-confirm h2, .quiz-list h2 { margin: 0; padding: 0; border: 0; font-size: var(--fs-lead); line-height: 1.5; font-weight: 600; }
.quiz-confirm > p { margin-top: var(--space-3); color: var(--ink-2); line-height: 1.8; font-size: var(--fs-ui); }
.quiz-confirm-actions { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: var(--space-2); margin-top: var(--space-4); }
.quiz-list-heading { display: flex; justify-content: space-between; align-items: center; gap: var(--space-3); margin-bottom: var(--space-4); }
.quiz-filters { display: flex; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-4); font-size: var(--fs-small); }
.quiz-filters button[aria-pressed="true"] { background: var(--tim-soft); border-color: var(--tim); color: var(--tim); font-weight: 600; }
.quiz-search { display: grid; gap: var(--space-2); margin-top: var(--space-3); color: var(--ink-2); font-size: var(--fs-small); }
.quiz-search input, .quiz-search select { width: 100%; min-width: 0; min-height: 44px; padding: var(--space-3); border: 1px solid var(--control); border-radius: var(--radius); color: var(--ink); background: var(--paper); font: var(--fs-ui)/1.5 var(--font-ui); }
.quiz-search input::placeholder { color: var(--ink-3); }
.quiz-list-count { margin: var(--space-4) 0 var(--space-3) !important; color: var(--ink-3); font-size: var(--fs-small); }
.quiz-question-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(125px, 1fr)); gap: var(--space-2); padding: 0; margin: 0; list-style: none; }
.quiz-question-grid li { margin: 0; min-width: 0; }
.quiz-question-grid button { display: grid; width: 100%; height: 100%; gap: var(--space-1); padding: var(--space-3) var(--space-2); text-align: left; overflow-wrap: anywhere; font-size: var(--fs-small); }
.quiz-question-grid small { font-size: var(--fs-meta); }
.quiz-question-grid .is-correct { border-color: var(--xanh); color: var(--xanh); background: var(--xanh-soft); }
.quiz-question-grid .is-wrong { border-color: var(--do); color: var(--do); background: var(--do-soft); }
.quiz-question-grid .is-current { outline: 2px solid var(--tim); outline-offset: 2px; }
.quiz-list-pages { display: flex; align-items: center; justify-content: space-between; gap: var(--space-2); margin-top: var(--space-4); font-size: var(--fs-small); }
.quiz-list-pages > span { white-space: nowrap; color: var(--ink-3); }
.quiz-storage-note { padding: var(--space-3) var(--space-4); margin-bottom: var(--space-5) !important; border-left: 3px solid var(--vang); background: var(--vang-soft); color: var(--ink-2); font-size: var(--fs-small); line-height: 1.8; }
.quiz-empty { padding: var(--space-5) 0; color: var(--ink-2); line-height: 1.8; }
.quiz-question { min-width: 0; padding-top: var(--space-2); }
.quiz-question-position { display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: var(--space-2); margin: 0 0 var(--space-4); padding: 0; border: 0; color: var(--ink-2); font-size: var(--fs-ui); font-weight: 500; line-height: 1.7; scroll-margin-top: calc(var(--vp-nav-height) + var(--space-5)); }
.quiz-question-position:focus { outline: none; }
.quiz-question-position:focus-visible { outline: 2px solid var(--tim); outline-offset: 4px; border-radius: var(--radius-sm); }
.quiz-question-id { color: var(--ink-3); font-size: var(--fs-meta); overflow-wrap: anywhere; }
.quiz-choices { min-width: 0; margin: 0; padding: 0; border: 0; }
.quiz-choices legend { display: block; max-width: 100%; padding: 0; margin-bottom: var(--space-5); font: 600 var(--fs-h3)/1.7 var(--font-read); overflow-wrap: anywhere; white-space: pre-line; }
.quiz-option { display: grid; grid-template-columns: 20px 22px minmax(0, 1fr); gap: var(--space-3); align-items: start; min-height: 60px; padding: var(--space-4); margin-bottom: var(--space-3); border: 1px solid var(--control); border-radius: var(--radius); background: var(--paper); cursor: pointer; line-height: 1.8; transition: background var(--motion-fast) var(--ease), border-color var(--motion-fast) var(--ease); }
.quiz-option:not(.is-locked):hover { border-color: var(--tim); background: var(--tim-soft); }
.quiz-option:has(input:focus-visible) { outline: 2px solid var(--tim); outline-offset: 3px; }
.quiz-option input { appearance: auto; width: 20px; height: 20px; margin: 4px 0 0; accent-color: var(--tim); flex-shrink: 0; }
.quiz-option-key { color: var(--ink-2); font-weight: 600; }
.quiz-option-body { min-width: 0; font: var(--fs-read)/1.75 var(--font-read); overflow-wrap: anywhere; white-space: pre-line; }
.quiz-option.is-selected { background: var(--tim-soft); border-color: var(--tim); }
.quiz-option.is-correct { background: var(--xanh-soft); border-color: var(--xanh); }
.quiz-option.is-wrong { background: var(--do-soft); border-color: var(--do); }
.quiz-option.is-locked { cursor: default; }
.quiz-option-verdict { display: block; margin-top: var(--space-2); font: 600 var(--fs-small)/1.6 var(--font-ui); color: var(--ink-2); }
.quiz-option.is-correct .quiz-option-verdict { color: var(--xanh); }
.quiz-option.is-wrong .quiz-option-verdict { color: var(--do); }
.quiz-result { min-width: 0; padding: var(--space-5); margin-top: var(--space-5); border: 1px solid var(--rule); border-top: 3px solid var(--xanh); border-radius: var(--radius); background: var(--canvas); font: var(--fs-read)/1.85 var(--font-read); overflow-wrap: anywhere; }
.quiz-result.is-wrong { border-top-color: var(--do); }
.quiz-result h3 { margin: 0 0 var(--space-3); font: 600 var(--fs-lead)/1.5 var(--font-ui); color: var(--xanh); }
.quiz-result h3:focus { outline: none; }
.quiz-result h3:focus-visible { outline: 2px solid var(--tim); outline-offset: 4px; border-radius: var(--radius-sm); }
.quiz-result.is-wrong h3 { color: var(--do); }
.quiz-correct-answer { margin-bottom: var(--space-4) !important; }
.quiz-correct-answer strong { font-weight: 600; }
.quiz-explanation { white-space: pre-line; }
.quiz-result h4 { margin: var(--space-5) 0 var(--space-3); font: 600 var(--fs-ui)/1.7 var(--font-ui); }
.quiz-distractors { display: grid; gap: var(--space-4); padding: 0; margin: 0; list-style: none; }
.quiz-distractors li { display: grid; grid-template-columns: 22px minmax(0, 1fr); gap: var(--space-2); margin: 0; }
.quiz-distractors li > strong { font: 600 var(--fs-ui)/1.85 var(--font-ui); }
.quiz-distractors p { white-space: pre-line; }
.quiz-takeaway { margin-top: var(--space-5) !important; border-top: 1px solid var(--rule); padding-top: var(--space-4); white-space: pre-line; }
.quiz-takeaway strong { font-weight: 600; }
.quiz-complete { display: grid; gap: var(--space-2); padding: var(--space-4); margin-top: var(--space-5); background: var(--tim-soft); border-radius: var(--radius); color: var(--ink-2); font-size: var(--fs-ui); line-height: 1.8; }
.quiz-navigation { display: grid; gap: var(--space-3); margin-top: var(--space-5); padding-top: var(--space-5); border-top: 1px solid var(--rule); font-size: var(--fs-ui); }
.quiz-adjacent { display: flex; justify-content: space-between; gap: var(--space-3); }
.quiz-next-unanswered { justify-self: end; color: var(--tim) !important; }
.quiz-next-unanswered:disabled { color: var(--ink-3) !important; }
.quiz-history { padding-top: var(--space-5); margin-top: var(--space-5); border-top: 1px solid var(--rule); font-size: var(--fs-small); }
.quiz-history ol { display: grid; gap: var(--space-3); list-style: none; margin: var(--space-4) 0 0; padding: 0; }
.quiz-history li { display: flex; flex-wrap: wrap; gap: var(--space-2) var(--space-4); justify-content: space-between; padding: var(--space-3) 0; margin: 0; border-bottom: 1px solid var(--rule); color: var(--ink-2); line-height: 1.8; }
.quiz-history strong { font-weight: 500; }
.quiz-sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; border: 0; }
@media (max-width: 480px) {
  .quiz-stats { grid-template-columns: 1.3fr repeat(3, 1fr); }
  .quiz-stats dd { font-size: var(--fs-lead); }
  .quiz-stats dd span { display: block; margin-top: var(--space-1); }
  .quiz-tools { gap: var(--space-2); }
  .quiz-tools button { padding-inline: var(--space-3); }
  .quiz-confirm, .quiz-list, .quiz-result { padding: var(--space-4); }
  .quiz-option { grid-template-columns: 20px 18px minmax(0, 1fr); gap: var(--space-2); padding: var(--space-3); }
  .quiz-next-unanswered { justify-self: stretch; }
  .quiz-question-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .quiz-list-pages button { padding-inline: var(--space-2); }
}
@media (prefers-reduced-motion: reduce) { .philosophy-quiz button, .quiz-option { transition: none; } }
</style>
