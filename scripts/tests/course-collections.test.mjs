import test from 'node:test'
import assert from 'node:assert/strict'

import {
  DEFAULT_COLLECTION,
  COLLECTION_UET,
  COLLECTION_EXTENDED,
  COLLECTIONS,
  getCourseCollection,
  isUetCourse,
  isExtendedCourse,
  filterCoursesByCollection,
  getUetCourses,
  getExtendedCourses,
  getCourseSource,
  getCollectionMeta,
  resolveCollectionBreadcrumbs
} from '../../src/content/collections.mjs'

import { buildThemeConfig } from '../../src/features/course/services/build-navigation.mjs'
import { useStudyHome } from '../../src/features/study-progress/controllers/useStudyHome.js'
import {
  useCollections,
  normalizeSearch,
  getStartAction,
  getAvailableChapterCount,
  getSourceHostname,
  getMaterialKindLabel
} from '../../src/features/collections/controllers/useCollections.js'

// Fixture catalog representing both legacy UET courses and extended learning materials
const fixtureCatalog = [
  {
    id: 'toan-cho-ai',
    name: 'Cơ sở toán học cho AI',
    description: 'Tối ưu lồi và giải tích ma trận cho học máy',
    // collection is omitted, defaulting to 'uet'
    lessons: [
      { slug: 'bai-01-nhap-mon', title: 'Nhập môn tối ưu', status: 'ready', number: 1 },
      { slug: 'bai-02-tap-loi', title: 'Tập lồi và nón lồi', status: 'ready', number: 2 }
    ]
  },
  {
    id: 'xac-suat-thong-ke',
    name: 'Xác suất thống kê',
    description: 'Xác suất và suy luận thống kê ứng dụng',
    collection: 'uet',
    lessons: [
      { slug: '01-bien-co', title: 'Biến cố và xác suất', status: 'ready', number: 1 }
    ]
  },
  {
    id: 'ai-nen-tang-tac-tu',
    name: 'Trí tuệ nhân tạo: Nền tảng của tác tử tính toán',
    description: 'Giáo trình trí tuệ nhân tạo tiếp cận theo hướng tác tử tính toán, bao gồm biểu diễn tri thức, lập luận logic, lập kế hoạch và học máy',
    collection: 'extended',
    source: {
      title: 'Artificial Intelligence: Foundations of Computational Agents',
      authors: ['David L. Poole', 'Alan K. Mackworth'],
      edition: '3rd',
      year: 2023,
      publisher: 'Cambridge University Press',
      url: 'https://artint.info/3e/html/ArtInt3e.html',
      kind: 'book',
      permission: 'user-confirmed'
    },
    parts: [
      {
        title: 'Phần II: Lập luận và lập kế hoạch tất định (Reasoning and Planning with Certainty)',
        lessons: ['05-menh-de-va-suy-dien']
      },
      {
        title: 'Phần V: Biểu diễn cá thể và quan hệ (Representing Individuals and Relations)',
        lessons: ['15-ca-the-va-quan-he']
      }
    ],
    lessons: [
      { slug: '05-menh-de-va-suy-dien', title: 'Mệnh đề và suy diễn', status: 'ready', number: 5 },
      { slug: '15-ca-the-va-quan-he', title: 'Cá thể và quan hệ', status: 'ready', number: 15 }
    ]
  },
  {
    id: 'chuyen-khao-hoc-sau',
    name: 'Chuyên khảo học sâu nâng cao',
    description: 'Kiến trúc Transformer và mô hình khuếch tán',
    collection: 'extended',
    source: {
      title: 'Advanced Deep Learning Foundations',
      authors: 'Research Lab',
      edition: '1st',
      year: 2024,
      kind: 'monograph',
      permission: 'user-confirmed'
    },
    lessons: [
      { slug: '01-transformer', title: 'Kiến trúc Transformer', status: 'ready', number: 1 }
    ]
  },
  {
    id: 'cs188-ai',
    name: 'Nhập môn trí tuệ nhân tạo',
    description: 'Học phần đại học về tìm kiếm, xác suất và học tăng cường',
    collection: 'extended',
    source: {
      title: 'CS 188: Introduction to Artificial Intelligence',
      authors: ['Dan Klein', 'Pieter Abbeel'],
      year: 2024,
      url: 'https://inst.eecs.berkeley.edu/~cs188/',
      kind: 'university-course',
      permission: 'user-confirmed'
    },
    lessons: [
      { slug: '01-search', title: 'Search', status: 'draft', number: 1 }
    ]
  }
]

test('collections helper defaults legacy courses to uet without hardcoded IDs', () => {
  assert.equal(DEFAULT_COLLECTION, 'uet')
  assert.equal(getCourseCollection({ id: 'toan-cho-ai' }), 'uet')
  assert.equal(getCourseCollection({ id: 'any-new-uet', collection: 'uet' }), 'uet')
  assert.equal(getCourseCollection(null), 'uet')
  assert.equal(getCourseCollection(undefined), 'uet')

  assert.equal(getCourseCollection({ id: 'ai-nen-tang-tac-tu', collection: 'extended' }), 'extended')
  assert.equal(getCourseCollection({ id: 'other-book', collection: 'extended' }), 'extended')

  assert.equal(isUetCourse({ id: 'toan-cho-ai' }), true)
  assert.equal(isUetCourse({ id: 'ai-nen-tang-tac-tu', collection: 'extended' }), false)

  assert.equal(isExtendedCourse({ id: 'ai-nen-tang-tac-tu', collection: 'extended' }), true)
  assert.equal(isExtendedCourse({ id: 'toan-cho-ai' }), false)
})

test('filterCoursesByCollection cleanly separates UET courses and extended materials', () => {
  const uet = getUetCourses(fixtureCatalog)
  const ext = getExtendedCourses(fixtureCatalog)

  assert.equal(uet.length, 2)
  assert.deepEqual(uet.map(c => c.id), ['toan-cho-ai', 'xac-suat-thong-ke'])

  assert.equal(ext.length, 3)
  assert.deepEqual(ext.map(c => c.id), ['ai-nen-tang-tac-tu', 'chuyen-khao-hoc-sau', 'cs188-ai'])
})

test('getCollectionMeta and getCourseSource extract metadata accurately', () => {
  const uetMeta = getCollectionMeta(fixtureCatalog[0])
  assert.equal(uetMeta.id, 'uet')
  assert.equal(uetMeta.isUet, true)
  assert.equal(uetMeta.isExtended, false)
  assert.equal(uetMeta.source, null)

  const extMeta = getCollectionMeta(fixtureCatalog[2])
  assert.equal(extMeta.id, 'extended')
  assert.equal(extMeta.isUet, false)
  assert.equal(extMeta.isExtended, true)
  assert.equal(extMeta.source.title, 'Artificial Intelligence: Foundations of Computational Agents')
  assert.equal(extMeta.source.year, 2023)
  assert.equal(extMeta.source.permission, 'user-confirmed')
})

test('resolveCollectionBreadcrumbs routes extended courses to /hoc-lieu-mo-rong/', () => {
  const uetCrumbs = resolveCollectionBreadcrumbs(fixtureCatalog[0])
  assert.deepEqual(uetCrumbs, [
    { label: 'Trang chủ', link: '/' },
    { label: 'Học phần', link: '/#hoc-phan' }
  ])

  const extCrumbs = resolveCollectionBreadcrumbs(fixtureCatalog[2])
  assert.deepEqual(extCrumbs, [
    { label: 'Trang chủ', link: '/' },
    { label: 'Học liệu mở rộng', link: '/hoc-lieu-mo-rong/' }
  ])
})

test('buildThemeConfig separates navbar menus between UET courses and extended portal', () => {
  const themeConfig = buildThemeConfig({ courseCatalog: fixtureCatalog, wikiGroups: [], concepts: {} })

  const nav = themeConfig.nav
  const uetMenu = nav.find(item => item.text === 'Học phần UET')
  const extMenu = nav.find(item => item.text === 'Học liệu mở rộng')

  assert.ok(uetMenu, 'Nav must contain separate Học phần UET menu')
  assert.ok(extMenu, 'Nav must contain separate Học liệu mở rộng menu')

  // UET menu only contains UET courses
  assert.equal(uetMenu.items.length, 2)
  assert.ok(uetMenu.items.some(i => i.link === '/toan-cho-ai/'))
  assert.ok(!uetMenu.items.some(i => i.link === '/ai-nen-tang-tac-tu/'))

  // Extended menu links to /hoc-lieu-mo-rong/ and contains extended courses
  assert.equal(extMenu.link, '/hoc-lieu-mo-rong/')
  assert.ok(extMenu.items.some(i => i.link === '/hoc-lieu-mo-rong/'))
  assert.ok(extMenu.items.some(i => i.link === '/ai-nen-tang-tac-tu/'))
  assert.ok(!extMenu.items.some(i => i.link === '/toan-cho-ai/'))

  // Sidebar contains dedicated entry for /hoc-lieu-mo-rong/
  assert.ok(themeConfig.sidebar['/hoc-lieu-mo-rong/'])
  assert.ok(themeConfig.sidebar['/ai-nen-tang-tac-tu/'])
})

test('buildThemeConfig supports missing wikiGroups and concepts by default', () => {
  const themeConfig = buildThemeConfig({ courseCatalog: fixtureCatalog })
  assert.ok(themeConfig.nav)
  assert.ok(themeConfig.sidebar)
  assert.deepEqual(themeConfig.sidebar['/wiki/'], [
    { text: 'Wiki học tập', items: [{ text: 'Tất cả thuật ngữ', link: '/wiki/' }] }
  ])
})

test('useStudyHome isolates UET course listings and counts on homepage', () => {
  const home = useStudyHome({ catalog: fixtureCatalog, lastLesson: { value: null } })

  // Homepage listing and counts only UET courses
  assert.equal(home.catalog.length, 2)
  assert.equal(home.visibleCourses.value.length, 2)
  assert.deepEqual(home.visibleCourses.value.map(c => c.id), ['toan-cho-ai', 'xac-suat-thong-ke'])

  // Total count in category all matches UET courses only
  assert.equal(home.getCategoryCount('all'), 2)

  // Extended count is available for the portal card
  assert.equal(home.extendedCount, 3)
  assert.equal(home.extendedCourses.length, 3)
})

test('normalizeSearch handles Vietnamese diacritics and replaces đ with d', () => {
  assert.equal(normalizeSearch('Mệnh đề và suy diễn'), 'menh de va suy dien')
  assert.equal(normalizeSearch('Đại học Công nghệ'), 'dai hoc cong nghe')
  assert.equal(normalizeSearch('Điểm cực trị'), 'diem cuc tri')
})

test('getSourceHostname extracts clean generic hostnames from source URLs', () => {
  assert.equal(getSourceHostname('https://artint.info/3e/html/ArtInt3e.html'), 'artint.info')
  assert.equal(getSourceHostname('https://www.cambridge.org/core/books/ai'), 'cambridge.org')
  assert.equal(getSourceHostname('https://inst.eecs.berkeley.edu/~cs188/'), 'inst.eecs.berkeley.edu')
  assert.equal(getSourceHostname(''), '')
})

test('useCollections powers the extended academic library with search, filter, and safe CTAs', () => {
  const lib = useCollections({ catalog: fixtureCatalog })

  assert.equal(lib.totalCount, 3)
  assert.equal(lib.filteredCourses.value.length, 3)

  // Search by author
  lib.query.value = 'Poole'
  assert.equal(lib.filteredCourses.value.length, 1)
  assert.equal(lib.filteredCourses.value[0].id, 'ai-nen-tang-tac-tu')

  // Search with Vietnamese diacritics and d/đ
  lib.query.value = 'mệnh đề'
  assert.equal(lib.filteredCourses.value.length, 1)
  assert.equal(lib.filteredCourses.value[0].id, 'ai-nen-tang-tac-tu')

  lib.query.value = 'menh de'
  assert.equal(lib.filteredCourses.value.length, 1)
  assert.equal(lib.filteredCourses.value[0].id, 'ai-nen-tang-tac-tu')

  // Search by keyword in description
  lib.query.value = 'Transformer'
  assert.equal(lib.filteredCourses.value.length, 1)
  assert.equal(lib.filteredCourses.value[0].id, 'chuyen-khao-hoc-sau')

  // Filter by material type: book
  lib.query.value = ''
  lib.selectedType.value = 'book'
  assert.equal(lib.filteredCourses.value.length, 1)
  assert.equal(lib.filteredCourses.value[0].id, 'ai-nen-tang-tac-tu')

  // Filter by material type: monograph
  lib.selectedType.value = 'monograph'
  assert.equal(lib.filteredCourses.value.length, 1)
  assert.equal(lib.filteredCourses.value[0].id, 'chuyen-khao-hoc-sau')

  // Filter by material type: university-course
  lib.selectedType.value = 'university-course'
  assert.equal(lib.filteredCourses.value.length, 1)
  assert.equal(lib.filteredCourses.value[0].id, 'cs188-ai')

  // Empty search state
  lib.query.value = 'khong-ton-tai-12345'
  assert.equal(lib.filteredCourses.value.length, 0)
  assert.equal(lib.filteredCount.value, 0)

  // Reset filters
  lib.resetFilters()
  assert.equal(lib.query.value, '')
  assert.equal(lib.selectedType.value, 'all')
  assert.equal(lib.filteredCourses.value.length, 3)

  // Safe CTA: ready lesson in chapter 5 links directly to chapter 5 with label 'Bắt đầu đọc'
  const readyActionArtInt = lib.getStartAction(fixtureCatalog[2])
  assert.equal(readyActionArtInt.link, '/ai-nen-tang-tac-tu/bai-giang/05-menh-de-va-suy-dien')
  assert.equal(readyActionArtInt.label, 'Bắt đầu đọc')
  assert.equal(readyActionArtInt.isReady, true)

  const readyActionMonograph = lib.getStartAction(fixtureCatalog[3])
  assert.equal(readyActionMonograph.link, '/chuyen-khao-hoc-sau/bai-giang/01-transformer')
  assert.equal(readyActionMonograph.label, 'Bắt đầu đọc')
  assert.equal(readyActionMonograph.isReady, true)

  // Course with only draft lessons links safely to overview with 'Xem mục lục & tài liệu'
  const draftAction = lib.getStartAction(fixtureCatalog[4])
  assert.equal(draftAction.link, '/cs188-ai/')
  assert.equal(draftAction.label, 'Xem mục lục & tài liệu')
  assert.equal(draftAction.isReady, false)

  // Chapter counts
  assert.equal(getAvailableChapterCount(fixtureCatalog[2]), 2)
  assert.equal(getAvailableChapterCount(fixtureCatalog[3]), 1)
  assert.equal(getAvailableChapterCount(fixtureCatalog[4]), 0)
})

test('ArtInt course structure conforms to plan requirements', () => {
  const artint = fixtureCatalog[2]
  assert.equal(artint.id, 'ai-nen-tang-tac-tu')
  assert.equal(artint.name, 'Trí tuệ nhân tạo: Nền tảng của tác tử tính toán')
  assert.equal(artint.collection, 'extended')
  assert.equal(artint.source.kind, 'book')
  assert.equal(artint.source.year, 2023)
  assert.equal(artint.source.edition, '3rd')
  assert.equal(artint.source.permission, 'user-confirmed')

  // Parts must be Part II and Part V only
  assert.equal(artint.parts.length, 2)
  assert.ok(artint.parts[0].title.includes('Reasoning and Planning with Certainty'))
  assert.deepEqual(artint.parts[0].lessons, ['05-menh-de-va-suy-dien'])
  assert.ok(artint.parts[1].title.includes('Representing Individuals and Relations'))
  assert.deepEqual(artint.parts[1].lessons, ['15-ca-the-va-quan-he'])

  // Published lessons must only be chapter 5 and 15
  assert.equal(artint.lessons.length, 2)
  assert.equal(artint.lessons[0].slug, '05-menh-de-va-suy-dien')
  assert.equal(artint.lessons[0].status, 'ready')
  assert.equal(artint.lessons[1].slug, '15-ca-the-va-quan-he')
  assert.equal(artint.lessons[1].status, 'ready')
})
