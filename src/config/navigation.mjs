/**
 * Navigation configuration constants for StudyHub.
 */

export const NAVIGATION_BREAKPOINTS = {
  sidebar: '(min-width: 960px)',
  navigation: '(min-width: 1200px)'
}

export const LECTURE_PART_IDS = [
  'kien-thuc-can-co',
  'notes',
  'bai-tap',
  'cheatsheet'
]

export const LECTURE_PART_HASHES = [
  '#notes',
  '#cheatsheet',
  '#kien-thuc-can-co',
  '#bai-tap'
]

export const DEFAULT_LECTURE_PART = 'notes'
export const EXERCISE_LECTURE_PART = 'bai-tap'

export const PHYSICS_COURSE_IDS = ['vat-ly-1', 'vat-ly-2']

export const NAVIGATION_SELECTORS = {
  sidebarOpen: '.VPSidebar.open',
  sidebar: '.VPSidebar',
  backdrop: '.Layout > .VPBackdrop.backdrop',
  sidebarToggle: '.course-sidebar-toggle',
  navBarHamburgerExpanded: '.VPNavBarHamburger[aria-expanded="true"]',
  docSearchButton: '.site-search-button, .DocSearch-Button',
  exerciseContent: '.lecture-exercises-content'
}
