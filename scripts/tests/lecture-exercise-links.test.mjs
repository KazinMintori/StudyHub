import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import config from '../../docs/.vitepress/config.mjs'
import { course } from '../../src/content/courses/toan-cho-ai/course.mjs'

test('Math for AI homework hub and sidebar link to all five complete assigned sets', async () => {
  const docs = fileURLToPath(new URL('../../docs/', import.meta.url))
  const md = await createMarkdownRenderer(docs, config.markdown)
  const source = await readFile(`${docs}/toan-cho-ai/bai-tap.md`, 'utf8')
  const links = [...source.matchAll(/\]\(problem-set\/(homework-0[1-5])\.md\)/g)].map(match=>match[1])
  assert.deepEqual(links, course.problemSets.map(set=>set.slug))
  assert.equal(links.length,5)
  const counts=[10,8,8,6,8]
  for (const [index,slug] of links.entries()) {
    const relativePath = `toan-cho-ai/problem-set/${slug}.md`
    const source = await readFile(`${docs}/${relativePath}`, 'utf8')
    assert.match(source,/^course: toan-cho-ai$/m)
    assert.match(source,/^section: problem-set$/m)
    const tokens=md.parse(source,{relativePath})
    assert.equal(tokens.filter(token=>token.type==='heading_open'&&token.tag==='h1').length,1)
    assert.equal([...source.matchAll(/^::: exercise\b/gm)].length,counts[index])
    assert.equal([...source.matchAll(/^::: solution\b/gm)].length,counts[index])
  }
})
