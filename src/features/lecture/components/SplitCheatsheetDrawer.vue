<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useLecture } from '../../navigation/index.mjs'
import { loadLecturePayload } from '../services/lecture-payload.mjs'
import { lecturePath } from '../services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'
import MathText from '../../../core/math/components/MathText.vue'

const { course, lesson } = useLecture()
const isOpen = ref(false)
const payload = ref(null)
const loading = ref(false)

const cheatsheet = computed(() => payload.value?.cheatsheet)
const fullCheatsheetLink = computed(() => {
  if (!course.value?.id || !lesson.value?.slug) return ''
  return studyLink(lecturePath(course.value.id, lesson.value.slug, 'cheatsheet'))
})

async function fetchCheatsheet() {
  if (!course.value || !lesson.value) return
  loading.value = true
  try {
    const data = await loadLecturePayload(course.value, lesson.value)
    payload.value = data
  } catch {
    payload.value = null
  } finally {
    loading.value = false
  }
}

function toggleDrawer() {
  isOpen.value = !isOpen.value
  if (isOpen.value && !payload.value) {
    fetchCheatsheet()
  }
}

function closeDrawer() {
  isOpen.value = false
}

function handleKeydown(e) {
  if (typeof window === 'undefined') return
  const target = e.target
  if (['INPUT', 'TEXTAREA', 'SELECT'].includes(target?.tagName) || target?.isContentEditable) return

  if (e.altKey && (e.key === 'c' || e.key === 'C')) {
    e.preventDefault()
    toggleDrawer()
  } else if (e.key === 'Escape' && isOpen.value) {
    e.preventDefault()
    closeDrawer()
  }
}

watch([course, lesson], () => {
  payload.value = null
  if (isOpen.value) {
    fetchCheatsheet()
  }
})

onMounted(() => {
  if (typeof window !== 'undefined') {
    window.addEventListener('keydown', handleKeydown)
  }
})

onUnmounted(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('keydown', handleKeydown)
  }
})
</script>

<template>
  <div v-if="course && lesson && course.id !== 'triet-hoc-mac-lenin'" class="split-cheatsheet-container">
    <button
      type="button"
      class="split-cheatsheet-trigger"
      :class="{ 'is-open': isOpen }"
      title="Tra cứu nhanh công thức song song (Phím tắt: Alt + C)"
      :aria-label="isOpen ? 'Đóng Cheatsheet song song' : 'Mở Cheatsheet song song'"
      :aria-expanded="isOpen"
      @click="toggleDrawer"
    >
      <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
      </svg>
      <span>Tra cứu song song</span>
      <kbd class="shortcut-key">Alt+C</kbd>
    </button>

    <Teleport to="body">
      <div v-if="isOpen" class="split-drawer-backdrop" @click="closeDrawer" />
      <aside
        v-if="isOpen"
        class="split-cheatsheet-drawer"
        role="complementary"
        aria-label="Tra cứu Cheatsheet song song"
      >
        <header class="drawer-header">
          <div class="drawer-title-group">
            <span class="drawer-kicker">CẨM NANG ÔN TẬP</span>
            <h3 class="drawer-title">Cheatsheet: {{ lesson.title }}</h3>
          </div>
          <div class="drawer-actions">
            <a
              v-if="fullCheatsheetLink"
              :href="fullCheatsheetLink"
              class="drawer-link-btn"
              title="Mở toàn màn hình tab Cheatsheet"
              @click="closeDrawer"
            >
              Mở tab ↗
            </a>
            <button
              type="button"
              class="drawer-close-btn"
              aria-label="Đóng ngăn kéo"
              @click="closeDrawer"
            >
              ✕
            </button>
          </div>
        </header>

        <div class="drawer-body">
          <div v-if="loading" class="drawer-loading">
            <span>Đang tải công thức bài học…</span>
          </div>

          <div v-else-if="cheatsheet && cheatsheet.sections && cheatsheet.sections.length" class="drawer-content">
            <p v-if="cheatsheet.summary" class="drawer-summary">
              <MathText :text="cheatsheet.summary" />
            </p>

            <article
              v-for="section in cheatsheet.sections"
              :key="section.id"
              class="drawer-section-card"
            >
              <h4 class="drawer-section-title">{{ section.title }}</h4>
              <div v-if="section.items && section.items.length" class="drawer-items">
                <div v-for="(item, idx) in section.items" :key="idx" class="drawer-item">
                  <strong v-if="item.name" class="item-heading">{{ item.name }}</strong>

                  <div v-if="item.formulaRows?.length" class="formula-group">
                    <div v-for="(row, rIdx) in item.formulaRows" :key="rIdx" class="formula-line">
                      <span v-if="row.label" class="formula-label"><MathText :text="row.label" /></span>
                      <MathText as="div" class="formula-math" :text="row.formula" />
                    </div>
                  </div>
                  <div v-else-if="item.formula" class="formula-single">
                    <MathText as="div" :text="item.formula" />
                  </div>

                  <p v-if="item.note" class="item-note">
                    <MathText :text="item.note" />
                  </p>
                </div>
              </div>
            </article>
          </div>

          <div v-else class="drawer-empty">
            <p>Bài học này chưa có dữ liệu Cheatsheet tóm tắt riêng.</p>
          </div>
        </div>
      </aside>
    </Teleport>
  </div>
</template>

<style scoped>
.split-cheatsheet-container {
  display: inline-flex;
  align-items: center;
}

.split-cheatsheet-trigger {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: 999px;
  background: var(--canvas);
  border: 1px solid var(--rule);
  color: var(--ink-2);
  font-family: var(--font-ui);
  font-size: var(--fs-small, 13px);
  font-weight: 500;
  cursor: pointer;
  transition: all var(--motion-fast) var(--ease);
}
.split-cheatsheet-trigger:hover,
.split-cheatsheet-trigger.is-open {
  background: var(--tim-soft, rgba(99, 102, 241, 0.12));
  color: var(--tim);
  border-color: var(--control);
}
.shortcut-key {
  font-size: 11px;
  padding: 1px 5px;
  border-radius: 4px;
  background: var(--sunken);
  color: var(--ink-3);
  font-family: var(--font-code);
}

.split-drawer-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(2px);
  z-index: 1000;
}

.split-cheatsheet-drawer {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: min(480px, 94vw);
  background: var(--paper);
  border-left: 1px solid var(--rule);
  box-shadow: -8px 0 32px rgba(0, 0, 0, 0.3);
  z-index: 1001;
  display: flex;
  flex-direction: column;
  animation: slide-in 0.25s cubic-bezier(0.16, 1, 0.3, 1) both;
}

@keyframes slide-in {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}

.drawer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-5);
  border-bottom: 1px solid var(--rule);
  background: var(--canvas);
}
.drawer-kicker {
  display: block;
  font-size: var(--fs-meta, 11px);
  font-weight: 700;
  letter-spacing: 0.05em;
  color: var(--tim);
}
.drawer-title {
  margin: 2px 0 0;
  font-size: var(--fs-ui, 15px);
  font-weight: 600;
  color: var(--ink);
  line-height: 1.3;
}
.drawer-actions {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}
.drawer-link-btn {
  font-size: var(--fs-meta, 12px);
  color: var(--tim);
  text-decoration: none;
  padding: 4px 8px;
  border-radius: var(--radius-sm);
  background: var(--paper);
  border: 1px solid var(--rule);
}
.drawer-link-btn:hover {
  background: var(--sunken);
}
.drawer-close-btn {
  background: transparent;
  border: none;
  font-size: 16px;
  color: var(--ink-3);
  cursor: pointer;
  padding: 4px 8px;
  border-radius: var(--radius-sm);
}
.drawer-close-btn:hover {
  background: var(--sunken);
  color: var(--ink);
}

.drawer-body {
  flex: 1;
  overflow-y: auto;
  padding: var(--space-4) var(--space-5);
}
.drawer-loading,
.drawer-empty {
  padding: var(--space-6) 0;
  text-align: center;
  color: var(--ink-3);
  font-size: var(--fs-ui);
}
.drawer-summary {
  font-size: var(--fs-small);
  line-height: 1.6;
  color: var(--ink-2);
  margin-bottom: var(--space-4);
  padding: var(--space-3);
  border-radius: var(--radius-sm);
  background: var(--canvas);
  border-left: 3px solid var(--tim);
}
.drawer-section-card {
  margin-bottom: var(--space-4);
  padding: var(--space-4);
  border-radius: var(--radius-md);
  background: var(--canvas);
  border: 1px solid var(--rule);
}
.drawer-section-title {
  margin: 0 0 var(--space-3);
  font-size: var(--fs-ui, 14px);
  font-weight: 600;
  color: var(--ink);
}
.drawer-items {
  display: grid;
  gap: var(--space-3);
}
.drawer-item {
  padding-bottom: var(--space-3);
  border-bottom: 1px dashed var(--rule);
}
.drawer-item:last-child {
  padding-bottom: 0;
  border-bottom: none;
}
.item-heading {
  display: block;
  font-size: var(--fs-small, 13px);
  color: var(--ink-2);
  margin-bottom: var(--space-2);
}
.formula-line {
  margin: var(--space-2) 0;
}
.formula-label {
  font-size: var(--fs-meta, 12px);
  color: var(--ink-3);
  margin: 0 0 2px;
}
.item-note {
  font-size: var(--fs-meta, 12px);
  color: var(--ink-3);
  margin: var(--space-2) 0 0;
}
</style>
