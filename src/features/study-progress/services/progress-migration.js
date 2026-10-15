import { findCourse as defaultFindCourse } from '../../../content/catalog.mjs'
import { readStored, writeStored } from '../../../core/storage/local-storage.js'

export function canonicalLesson(path, findCourse = defaultFindCourse) {
  if (typeof path !== 'string') return path
  const parts = path.replace(/\.html$/, '').split('/').filter(Boolean)
  if (!parts.length) return path

  const course = typeof findCourse === 'function' ? findCourse(parts[0]) : null
  if (course && parts.length === 2 && course.lessons?.some(lesson => lesson.slug === parts[1])) {
    return `/${course.id}/bai-giang/${parts[1]}.html`
  }
  if (
    course &&
    ['notes', 'bai-giang'].includes(parts[1]) &&
    parts.length === 3 &&
    course.lessons?.some(lesson => lesson.slug === parts[2])
  ) {
    return `/${course.id}/bai-giang/${parts[2]}.html`
  }
  return path
}

export function migrateCompletedLessons(existingCompleted, canonicalLessonFn = canonicalLesson) {
  const existing = existingCompleted || {}
  const completed = {}
  for (const [path, done] of Object.entries(existing)) {
    const canonicalPath = canonicalLessonFn(path)
    completed[canonicalPath] = completed[canonicalPath] || Boolean(done)
  }
  return completed
}

export function migrateLastLesson(lastLesson, canonicalLessonFn = canonicalLesson) {
  if (!lastLesson?.path) return lastLesson
  return {
    ...lastLesson,
    path: canonicalLessonFn(lastLesson.path)
  }
}

export function migrateProgress(storageAdapter = { read: readStored, write: writeStored }, canonicalLessonFn = canonicalLesson) {
  const read = storageAdapter?.read || readStored
  const write = storageAdapter?.write || writeStored

  const existing = read('studyhub_completed', {}) || {}
  const completed = migrateCompletedLessons(existing, canonicalLessonFn)
  write('studyhub_completed', completed)

  const last = read('studyhub_last_lesson', null)
  if (last?.path) {
    write('studyhub_last_lesson', migrateLastLesson(last, canonicalLessonFn))
  }
}
