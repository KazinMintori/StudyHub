<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useData } from 'vitepress'

// Reading mode hides the course sidebar and outline, and uses the browser's
// fullscreen view when it is available. It is deliberately not persisted:
// a sidebar that is missing after a reload, with no visible cause, confuses readers.
const { frontmatter } = useData()
const isZen = ref(false)
const LEGACY_STORAGE_KEY = 'studyhub:zen-mode'
const WIDE_QUERY = '(min-width: 960px)'
let enteredFullscreen = false

function setLayout(value) {
  isZen.value = value
  document.documentElement.classList.toggle('study-zen-mode', value)
}

async function enter() {
  setLayout(true)
  const root = document.documentElement
  if (!document.fullscreenElement && root.requestFullscreen) {
    try {
      await root.requestFullscreen({ navigationUI: 'hide' })
      enteredFullscreen = true
    } catch {
      // Fullscreen can be refused (iframes, browser policy). The reading layout still applies.
    }
  }
}

async function leave() {
  setLayout(false)
  if (enteredFullscreen && document.fullscreenElement) {
    enteredFullscreen = false
    try { await document.exitFullscreen() } catch { /* already left */ }
  }
  enteredFullscreen = false
}

function toggle() { isZen.value ? leave() : enter() }

// Esc in browser fullscreen is consumed by the browser, so follow its state instead.
function onFullscreenChange() {
  if (!document.fullscreenElement && enteredFullscreen) {
    enteredFullscreen = false
    setLayout(false)
  }
}

function handleKeydown(e) {
  if (frontmatter.value?.layout === 'home' || e.isComposing || e.metaKey || e.ctrlKey || e.altKey) return
  const target = e.target
  if (['INPUT', 'TEXTAREA', 'SELECT'].includes(target?.tagName) || target?.isContentEditable || target?.closest?.('[contenteditable="true"], dialog[open]')) return
  if (e.key?.toLowerCase() === 'f' && window.matchMedia(WIDE_QUERY).matches) {
    e.preventDefault()
    toggle()
  } else if (e.key === 'Escape' && isZen.value) {
    leave()
  }
}

onMounted(() => {
  try { localStorage.removeItem(LEGACY_STORAGE_KEY) } catch { /* storage may be blocked */ }
  window.addEventListener('keydown', handleKeydown)
  document.addEventListener('fullscreenchange', onFullscreenChange)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
  document.removeEventListener('fullscreenchange', onFullscreenChange)
  document.documentElement.classList.remove('study-zen-mode')
})
</script>

<template>
  <button
    v-if="frontmatter?.layout !== 'home'"
    type="button"
    class="zen-toggle-btn"
    :class="{ 'is-active': isZen }"
    :title="isZen ? 'Thoát chế độ đọc tập trung (F hoặc Esc)' : 'Đọc toàn màn hình, ẩn thanh bên và mục lục (F)'"
    :aria-pressed="isZen"
    @click="toggle"
  >
    <svg v-if="!isZen" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5M4 4l5 5M20 4l-5 5M4 20l5-5M20 20l-5-5" /></svg>
    <svg v-else viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M9 4v5H4M15 4v5h5M9 20v-5H4M15 20v-5h5M4 4l5 5M20 4l-5 5M4 20l5-5M20 20l-5-5" /></svg>
    <span class="zen-label">{{ isZen ? 'Thoát tập trung' : 'Đọc tập trung' }}</span>
  </button>
</template>

<style scoped>
.zen-toggle-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  min-height: 36px;
  min-width: 44px;
  padding: 0 var(--space-3);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  font: 500 var(--fs-small)/1 var(--font-ui);
  color: var(--ink-2);
  background: var(--paper);
  cursor: pointer;
  white-space: nowrap;
  transition: color var(--motion-fast) var(--ease), border-color var(--motion-fast) var(--ease), background var(--motion-fast) var(--ease);
}
.zen-toggle-btn svg { flex-shrink: 0; fill: none; stroke: currentColor; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; }
.zen-toggle-btn:hover { color: var(--tim); border-color: var(--tim); }
.zen-toggle-btn:focus-visible { outline: 2px solid var(--tim); outline-offset: 2px; }
.zen-toggle-btn.is-active { color: var(--tim); border-color: var(--tim); background: var(--tim-soft); }
@media (max-width: 1439px) {
  .zen-label { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
  .zen-toggle-btn { padding: 0; width: 44px; }
}
/* The reading layout only changes anything when the sidebar is shown. */
@media (max-width: 959px) { .zen-toggle-btn { display: none; } }
@media (prefers-reduced-motion: reduce) { .zen-toggle-btn { transition: none; } }
</style>
