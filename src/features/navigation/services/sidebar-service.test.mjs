import { test, describe } from 'node:test'
import assert from 'node:assert/strict'
import {
  isCoursePath,
  resolveHasCourseSidebar,
  resolveLayoutClasses,
  evaluateResponsiveSidebar
} from './sidebar-service.mjs'

const mockCatalog = [
  { id: 'toan-ai', title: 'Toán cho AI' },
  { id: 'vat-ly-1', title: 'Vật lý 1' },
  { id: 'vat-ly-2', title: 'Vật lý 2' },
  { id: 'ctdl-gt', title: 'Cấu trúc dữ liệu' }
]

describe('sidebar-service: isCoursePath', () => {
  test('returns true for paths matching any course prefix', () => {
    assert.equal(isCoursePath('toan-ai/bai-giang/gioi-thieu.md', mockCatalog), true)
    assert.equal(isCoursePath('vat-ly-1/on-luyen/tong-hop.md', mockCatalog), true)
    assert.equal(isCoursePath('ctdl-gt/index.md', mockCatalog), true)
  })

  test('returns false for non-course paths', () => {
    assert.equal(isCoursePath('index.md', mockCatalog), false)
    assert.equal(isCoursePath('wiki/giai-thuat.md', mockCatalog), false)
    assert.equal(isCoursePath('about.md', mockCatalog), false)
  })

  test('handles null, undefined, or empty values safely', () => {
    assert.equal(isCoursePath(null, mockCatalog), false)
    assert.equal(isCoursePath(undefined, mockCatalog), false)
    assert.equal(isCoursePath('', mockCatalog), false)
    assert.equal(isCoursePath('toan-ai/bai-giang/1', null), false)
    assert.equal(isCoursePath('toan-ai/bai-giang/1', []), false)
  })
})

describe('sidebar-service: resolveHasCourseSidebar', () => {
  test('returns true only when both hasSidebar is true and path is in a course', () => {
    assert.equal(
      resolveHasCourseSidebar(true, 'toan-ai/bai-giang/gioi-thieu.md', mockCatalog),
      true
    )
  })

  test('returns false when hasSidebar is false even if path is in a course', () => {
    assert.equal(
      resolveHasCourseSidebar(false, 'toan-ai/bai-giang/gioi-thieu.md', mockCatalog),
      false
    )
  })

  test('returns false when path is not in a course even if hasSidebar is true', () => {
    assert.equal(
      resolveHasCourseSidebar(true, 'index.md', mockCatalog),
      false
    )
  })
})

describe('sidebar-service: resolveLayoutClasses', () => {
  test('resolves standard lecture layout classes with notes tab', () => {
    const classes = resolveLayoutClasses({
      frontmatter: { section: 'lecture', course: 'toan-ai' },
      hasCourseSidebar: true,
      desktopSidebarCollapsed: false,
      lecturePart: 'notes'
    })

    assert.equal(classes['sidebar-collapsed'], false)
    assert.equal(classes['lecture-layout'], true)
    assert.equal(classes['topic-layout'], false)
    assert.equal(classes['physics-layout'], false)
    assert.equal(classes['lecture-reading-plain'], false)
    assert.equal(classes['lecture-slides-layout'], false)
    assert.equal(classes['lecture-alt'], false)
    assert.equal(classes['has-chapter-exercises'], false)
    assert.equal(classes['lecture-exercises-layout'], false)
  })

  test('resolves sidebar-collapsed when desktop sidebar is collapsed', () => {
    const collapsed = resolveLayoutClasses({
      frontmatter: { section: 'lecture' },
      hasCourseSidebar: true,
      desktopSidebarCollapsed: true,
      lecturePart: 'notes'
    })
    assert.equal(collapsed['sidebar-collapsed'], true)

    const noCourseSidebar = resolveLayoutClasses({
      frontmatter: { section: 'lecture' },
      hasCourseSidebar: false,
      desktopSidebarCollapsed: true,
      lecturePart: 'notes'
    })
    assert.equal(noCourseSidebar['sidebar-collapsed'], false)
  })

  test('resolves slides tab classes', () => {
    const classes = resolveLayoutClasses({
      frontmatter: { section: 'lecture' },
      hasCourseSidebar: true,
      desktopSidebarCollapsed: false,
      lecturePart: 'slides'
    })
    assert.equal(classes['lecture-slides-layout'], true)
    assert.equal(classes['lecture-alt'], true)
  })

  test('resolves chapter exercises classes', () => {
    const classes = resolveLayoutClasses({
      frontmatter: { section: 'lecture', hasChapterExercises: true },
      hasCourseSidebar: true,
      desktopSidebarCollapsed: false,
      lecturePart: 'bai-tap'
    })
    assert.equal(classes['has-chapter-exercises'], true)
    assert.equal(classes['lecture-exercises-layout'], true)
    assert.equal(classes['lecture-alt'], true)
  })

  test('resolves physics-layout for vat-ly-1 and vat-ly-2', () => {
    const phy1 = resolveLayoutClasses({
      frontmatter: { section: 'lecture', course: 'vat-ly-1' }
    })
    assert.equal(phy1['physics-layout'], true)

    const phy2 = resolveLayoutClasses({
      frontmatter: { section: 'lecture', course: 'vat-ly-2' }
    })
    assert.equal(phy2['physics-layout'], true)

    const math = resolveLayoutClasses({
      frontmatter: { section: 'lecture', course: 'toan-ai' }
    })
    assert.equal(math['physics-layout'], false)
  })

  test('resolves topic layout classes', () => {
    const classes = resolveLayoutClasses({
      frontmatter: { section: 'topic', course: 'toan-ai' }
    })
    assert.equal(classes['topic-layout'], true)
    assert.equal(classes['lecture-layout'], true)
  })

  test('resolves plain reading style class', () => {
    const classes = resolveLayoutClasses({
      frontmatter: { section: 'lecture', readingStyle: 'plain' }
    })
    assert.equal(classes['lecture-reading-plain'], true)
  })
})

describe('sidebar-service: evaluateResponsiveSidebar', () => {
  test('evaluates drawer closure when sidebar breakpoint matches and drawer is open', () => {
    const res = evaluateResponsiveSidebar({
      sidebarMatches: true,
      navigationMatches: false,
      isSidebarOpen: true,
      desktopSidebarCollapsed: false,
      isSidebarActiveElement: false
    })
    assert.equal(res.shouldCloseDrawer, true)
    assert.equal(res.shouldRestoreFocus, false)
    assert.equal(res.shouldCloseNavHamburger, false)
  })

  test('evaluates focus restoration when collapsed and drawer had focus', () => {
    const res = evaluateResponsiveSidebar({
      sidebarMatches: true,
      navigationMatches: false,
      isSidebarOpen: true,
      desktopSidebarCollapsed: true,
      isSidebarActiveElement: true
    })
    assert.equal(res.shouldCloseDrawer, true)
    assert.equal(res.shouldRestoreFocus, true)
  })

  test('does not close drawer when drawer is already closed', () => {
    const res = evaluateResponsiveSidebar({
      sidebarMatches: true,
      navigationMatches: false,
      isSidebarOpen: false,
      desktopSidebarCollapsed: true,
      isSidebarActiveElement: false
    })
    assert.equal(res.shouldCloseDrawer, false)
    assert.equal(res.shouldRestoreFocus, false)
  })

  test('evaluates closing navigation hamburger when navigation breakpoint matches', () => {
    const res = evaluateResponsiveSidebar({
      sidebarMatches: false,
      navigationMatches: true,
      isSidebarOpen: false
    })
    assert.equal(res.shouldCloseNavHamburger, true)
  })
})
