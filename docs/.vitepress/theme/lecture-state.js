import { ref, computed } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../course-catalog.mjs'
import { findLecture } from '../lecture-model.mjs'
export { lectureParts } from '../lecture-model.mjs'
import { lectureParts } from '../lecture-model.mjs'

export const lecturePart = ref('notes')
export function syncLecturePart() {
  const hash = window.location.hash.slice(1)
  lecturePart.value = lectureParts.some(part => part.id === hash) ? hash : 'notes'
}
export function useLecture() {
  const { frontmatter } = useData()
  const course = computed(() => findCourse(frontmatter.value.course))
  const lesson = computed(() => findLecture(frontmatter.value.course, frontmatter.value.lecture))
  return { frontmatter, course, lesson, part: lecturePart }
}
