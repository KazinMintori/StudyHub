import test from 'node:test'
import assert from 'node:assert/strict'
import { createRenderer, h } from 'vue'
import { useFocusTimer } from '../controllers/useFocusTimer.js'
import { useFlashcards } from '../controllers/useFlashcards.js'

const renderer = createRenderer({
  createElement: () => ({}),
  createText: () => ({}),
  createComment: () => ({}),
  setText() {}, setElementText() {}, insert() {}, remove() {}, patchProp() {},
  parentNode: () => null,
  nextSibling: () => null
})

function mountController(t, useController) {
  const previousWindow = globalThis.window
  const stored = new Map()
  const storage = {
    getItem: key => stored.get(key) ?? null,
    setItem: (key, value) => stored.set(key, value)
  }
  const browser = new EventTarget()
  browser.localStorage = storage
  globalThis.window = browser
  let controller
  const app = renderer.createApp({
    setup() {
      controller = useController()
      return () => h('span')
    }
  })
  app.mount({})
  t.after(() => {
    app.unmount()
    globalThis.window = previousWindow
  })

  function externalWrite(key, value, notify = true) {
    const newValue = JSON.stringify(value)
    storage.setItem(key, newValue)
    if (notify) {
      const event = new Event('storage')
      Object.assign(event, { key, newValue, storageArea: storage })
      browser.dispatchEvent(event)
    }
  }
  function externalClear() {
    stored.clear()
    const event = new Event('storage')
    Object.assign(event, { key: null, newValue: null, storageArea: storage })
    browser.dispatchEvent(event)
  }
  return { controller, app, storage, externalWrite, externalClear }
}

test('Focus timer follows start, pause and reset from another tab', t => {
  const { controller: timer, externalWrite } = mountController(t, useFocusTimer)
  externalWrite('studyhub_focus', {
    minutes: 17, remaining: 1020, running: true, deadline: Date.now() + 1020000, sessions: 2
  })
  assert.equal(timer.minutes.value, 17)
  assert.equal(timer.running.value, true)
  assert.equal(timer.sessions.value, 2)
  externalWrite('studyhub_focus', {
    minutes: 17, remaining: 840, running: false, deadline: 0, sessions: 2
  })
  assert.equal(timer.running.value, false)
  assert.equal(timer.remaining.value, 840)
  externalWrite('studyhub_focus', {
    minutes: 25, remaining: 1500, running: false, deadline: 0, sessions: 2
  })
  assert.equal(timer.minutes.value, 25)
  assert.equal(timer.remaining.value, 1500)
})

test('Leaving an old timer tab does not overwrite a newer session before storage event delivery', t => {
  const { app, storage, externalWrite } = mountController(t, useFocusTimer)
  const session = {
    minutes: 17, remaining: 1020, running: true, deadline: Date.now() + 1020000, sessions: 2
  }
  externalWrite('studyhub_focus', session, false)
  app.unmount()
  assert.deepEqual(JSON.parse(storage.getItem('studyhub_focus')), session)
})

const cards = [
  { course: 'c1', q: 'First question' },
  { course: 'c2', q: 'Second question' }
]

test('Flashcard review preserves a card reviewed in another tab before storage event delivery', t => {
  const { controller: deck, storage, externalWrite } = mountController(t, () => useFlashcards({ cards }))
  externalWrite('studyhub_flashcards', { 'c2:Second question': true }, false)
  deck.review(true)
  assert.deepEqual(JSON.parse(storage.getItem('studyhub_flashcards')), {
    'c1:First question': true,
    'c2:Second question': true
  })
})

test('Flashcard count follows another tab and a course reset preserves its newer reviews', t => {
  const { controller: deck, storage, externalWrite } = mountController(t, () => useFlashcards({ cards }))
  externalWrite('studyhub_flashcards', { 'c1:First question': true })
  assert.equal(deck.knownCount.value, 1)
  deck.subject.value = 'c1'
  externalWrite('studyhub_flashcards', { 'c1:First question': true, 'c2:Second question': true }, false)
  deck.resetReview()
  assert.deepEqual(JSON.parse(storage.getItem('studyhub_flashcards')), { 'c2:Second question': true })
})

test('Flashcard reviews remain available in memory when browser storage becomes blocked', t => {
  const { controller: deck, storage } = mountController(t, () => useFlashcards({ cards }))
  storage.getItem = () => { throw new Error('Storage access denied') }
  storage.setItem = () => { throw new Error('Storage access denied') }
  deck.review(true)
  deck.review(true)
  assert.equal(deck.knownCount.value, 2)
  assert.deepEqual({ ...deck.remembered.value }, {
    'c1:First question': true,
    'c2:Second question': true
  })
})

test('A flashcard quota error does not restore older readable progress over unsaved reviews', t => {
  const { controller: deck, storage } = mountController(t, () => useFlashcards({ cards }))
  storage.setItem = () => { throw new Error('Storage quota exceeded') }
  deck.review(true)
  deck.review(true)
  assert.equal(deck.knownCount.value, 2)
  assert.deepEqual({ ...deck.remembered.value }, {
    'c1:First question': true,
    'c2:Second question': true
  })
})

test('Clearing storage in another tab resets the remembered flashcard count', t => {
  const { controller: deck, storage, externalClear } = mountController(t, () => useFlashcards({ cards }))
  storage.setItem = () => { throw new Error('Storage quota exceeded') }
  deck.review(true)
  assert.equal(deck.knownCount.value, 1)
  externalClear()
  assert.equal(deck.knownCount.value, 0)
  assert.deepEqual({ ...deck.remembered.value }, {})
})
