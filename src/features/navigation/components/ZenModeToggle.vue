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
  const target = e.target
  if (['INPUT', 'TEXTAREA', 'SELECT'].includes(target?.tagName) || target?.isContentEditable) return
  if (e.metaKey || e.ctrlKey || e.altKey) return

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
    @click="toggleZen"
  >
    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7" />
    </svg>
    <span>{{ isZen ? 'Thoát Zen' : 'Zen (F)' }}</span>
  </button>
</template>

<style scoped>
.zen-toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  min-height: 32px;
  padding: 4px 10px;
  border-radius: var(--radius-sm, 6px);
  font-family: var(--font-ui);
  font-size: var(--fs-small, 13px);
  font-weight: 500;
  color: var(--ink-2);
  background: var(--canvas);
  border: 1px solid var(--rule);
  cursor: pointer;
  transition: all var(--motion-fast, 120ms) var(--ease);
  white-space: nowrap;
}
.zen-toggle-btn:hover {
  background: var(--sunken);
  color: var(--tim);
  border-color: var(--control);
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
