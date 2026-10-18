import assert from 'node:assert/strict'
import { mkdir, readFile, writeFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import puppeteer from 'puppeteer'

const base = process.env.QA_URL || 'http://127.0.0.1:5187'
assert(/^http:\/\/127\.0\.0\.1:\d+$/.test(base), 'Use the local dev server')
const root = fileURLToPath(new URL('../', import.meta.url))
const placement = JSON.parse(await readFile(new URL('../raw_materials/xu-ly-du-lieu/lab-placement.json', import.meta.url), 'utf8'))
const output = process.env.QA_OUTPUT || `${root}/qa/data-labs`
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true, executablePath: process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe' })
const report = { pages: [], failures: [], errors: [] }
try {
  const page = await browser.newPage()
  page.on('pageerror', error => report.errors.push(error.message))
  await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
  for (const width of (process.env.QA_WIDTHS || '360,375,768,1280').split(',').map(Number)) {
    await page.setViewport({ width, height: 900 })
    for (const chapter of placement) {
      let response = await page.goto(`${base}/xu-ly-du-lieu/bai-giang/${chapter.slug}.html#bai-tap`, { waitUntil: 'networkidle2', timeout: 120000 })
      if (!response) response = await page.reload({ waitUntil: 'networkidle2', timeout: 120000 })
      if (response) assert(response.ok(), `${chapter.slug}: HTTP ${response.status()}`)
      else assert(page.url().includes(`/bai-giang/${chapter.slug}.html`), 'Unexpected same-document navigation')
      await page.waitForSelector('.lecture-exercises-layout .data-lab-set', { timeout: 30000 })
      await page.evaluate(() => document.fonts.ready)
      assert.equal(await page.$$eval('.data-lab-set', nodes => nodes.length), chapter.files.length)
      assert(await page.$$eval('.data-lab-set details', nodes => nodes.every(node => !node.open)), 'Solutions must initially be folded')
      await page.$$eval('.data-lab-set details', nodes => nodes.forEach(node => { node.open = true }))
      await page.evaluate(async () => {
        await document.fonts.ready
        const images = [...document.querySelectorAll('.data-lab-set img')]
        images.forEach(image => { image.loading = 'eager' })
        await Promise.all(images.map(image => image.decode().catch(() => {})))
      })
      const result = await page.evaluate(() => {
        const visible = element => {
          const head = element.closest('thead')
          return element.getClientRects().length > 0 && (!head || getComputedStyle(head).clipPath === 'none')
        }
        const sets = [...document.querySelectorAll('.data-lab-set')]
        return {
          docWidth: document.documentElement.scrollWidth,
          viewport: innerWidth,
          fontReady: document.fonts.status === 'loaded',
          loadedFonts: [...document.fonts].filter(font => font.status === 'loaded').map(font => font.family),
          mathErrors: [...document.querySelectorAll('.data-lab-set mjx-merror')].map(e => e.textContent),
          unrenderedTex: [...document.querySelectorAll('.data-lab-set pre code')].map(e => e.textContent).filter(text => /\$[^$\n]*\\(?:frac|sqrt|sigma|mu|approx|begin)\b/.test(text)).map(text => text.slice(0, 120)),
          mathOverflow: [...document.querySelectorAll('.data-lab-set mjx-container')].filter(visible).filter(e => {
            const rect = e.getBoundingClientRect()
            return rect.left < -1 || rect.right > innerWidth + 1 || e.scrollWidth > e.clientWidth + 2
          }).map(e => e.textContent.slice(0, 100)),
          missingImages: [...document.querySelectorAll('.data-lab-set img')].filter(e => !e.complete || !e.naturalWidth).map(e => e.src),
          codeBlocks: [...document.querySelectorAll('.data-lab-set div[class*="language-python"]')].map(block => {
            const pre = block.querySelector('pre'), code = pre?.querySelector('code'), copy = block.querySelector('button.copy')
            const rect = pre?.getBoundingClientRect(), button = copy?.getBoundingClientRect()
            return {
              font: code && getComputedStyle(code).fontFamily,
              fontSize: code && parseFloat(getComputedStyle(code).fontSize),
              whitespace: pre && getComputedStyle(pre).whiteSpace,
              fits: Boolean(rect && rect.left >= -1 && rect.right <= innerWidth + 1),
              scrollable: Boolean(pre && (pre.scrollWidth <= pre.clientWidth + 2 || ['auto', 'scroll'].includes(getComputedStyle(pre).overflowX))),
              highlighted: Boolean(code?.querySelector('span[style]')),
              maxLine: Math.max(0, ...(code?.textContent.split('\n').map(line => line.length) || [])),
              copyTarget: Boolean(button && button.width >= 44 && button.height >= 44 && (copy.getAttribute('title') || copy.getAttribute('aria-label')))
            }
          }),
          sets: sets.map(set => ({
            id: set.dataset.lab,
            heading: set.querySelector('h2')?.textContent,
            solutions: set.querySelectorAll('details').length,
            tables: [...set.querySelectorAll('table')].map(table => {
              const rect = table.getBoundingClientRect()
              return { rows: table.rows.length, cols: table.rows[0]?.cells.length, width: rect.width,
                labeled: [...table.querySelectorAll('tbody td')].every(cell => Boolean(cell.dataset.label?.trim())),
                fits: rect.left >= -1 && rect.right <= innerWidth + 1 && (table.scrollWidth <= table.clientWidth + 2 || ['auto', 'scroll'].includes(getComputedStyle(table).overflowX)),
                consistent: [...table.rows].every(row => [...row.cells].reduce((n, cell) => n + cell.colSpan, 0) === table.rows[0].cells.length) }
            })
          }))
        }
      })
      report.pages.push({ width, slug: chapter.slug, ...result })
      const fontsComplete = ['Be Vietnam Pro', 'Source Serif 4', 'JetBrains Mono'].every(name => result.loadedFonts.some(family => family.includes(name)))
      const codeComplete = result.codeBlocks.length > 0 && result.codeBlocks.every(block => block.fits && block.scrollable && block.highlighted && block.copyTarget && block.fontSize >= 14 && block.font.includes('JetBrains') && block.whitespace.startsWith('pre'))
      if (result.docWidth > width + 1 || !result.fontReady || !fontsComplete || !codeComplete || result.mathErrors.length || result.mathOverflow.length || result.unrenderedTex.length || result.missingImages.length || result.sets.some(set => !set.heading || !set.solutions || !set.tables.length || set.tables.some(t => !t.fits || !t.consistent || !t.labeled))) {
        report.failures.push({ width, slug: chapter.slug, result })
      }
      if ([360, 1280].includes(width)) {
        const codeBlock = await page.$('.data-lab-set div[class*="language-python"]')
        await page.evaluate(() => {
          window.__labCopiedText = null
          Object.defineProperty(navigator.clipboard, 'writeText', { configurable: true, value: async text => { window.__labCopiedText = text } })
        })
        const expectedCode = await codeBlock.$eval('pre code', code => code.textContent.trimEnd())
        await (await codeBlock.$('button.copy')).click()
        await page.waitForFunction(() => typeof window.__labCopiedText === 'string', { timeout: 10000 })
        assert.equal(await page.evaluate(() => window.__labCopiedText.trimEnd()), expectedCode, 'Copy must preserve the entire visible code and indentation')
        await codeBlock.scrollIntoView()
        await page.screenshot({ path: `${output}/${chapter.slug}-${width}-code.png` })
        const exerciseId = await page.$eval('.data-lab-set [id^="data-lab-"]', node => node.id)
        await page.evaluate(id => { location.hash = id }, exerciseId)
        await page.waitForSelector('.lecture-exercises-layout .data-lab-set', { timeout: 10000 })
        assert(await page.$eval(`[id="${exerciseId}"]`, node => node.closest('.lecture-exercises-content').getClientRects().length > 0), 'Exercise anchors must keep the exercise tab visible')
        for (const set of await page.$$('.data-lab-set')) {
          const id = await set.evaluate(node => node.dataset.lab)
          const table = await set.$('table')
          if (table) {
            await table.scrollIntoView()
            await page.screenshot({ path: `${output}/${id}-${width}-table.png` })
          }
          const figure = await set.$('figure')
          if (figure) {
            await figure.scrollIntoView()
            await page.screenshot({ path: `${output}/${id}-${width}-figure.png` })
          }
        }
      }
      console.log(`Checked ${width}px ${chapter.slug}: ${result.sets.length} lab sets`)
    }
  }
} finally {
  await browser.close()
  await writeFile(`${output}/browser-report.json`, JSON.stringify(report, null, 2) + '\n')
}
assert.equal(report.failures.length, 0, `Lab render failures: ${report.failures.length}. See report.`)
assert.equal(report.errors.length, 0, `Browser errors: ${report.errors.join('; ')}`)
console.log(`Passed ${report.pages.length} chapter/viewport checks.`)
