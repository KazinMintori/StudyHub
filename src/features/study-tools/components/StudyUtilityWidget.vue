<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vitepress'
import { useFocusTimer } from '../controllers/useFocusTimer.js'

const route = useRoute()
const { display, running, toggle, reset, remaining, minutes, finished } = useFocusTimer()

const progressPercent = computed(() => {
  const total = (minutes?.value || 25) * 60
  if (!total) return 0
  const rem = remaining?.value ?? total
  return Math.min(100, Math.max(0, ((total - rem) / total) * 100))
})

const showTopBar = computed(() => running?.value || progressPercent.value > 0)

const showScratchpad = ref(false)
const noteContent = ref('')
const storageError = ref(false)
const widgetRef = ref(null)

const storageKey = computed(() => {
  const p = route?.path || ''
  return `studyhub:scratchpad:${p.replace(/\.html$/, '')}`
})

const hasNote = computed(() => Boolean(noteContent.value && noteContent.value.trim().length > 0))

const storageStatusText = computed(() => {
  if (storageError.value) {
    return 'Không thể lưu (Bộ nhớ trình duyệt bị chặn hoặc đầy)'
  }
  if (hasNote.value) {
    return 'Đã lưu tự động trên trình duyệt'
  }
  return 'Tự động lưu vào trình duyệt'
})

function loadNote() {
  if (typeof window === 'undefined') return
  try {
    noteContent.value = localStorage.getItem(storageKey.value) || ''
    storageError.value = false
  } catch {
    noteContent.value = ''
    storageError.value = true
  }
}

watch(() => route.path, loadNote)

watch(noteContent, (val) => {
  if (typeof window === 'undefined') return
  try {
    if (val && val.trim()) {
      localStorage.setItem(storageKey.value, val)
    } else {
      localStorage.removeItem(storageKey.value)
    }
    storageError.value = false
  } catch {
    storageError.value = true
  }
})

function handleClickOutside(e) {
  if (showScratchpad.value && widgetRef.value && !widgetRef.value.contains(e.target)) {
    showScratchpad.value = false
  }
}

function handleKeydown(e) {
  if (e.key === 'Escape' && showScratchpad.value) {
    e.stopPropagation()
    showScratchpad.value = false
  }
}

onMounted(() => {
  loadNote()
  if (typeof document !== 'undefined') {
    document.addEventListener('click', handleClickOutside)
    document.addEventListener('keydown', handleKeydown)
  }
})

onUnmounted(() => {
  if (typeof document !== 'undefined') {
    document.removeEventListener('click', handleClickOutside)
    document.removeEventListener('keydown', handleKeydown)
  }
})
</script>

<template>
  <div ref="widgetRef" class="study-utility-widget">
    <!-- Top-edge Ambient Pomodoro Bar: exactly 2px, subdued token singlecolor, no glow, no pointer interception -->
    <Teleport to="body">
      <div
        v-if="showTopBar"
        class="studyhub-pomodoro-top-bar"
        :style="{ width: `${progressPercent}%` }"
        aria-hidden="true"
      />
    </Teleport>

    <!-- Ambient Pomodoro Pill with clear compact text labels, 44px targets -->
    <div class="pomodoro-pill" :class="{ 'is-running': running, 'is-finished': finished }">
      <button
        type="button"
        class="pomo-toggle"
        :title="running ? 'Tạm dừng Pomodoro' : 'Bắt đầu Pomodoro'"
        :aria-label="running ? 'Tạm dừng Pomodoro' : 'Bắt đầu Pomodoro'"
        @click="toggle"
      >
        <span class="pomo-label">{{ running ? 'Dừng' : 'Học' }}</span>
        <span class="pomo-time">{{ display }}</span>
      </button>
      <button
        type="button"
        class="pomo-reset"
        title="Đặt lại Pomodoro"
        aria-label="Đặt lại Pomodoro"
        @click="reset"
      >
        Đặt lại
      </button>
    </div>

    <!-- Contextual Scratchpad Button: clear compact text label 'Nháp', 44px target -->
    <button
      type="button"
      class="scratchpad-toggle-btn"
      :class="{ 'has-note': hasNote, 'is-active': showScratchpad }"
      :title="showScratchpad ? 'Đóng sổ nháp' : 'Sổ nháp cho bài này'"
      :aria-label="showScratchpad ? 'Đóng sổ nháp' : (hasNote ? 'Mở sổ nháp (đang có ghi chú)' : 'Mở sổ nháp')"
      :aria-expanded="showScratchpad"
      @click="showScratchpad = !showScratchpad"
    >
      <span>Nháp</span>
    </button>

    <!-- Contextual Scratchpad Popover: honest storage status, 44px close target -->
    <div v-if="showScratchpad" class="scratchpad-popover" role="dialog" aria-label="Sổ nháp bài học">
      <div class="scratchpad-header">
        <span class="scratchpad-title">Ghi chú nháp cho bài này</span>
        <button
          type="button"
          class="scratchpad-close-btn"
          aria-label="Đóng sổ nháp"
          title="Đóng sổ nháp"
          @click="showScratchpad = false"
        >
          Đóng
        </button>
      </div>
      <textarea
        v-model="noteContent"
        rows="5"
        class="scratchpad-textarea"
        placeholder="Ghi nhanh công thức, ý tưởng hoặc thắc mắc của bạn (Tự động lưu)..."
        aria-label="Nội dung ghi chú nháp"
      />
      <div class="scratchpad-footer">
        <span class="scratchpad-hint" :class="{ 'is-error': storageError }">
          {{ storageStatusText }}
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.study-utility-widget {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: var(--space-2, 8px);
  flex-shrink: 0;
}

.pomodoro-pill {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1, 4px);
  min-height: 44px;
  padding: 0 4px;
  border-radius: var(--radius-sm, 4px);
  background: var(--canvas);
  border: 1px solid var(--rule);
  font-variant-numeric: tabular-nums;
  font-family: var(--font-ui);
  font-size: var(--fs-small, 14px);
  box-sizing: border-box;
  transition: border-color var(--motion-fast, 120ms) var(--ease),
              background-color var(--motion-fast, 120ms) var(--ease);
}
.pomodoro-pill.is-running {
  border-color: var(--xanh);
  background: var(--xanh-soft);
}
.pomodoro-pill.is-finished {
  border-color: var(--vang);
  background: var(--vang-soft);
}

.pomo-toggle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-1, 4px);
  min-height: 44px;
  min-width: 44px;
  padding: 0 var(--space-2, 8px);
  border: none;
  background: transparent;
  color: var(--ink);
  font-family: var(--font-ui);
  font-size: var(--fs-small, 14px);
  font-weight: 500;
  cursor: pointer;
  border-radius: var(--radius-sm, 4px);
  box-sizing: border-box;
  transition: background-color var(--motion-fast, 120ms) var(--ease),
              color var(--motion-fast, 120ms) var(--ease);
  white-space: nowrap;
}
.pomo-toggle:hover {
  background: var(--sunken);
  color: var(--tim);
}
.pomo-toggle:focus-visible {
  outline: 2px solid var(--tim);
  outline-offset: -2px;
}

.pomo-label {
  font-weight: 600;
}

.pomo-time {
  font-variant-numeric: tabular-nums;
}

.pomo-reset {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  min-width: 44px;
  padding: 0 var(--space-2, 8px);
  border: none;
  background: transparent;
  color: var(--ink-3);
  font-family: var(--font-ui);
  font-size: var(--fs-meta, 13px);
  font-weight: 500;
  cursor: pointer;
  border-radius: var(--radius-sm, 4px);
  box-sizing: border-box;
  transition: background-color var(--motion-fast, 120ms) var(--ease),
              color var(--motion-fast, 120ms) var(--ease);
  white-space: nowrap;
}
.pomo-reset:hover {
  background: var(--sunken);
  color: var(--tim);
}
.pomo-reset:focus-visible {
  outline: 2px solid var(--tim);
  outline-offset: -2px;
}

.scratchpad-toggle-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
  padding: 0 var(--space-3, 12px);
  border-radius: var(--radius-sm, 4px);
  background: var(--canvas);
  border: 1px solid var(--rule);
  color: var(--ink-2);
  font-family: var(--font-ui);
  font-size: var(--fs-small, 14px);
  font-weight: 500;
  cursor: pointer;
  box-sizing: border-box;
  transition: all var(--motion-fast, 120ms) var(--ease);
  white-space: nowrap;
}
.scratchpad-toggle-btn:hover,
.scratchpad-toggle-btn.is-active {
  background: var(--sunken);
  color: var(--tim);
  border-color: var(--control);
}
.scratchpad-toggle-btn:focus-visible {
  outline: 2px solid var(--tim);
  outline-offset: 2px;
}
.scratchpad-toggle-btn.has-note {
  color: var(--tim);
  border-color: var(--tim);
  font-weight: 600;
}

.scratchpad-popover {
  position: absolute;
  top: calc(100% + var(--space-2, 8px));
  right: 0;
  width: min(320px, calc(100vw - 24px));
  padding: var(--space-4, 16px);
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: var(--radius-lg, 12px);
  box-shadow: var(--shadow);
  z-index: 100;
  box-sizing: border-box;
}
.scratchpad-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-2, 8px);
  margin-bottom: var(--space-2, 8px);
}
.scratchpad-title {
  font-family: var(--font-ui);
  font-size: var(--fs-meta, 13px);
  font-weight: 600;
  color: var(--ink-2);
}
.scratchpad-close-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  min-width: 44px;
  background: transparent;
  border: 1px solid transparent;
  color: var(--ink-3);
  font-family: var(--font-ui);
  font-size: var(--fs-meta, 13px);
  font-weight: 500;
  cursor: pointer;
  padding: 0 var(--space-2, 8px);
  border-radius: var(--radius-sm, 4px);
  box-sizing: border-box;
  transition: all var(--motion-fast, 120ms) var(--ease);
}
.scratchpad-close-btn:hover {
  background: var(--sunken);
  color: var(--ink);
  border-color: var(--rule);
}
.scratchpad-close-btn:focus-visible {
  outline: 2px solid var(--tim);
  outline-offset: 2px;
}

.scratchpad-textarea {
  width: 100%;
  min-height: 120px;
  padding: var(--space-2, 8px);
  border: 1px solid var(--rule);
  border-radius: var(--radius-sm, 4px);
  background: var(--canvas);
  color: var(--ink);
  font-family: var(--font-ui);
  font-size: var(--fs-small, 14px);
  line-height: 1.5;
  resize: vertical;
  box-sizing: border-box;
}
.scratchpad-textarea:focus {
  border-color: var(--tim);
  outline: 1px solid var(--tim);
}

.scratchpad-footer {
  margin-top: var(--space-2, 8px);
  font-size: var(--fs-meta, 13px);
  color: var(--ink-3);
  text-align: right;
}
.scratchpad-hint.is-error {
  color: var(--do);
  font-weight: 500;
}

@media (max-width: 480px) {
  .pomo-label {
    display: none;
  }
}
</style>

<style>
/* Global top-bar running on top edge of window */
.studyhub-pomodoro-top-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 2px;
  background: var(--tim);
  box-shadow: none;
  z-index: 99999;
  transition: width var(--motion-fast, 120ms) var(--ease);
  pointer-events: none;
}
@media (prefers-reduced-motion:reduce) {
 .studyhub-pomodoro-top-bar { transition:none; }
}
</style>
