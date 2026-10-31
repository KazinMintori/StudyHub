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
  const lessonIndex = computed(() => course.value?.lessons?.findIndex(item => item.slug === lesson.value?.slug) ?? -1)
  const previousLesson = computed(() => lessonIndex.value > 0 ? course.value.lessons[lessonIndex.value - 1] : undefined)
  const nextLesson = computed(() => {
    return lessonIndex.value >= 0 ? course.value.lessons[lessonIndex.value + 1] : undefined
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
    previousLesson,
    nextLesson,
    storageMessage
  }
}
