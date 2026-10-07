import { ref, onMounted, onUnmounted } from 'vue'
import { readStored } from './storage'
import { canonicalLesson } from './progress-migration'

export const lastLesson = ref(null)
export const progressKey = (course, lesson) => canonicalLesson(`/${course.id}/bai-giang/${lesson.slug}.html`)

export function useStudyProgress() {
  function load() {
    lastLesson.value = readStored('studyhub_last_lesson', null)
  }
  onMounted(() => {
    load()
    window.addEventListener('storage', load)
  })
  onUnmounted(() => window.removeEventListener('storage', load))
  return { lastLesson }
}
