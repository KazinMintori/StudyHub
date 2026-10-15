import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import { courseCatalog } from '../../src/content/catalog.mjs'

const base = process.env.QA_URL || 'http://127.0.0.1:5173'
const output = 'qa/refactor'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true })
const page = await browser.newPage()
const results = [], errors = []
page.on('pageerror', error => { errors.push(error.message); console.error('Browser runtime error:', error.message) })
page.on('response', response => {
  if (response.status() >= 400 && response.url().startsWith(base) && /\.(js|css|woff2?)(?:\?|$)/.test(response.url())) {
    errors.push(`Failed asset ${response.status()}: ${response.url()}`)
  }
})
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
const go = async path => {
  const response = await page.goto(base + path, { waitUntil: 'networkidle0', timeout: 120000 })
  assert(response && (response.ok() || response.status() === 304), `Route failed: ${path} (${response?.status() ?? 'no HTTP response'})`)
  await page.waitForFunction(() => !!document.querySelector('#app')?.__vue_app__, { timeout: 60000 })
  const courseOverview = courseCatalog.some(course => path === `/${course.id}/`)
  if (courseOverview) await page.waitForSelector('.course-overview .lecture-row', { timeout: 60000 })
  if (path.startsWith('/goc-hoc-tap')) await page.waitForSelector('.study-workspace', { timeout: 60000 })
  if (path === '/') await page.waitForSelector('.study-home .course-row', { timeout: 60000 })
  await page.evaluate(() => document.fonts.ready)
}
async function check(name, action) { await action(); results.push(name); console.log('PASS', name) }
async function clickText(selector, text) {
  assert(await page.evaluate((selector, text) => {
    const target = [...document.querySelectorAll(selector)].find(element => element.textContent.trim() === text)
    target?.click(); return !!target
  }, selector, text), `Missing control: ${text}`)
}
const lecture = '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html'
try {
  await page.setViewport({ width: 1440, height: 900 })
  await go('/')
  await check('All current courses and Vietnamese filtering are preserved', async () => {
    assert.equal(await page.$$eval('.course-row', rows => rows.length), courseCatalog.length)
    await page.type('.course-search input', 'xu ly du lieu')
    await page.waitForFunction(() => document.querySelectorAll('.course-row').length === 1)
    assert.equal(await page.$$eval('.course-row', rows => rows.length), 1)
  })
  for (const course of courseCatalog) {
    await go(`/${course.id}/`)
    await check(`${course.id}: Course ordering and destinations`, async () => {
      const destinations = await page.$$eval('.lecture-list .lecture-row', rows => rows.map(row => row.getAttribute('href')))
      const expected = (course.parts || [{ lessons: course.lessons.map(l => l.slug) }]).flatMap(part => part.lessons).filter(slug => course.lessons.some(l => l.slug === slug))
      assert.deepEqual(destinations, expected.map(slug => `/${course.id}/bai-giang/${slug}.html`))
    })
  }
  await go(lecture + '#notes')
  await check('Desktop sidebar collapse and expand preserve accessibility state', async () => {
    await page.waitForSelector('.course-sidebar-toggle')
    await page.click('.course-sidebar-toggle')
    await page.waitForFunction(() => document.querySelector('.Layout').classList.contains('sidebar-collapsed'))
    assert.equal(await page.$eval('.course-sidebar-toggle', el => el.getAttribute('aria-expanded')), 'false')
    await page.click('.course-sidebar-toggle')
    await page.waitForFunction(() => !document.querySelector('.Layout').classList.contains('sidebar-collapsed'))
  })
  await check('DefaultTheme light and dark appearance still works', async () => {
    const before = await page.$eval('html', el => el.classList.contains('dark'))
    await page.click('.VPNavBarAppearance button')
    await page.waitForFunction(before => document.documentElement.classList.contains('dark') !== before, {}, before)
    await page.click('.VPNavBarAppearance button')
  })
  await check('Lecture tabs retain hash navigation and foundations', async () => {
    for (const part of ['slides', 'cheatsheet', 'kien-thuc-can-co', 'notes']) {
      await page.click(`.lecture-tabs a[href$="#${part}"]`)
      await page.waitForFunction(part => location.hash === `#${part}` && !!document.querySelector(`.lecture-tabs a[href$="#${part}"][aria-current="page"]`), {}, part)
    }
  })
  await check('Bookmarks resolve into the existing resume link', async () => {
    const heading = await page.$eval('.main > .vp-doc h2[id]', el => { el.scrollIntoView(); return el.id })
    await page.waitForFunction(heading => JSON.parse(localStorage.getItem('studyhub_last_lesson'))?.heading === heading, {}, heading)
    await go('/')
    assert(await page.$eval('.resume-panel a', (el, heading) => el.getAttribute('href').endsWith('#' + heading), heading))
  })
  await check('Lazy registered Lab renders on its published topic route', async () => {
    await go('/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/bai-toan-toi-uu.html')
    await page.waitForSelector('.study-lab svg', { timeout: 60000 })
    assert.equal(await page.$$eval('.study-lab svg', nodes => nodes.length > 0), true)
  })
  await go('/goc-hoc-tap.html#notes')
  await check('Notebook saves, reloads and safely previews existing storage schema', async () => {
    await page.waitForSelector('#notes textarea:not([disabled])')
    const content = '# Kiểm tra refactor\n\n<script>throw new Error("unsafe")</script>'
    await page.$eval('#notes textarea', (el, content) => { el.value = content; el.dispatchEvent(new Event('input', { bubbles: true })) }, content)
    await page.waitForFunction(content => JSON.parse(localStorage.getItem('studyhub_note_general')) === content, {}, content)
    await page.reload({ waitUntil: 'networkidle0' })
    assert.equal(await page.$eval('#notes textarea', el => el.value), content)
    await clickText('#notes button', 'Xem trước')
    assert.equal(await page.$('.note-preview script'), null)
  })
  await check('Flashcard reviews persist under the original key', async () => {
    await page.click('.workspace-tabs a[href="#flashcards"]')
    await clickText('#flashcards button', 'Xem đáp án')
    await clickText('.flashcard-actions button', 'Đã nhớ')
    assert(await page.evaluate(() => Object.values(JSON.parse(localStorage.getItem('studyhub_flashcards'))).includes(true)))
  })
  await check('Running timer restores across reload and can pause/reset', async () => {
    await page.click('.workspace-tabs a[href="#focus"]')
    await clickText('#focus button', 'Bắt đầu')
    await page.waitForFunction(() => document.querySelector('.timer-display').textContent.trim() !== '25:00')
    await page.reload({ waitUntil: 'networkidle0' })
    assert(await page.evaluate(() => [...document.querySelectorAll('#focus button')].some(el => el.textContent.trim() === 'Tạm dừng')))
    await clickText('#focus button', 'Tạm dừng')
    await clickText('#focus button', 'Đặt lại')
    assert.equal(await page.$eval('.timer-display', el => el.textContent.trim()), '25:00')
  })
  await page.setViewport({ width: 375, height: 900 })
  await go(lecture + '#notes')
  await check('Mobile sidebar opens and closes with Escape', async () => {
    await page.click('.mobile-lecture-nav > button')
    await page.waitForSelector('.VPSidebar.open')
    await page.keyboard.press('Escape')
    await page.waitForFunction(() => !document.querySelector('.VPSidebar.open'))
  })
  await check('Mobile reading has no horizontal page overflow', async () => {
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1))
  })
  await page.screenshot({ path: `${output}/lecture-mobile.png`, fullPage: false })
  await page.setViewport({ width: 1440, height: 900 })
  await go('/wiki/gradient.html')
  await check('Wiki definitions and math remain available', async () => {
    assert(await page.$('mjx-container'))
    assert(await page.$('.wiki-usage-top'))
  })
  await check('Wiki popover pins, closes and restores focus on mobile', async () => {
    await page.setViewport({ width: 375, height: 900, isMobile: true, hasTouch: true })
    await go('/wiki/gradient.html')
    const button = await page.$('.vp-doc p button.study-term')
    assert(button)
    await button.evaluate(element => element.scrollIntoView({ block: 'center' }))
    await button.tap()
    await page.waitForSelector('.term-preview.is-pinned')
    assert(await page.$eval('.term-preview', el => {
      const rect = el.getBoundingClientRect()
      return rect.left >= 0 && rect.right <= innerWidth + 1
    }))
    await page.keyboard.press('Escape')
    await page.waitForFunction(() => !document.querySelector('.term-preview'))
    assert(await page.evaluate(() => document.activeElement?.matches('button.study-term')))
  })
  await check('Physics slides, exercises and formula rendering stay available', async () => {
    await page.setViewport({ width: 1440, height: 900, isMobile: false, hasTouch: false })
    await go('/vat-ly-2/bai-giang/09-cam-ung-dien-tu.html#slides')
    await page.waitForSelector('.course-slide')
    assert(await page.$('.course-slide mjx-container'))
    await page.click('.lecture-tabs a[href$="#bai-tap"]')
    await page.waitForFunction(() => document.querySelector('.lecture-tabs a[href$="#bai-tap"][aria-current="page"]'))
    assert(await page.$eval('.lecture-exercises-content', el => getComputedStyle(el).display !== 'none'))
    await page.click('.lecture-tabs a[href$="#notes"]')
    await page.waitForFunction(() => document.querySelector('.lecture-tabs a[href$="#notes"][aria-current="page"]'))
    const anchor = await page.evaluate(() => {
      const heading = document.createElement('h3')
      heading.id = 'refactor-percent-%-anchor'
      document.querySelector('.lecture-exercises-content').append(heading)
      location.hash = encodeURIComponent(heading.id)
      return heading.id
    })
    await page.waitForFunction(() => document.querySelector('.lecture-tabs a[href$="#bai-tap"][aria-current="page"]'))
    await page.evaluate(anchor => document.getElementById(anchor).remove(), anchor)
  })
  await check('Responsive sidebar clears the drawer after resizing to desktop', async () => {
    await page.setViewport({ width: 375, height: 900 })
    await go(lecture + '#notes')
    await page.click('.mobile-lecture-nav > button')
    await page.waitForSelector('.VPSidebar.open')
    await page.setViewport({ width: 1440, height: 900 })
    await page.waitForFunction(() => !document.querySelector('.VPSidebar.open'))
    assert.equal(await page.$eval('.course-sidebar-toggle', el => el.getAttribute('aria-expanded')), 'true')
  })
  await check('Mermaid redraws when the existing appearance switch changes', async () => {
    await go('/bieu-dien-tri-thuc/bai-giang/02-tim-kiem-mu.html')
    await page.waitForSelector('.mermaid svg', { timeout: 60000 })
    const before = await page.$eval('.mermaid svg', el => el.outerHTML)
    await page.click('.VPNavBarAppearance button')
    await page.waitForFunction(before => document.querySelector('.mermaid svg')?.outerHTML !== before, {}, before)
  })
  await page.screenshot({ path: `${output}/wiki-desktop.png`, fullPage: false })
  assert.deepEqual(errors, [])
  await writeFile(`${output}/behavior.json`, JSON.stringify({ results, errors }, null, 2))
  console.log(`PASS ${results.length} browser checks, zero runtime errors.`)
} finally { await browser.close() }
