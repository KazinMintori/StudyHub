import { findCourse } from '../course-catalog.mjs'
import { readStored, writeStored } from './storage'
export function canonicalLesson(path) {
  if (typeof path !== 'string') return path
  const parts = path.replace(/\.html$/, '').split('/').filter(Boolean)
  const course = findCourse(parts[0])
  if (course && parts.length === 2 && course.lessons.some(lesson => lesson.slug === parts[1])) return `/${course.id}/bai-giang/${parts[1]}.html`
  if (course && ['notes','bai-giang'].includes(parts[1]) && parts.length===3 && course.lessons.some(lesson=>lesson.slug===parts[2])) return `/${course.id}/bai-giang/${parts[2]}.html`
  return path
}
export function migrateProgress() {
  const existing = readStored('studyhub_completed', {}) || {}, completed = {}
  for (const [path, done] of Object.entries(existing)) completed[canonicalLesson(path)] = completed[canonicalLesson(path)] || !!done
  writeStored('studyhub_completed', completed)
  const last = readStored('studyhub_last_lesson', null)
  if (last?.path) writeStored('studyhub_last_lesson', { ...last, path: canonicalLesson(last.path) })
}
