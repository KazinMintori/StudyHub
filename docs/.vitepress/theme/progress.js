import { ref, onMounted, onUnmounted } from 'vue'
import { readStored, writeStored } from './storage'
import { canonicalLesson, migrateProgress } from './progress-migration'
export const completed = ref({}), lastLesson = ref(null)
export const progressKey = (course, lesson) => canonicalLesson(`/${course.id}/bai-giang/${lesson.slug}.html`)
export const isCompleted = (course, lesson) => !!completed.value[progressKey(course, lesson)]
export const courseCompleted = course => course.lessons.filter(lesson => isCompleted(course, lesson)).length
export function toggleCompleted(course, lesson) {
  const path = progressKey(course, lesson)
  const next = { ...(readStored('studyhub_completed', {}) || {}), [path]: !isCompleted(course, lesson) }
  if (writeStored('studyhub_completed', next)) completed.value = next
}
export function useStudyProgress() {
  function load() { completed.value = readStored('studyhub_completed', {}) || {}; lastLesson.value = readStored('studyhub_last_lesson', null) }
  onMounted(() => { migrateProgress(); load(); window.addEventListener('storage', load) })
  onUnmounted(() => window.removeEventListener('storage', load))
  return { completed, lastLesson }
}
