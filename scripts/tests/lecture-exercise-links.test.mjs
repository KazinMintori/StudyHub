import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import config from '../../docs/.vitepress/config.mjs'

test('every Math for AI exercise-directory link targets an authored heading', async () => {
  const docs = fileURLToPath(new URL('../../docs/', import.meta.url))
  const md = await createMarkdownRenderer(docs, config.markdown)
  const source = await readFile(`${docs}/toan-cho-ai/bai-tap.md`, 'utf8')
  const links = [...source.matchAll(/\]\(\.\/bai-giang\/([^)#]+\.md)#([^)]*)\)/g)]
  assert.equal(links.length, 8)
  for (const [, file, anchor] of links) {
    const relativePath = `toan-cho-ai/bai-giang/${file}`
    const source = await readFile(`${docs}/${relativePath}`, 'utf8')
    // Let the actual renderer derive automatic IDs too, as in lessons 05/06.
    const html = md.render(source, { relativePath })
    assert.equal(anchor, 'bai-tap-tu-luyen')
    assert(html.includes(`id="${anchor}"`), `${relativePath}: Missing exercise heading ${anchor}`)
  }
})
