import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import { courseCatalog } from '../../src/content/catalog.mjs'

const base = (process.env.QA_URL || 'http://127.0.0.1:5173').replace(/\/$/, '')
const basePath = new URL(base).pathname.replace(/\/$/, '')
const output = 'qa/navigation-stability'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true, ignoreDefaultArgs: ['--hide-scrollbars'] })
const errors = [], timings = [], results = []
let page
const delay = ms => new Promise(resolve => setTimeout(resolve, ms))
try {
  page = await browser.newPage()
  page.setDefaultTimeout(60000)
  page.on('pageerror', error => errors.push(error.message))
  let documents = 0
  page.on('request', request => { if (request.resourceType() === 'document' && request.frame() === page.mainFrame()) documents++ })
  await page.evaluateOnNewDocument(() => {
    sessionStorage.setItem('studyhub_welcome_seen', '1')
    window.navigationProbe = { id: Math.random(), scrolls: [], writes: 0 }
    const scroll = window.scrollTo.bind(window)
    window.scrollTo = (...args) => { window.navigationProbe.scrolls.push(args); return scroll(...args) }
    const write = Storage.prototype.setItem
    Storage.prototype.setItem = function(key, value) { if (key === 'studyhub_last_lesson') window.navigationProbe.writes++; return write.call(this, key, value) }
  })
  await page.setViewport({ width: 1280, height: 900 })
  await page.goto(base + '/', { waitUntil: 'networkidle0', timeout: 120000 })
  await page.waitForSelector('.study-home')
  const documentId = await page.evaluate(() => window.navigationProbe.id)
  const initialDocuments = documents
  async function clickLink(href) {
    await page.evaluate(href => {
      const anchor = [...document.querySelectorAll('a[href]')].find(anchor => anchor.getAttribute('href') === href)
      assertLink(anchor, href)
      function assertLink(anchor, href) { if (!anchor) throw Error('Missing existing link: ' + href); anchor.click() }
    }, basePath + href)
  }
  async function coursePage(course) {
    const start = performance.now()
    await clickLink(`/${course.id}/`)
    await page.waitForFunction(name => document.querySelector('.VPContent h1')?.textContent.trim() === name, {}, course.name)
    timings.push({ course: course.id, ms: Math.round(performance.now() - start) })
    assert.equal(await page.evaluate(() => window.navigationProbe.id), documentId)
    assert.equal(await page.evaluate(() => scrollY), 0)
  }
  for (const course of courseCatalog) await coursePage(course)
  assert.equal(documents, initialDocuments, 'Internal links must retain the current document')
  results.push('All ten course links commit without reloading the document')
  const lecture = '/xac-suat-thong-ke/bai-giang/01-hieu-the-gioi-bang-du-lieu.html'
  await coursePage(courseCatalog.find(course => course.id === 'xac-suat-thong-ke'))
  await clickLink(lecture)
  await page.waitForSelector('.shared-reading-outline .lecture-header')
  async function select(part, fromBottom = true) {
    await page.evaluate((part, fromBottom) => {
      if (fromBottom) scrollTo({ top: document.body.scrollHeight, behavior: 'instant' })
      window.navigationProbe.scrolls = []
      document.querySelector(`.lecture-tabs a[href$="#${part}"]`).click()
    }, part, fromBottom)
    await page.waitForFunction(part => document.querySelector(`.lecture-tabs a[href$="#${part}"][aria-current="page"]`) && scrollY < 2, {}, part)
    await page.waitForFunction(() => !document.querySelector('.panel-loading'))
    const calls = await page.evaluate(() => window.navigationProbe.scrolls)
    assert.equal(calls.length, 1, `Only one scroll owner for ${part}: ${JSON.stringify(calls)}`)
    assert.equal(calls[0][0].top, 0)
  }
  for (const width of [375, 768, 1280, 1920]) {
    await page.setViewport({ width, height: 900 })
    for (const part of ['bai-tap', 'cheatsheet', 'kien-thuc-can-co', 'notes']) await select(part)
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `Overflow at ${width}`)
    if (width === 375) assert(await page.evaluate(() => innerWidth - document.documentElement.clientWidth <= 4), 'Phone scrollbar must stay light and narrow')
    await page.screenshot({ path: `${output}/notes-${width}.png` })
  }
  results.push('Every lecture tab resets once at four viewport widths')
  await select('kien-thuc-can-co')
  await page.waitForSelector('.lecture-foundations h3[id]')
  const foundationId = await page.$eval('.lecture-foundations h3[id]', element => element.id)
  await page.waitForFunction(id => [...document.querySelectorAll('.reading-outline nav a')].some(anchor => decodeURIComponent(anchor.hash.slice(1)) === id), {}, foundationId)
  await page.evaluate(id => [...document.querySelectorAll('.reading-outline nav a')].find(anchor => decodeURIComponent(anchor.hash.slice(1)) === id).click(), foundationId)
  await page.waitForFunction(() => !!document.querySelector('.lecture-tabs a[href$="#kien-thuc-can-co"][aria-current="page"]'))
  await page.reload({ waitUntil: 'networkidle0' })
  await page.waitForSelector('.lecture-foundations h3[id]')
  assert.equal(await page.$eval('.lecture-tabs a[aria-current="page"]', anchor => anchor.hash), '#kien-thuc-can-co')
  results.push('Foundation heading links keep their panel after clicking and reloading')
  await select('notes')
  await page.evaluate(async () => {
    scrollTo({ top: 610, behavior: 'instant' })
    await new Promise(resolve => setTimeout(resolve, 250))
    window.navigationProbe.writes = 0
    for (let i = 0; i < 30; i++) { scrollTo({ top: 610 + i, behavior: 'instant' }); await new Promise(requestAnimationFrame) }
  })
  await delay(300)
  const writes = await page.evaluate(() => window.navigationProbe.writes)
  assert(writes <= 1, `Repeated writes within one heading: ${writes}`)
  results.push('Scrolling within one heading does not repeatedly write storage')
  await page.evaluate(() => scrollTo({ top: 900, behavior: 'instant' }))
  await delay(250)
  const savedY = await page.evaluate(() => scrollY)
  await select('cheatsheet', false)
  await page.goBack()
  await page.waitForFunction(y => location.hash === '#notes' && Math.abs(scrollY - y) < 3, {}, savedY)
  await page.goForward()
  await page.waitForFunction(() => location.hash === '#cheatsheet' && scrollY < 2)
  results.push('Back and Forward restore the tab and saved reading position')
  // A late resize or content mutation must not pull an actively scrolling reader.
  await select('notes')
  await page.mouse.wheel({ deltaY: 700 })
  await delay(250)
  const y = await page.evaluate(() => scrollY)
  await page.evaluate(() => { const marker = document.createElement('p'); marker.textContent = 'Navigation verification'; document.querySelector('.main > .vp-doc').append(marker) })
  await delay(400)
  assert(Math.abs(await page.evaluate(() => scrollY) - y) < 3)
  results.push('Late content updates preserve the reader position')
  await page.setViewport({ width: 375, height: 900 })
  await page.goto(base + '/triet-hoc-mac-lenin/bai-giang/chuong-1-triet-hoc-va-vai-tro/doi-tuong-chuc-nang-vai-tro.html', { waitUntil: 'networkidle0' })
  await page.waitForSelector('.philosophy-topic-practice')
  await page.evaluate(() => {
    scrollTo({ top: document.body.scrollHeight, behavior: 'instant' })
    window.navigationProbe.scrolls = []
    document.querySelector('.philosophy-topic-practice').click()
  })
  await page.waitForFunction(() => location.hash === '#bai-tap' && scrollY < 2 && document.querySelector('.philosophy-topic-tabs [aria-selected="true"]')?.textContent.trim() === 'Bài tập')
  assert.equal(await page.evaluate(() => window.navigationProbe.scrolls.length), 1)
  results.push('The Philosophy practice link uses the same single top reset as lecture tabs')
  assert.deepEqual(errors, [])
  await writeFile(`${output}/report.json`, JSON.stringify({ results, timings, writes, documents, errors }, null, 2))
  for (const result of results) console.log('PASS', result)
  console.log(JSON.stringify({ timings, writes, documents, runtimeErrors: errors.length }))
} catch (error) {
  const state = page ? await page.evaluate(() => ({ url: location.href, titles: [...document.querySelectorAll('h1')].map(element => element.textContent), text: document.querySelector('.VPContent')?.textContent.slice(0, 1000) })).catch(() => ({})) : {}
  const diagnostic = { message: error.message, errors, results, timings, ...state }
  console.error(JSON.stringify(diagnostic, null, 2))
  await writeFile(`${output}/failure.json`, JSON.stringify(diagnostic, null, 2))
  await page?.screenshot({ path: `${output}/failure.png` }).catch(() => {})
  throw error
} finally { await browser.close() }
