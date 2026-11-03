import { computed, ref, onMounted, onUnmounted, watch } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../../../content/catalog.mjs'
import { lecturePath, topicPath } from '../../lecture/services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'

export function useCourseOverview() {
  const { frontmatter, page } = useData()
  const course = computed(() => {
    const courseId = frontmatter.value?.course || (page.value?.relativePath ? page.value.relativePath.split('/')[0] : null)
    return courseId ? findCourse(courseId) : null
  })
  const review = computed(() => course.value?.review)
  const view = ref(frontmatter.value?.reviewOverview ? 'on-luyen' : 'bai-giang')
  const lessons = computed(() => course.value?.lessons || [])
  const primaryLessonCount = computed(() => lessons.value.filter(lesson => !lesson.supplementary).length)
  const supplementCount = computed(() => lessons.value.filter(lesson => lesson.supplementary).length)
  const groups = computed(() => {
    if (!course.value) return [{ title: 'Bài giảng', entries: [] }]
    return course.value.parts?.length
      ? course.value.parts
          .map(p => ({
            ...p,
            entries: (p.lessons || []).map(slug => lessons.value.find(l => l.slug === slug)).filter(Boolean)
          }))
          .filter(group => group.entries.length)
      : [{ title: 'Bài giảng', entries: lessons.value }]
  })
  function syncView() {
    view.value = review.value && (frontmatter.value?.reviewOverview || (typeof window !== 'undefined' && window.location.hash === '#on-luyen')) ? 'on-luyen' : 'bai-giang'
  }
  onMounted(() => {
    syncView()
    window.addEventListener('hashchange', syncView)
    window.addEventListener('popstate', syncView)
  })
  onUnmounted(() => {
    window.removeEventListener('hashchange', syncView)
    window.removeEventListener('popstate', syncView)
  })
  watch(
    () => [frontmatter.value?.course, page.value?.relativePath],
    () => { if (typeof window !== 'undefined') syncView() }
  )

  return { frontmatter, course, review, view, lessons, primaryLessonCount, supplementCount, groups, syncView, studyLink, lecturePath, topicPath }
}
