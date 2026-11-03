import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile, readFile } from 'node:fs/promises'
import { course } from '../../src/content/courses/bieu-dien-tri-thuc/course.mjs'
const base = process.env.QA_BASE_URL || 'http://127.0.0.1:5188'
const output = 'qa/knowledge-course'
await mkdir(output, { recursive: true })
const recheck = process.env.QA_RECHECK === '1'
const previous = recheck ? JSON.parse(await readFile(output + '/pages.json', 'utf8')) : null
const retryRoutes = new Set(previous?.issues.map(issue => issue.route) || [])
for (let attempt = 0; attempt < 90; attempt++) {
  const ready = await fetch(base, { signal: AbortSignal.timeout(2000) }).then(response => response.ok, () => false)
  if (ready) break
  if (attempt === 89) throw Error('Preview unavailable')
  await new Promise(resolve => setTimeout(resolve, 1000))
}
const browser = await puppeteer.launch({
  headless: true,
  executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe',
  args: ['--no-sandbox']
})
const errors = [], issues = [], results = []
const root = '/bieu-dien-tri-thuc/bai-giang/'
try {
  assert.equal(course.lessons.length, 15)
  assert.deepEqual(course.lessons.map(lesson => lesson.number), Array.from({ length: 15 }, (_, index) => index + 1))
  for (const width of [375, 1440]) {
    const tasks = course.lessons.flatMap(lesson => [
      { route: lesson.slug, lesson },
      ...lesson.topicGroups.flatMap(group => group.topics.map(topic => ({ route: lesson.slug + '/' + topic.slug, lesson })))
    ])
    await Promise.all([0, 1].map(async () => {
      const page = await browser.newPage()
      await page.setViewport({ width, height: 950 })
      page.on('pageerror', error => errors.push(error.message))
      page.on('console', message => { if (message.text().includes('Failed to resolve component')) errors.push(message.text()) })
      while (tasks.length) {
        const { route, lesson } = tasks.shift()
        if (recheck && route !== lesson.slug && !retryRoutes.has(route)) continue
        const response = await page.goto(base + root + route + '.html', { waitUntil: 'networkidle0', timeout: 120000 })
        assert.equal(response.status(), 200, route)
        await page.waitForSelector('.vp-doc', { timeout: 60000 }).catch(async error => {
          console.log('Failed route', route, 'page errors', errors)
          console.log((await page.$eval('body', element => element.textContent)).slice(0, 600))
          throw error
        })
        if (route === lesson.slug) {
          for (const hash of ['#notes', '#cheatsheet', '#kien-thuc-can-co']) {
            await page.evaluate(hash => { location.hash = hash }, hash)
            await new Promise(resolve => setTimeout(resolve, 100))
            const bad = await page.$$eval('.math-text svg', elements => elements.filter(element => {
              const rect = element.getBoundingClientRect()
              return rect.width > 0 && (rect.right > innerWidth + 2 || rect.left < -2)
            }).map(element => element.closest('.math-text').textContent))
            if (bad.length) issues.push({ width, route, panel: hash, math: bad })
          }
          await page.evaluate(() => { location.hash = '#notes' })
          await page.waitForSelector('.knowledge-review select')
          const count = course.slides.filter(slide => slide.note === lesson.slug).length
          assert.equal(await page.$$eval('.knowledge-review option', elements => elements.length), count)
          for (let i = 0; i < count; i++) await page.select('.knowledge-review select', String(i))
          results.push({ width, route, cards: count })
        }
        await page.evaluate(() => document.documentElement.classList.remove('dark'))
        const state = await page.evaluate(() => {
          const content = document.querySelector('.vp-doc')
          const bounds = content.getBoundingClientRect()
          const math = [...content.querySelectorAll('mjx-container svg')].filter(element => {
            const rect = element.getBoundingClientRect()
            return rect.width > bounds.width + 2 || rect.right > innerWidth + 2
          }).map(element => element.closest('mjx-container').textContent)
          const images = [...content.querySelectorAll('img')].filter(image => image.complete && image.naturalWidth === 0).map(image => image.src)
          return { overflow: document.documentElement.scrollWidth > innerWidth + 2, math, images }
        })
        if (state.overflow || state.math.length || state.images.length) issues.push({ width, route, ...state })
        for (const slider of await page.$$('.math-lab .simulation-controls input[type=range]')) {
          await slider.evaluate(element => { element.value = element.max; element.dispatchEvent(new Event('input', { bubbles: true })) })
        }
        results.push({ width, route })
      }
      await page.close()
    }))
    console.log(width + 'px: all fifteen lesson hubs, tabs, cards and topics checked')
  }
  await writeFile(output + (recheck ? '/pages-recheck.json' : '/pages.json'), JSON.stringify({ base, results, issues, errors }, null, 2))
  assert.deepEqual(errors, [])
  assert.deepEqual(issues, [])
} finally {
  await writeFile(output + (recheck ? '/pages-recheck.json' : '/pages.json'), JSON.stringify({ base, results, issues, errors }, null, 2))
  await browser.close()
}
