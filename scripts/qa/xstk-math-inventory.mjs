import { readFile, readdir, writeFile } from 'node:fs/promises'
import path from 'node:path'
import { createRequire } from 'node:module'

const require = createRequire(import.meta.url)
const MarkdownIt = require('markdown-it')
const mathjax = require('markdown-it-mathjax3')
const md = new MarkdownIt({ html: true }).use(mathjax.default || mathjax)
const directory = process.argv[2] || 'docs/xac-suat-thong-ke/bai-giang'
const output = process.argv[3] || 'C:/Users/Ai/.codex/tmp/xstk-math-inventory.json'
const results = []
const cache = new Map()
for (const name of await readdir(directory)) {
  if (!/^\d{2}-.+\.md$/.test(name)) continue
  if (process.env.QA_LESSONS && !process.env.QA_LESSONS.split(',').some(prefix => name.startsWith(prefix))) continue
  const file = path.join(directory, name)
  const source = await readFile(file, 'utf8')
  const text = source.replace(/^---[\s\S]*?---/, m => m.replace(/[^\n]/g, ' ')).replace(/```[\s\S]*?```/g, m => m.replace(/[^\n]/g, ' '))
  for (const match of text.matchAll(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g)) {
    const display = match[1] !== undefined
    const tex = (match[1] ?? match[2]).trim()
    const key = `${display}:${tex}`
    if (!cache.has(key)) {
      let html
      try { html = display ? md.render(`$$\n${tex}\n$$`) : md.renderInline(`$${tex}$`) }
      catch (error) { throw new Error(`${name}: ${tex.slice(0, 180)}: ${error.message}`) }
      cache.set(key, { widthEx: Number(html.match(/<svg[^>]*width="([\d.]+)ex"/)?.[1] || 0), error: html.includes('data-mml-node="merror"') })
    }
    const { widthEx, error } = cache.get(key)
    const delimiterLine = source.slice(source.lastIndexOf('\n', match.index) + 1, source.indexOf('\n', match.index) < 0 ? undefined : source.indexOf('\n', match.index)).trim()
    const ownLines = !display || (delimiterLine === '$$' && /\n[\t ]*$/.test(match[1]))
    const invalidBreak = display && /(?:^|\\\\)\s*&?\s*(?:\\quad\s*)?[+-]/.test(tex) && /\\\\/.test(tex)
    if (error || widthEx > (display ? 34 : 38) || !ownLines || invalidBreak) {
      results.push({ file, line: source.slice(0, match.index).split('\n').length, display, widthEx, error, ownLines, invalidBreak, tex })
    }
  }
}
await writeFile(output, JSON.stringify(results, null, 2))
console.log(JSON.stringify({ directory, findings: results.length, errors: results.filter(r => r.error).length, wide: results.filter(r => r.widthEx > (r.display ? 34 : 38)).length, delimiterLines: results.filter(r => !r.ownLines).length, invalidBreaks: results.filter(r => r.invalidBreak).length, output }))
