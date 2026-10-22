// Parse documents without bundling the site or generating static HTML.
import { createMarkdownRenderer } from 'vitepress'
import { configureStudyMarkdown } from '../build/markdown-presentation.mjs'
import { readdir, readFile, mkdir, writeFile } from 'node:fs/promises'
import path from 'node:path'

const out = process.argv[2] || 'qa/markdown-audit'
await mkdir(out, { recursive: true })
const md = await createMarkdownRenderer(path.resolve('docs'), { math: true, config: md => configureStudyMarkdown(md, { base: '/' }) })
async function* files(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    if (entry.isDirectory() && !['.vitepress', 'public', 'agy-plans'].includes(entry.name)) yield* files(`${dir}/${entry.name}`)
    else if (entry.isFile() && entry.name.endsWith('.md')) yield `${dir}/${entry.name}`
  }
}
const issues = [], fences = [], stats = { files: 0, math: 0, code: 0 }
for await (const file of files('docs')) {
  const source = await readFile(file, 'utf8'), tokens = md.parse(source, { relativePath: file.slice(5) })
  stats.files++
  for (const token of tokens) {
    if (token.type === 'fence') {
      stats.code++
      fences.push({ file, line: token.map[0] + 2, language: token.info.trim().split(/\s/)[0], code: token.content })
    }
    if (token.type === 'math_block') {
      stats.math++
      if (/^\s*(?:#{1,6} |:::|\d+\.\s*\*\*|-\s*\*\*)/m.test(token.content) || /\*\*[^*]+\*\*/.test(token.content)) issues.push({ file, line: token.map[0] + 1, kind: 'prose-in-math', sample: token.content.slice(0, 220) })
      if (/(?<!\\)\$/.test(token.content)) issues.push({ file, line: token.map[0] + 1, kind: 'nested-math-delimiter', sample: token.content.slice(0, 220) })
      if (/\\(?:vert|Vert)\{\}/.test(token.content)) issues.push({ file, line: token.map[0] + 1, kind: 'empty-absolute-delimiter' })
      if (/\\\\/.test(token.content) && !/\\begin\{/.test(token.content)) issues.push({ file, line: token.map[0] + 1, kind: 'linebreak-outside-environment' })
      if (/(?<!\\)\b(?:lambda|theta|alpha|omega|Delta)\b/.test(token.content)) issues.push({ file, line: token.map[0] + 1, kind: 'unescaped-greek-name' })
    }
  }
}
await writeFile(`${out}/markdown-audit.json`, JSON.stringify({ stats, issues }, null, 2))
await writeFile(`${out}/code-fences.json`, JSON.stringify(fences, null, 2))
console.log(JSON.stringify({ stats, count: issues.length, sample: issues.slice(0, 20) }, null, 2))
if (issues.length) process.exitCode = 1
