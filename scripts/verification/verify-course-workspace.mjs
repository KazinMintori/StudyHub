import assert from 'node:assert/strict'
import puppeteer from 'puppeteer'
import { mkdir, writeFile } from 'node:fs/promises'
import { courseCatalog } from '../../src/content/catalog.mjs'
const base = process.env.QA_URL || 'http://127.0.0.1:5173'
const output = 'qa/course-workspace'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true }), page = await browser.newPage()
const results = [], errors = []
page.on('pageerror', error => errors.push(error.message))
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
const go = async route => { await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 60000 }); await page.waitForFunction(() => !!document.querySelector('#app')?.__vue_app__) }
const clickTab = async tab => { await page.click(`.workspace-tabs a[href$="#${tab}"]`); await page.waitForFunction(tab => location.hash === `#${tab}` && document.getElementById(tab)?.checkVisibility(), {}, tab) }
const setNote = async text => {
  await page.waitForSelector('#notes textarea:not([disabled])')
  await page.$eval('#notes textarea', (el, text) => { el.value = text; el.dispatchEvent(new Event('input', { bubbles: true })) }, text)
}
const pass = name => { results.push(name); console.log('PASS', name) }
try {
  await page.setViewport({ width: 1440, height: 1000 })
  await go('/toan-cho-ai/')
  const courseLink = await page.$eval('.course-meta a[href*="goc-hoc-tap"]', el => el.getAttribute('href'))
  assert.equal(courseLink, '/goc-hoc-tap.html?mon=toan-cho-ai')
  await go(courseLink + '#notes')
  await page.waitForFunction(() => document.getElementById('workspace-course').value === 'toan-cho-ai')
  await setNote('Ghi chú riêng môn Toán')
  await page.waitForFunction(() => JSON.parse(localStorage.getItem('studyhub_note_toan-cho-ai')) === 'Ghi chú riêng môn Toán')
  await page.select('#workspace-course', 'dsa')
  await setNote('Ghi chú riêng môn Giải thuật')
  await page.waitForFunction(() => JSON.parse(localStorage.getItem('studyhub_note_dsa')) === 'Ghi chú riêng môn Giải thuật')
  await page.select('#workspace-course', 'toan-cho-ai')
  await page.waitForFunction(() => document.querySelector('#notes textarea').value === 'Ghi chú riêng môn Toán')
  assert.equal(new URL(page.url()).searchParams.get('mon'), 'toan-cho-ai')
  pass('Course entry links preserve the selected subject; notebooks remain isolated')

  await clickTab('plan')
  await page.type('#study-plan-draft', 'Tự giải bài về tập lồi')
  await page.click('.study-plan-form button')
  await page.waitForSelector('.study-plan-list li')
  await page.click('.study-plan-list input')
  await page.reload({ waitUntil: 'networkidle0' })
  await page.waitForFunction(() => document.querySelector('.study-plan-list input')?.checked)
  await page.select('#workspace-course', 'dsa')
  assert.equal(await page.$('.study-plan-list'), null)
  await page.select('#workspace-course', 'toan-cho-ai')
  await page.waitForSelector('.study-plan-list .is-complete')
  pass('Study tasks persist, keep completion and use a separate list for every course')

  await clickTab('flashcards')
  for (const course of courseCatalog) {
    await page.select('#workspace-course', course.id)
    await page.waitForFunction(name => document.querySelector('.flashcard-top span')?.textContent.trim() === name, {}, course.name)
    assert(await page.$('.flashcard-question'))
  }
  pass('All ten subjects have a nonempty course-specific flashcard deck')

  await page.select('#workspace-course', 'toan-cho-ai')
  await clickTab('simulation')
  assert((await page.$$('.workspace-simulation-grid > a')).length >= 3)
  assert.equal(await page.$('.field-simulation'), null)
  await page.click('.workspace-simulation-grid a[href*="mo-phong=affine"]')
  await page.waitForSelector('.workspace-lab-runner .lab-point-controls')
  assert.equal(new URL(page.url()).searchParams.get('mo-phong'), 'affine')
  await page.reload({ waitUntil: 'networkidle0' })
  await page.waitForSelector('.workspace-lab-runner .lab-point-controls')
  assert(await page.$eval('.workspace-lab-runner h3', el => el.textContent.includes('affine')))
  await page.select('#workspace-course', 'triet-hoc-mac-lenin')
  assert.equal(await page.$('.workspace-simulation-grid'), null)
  assert.match(await page.$eval('#simulation .empty-state', el => el.textContent), /chưa có mô phỏng riêng/)
  pass('Simulation directory filters subjects, opens a standalone lab and restores its shared URL')

  await clickTab('focus')
  await page.type('#workspace-focus-minutes', '17')
  await page.$eval('#workspace-focus-minutes', el => { el.value = '17'; el.dispatchEvent(new Event('input', { bubbles: true })) })
  await page.click('.workspace-duration-form button')
  await page.waitForFunction(() => document.querySelector('.timer-display').textContent.trim() === '17:00')
  pass('The workspace timer accepts a custom study duration')

  for (const width of [360, 375, 768]) {
    await page.setViewport({ width, height: 900 })
    for (const tab of ['notes', 'plan', 'flashcards', 'focus', 'simulation']) {
      await clickTab(tab)
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth), width, `${width}px ${tab}`)
    }
    await page.screenshot({ path: `${output}/workspace-${width}.png` })
  }
  pass('All five tools fit phone and tablet widths without horizontal overflow')
  assert.deepEqual(errors, [])
} finally {
  await writeFile(`${output}/results.json`, JSON.stringify({ results, errors }, null, 2))
  await browser.close()
}
