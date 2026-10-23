import assert from 'node:assert/strict'
import puppeteer from 'puppeteer'
import { mkdir, writeFile } from 'node:fs/promises'

const base = (process.env.QA_URL || 'http://127.0.0.1:5173').replace(/\/$/, '')
const output = process.env.QA_OUTPUT || 'qa/exam-usability'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true })
const page = await browser.newPage()
await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
const results = [], errors = []
page.on('pageerror', error => errors.push(error.message))
const record = name => { results.push(name); console.log('PASS', name) }
const route = '/xu-ly-du-lieu/on-thi/bai-01.html'
const go = async () => {
  await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 60000 })
  await page.waitForFunction(() => location.search.includes('cau=B1-001') && !!document.querySelector('.exam-choice__radio'))
}

try {
  await page.setViewport({ width: 1280, height: 900 })
  await go()
  const originalUrl = page.url()

  await page.click('.study-tools-trigger')
  await page.waitForFunction(() => document.activeElement?.classList.contains('study-tools-close'))
  await page.keyboard.press('ArrowRight')
  assert.equal(page.url(), originalUrl, 'the tools panel must not navigate the underlying exam')
  assert(await page.$('.study-tools-panel'))
  await page.keyboard.press('a')
  assert.equal(await page.$$eval('.exam-choice.is-selected', nodes => nodes.length), 0, 'a tools-panel key must not submit an answer')
  assert(await page.$eval('.study-tools-close', button => button === document.activeElement))
  await page.keyboard.press('Escape')
  await page.waitForFunction(() => !document.querySelector('.study-tools-panel'))
  record('Study tools keep focus and cannot navigate or answer the exam')

  await page.$eval('.exam-question__heading', heading => {
    heading.focus()
    heading.addEventListener('keydown', event => event.preventDefault(), { once: true })
  })
  await page.keyboard.press('ArrowRight')
  assert.equal(page.url(), originalUrl, 'already handled keys must not navigate the exam')
  await page.keyboard.press('ArrowRight')
  await page.waitForFunction(() => location.search.includes('cau=B1-002'))
  await page.keyboard.press('ArrowLeft')
  await page.waitForFunction(() => location.search.includes('cau=B1-001'))
  record('Exam arrow shortcuts work while respecting an already handled key')

  await page.focus('.exam-choice__radio')
  await page.keyboard.press('ArrowRight')
  assert.equal(page.url(), originalUrl)
  assert.equal(await page.$eval(':focus', input => input.value), 'B')
  await page.keyboard.press('Enter')
  assert.equal(await page.$eval('.exam-choice.is-selected input', input => input.value), 'B')
  await page.reload({ waitUntil: 'networkidle0' })
  await page.waitForFunction(() => document.querySelector('.exam-choice.is-selected input')?.value === 'B')
  record('Keyboard option navigation selects once and survives reload')

  await page.setViewport({ width: 360, height: 640 })
  await page.evaluate(() => window.scrollTo(0, 0))
  await page.click('.exam-jump-trigger')
  await page.waitForSelector('.exam-modal')
  await page.waitForFunction(() => document.documentElement.style.overflow === 'hidden')
  const before = await page.evaluate(() => scrollY)
  await page.mouse.move(8, 400)
  await page.mouse.wheel({ deltaY: 500 })
  // Wait for the browser's wheel processing without depending on arbitrary timing.
  await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))))
  assert.equal(await page.evaluate(() => scrollY), before, 'the modal backdrop must not scroll the page behind it')
  await page.focus('.exam-modal__cell:last-child')
  await page.keyboard.press('Tab')
  assert(await page.$eval('.exam-modal__close-btn', button => button === document.activeElement))
  await page.keyboard.press('Escape')
  await page.waitForFunction(() => !document.querySelector('.exam-modal') && document.documentElement.style.overflow !== 'hidden')
  assert(await page.$eval('.exam-jump-trigger', button => button === document.activeElement))
  await page.mouse.move(8, 400)
  await page.mouse.wheel({ deltaY: 300 })
  await page.waitForFunction(previous => scrollY > previous, {}, before)
  record('Question modal blocks background scroll, traps Tab, and restores Escape focus and scrolling')

  await page.evaluate(() => {
    window.scrollTo(0, 0)
    document.documentElement.style.overflow = 'clip'
  })
  await page.click('.exam-jump-trigger')
  await page.waitForSelector('.exam-modal')
  await page.click('.exam-modal__cell:nth-child(3)')
  await page.waitForFunction(() => location.search.includes('cau=B1-003') && !document.querySelector('.exam-modal'))
  assert.equal(await page.evaluate(() => document.documentElement.style.overflow), 'clip')
  await page.evaluate(() => { document.documentElement.style.overflow = '' })
  record('Jumping to a question restores the exact preexisting page overflow style')

  await page.click('.exam-jump-trigger')
  await page.waitForSelector('.exam-modal')
  await page.evaluate(() => document.querySelector('.exam-course-link').click())
  await page.waitForFunction(() => !document.querySelector('.exam-practice') && document.documentElement.style.overflow !== 'hidden')
  record('Leaving an exam with an open question modal releases the page scroll lock')

  assert.deepEqual(errors, [])
  console.log(`PASS ${results.length} exam browser checks, zero runtime errors.`)
} finally {
  await writeFile(`${output}/results.json`, JSON.stringify({ results, errors }, null, 2))
  await browser.close()
}
