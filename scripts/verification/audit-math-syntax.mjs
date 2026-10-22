// Compile unique TeX expressions in bounded worker processes, without a site build.
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import { createMarkdownRenderer } from 'vitepress'
import { readFile, readdir, mkdir, writeFile } from 'node:fs/promises'
import { spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'
import { concepts } from '../../docs/.vitepress/concepts.mjs'
import { courseCatalog } from '../../src/content/catalog.mjs'
import { configureStudyMarkdown } from '../build/markdown-presentation.mjs'

if (process.argv.includes('--worker')) {
  let input = ''
  for await (const chunk of process.stdin) input += chunk
  const md = new MarkdownIt().use(mathjax), issues = []
  for (const entry of JSON.parse(input)) {
    try {
      const html = entry.type === 'math_block' ? md.render(`$$\n${entry.tex}\n$$`) : md.renderInline(`$${entry.tex}$`)
      if (/data-mjx-error|data-mml-node="merror"|<merror/.test(html)) issues.push({ ...entry, message: 'MathJax returned a rendering error' })
    } catch (error) { issues.push({ ...entry, message: error.message }) }
  }
  console.log(JSON.stringify(issues))
} else {
  const out = process.argv[2] || 'qa/math-syntax'
  await mkdir(out, { recursive: true })
  const md = await createMarkdownRenderer(process.cwd() + '/docs', { math: true, config: md => configureStudyMarkdown(md, { base: '/' }) })
  const expressions = new Map(), skipped = [], issues = []
  let files = 0, occurrences = 0
  function collect(source, file) {
    const tokens = md.parse(source, {})
    for (const token of tokens) {
      for (const math of token.type === 'math_block' ? [token] : (token.children || []).filter(child => child.type === 'math_inline')) {
        occurrences++
        const entry = { type: math.type, tex: math.content, file, line: (math.map?.[0] ?? token.map?.[0] ?? 0) + 1 }
        const key = `${math.type}\0${math.content}`
        if (!expressions.has(key)) expressions.set(key, entry)
      }
    }
  }
  async function walk(dir) {
    for (const entry of await readdir(dir, { withFileTypes: true })) {
      if (entry.isDirectory() && !['.vitepress', 'public', 'agy-plans'].includes(entry.name)) await walk(`${dir}/${entry.name}`)
      else if (entry.isFile() && entry.name.endsWith('.md')) {
        const file = `${dir}/${entry.name}`
        collect(await readFile(file, 'utf8'), file)
        files++
      }
    }
  }
  await walk('docs')
  function data(value, label) {
    if (typeof value === 'string' && value.includes('$')) collect(value, label)
    else if (Array.isArray(value)) value.forEach((item, i) => data(item, `${label}[${i}]`))
    else if (value && typeof value === 'object') for (const [key, item] of Object.entries(value)) data(item, `${label}.${key}`)
  }
  data(concepts, 'concepts')
  data(courseCatalog, 'courseCatalog')
  const entries = [...expressions.values()].filter(entry => {
    if (/\\(?:label|ref|eqref)\b/.test(entry.tex)) { skipped.push(entry); return false }
    return true
  })
  console.log('Collected', occurrences, 'math occurrences;', entries.length, 'unique expressions')
  for (let i = 0; i < entries.length; i += 350) {
    const result = spawnSync(process.execPath, ['--max-old-space-size=512', fileURLToPath(import.meta.url), '--worker'], { input: JSON.stringify(entries.slice(i, i + 350)), encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 })
    if (result.status !== 0) throw new Error(`Math worker failed: ${result.stderr.slice(0, 1200)}`)
    issues.push(...JSON.parse(result.stdout))
    console.log('Compiled', Math.min(i + 350, entries.length), '/', entries.length)
  }
  await writeFile(`${out}/math-syntax.json`, JSON.stringify({ files, occurrences, unique: entries.length, skipped, issues }, null, 2))
  console.log(JSON.stringify({ files, occurrences, unique: entries.length, skipped: skipped.length, issues: issues.length }))
  if (issues.length) process.exitCode = 1
}
