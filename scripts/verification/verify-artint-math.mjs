// Focused source validation; this parses Markdown and TeX without a site build.
import { readdir, readFile, mkdir, writeFile } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import { vietnameseMathOptions } from '../math-fonts/vietnamese.mjs'
import { mathTokens, swallowedMarkdown } from '../math-integrity.mjs'
import { createMathValidator } from './math-validator.mjs'

const root = fileURLToPath(new URL('../../', import.meta.url))
const targets = process.argv.slice(2)
if (!targets.length) targets.push('docs/ai-nen-tang-tac-tu/bai-giang')
const md = await createMarkdownRenderer(path.join(root, 'docs'), { math: vietnameseMathOptions })
const measure = new MarkdownIt().use(mathjax)
const validate = createMathValidator(vietnameseMathOptions)
const cache = new Map(), issues = [], pages = []
let expressions = 0
async function* files(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name)
    if (entry.isDirectory()) yield* files(file)
    else if (entry.name.endsWith('.md')) yield file
  }
}
for (const directory of targets) for await (const file of files(path.resolve(directory))) {
  const source = (await readFile(file, 'utf8')).replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '')
  const relative = path.relative(root, file).replaceAll('\\', '/')
  const env = { relativePath: relative }
  let count = 0
  for (const token of mathTokens(md.parse(source, env))) {
    count++; expressions++
    try {
      if (swallowedMarkdown(token)) throw Error('Markdown swallowed by math delimiters')
      validate(token.content, token.type === 'math_block', relative)
      {
        if (!cache.has(token.content)) {
          const html = token.type === 'math_inline' ? measure.renderInline(`$${token.content}$`) : measure.render(`$$\n${token.content}\n$$`)
          cache.set(token.content, Number(html.match(/width="([\d.]+)ex"/)?.[1] || 0))
        }
        const width = cache.get(token.content)
        if (width > (token.type === 'math_inline' ? 32 : 26)) issues.push({ file: relative, kind: token.type === 'math_inline' ? 'inline-width' : 'display-width', width, tex: token.content })
      }
    } catch (error) { issues.push({ file: relative, kind: 'invalid-math', message: error.message, tex: token.content }) }
  }
  pages.push({ file: relative, expressions: count })
}
const report = { pages: pages.length, expressions, issues, details: pages }
await mkdir(path.join(root, 'qa/artint3e'), { recursive: true })
await writeFile(path.join(root, 'qa/artint3e/math-source.json'), JSON.stringify(report, null, 2))
console.log(JSON.stringify({ pages: report.pages, expressions, issues: issues.length }))
for (const issue of issues) console.log(JSON.stringify(issue))
process.exitCode = issues.length ? 1 : 0
