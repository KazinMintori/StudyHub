import { PHYSICS_COURSE_IDS } from '../../../config/navigation.mjs'

/**
 * Checks whether a relative page path belongs to any course in the catalog.
 *
 * @param {string|null|undefined} relativePath
 * @param {Array<{id: string}>} [courseCatalog]
 * @returns {boolean}
 */
export function isCoursePath(relativePath, courseCatalog = []) {
  if (!relativePath || !Array.isArray(courseCatalog)) return false
  return courseCatalog.some(course => course?.id && relativePath.startsWith(`${course.id}/`))
}

/**
 * Determines if the course sidebar toggle should be active.
 *
 * @param {boolean} hasSidebar - VitePress default theme hasSidebar value
 * @param {string|null|undefined} relativePath - page relative path
 * @param {Array<{id: string}>} [courseCatalog] - catalog courses
 * @returns {boolean}
 */
export function resolveHasCourseSidebar(hasSidebar, relativePath, courseCatalog = []) {
  return Boolean(hasSidebar && isCoursePath(relativePath, courseCatalog))
}

/**
 * Resolves the class dictionary for the top-level Layout component.
 *
 * @param {object} [params]
 * @param {object} [params.frontmatter]
 * @param {boolean} [params.hasCourseSidebar]
 * @param {boolean} [params.desktopSidebarCollapsed]
 * @param {string} [params.lecturePart]
 * @param {string[]} [params.physicsCourses]
 * @returns {Record<string, boolean>}
 */
export function resolveLayoutClasses({
  frontmatter = {},
  hasCourseSidebar = false,
  desktopSidebarCollapsed = false,
  lecturePart = 'notes',
  physicsCourses = PHYSICS_COURSE_IDS
} = {}) {
  const section = frontmatter?.section
  const readingStyle = frontmatter?.readingStyle
  const course = frontmatter?.course
  const hasChapterExercises = Boolean(frontmatter?.hasChapterExercises)

  return {
    'sidebar-collapsed': Boolean(hasCourseSidebar && desktopSidebarCollapsed),
    'lecture-layout': section === 'lecture' || section === 'topic',
    'topic-layout': section === 'topic',
    'physics-layout': Boolean(course && physicsCourses.includes(course)),
    'lecture-reading-plain': section === 'lecture' && readingStyle === 'plain',
    'lecture-slides-layout': section === 'lecture' && lecturePart === 'slides',
    'lecture-alt': section === 'lecture' && lecturePart !== 'notes',
    'has-chapter-exercises': hasChapterExercises,
    'lecture-exercises-layout': Boolean(hasChapterExercises && lecturePart === 'bai-tap')
  }
}

/**
 * Evaluates responsive breakpoint conditions to decide drawer and hamburger actions.
 *
 * @param {object} [params]
 * @param {boolean} [params.sidebarMatches] - min-width: 960px matches
 * @param {boolean} [params.navigationMatches] - min-width: 1200px matches
 * @param {boolean} [params.isSidebarOpen] - .VPSidebar.open is present
 * @param {boolean} [params.desktopSidebarCollapsed] - whether desktop sidebar is collapsed
 * @param {boolean} [params.isSidebarActiveElement] - activeElement is inside .VPSidebar
 * @returns {{ shouldCloseDrawer: boolean, shouldRestoreFocus: boolean, shouldCloseNavHamburger: boolean }}
 */
export function evaluateResponsiveSidebar({
  sidebarMatches = false,
  navigationMatches = false,
  isSidebarOpen = false,
  desktopSidebarCollapsed = false,
  isSidebarActiveElement = false
} = {}) {
  const shouldCloseDrawer = Boolean(sidebarMatches && isSidebarOpen)
  const shouldRestoreFocus = Boolean(shouldCloseDrawer && desktopSidebarCollapsed && isSidebarActiveElement)
  const shouldCloseNavHamburger = Boolean(navigationMatches)

  return {
    shouldCloseDrawer,
    shouldRestoreFocus,
    shouldCloseNavHamburger
  }
}
