import assert from 'node:assert/strict'
import puppeteer from 'puppeteer'
import { mkdir, writeFile } from 'node:fs/promises'

const base = (process.env.QA_URL || 'http://127.0.0.1:5173').replace(/\/$/, '')
const output = process.env.QA_OUTPUT || 'qa/math-mobile-regression'
const routes = [
  ['rl', '/vat-ly-2/bai-giang/10-tu-cam/mach-rl.html', '.vp-doc'],
  ['lc', '/vat-ly-2/bai-giang/10-tu-cam/mach-lc.html', '.vp-doc'],
  ['rlc', '/vat-ly-2/bai-giang/10-tu-cam/mach-rlc.html', '.vp-doc'],
  ['wiki', '/wiki/gradient.html', '.vp-doc'],
  ['affine', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/duong-thang-va-tap-affine.html', '.vp-doc'],
  ['cone', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/non-loi.html', '.vp-doc'],
  ['pagerank', '/giai-thuat-du-lieu/bai-giang/bai-03-pagerank-mo-hinh-va-tinh-toan.html', '.vp-doc'],
  ['bayes', '/bieu-dien-tri-thuc/bai-giang/16-mang-bayes.html', '.vp-doc'],
  ['cheatsheet', '/vat-ly-2/bai-giang/10-tu-cam.html#cheatsheet', '.lecture-cheatsheet'],
  ['foundations', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html#kien-thuc-can-co', '.lecture-foundations'],
  ['data-lab', '/xu-ly-du-lieu/bai-giang/bai-08-du-lieu-thoi-gian.html#bai-tap', '.lecture-exercises-content'],
  ['simulation', '/goc-hoc-tap.html?mon=toan-cho-ai&mo-phong=affine#simulation', '.workspace-lab-runner'],
  ...['01-don-vi-vector', '05-ung-dung-newton', '12-co-hoc-chat-luu', '13-hap-dan', '14-dao-dong', '15-song-co', '16-am-hoc']
    .map(slug => [slug, `/vat-ly-1/bai-giang/${slug}.html#cheatsheet`, '.lecture-cheatsheet'])
].filter(([name]) => !process.env.QA_CASES || process.env.QA_CASES.split(',').includes(name))
assert(routes.length, 'Select at least one known QA case')
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true }), page = await browser.newPage()
const results = [], errors = []
page.on('pageerror', error => errors.push({ url: page.url(), message: error.message }))
await page.evaluateOnNewDocument(() => { try { sessionStorage.setItem('studyhub_welcome_seen', '1') } catch {} })
await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
try {
  for (const width of (process.env.QA_WIDTHS || '360,375,768').split(',').map(Number)) {
    await page.setViewport({ width, height: 900, isMobile: true, hasTouch: true })
    for (const [name, route, selector] of routes) {
      const response = await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 90000 })
      assert(response?.ok(), `${route}: HTTP ${response?.status()}`)
      await page.waitForSelector(selector, { visible: true })
      if (name === 'simulation') await page.waitForSelector(`${selector} .lab-point-controls`)
      else await page.waitForFunction(selector => !!document.querySelector(`${selector} mjx-container`), {}, selector)
      await page.evaluate(async selector => {
        await document.fonts.ready
        document.querySelectorAll(`${selector} details`).forEach(element => { element.open = true })
        await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))
      }, selector)
      const metrics = await page.evaluate(({ selector, width }) => {
        const root = document.querySelector(selector), raw = []
        const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT)
        while (walker.nextNode()) {
          const node = walker.currentNode, parent = node.parentElement
          if (!parent.checkVisibility() || parent.closest('svg,mjx-container,code,pre,script,style')) continue
          if (/\\(?:frac|begin|end|mathcal|sqrt|tag)\b|(?<!\\)\$/.test(node.textContent)) raw.push(node.textContent.slice(0, 160))
        }
        const math = [...root.querySelectorAll('mjx-container')].filter(element => element.checkVisibility())
        const wide = math.filter(element => {
          const rect = element.querySelector('svg')?.getBoundingClientRect()
          if (!rect || rect.right <= width + 1 && rect.left >= -1) return false
          // A table is tested within its own scroll viewport. Clipping a
          // formula in any other ancestor must still fail this check.
          for (let parent = element.parentElement; parent && parent !== root; parent = parent.parentElement) {
            if (['auto', 'scroll'].includes(getComputedStyle(parent).overflowX) && parent.scrollWidth > parent.clientWidth + 1) return false
          }
          return true
        }).map(element => element.querySelector('mjx-assistive-mml')?.textContent?.slice(0, 180))
        const outsideFrame = math.filter(element => {
          if (!element.hasAttribute('display')) return false
          const svg = element.querySelector('svg')?.getBoundingClientRect()
          const frame = element.closest('blockquote,.custom-block,details,.cheatsheet-card,.term-preview')
          if (!svg || !frame) return false
          const rect = frame.getBoundingClientRect(), style = getComputedStyle(frame)
          const left = rect.left + parseFloat(style.borderLeftWidth) + parseFloat(style.paddingLeft)
          const right = rect.right - parseFloat(style.borderRightWidth) - parseFloat(style.paddingRight)
          return svg.left < left - 1 || svg.right > right + 1
        }).map(element => element.querySelector('mjx-assistive-mml')?.textContent?.slice(0, 180))
        return {
          pageWidth: document.documentElement.scrollWidth,
          formulas: math.length, raw, wide, outsideFrame,
          mathErrors: root.querySelectorAll('merror,[data-mjx-error],[data-mml-node="merror"]').length,
          scrollbars: math.filter(element => ['auto', 'scroll'].includes(getComputedStyle(element).overflowX) || ['auto', 'scroll'].includes(getComputedStyle(element).overflowY)).length,
          visibleMathML: [...root.querySelectorAll('mjx-assistive-mml')].filter(element => element.checkVisibility()).length
        }
      }, { selector, width })
      results.push({ name, width, ...metrics })
      const failed = metrics.pageWidth > width + 1 || metrics.raw.length || metrics.wide.length || metrics.outsideFrame.length || metrics.mathErrors || metrics.scrollbars || metrics.visibleMathML
      if (failed || process.env.QA_SCREENSHOTS === '1') await page.screenshot({ path: `${output}/${name}-${width}.png` })
      console.log(`${failed ? 'FAIL' : 'PASS'} ${name} at ${width}px (${metrics.formulas} formulas)`)
    }
  }
  assert.deepEqual(errors, [], 'No browser runtime errors')
  assert.deepEqual(results.filter(result => result.pageWidth > result.width + 1 || result.raw.length || result.wide.length || result.outsideFrame.length || result.mathErrors || result.scrollbars || result.visibleMathML), [], 'Every tested surface must render valid, readable math')
  console.log(`PASS ${results.length} math display checks, zero runtime errors.`)
} finally {
  await writeFile(`${output}/results.json`, JSON.stringify({ results, errors }, null, 2))
  await browser.close()
}
