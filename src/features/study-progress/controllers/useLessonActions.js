import { computed } from 'vue'
import { useRoute } from 'vitepress'
import { useLecture as defaultUseLecture } from '../../navigation/index.mjs'
import { storageMessage } from '../../../core/storage/index.js'
import { useHeadingTracker } from './useHeadingTracker.js'

export function useLessonActions(options = {}) {
  const route = options.route || useRoute()
  const lectureState = options.useLecture ? options.useLecture() : defaultUseLecture()
  const course = options.course || lectureState.course
  const lesson = options.lesson || lectureState.lesson
  const part = options.part || lectureState.part

  const readable = computed(() => lesson.value?.status === 'ready')
  const nextLesson = computed(() => {
    if (!course.value?.lessons || !lesson.value) return undefined
    const idx = course.value.lessons.indexOf(lesson.value)
    return idx >= 0 ? course.value.lessons[idx + 1] : undefined
  })

  useHeadingTracker({
    course,
    lesson,
    part,
    route,
    readable
  })

  return {
    course,
    lesson,
    part,
    readable,
    nextLesson,
    storageMessage
  }
}
