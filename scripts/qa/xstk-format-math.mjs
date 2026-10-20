// Format XSTK display equations without changing their terms or splitting sums.
// Long indivisible sides still require an author to introduce short notation.
import { readFile, writeFile } from 'node:fs/promises'
import { createRequire } from 'node:module'
import { pathToFileURL } from 'node:url'
import path from 'node:path'

const require = createRequire(import.meta.url)
const MarkdownIt = require('markdown-it')
const mathjax = require('markdown-it-mathjax3')
const md = new MarkdownIt().use(mathjax.default || mathjax)
const widths = new Map()
function width(tex) {
  const clean = tex.replaceAll('&', '').trim()
  if (!widths.has(clean)) {
    const html = md.render(`$$\n${clean}\n$$`)
    widths.set(clean, Number(html.match(/<svg[^>]*width="([\d.]+)ex"/)?.[1] || 0))
  }
  return widths.get(clean)
}

function relationPositions(tex) {
  const result = []
  let brace = 0, paren = 0
  for (let i = 0; i < tex.length; i++) {
    const char = tex[i]
    if (char === '\\') {
      const command = tex.slice(i).match(/^\\(?:approx|implies|iff|leq|geq|le|ge|neq|ne)(?![A-Za-z])/)?.[0]
      if (command && brace === 0 && paren === 0) result.push({ index: i, token: command })
      const escaped = tex.slice(i).match(/^\\(?:[A-Za-z]+|.)/)?.[0]
      i += (escaped?.length || 1) - 1
      continue
    }
    if (char === '{') brace++
    else if (char === '}') brace--
    else if (brace === 0 && (char === '(' || char === '[')) paren++
    else if (brace === 0 && (char === ')' || char === ']')) paren--
    else if (brace === 0 && paren === 0 && '=<>'.includes(char)) result.push({ index: i, token: char })
  }
  return result
}

function breakChain(row, aligned) {
  if (width(row) <= 29 || /\\(?:begin|tag|quad|qquad|lbrace|rbrace)\b|\\[{}]/.test(row)) return [row]
  const relations = relationPositions(row)
  if (relations.length < 2) return [row]
  // A comma at the same level may introduce a different equation or condition.
  // Leave those cases for an author, rather than turn them into a false chain.
  if (relations.slice(1).some((r, i) => /,\s*(?:\\(?:quad|qquad)\s*)?[^,]*$/.test(row.slice(relations[i].index + relations[i].token.length, r.index)))) return [row]
  const first = relations[0]
  let left = row.slice(0, first.index).replaceAll('&', '').trim()
  if (!left && !aligned) return [row]
  const result = []
  for (let i = 0; i < relations.length; i++) {
    const current = relations[i]
    const right = row.slice(current.index + current.token.length, relations[i + 1]?.index).trim()
    result.push(`${i === 0 ? left + ' ' : ''}&${current.token} ${right}`.trim())
  }
  return result
}

export function formatMathSource(source) {
  let changed = 0
  // Code fences are preserved verbatim, including literal math delimiters.
  const pieces = source.split(/(^[ \t]*```[^\n]*\n[\s\S]*?^[ \t]*```[^\n]*$)/gm)
  const formatted = pieces.map((piece, index) => {
    if (index % 2) return piece
    return piece.replace(/\$\$([\s\S]*?)\$\$/g, (original, body) => {
      let tex = body.trim()
      const aligned = tex.match(/^\\begin\{aligned\}([\s\S]*?)\\end\{aligned\}$/)
      if (aligned && !/\\begin\{/.test(aligned[1])) {
        const rows = aligned[1].trim().split(/\\\\(?:\[[^\]]*\])?\s*/)
        const broken = rows.flatMap(row => breakChain(row.trim(), true))
        tex = `\\begin{aligned}\n${broken.join(' \\\\\n')}\n\\end{aligned}`
      } else if (!/\\begin\{/.test(tex)) {
        const broken = breakChain(tex, false)
        if (broken.length > 1) tex = `\\begin{aligned}\n${broken.join(' \\\\\n')}\n\\end{aligned}`
      }
      const replacement = `\n\n$$\n${tex}\n$$\n\n`
      if (original !== replacement) changed++
      return replacement
    })
  }).join('').replace(/\n[\t ]*\n(?:[\t ]*\n)+/g, '\n\n')
  return { source: formatted, changed }
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  const write = process.argv.includes('--write')
  for (const file of process.argv.slice(2).filter(arg => arg !== '--write')) {
    if (!/\/xac-suat-thong-ke\/bai-giang\/\d{2}-[^/]+\.md$/.test(path.resolve(file).replaceAll('\\', '/'))) throw new Error(`Outside XSTK Notes: ${file}`)
    const before = await readFile(file, 'utf8')
    const result = formatMathSource(before)
    if (write && result.source !== before) await writeFile(file, result.source)
    console.log(`${write ? 'Formatted' : 'Preview'} ${file}: ${result.changed} display blocks inspected`)
  }
}
