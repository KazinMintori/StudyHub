// Single source of truth for course collection metadata and isolation.
export const DEFAULT_COLLECTION = 'uet'
export const COLLECTION_UET = 'uet'
export const COLLECTION_EXTENDED = 'extended'

export const COLLECTIONS = {
  [COLLECTION_UET]: {
    id: COLLECTION_UET,
    name: 'Học phần UET',
    shortName: 'UET',
    description: 'Chương trình bài giảng ôn tập chuẩn Đại học Công nghệ (UET) - ĐHQGHN',
    path: '/'
  },
  [COLLECTION_EXTENDED]: {
    id: COLLECTION_EXTENDED,
    name: 'Học liệu mở rộng',
    shortName: 'Mở rộng',
    description: 'Sách và học phần ngoài chương trình UET',
    path: '/hoc-lieu-mo-rong/'
  }
}

/**
 * Returns the collection ID of a course, defaulting older courses to 'uet'.
 * Uses course metadata as the sole decision source without hardcoding course IDs.
 */
export function getCourseCollection(course) {
  if (!course || typeof course !== 'object') return DEFAULT_COLLECTION
  return course.collection || DEFAULT_COLLECTION
}

export function isUetCourse(course) {
  return getCourseCollection(course) === COLLECTION_UET
}

export function isExtendedCourse(course) {
  return getCourseCollection(course) === COLLECTION_EXTENDED
}

export function filterCoursesByCollection(catalog, collection = DEFAULT_COLLECTION) {
  if (!Array.isArray(catalog)) return []
  return catalog.filter(course => getCourseCollection(course) === collection)
}

export function getUetCourses(catalog) {
  return filterCoursesByCollection(catalog, COLLECTION_UET)
}

export function getExtendedCourses(catalog) {
  return filterCoursesByCollection(catalog, COLLECTION_EXTENDED)
}

export function getCourseSource(course) {
  return course?.source || null
}

export function getCollectionMeta(course) {
  const colId = getCourseCollection(course)
  const meta = COLLECTIONS[colId] || COLLECTIONS[DEFAULT_COLLECTION]
  return {
    ...meta,
    isUet: colId === COLLECTION_UET,
    isExtended: colId === COLLECTION_EXTENDED,
    source: getCourseSource(course)
  }
}

export function resolveCollectionBreadcrumbs(course) {
  const isExt = isExtendedCourse(course)
  if (isExt) {
    return [
      { label: 'Trang chủ', link: '/' },
      { label: 'Học liệu mở rộng', link: '/hoc-lieu-mo-rong/' }
    ]
  }
  return [
    { label: 'Trang chủ', link: '/' },
    { label: 'Học phần', link: '/#hoc-phan' }
  ]
}
