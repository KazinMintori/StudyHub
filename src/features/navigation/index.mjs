// Config
export {
  NAVIGATION_BREAKPOINTS,
  LECTURE_PART_IDS,
  LECTURE_PART_HASHES,
  DEFAULT_LECTURE_PART,
  EXERCISE_LECTURE_PART,
  PHYSICS_COURSE_IDS,
  NAVIGATION_SELECTORS
} from '../../config/navigation.mjs'

// Services
export {
  normalizeHash,
  isValidLecturePartId,
  classifyLectureHash,
  isSamePageLectureLink,
  shouldIgnoreNavigationClick
} from './services/tab-service.mjs'

export {
  isCoursePath,
  resolveHasCourseSidebar,
  resolveLayoutClasses,
  evaluateResponsiveSidebar
} from './services/sidebar-service.mjs'

export {
  findAnchorElement,
  isExerciseElement,
  openSearch
} from './adapters/vitepress-dom.mjs'

// Controllers
export {
  useResponsiveSidebar
} from './controllers/use-responsive-sidebar.mjs'

export {
  lecturePart,
  syncLecturePart,
  syncLink,
  useLectureNavigation
} from './controllers/use-lecture-navigation.mjs'

export {
  useLecture
} from './controllers/use-lecture.mjs'
