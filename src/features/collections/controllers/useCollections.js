import { ref, computed } from 'vue'
import { courseCatalog as defaultCatalog } from '../../../content/catalog.mjs'
import { getExtendedCourses } from '../../../content/collections.mjs'
import { normalizeVietnamese } from '../../study-progress/services/course-filter.js'

export const MATERIAL_TYPES = [
  { id: 'all', label: 'Tất cả' },
  { id: 'book', label: 'Giáo trình' },
  { id: 'monograph', label: 'Chuyên khảo' },
  { id: 'university-course', label: 'Học phần ngoài UET' }
]

export const MATERIAL_KIND_LABELS = {
  book: 'Giáo trình',
  monograph: 'Chuyên khảo',
  'university-course': 'Học phần ngoài UET'
}

export function getMaterialKindLabel(kind) {
  return MATERIAL_KIND_LABELS[kind] || 'Tài liệu'
}

export function getSourceHostname(url) {
  if (!url) return ''
  try {
    return new URL(url).hostname.replace(/^www\./, '')
  } catch {
    return String(url)
  }
}

export function normalizeSearch(str) {
  if (!str) return ''
  return normalizeVietnamese(String(str)).trim()
}

export function getStartAction(course) {
  if (!course) return { link: '/', label: 'Trang chủ', isReady: false }
  const readyLesson = (course.lessons || []).find(l => l.status === 'ready')
  if (readyLesson) {
    return {
      link: `/${course.id}/bai-giang/${readyLesson.slug}`,
      label: 'Bắt đầu đọc',
      isReady: true
    }
  }
  return {
    link: `/${course.id}/`,
    label: 'Xem mục lục & tài liệu',
    isReady: false
  }
}

export function getAvailableChapterCount(course) {
  return (course?.lessons || []).filter(lesson => lesson.status === 'ready').length
}

export function useCollections(options = {}) {
  const catalog = options.catalog || defaultCatalog
  const extendedCourses = getExtendedCourses(catalog)

  const query = ref('')
  const selectedType = ref('all')

  const filteredCourses = computed(() => {
    let list = extendedCourses

    if (selectedType.value !== 'all') {
      list = list.filter(course => {
        const kind = course.source?.kind || 'book'
        return kind === selectedType.value
      })
    }

    const q = normalizeSearch(query.value)
    if (!q) return list

    return list.filter(course => {
      const matchName = normalizeSearch(course.name).includes(q)
      const matchDesc = normalizeSearch(course.description).includes(q)
      const matchSourceTitle = normalizeSearch(course.source?.title).includes(q)
      const authorsStr = Array.isArray(course.source?.authors)
        ? course.source.authors.join(' ')
        : (course.source?.authors || '')
      const matchAuthors = normalizeSearch(authorsStr).includes(q)
      const matchPublisher = normalizeSearch(course.source?.publisher).includes(q)
      const matchChapter = (course.lessons || []).some(lesson => normalizeSearch(lesson.title).includes(q))
      return matchName || matchDesc || matchSourceTitle || matchAuthors || matchPublisher || matchChapter
    })
  })

  function resetFilters() {
    query.value = ''
    selectedType.value = 'all'
  }

  return {
    query,
    selectedType,
    materialTypes: MATERIAL_TYPES,
    extendedCourses,
    filteredCourses,
    totalCount: extendedCourses.length,
    filteredCount: computed(() => filteredCourses.value.length),
    resetFilters,
    getStartAction,
    getAvailableChapterCount,
    getSourceHostname,
    getMaterialKindLabel
  }
}
