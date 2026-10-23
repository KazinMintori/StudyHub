<script setup>
import { ref, computed, onMounted, watch, nextTick } from 'vue'
import { useRoute } from 'vitepress'
import { useLessonActions } from '../controllers/useLessonActions.js'
import { lecturePath } from '../../lecture/services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'
import { calculateProgressKey } from '../services/progress-key.js'
import { readStored, writeStored } from '../../../core/storage/local-storage.js'

const route = useRoute()
const {
  course,
  lesson,
  nextLesson,
  part,
  readable,
  storageMessage
} = useLessonActions()

const isCompleted = ref(false)

const currentKey = computed(() => {
  if (!course.value || !lesson.value) return ''
  return calculateProgressKey(course.value, lesson.value)
})

function checkCompletion() {
  if (typeof window === 'undefined' || !currentKey.value) return
  const completed = readStored('studyhub_completed', {}) || {}
  isCompleted.value = Boolean(completed[currentKey.value])
}

function syncSidebarCheckmarks() {
  if (typeof document === 'undefined') return
  const completed = readStored('studyhub_completed', {}) || {}
  const completedKeys = new Set(Object.keys(completed).filter(k => completed[k]))

  const sidebarLinks = document.querySelectorAll('.VPSidebar a.link')
  sidebarLinks.forEach((link) => {
    const href = link.getAttribute('href')
    if (!href) return
    const norm = href.replace(/\.html$/, '').replace(/\/$/, '')
    const isMatch = Array.from(completedKeys).some(k => {
      const kNorm = k.replace(/\.html$/, '').replace(/\/$/, '')
      return kNorm.endsWith(norm) || norm.endsWith(kNorm)
    })
    link.classList.toggle('is-lecture-completed', isMatch)
  })
}

function toggleComplete() {
  if (!currentKey.value) return
  const completed = readStored('studyhub_completed', {}) || {}
  const nextVal = !completed[currentKey.value]
  completed[currentKey.value] = nextVal
  writeStored('studyhub_completed', completed)
  isCompleted.value = nextVal
  nextTick(syncSidebarCheckmarks)
}

watch(currentKey, () => {
  checkCompletion()
  nextTick(syncSidebarCheckmarks)
})

onMounted(() => {
  checkCompletion()
  nextTick(syncSidebarCheckmarks)
})
</script>

<template>
  <section v-if="readable" v-show="part === 'notes'" class="lesson-actions">
    <div class="lesson-checkpoint-row">
      <button
        type="button"
        class="study-button checkpoint-toggle-btn"
        :class="{ 'is-completed': isCompleted }"
        :title="isCompleted ? 'Bỏ đánh dấu hoàn thành' : 'Đánh dấu đã hiểu và nắm vững bài học này'"
        @click="toggleComplete"
      >
        <span class="checkpoint-icon" aria-hidden="true">{{ isCompleted ? '✓' : '○' }}</span>
        <span>{{ isCompleted ? 'Đã nắm vững bài này' : 'Đánh dấu đã học xong' }}</span>
      </button>

      <nav v-if="nextLesson" aria-label="Sau bài học" class="next-lesson-nav">
        <a class="text-link next-lesson-link" :href="studyLink(lecturePath(course.id, nextLesson.slug))">
          <span>Tiếp: {{ nextLesson.title }}</span>
          <span aria-hidden="true">→</span>
        </a>
      </nav>
    </div>
    <p v-if="storageMessage" role="status" class="storage-notice">{{ storageMessage }}</p>
  </section>
</template>
