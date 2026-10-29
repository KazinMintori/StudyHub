import test from 'node:test'
import assert from 'node:assert/strict'
import { mkdtemp, writeFile, rm } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import path from 'node:path'
import { pathToFileURL } from 'node:url'
import { sharedFrameworkProxy } from '../build/shared-framework-plugin.mjs'

test('different batch chunks reuse one injection symbol and one reactive API', async t => {
  const root = await mkdtemp(path.join(tmpdir(), 'studyhub-runtime-'))
  const key = `studyhub-test-${Date.now()}-${Math.random()}`
  t.after(async () => { delete globalThis[Symbol.for(key)]; await rm(root, { recursive: true, force: true }) })
  await writeFile(path.join(root, 'first.mjs'), 'export const dataSymbol = Symbol(); export const ref = value => ({ value })')
  await writeFile(path.join(root, 'second.mjs'), 'throw Error("A later native framework must not execute"); export const dataSymbol = Symbol(); export const ref = null')
  await writeFile(path.join(root, 'proxy-first.mjs'), sharedFrameworkProxy('first.mjs', ['dataSymbol', 'ref'], key))
  await writeFile(path.join(root, 'proxy-second.mjs'), sharedFrameworkProxy('second.mjs', ['dataSymbol', 'ref'], key))
  const first = await import(pathToFileURL(path.join(root, 'proxy-first.mjs')))
  const second = await import(pathToFileURL(path.join(root, 'proxy-second.mjs')))
  assert.equal(first.dataSymbol, second.dataSymbol)
  assert.equal(first.ref, second.ref)
  assert.deepEqual(second.ref(42), { value: 42 })
})

test('incompatible batch export surfaces fail explicitly', async t => {
  const root = await mkdtemp(path.join(tmpdir(), 'studyhub-runtime-'))
  const key = `studyhub-test-${Date.now()}-${Math.random()}`
  globalThis[Symbol.for(key)] = { ref() {} }
  t.after(async () => { delete globalThis[Symbol.for(key)]; await rm(root, { recursive: true, force: true }) })
  await writeFile(path.join(root, 'proxy.mjs'), sharedFrameworkProxy('unused.mjs', ['ref', 'useData'], key))
  await assert.rejects(import(pathToFileURL(path.join(root, 'proxy.mjs'))), /Incompatible StudyHub runtime export: useData/)
  assert.throws(() => sharedFrameworkProxy('framework.mjs', ['invalid-name']))
})
