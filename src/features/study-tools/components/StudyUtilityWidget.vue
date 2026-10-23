<script setup>
import { ref, computed, watch, nextTick, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vitepress'
import { useFocusTimer } from '../controllers/useFocusTimer.js'

defineProps({ courseName: { type: String, default: '' } })
const route = useRoute()
const { display, running, toggle, reset, remaining, minutes, finished, selectMinutes } = useFocusTimer()
const open = ref(false), showScratchpad = ref(false), noteContent = ref(''), storageError = ref(false)
const customMinutes = ref('25'), durationError = ref('')
const widgetRef = ref(null), triggerRef = ref(null), closeRef = ref(null), noteRef = ref(null)
const progressPercent = computed(() => Math.min(100, Math.max(0, (1 - remaining.value / (minutes.value * 60)) * 100)))
const showTopBar = computed(() => running.value || progressPercent.value > 0)
const storageKey = computed(() => `studyhub:scratchpad:${route.path.replace(/\.html$/, '')}`)
const hasNote = computed(() => Boolean(noteContent.value.trim()))
watch(minutes, value => { customMinutes.value = String(value); durationError.value = '' }, { immediate: true })
function applyDuration() {
  if (running.value) return
  const value = customMinutes.value.trim()
  if (!/^\d+$/.test(value) || !selectMinutes(Number(value))) {
    durationError.value = 'Nhập số phút nguyên từ 1 đến 240.'
    return
  }
  customMinutes.value = String(minutes.value)
  durationError.value = ''
}
function selectPreset(value) {
  if (running.value) return
  if (selectMinutes(value)) {
    customMinutes.value = String(value)
    durationError.value = ''
  }
}
const storageStatusText = computed(() => storageError.value
  ? 'Chưa lưu được. Bộ nhớ trình duyệt bị chặn hoặc đầy.'
  : hasNote.value ? 'Đã lưu trên trình duyệt này' : 'Ghi chú được lưu tự động trên trình duyệt này')

function loadNote() {
  if (typeof window === 'undefined') return
  try { noteContent.value = localStorage.getItem(storageKey.value) || ''; storageError.value = false }
  catch { noteContent.value = ''; storageError.value = true }
}
watch(() => route.path, () => { open.value = false; showScratchpad.value = false; loadNote() })
watch(noteContent, value => {
  if (typeof window === 'undefined') return
  try {
    if (value.trim()) localStorage.setItem(storageKey.value, value)
    else localStorage.removeItem(storageKey.value)
    storageError.value = false
  } catch { storageError.value = true }
})
async function toggleTools() {
  open.value = !open.value
  if (open.value) { await nextTick(); closeRef.value?.focus() }
}
function closeTools(restoreFocus = false) {
  open.value = false
  if (restoreFocus) nextTick(() => triggerRef.value?.focus())
}
async function toggleScratchpad() {
  showScratchpad.value = !showScratchpad.value
  if (showScratchpad.value) { await nextTick(); noteRef.value?.focus() }
}
function handleClickOutside(event) {
  if (open.value && !widgetRef.value?.contains(event.target)) closeTools()
}
function handleKeydown(event) {
  if (event.key !== 'Escape' || !open.value || document.querySelector('dialog[open]')) return
  event.stopPropagation()
  closeTools(true)
}
function handleFocusOut(event) {
  if (open.value && event.relatedTarget && !widgetRef.value?.contains(event.relatedTarget)) closeTools()
}
onMounted(() => {
  loadNote()
  document.addEventListener('click', handleClickOutside)
  document.addEventListener('keydown', handleKeydown)
})
onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
  document.removeEventListener('keydown', handleKeydown)
})
</script>

<template>
  <div ref="widgetRef" class="study-utility-widget" @focusout="handleFocusOut">
    <Teleport to="body">
      <div v-if="showTopBar" class="studyhub-pomodoro-top-bar" :style="{ width: `${progressPercent}%` }" aria-hidden="true" />
    </Teleport>
    <button ref="triggerRef" type="button" class="study-tools-trigger" :class="{ 'is-open': open }" aria-haspopup="dialog" :aria-expanded="open" aria-controls="study-tools-panel" @click="toggleTools">
      <svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="2" /><rect x="14" y="3" width="7" height="7" rx="2" /><rect x="3" y="14" width="7" height="7" rx="2" /><path d="M14 17.5h7m-3.5-3.5v7" /></svg>
      <span>Công cụ học tập</span>
      <span v-if="running" class="tools-running-time">{{ display }}</span>
      <svg class="tools-chevron" viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="m4 6 4 4 4-4" /></svg>
    </button>

    <section v-if="open" id="study-tools-panel" class="study-tools-panel" role="dialog" aria-labelledby="study-tools-title">
      <header class="study-tools-header">
        <div><h2 id="study-tools-title">Công cụ học tập</h2><p>{{ courseName }}</p></div>
        <button ref="closeRef" type="button" class="study-tools-close" aria-label="Đóng công cụ học tập" @click="closeTools(true)"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18" /></svg></button>
      </header>
      <div class="study-tools-cards">
        <section class="study-tool-card timer-tool-card" aria-labelledby="focus-tool-title">
          <div class="tool-card-heading">
            <span class="tool-icon timer-icon"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="13" r="8" /><path d="M12 9v4l2.5 1.5M9 2h6m-3 0v3m6 1 1.5-1.5" /></svg></span>
            <div><h3 id="focus-tool-title">Hẹn giờ tập trung</h3><p>{{ finished ? 'Đã hoàn thành phiên học' : running ? 'Đang trong phiên học' : 'Dành một khoảng riêng để học' }}</p></div>
          </div>
          <div class="timer-presets" aria-label="Thời lượng phiên học">
            <button v-for="duration in [25, 50]" :key="duration" type="button" :aria-pressed="minutes === duration" :disabled="running" @click="selectPreset(duration)">{{ duration }} phút</button>
          </div>
          <form class="custom-timer-form" novalidate @submit.prevent="applyDuration">
            <label for="custom-focus-minutes">Thời gian tùy chọn (phút)</label>
            <div class="custom-timer-row">
              <input id="custom-focus-minutes" v-model="customMinutes" type="text" inputmode="numeric" pattern="[0-9]*" maxlength="3" autocomplete="off" :disabled="running" :aria-invalid="Boolean(durationError)" aria-describedby="custom-duration-hint" />
              <button type="submit" :disabled="running">Áp dụng</button>
            </div>
            <p id="custom-duration-hint" :class="{ 'is-error': durationError }" :role="durationError ? 'alert' : undefined">{{ durationError || (running ? 'Tạm dừng để đổi thời lượng.' : '1–240 phút. Áp dụng sẽ đặt lại đồng hồ.') }}</p>
          </form>
          <div class="pomo-time" role="timer" :aria-label="`Thời gian còn lại: ${display}`">{{ display }}</div>
          <div class="timer-card-actions">
            <button type="button" class="pomo-toggle" :aria-label="running ? 'Tạm dừng Pomodoro' : 'Bắt đầu Pomodoro'" @click="toggle">
              <svg v-if="running" viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M7 4v12m6-12v12" /></svg>
              <svg v-else viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round" aria-hidden="true"><path d="m6 3 10 7-10 7z" /></svg>
              {{ running ? 'Tạm dừng' : finished ? 'Học tiếp' : 'Bắt đầu' }}
            </button>
            <button type="button" class="pomo-reset" aria-label="Đặt lại Pomodoro" @click="reset"><svg viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7a6.5 6.5 0 1 1-.5 5M4 3v4h4" /></svg>Đặt lại</button>
          </div>
        </section>

        <section class="study-tool-card note-tool-card">
          <button type="button" class="scratchpad-toggle-btn" :aria-expanded="showScratchpad" aria-controls="study-note-body" @click="toggleScratchpad">
            <span class="tool-icon note-icon"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-9M8 16l1-4L18 3l3 3-9 9-4 1z" /></svg></span>
            <span class="note-card-copy"><strong>Sổ nháp</strong><span>{{ hasNote ? 'Trang này có ghi chú đã lưu' : 'Ghi lại ý tưởng cho trang đang đọc' }}</span></span>
            <svg class="note-chevron" :class="{ 'is-open': showScratchpad }" viewBox="0 0 16 16" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="m4 6 4 4 4-4" /></svg>
          </button>
          <div v-if="showScratchpad" id="study-note-body" class="scratchpad-body">
            <label for="study-scratchpad">Ghi chú cho trang này</label>
            <textarea id="study-scratchpad" ref="noteRef" v-model="noteContent" rows="5" class="scratchpad-textarea" placeholder="Công thức cần nhớ, ý tưởng hoặc câu hỏi…" />
            <p class="scratchpad-hint" :class="{ 'is-error': storageError }" role="status">{{ storageStatusText }}</p>
          </div>
        </section>
      </div>
    </section>
  </div>
</template>

<style scoped>
.study-utility-widget { position:relative; flex-shrink:0; font-family:var(--font-ui); }
.study-tools-trigger { display:inline-flex; align-items:center; gap:var(--space-2); min-height:44px; padding:0 var(--space-3); border:1px solid var(--rule); border-radius:var(--radius); background:var(--paper); color:var(--ink-2); font:600 var(--fs-small)/1.4 var(--font-ui); white-space:nowrap; cursor:pointer; transition:background var(--motion-fast) var(--ease),border-color var(--motion-fast) var(--ease); }
.study-tools-trigger:hover,.study-tools-trigger.is-open { background:var(--tim-soft); color:var(--tim); border-color:var(--control); }
.tools-chevron { flex-shrink:0; transition:transform var(--motion-fast) var(--ease); }
.is-open .tools-chevron { transform:rotate(180deg); }
.tools-running-time { padding-left:var(--space-2); border-left:1px solid var(--rule); color:var(--tim); font-variant-numeric:tabular-nums; }
.study-tools-panel { position:absolute; top:calc(100% + var(--space-3)); right:0; width:min(400px,calc(100vw - 32px)); max-height:calc(100dvh - var(--vp-nav-height) - 32px); overflow-y:auto; padding:var(--space-4); background:var(--paper); color:var(--ink); border:1px solid var(--rule); border-radius:var(--radius-xl); box-shadow:var(--shadow-lift); z-index:100; box-sizing:border-box; }
.study-tools-header { display:flex; align-items:flex-start; justify-content:space-between; gap:var(--space-2); margin-bottom:var(--space-4); }
.study-tools-header h2 { margin:3px 0 var(--space-1); font:600 17px/1.4 var(--font-ui); }
.study-tools-header p { margin:0; color:var(--ink-3); font-size:var(--fs-meta); line-height:1.5; }
.study-tools-close { display:grid; place-items:center; flex:0 0 44px; width:44px; height:44px; border:1px solid var(--rule); border-radius:var(--radius); background:var(--paper); color:var(--ink-2); cursor:pointer; }
.study-tools-close:hover { background:var(--canvas); color:var(--ink); }
.study-tools-cards { display:grid; gap:var(--space-3); }
.study-tool-card { min-width:0; border:1px solid var(--rule); border-radius:var(--radius-lg); background:var(--canvas); }
.timer-tool-card { padding:var(--space-4); }
.tool-card-heading { display:flex; align-items:center; gap:var(--space-3); }
.tool-icon { display:grid; place-items:center; flex:0 0 40px; width:40px; height:40px; border-radius:var(--radius); }
.timer-icon { background:var(--tim-soft); color:var(--tim); }
.note-icon { background:var(--lam-soft); color:var(--lam); }
.tool-card-heading h3 { margin:0 0 2px; font:600 var(--fs-ui)/1.4 var(--font-ui); }
.tool-card-heading p { margin:0; color:var(--ink-3); font-size:var(--fs-meta); line-height:1.5; }
.timer-presets { display:flex; justify-content:center; gap:var(--space-2); margin-top:var(--space-4); }
.timer-presets button { min-width:84px; min-height:44px; padding:var(--space-2) var(--space-3); border:1px solid var(--rule); border-radius:var(--radius); background:var(--paper); color:var(--ink-2); font:500 var(--fs-small)/1.4 var(--font-ui); cursor:pointer; }
.timer-presets button[aria-pressed=true] { color:var(--tim); border-color:var(--tim); background:var(--tim-soft); }
.timer-presets button:disabled { cursor:default; }
.custom-timer-form { margin-top:var(--space-3); }
.custom-timer-form label { display:block; margin-bottom:var(--space-2); color:var(--ink-2); font-size:var(--fs-meta); line-height:1.5; }
.custom-timer-row { display:grid; grid-template-columns:minmax(0,1fr) auto; gap:var(--space-2); }
.custom-timer-row input { width:100%; min-width:0; min-height:44px; padding:var(--space-2) var(--space-3); border:1px solid var(--rule); border-radius:var(--radius); background:var(--paper); color:var(--ink); font:500 16px/1.4 var(--font-ui); box-sizing:border-box; }
.custom-timer-row button { min-height:44px; padding:var(--space-2) var(--space-3); border:1px solid var(--rule); border-radius:var(--radius); background:var(--paper); color:var(--ink-2); font:600 var(--fs-small)/1.4 var(--font-ui); cursor:pointer; }
.custom-timer-row button:hover:not(:disabled) { background:var(--tim-soft); color:var(--tim); }
.custom-timer-row :disabled { opacity:.6; cursor:default; }
.custom-timer-form p { margin:var(--space-2) 0 0; color:var(--ink-3); font-size:var(--fs-meta); line-height:1.5; }
.custom-timer-form p.is-error { color:var(--do); }
.pomo-time { margin:var(--space-3) 0 var(--space-4); text-align:center; font:500 48px/1.2 var(--font-ui); font-variant-numeric:tabular-nums; letter-spacing:-1.5px; color:var(--ink); }
.timer-card-actions { display:grid; grid-template-columns:1fr auto; gap:var(--space-2); }
.timer-card-actions button { display:flex; align-items:center; justify-content:center; gap:var(--space-2); min-height:44px; padding:var(--space-2) var(--space-3); border:1px solid var(--rule); border-radius:var(--radius); font:600 var(--fs-small)/1.4 var(--font-ui); cursor:pointer; }
.pomo-toggle { background:var(--tim); color:var(--paper); }
.pomo-toggle:hover { background:var(--tim-hover); }
.pomo-reset { background:var(--paper); color:var(--ink-2); }
.pomo-reset:hover { background:var(--sunken); }
.scratchpad-toggle-btn { display:flex; align-items:center; gap:var(--space-3); width:100%; min-height:84px; padding:var(--space-4); border:0; border-radius:var(--radius-lg); background:transparent; color:var(--ink); text-align:left; cursor:pointer; }
.scratchpad-toggle-btn:hover { background:var(--sunken); }
.note-card-copy { display:grid; flex:1; min-width:0; gap:var(--space-1); }
.note-card-copy strong { font:600 var(--fs-ui)/1.4 var(--font-ui); }
.note-card-copy>span { color:var(--ink-3); font-size:var(--fs-meta); line-height:1.5; }
.note-chevron { flex:0 0 16px; color:var(--ink-3); transition:transform var(--motion-fast) var(--ease); }
.note-chevron.is-open { transform:rotate(180deg); }
.scratchpad-body { padding:0 var(--space-4) var(--space-4); }
.scratchpad-body label { display:block; margin-bottom:var(--space-2); font-size:var(--fs-meta); color:var(--ink-2); }
.scratchpad-textarea { display:block; width:100%; min-height:120px; padding:var(--space-3); border:1px solid var(--rule); border-radius:var(--radius); background:var(--paper); color:var(--ink); font:400 var(--fs-small)/1.6 var(--font-ui); resize:vertical; box-sizing:border-box; }
.scratchpad-hint { margin:var(--space-2) 0 0; color:var(--ink-3); font-size:var(--fs-meta); line-height:1.5; }
.scratchpad-hint.is-error { color:var(--do); }
:is(button,textarea):focus-visible { outline:2px solid var(--tim); outline-offset:3px; }
@media(max-width:767px) { .study-tools-panel { position:fixed; top:calc(var(--vp-nav-height) + 60px); right:16px; max-height:calc(100dvh - var(--vp-nav-height) - 76px); } }
@media(max-width:479px) { .tools-running-time { display:none; } }
@media(prefers-reduced-motion:reduce) { .tools-chevron,.note-chevron,.study-tools-trigger { transition:none; } }
</style>

<style>
.studyhub-pomodoro-top-bar { position:fixed; top:0; left:0; height:2px; background:var(--tim); box-shadow:none; z-index:99999; pointer-events:none; transition:width var(--motion-fast) var(--ease); }
@media(prefers-reduced-motion:reduce) { .studyhub-pomodoro-top-bar { transition:none; } }
</style>
