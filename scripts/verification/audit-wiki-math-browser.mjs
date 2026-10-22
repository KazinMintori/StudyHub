// Render only Wiki content into the live reading column, one document at a time.
// This uses the site's Markdown/MathJax pipeline without a full static build.
import puppeteer from 'puppeteer'
import { createMarkdownRenderer } from 'vitepress'
import { configureStudyMarkdown } from '../build/markdown-presentation.mjs'
import { readdir, readFile, mkdir, writeFile } from 'node:fs/promises'
import path from 'node:path'
import { resolveLayoutClasses } from '../../src/features/navigation/services/sidebar-service.mjs'

const out = process.env.QA_OUT_DIR || 'qa/wiki-expansion-20261022'
await mkdir(out, { recursive: true })
let currentMath = []
const makeRenderer = async () => {
  const renderer = await createMarkdownRenderer(path.resolve('docs'), { math: true, config: md => configureStudyMarkdown(md, { base: '/' }) })
  for (const type of ['math_inline', 'math_block']) {
    const render = renderer.renderer.rules[type]
    renderer.renderer.rules[type] = (...args) => {
      const index = currentMath.push({ type, tex: args[0][args[1]].content }) - 1
      return render(...args).replace(/class="static-math\b/, `data-qa-math="${index}" class="static-math`)
    }
  }
  return renderer
}
let md = await makeRenderer()
const allDocs = process.env.QA_ALL_DOCS === '1'
const browser = await puppeteer.launch({ headless: true })
const page = await browser.newPage(), results = []
await page.setViewport({ width: 320, height: 900 })
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
await page.goto((process.env.QA_BASE_URL || 'http://127.0.0.1:5191') + '/wiki/vector.html', { waitUntil: 'networkidle0' })
await page.evaluate(() => document.fonts.ready)
try {
  async function list(dir) {
    const files = []
    for (const entry of await readdir(dir, { withFileTypes: true })) {
      if (entry.isDirectory() && !['.vitepress', 'public', 'agy-plans'].includes(entry.name)) files.push(...await list(`${dir}/${entry.name}`))
      else if (entry.isFile() && entry.name.endsWith('.md')) files.push(`${dir}/${entry.name}`)
    }
    return files
  }
  let files = allDocs ? await list('docs') : (await readdir('docs/wiki')).filter(file => file.endsWith('.md') && file !== 'index.md').map(file => `docs/wiki/${file}`)
  if (process.env.QA_ONLY_FAILURES) {
    const previous = JSON.parse(await readFile(process.env.QA_ONLY_FAILURES, 'utf8'))
    const subset = new Set(previous.failures.map(entry => entry.file))
    files = files.filter(file => subset.has(file))
  }
  for (const [i, file] of files.entries()) {
    if (i && i % 20 === 0) md = await makeRenderer()
    const document = await readFile(file, 'utf8')
    const front = document.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/)?.[1] || ''
    const frontmatter = Object.fromEntries([...front.matchAll(/^([\w]+):\s*["']?([^\r\n"']*)/gm)].map(match => [match[1], match[2].trim()]))
    const classes = resolveLayoutClasses({ frontmatter })
    const source = document.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '')
    currentMath = []
    const html = md.render(source, { relativePath: file.slice(5) })
    const issues = await page.evaluate(({ html, classes }) => {
      const layout = document.querySelector('.Layout')
      Object.entries(classes).forEach(([name, value]) => layout.classList.toggle(name, value))
      const root = document.querySelector('.main > .vp-doc')
      root.innerHTML = html
      root.querySelectorAll('script, style, iframe, video, audio, img').forEach(el => el.remove())
      root.querySelectorAll('[v-html]').forEach(el => { el.innerHTML = JSON.parse(el.getAttribute('v-html')) })
      root.querySelectorAll('details').forEach(el => { el.open = true })
      const errors = []
      root.querySelectorAll('mjx-container').forEach((el, index) => {
        if (el.closest('table')) return
        const svg = el.querySelector('svg'), r = svg?.getBoundingClientRect()
        const math = el.querySelector('mjx-assistive-mml')?.textContent
        if (el.querySelector('[data-mjx-error], [data-mml-node=merror]')) errors.push({ index, kind: 'render', math })
        if (r?.width && (r.left < -1 || r.right > innerWidth + 1)) errors.push({ index, sourceIndex: Number(el.closest('[data-qa-math]')?.dataset.qaMath), kind: 'overflow', math, width: r.width, right: r.right, left: r.left })
      })
      return { count: root.querySelectorAll('mjx-container').length, errors }
    }, { html, classes })
    for (const error of issues.errors) Object.assign(error, currentMath[error.sourceIndex] || {})
    results.push({ file, ...issues })
    if (issues.errors.length) console.log('ISSUES', file, JSON.stringify(issues.errors))
    if ((i + 1) % 50 === 0) console.log('Checked', i + 1, '/', files.length)
  }
} finally {
  await browser.close()
  const failures = results.filter(result => result.errors.length)
  const report = { files: results.length, math: results.reduce((sum, result) => sum + result.count, 0), failures, results }
  await writeFile(`${out}/${allDocs ? 'all-docs' : 'all-wiki'}-math.json`, JSON.stringify(report, null, 2))
  console.log(JSON.stringify({ files: report.files, math: report.math, failures: failures.length }))
  if (failures.length) process.exitCode = 1
}
