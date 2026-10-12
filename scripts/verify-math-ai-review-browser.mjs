import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import { mathAiReviewLesson as lesson } from '../docs/.vitepress/math-ai-review-course.mjs'

const base = process.env.QA_URL || 'http://127.0.0.1:5191'
const browser = await puppeteer.launch({ headless: true, executablePath: process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe' })
const page = await browser.newPage()
const errors = [], results = [], overflow = []
page.on('pageerror', error => errors.push(error.message))
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
await mkdir('qa/math-ai-review', { recursive: true })
async function go(path) {
  const response = await page.goto(base + path, { waitUntil: 'networkidle0', timeout: 60000 })
  if (response) assert.equal(response.status(), 200, path)
  await page.evaluate(() => document.fonts.ready)
}
async function inspect(label) {
  const issues = await page.evaluate(() => {
    document.querySelectorAll('.vp-doc details').forEach(element => { element.open = true })
    const nodes = [...document.querySelectorAll('.vp-doc mjx-container')]
    const math = nodes.filter(element => element.getBoundingClientRect().width > 0).flatMap(element => {
      const rect = element.getBoundingClientRect(), svg = element.querySelector('svg')?.getBoundingClientRect()
      const style = getComputedStyle(element)
      const problem = rect.right > innerWidth + 2 || rect.left < -2 || (svg && svg.width > rect.width + 2)
      const scroll = ['auto', 'scroll'].includes(style.overflowX) && element.scrollWidth > element.clientWidth + 1
      return problem || scroll ? [{ text: element.textContent.trim().slice(0, 160), width: rect.width, svg: svg?.width, left: rect.left, right: rect.right, scroll }] : []
    })
    return { math, documentOverflow: document.documentElement.scrollWidth > innerWidth + 2, errors: document.querySelectorAll('mjx-merror,[data-mml-node="merror"]').length }
  })
  assert.equal(issues.errors, 0, `${label}: math rendering error`)
  if (issues.math.length || issues.documentOverflow) overflow.push({ label, ...issues })
  results.push(label)
}
try {
  await page.setViewport({ width: 1440, height: 1000 })
  await go('/toan-cho-ai/')
  assert.equal(await page.$$eval('#bai-giang .lecture-row', elements => elements.length), 8)
  await page.click('.course-overview-tabs a[href="#on-luyen"]')
  await page.waitForSelector('#on-luyen .lecture-row')
  assert.deepEqual(await page.$$eval('#on-luyen .part-banner h2', elements => elements.map(element => element.textContent)), lesson.topicGroups.map(group => group.title))
  assert.equal(await page.$$eval('#on-luyen .lecture-row', elements => elements.length), 12)
  await page.screenshot({ path: 'qa/math-ai-review/overview-desktop.png', fullPage: true })
  await page.reload({ waitUntil: 'networkidle0' })
  assert(await page.$('#on-luyen'))
  await page.click('.course-overview-tabs a[href="#bai-giang"]')
  await page.waitForSelector('#bai-giang')
  await page.goBack({ waitUntil: 'networkidle0' })
  await page.waitForSelector('#on-luyen')
  await page.goForward({ waitUntil: 'networkidle0' })
  await page.waitForSelector('#bai-giang')
  results.push('Course tabs, direct link, reload and browser history')

  for (const width of (process.env.QA_SMOKE ? [375] : [360, 375, 1440])) {
    await page.setViewport({ width, height: 900 })
    await go('/toan-cho-ai/#on-luyen')
    await inspect(`overview-${width}`)
    if (width === 375) await page.screenshot({ path: 'qa/math-ai-review/overview-mobile.png', fullPage: true })
    for (const group of lesson.topicGroups) {
      for (const topic of group.topics) {
        if (process.env.QA_SMOKE && !['khong-gian-va-ma-tran', 'bai-tap-cos', 'gradient-backtracking-newton'].includes(topic.slug)) continue
        await go(`/toan-cho-ai/bai-giang/${lesson.slug}/${topic.slug}.html`)
        assert.equal(await page.$eval('.topic-header h1', element => element.textContent), topic.title)
        await inspect(`${width}/${topic.slug}`)
        if (width === 375 && ['mo-hinh-va-hoi-quy', 'bai-tap-cos', 'gradient-backtracking-newton'].includes(topic.slug)) {
          await page.screenshot({ path: `qa/math-ai-review/${topic.slug}-mobile.png`, fullPage: true })
        }
      }
    }
    await go(`/toan-cho-ai/bai-giang/${lesson.slug}.html`)
    for (const part of ['cheatsheet', 'kien-thuc-can-co', 'notes']) {
      await page.click(`.lecture-tabs a[href$="#${part}"]`)
      await page.waitForFunction(part => document.querySelector(`.lecture-tabs a[href$="#${part}"]`)?.getAttribute('aria-current') === 'page', {}, part)
      assert.equal(await page.$$eval('mjx-merror,[data-mml-node="merror"]', elements => elements.length), 0)
      assert.equal(await page.$eval('body', element => element.textContent.includes('$$')), false, `${part}: raw formula delimiters`)
      await inspect(`${width}/bundle-${part}`)
    }
  }
  assert.deepEqual(errors, [])
  await writeFile(`qa/math-ai-review/browser-results${process.env.QA_SMOKE ? '-built' : ''}.json`, JSON.stringify({ base, results, errors, overflow }, null, 2))
  console.log(JSON.stringify({ checks: results.length, errors, overflow }, null, 2))
  assert.equal(overflow.length, 0, 'Math or document overflow detected')
} finally {
  await browser.close()
}
