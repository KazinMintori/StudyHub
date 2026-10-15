import { ref, computed } from 'vue'
import { courseCatalog as defaultCatalog } from '../../../content/catalog.mjs'
import { useStudyProgress } from './useStudyProgress.js'
import { filterCourses } from '../services/course-filter.js'
import {
  resolveResumeLesson,
  resolveResumeLink,
  resolveDefaultReadyLesson
} from '../services/resume-service.js'
import { getLessonChapter, getLessonDetailTitle } from '../services/lesson-labels.js'

export function useStudyHome(options = {}) {
  const catalog = options.catalog || defaultCatalog
  const query = ref('')
  const progressState = options.useStudyProgress ? options.useStudyProgress() : useStudyProgress()
  const lastLesson = options.lastLesson || progressState.lastLesson

  const visibleCourses = computed(() => filterCourses(catalog, query.value))

  const resume = computed(() => resolveResumeLesson(lastLesson.value, catalog))
  const resumeLink = computed(() => resolveResumeLink(resume.value))

  const defaultStarter = computed(() => resolveDefaultReadyLesson(catalog))

  const activeResume = computed(() => resume.value || defaultStarter.value)
  const activeResumeLink = computed(() => {
    if (resume.value) return resumeLink.value
    if (defaultStarter.value) return defaultStarter.value.path
    return ''
  })

  return {
    query,
    visibleCourses,
    catalog,
    lastLesson,
    resume,
    resumeLink,
    defaultStarter,
    activeResume,
    activeResumeLink,
    getLessonChapter,
    getLessonDetailTitle
  }
}
