import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir } from 'node:fs/promises'

const base = process.env.QA_URL || 'http://127.0.0.1:5173'
const output = 'qa/reading-navigation'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true, ignoreDefaultArgs: ['--hide-scrollbars'] })
const page = await browser.newPage()
const errors = []
page.on('pageerror', error => errors.push(error.message))
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
const lecture = '/xac-suat-thong-ke/bai-giang/01-hieu-the-gioi-bang-du-lieu.html'
const go = async path => {
  await page.goto(base + path, { waitUntil: 'networkidle0', timeout: 120000 })
  await page.waitForSelector('.reading-outline nav a')
}
const select = async part => {
  await page.click(`.lecture-tabs a[href$="#${part}"]`)
  await page.waitForFunction(part => document.querySelector(`.lecture-tabs a[href$="#${part}"]`)?.getAttribute('aria-current') === 'page', {}, part)
  await page.waitForFunction(() => !document.querySelector('.panel-loading'))
  await page.waitForFunction(() => window.scrollY < 2)
}
try {
  for (const width of [375, 768, 1280, 1920]) {
    await page.setViewport({ width, height: 900 })
    await go(lecture)
    await page.waitForSelector('.site-search-button', { visible: true })
    assert.notEqual(await page.$eval('html', el => getComputedStyle(el).scrollbarWidth), 'none')
    assert.equal(await page.$eval('html', el => el.scrollWidth <= el.clientWidth + 1), true, `Horizontal overflow at ${width}`)
    await page.evaluate(() => window.scrollTo({ top: document.body.scrollHeight, behavior: 'instant' }))
    await select('bai-tap')
    await page.waitForFunction(() => [...document.querySelectorAll('.reading-outline nav a')].some(a => document.getElementById(decodeURIComponent(a.hash.slice(1)))?.closest('.lecture-exercises-content')))
    await page.screenshot({ path: `${output}/exercises-${width}.png` })
    await page.evaluate(() => window.scrollTo({ top: document.body.scrollHeight, behavior: 'instant' }))
    await select('cheatsheet')
    await page.waitForFunction(() => !!document.querySelector('.reading-outline a[href^="#cheatsheet--"]'))
    const outline = width < 768 ? '.mobile-lecture-nav .reading-outline-dropdown' : width < 1280 ? '.tablet-reading-outline' : '.aside .reading-outline'
    if (width < 1280) await page.click(`${outline} summary`)
    assert.equal(await page.$eval('html', el => el.scrollWidth <= el.clientWidth + 1), true, `Outline causes overflow at ${width}`)
    const links = await page.$$(`${outline} nav a`)
    await links.at(-1).click()
    await page.waitForFunction(() => location.hash.startsWith('#cheatsheet--'))
    assert.equal(await page.$eval('.lecture-tabs a[href$="#cheatsheet"]', el => el.getAttribute('aria-current')), 'page')
    const saved = page.url()
    await page.reload({ waitUntil: 'networkidle0' })
    await page.waitForSelector('.lecture-cheatsheet')
    await page.waitForFunction(() => !!document.getElementById(decodeURIComponent(location.hash.slice(1))))
    assert.equal(page.url(), saved)
    await select('notes')
    await page.screenshot({ path: `${output}/notes-${width}.png` })
    await page.click('[aria-label="Đến cuối bài"]')
    await page.waitForFunction(() => window.scrollY > 100)
    await page.click('[aria-label="Về đầu bài"]')
    await page.waitForFunction(() => window.scrollY < 2)
    await page.click('.site-search-button')
    await page.waitForSelector('.site-search-dialog[open]')
    await page.type('#site-search-input', 'xac suat')
    await page.waitForSelector('.site-search-results a')
    assert.equal(await page.$eval('html', el => el.scrollWidth <= el.clientWidth + 1), true, `Search causes overflow at ${width}`)
    await page.keyboard.press('ArrowDown')
    assert.equal(await page.evaluate(() => document.activeElement.matches('.site-search-results a')), true)
    await page.screenshot({ path: `${output}/search-${width}.png` })
    await page.keyboard.press('Escape')
    await page.waitForFunction(() => !document.querySelector('.site-search-dialog').open)
    assert.equal(await page.evaluate(() => document.activeElement.matches('.site-search-button')), true)
    console.log(`PASS ${width}px: Search, scrollbar, tab reset, shared outline, deep link reload, quick jumps`)
  }
  await go(lecture + '#bai-tap')
  await page.waitForFunction(() => window.scrollY < 2)
  assert.equal(await page.$eval('.lecture-tabs a[href$="#bai-tap"]', el => el.getAttribute('aria-current')), 'page')
  console.log('PASS opening an exercise tab URL starts at the top')
  await go('/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html')
  await page.goto(base + '/goc-hoc-tap.html#notes', { waitUntil: 'networkidle0' })
  await page.waitForSelector('#workspace-course')
  assert.equal(await page.$eval('#workspace-course', el => [...el.options].some(option => option.value === 'all')), false)
  assert.equal(await page.$eval('#workspace-course', el => el.value), 'bieu-dien-tri-thuc')
  await page.select('#workspace-course', 'toan-cho-ai')
  assert.equal(new URL(page.url()).searchParams.get('mon'), 'toan-cho-ai')
  await page.reload({ waitUntil: 'networkidle0' })
  assert.equal(await page.$eval('#workspace-course', el => el.value), 'toan-cho-ai')
  await page.click('.workspace-tabs a[href$="#plan"]')
  await page.waitForFunction(() => location.hash === '#plan')
  assert.equal(await page.$eval('.workspace-tabs a[href$="#plan"]', el => el.getAttribute('aria-current')), 'page')
  console.log('PASS workspace: Only courses in the menu, default and selected course match, selection survives reload, tabs work')
  assert.deepEqual(errors, [])
} finally {
  await browser.close()
}
