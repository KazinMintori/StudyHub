import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'

await mkdir('qa', { recursive: true })
const browser = await puppeteer.launch({ headless: true })
const page = await browser.newPage()
const errors = [], results = []
page.on('pageerror', error => { errors.push(error.message); console.error('Browser error:', error.message) })
const base = process.env.QA_URL || 'http://127.0.0.1:5173'
async function check(name, fn) { await fn(); results.push(name); console.log(`PASS ${name}`) }
async function clickText(text) {
  const clicked = await page.evaluate(text => { const button = [...document.querySelectorAll('button, a')].find(el => el.textContent.trim() === text); button?.click(); return !!button }, text)
  assert(clicked, `Control not found: ${text}`)
}
async function go(path = '/') { await page.goto(base + path, { waitUntil: 'networkidle0', timeout: 120000 }); await page.waitForSelector('.study-home, .study-workspace, .lesson-actions', { timeout: 120000 }) }
try {
  await page.setViewport({ width: 1440, height: 1000, deviceScaleFactor: 1 })
  await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: 'light' }])
  await go()
  await check('Five courses and no decorative emoji', async () => {
    assert.equal(await page.$$eval('.course-row', rows => rows.length), 5)
    assert.equal(await page.$eval('main', el => /[\u2600-\u27bf\u{1f000}-\u{1faff}]/u.test(el.textContent)), false)
  })
  await page.screenshot({ path: 'qa/home-desktop.png', fullPage: true })
  await check('Course filter accepts Vietnamese without accents', async () => {
    await page.type('.course-search input', 'xu ly du lieu'); assert.equal(await page.$$eval('.course-row', rows => rows.length), 1)
    await page.$eval('.course-search input', el => { el.value = ''; el.dispatchEvent(new Event('input', { bubbles: true })) })
  })
  await check('Full-text lesson search opens and returns matches', async () => {
    await page.click('.DocSearch-Button'); await page.waitForSelector('.VPLocalSearchBox input')
    await page.type('.VPLocalSearchBox input', 'Minimax'); await page.waitForSelector('.VPLocalSearchBox .result', { timeout: 30000 })
    await page.keyboard.press('Escape'); await page.waitForFunction(() => !document.querySelector('.VPLocalSearchBox'))
  })
  await check('Timer runs, survives reload, pauses and resets', async () => {
    await clickText('Bắt đầu'); await new Promise(r => setTimeout(r, 1200)); assert.notEqual(await page.$eval('.timer-display', el => el.textContent), '25:00')
    await go(); assert(await page.evaluate(() => [...document.querySelectorAll('button')].some(b => b.textContent.trim() === 'Tạm dừng')))
    await clickText('Tạm dừng'); const paused = await page.$eval('.timer-display', el => el.textContent); await new Promise(r => setTimeout(r, 1100)); assert.equal(await page.$eval('.timer-display', el => el.textContent), paused)
    await clickText('Đặt lại'); assert.equal(await page.$eval('.timer-display', el => el.textContent), '25:00')
  })
  await check('Lesson renders math, diagrams and completion', async () => {
    await go('/bieu-dien-tri-thuc/02-tim-kiem-mu'); await page.waitForSelector('.mermaid svg', { timeout: 120000 }); assert(await page.$('mjx-container, .katex'))
    await clickText('Đánh dấu đã học'); assert(await page.$('.lesson-actions button[aria-pressed=true]'))
    await page.screenshot({ path: 'qa/lesson-desktop.png', fullPage: false })
    await page.click('.mermaid-zoom-btn'); await page.waitForSelector('dialog[open]'); await page.keyboard.press('Escape'); assert.equal(await page.$('dialog[open]'), null)
    await go(); assert.match(await page.$eval('.start-panel', el => el.textContent), /TIẾP TỤC HỌC/); assert.match(await page.$eval('.start-panel-footer', el => el.textContent), /1 bài/)
  })
  await go('/goc-hoc-tap#flashcards')
  await check('Flashcards reveal, rate and preserve subject progress', async () => {
    await page.select('#flashcards select', 'vat-ly-2'); assert.match(await page.$eval('.flashcard-question', el => el.textContent), /Dấu trừ/)
    await clickText('Xem đáp án'); assert(await page.$('.flashcard-answer')); await clickText('Đã nhớ'); assert.match(await page.$eval('.flashcard-progress', el => el.textContent), /1 \/ 3/)
    await go('/goc-hoc-tap#flashcards'); await page.select('#flashcards select', 'vat-ly-2'); assert.match(await page.$eval('.flashcard-progress', el => el.textContent), /1 \/ 3/)
  })
  await check('Markdown notes persist, preview escapes HTML, notebooks stay separate', async () => {
    await clickText('Ghi chú'); await page.waitForSelector('#notes textarea:not([disabled])')
    const content = '# Ghi chú thử\n\n**Kiến thức**\n\n<script>alert(1)</script>'
    await page.$eval('#notes textarea', (el, content) => { el.value = content; el.dispatchEvent(new Event('input', { bubbles: true })) }, content)
    await clickText('Xem trước'); assert.equal(await page.$eval('.note-preview strong', el => el.textContent), 'Kiến thức'); assert.equal(await page.$('.note-preview script'), null)
    await go('/goc-hoc-tap#notes'); assert.equal(await page.$eval('#notes textarea', el => el.value), content)
    await page.select('#notes select', 'xu-ly-du-lieu'); await page.waitForFunction(() => !document.querySelector('#notes textarea').disabled); assert.notEqual(await page.$eval('#notes textarea', el => el.value), content)
    await page.select('#notes select', 'general'); await page.waitForFunction(() => !document.querySelector('#notes textarea').disabled); assert.equal(await page.$eval('#notes textarea', el => el.value), content)
  })
  await check('Electric field responds to adding and removing charges', async () => {
    await clickText('Mô phỏng'); assert.equal(await page.$$eval('.field-canvas circle', els => els.length), 2)
    await clickText('Thêm ở giữa'); assert.equal(await page.$$eval('.field-canvas circle', els => els.length), 3)
    await clickText('Xóa tất cả'); assert.equal(await page.$$eval('.field-canvas circle', els => els.length), 0)
    await clickText('Điện tích âm (−)'); await page.click('.field-canvas'); assert.equal(await page.$$eval('.field-canvas circle', els => els.length), 1)
    await page.screenshot({ path: 'qa/simulation-desktop.png', fullPage: true })
  })
  for (const width of [375, 768, 1024, 1440]) {
    await page.setViewport({ width, height: 900, deviceScaleFactor: 1 })
    for (const path of ['/', '/goc-hoc-tap#notes', '/goc-hoc-tap#flashcards', '/goc-hoc-tap#simulation']) {
      await go(path)
      await check(`No horizontal overflow: ${width}px ${path}`, async () => assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)))
    }
    await go(); await page.screenshot({ path: `qa/home-${width}.png`, fullPage: true })
    if (width < 1200) {
      await check(`Responsive navigation opens: ${width}px`, async () => {
        await page.click('.VPNavBarHamburger'); await page.waitForSelector('.VPNavScreen'); assert(await page.$eval('.VPNavScreen', el => getComputedStyle(el).display !== 'none'))
        await page.click('.VPNavBarHamburger'); await page.waitForFunction(() => !document.querySelector('.VPNavScreen'))
      })
    }
  }
  await page.setViewport({ width: 1440, height: 1000 })
  await page.evaluate(() => { document.documentElement.classList.add('dark') })
  await page.screenshot({ path: 'qa/home-dark.png', fullPage: true })
  assert.deepEqual(errors, [])
  await writeFile('qa/results.json', JSON.stringify({ results, errors }, null, 2))
  console.log(`${results.length} checks passed; no browser runtime errors.`)
} finally { await browser.close() }
