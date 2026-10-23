<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vitepress'
import { useFocusTimer } from '../controllers/useFocusTimer.js'

const route = useRoute()
const { display, running, toggle, reset, remaining, minutes } = useFocusTimer()

const progressPercent = computed(() => {
  const total = (minutes?.value || 25) * 60
  if (!total) return 0
  const rem = remaining?.value ?? total
  return Math.min(100, Math.max(0, ((total - rem) / total) * 100))
})

const showScratchpad = ref(false)
const noteContent = ref('')
const widgetRef = ref(null)

const storageKey = computed(() => {
  const p = route?.path || ''
  return `studyhub:scratchpad:${p.replace(/\.html$/, '')}`
})

function loadNote() {
  if (typeof window === 'undefined') return
  try {
    noteContent.value = localStorage.getItem(storageKey.value) || ''
  } catch {
    noteContent.value = ''
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
  } catch {
    // Ignore storage quota errors
  }
})

function handleClickOutside(e) {
  if (showScratchpad.value && widgetRef.value && !widgetRef.value.contains(e.target)) {
    showScratchpad.value = false
  }
}

function handleKeydown(e) {
  if (e.key === 'Escape' && showScratchpad.value) {
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
    <!-- Top-edge Ambient Pomodoro Bar -->
    <Teleport to="body">
      <div
        v-if="running || (progressPercent > 0 && progressPercent < 100)"
        class="studyhub-pomodoro-top-bar"
        :style="{ width: `${progressPercent}%` }"
        aria-hidden="true"
      />
    </Teleport>

    <!-- Ambient Pomodoro Pill -->
    <div class="pomodoro-pill" :class="{ 'is-running': running }">
      <button
        type="button"
        class="pomo-toggle"
        :title="running ? 'Tạm dừng Pomodoro' : 'Bắt đầu phiên học tập trung'"
        :aria-label="running ? 'Tạm dừng Pomodoro' : 'Bắt đầu Pomodoro'"
        @click="toggle"
      >
        <span class="pomo-dot" aria-hidden="true" />
        <span class="pomo-time">{{ display }}</span>
      </button>
      <button
        type="button"
        class="pomo-reset"
        title="Đặt lại đồng hồ"
        aria-label="Đặt lại Pomodoro"
        @click="reset"
      >
        <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <polyline points="1 4 1 10 7 10" />
          <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10" />
        </svg>
      </button>
    </div>

    <!-- Contextual Scratchpad Button -->
    <button
      type="button"
      class="scratchpad-toggle-btn"
      :class="{ 'has-note': noteContent.trim().length > 0, 'is-active': showScratchpad }"
      title="Sổ nháp cho bài này (Tự động lưu)"
      :aria-label="showScratchpad ? 'Đóng sổ nháp' : 'Mở sổ nháp'"
      :aria-expanded="showScratchpad"
      @click="showScratchpad = !showScratchpad"
    >
      <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M12 20h9" />
        <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z" />
      </svg>
      <span v-if="noteContent.trim().length > 0" class="note-indicator" aria-hidden="true" />
    </button>

    <!-- Contextual Scratchpad Popover -->
    <div v-if="showScratchpad" class="scratchpad-popover" role="dialog" aria-label="Sổ nháp bài học">
      <div class="scratchpad-header">
        <span class="scratchpad-title">Ghi chú nháp cho bài này</span>
        <button
          type="button"
          class="scratchpad-close-btn"
          aria-label="Đóng sổ nháp"
          @click="showScratchpad = false"
        >
          ✕
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
        <span class="scratchpad-hint">Đã lưu tự động trên trình duyệt</span>
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
  margin-inline: var(--space-2, 8px);
}

.pomodoro-pill {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  min-height: 32px;
  padding: 3px 8px;
  border-radius: 999px;
  background: var(--canvas);
  border: 1px solid var(--rule);
  font-variant-numeric: tabular-nums;
  font-family: var(--font-ui);
  font-size: var(--fs-small, 13px);
  transition: all var(--motion-fast, 120ms) var(--ease);
}
.pomodoro-pill.is-running {
  border-color: var(--xanh, #1d6b45);
  background: var(--xanh-soft, #e6f4ec);
}

.pomo-toggle {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  border: none;
  background: transparent;
  color: var(--ink);
  font-weight: 500;
  cursor: pointer;
  padding: 0;
}
.pomo-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--ink-3);
  transition: all var(--motion-fast, 120ms) var(--ease);
}
.pomodoro-pill.is-running .pomo-dot {
  background: var(--xanh, #1d6b45);
  box-shadow: 0 0 6px var(--xanh, #1d6b45);
}

.pomo-reset {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border: none;
  background: transparent;
  color: var(--ink-3);
  cursor: pointer;
  padding: 0;
  border-radius: 50%;
  transition: color var(--motion-fast, 120ms) var(--ease);
}
.pomo-reset:hover {
  color: var(--tim);
}

.scratchpad-toggle-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 32px;
  min-height: 32px;
  padding: 4px;
  border-radius: var(--radius-sm, 6px);
  background: var(--canvas);
  border: 1px solid var(--rule);
  color: var(--ink-2);
  cursor: pointer;
  transition: all var(--motion-fast, 120ms) var(--ease);
}
.scratchpad-toggle-btn:hover,
.scratchpad-toggle-btn.is-active {
  background: var(--sunken);
  color: var(--tim);
  border-color: var(--control);
}
.note-indicator {
  position: absolute;
  top: 3px;
  right: 3px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--tim);
}

.scratchpad-popover {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  width: min(320px, calc(100vw - 32px));
  padding: var(--space-4, 16px);
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: var(--radius-lg, 12px);
  box-shadow: var(--shadow);
  z-index: 100;
}
.scratchpad-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-2, 8px);
}
.scratchpad-title {
  font-family: var(--font-ui);
  font-size: var(--fs-meta, 12px);
  font-weight: 600;
  color: var(--ink-2);
}
.scratchpad-close-btn {
  background: transparent;
  border: none;
  color: var(--ink-3);
  font-size: 14px;
  cursor: pointer;
  padding: 2px 6px;
  border-radius: 4px;
}
.scratchpad-close-btn:hover {
  background: var(--sunken);
  color: var(--ink);
}
.scratchpad-textarea {
  width: 100%;
  min-height: 110px;
  padding: var(--space-2, 8px);
  border: 1px solid var(--rule);
  border-radius: var(--radius-sm, 6px);
  background: var(--canvas);
  color: var(--ink);
  font-family: var(--font-ui);
  font-size: var(--fs-small, 13px);
  line-height: 1.5;
  resize: vertical;
}
.scratchpad-footer {
  margin-top: var(--space-2, 8px);
  font-size: 11px;
  color: var(--ink-3);
  text-align: right;
}

@media (max-width: 600px) {
  .pomo-time {
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
  height: 2.5px;
  background: linear-gradient(90deg, #6366f1, #10b981);
  box-shadow: 0 0 8px rgba(99, 102, 241, 0.5);
  z-index: 99999;
  transition: width 0.35s ease;
  pointer-events: none;
}
</style>
