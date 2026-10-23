import assert from 'node:assert/strict'
import puppeteer from 'puppeteer'
import { mkdir, writeFile } from 'node:fs/promises'

const base = (process.env.QA_URL || 'http://127.0.0.1:5173').replace(/\/$/, '')
const output = process.env.QA_OUTPUT || 'qa/lecture-usability'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true }), page = await browser.newPage()
const results = [], errors = []
page.on('pageerror', error => errors.push({ url: page.url(), message: error.message }))
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
const go = async route => {
  const response = await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 60000 })
  assert(response?.ok(), `${route}: HTTP ${response?.status()}`)
  await page.waitForFunction(() => !!document.querySelector('#app')?.__vue_app__)
  await page.evaluate(() => document.fonts.ready)
}
const record = (name, details) => { results.push({ name, ...details }); console.log('PASS', name) }
const topic = '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/bai-toan-toi-uu.html'
const mathRoutes = [topic, '/bieu-dien-tri-thuc/bai-giang/02-tim-kiem-mu.html',
  '/discrete-math/bai-tap.html', '/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang.html',
  '/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange.html',
  '/toan-cho-ai/bai-giang/bai-04-gradient-newton/phuong-phap-primal-dual.html']
const requestedMath = process.env.QA_MATH_ROUTES?.split(',').map(Number)
const selectedMathRoutes = requestedMath ? mathRoutes.filter((_, index) => requestedMath.includes(index)) : mathRoutes
try {
  // Open solutions too: A collapsed details element can hide an overflowing formula.
  for (const width of process.env.QA_SKIP_MATH === '1' ? [] : [360, 375, 768, 1440]) {
    await page.setViewport({ width, height: 900 })
    for (const route of selectedMathRoutes) {
      await go(route)
      await page.evaluate(async () => {
        document.querySelectorAll('.vp-doc details').forEach(el => { el.open = true })
        await Promise.all([...document.querySelectorAll('.vp-doc details')].flatMap(el => el.getAnimations({ subtree: true })).filter(animation => animation.effect?.getComputedTiming().iterations !== Infinity).map(animation => animation.finished.catch(() => {})))
        await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))
      })
      const metrics = await page.evaluate(() => ({
        pageWidth: document.documentElement.scrollWidth,
        mathErrors: document.querySelectorAll('[data-mjx-error]').length,
        overflow: [...document.querySelectorAll('mjx-container')]
          .filter(el => el.checkVisibility() && el.getBoundingClientRect().width > 0 && el.scrollWidth > el.clientWidth + 1)
          .map(el => ({ text: el.textContent.slice(0, 100), width: el.clientWidth, contentWidth: el.scrollWidth }))
      }))
      assert.equal(metrics.mathErrors, 0, `Broken MathJax: ${route}`)
      assert(metrics.pageWidth <= width + 1, `Page overflow at ${width}: ${route} (${metrics.pageWidth}px)`)
      assert.deepEqual(metrics.overflow, [], `Formula overflow at ${width}: ${route}`)
      record(`${width}px: Complete lecture and solution math fits`, { route, ...metrics })
    }
  }
  if (process.env.QA_ONLY_MATH !== '1') {
  await page.setViewport({ width: 1440, height: 900 })
  await go(topic)
  await go('/')
  const resume = await page.$eval('.resume-cta-btn', el => ({ text: el.textContent.trim(), href: el.href }))
  assert(resume.href.includes(topic.replace(/\.html$/, '')), JSON.stringify(resume))
  assert.match(resume.text, /Tiếp tục học/)
  record('Homepage resumes the exact topic just read', resume)

  await go('/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange.html')
  const before = page.url()
  await page.evaluate(() => {
    window.modifiedLectureClick = null
    window.addEventListener('click', event => {
      if (event.ctrlKey && event.target.closest('.lecture-tabs a')) queueMicrotask(() => {
        window.modifiedLectureClick = { trusted: event.isTrusted, prevented: event.defaultPrevented }
      })
    })
  })
  await page.keyboard.down('Control')
  await page.click('.lecture-tabs a[href$="#cheatsheet"]')
  await page.keyboard.up('Control')
  await page.waitForFunction(() => !!window.modifiedLectureClick)
  assert.deepEqual(await page.evaluate(() => window.modifiedLectureClick), { trusted: true, prevented: false })
  assert.equal(page.url(), before)
  await page.click('.lecture-tabs a[href$="#cheatsheet"]')
  await page.waitForFunction(() => location.hash === '#cheatsheet' && !!document.querySelector('.lecture-cheatsheet'))
  record('Ctrl+click preserves native link handling; ordinary clicks switch the lecture tab')

  await go('/toan-cho-ai/bai-tap.html')
  const exerciseLinks = await page.$$eval('.vp-doc table a', links => links.map(link => link.href))
  assert.equal(exerciseLinks.length, 8)
  for (const href of [exerciseLinks[0], exerciseLinks[3]]) {
    const url = new URL(href, page.url())
    assert.equal(url.hash, '#bai-tap-tu-luyen')
    await page.goto(url.href, { waitUntil: 'networkidle0', timeout: 60000 })
    await page.waitForFunction(() => !!document.getElementById('bai-tap-tu-luyen')?.checkVisibility())
    assert(await page.$eval('#bai-tap-tu-luyen', el => {
      const rect = el.getBoundingClientRect()
      return rect.top >= 0 && rect.top < innerHeight
    }))
  }
  record('Math for AI exercise links scroll to authored exercise headings')

  const vectorTopic = '/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang/he-thieu-xac-dinh-va-giai-tich-ma-tran.html'
  await page.setViewport({ width: 768, height: 600 })
  await go(vectorTopic)
  const vector = '.vp-doc button.study-term[data-term="vector"]'
  await page.$eval(vector, el => window.scrollBy(0, el.getBoundingClientRect().top - 250))
  await page.hover(vector)
  await page.waitForSelector('.term-preview:not(.is-pinned)')
  const preview = await page.$eval('.term-preview', el => { const r = el.getBoundingClientRect(); return { top: r.top, bottom: r.bottom, right: r.right } })
  assert(preview.top >= 0 && preview.bottom <= 600 && preview.right <= 768, JSON.stringify(preview))
  await page.click(vector)
  await page.waitForSelector('.term-preview.is-pinned')
  await page.keyboard.press('Escape')
  await page.waitForFunction(() => !document.querySelector('.term-preview'))
  assert(await page.$eval(vector, el => el === document.activeElement))
  record('Tablet Wiki previews fit the viewport and preserve pin, Escape and focus', preview)
  await page.screenshot({ path: `${output}/tablet.png` })

  await go('/404.html')
  const wikiLink = '.not-found-page a[href$="/wiki/"]'
  assert.match(await page.$eval(wikiLink, el => el.textContent), /Tra cứu Wiki/)
  await page.click(wikiLink)
  await page.waitForFunction(() => /Wiki thuật ngữ/.test(document.querySelector('h1')?.textContent || ''))
  record('The 404 recovery link opens the Wiki')

  await go('/vat-ly-1/bai-giang/11-can-bang-dan-hoi.html#bai-tap')
  await page.waitForSelector('.chapter-exercise-groups .exercise-group-content', { timeout: 30000 })
  assert(await page.$('.chapter-exercise-groups .exercise-group-content mjx-container'))
  record('Physics exercises render on demand in a fresh dev checkout')
  }
  assert.deepEqual(errors, [])
  console.log(`PASS ${results.length} browser checks, zero runtime errors.`)
} finally {
  await writeFile(`${output}/results.json`, JSON.stringify({ results, errors }, null, 2))
  await browser.close()
}
