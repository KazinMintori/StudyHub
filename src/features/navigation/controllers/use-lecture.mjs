import { computed } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../../../content/catalog.mjs'
import { findLecture } from '../../lecture/services/lecture-model.mjs'
import { lecturePart } from './use-lecture-navigation.mjs'

/**
 * Composable returning current course, lesson, frontmatter, and lecture tab.
 */
export function useLecture() {
  const { frontmatter } = useData()
  const course = computed(() => findCourse(frontmatter.value?.course))
  const lesson = computed(() => findLecture(frontmatter.value?.course, frontmatter.value?.lecture))
  return { frontmatter, course, lesson, part: lecturePart }
}
