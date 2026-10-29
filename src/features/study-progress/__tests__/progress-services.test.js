import test from 'node:test'
import assert from 'node:assert/strict'
import { courseCatalog } from '../../../content/catalog.mjs'

import {
  canonicalLesson,
  migrateCompletedLessons,
  migrateLastLesson,
  migrateProgress
} from '../services/progress-migration.js'

import {
  calculateProgressKey,
  progressKey
} from '../services/progress-key.js'

import {
  mathAiChapters,
  getLessonChapter,
  getLessonDetailTitle
} from '../services/lesson-labels.js'

import {
  resolveResumeLesson,
  resolveResumeLink,
  resolveDefaultReadyLesson,
  resolveActiveResume
} from '../services/resume-service.js'

import {
  normalizeVietnamese,
  filterCourses
} from '../services/course-filter.js'

import {
  cleanHeadingTitle,
  findActiveHeading,
  buildLastLessonPayload
} from '../services/heading-bookmark.js'

import {
  COURSE_CATEGORIES,
  COURSE_CATEGORY_MAP,
  getCourseCategoryLabel,
  getCourseQuickLinks,
  useStudyHome
} from '../controllers/useStudyHome.js'

// Mock course catalog for pure testing
const mockCourses = [
  {
    id: 'toan-cho-ai',
    name: 'Cơ sở toán học cho AI',
    description: 'Tối ưu lồi và đại số tuyến tính',
    parts: [
      { title: 'Tối ưu lồi', lessons: ['bai-01-nhap-mon'] },
      { title: 'Bài giảng', lessons: ['bai-02-tap-loi'] }
    ],
    lessons: [
      { slug: 'bai-00-on-tap-nen-tang', title: 'Ôn tập nền tảng', status: 'ready', number: 0 },
      { slug: 'bai-01-nhap-mon', title: 'Nhập môn tối ưu', status: 'ready', number: 1 },
      { slug: 'bai-02-tap-loi', title: 'Bài 2: Tập lồi', status: 'ready', number: 2 },
      { slug: 'bai-03-chua-soan', title: 'Chưa soạn', status: 'draft', number: 3 }
    ]
  },
  {
    id: 'lap-trinh-web',
    name: 'Phát triển ứng dụng Web',
    description: 'Frontend và Backend hiện đại',
    lessons: [
      { slug: 'bai-01-html-css', title: 'HTML và CSS cơ bản', status: 'ready', number: 1 }
    ]
  }
]

function mockFindCourse(id) {
  return mockCourses.find(c => c.id === id) || null
}

// 1. Progress Migration & Canonical Paths
test('canonicalLesson standardizes 2-part legacy paths', () => {
  const result = canonicalLesson('/toan-cho-ai/bai-01-nhap-mon', mockFindCourse)
  assert.strictEqual(result, '/toan-cho-ai/bai-giang/bai-01-nhap-mon.html')
})

test('canonicalLesson standardizes notes legacy paths', () => {
  const result = canonicalLesson('/toan-cho-ai/notes/bai-01-nhap-mon.html', mockFindCourse)
  assert.strictEqual(result, '/toan-cho-ai/bai-giang/bai-01-nhap-mon.html')
})

test('canonicalLesson leaves already canonical paths intact', () => {
  const path = '/toan-cho-ai/bai-giang/bai-01-nhap-mon.html'
  assert.strictEqual(canonicalLesson(path, mockFindCourse), path)
})

test('canonicalLesson handles non-lesson or unknown courses safely', () => {
  assert.strictEqual(canonicalLesson('/unknown/bai-01', mockFindCourse), '/unknown/bai-01')
  assert.strictEqual(canonicalLesson(null, mockFindCourse), null)
  assert.strictEqual(canonicalLesson(123, mockFindCourse), 123)
})

test('migrateCompletedLessons migrates all legacy keys to canonical keys', () => {
  const legacyMap = {
    '/toan-cho-ai/bai-01-nhap-mon': true,
    '/toan-cho-ai/notes/bai-02-tap-loi': 1
  }
  const migrated = migrateCompletedLessons(legacyMap, p => canonicalLesson(p, mockFindCourse))
  assert.deepEqual(migrated, {
    '/toan-cho-ai/bai-giang/bai-01-nhap-mon.html': true,
    '/toan-cho-ai/bai-giang/bai-02-tap-loi.html': true
  })
})

test('migrateLastLesson updates last lesson path to canonical', () => {
  const last = { path: '/toan-cho-ai/notes/bai-01-nhap-mon', heading: 'dinh-nghia' }
  const migrated = migrateLastLesson(last, p => canonicalLesson(p, mockFindCourse))
  assert.strictEqual(migrated.path, '/toan-cho-ai/bai-giang/bai-01-nhap-mon.html')
  assert.strictEqual(migrated.heading, 'dinh-nghia')
  assert.strictEqual(migrateLastLesson(null), null)
})

test('migrateProgress runs migration through storage adapter', () => {
  const store = {
    studyhub_completed: { '/toan-cho-ai/bai-01-nhap-mon': true },
    studyhub_last_lesson: { path: '/toan-cho-ai/bai-01-nhap-mon', title: 'Nhập môn' }
  }
  const storageAdapter = {
    read(key, fallback) { return store[key] !== undefined ? store[key] : fallback },
    write(key, val) { store[key] = val }
  }

  migrateProgress(storageAdapter, p => canonicalLesson(p, mockFindCourse))

  assert.strictEqual(
    store.studyhub_completed['/toan-cho-ai/bai-giang/bai-01-nhap-mon.html'],
    true
  )
  assert.strictEqual(
    store.studyhub_last_lesson.path,
    '/toan-cho-ai/bai-giang/bai-01-nhap-mon.html'
  )
})

// 2. Progress Key
test('calculateProgressKey generates correct canonical lesson key', () => {
  const course = mockCourses[0]
  const lesson = course.lessons[0]
  const key = calculateProgressKey(course, lesson, p => canonicalLesson(p, mockFindCourse))
  assert.strictEqual(key, '/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang.html')
  assert.strictEqual(progressKey(null, null), '')
})

test('review bookmarks and progress keys point to the published review hub', () => {
  const course = courseCatalog.find(course => course.id === 'toan-cho-ai')
  const path = calculateProgressKey(course, course.review)
  assert.equal(path, '/toan-cho-ai/on-luyen/tong-hop.html')
  const home = useStudyHome({ catalog: courseCatalog, lastLesson: { value: { path } } })
  assert.equal(home.activeResume.value?.lesson, course.review)
  assert.equal(home.activeResumeLink.value, `${path}#notes`)
})

test('old review progress and saved headings migrate to the published hub without losing completion', () => {
  const oldPath = '/toan-cho-ai/bai-giang/on-luyen.html'
  const path = '/toan-cho-ai/on-luyen/tong-hop.html'
  const saved = { path: oldPath, heading: 'on-luyen-1', headingTitle: 'Ôn luyện 1' }
  const store = {
    studyhub_completed: { [oldPath]: true, [path]: false },
    studyhub_last_lesson: saved
  }

  // The home page may load before the storage migration runs.
  assert.equal(resolveActiveResume(saved, courseCatalog).activeResumeLink, `${path}#on-luyen-1`)
  migrateProgress({
    read: (key, fallback) => store[key] ?? fallback,
    write: (key, value) => { store[key] = value }
  })
  assert.deepEqual(store.studyhub_completed, { [path]: true })
  assert.deepEqual(store.studyhub_last_lesson, { ...saved, path })
  assert.equal(resolveActiveResume(store.studyhub_last_lesson, courseCatalog).activeResumeLink, `${path}#on-luyen-1`)
})

// 3. Lesson Labels
test('getLessonChapter uses mathAiChapters mapping for toan-cho-ai', () => {
  const course = mockCourses[0]
  const lesson = course.lessons[0]
  const chapter = getLessonChapter(course, lesson)
  assert.strictEqual(chapter, mathAiChapters['bai-00-on-tap-nen-tang'])
})

test('getLessonChapter falls back to course part title when not generic', () => {
  const course = mockCourses[0]
  const lesson = course.lessons[1] // in 'Tối ưu lồi' part
  const chapter = getLessonChapter(course, lesson)
  assert.strictEqual(chapter, 'Tối ưu lồi')
})

test('getLessonChapter returns empty string when lesson has no matching part', () => {
  const courseWithoutParts = {
    id: 'lap-trinh-web',
    parts: [{ title: 'Bài giảng', lessons: ['other-slug'] }],
    lessons: [{ slug: 'bai-01-html-css', title: 'HTML' }]
  }
  const chapter = getLessonChapter(courseWithoutParts, courseWithoutParts.lessons[0])
  assert.strictEqual(chapter, '')
})

test('getLessonDetailTitle formats title with lesson number or preserves existing prefix', () => {
  const course = mockCourses[0]
  // lesson 1 does not start with "bài X"
  assert.strictEqual(getLessonDetailTitle(course, course.lessons[1]), 'Bài 1: Nhập môn tối ưu')
  // lesson 2 already starts with "Bài 2:"
  assert.strictEqual(getLessonDetailTitle(course, course.lessons[2]), 'Bài 2: Tập lồi')
  assert.strictEqual(getLessonDetailTitle(null, null), '')
})

// 4. Resume Service & Fallback
test('resolveResumeLesson resolves valid saved lesson', () => {
  const saved = {
    path: '/toan-cho-ai/bai-giang/bai-01-nhap-mon.html',
    heading: 'khai-niem',
    headingTitle: '1. Khái niệm'
  }
  const resume = resolveResumeLesson(saved, mockCourses, {
    canonicalLesson: p => canonicalLesson(p, mockFindCourse),
    progressKey: (c, l) => calculateProgressKey(c, l, p => canonicalLesson(p, mockFindCourse))
  })

  assert.ok(resume)
  assert.strictEqual(resume.course.id, 'toan-cho-ai')
  assert.strictEqual(resume.lesson.slug, 'bai-01-nhap-mon')
  assert.strictEqual(resume.heading, 'khai-niem')
  assert.strictEqual(resume.headingTitle, '1. Khái niệm')
})

test('resolveResumeLesson ignores non-ready draft lessons', () => {
  const saved = {
    path: '/toan-cho-ai/bai-giang/bai-03-chua-soan.html'
  }
  const resume = resolveResumeLesson(saved, mockCourses, {
    canonicalLesson: p => canonicalLesson(p, mockFindCourse),
    progressKey: (c, l) => calculateProgressKey(c, l, p => canonicalLesson(p, mockFindCourse))
  })
  assert.strictEqual(resume, null)
})

test('resolveResumeLesson returns null for null or missing path', () => {
  assert.strictEqual(resolveResumeLesson(null, mockCourses), null)
  assert.strictEqual(resolveResumeLesson({}, mockCourses), null)
})

test('the home page resumes the actual topic URL instead of falling back to another course', () => {
  const path = '/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang/he-thieu-xac-dinh-va-giai-tich-ma-tran.html'
  const home = useStudyHome({
    catalog: courseCatalog,
    lastLesson: { value: { path, heading: 'giai-tich-ma-tran', headingTitle: 'Giải tích ma trận' } }
  })

  assert.equal(home.resume.value?.course.id, 'toan-cho-ai')
  assert.equal(home.resume.value?.lesson.slug, 'bai-00-on-tap-nen-tang')
  assert.equal(home.activeResumeLink.value, `${path}#giai-tich-ma-tran`)
  assert.equal(home.resume.value?.headingTitle, 'Giải tích ma trận')
})

test('resume recognizes the review hub and its own topics outside course.lessons', () => {
  for (const path of [
    '/toan-cho-ai/on-luyen/tong-hop.html',
    '/toan-cho-ai/on-luyen/gradient-backtracking-newton.html'
  ]) {
    const active = resolveActiveResume({ path }, courseCatalog)
    assert.equal(active.resume?.course.id, 'toan-cho-ai')
    assert.equal(active.resume?.lesson.slug, 'on-luyen')
    assert.equal(active.defaultStarter, null)
    assert.equal(active.activeResumeLink, `${path}#notes`)
  }
})

test('resume recognizes philosophy topics and trailing-slash topic URLs', () => {
  const base = '/triet-hoc-mac-lenin/bai-giang/chuong-1-triet-hoc-va-vai-tro/nguon-goc-triet-hoc'
  for (const path of [`${base}.html`, `${base}/`]) {
    const resume = resolveResumeLesson({ path }, courseCatalog)
    assert.equal(resume?.course.id, 'triet-hoc-mac-lenin')
    assert.equal(resume?.lesson.slug, 'chuong-1-triet-hoc-va-vai-tro')
    assert.equal(resume?.path, path)
  }
})

test('resume rejects unlisted topics, unknown review routes and malformed stored paths', () => {
  for (const path of [
    '/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang/khong-ton-tai.html',
    '/toan-cho-ai/on-luyen/khong-ton-tai.html',
    123, {}, [], false
  ]) {
    assert.equal(resolveResumeLesson({ path }, courseCatalog), null)
  }
})

test('resume does not make a draft lesson readable just because it has topics', () => {
  const catalog = [{ id: 'draft-course', lessons: [{
    slug: 'draft', status: 'draft', topics: [{ slug: 'topic' }]
  }] }]
  assert.equal(resolveResumeLesson({ path: '/draft-course/bai-giang/draft/topic.html' }, catalog), null)
})

test('resolveResumeLink builds hash anchor correctly', () => {
  assert.strictEqual(
    resolveResumeLink({ path: '/toan/bai-01.html', heading: 'section-2' }),
    '/toan/bai-01.html#section-2'
  )
  assert.strictEqual(
    resolveResumeLink({ path: '/toan/bai-01.html', heading: '' }),
    '/toan/bai-01.html#notes'
  )
  assert.strictEqual(resolveResumeLink(null), '')
})

test('resolveDefaultReadyLesson finds first ready lesson in catalog', () => {
  const starter = resolveDefaultReadyLesson(mockCourses)
  assert.ok(starter)
  assert.strictEqual(starter.course.id, 'toan-cho-ai')
  assert.strictEqual(starter.lesson.slug, 'bai-00-on-tap-nen-tang')
  assert.strictEqual(starter.path, '/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang')
})

test('resolveDefaultReadyLesson returns null on empty or draft-only catalog', () => {
  const emptyCourses = [{ id: 'empty', lessons: [{ slug: 'draft', status: 'draft' }] }]
  assert.strictEqual(resolveDefaultReadyLesson(emptyCourses), null)
  assert.strictEqual(resolveDefaultReadyLesson([]), null)
})

test('resolveActiveResume falls back to defaultStarter when no saved resume exists', () => {
  const active = resolveActiveResume(null, mockCourses)
  assert.strictEqual(active.resume, null)
  assert.ok(active.defaultStarter)
  assert.strictEqual(active.activeResumeLink, '/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang')
})

test('resolveActiveResume uses resume when valid saved lesson exists', () => {
  const saved = { path: '/toan-cho-ai/bai-giang/bai-01-nhap-mon.html', heading: 'sec-1' }
  const active = resolveActiveResume(saved, mockCourses, {
    canonicalLesson: p => canonicalLesson(p, mockFindCourse),
    progressKey: (c, l) => calculateProgressKey(c, l, p => canonicalLesson(p, mockFindCourse))
  })
  assert.ok(active.resume)
  assert.strictEqual(active.defaultStarter, null)
  assert.strictEqual(active.activeResumeLink, '/toan-cho-ai/bai-giang/bai-01-nhap-mon.html#sec-1')
})

// 5. Course Filter
test('normalizeVietnamese strips diacritics and replaces đ with d', () => {
  assert.strictEqual(normalizeVietnamese('Đại Số Tuyến Tính'), 'dai so tuyen tinh')
  assert.strictEqual(normalizeVietnamese('Bài Giảng Ôn Tập'), 'bai giang on tap')
})

test('filterCourses searches by name and description', () => {
  const matches = filterCourses(mockCourses, 'tuyen tinh')
  assert.strictEqual(matches.length, 1)
  assert.strictEqual(matches[0].id, 'toan-cho-ai')

  const webMatches = filterCourses(mockCourses, 'ung dung web')
  assert.strictEqual(webMatches.length, 1)
  assert.strictEqual(webMatches[0].id, 'lap-trinh-web')

  const all = filterCourses(mockCourses, '')
  assert.strictEqual(all.length, 2)
})

// 6. Heading Bookmark
test('cleanHeadingTitle strips zero-width spaces and whitespace', () => {
  const raw = ' \u200B 2. Khái niệm cơ bản \u200B '
  assert.strictEqual(cleanHeadingTitle(raw), '2. Khái niệm cơ bản')
  assert.strictEqual(cleanHeadingTitle(null), '')
})

test('bookmarks ignore hidden exercise headings and closed solution headings', () => {
  const reading = { id: 'reading', getBoundingClientRect: () => ({ top: 120, height: 32 }) }
  const exercise = { id: 'exercise', getBoundingClientRect: () => ({ top: 0, height: 0 }) }
  assert.equal(findActiveHeading([reading, exercise]), reading)
  assert.equal(findActiveHeading([exercise]), null)
})

test('findActiveHeading returns the last heading at or above maxTop threshold', () => {
  const headings = [
    { id: 'h1', top: 50 },
    { id: 'h2', top: 120 },
    { id: 'h3', top: 180 }
  ]
  const active = findActiveHeading(headings, 160)
  assert.strictEqual(active.id, 'h2')

  const noneVisible = findActiveHeading([{ id: 'h1', top: 200 }], 160)
  assert.strictEqual(noneVisible, null)
  assert.strictEqual(findActiveHeading([]), null)
})

test('buildLastLessonPayload constructs record preserving previous fields', () => {
  const previous = { otherField: 'preserve_me', path: '/old/path' }
  const payload = buildLastLessonPayload({
    previous,
    trackedPath: '/toan-cho-ai/bai-giang/bai-01.html',
    trackedTitle: 'Nhập môn',
    headingId: 'sec-2',
    headingTitle: 'Mục 2'
  })

  assert.deepEqual(payload, {
    otherField: 'preserve_me',
    path: '/toan-cho-ai/bai-giang/bai-01.html',
    title: 'Nhập môn',
    heading: 'sec-2',
    headingTitle: 'Mục 2'
  })
})

test('COURSE_CATEGORIES defines standard categories with labels', () => {
  assert.ok(Array.isArray(COURSE_CATEGORIES))
  assert.ok(COURSE_CATEGORIES.some(c => c.id === 'all'))
  assert.ok(COURSE_CATEGORIES.some(c => c.id === 'toan'))
  assert.ok(COURSE_CATEGORIES.some(c => c.id === 'ai-cs'))
})

test('getCourseCategoryLabel returns mapped category or fallback', () => {
  assert.strictEqual(getCourseCategoryLabel('toan-cho-ai'), 'Toán & Cơ sở ngành')
  assert.strictEqual(getCourseCategoryLabel('unknown-course'), 'Học phần')
})

test('useStudyHome filters courses by category and query together', () => {
  const customCatalog = [
    { id: 'toan-cho-ai', name: 'Cơ sở toán cho AI', description: 'Toán', lessons: [] },
    { id: 'vat-ly-1', name: 'Vật lý 1', description: 'Cơ nhiệt', lessons: [] },
    { id: 'dsa', name: 'DSA', description: 'Cấu trúc dữ liệu', lessons: [] }
  ]
  const home = useStudyHome({ catalog: customCatalog, lastLesson: { value: null } })
  assert.strictEqual(home.visibleCourses.value.length, 3)

  home.selectedCategory.value = 'toan'
  assert.strictEqual(home.visibleCourses.value.length, 1)
  assert.strictEqual(home.visibleCourses.value[0].id, 'toan-cho-ai')

  home.selectedCategory.value = 'all'
  home.query.value = 'vật lý'
  assert.strictEqual(home.visibleCourses.value.length, 1)
  assert.strictEqual(home.visibleCourses.value[0].id, 'vat-ly-1')
})
test('getCourseQuickLinks generates correct links for standard and philosophy courses', () => {
  const stdCourse = {
    id: 'toan-cho-ai',
    lessons: [{ slug: 'bai-01-nhap-mon-toi-uu', status: 'ready' }]
  }
  const stdLinks = getCourseQuickLinks(stdCourse)
  assert.strictEqual(stdLinks.notes, '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu')
  assert.strictEqual(stdLinks.slides, undefined)
  assert.strictEqual(stdLinks.cheatsheet, '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu#cheatsheet')
  assert.strictEqual(stdLinks.exercises, '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu#bai-tap')

  const philCourse = {
    id: 'triet-hoc-mac-lenin',
    presentation: 'philosophy',
    lessons: [{ slug: 'chuong-01-khai-luan', status: 'ready' }]
  }
  const philLinks = getCourseQuickLinks(philCourse)
  assert.strictEqual(philLinks.notes, '/triet-hoc-mac-lenin/chuong-01-khai-luan/')
  assert.strictEqual(philLinks.exercises, '/triet-hoc-mac-lenin/chuong-01-khai-luan/#bai-tap')
})
