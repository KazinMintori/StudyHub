import test from 'node:test'
import assert from 'node:assert/strict'
import { mkdir, mkdtemp, copyFile, writeFile, readFile, access, rm } from 'node:fs/promises'
import { spawnSync } from 'node:child_process'
import path from 'node:path'

test('Explicit export replaces marked output without retaining stale chunks', async () => {
  const temporaryRoot = path.resolve('tmp')
  await mkdir(temporaryRoot, { recursive: true })
  const fixture = await mkdtemp(path.join(temporaryRoot, 'static-export-test-'))
  assert(fixture.startsWith(temporaryRoot + path.sep))
  try {
    for (const directory of ['scripts', 'config', 'docs/.vitepress/dist/assets']) await mkdir(path.join(fixture, directory), { recursive: true })
    await copyFile('scripts/export-static.mjs', path.join(fixture, 'scripts/export-static.mjs'))
    await copyFile('config/build.mjs', path.join(fixture, 'config/build.mjs'))
    await writeFile(path.join(fixture, 'docs/.vitepress/dist/index.html'), '<p>Current site</p>')
    await writeFile(path.join(fixture, 'docs/.vitepress/dist/assets/current.js'), 'export default 1')
    const run = () => spawnSync(process.execPath, ['scripts/export-static.mjs'], { cwd: fixture, encoding: 'utf8' })
    const first = run()
    assert.equal(first.status, 0, first.stderr)
    await writeFile(path.join(fixture, 'dist/assets/obsolete.js'), 'old chunk')
    const second = run()
    assert.equal(second.status, 0, second.stderr)
    await assert.rejects(access(path.join(fixture, 'dist/assets/obsolete.js')))
    assert.equal(await readFile(path.join(fixture, 'dist/index.html'), 'utf8'), '<p>Current site</p>')
    await assert.rejects(access(path.join(fixture, 'index.html')))
    await rm(path.join(fixture, 'dist/.studyhub-generated.json'))
    const unmarked = run()
    assert.notEqual(unmarked.status, 0)
    assert.equal(await readFile(path.join(fixture, 'dist/index.html'), 'utf8'), '<p>Current site</p>')
  } finally {
    await rm(fixture, { recursive: true })
  }
})
