import { computed, ref, onMounted, onUnmounted, watch } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../../../content/catalog.mjs'
import { lecturePath, topicPath } from '../../lecture/services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'

export function useCourseOverview() {
  const { frontmatter } = useData()
  const course = computed(() => findCourse(frontmatter.value.course))
  const review = computed(() => course.value?.review)
  const view = ref(frontmatter.value.reviewOverview ? 'on-luyen' : 'bai-giang')
  const lessons = computed(() => course.value?.lessons || [])
  const primaryLessonCount = computed(() => lessons.value.filter(lesson => !lesson.supplementary).length)
  const supplementCount = computed(() => lessons.value.filter(lesson => lesson.supplementary).length)
  const groups = computed(() => course.value.parts?.length ? course.value.parts.map(p => ({ ...p, entries: p.lessons.map(slug => lessons.value.find(l => l.slug === slug)).filter(Boolean) })).filter(group => group.entries.length) : [{ title: 'Bài giảng', entries: lessons.value }])
  function syncView() { view.value = review.value && (frontmatter.value.reviewOverview || window.location.hash === '#on-luyen') ? 'on-luyen' : 'bai-giang' }
  onMounted(() => {
    syncView()
    window.addEventListener('hashchange', syncView)
    window.addEventListener('popstate', syncView)
  })
  onUnmounted(() => {
    window.removeEventListener('hashchange', syncView)
    window.removeEventListener('popstate', syncView)
  })
  watch(() => frontmatter.value.course, () => { if (typeof window !== 'undefined') syncView() })

  return { frontmatter, course, review, view, lessons, primaryLessonCount, supplementCount, groups, syncView, studyLink, lecturePath, topicPath }
}
