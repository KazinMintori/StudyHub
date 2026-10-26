import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile, access } from 'node:fs/promises'
import { createRenderer, h, ref, nextTick } from 'vue'
import { normalizeWorkspaceCourse, parseWorkspaceCourse, workspacePath, studyPlanKey, normalizeStudyTasks } from '../services/courseWorkspaceService.mjs'
import { simulationCatalog, courseSimulations } from '../data/course-simulations.mjs'
import { cards } from '../data/flashcards.mjs'
import { courseCatalog } from '../../../content/catalog.mjs'
import { useFlashcards } from '../controllers/useFlashcards.js'
import { useNotebook } from '../controllers/useNotebook.js'

test('course workspace links preserve valid subjects, tabs and a safe static-page URL', () => {
  assert.equal(normalizeWorkspaceCourse('toan-cho-ai', courseCatalog), 'toan-cho-ai')
  for (const value of ['unknown', 'general', '../../private', null, {}, 'TOAN-CHO-AI']) assert.equal(normalizeWorkspaceCourse(value, courseCatalog), 'all')
  assert.equal(parseWorkspaceCourse('?mon=toan-cho-ai&keep=1', courseCatalog), 'toan-cho-ai')
  assert.equal(parseWorkspaceCourse('?mon=unknown', courseCatalog), 'all')
  assert.equal(workspacePath('toan-cho-ai', 'notes'), '/goc-hoc-tap.html?mon=toan-cho-ai#notes')
  assert.equal(workspacePath('all', 'focus'), '/goc-hoc-tap.html#focus')
  assert.equal(workspacePath('../../private', 'unknown'), '/goc-hoc-tap.html#flashcards')
  assert.equal(workspacePath('toan-cho-ai', 'simulation', 'affine'), '/goc-hoc-tap.html?mon=toan-cho-ai&mo-phong=affine#simulation')
  assert.equal(workspacePath('all', 'simulation', 'affine'), '/goc-hoc-tap.html?mo-phong=affine#simulation')
  assert.equal(workspacePath('dsa', 'notes', 'invalid value'), '/goc-hoc-tap.html?mon=dsa#notes')
})

test('every simulation card links to a real Notes page containing its interactive component', async () => {
  assert(simulationCatalog.length >= 10)
  assert.equal(new Set(simulationCatalog.map(item => item.id)).size, simulationCatalog.length)
  for (const entry of simulationCatalog) {
    assert(courseCatalog.some(course => course.id === entry.course))
    const source = await readFile(`docs${entry.path.replace(/\.html$/, '.md')}`, 'utf8')
    assert(source.includes(`<${entry.component}`), entry.path)
    assert(entry.title && entry.description)
  }
  assert(courseSimulations('toan-cho-ai').every(entry => entry.course === 'toan-cho-ai'))
  assert.equal(courseSimulations('all').length, simulationCatalog.length)
  assert.deepEqual(courseSimulations('triet-hoc-mac-lenin'), [])
})

test('each course has flashcards whose lesson links resolve in the published catalog', async () => {
  for (const course of courseCatalog) assert(cards.filter(card => card.course === course.id).length >= 3, course.id)
  for (const card of cards) {
    const course = courseCatalog.find(course => course.id === card.course)
    assert(course, card.course)
    if (card.lesson) {
      assert(course.lessons.some(lesson => lesson.slug === card.lesson), `${card.course}/${card.lesson}`)
      await access(`docs/${card.course}/bai-giang/${card.lesson}.md`)
    }
  }
})

test('study plans have distinct course keys and discard malformed, duplicate and oversized persisted tasks', () => {
  assert.equal(studyPlanKey('all'), 'studyhub_plan_general')
  assert.notEqual(studyPlanKey('toan-cho-ai'), studyPlanKey('vat-ly-1'))
  assert.equal(studyPlanKey('../../private'), 'studyhub_plan_general')
  assert.deepEqual(normalizeStudyTasks(null), [])
  assert.deepEqual(normalizeStudyTasks([
    { id: 'a', text: ' Đọc lại ví dụ ', done: true, secret: 'ignored' },
    { id: 'a', text: 'duplicate', done: false }, null, { id: 'b', text: '' },
    { id: 'c', text: 'Làm bài tập', done: 'false' }
  ]), [{ id: 'a', text: 'Đọc lại ví dụ', done: true }, { id: 'c', text: 'Làm bài tập', done: false }])
  assert.equal(normalizeStudyTasks(Array.from({ length: 200 }, (_, i) => ({ id: String(i), text: 'x'.repeat(500), done: false }))).length, 100)
  assert.equal(normalizeStudyTasks([{ id: 'a', text: 'x'.repeat(500) }])[0].text.length, 300)
})

const renderer = createRenderer({
  createElement: () => ({}), createText: () => ({}), createComment: () => ({}),
  setText() {}, setElementText() {}, insert() {}, remove() {}, patchProp() {}, parentNode: () => null, nextSibling: () => null
})
function mounted(t, create, seed = {}) {
  const oldWindow = globalThis.window, data = new Map(Object.entries(seed).map(([key, value]) => [key, JSON.stringify(value)]))
  const browser = new EventTarget()
  browser.localStorage = { getItem: key => data.get(key) ?? null, setItem: (key, value) => data.set(key, value) }
  globalThis.window = browser
  let controller
  const app = renderer.createApp({ setup() { controller = create(); return () => h('span') } })
  app.mount({})
  t.after(() => { app.unmount(); globalThis.window = oldWindow })
  return { controller, data, storage: browser.localStorage }
}
const courses = [{ id: 'a', name: 'Course A' }, { id: 'b', name: 'Course B' }]

test('changing the shared course filters flashcards without losing progress in another course', async t => {
  const courseId = ref('a')
  const deckCards = [{ course: 'a', q: 'A', a: 'Answer A' }, { course: 'b', q: 'B', a: 'Answer B' }]
  const { controller: deck } = mounted(t, () => useFlashcards({ courses, cards: deckCards, courseId }))
  assert.equal(deck.current.value.q, 'A')
  deck.review(true)
  deck.revealed.value = true
  courseId.value = 'b'; await nextTick()
  assert.equal(deck.current.value.q, 'B')
  assert.equal(deck.knownCount.value, 0)
  assert.equal(deck.revealed.value, false)
  courseId.value = 'a'; await nextTick()
  assert.equal(deck.knownCount.value, 1)
  courseId.value = 'all'; await nextTick()
  assert.equal(deck.deck.value.length, 2)
})

test('changing notebook courses never writes the outgoing note into the next subject, even in one tick', async t => {
  const courseId = ref('a')
  const { controller: notebook, data } = mounted(t, () => useNotebook({ courses, courseId }), {
    studyhub_note_a: '# Course A', studyhub_note_b: '# Course B', studyhub_note_general: '# General'
  })
  await nextTick()
  assert.equal(notebook.note.value, '# Course A')
  notebook.note.value = '# Edited A'
  courseId.value = 'b'
  courseId.value = 'all'
  await nextTick()
  assert.equal(notebook.noteSubject.value, 'general')
  assert.equal(notebook.note.value, '# General')
  assert.equal(JSON.parse(data.get('studyhub_note_a')), '# Edited A')
  assert.equal(JSON.parse(data.get('studyhub_note_b')), '# Course B')
  notebook.note.value = '# Edited General'
  courseId.value = 'a'; await nextTick()
  assert.equal(notebook.note.value, '# Edited A')
  assert.equal(JSON.parse(data.get('studyhub_note_general')), '# Edited General')
})

test('notebook drafts survive quota errors and remain isolated across courses', async t => {
  const courseId = ref('a')
  const { controller: notebook, data, storage } = mounted(t, () => useNotebook({ courses, courseId }), {
    studyhub_note_a: '# Saved A', studyhub_note_b: '# Saved B'
  })
  await nextTick()
  storage.setItem = () => { throw new Error('Storage quota exceeded') }
  notebook.note.value = '# Pending A'
  assert.match(notebook.saved.value, /Chưa lưu/)
  courseId.value = 'b'; await nextTick()
  assert.equal(notebook.note.value, '# Saved B')
  assert.equal(notebook.saved.value, '')
  notebook.note.value = '# Pending B'
  courseId.value = 'a'; await nextTick()
  assert.equal(notebook.note.value, '# Pending A')
  assert.match(notebook.saved.value, /Chưa lưu/)
  courseId.value = 'b'; await nextTick()
  assert.equal(notebook.note.value, '# Pending B')
  assert.equal(JSON.parse(data.get('studyhub_note_a')), '# Saved A')
  assert.equal(JSON.parse(data.get('studyhub_note_b')), '# Saved B')
})

test('notebook keeps an empty unsaved note when storage reads and writes are blocked', async t => {
  const courseId = ref('a')
  const { controller: notebook, storage } = mounted(t, () => useNotebook({ courses, courseId }), { studyhub_note_a: '# Saved A' })
  await nextTick()
  storage.getItem = () => { throw new Error('Storage access denied') }
  storage.setItem = () => { throw new Error('Storage access denied') }
  notebook.note.value = ''
  courseId.value = 'b'; await nextTick()
  notebook.note.value = '# Pending B'
  courseId.value = 'a'; await nextTick()
  assert.equal(notebook.note.value, '')
  assert.match(notebook.saved.value, /Chưa lưu/)
  courseId.value = 'b'; await nextTick()
  assert.equal(notebook.note.value, '# Pending B')
})

test('retrying a notebook save removes its pending overlay and later reads newer saved content', async t => {
  const courseId = ref('a')
  const { controller: notebook, storage, data } = mounted(t, () => useNotebook({ courses, courseId }), { studyhub_note_a: '# Saved A' })
  await nextTick()
  const write = storage.setItem
  storage.setItem = () => { throw new Error('Storage quota exceeded') }
  notebook.note.value = '# Pending A'
  courseId.value = 'b'; await nextTick()
  courseId.value = 'a'; await nextTick()
  assert.equal(notebook.note.value, '# Pending A')
  storage.setItem = write
  notebook.saveNote()
  assert.equal(JSON.parse(data.get('studyhub_note_a')), '# Pending A')
  assert.match(notebook.saved.value, /^Đã lưu/)
  data.set('studyhub_note_a', JSON.stringify('# Newer A from another tab'))
  courseId.value = 'b'; await nextTick()
  courseId.value = 'a'; await nextTick()
  assert.equal(notebook.note.value, '# Newer A from another tab')
})
