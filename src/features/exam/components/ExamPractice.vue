<template>
  <div ref="examRootRef" class="exam-practice vp-doc" :class="{ 'is-empty': !currentQuestion }" @click="copyCode">
    <a class="exam-course-link" :href="withBase(courseLink)">← Chọn bài ôn thi</a>
    <!-- Top Header Bar -->
    <header class="exam-header">
      <div class="exam-header__left">
        <h1 class="exam-header__title">{{ bank?.title || 'Ôn tập ngân hàng câu hỏi' }}</h1>
        <div v-if="bank?.lesson" class="exam-header__lesson-tag">
          Bài {{ bank.lesson }}
        </div>
      </div>

      <div class="exam-header__right">
        <!-- Mode Switcher (Quiz vs Essay) -->
        <div class="exam-mode-switch" role="group" aria-label="Chế độ ôn tập">
          <button
            type="button"
            class="exam-mode-switch__btn"
            :class="{ 'is-active': currentMode === 'quiz' }"
            :aria-pressed="currentMode === 'quiz'"
            @click="switchMode('quiz')"
          >
            <span>Trắc nghiệm</span>
            <span class="exam-mode-switch__count">({{ quizQuestions.length }})</span>
          </button>
          <button
            v-if="essayQuestions.length"
            type="button"
            class="exam-mode-switch__btn"
            :class="{ 'is-active': currentMode === 'essay' }"
            :aria-pressed="currentMode === 'essay'"
            @click="switchMode('essay')"
          >
            <span>Tự luận</span>
            <span class="exam-mode-switch__count">({{ essayQuestions.length }})</span>
          </button>
        </div>

        <!-- Question List / Jump Trigger -->
        <button
          ref="jumpTriggerRef"
          type="button"
          class="exam-jump-trigger"
          :aria-expanded="showJumpModal"
          aria-label="Xem danh sách tất cả các câu hỏi"
          @click="toggleJumpModal"
        >
          <svg
            aria-hidden="true"
            width="18"
            height="18"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <rect x="3" y="3" width="7" height="7"></rect>
            <rect x="14" y="3" width="7" height="7"></rect>
            <rect x="14" y="14" width="7" height="7"></rect>
            <rect x="3" y="14" width="7" height="7"></rect>
          </svg>
          <span class="exam-jump-trigger__text">Danh sách câu</span>
        </button>
      </div>
    </header>

    <!-- Progress Row matching screenshot -->
    <div v-if="currentQuestion" class="exam-progress-row">
      <div class="exam-progress-bar-wrap">
        <div
          class="exam-progress-bar"
          role="progressbar"
          :aria-valuenow="activeIndex + 1"
          :aria-valuemin="1"
          :aria-valuemax="questionsForMode.length"
          :aria-valuetext="`Câu hỏi ${activeIndex + 1} trên ${questionsForMode.length}`"
        >
          <div
            class="exam-progress-bar__fill"
            :style="{ width: `${progressPercentage}%` }"
          ></div>
        </div>
      </div>

      <div class="exam-progress-info">
        <span class="exam-progress-counter">
          {{ activeIndex + 1 }}/{{ questionsForMode.length }}
        </span>

        <!-- Badges for Quiz: Wrong & Correct count -->
        <div v-if="currentMode === 'quiz'" class="exam-score-badges">
          <span class="exam-score-badge exam-score-badge--wrong" title="Số câu trả lời sai" :aria-label="`${stats.wrongCount} câu sai`">
            <svg aria-hidden="true" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
            <span class="exam-score-badge__count">{{ stats.wrongCount }}</span>
          </span>

          <span class="exam-score-badge exam-score-badge--correct" title="Số câu trả lời đúng" :aria-label="`${stats.correctCount} câu đúng`">
            <svg aria-hidden="true" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
            <span class="exam-score-badge__count">{{ stats.correctCount }}</span>
          </span>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="!currentQuestion" class="exam-empty">
      <p class="exam-empty__message">Không có câu hỏi nào trong danh mục này.</p>
    </div>

    <!-- Active Question View -->
    <main v-else class="exam-question-card">
      <!-- Question Heading (Receives focus on navigation for screen readers) -->
      <div class="exam-question__header">
        <h2
          :id="headingId"
          ref="questionHeadingRef"
          tabindex="-1"
          class="exam-question__heading"
        >
          Câu hỏi {{ activeIndex + 1 }}
          <span v-if="currentQuestion.id" class="exam-question__id-tag">
            {{ currentQuestion.id }}
          </span>
        </h2>
        <span v-if="currentQuestion.group" class="exam-question__group-tag">
          {{ formatGroup(currentQuestion.group) }}
        </span>
      </div>

      <!-- Question Prompt (Pre-rendered VitePress HTML) -->
      <div class="exam-question__prompt" v-html="currentQuestion.promptHtml"></div>

      <!-- QUIZ MODE: 4 vertical options A–D -->
      <div
        v-if="currentMode === 'quiz'"
        class="exam-choices"
        role="radiogroup"
        :aria-labelledby="headingId"
      >
        <div
          v-for="option in currentOptions"
          :key="option.key"
          class="exam-choice"
          :class="{
            'is-selected': selectedKey === option.key,
            'is-correct': isAnswered && isOptionCorrect(option.key),
            'is-wrong': isAnswered && selectedKey === option.key && !isOptionCorrect(option.key),
            'is-answered': isAnswered,
          }"
          @click="onCardClick($event, option.key)"
        >
          <div class="exam-choice__header">
            <!-- Non-nested radio control for accessibility -->
            <label
              class="exam-choice__control"
              :for="getOptionInputId(option.key)"
            >
              <input
                :id="getOptionInputId(option.key)"
                :aria-labelledby="`${getOptionInputId(option.key)}-key ${getOptionInputId(option.key)}-text`"
                type="radio"
                class="exam-choice__radio"
                :name="'exam-choice-' + currentQuestion.id"
                :value="option.key"
                :checked="selectedKey === option.key"
                :disabled="isAnswered"
                @change="handleSelect(option.key)"
                @keydown="onRadioKeydown($event, option.key)"
              />
              <span :id="`${getOptionInputId(option.key)}-key`" class="exam-choice__key-label">{{ option.key }}.</span>
            </label>

            <!-- Option Text Content Body -->
            <div class="exam-choice__body">
              <div :id="`${getOptionInputId(option.key)}-text`" class="exam-choice__html" v-html="option.html"></div>
              <span
                v-if="isAnswered && selectedKey === option.key"
                class="exam-choice__user-badge"
              >
                (Câu trả lời của bạn)
              </span>
            </div>

            <!-- Status Pill Badges Once Answered -->
            <div v-if="isAnswered" class="exam-choice__status-slot">
              <span
                v-if="isOptionCorrect(option.key)"
                class="exam-badge exam-badge--correct"
              >
                <svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                <span>Câu trả lời chính xác</span>
              </span>
              <span
                v-else-if="selectedKey === option.key"
                class="exam-badge exam-badge--wrong"
              >
                <svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
                <span>Không chính xác</span>
              </span>
            </div>
          </div>

          <!-- Per-option Explanation Body Once Answered -->
          <div
            v-if="isAnswered && option.explanationHtml"
            class="exam-choice__explanation"
            v-html="option.explanationHtml"
          ></div>
        </div>

        <!-- Optional overall answer notes / verification for quiz if present -->
        <details
          :key="`quiz-notes-${currentQuestion.id}`"
          v-if="isAnswered && (currentQuestion.answerHtml || currentQuestion.verificationHtml)"
          class="exam-quiz-notes"
        >
          <summary class="exam-quiz-notes__summary">
            <span>Xem lời giải</span>
          </summary>
          <div class="exam-quiz-notes__content">
            <div v-if="currentQuestion.answerHtml" v-html="currentQuestion.answerHtml"></div>
          </div>
        </details>
      </div>

      <!-- ESSAY MODE: Single prompt + Native details initially closed every new question -->
      <div v-else-if="currentMode === 'essay'" class="exam-essay">
        <details
          :key="'essay-details-' + currentQuestion.id"
          class="exam-essay__details"
        >
          <summary class="exam-essay__summary">
            <span class="exam-essay__summary-title">Xem lời giải</span>
            <span class="exam-essay__summary-action">(Bấm để mở)</span>
          </summary>
          <div class="exam-essay__body">
            <div
              v-if="currentQuestion.answerHtml"
              class="exam-essay__answer"
              v-html="currentQuestion.answerHtml"
            ></div>
          </div>
        </details>
      </div>

      <!-- Bottom Navigation matching screenshot -->
      <footer class="exam-nav-footer">
        <div class="exam-nav-footer__info">
          <span class="exam-nav-footer__hint">Phím tắt: <kbd>←</kbd> Trước, <kbd>→</kbd> Tiếp theo</span>
        </div>

        <div class="exam-nav-footer__actions">
          <button
            type="button"
            class="exam-nav-btn exam-nav-btn--prev"
            :disabled="!nav.hasPrev"
            @click="goToPrev"
          >
            Quay lại
          </button>
          <button
            type="button"
            class="exam-nav-btn exam-nav-btn--next"
            :disabled="!nav.hasNext"
            @click="goToNext"
          >
            Tiếp theo
          </button>
        </div>
      </footer>
    </main>


    <!-- Question Jump Matrix Modal -->
    <div
      v-if="showJumpModal"
      class="exam-modal-backdrop"
      role="dialog"
      aria-modal="true"
      aria-label="Danh sách câu hỏi ôn tập"
      @click.self="toggleJumpModal"
      @keydown.esc.stop.prevent="toggleJumpModal"
      @keydown.tab="trapModalFocus"
    >
      <div ref="modalRef" class="exam-modal">
        <div class="exam-modal__header">
          <h3 class="exam-modal__title">
            Danh sách câu hỏi: {{ currentMode === 'quiz' ? 'Trắc nghiệm' : 'Tự luận' }}
          </h3>
          <button
            type="button"
            class="exam-modal__close-btn"
            aria-label="Đóng bảng chọn câu hỏi"
            @click="toggleJumpModal"
          >
            &times;
          </button>
        </div>

        <div class="exam-modal__grid">
          <button
            v-for="(q, idx) in questionsForMode"
            :key="q.id"
            type="button"
            class="exam-modal__cell"
            :class="{
              'is-current': idx === activeIndex,
              'is-correct': currentMode === 'quiz' && isQuestionCorrect(q.id),
              'is-wrong': currentMode === 'quiz' && isQuestionWrong(q.id),
              'is-answered': isQuestionAnswered(q.id),
            }"
            :aria-current="idx === activeIndex ? 'true' : undefined"
            @click="jumpToQuestion(q.id)"
          >
            <span class="exam-modal__cell-num">{{ idx + 1 }}</span>
            <span class="exam-modal__cell-id">{{ q.id }}</span>
          </button>
        </div>

        <div class="exam-modal__legend">
          <span class="exam-legend-item">
            <span class="exam-legend-dot exam-legend-dot--current"></span> Đang xem
          </span>
          <span v-if="currentMode === 'quiz'" class="exam-legend-item">
            <span class="exam-legend-dot exam-legend-dot--correct"></span> Đúng
          </span>
          <span v-if="currentMode === 'quiz'" class="exam-legend-item">
            <span class="exam-legend-dot exam-legend-dot--wrong"></span> Sai
          </span>
          <span class="exam-legend-item">
            <span class="exam-legend-dot exam-legend-dot--unanswered"></span> Chưa làm
          </span>
        </div>
      </div>
    </div>

    <!-- Screen Reader Live Status Region -->
    <div
      class="sr-only"
      role="status"
      aria-live="polite"
      aria-atomic="true"
    >
      {{ liveStatus }}
    </div>
  </div>
</template>

<script setup>
import { ref, computed, reactive, watch, onMounted, onUnmounted, nextTick } from 'vue';
import { withBase } from 'vitepress';
import {
  normalizeMode,
  filterQuestionsByMode,
  resolveActiveIndex,
  getAdjacentNav,
  parseExamQuery,
  buildExamQueryString,
  createExamSessionState,
  recordQuizAnswer,
  getAnswer,
  calculateSessionStats,
  loadStoredAnswers,
  reconcileStoredAnswers,
  saveStoredAnswers,
} from '../services/exam-session.mjs';

const props = defineProps({
  courseLink: { type: String, default: '/xu-ly-du-lieu/on-thi/' },
  sessionKey: { type: String, default: '' },
  restoreState: { type: Function, default: null },
  bank: {
    type: Object,
    required: true,
    default: () => ({
      lesson: '',
      title: '',
      questions: [],
    }),
  },
});
const emit = defineEmits(['answer', 'navigate']);
let restoredQuestionId = null;

// Reactive state
const currentMode = ref('quiz');
const currentQuestionId = ref(null);
const showJumpModal = ref(false);
const liveStatus = ref('');
const examRootRef = ref(null);
const questionHeadingRef = ref(null);
const jumpTriggerRef = ref(null);
const modalRef = ref(null);
let previousPageOverflow;

function restorePageScroll() {
  if (previousPageOverflow === undefined || typeof document === 'undefined') return;
  document.documentElement.style.overflow = previousPageOverflow;
  previousPageOverflow = undefined;
}

watch(showJumpModal, (open) => {
  if (typeof document === 'undefined') return;
  if (open) {
    previousPageOverflow = document.documentElement.style.overflow;
    document.documentElement.style.overflow = 'hidden';
  } else {
    restorePageScroll();
  }
});

// In-memory session state (preserves answers during current session)
const sessionState = reactive(createExamSessionState());

// Unique storage key per lesson
const storageKey = computed(() => {
  if (props.sessionKey) return props.sessionKey;
  const lesson = props.bank?.lesson || 'default';
  return `studyhub_exam_session_lesson_${lesson}`;
});

// Filtered question lists
const allQuestions = computed(() => (Array.isArray(props.bank?.questions) ? props.bank.questions : []));
const quizQuestions = computed(() => filterQuestionsByMode(allQuestions.value, 'quiz'));
const essayQuestions = computed(() => filterQuestionsByMode(allQuestions.value, 'essay'));

const questionsForMode = computed(() => {
  return currentMode.value === 'essay' ? essayQuestions.value : quizQuestions.value;
});

// Active index and question
const activeIndex = computed(() => {
  return resolveActiveIndex(questionsForMode.value, currentQuestionId.value);
});

const currentQuestion = computed(() => {
  const list = questionsForMode.value;
  const idx = activeIndex.value;
  return idx >= 0 && idx < list.length ? list[idx] : null;
});

// Adjacent navigation
const nav = computed(() => {
  return getAdjacentNav(questionsForMode.value, activeIndex.value);
});

// Overall quiz session statistics
const stats = computed(() => {
  return calculateSessionStats(sessionState, allQuestions.value);
});

// Active question's quiz options
const currentOptions = computed(() => {
  if (currentQuestion.value?.kind === 'quiz' && Array.isArray(currentQuestion.value.options)) {
    return currentQuestion.value.options;
  }
  return [];
});

// Answer state for current question
const currentAnswer = computed(() => {
  if (!currentQuestion.value?.id) return null;
  return getAnswer(sessionState, currentQuestion.value.id);
});

const isAnswered = computed(() => Boolean(currentAnswer.value));
const selectedKey = computed(() => currentAnswer.value?.selectedKey || null);

// Progress percentage
const progressPercentage = computed(() => {
  const total = questionsForMode.value.length;
  if (total === 0) return 0;
  return Math.min(100, Math.round(((activeIndex.value + 1) / total) * 100));
});

const headingId = computed(() => {
  return currentQuestion.value?.id ? `heading-${currentQuestion.value.id}` : 'exam-heading';
});

// Helpers
function formatGroup(group) {
  if (group === 'core') return 'Cốt lõi';
  if (group === 'extension') return 'Mở rộng';
  if (group === 'regex') return 'Regex';
  return group || '';
}

function getOptionInputId(key) {
  const qId = currentQuestion.value?.id || 'q';
  return `exam-opt-${qId}-${key}`;
}

function isOptionCorrect(key) {
  if (!currentQuestion.value?.correctKey) return false;
  return String(key).trim().toUpperCase() === String(currentQuestion.value.correctKey).trim().toUpperCase();
}

function isQuestionCorrect(questionId) {
  const ans = getAnswer(sessionState, questionId);
  return Boolean(ans && ans.isCorrect);
}

function isQuestionWrong(questionId) {
  const ans = getAnswer(sessionState, questionId);
  return Boolean(ans && !ans.isCorrect);
}

function isQuestionAnswered(questionId) {
  return Boolean(getAnswer(sessionState, questionId));
}

// User Actions
function handleSelect(key) {
  if (!currentQuestion.value || isAnswered.value || currentMode.value !== 'quiz') return;
  const recorded = recordQuizAnswer(sessionState, currentQuestion.value, key);
  saveStoredAnswers(storageKey.value, sessionState.answers);

  if (recorded) {
    emit('answer', { questionId: currentQuestion.value.id, selectedKey: recorded.selectedKey });
    const isCorrect = recorded.isCorrect;
    liveStatus.value = `Đã chọn đáp án ${key}. Kết quả: ${
      isCorrect ? 'Chính xác' : 'Không chính xác'
    }. ${!isCorrect && recorded.correctKey ? `Đáp án đúng là ${recorded.correctKey}.` : ''}`;
  }
}

function onCardClick(event, key) {
  if (isAnswered.value) return;
  // If the user clicked directly on interactive content (link, button, code block controls), don't trigger select
  if (event.target.closest('a, button, input, summary, details, pre')) {
    return;
  }
  handleSelect(key);
}

function onRadioKeydown(event, currentKey) {
  const keys = ['A', 'B', 'C', 'D'];
  const currentIndex = keys.indexOf(currentKey);

  if (event.key === 'ArrowDown' || event.key === 'ArrowRight') {
    event.preventDefault();
    const nextKey = keys[(currentIndex + 1) % keys.length];
    const nextInput = document.getElementById(getOptionInputId(nextKey));
    nextInput?.focus();
  } else if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') {
    event.preventDefault();
    const prevKey = keys[(currentIndex - 1 + keys.length) % keys.length];
    const prevInput = document.getElementById(getOptionInputId(prevKey));
    prevInput?.focus();
  } else if (event.key === ' ' || event.key === 'Enter') {
    event.preventDefault();
    handleSelect(currentKey);
  }
}

function switchMode(newMode) {
  const target = normalizeMode(newMode);
  if (target === currentMode.value) return;

  currentMode.value = target;
  const list = target === 'essay' ? essayQuestions.value : quizQuestions.value;
  currentQuestionId.value = list[0]?.id || null;

  updateUrlQuery();
  announceQuestion();
  focusHeading();
}

function goToPrev() {
  if (nav.value.hasPrev && nav.value.prevId) {
    navigateToId(nav.value.prevId);
  }
}

function goToNext() {
  if (nav.value.hasNext && nav.value.nextId) {
    navigateToId(nav.value.nextId);
  }
}

function jumpToQuestion(id) {
  showJumpModal.value = false;
  navigateToId(id);
}

function navigateToId(id) {
  currentQuestionId.value = id;
  emit('navigate', id);
  updateUrlQuery();
  announceQuestion();
  focusHeading();
}

async function toggleJumpModal() {
  showJumpModal.value = !showJumpModal.value;
  await nextTick();
  if (showJumpModal.value) modalRef.value?.querySelector('button')?.focus();
  else jumpTriggerRef.value?.focus();
}

function trapModalFocus(event) {
  const controls = [...(modalRef.value?.querySelectorAll('button:not(:disabled), a[href], [tabindex="0"]') || [])];
  const first = controls[0], last = controls.at(-1);
  if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last?.focus(); }
  else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first?.focus(); }
}

async function copyCode(event) {
  const button = event.target.closest('button.copy');
  if (!button) return;
  const code = button.parentElement?.querySelector('pre code')?.textContent;
  if (code == null || !navigator.clipboard?.writeText) return;
  try {
    await navigator.clipboard.writeText(code);
    liveStatus.value = 'Đã sao chép mã, giữ nguyên thụt dòng.';
  } catch { liveStatus.value = 'Có thể chọn đoạn mã để sao chép.'; }
}

async function focusHeading() {
  await nextTick();
  if (questionHeadingRef.value) {
    questionHeadingRef.value.focus();
  }
}

function announceQuestion() {
  const num = activeIndex.value + 1;
  const total = questionsForMode.value.length;
  const id = currentQuestion.value?.id || '';
  liveStatus.value = `Chuyển tới câu hỏi ${num} trên ${total}: ${id}`;
}

// URL query synchronization with history.replaceState
function updateUrlQuery() {
  if (typeof window === 'undefined') return;
  const queryStr = buildExamQueryString({
    mode: currentMode.value,
    questionId: currentQuestionId.value,
  });
  const url = new URL(window.location.href);
  url.search = queryStr;
  window.history.replaceState(null, '', url.toString());
}

function syncFromUrl() {
  if (typeof window === 'undefined') return;
  const { mode, questionId } = parseExamQuery(window.location.search);
  currentMode.value = mode;

  const list = mode === 'essay' ? essayQuestions.value : quizQuestions.value;
  const activeIdx = resolveActiveIndex(list, questionId || restoredQuestionId);
  if (activeIdx >= 0 && activeIdx < list.length) {
    currentQuestionId.value = list[activeIdx].id;
  } else {
    currentQuestionId.value = list[0]?.id || null;
  }
  updateUrlQuery();
}

// Keyboard shortcuts for full exam page navigation
function onGlobalKeydown(event) {
  if (showJumpModal.value || event.defaultPrevented || event.isComposing || event.ctrlKey || event.altKey || event.metaKey) return;

  const target = event.target;
  // Header controls and other dialogs keep their own keyboard interactions.
  if (target && target !== document.body && !examRootRef.value?.contains(target)) return;
  if (target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA' || target.tagName === 'SELECT' || target.closest('pre') || target.isContentEditable)) {
    return;
  }

  if (event.key === 'ArrowLeft') {
    if (nav.value.hasPrev) {
      event.preventDefault();
      goToPrev();
    }
  } else if (event.key === 'ArrowRight') {
    if (nav.value.hasNext) {
      event.preventDefault();
      goToNext();
    }
  } else if (currentMode.value === 'quiz' && !isAnswered.value) {
    const keyMap = {
      '1': 'A', 'a': 'A', 'A': 'A',
      '2': 'B', 'b': 'B', 'B': 'B',
      '3': 'C', 'c': 'C', 'C': 'C',
      '4': 'D', 'd': 'D', 'D': 'D',
    };
    const choice = keyMap[event.key];
    if (choice) {
      event.preventDefault();
      handleSelect(choice);
    }
  }
}

function onPopstate() {
  syncFromUrl();
  announceQuestion();
  focusHeading();
}

onMounted(() => {
  // Load persisted session answers safely
  const restored = props.restoreState?.();
  restoredQuestionId = restored?.currentQuestionId || null;
  const stored = loadStoredAnswers(storageKey.value);
  const answers = { ...restored?.answers, ...stored };
  if (answers && typeof answers === 'object') {
    Object.assign(sessionState.answers, reconcileStoredAnswers(props.bank.questions, answers));
  }

  // Sync state from query parameters on client mount
  syncFromUrl();

  // Attach window event listeners
  window.addEventListener('popstate', onPopstate);
  window.addEventListener('keydown', onGlobalKeydown);
});

onUnmounted(() => {
  restorePageScroll();
  if (typeof window !== 'undefined') {
    window.removeEventListener('popstate', onPopstate);
    window.removeEventListener('keydown', onGlobalKeydown);
  }
});
</script>

<style scoped>
/* StudyHub Design Tokens Integration */
.exam-practice {
  --ep-paper: var(--paper);
  --ep-canvas: var(--canvas);
  --ep-sunken: var(--sunken);
  --ep-rule: var(--rule);
  --ep-control: var(--control);
  --ep-ink: var(--ink);
  --ep-ink-2: var(--ink-2);
  --ep-ink-3: var(--ink-3);
  --ep-tim: var(--tim);
  --ep-tim-hover: var(--tim-hover);
  --ep-tim-soft: var(--tim-soft);
  --ep-do: var(--do);
  --ep-do-soft: var(--do-soft);
  --ep-xanh: var(--xanh);
  --ep-xanh-soft: var(--xanh-soft);
  --ep-font-ui: var(--font-ui, 'Be Vietnam Pro', system-ui, sans-serif);
  --ep-font-read: var(--font-read, 'Source Serif 4 Variable', Georgia, serif);
  --ep-font-code: var(--font-code, 'JetBrains Mono Variable', ui-monospace, monospace);
  --ep-radius: var(--radius, 8px);
  --ep-radius-lg: var(--radius-lg, 12px);

  width: 100%;
  max-width: 860px;
  margin: 0 auto;
  padding: 16px 20px 48px;
  font-family: var(--ep-font-ui);
  color: var(--ep-ink);
  box-sizing: border-box;
}

/* Header */
.exam-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: nowrap;
  gap: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--ep-rule);
}

.exam-header__left {
  flex: 1;
  min-width: 0;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.exam-header__title {
  flex: 1;
  min-width: 0;
  margin: 0;
  font-size: 20px;
  font-weight: 700;
  color: var(--ep-ink);
  line-height: 1.3;
}

.exam-header__lesson-tag {
  display: inline-flex;
  align-items: center;
  padding: 2px 10px;
  border-radius: 9999px;
  background: var(--ep-tim-soft);
  color: var(--ep-tim);
  font-size: 13px;
  font-weight: 600;
}

.exam-header__right {
  display: flex;
  align-items: center;
  gap: 12px;
}

/* Mode Switcher */
.exam-mode-switch {
  display: inline-flex;
  background: var(--ep-sunken);
  padding: 3px;
  border-radius: 9999px;
  border: 1px solid var(--ep-rule);
}

.exam-mode-switch__btn {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  min-height: 44px;
  padding: 6px 14px;
  border: none;
  border-radius: 9999px;
  background: transparent;
  color: var(--ep-ink-2);
  font-family: inherit;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 150ms ease;
}

.exam-mode-switch__btn:hover {
  color: var(--ep-ink);
}

.exam-mode-switch__btn.is-active {
  background: var(--ep-paper);
  color: var(--ep-tim);
  font-weight: 700;
  box-shadow: var(--shadow);
}

.exam-mode-switch__count {
  font-size: 12px;
  opacity: 0.8;
}

/* Jump to Question button */
.exam-jump-trigger {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  min-height: 44px;
  padding: 6px 14px;
  border-radius: 9999px;
  border: 1px solid var(--ep-rule);
  background: var(--ep-paper);
  color: var(--ep-ink-2);
  font-family: inherit;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 150ms ease;
}

.exam-jump-trigger:hover {
  background: var(--ep-sunken);
  color: var(--ep-ink);
}

/* Progress Row matching screenshot */
.exam-progress-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 20px 0 24px;
}

.exam-progress-bar-wrap {
  flex: 1;
  min-width: 100px;
}

.exam-progress-bar {
  width: 100%;
  height: 6px;
  border-radius: 9999px;
  background: var(--ep-sunken);
  overflow: hidden;
}

.exam-progress-bar__fill {
  height: 100%;
  background: var(--ep-ink-2);
  border-radius: 9999px;
  transition: width 200ms ease;
}

.exam-progress-info {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.exam-progress-counter {
  font-size: 15px;
  font-weight: 700;
  color: var(--ep-ink-2);
  letter-spacing: 0.02em;
}

/* Badges for Wrong/Correct counts */
.exam-score-badges {
  display: flex;
  align-items: center;
  gap: 8px;
}

.exam-score-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 13px;
  font-weight: 700;
}

.exam-score-badge--wrong {
  background: var(--ep-do-soft);
  color: var(--ep-do);
}

.exam-score-badge--correct {
  background: var(--ep-xanh-soft);
  color: var(--ep-xanh);
}

/* Question Card */
.exam-question-card {
  margin-top: 8px;
}

.exam-question__header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.exam-question__heading {
  margin: 0;
  font-size: 18px;
  font-weight: 700;
  color: var(--ep-ink);
  outline: none;
}

.exam-question__id-tag {
  display: none;
  font-size: 13px;
  font-weight: 500;
  color: var(--ep-ink-3);
  margin-left: 6px;
}

.exam-question__group-tag {
  display: none;
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 4px;
  background: var(--ep-sunken);
  color: var(--ep-ink-2);
}

.exam-question__prompt {
  font-size: 17px;
  line-height: 1.65;
  color: var(--ep-ink);
  margin-bottom: 24px;
  word-break: break-word;
}

/* Vertical Quiz Choices */
.exam-choices {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 32px;
}

.exam-choice {
  border-radius: var(--ep-radius-lg);
  background: var(--ep-sunken);
  border: 1.5px solid transparent;
  padding: 16px 18px;
  cursor: pointer;
  transition: all 160ms cubic-bezier(0.2, 0, 0, 1);
  box-sizing: border-box;
}

.exam-choice:not(.is-answered):hover {
  background: var(--ep-canvas);
  border-color: var(--ep-rule);
  transform: translateY(-1px);
}

.exam-choice.is-selected {
  border-color: var(--ep-tim);
  background: var(--ep-tim-soft);
}

.exam-choice.is-correct {
  border-color: var(--ep-xanh);
  background: var(--ep-xanh-soft);
}

.exam-choice.is-wrong {
  border-color: var(--ep-do);
  background: var(--ep-do-soft);
}

.exam-choice.is-answered {
  cursor: default;
}

.exam-choice__header {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  min-height: 44px;
}

/* Radio control */
.exam-choice__control {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
  min-height: 44px;
  cursor: pointer;
}

.exam-choice.is-answered .exam-choice__control {
  cursor: default;
}

.exam-choice__radio {
  width: 18px;
  height: 18px;
  accent-color: var(--ep-tim);
  margin: 0;
  cursor: pointer;
}

.exam-choice.is-answered .exam-choice__radio {
  cursor: default;
}

.exam-choice__key-label {
  font-size: 16px;
  font-weight: 700;
  color: var(--ep-ink);
}

/* Body */
.exam-choice__body {
  flex: 1;
  min-width: 0;
  padding-top: 10px;
}

.exam-choice__html {
  font-size: 16px;
  line-height: 1.55;
  color: var(--ep-ink);
  word-break: break-word;
}

.exam-choice__user-badge {
  display: inline-block;
  margin-top: 4px;
  font-size: 13px;
  font-weight: 500;
  color: var(--ep-ink-2);
}

/* Status Pill Badge matching screenshot */
.exam-choice__status-slot {
  flex-shrink: 0;
  padding-top: 8px;
}

.exam-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 9999px;
  font-size: 13px;
  font-weight: 700;
  white-space: nowrap;
}

.exam-badge--correct {
  background: var(--ep-xanh);
  color: var(--paper);
}

.exam-badge--wrong {
  background: var(--ep-do);
  color: var(--paper);
}

/* Per-option explanation text once answered */
.exam-choice__explanation {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px dashed var(--ep-rule);
  font-size: 15px;
  line-height: 1.55;
  color: var(--ep-ink-2);
  word-break: break-word;
}
.exam-choice__explanation :deep(p) { margin: 0 0 0.6em; }
.exam-choice__explanation :deep(p:last-child) { margin-bottom: 0; }

/* Quiz Extra Notes */
.exam-quiz-notes {
  margin-top: 16px;
  border-radius: var(--ep-radius);
  border: 1px solid var(--ep-rule);
  background: var(--ep-paper);
  overflow: hidden;
}

.exam-quiz-notes__summary {
  padding: 12px 16px;
  min-height: 44px;
  display: flex;
  align-items: center;
  cursor: pointer;
  font-weight: 600;
  font-size: 14px;
  color: var(--ep-tim);
  background: var(--ep-sunken);
}

.exam-quiz-notes__content {
  padding: 16px;
  font-size: 15px;
  line-height: 1.6;
}

.exam-quiz-notes__verification {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--ep-rule);
  font-size: 13px;
  color: var(--ep-ink-2);
}

/* ESSAY MODE */
.exam-essay {
  margin-bottom: 32px;
}

.exam-essay__details {
  border-radius: var(--ep-radius-lg);
  border: 1px solid var(--ep-rule);
  background: var(--ep-paper);
  overflow: hidden;
}

.exam-essay__summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 48px;
  padding: 14px 20px;
  background: var(--ep-sunken);
  color: var(--ep-ink);
  font-weight: 600;
  font-size: 15px;
  cursor: pointer;
  user-select: none;
  transition: background 150ms ease;
}

.exam-essay__summary:hover {
  background: var(--ep-canvas);
}

.exam-essay__summary-action {
  font-size: 13px;
  color: var(--ep-tim);
  font-weight: 500;
}

.exam-essay__body {
  padding: 20px;
  font-size: 16px;
  line-height: 1.65;
  color: var(--ep-ink);
  border-top: 1px solid var(--ep-rule);
}

.exam-essay__verification {
  margin-top: 16px;
  padding: 12px 16px;
  border-radius: var(--ep-radius);
  background: var(--ep-sunken);
  font-size: 14px;
  color: var(--ep-ink-2);
}

.exam-essay__verification-title {
  font-weight: 700;
  margin-bottom: 4px;
  color: var(--ep-ink);
}

/* Bottom Navigation Footer matching screenshot */
.exam-nav-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  padding-top: 20px;
  border-top: 1px solid var(--ep-rule);
}

.exam-nav-footer__hint {
  font-size: 13px;
  color: var(--ep-ink-3);
}

.exam-nav-footer__actions {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-left: auto;
}

.exam-nav-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 10px 24px;
  border-radius: 9999px;
  font-family: inherit;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 150ms ease;
  border: none;
}

.exam-nav-btn--prev {
  background: var(--ep-sunken);
  color: var(--ep-ink);
}

.exam-nav-btn--prev:hover:not(:disabled) {
  background: var(--ep-rule);
}

.exam-nav-btn--next {
  background: var(--ep-tim);
  color: var(--paper);
}

.exam-nav-btn--next:hover:not(:disabled) {
  background: var(--ep-tim-hover);
}

.exam-nav-btn:disabled {
  opacity: 0.45;
  cursor: not-allowed;
}

/* Focus Rings */
.exam-nav-btn:focus-visible,
.exam-jump-trigger:focus-visible,
.exam-mode-switch__btn:focus-visible,
.exam-choice__radio:focus-visible,
.exam-essay__summary:focus-visible,
.exam-modal__cell:focus-visible,
.exam-modal__close-btn:focus-visible {
  outline: 2px solid var(--ep-tim);
  outline-offset: 2px;
}

/* Jump Modal */
.exam-modal-backdrop {
  position: fixed;
  inset: 0;
  background: var(--scrim);
  backdrop-filter: blur(2px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
}

.exam-modal {
  width: 100%;
  max-width: 600px;
  max-height: 85vh;
  background: var(--ep-paper);
  border-radius: var(--ep-radius-lg);
  box-shadow: var(--shadow);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid var(--ep-rule);
}

.exam-modal__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid var(--ep-rule);
}

.exam-modal__title {
  margin: 0;
  font-size: 17px;
  font-weight: 700;
  color: var(--ep-ink);
}

.exam-modal__close-btn {
  background: transparent;
  border: none;
  font-size: 24px;
  line-height: 1;
  color: var(--ep-ink-2);
  cursor: pointer;
  padding: 4px 8px;
  min-height: 44px;
  border-radius: 4px;
}

.exam-modal__grid {
  flex: 1;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 16px;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(64px, 1fr));
  gap: 10px;
}

.exam-modal__cell {
  min-height: 48px;
  padding: 6px 4px;
  border-radius: var(--ep-radius);
  border: 1px solid var(--ep-rule);
  background: var(--ep-sunken);
  color: var(--ep-ink);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: inherit;
  transition: all 120ms ease;
}

.exam-modal__cell:hover {
  background: var(--ep-canvas);
  border-color: var(--ep-tim);
}

.exam-modal__cell.is-current {
  border-color: var(--ep-tim);
  box-shadow: 0 0 0 2px var(--ep-tim);
  font-weight: 700;
}

.exam-modal__cell.is-correct {
  background: var(--ep-xanh-soft);
  color: var(--ep-xanh);
  border-color: var(--ep-xanh);
}

.exam-modal__cell.is-wrong {
  background: var(--ep-do-soft);
  color: var(--ep-do);
  border-color: var(--ep-do);
}

.exam-modal__cell-num {
  font-size: 15px;
  font-weight: 700;
}

.exam-modal__cell-id {
  font-size: 10px;
  opacity: 0.75;
}

.exam-modal__legend {
  padding: 12px 20px;
  border-top: 1px solid var(--ep-rule);
  background: var(--ep-sunken);
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  font-size: 13px;
  color: var(--ep-ink-2);
}

.exam-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.exam-legend-dot {
  width: 10px;
  height: 10px;
  border-radius: 9999px;
}

.exam-legend-dot--current {
  border: 2px solid var(--ep-tim);
}

.exam-legend-dot--correct {
  background: var(--ep-xanh);
}

.exam-legend-dot--wrong {
  background: var(--ep-do);
}

.exam-legend-dot--unanswered {
  background: var(--ep-control);
}

/* Keep the answer body beside its A–D label on narrow screens. */
.exam-choice__body { min-width: 0; }
.exam-choice__status-slot { max-width: 100%; }
.exam-course-link { display: inline-block; min-height: 44px; padding-block: var(--space-2); }
.exam-question__heading { scroll-margin-top: 100px; }
.exam-practice :deep(div[class*="language-"]) { min-width: 0; max-width: 100%; }
.exam-practice :deep(pre) { width: 100%; box-sizing: border-box; }
.exam-practice :deep(div[class*="language-"] pre) { margin: 0; border: 0; padding-top: 40px; }
.exam-choice__html :deep(p) { margin: 0; }
.exam-practice :deep(p) { overflow-wrap: anywhere; }
@media (prefers-reduced-motion: reduce) {
  .exam-practice *, .exam-practice *::before, .exam-practice *::after { transition: none !important; }
}
/* Empty State */
.exam-empty {
  padding: 48px 20px;
  text-align: center;
  color: var(--ep-ink-2);
}

/* Screen reader only utility */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Scoped Rendered Content Styling (Markdown / Code / Math / Tables) */
:deep(pre),
:deep(code) {
  font-family: var(--ep-font-code);
  font-size: 14px;
}

:deep(pre) {
  overflow-x: auto;
  max-width: 100%;
  padding: 12px 16px;
  border-radius: var(--ep-radius);
  background: var(--ep-sunken);
  border: 1px solid var(--ep-rule);
  margin: 12px 0;
  white-space: pre;
}

:deep(table) {
  width: 100%;
  display: block;
  overflow-x: auto;
  border-collapse: collapse;
  margin: 16px 0;
}

:deep(th),
:deep(td) {
  border: 1px solid var(--ep-rule);
  padding: 8px 12px;
  text-align: left;
}

:deep(th) {
  background: var(--ep-sunken);
  font-weight: 600;
}

/* Math formatting: Zero scrollbars on equations */
:deep(.MathJax),
:deep(mjx-container),
:deep(.mjx-chtml) {
  overflow: visible !important;
  scrollbar-width: none !important;
  -ms-overflow-style: none !important;
}

:deep(mjx-assistive-mml) {
  display: none !important;
  visibility: hidden !important;
}

/* Responsive Media Queries down to 360px */
@media (max-width: 640px) {
  .exam-practice {
    padding: 12px 14px 40px;
  }

  .exam-header {
    flex-direction: column;
    align-items: stretch;
  }

  .exam-header__right {
    justify-content: space-between;
    gap: 8px;
  }
  .exam-mode-switch { flex: 1; }
  .exam-mode-switch__btn { flex: 1; justify-content: center; padding-inline: 8px; white-space: nowrap; }
  .exam-jump-trigger { padding-inline: 12px; }
  .exam-jump-trigger__text { display: none; }

  .exam-progress-row {
    margin: 16px 0 20px;
    gap: 12px;
  }

  .exam-choice__header {
    flex-wrap: wrap;
    align-items: flex-start;
  }

  .exam-choice__status-slot {
    flex-basis: 100%;
    width: 100%;
    align-self: flex-start;
    padding-top: 4px;
  }

  :deep(div[class*="language-"] > button.copy) { opacity: 1; min-width: 44px; min-height: 44px; top: 6px; }
  :deep(div[class*="language-"] > span.lang) { left: 16px; right: auto; top: 12px; }
  :deep(div[class*="language-"] > pre) { padding-top: 56px; }

  .exam-nav-footer {
    flex-direction: column;
    align-items: stretch;
  }

  .exam-nav-footer__actions {
    width: 100%;
    justify-content: space-between;
    margin-left: 0;
  }

  .exam-nav-btn {
    flex: 1;
  }
}
</style>
