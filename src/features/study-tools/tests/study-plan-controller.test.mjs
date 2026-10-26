import test from 'node:test'
import assert from 'node:assert/strict'
import { createRenderer, h, ref } from 'vue'
import { useStudyPlan } from '../controllers/useStudyPlan.js'
import { studyPlanKey } from '../services/courseWorkspaceService.mjs'

const renderer = createRenderer({
  createElement: () => ({}), createText: () => ({}), createComment: () => ({}),
  setText() {}, setElementText() {}, insert() {}, remove() {}, patchProp() {},
  parentNode: () => null, nextSibling: () => null
})
const task = (id, text = id, done = false) => ({ id, text, done })
function mounted(t, seed = {}, initialCourse = 'a') {
  const previousWindow = globalThis.window, data = new Map(Object.entries(seed).map(([course, tasks]) => [studyPlanKey(course), JSON.stringify(tasks)]))
  const browser = new EventTarget(), course = ref(initialCourse)
  const storage = {
    getItem: key => data.get(key) ?? null,
    setItem: (key, value) => data.set(key, value)
  }
  browser.localStorage = storage
  globalThis.window = browser
  let plan, unmounted = false
  const app = renderer.createApp({ setup() { plan = useStudyPlan(course); return () => h('span') } })
  app.mount({})
  const unmount = () => { if (!unmounted) { unmounted = true; app.unmount() } }
  t.after(() => { unmount(); globalThis.window = previousWindow })
  function notify(key, newValue, storageArea = storage) {
    const event = new Event('storage')
    Object.assign(event, { key, newValue, storageArea })
    browser.dispatchEvent(event)
  }
  function externalWrite(courseId, tasks, emit = true) {
    const key = studyPlanKey(courseId), value = JSON.stringify(tasks)
    data.set(key, value)
    if (emit) notify(key, value)
  }
  function externalDelete(courseId) {
    const key = studyPlanKey(courseId)
    data.delete(key)
    notify(key, null)
  }
  function externalClear() { data.clear(); notify(null, null) }
  function add(text) { plan.draft.value = text; plan.add() }
  return { plan, course, storage, data, externalWrite, externalDelete, externalClear, notify, unmount, add }
}

test('study plans keep tasks, drafts and completion isolated when the course changes', t => {
  const { plan, course, data, add } = mounted(t, { a: [task('a1')], b: [task('b1')] })
  add('New task for A')
  plan.toggle('a1')
  plan.draft.value = 'Unsubmitted A draft'
  course.value = 'b'
  assert.deepEqual(plan.tasks.value, [task('b1')])
  assert.equal(plan.draft.value, '')
  assert.equal(plan.completed.value, 0)
  add('New task for B')
  course.value = 'a'
  assert.equal(plan.completed.value, 1)
  assert.deepEqual(plan.tasks.value.map(item => item.text), ['a1', 'New task for A'])
  assert.deepEqual(JSON.parse(data.get(studyPlanKey('b'))).map(item => item.text), ['b1', 'New task for B'])
})

test('a plan update merges the latest saved tasks before its storage event is delivered', t => {
  const { plan, data, externalWrite, add } = mounted(t, { a: [task('a1')] })
  externalWrite('a', [task('a1'), task('other-tab')], false)
  plan.toggle('a1')
  assert.deepEqual(plan.tasks.value, [task('a1', 'a1', true), task('other-tab')])
  plan.remove('a1')
  add('Third task')
  assert.deepEqual(JSON.parse(data.get(studyPlanKey('a'))).map(item => item.text), ['other-tab', 'Third task'])
})

test('blocked storage keeps loaded tasks and newer edits in memory', t => {
  const { plan, storage, add } = mounted(t, { a: [task('saved')] })
  storage.getItem = () => { throw new Error('Storage is blocked') }
  storage.setItem = () => { throw new Error('Storage is blocked') }
  add('Unsaved task')
  assert.deepEqual(plan.tasks.value.map(item => item.text), ['saved', 'Unsaved task'])
  plan.toggle('saved')
  assert.equal(plan.tasks.value.find(item => item.id === 'saved')?.done, true)
})

test('a successful write is remembered if storage becomes blocked before the next edit', t => {
  const { plan, storage, add } = mounted(t)
  add('Saved in this session')
  storage.getItem = () => { throw new Error('Storage is blocked') }
  storage.setItem = () => { throw new Error('Storage is blocked') }
  add('Now only in memory')
  assert.deepEqual(plan.tasks.value.map(item => item.text), ['Saved in this session', 'Now only in memory'])
})

test('quota errors preserve pending tasks across course changes and merge other tabs', t => {
  const { plan, course, storage, externalWrite, add } = mounted(t, { a: [task('saved-a')], b: [task('saved-b')] })
  storage.setItem = () => { throw new Error('Storage quota exceeded') }
  add('Pending A')
  course.value = 'b'; add('Pending B')
  externalWrite('a', [task('saved-a'), task('other-a')])
  course.value = 'a'
  assert.deepEqual(plan.tasks.value.map(item => item.text), ['saved-a', 'other-a', 'Pending A'])
  plan.remove('saved-a')
  course.value = 'b'; course.value = 'a'
  assert.deepEqual(plan.tasks.value.map(item => item.text), ['other-a', 'Pending A'])
})

test('clearing storage also clears pending plans in courses that are not currently open', t => {
  const { plan, course, storage, externalClear, add } = mounted(t)
  storage.setItem = () => { throw new Error('Storage quota exceeded') }
  add('Pending A')
  course.value = 'b'; add('Pending B')
  externalClear()
  assert.deepEqual(plan.tasks.value, [])
  course.value = 'a'
  assert.deepEqual(plan.tasks.value, [])
})

test('deleting an inactive course plan discards its unsaved overlay too', t => {
  const { plan, course, storage, externalDelete, add } = mounted(t)
  storage.setItem = () => { throw new Error('Storage quota exceeded') }
  add('Pending A')
  course.value = 'b'
  externalDelete('a')
  course.value = 'a'
  assert.deepEqual(plan.tasks.value, [])
})

test('missing and corrupt plans recover, and external updates affect only their own course', t => {
  const { plan, course, data, externalWrite } = mounted(t, { a: [task('a1')] })
  externalWrite('b', [task('b1')])
  assert.deepEqual(plan.tasks.value, [task('a1')])
  data.set(studyPlanKey('b'), 'not JSON')
  course.value = 'b'
  assert.deepEqual(plan.tasks.value, [])
  externalWrite('b', [{ id: 'b1', text: ' Good ', done: true }, null, { id: 'b1', text: 'duplicate' }])
  assert.deepEqual(plan.tasks.value, [task('b1', 'Good', true)])
  course.value = 'all'
  assert.deepEqual(plan.tasks.value, [])
})

test('unmount releases plan storage listeners without overwriting a newer task list', t => {
  const { plan, data, externalWrite, unmount } = mounted(t, { a: [task('a1')] })
  unmount()
  externalWrite('a', [task('new')])
  assert.deepEqual(plan.tasks.value, [task('a1')])
  assert.deepEqual(JSON.parse(data.get(studyPlanKey('a'))), [task('new')])
})

test('plan form rejects empty drafts and respects the saved task limit', t => {
  const saved = Array.from({ length: 100 }, (_, i) => task(String(i)))
  const { plan, add } = mounted(t, { a: saved })
  add('   ')
  assert.match(plan.error.value, /Nhập một việc/)
  add('One too many')
  assert.match(plan.error.value, /100 việc/)
  assert.equal(plan.tasks.value.length, 100)
  plan.remove('0'); add('Allowed task')
  assert.equal(plan.tasks.value.length, 100)
  assert.equal(plan.error.value, '')
})
