import { canonicalLesson } from './progress-migration.js'
import { lecturePath } from '../../lecture/services/lecture-model.mjs'

export function calculateProgressKey(course, lesson, canonicalLessonFn = canonicalLesson) {
  if (!course?.id || !lesson?.slug) return ''
  return canonicalLessonFn(`${lecturePath(course.id, lesson.slug)}.html`)
}

export const progressKey = calculateProgressKey
