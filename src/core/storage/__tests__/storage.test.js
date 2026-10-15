import test from 'node:test'
import assert from 'node:assert/strict'
import {
  readJson,
  writeJson,
  createStorageAdapter,
  getStorage,
  STORAGE_UNAVAILABLE_MESSAGE
} from '../local-storage.js'

function createMockStorage(initial = {}) {
  const store = new Map(Object.entries(initial))
  return {
    getItem(key) {
      return store.has(key) ? store.get(key) : null
    },
    setItem(key, value) {
      store.set(key, String(value))
    },
    removeItem(key) {
      store.delete(key)
    },
    clear() {
      store.clear()
    }
  }
}

test('Browser denial of the localStorage property falls back safely', () => {
  const previous = Object.getOwnPropertyDescriptor(globalThis, 'window')
  Object.defineProperty(globalThis, 'window', {
    configurable: true,
    value: { get localStorage() { throw new Error('Access denied') } }
  })
  try {
    assert.equal(getStorage(), null)
    assert.equal(readJson('notes', 'fallback'), 'fallback')
    assert.equal(writeJson('notes', 'text').success, false)
  } finally {
    if (previous) Object.defineProperty(globalThis, 'window', previous)
    else delete globalThis.window
  }
})

test('readJson retrieves and parses valid JSON', () => {
  const storage = createMockStorage({
    user_key: JSON.stringify({ name: 'StudyHub', version: 1 })
  })
  const result = readJson('user_key', null, storage)
  assert.deepEqual(result, { name: 'StudyHub', version: 1 })
})

test('readJson returns fallback when key is absent', () => {
  const storage = createMockStorage()
  const fallback = { empty: true }
  const result = readJson('nonexistent', fallback, storage)
  assert.strictEqual(result, fallback)
})

test('readJson returns fallback when JSON is malformed', () => {
  const storage = createMockStorage({ corrupted: '{invalid:json' })
  const result = readJson('corrupted', 'default_value', storage)
  assert.strictEqual(result, 'default_value')
})

test('readJson handles null storage without throwing', () => {
  const result = readJson('any_key', 'fallback', null)
  assert.strictEqual(result, 'fallback')
})

test('writeJson stringifies and saves payload successfully', () => {
  const storage = createMockStorage()
  const payload = { progress: 85, done: true }
  const res = writeJson('status', payload, storage)

  assert.strictEqual(res.success, true)
  assert.strictEqual(res.error, null)
  assert.strictEqual(storage.getItem('status'), JSON.stringify(payload))
})

test('writeJson catches storage errors gracefully', () => {
  const throwingStorage = {
    getItem() { return null },
    setItem() {
      throw new Error('QuotaExceededError')
    }
  }
  const res = writeJson('key', { data: 123 }, throwingStorage)
  assert.strictEqual(res.success, false)
  assert.ok(res.error instanceof Error)
  assert.strictEqual(res.error.message, 'QuotaExceededError')
})

test('writeJson fails safely when storage is unavailable', () => {
  const res = writeJson('key', 'value', null)
  assert.strictEqual(res.success, false)
  assert.ok(res.error instanceof Error)
})

test('createStorageAdapter wraps read and write correctly', () => {
  const storage = createMockStorage()
  const adapter = createStorageAdapter(storage)

  adapter.write('count', 42)
  assert.strictEqual(adapter.read('count', 0), 42)
  assert.strictEqual(adapter.read('missing', 99), 99)
})

test('getStorage prioritizes custom storage and provides fallback', () => {
  const custom = createMockStorage()
  assert.strictEqual(getStorage(custom), custom)
  assert.strictEqual(typeof STORAGE_UNAVAILABLE_MESSAGE, 'string')
})
