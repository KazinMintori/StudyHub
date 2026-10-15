import { ref, onMounted, onUnmounted } from 'vue'
import { readStored } from '../../../core/storage/index.js'
import { calculateProgressKey } from '../services/progress-key.js'

export const lastLesson = ref(null)
export const progressKey = calculateProgressKey

export function useStudyProgress(options = {}) {
  const storageKey = options.storageKey || 'studyhub_last_lesson'
  const read = options.readStored || readStored

  function load() {
    lastLesson.value = read(storageKey, null)
  }

  onMounted(() => {
    load()
    if (typeof window !== 'undefined') {
      window.addEventListener('storage', load)
    }
  })

  onUnmounted(() => {
    if (typeof window !== 'undefined') {
      window.removeEventListener('storage', load)
    }
  })

  return {
    lastLesson,
    load
  }
}
