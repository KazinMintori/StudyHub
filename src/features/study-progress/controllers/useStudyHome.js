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

export const COURSE_CATEGORIES = [
  { id: 'all', label: 'Tất cả' },
  { id: 'toan', label: 'Toán & Cơ sở ngành' },
  { id: 'ai-cs', label: 'AI & Khoa học máy tính' },
  { id: 'vat-ly', label: 'Vật lý & Kỹ thuật' },
  { id: 'dai-cuong', label: 'Đại cương & Triết' }
]

export const COURSE_CATEGORY_MAP = {
  'toan-cho-ai': 'toan',
  'xac-suat-thong-ke': 'toan',
  'discrete-math': 'toan',
  'bieu-dien-tri-thuc': 'ai-cs',
  'xu-ly-du-lieu': 'ai-cs',
  'giai-thuat-du-lieu': 'ai-cs',
  'dsa': 'ai-cs',
  'vat-ly-1': 'vat-ly',
  'vat-ly-2': 'vat-ly',
  'triet-hoc-mac-lenin': 'dai-cuong'
}

export function getCourseCategoryLabel(courseId) {
  const catId = COURSE_CATEGORY_MAP[courseId]
  const cat = COURSE_CATEGORIES.find(c => c.id === catId)
  return cat ? cat.label : 'Học phần'
}

export function getCourseQuickLinks(course) {
  if (!course?.id) return {}
  const firstReady = course.lessons?.find(l => l.status === 'ready') || course.lessons?.[0]
  if (!firstReady) return { overview: `/${course.id}/` }

  if (course.presentation === 'philosophy') {
    return {
      overview: `/${course.id}/`,
      notes: `/${course.id}/${firstReady.slug}/`,
      exercises: `/${course.id}/${firstReady.slug}/#bai-tap`
    }
  }

  const baseSlug = firstReady.slug === 'on-luyen' ? 'on-luyen/tong-hop' : `bai-giang/${firstReady.slug}`
  const baseLink = `/${course.id}/${baseSlug}`

  return {
    overview: `/${course.id}/`,
    notes: baseLink,
    slides: `${baseLink}#slides`,
    cheatsheet: `${baseLink}#cheatsheet`,
    exercises: `${baseLink}#bai-tap`
  }
}

export function useStudyHome(options = {}) {
  const catalog = options.catalog || defaultCatalog
  const query = ref('')
  const selectedCategory = ref('all')
  const lastLesson = options.lastLesson !== undefined
    ? options.lastLesson
    : (options.useStudyProgress ? options.useStudyProgress() : useStudyProgress()).lastLesson

  const visibleCourses = computed(() => {
    let list = catalog
    if (selectedCategory.value !== 'all') {
      list = list.filter(c => COURSE_CATEGORY_MAP[c.id] === selectedCategory.value)
    }
    return filterCourses(list, query.value)
  })

  const getCategoryCount = catId => {
    if (catId === 'all') return catalog.length
    return catalog.filter(c => COURSE_CATEGORY_MAP[c.id] === catId).length
  }

  const resume = computed(() => resolveResumeLesson(lastLesson.value, catalog))
  const resumeLink = computed(() => resolveResumeLink(resume.value))

  const defaultStarter = computed(() => resolveDefaultReadyLesson(catalog))

  const activeResume = computed(() => resume.value || defaultStarter.value)
  const activeResumeLink = computed(() => {
    if (resume.value) return resumeLink.value
    if (defaultStarter.value) return defaultStarter.value.path
    return ''
  })

  const activeResumeCheatsheetLink = computed(() => {
    const target = resume.value || defaultStarter.value
    if (!target?.course?.id || !target?.lesson?.slug) return ''
    if (target.course.id === 'triet-hoc-mac-lenin') return ''
    const baseSlug = target.lesson.slug
    return `/${target.course.id}/${baseSlug === 'on-luyen' ? 'on-luyen/tong-hop' : `bai-giang/${baseSlug}`}#cheatsheet`
  })

  return {
    query,
    selectedCategory,
    courseCategories: COURSE_CATEGORIES,
    visibleCourses,
    catalog,
    lastLesson,
    resume,
    resumeLink,
    defaultStarter,
    activeResume,
    activeResumeLink,
    activeResumeCheatsheetLink,
    getCategoryCount,
    getCourseCategoryLabel,
    getCourseQuickLinks,
    getLessonChapter,
    getLessonDetailTitle
  }
}
