import test from 'node:test'
import assert from 'node:assert/strict'
import { mkdtemp, mkdir, writeFile, readFile, rm } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import path from 'node:path'
import vm from 'node:vm'
import { spawnSync } from 'node:child_process'
import { partitionPages, expandedMarkdownBytes } from '../build/page-batches.mjs'
import { mergeBatch, finalizeBatches, replacePageMap } from '../build/merge-batches.mjs'

async function temporary(action) {
  const folder = await mkdtemp(path.join(tmpdir(), 'studyhub-batch-test-'))
  try { await action(folder) } finally { await rm(folder, { recursive: true }) }
}
const metadata = map => `<script>window.__VP_HASH_MAP__=JSON.parse(${JSON.stringify(JSON.stringify(map))});window.__VP_SITE_DATA__={title:'Vật lý'};</script>`

test('batch limits retain every page including an oversized chapter', () => {
  const entries = [10, 20, 100, 15, 15, 10].map((bytes, i) => ({ page: `${i}.md`, bytes }))
  const batches = partitionPages(entries, { maxBytes: 50, maxPages: 2 })
  assert.deepEqual(batches.map(batch => batch.pages), [['0.md', '1.md'], ['2.md'], ['3.md', '4.md'], ['5.md']])
  assert.deepEqual(batches.flatMap(batch => batch.pages), entries.map(entry => entry.page))
  assert.throws(() => partitionPages([...entries, entries[0]]), /duplicate/)
})

test('batch weight includes nested Markdown and rejects recursive includes', async () => temporary(async folder => {
  await mkdir(path.join(folder, 'parts'))
  const source = '<!--@include: parts/a.md-->'
  await writeFile(path.join(folder, 'index.md'), source)
  await writeFile(path.join(folder, 'parts/a.md'), 'Nhiệt độ $T$.')
  assert.equal(await expandedMarkdownBytes(path.join(folder, 'index.md')), Buffer.byteLength(source + 'Nhiệt độ $T$.'))
  await writeFile(path.join(folder, 'parts/a.md'), '<!--@include: ../index.md-->')
  await assert.rejects(expandedMarkdownBytes(path.join(folder, 'index.md')), /Recursive/)
}))

test('combined map preserves site data and safely escapes script text', () => {
  const map = { 'a.md': 'new', 'b.md': '</script>' }
  const html = replacePageMap(metadata({ 'a.md': 'old' }), map)
  assert(!html.includes('</script>"'))
  const context = { window: {} }
  vm.runInNewContext(html.slice(8, -9), context)
  assert.deepEqual(JSON.parse(JSON.stringify(context.window.__VP_HASH_MAP__)), map)
  assert.equal(context.window.__VP_SITE_DATA__.title, 'Vật lý')
  assert.throws(() => replacePageMap('<p>No metadata</p>', map), /Expected one/)
})

test('merge keeps both routes, math, images, public HTML and all icon rules', async () => temporary(async folder => {
  const state = { pageMap: {}, files: new Map(), icons: new Set() }
  const target = path.join(folder, 'merged')
  for (const name of ['a', 'b']) {
    const source = path.join(folder, name)
    await mkdir(path.join(source, 'assets'), { recursive: true })
    await writeFile(path.join(source, 'hashmap.json'), JSON.stringify({ [`${name}.md`]: name }))
    await writeFile(path.join(source, `${name}.html`), metadata({ [`${name}.md`]: name }) + '<svg><path d="M1 2"/></svg>')
    await writeFile(path.join(source, `assets/${name}.md.${name}.js`), `export default '${name}'`)
    await writeFile(path.join(source, `assets/${name}.md.${name}.lean.js`), `export default '${name}'`)
    await writeFile(path.join(source, 'image.png'), Buffer.from([1, 2, 3]))
    await writeFile(path.join(source, 'embedded.html'), '<p>Bài giảng nhúng độc lập</p>')
    await writeFile(path.join(source, 'vp-icons.css'), `.icon-${name}{color:red}`)
    await mergeBatch(source, target, state)
  }
  await finalizeBatches(target, { pages: ['a.md', 'b.md'], rewrites: {}, assetsDir: 'assets' }, state)
  assert.equal(await readFile(path.join(target, 'embedded.html'), 'utf8'), '<p>Bài giảng nhúng độc lập</p>')
  for (const name of ['a', 'b']) {
    const html = await readFile(path.join(target, `${name}.html`), 'utf8')
    assert(html.includes('b.md') && html.includes('a.md') && html.includes('<svg>'))
  }
  assert((await readFile(path.join(target, 'vp-icons.css'), 'utf8')).includes('.icon-b'))
  assert.deepEqual([...await readFile(path.join(target, 'image.png'))], [1, 2, 3])
  await rm(path.join(target, 'assets/b.md.b.lean.js'))
  state.files.delete('assets/b.md.b.lean.js')
  await assert.rejects(finalizeBatches(target, { pages: [], rewrites: {}, assetsDir: 'assets' }, state), /Missing page chunk/)
}))

test('merge rejects a differing shared asset rather than overwriting it', async () => temporary(async folder => {
  const source = path.join(folder, 'source'), target = path.join(folder, 'merged')
  await mkdir(source)
  await writeFile(path.join(source, 'hashmap.json'), '{}')
  await writeFile(path.join(source, 'shared.js'), 'first')
  const state = { pageMap: {}, files: new Map(), icons: new Set() }
  await mergeBatch(source, target, state)
  await writeFile(path.join(source, 'shared.js'), 'second')
  await assert.rejects(mergeBatch(source, target, state), /collision/)
  assert.equal(await readFile(path.join(target, 'shared.js'), 'utf8'), 'first')
}))

test('lowercase route map verifies mixed-case filenames without changing hash case', async () => temporary(async folder => {
  const source = path.join(folder, 'source'), target = path.join(folder, 'merged')
  await mkdir(path.join(source, 'assets'), { recursive:true })
  await writeFile(path.join(source, 'hashmap.json'), JSON.stringify({ 'practice-readme.md':'AbC' }))
  await writeFile(path.join(source, 'practice-README.html'), metadata({ 'practice-readme.md':'AbC' }))
  for (const suffix of ['.js','.lean.js']) await writeFile(path.join(source, 'assets/practice-README.md.AbC' + suffix), 'export default 1')
  const state = { pageMap:{}, files:new Map(), icons:new Set() }
  await mergeBatch(source, target, state)
  const plan = { pages:['practice-README.md'], rewrites:{}, assetsDir:'assets' }
  await finalizeBatches(target, plan, state)
  state.pageMap['practice-readme.md'] = 'abc'
  await assert.rejects(finalizeBatches(target, plan, state), /Missing page chunk/)
}))

test('full build refuses local execution before creating a lock or syncing', () => {
  const result = spawnSync(process.execPath, ['scripts/build/build-site.mjs'], {
    encoding: 'utf8', env: { ...process.env, GITHUB_ACTIONS: 'false' }
  })
  assert.notEqual(result.status, 0)
  assert.match(result.stderr, /GitHub Actions only/)
})
