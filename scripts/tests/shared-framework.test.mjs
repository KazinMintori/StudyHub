import test from 'node:test'
import assert from 'node:assert/strict'
import { mkdtemp, mkdir, writeFile, readFile, rm } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import path from 'node:path'
import { pathToFileURL } from 'node:url'
import { sharedFrameworkAlias } from '../build/shared-framework-plugin.mjs'
import { mergeBatch, replaceFrameworkPreloads } from '../build/merge-batches.mjs'

async function fixture(t) {
  const root = await mkdtemp(path.join(tmpdir(), 'studyhub-runtime-'))
  t.after(() => rm(root, { recursive: true, force: true }))
  await writeFile(path.join(root, 'package.json'), '{"type":"module"}')
  const alias = 'assets/chunks/framework-shared.abcdef.js'
  async function batch(name, exports) {
    const directory = path.join(root, name), native = `assets/chunks/framework.${name}.mjs`
    await mkdir(path.join(directory, 'assets/chunks'), { recursive: true })
    await writeFile(path.join(directory, 'hashmap.json'), '{}')
    await writeFile(path.join(directory, native), 'export const dataSymbol = Symbol(); export const ref = value => ({ value })')
    await writeFile(path.join(directory, alias), sharedFrameworkAlias(native))
    await writeFile(path.join(directory, `assets/chunks/framework-surface.${name}.json`), JSON.stringify({ alias, native, exports }))
    return directory
  }
  return { root, alias, batch }
}

test('all batches keep the first runtime alias and one injection symbol', async t => {
  const { root, alias, batch } = await fixture(t)
  const target = path.join(root, 'merged')
  const state = { pageMap: {}, files: new Map(), icons: new Set() }
  await mergeBatch(await batch('first', ['dataSymbol', 'ref']), target, state)
  const first = await import(pathToFileURL(path.join(target, alias)))
  await mergeBatch(await batch('second', ['dataSymbol', 'ref']), target, state)
  const second = await import(pathToFileURL(path.join(target, alias)))
  assert.equal(first.dataSymbol, second.dataSymbol)
  assert.equal(first.ref, second.ref)
  assert.match(await readFile(path.join(target, alias), 'utf8'), /framework\.first\.mjs/)
})

test('a batch cannot require helpers missing from the shared runtime', async t => {
  const { root, batch } = await fixture(t)
  const state = { pageMap: {}, files: new Map(), icons: new Set() }
  await mergeBatch(await batch('first', ['ref']), path.join(root, 'merged'), state)
  await assert.rejects(mergeBatch(await batch('second', ['ref', 'useData']), path.join(root, 'merged'), state), /Incompatible framework exports/)
})

test('HTML preloads use the canonical runtime rather than another batch copy', () => {
  const html = '<link rel="modulepreload" href="/StudyHub/assets/chunks/framework.other.js"><script src="/StudyHub/assets/app.js"></script>'
  assert.equal(replaceFrameworkPreloads(html, { alias: 'assets/chunks/framework-shared.abcdef.js' }), '<link rel="modulepreload" href="/StudyHub/assets/chunks/framework-shared.abcdef.js"><script src="/StudyHub/assets/app.js"></script>')
})
