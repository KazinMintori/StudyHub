import test from 'node:test'
import assert from 'node:assert/strict'
import { mkdtemp, mkdir, writeFile, rm } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import path from 'node:path'
import { readMarkdownIncludes } from '../read-markdown-includes.mjs'

test('published include expansion follows nested sources and removes fragment frontmatter', async () => {
  const prefix = path.join(tmpdir(), 'studyhub-includes-')
  const root = await mkdtemp(prefix)
  try {
    await mkdir(path.join(root, 'sources'))
    await writeFile(path.join(root, 'page.md'), '---\ntitle: Trang\n---\n<!-- @include: sources/a.md -->')
    await writeFile(path.join(root, 'sources/a.md'), '---\ntitle: Nguồn\n---\n<!--@include: b.md-->\nĐoạn văn ngoài công thức.')
    const literal = "$& $' $` $$ \\frac{1}{2}"
    await writeFile(path.join(root, 'sources/b.md'), '$$\nx = 0\n$$\n' + literal)
    const text = await readMarkdownIncludes(path.join(root, 'page.md'), root)
    assert(text.includes('title: Trang'))
    assert(!text.includes('title: Nguồn'))
    assert(!text.includes('@include:'))
    assert(text.includes('$$\nx = 0\n$$\n' + literal + '\nĐoạn văn ngoài công thức.'))
    await writeFile(path.join(root, 'sources/b.md'), '<!--@include: a.md-->')
    await assert.rejects(readMarkdownIncludes(path.join(root, 'page.md'), root), /Cyclic Markdown include/)
    await writeFile(path.join(root, 'sources/b.md'), '<!--@include: ../../outside.md-->')
    await assert.rejects(readMarkdownIncludes(path.join(root, 'page.md'), root), /outside repository/)
  } finally {
    // This exact directory was allocated by mkdtemp above, never a user path.
    assert(path.resolve(root).startsWith(path.resolve(prefix)))
    await rm(root, { recursive: true, force: true })
  }
})
