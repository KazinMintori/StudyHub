import { canonicalLesson } from './progress-migration.js'

export function calculateProgressKey(course, lesson, canonicalLessonFn = canonicalLesson) {
  if (!course?.id || !lesson?.slug) return ''
  return canonicalLessonFn(`/${course.id}/bai-giang/${lesson.slug}.html`)
}

export const progressKey = calculateProgressKey
