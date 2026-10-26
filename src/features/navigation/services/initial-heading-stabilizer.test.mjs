import test from 'node:test'
import assert from 'node:assert/strict'
import { stabilizeInitialHeading } from './initial-heading-stabilizer.mjs'

function environment() {
  const events = new Map(), frames = new Map(), timers = new Map()
  let nextId = 1, documentTop = 1000, targetExists = true, resize
  const region = {}
  const browser = {
    location: { href: 'https://study.test/lecture.html#exercise', hash: '#exercise' },
    scrollY: 0, scrolls: [],
    ResizeObserver: class {
      observed = new Set()
      constructor(callback) { resize = callback }
      observe(element) { this.observed.add(element) }
      disconnect() { this.observed.clear() }
    },
    requestAnimationFrame(callback) { const id = nextId++; frames.set(id, callback); return id },
    cancelAnimationFrame(id) { frames.delete(id) },
    setTimeout(callback) { const id = nextId++; timers.set(id, callback); return id },
    clearTimeout(id) { timers.delete(id) },
    addEventListener(name, callback) { events.set(name, callback) },
    removeEventListener(name, callback) { if (events.get(name) === callback) events.delete(name) },
    scrollTo(options) { this.scrolls.push(options); this.scrollY = options.top }
  }
  const target = {
    matches: selector => selector === 'h2, h3, h4',
    getBoundingClientRect: () => ({ top: documentTop - browser.scrollY, width: 600, height: 30 })
  }
  const document = {
    getElementById: id => id === 'exercise' && targetExists ? target : null,
    querySelectorAll: () => [region]
  }
  return {
    browser, document, events, timers,
    shiftTo(top) { documentTop = top; resize() },
    setTargetExists(value) { targetExists = value },
    flush() {
      while (frames.size) {
        const pending = [...frames.values()]; frames.clear()
        for (const callback of pending) callback()
      }
    }
  }
}

test('an initial link follows late article layout changes in both directions', () => {
  const env = environment()
  stabilizeInitialHeading({ ...env, getOffset: () => 134 })
  env.flush()
  assert.equal(env.browser.scrollY, 866)
  env.shiftTo(5200); env.flush()
  assert.equal(env.browser.scrollY, 5066)
  env.shiftTo(2400); env.flush()
  assert.equal(env.browser.scrollY, 2266)
  assert.ok(env.browser.scrolls.every(scroll => scroll.behavior === 'instant'))
})

test('late headings are picked up when content refreshes', () => {
  const env = environment()
  env.setTargetExists(false)
  const stabilizer = stabilizeInitialHeading({ ...env, getOffset: () => 134 })
  env.flush()
  assert.equal(env.browser.scrolls.length, 0)
  env.setTargetExists(true); stabilizer.refresh(); env.flush()
  assert.equal(env.browser.scrollY, 866)
})

test('a query-selected tool can stabilize its own heading without replacing the tab hash', () => {
  const env = environment()
  env.browser.location.href = 'https://study.test/workspace.html?mo-phong=affine#simulation'
  env.browser.location.hash = '#simulation'
  stabilizeInitialHeading({ ...env, targetId: 'exercise', getOffset: () => 72 })
  env.flush()
  assert.equal(env.browser.scrollY, 928)
  env.shiftTo(1800); env.flush()
  assert.equal(env.browser.scrollY, 1728)
  assert.equal(env.browser.location.hash, '#simulation')
})

for (const intent of ['wheel', 'touchstart', 'pointerdown', 'keydown']) {
  test(`${intent} cancels queued corrections and releases observers/listeners`, () => {
    const env = environment()
    stabilizeInitialHeading({ ...env, getOffset: () => 134 })
    env.events.get(intent)()
    env.flush(); env.shiftTo(5200); env.flush()
    assert.equal(env.browser.scrolls.length, 0)
    assert.equal(env.events.size, 0)
    assert.equal(env.timers.size, 0)
  })
}

test('navigation and the bounded deadline stop following the initial anchor', () => {
  for (const cancel of ['url', 'deadline']) {
    const env = environment()
    const stabilizer = stabilizeInitialHeading({ ...env, getOffset: () => 134 })
    env.flush()
    if (cancel === 'url') {
      env.browser.location.href = 'https://study.test/another.html#exercise'
      stabilizer.refresh()
    } else [...env.timers.values()][0]()
    env.shiftTo(5200); env.flush()
    assert.equal(env.browser.scrollY, 866)
    assert.equal(env.events.size, 0)
  }
})
