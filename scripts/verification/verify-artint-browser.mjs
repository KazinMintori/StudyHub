import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import puppeteer from 'puppeteer'
import { course } from '../../src/content/courses/ai-nen-tang-tac-tu/course.mjs'

const base = (process.env.QA_URL || 'http://127.0.0.1:5192/StudyHub').replace(/\/$/, '')
const output = 'qa/artint3e/browser'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true,
  ...(process.env.PUPPETEER_EXECUTABLE_PATH ? { executablePath: process.env.PUPPETEER_EXECUTABLE_PATH }
    : process.platform === 'win32' ? { executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' } : {}) })
const errors = [], checks = [], issues = []
try {
  const page = await browser.newPage()
  page.on('pageerror', error => errors.push(error.message))
  await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
  await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
  async function go(route) {
    const response = await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 90000 })
    assert(response?.ok(), `HTTP error ${route}`)
    await page.waitForFunction(() => Boolean(document.querySelector('#app')?.__vue_app__))
    await page.evaluate(() => document.fonts.ready)
  }
  async function inspect(route, width, dark) {
    const found = await page.evaluate(() => {
      const visible = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 }
      const reading = document.querySelector('.vp-doc')
      const math = [...document.querySelectorAll('.vp-doc mjx-container, .vp-doc .static-math')]
        .filter(visible).filter(el => {
          const svg = el.querySelector('svg')
          return el.scrollWidth > el.clientWidth + 2 || (svg && reading && svg.getBoundingClientRect().width > reading.clientWidth + 2)
        }).map(el => (el.textContent || el.getAttribute('data-math') || el.outerHTML).slice(0, 200))
      return { overflow: document.documentElement.scrollWidth > innerWidth + 2,
        math, brokenMath: [...document.querySelectorAll('[data-mjx-error], [data-mml-node="merror"]')].length,
        images: [...document.querySelectorAll('.vp-doc img')].filter(visible).filter(img => img.complete && !img.naturalWidth).map(img => img.getAttribute('src')) }
    })
    if (found.overflow || found.math.length || found.brokenMath || found.images.length) {
      issues.push({ route, width, dark, ...found })
    }
  }
  await page.setViewport({ width: 1280, height: 960 })
  await go('/')
  await page.waitForSelector('.home-extended-portal')
  assert.equal(await page.$(`.course-list a[href*="${course.id}"]`), null)
  await page.screenshot({ path: `${output}/home-1280.png`, fullPage: true })
  checks.push('UET homepage list excludes the external book and has a separate library entrance')

  await go('/hoc-lieu-mo-rong/')
  await page.waitForSelector('.academic-book-card')
  await page.type('#library-search-input', 'Poole')
  assert.equal((await page.$$('.academic-book-card')).length, 1)
  await page.$eval('#library-search-input', el => { el.value = 'khong-co-tai-lieu-12345'; el.dispatchEvent(new Event('input', { bubbles: true })) })
  await page.waitForSelector('.library-empty-state')
  await page.click('.library-empty-state button')
  await page.waitForSelector('.academic-book-card')
  await page.screenshot({ path: `${output}/library-1280.png`, fullPage: true })
  checks.push('Author search, empty results and reset work in the separate library')

  await go(`/${course.id}/`)
  await page.waitForSelector('.lecture-row')
  assert.equal((await page.$$('.lecture-row')).length, 2)
  assert.deepEqual(await page.$$eval('.lesson-number', els => els.map(el => el.textContent.trim())), ['5', '15'])
  assert(await page.$('.book-breadcrumbs a[href*="hoc-lieu-mo-rong"]'))
  checks.push('Course overview has the correct collection breadcrumb and original chapter numbers 5/15')

  for (const width of (process.env.QA_WIDTHS || '1280,375,360').split(',').map(Number)) {
    await page.setViewport({ width, height: 960 })
    for (const route of ['/', '/hoc-lieu-mo-rong/', `/${course.id}/`]) {
      await go(route)
      await inspect(route, width, false)
    }
    for (const lesson of course.lessons) {
      const chapter = `/${course.id}/bai-giang/${lesson.slug}.html`
      await go(chapter)
      await page.waitForSelector('.topic-map')
      assert.equal((await page.$$('h1')).length, 1)
      assert.equal((await page.$$('.topic-map li')).length, 13)
      await page.screenshot({ path: `${output}/chapter-${lesson.number}-${width}.png`, fullPage: true })
      await inspect(chapter, width, false)
      if (width !== 360) continue
      for (const topic of lesson.topicGroups.flatMap(group => group.topics)) {
        const route = `/${course.id}/bai-giang/${lesson.slug}/${topic.slug}.html`
        await go(route)
        await page.waitForSelector('.vp-doc')
        await inspect(route, width, false)
      }
    }
    checks.push(`${width}px: Library, overview and chapter hubs; 360px includes every translated topic`)
  }
  await go('/hoc-lieu-mo-rong/')
  await page.evaluate(() => document.documentElement.classList.add('dark'))
  await inspect('/hoc-lieu-mo-rong/', 360, true)
  await page.screenshot({ path: `${output}/library-dark-360.png`, fullPage: true })
  checks.push('Dark library and reduced-motion layout checked')
  assert.deepEqual(errors, [], 'Browser runtime errors')
  assert.deepEqual(issues, [], 'Responsive/math/image defects; see report.json')
} finally {
  await writeFile(`${output}/report.json`, JSON.stringify({ base, checks, errors, issues }, null, 2))
  await browser.close()
}
console.log(`PASS ${checks.length} ArtInt browser checks`)
