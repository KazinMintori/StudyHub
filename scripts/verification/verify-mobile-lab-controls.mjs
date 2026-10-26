import assert from 'node:assert/strict'
import puppeteer from 'puppeteer'
import { mkdir, writeFile } from 'node:fs/promises'

const base = (process.env.QA_URL || 'http://127.0.0.1:5173').replace(/\/$/, '')
const output = 'qa/mobile-lab-controls'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true }), page = await browser.newPage()
const results = [], errors = []
page.on('pageerror', error => errors.push(error.message))
await page.evaluateOnNewDocument(() => { try { sessionStorage.setItem('studyhub_welcome_seen', '1') } catch {} })
await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
const record = name => { results.push(name); console.log('PASS', name) }
const go = async route => {
  await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 60000 })
  await page.waitForSelector('.lab-point-controls', { visible: true })
  await page.evaluate(() => document.fonts.ready)
}
const tap = async element => {
  await element.evaluate(el => el.scrollIntoView({ block: 'center', behavior: 'instant' }))
  await element.tap()
}
const simulation = id => `/goc-hoc-tap.html?mon=toan-cho-ai&mo-phong=${id}#simulation`
const point = async (lab, index = 0) => lab.$$eval('svg .lab-handle', (handles, index) => ({ x: Number(handles[index].getAttribute('cx')), y: Number(handles[index].getAttribute('cy')) }), index)

try {
  await page.setViewport({ width: 375, height: 800, isMobile: true, hasTouch: true })
  await go(simulation('affine'))
  const affine = await page.$('.study-lab')
  assert.equal(await affine.$$eval('.lab-point-options option', options => options.length), 2)
  const before = await point(affine)
  await tap(await affine.$('[aria-label="Dịch điểm sang phải"]'))
  await page.waitForFunction((before) => Number(document.querySelector('.study-lab .lab-handle').getAttribute('cx')) > before, {}, before.x)
  const after = await point(affine)
  assert(after.x > before.x)
  assert.equal(after.y, before.y)
  await tap(await affine.$('.lab-point-step input'))
  await tap(await affine.$('[aria-label="Dịch điểm sang phải"]'))
  const fast = await point(affine)
  assert(Math.abs((fast.x - after.x) / (after.x - before.x) - 5) < 1e-8)
  record('Touch direction buttons and the faster step move the selected affine point')

  await (await affine.$('.lab-point-options select')).select('1')
  const otherBefore = await point(affine, 1)
  await tap(await affine.$('[aria-label="Dịch điểm lên trên"]'))
  const otherAfter = await point(affine, 1)
  assert(otherAfter.y < otherBefore.y)
  assert.deepEqual(await point(affine), fast)
  record('The point picker moves another point without changing the first point')

  const metrics = await page.$$eval('.lab-point-controls', controls => controls.map(control => ({
    right: control.getBoundingClientRect().right,
    left: control.getBoundingClientRect().left,
    buttons: [...control.querySelectorAll('.lab-point-directions button')].map(button => ({ width: button.getBoundingClientRect().width, height: button.getBoundingClientRect().height }))
  })))
  assert(metrics.every(control => control.left >= 0 && control.right <= 375 && control.buttons.every(button => button.width >= 44 && button.height >= 44)))
  assert(await affine.$eval('svg', svg => getComputedStyle(svg).touchAction.includes('pan-y')))
  await affine.screenshot({ path: `${output}/affine-375.png` })
  record('Mobile controls have touch targets of at least 44px and fit the viewport')

  const canvas = await affine.$(':scope > svg')
  await canvas.evaluate(el => window.scrollTo({ top: window.scrollY + el.getBoundingClientRect().top - 180, behavior: 'instant' }))
  const canvasRect = await canvas.boundingBox()
  const scrollBefore = await page.evaluate(() => scrollY)
  const client = await page.createCDPSession()
  const x = canvasRect.x + 20, y = canvasRect.y + Math.min(160, canvasRect.height - 15)
  await client.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x, y }] })
  await client.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x, y: y - 100 }] })
  await client.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] })
  await page.waitForFunction(previous => scrollY > previous + 20, { timeout: 5000 }, scrollBefore)
  await client.detach()
  record('Swiping the empty simulation canvas scrolls the page instead of trapping the gesture')

  await go(simulation('lifeguard'))
  const lifeguard = await page.$('.study-lab')
  assert(await lifeguard.$eval('[aria-label="Dịch điểm lên trên"]', button => button.disabled))
  const readoutBefore = await lifeguard.$eval('.lab-point-readout', el => el.textContent)
  await tap(await lifeguard.$('[aria-label="Dịch điểm sang phải"]'))
  await page.waitForFunction(previous => document.querySelector('.lab-point-readout')?.textContent !== previous, {}, readoutBefore)
  const lifeguardAfter = await point(lifeguard)
  assert(lifeguardAfter.x > 0)
  await lifeguard.screenshot({ path: `${output}/lifeguard-375.png` })
  record('One-dimensional controls keep the shore constraint and update their position readout')

  await page.setViewport({ width: 1440, height: 900, isMobile: false, hasTouch: false })
  await go(simulation('affine'))
  await page.$eval('.study-lab .lab-handle', el => el.focus())
  const keyboardBefore = await page.$eval('.study-lab .lab-handle', el => Number(el.getAttribute('cx')))
  await page.keyboard.press('ArrowRight')
  const keyboardAfter = await page.$eval('.study-lab .lab-handle', el => Number(el.getAttribute('cx')))
  assert(keyboardAfter > keyboardBefore)
  await page.$eval('.study-lab .lab-handle', el => el.scrollIntoView({ block: 'center', behavior: 'instant' }))
  const handle = await page.$('.study-lab .lab-handle'), bounds = await handle.boundingBox()
  const dragBefore = await page.$eval('.study-lab .lab-handle', el => Number(el.getAttribute('cx')))
  await page.mouse.move(bounds.x + bounds.width / 2, bounds.y + bounds.height / 2)
  await page.mouse.down()
  await page.mouse.move(bounds.x + bounds.width / 2 + 30, bounds.y + bounds.height / 2, { steps: 3 })
  await page.mouse.up()
  assert(await page.$eval('.study-lab .lab-handle', el => Number(el.getAttribute('cx'))) > dragBefore)
  await page.screenshot({ path: `${output}/desktop.png`, fullPage: false })
  record('The original keyboard and mouse dragging operations still work on desktop')
  assert.deepEqual(errors, [])
  console.log(`PASS ${results.length} mobile simulation checks, zero runtime errors.`)
} finally {
  await writeFile(`${output}/results.json`, JSON.stringify({ results, errors }, null, 2))
  await browser.close()
}
