import test from 'node:test'
import assert from 'node:assert/strict'
import { physicsExercisesDevPlugin } from '../build/physics-exercises-dev.mjs'

function devServer(base = '/') {
  let middleware
  const plugin = physicsExercisesDevPlugin({ base })
  assert.equal(plugin.apply, 'serve')
  plugin.configureServer({ middlewares: { use(handler) { middleware = handler } } })
  return async url => {
    const result = { status: 200, headers: {}, skipped: false }
    const response = {
      set statusCode(value) { result.status = value },
      setHeader(name, value) { result.headers[name] = value },
      end(body) { result.body = body }
    }
    await middleware({ url }, response, () => { result.skipped = true })
    return result
  }
}

test('a fresh dev checkout serves a complete Physics index and only the requested rendered group', async () => {
  const request = devServer('/StudyHub/')
  const indexResponse = await request('/StudyHub/physics-exercises/ch11/index.json?v=1')
  assert.equal(indexResponse.status, 200)
  const index = JSON.parse(indexResponse.body)
  assert.equal(index.chapter, 11)
  assert.equal(index.total, 133)
  assert.equal(index.groups.flatMap(group => group.ids).length, index.total)
  assert(index.groups.every(group => !('markdown' in group)))
  const group = index.groups[0]
  const response = await request(`/StudyHub/physics-exercises/ch11/${group.id}.json`)
  assert.equal(response.status, 200)
  const rendered = JSON.parse(response.body)
  assert.deepEqual(rendered.ids, group.ids)
  assert.equal(rendered.id, group.id)
  assert.match(rendered.html, /<mjx-container/)
  assert.doesNotMatch(rendered.html, /v-html=|data-mjx-error|<merror/)
  assert.equal(response.headers['Cache-Control'], 'no-store')
  assert.equal((await request(`/physics-exercises/ch11/${group.id}.json`)).body, response.body)
})

test('the dev middleware ignores other URLs and rejects unknown chapters, groups and traversal', async () => {
  const request = devServer()
  assert.equal((await request('/wiki/')).skipped, true)
  for (const url of ['/physics-exercises/ch99/index.json', '/physics-exercises/ch11/missing.json', '/physics-exercises/ch11/%2e%2e%2fprivate.json']) {
    assert.equal((await request(url)).status, 404, url)
  }
})
