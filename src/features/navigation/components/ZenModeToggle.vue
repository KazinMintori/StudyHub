<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useData } from 'vitepress'

const { frontmatter } = useData()
const isZen = ref(false)
const STORAGE_KEY = 'studyhub:zen-mode'

function applyZenState(value) {
  isZen.value = value
  if (typeof document !== 'undefined') {
    document.documentElement.classList.toggle('study-zen-mode', value)
    try {
      localStorage.setItem(STORAGE_KEY, value ? '1' : '0')
    } catch {
      // Ignore storage errors in restricted contexts
    }
  }
}

function toggleZen() {
  applyZenState(!isZen.value)
}

function handleKeydown(e) {
  if (frontmatter.value?.layout === 'home') return
  if (e.isComposing) return
  if (e.metaKey || e.ctrlKey || e.altKey) return

  const target = e.target
  if (['INPUT', 'TEXTAREA', 'SELECT'].includes(target?.tagName) || target?.isContentEditable || Boolean(target?.closest?.('[contenteditable="true"]'))) return

  if (e.key && e.key.toLowerCase() === 'f') {
    e.preventDefault()
    toggleZen()
  } else if (e.key === 'Escape' && isZen.value) {
    applyZenState(false)
  }
}

onMounted(() => {
  if (typeof window !== 'undefined') {
    try {
      const saved = localStorage.getItem(STORAGE_KEY) === '1'
      if (saved) applyZenState(true)
    } catch {
      // Ignore storage errors
    }
    window.addEventListener('keydown', handleKeydown)
  }
})

onUnmounted(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('keydown', handleKeydown)
    document.documentElement.classList.remove('study-zen-mode')
  }
})
</script>

<template>
  <button
    v-if="frontmatter?.layout !== 'home'"
    type="button"
    class="zen-toggle-btn"
    :class="{ 'is-active': isZen }"
    :title="isZen ? 'Thoát Zen Mode tập trung (Phím F hoặc Esc)' : 'Bật Zen Mode tập trung đọc (Phím F)'"
    :aria-pressed="isZen"
    :aria-label="isZen ? 'Thoát chế độ tập trung' : 'Bật chế độ tập trung'"
    @click="toggleZen"
  >
    <svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5" /></svg>
  </button>
</template>

<style scoped>
.zen-toggle-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  min-width: 44px;
  padding: 0 var(--space-3, 12px);
  border-radius: var(--radius-sm, 4px);
  font-family: var(--font-ui);
  font-size: var(--fs-small, 14px);
  font-weight: 500;
  color: var(--ink-2);
  background: transparent;
  border: 1px solid transparent;
  cursor: pointer;
  transition: all var(--motion-fast, 120ms) var(--ease);
  white-space: nowrap;
  box-sizing: border-box;
}
.zen-toggle-btn:hover {
  background: var(--sunken);
  color: var(--tim);
  border-color: var(--control);
}
.zen-toggle-btn:focus-visible {
  outline: 2px solid var(--tim);
  outline-offset: 2px;
}
.zen-toggle-btn.is-active {
  color: var(--tim);
  border-color: var(--tim);
  background: var(--tim-soft);
  font-weight: 600;
}
@media (max-width: 767px) {
  .zen-toggle-btn {
    display: none;
  }
}
</style>
