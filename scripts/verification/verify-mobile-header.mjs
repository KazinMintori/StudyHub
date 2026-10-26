import assert from 'node:assert/strict'
import puppeteer from 'puppeteer'
import { mkdir, writeFile } from 'node:fs/promises'

const base = (process.env.QA_URL || 'http://127.0.0.1:5173').replace(/\/$/, '')
const output = 'qa/mobile-header'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true }), page = await browser.newPage()
const results = [], errors = []
page.on('pageerror', error => errors.push({ url: page.url(), message: error.message }))
await page.evaluateOnNewDocument(() => { try { sessionStorage.setItem('studyhub_welcome_seen', '1') } catch {} })
const routes = [
  ['topic', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/duong-thang-va-tap-affine.html'],
  ['wiki', '/wiki/gradient.html'],
  ['workspace', '/goc-hoc-tap.html?mon=toan-cho-ai#simulation'],
  ['course', '/toan-cho-ai/']
]
const settle = () => page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))))
const headerMetrics = () => page.evaluate(() => {
  const rect = selector => {
    const element = document.querySelector(selector)
    if (!element || !element.checkVisibility()) return null
    const r = element.getBoundingClientRect(), style = getComputedStyle(element)
    return { top: r.top, bottom: r.bottom, left: r.left, right: r.right, height: r.height, position: style.position }
  }
  return {
    scrollY, width: document.documentElement.clientWidth,
    nav: rect('.VPNav'), local: rect('.VPLocalNav'),
    tools: rect('.study-tools-trigger'), menu: rect('.VPNavBarHamburger'),
    emptyLocalVisible: !!document.querySelector('.VPLocalNav.empty:not(.has-sidebar)')?.checkVisibility()
  }
})

try {
  for (const width of [360, 375, 768, 959]) {
    await page.setViewport({ width, height: 900, isMobile: true, hasTouch: true })
    for (const [name, route] of routes) {
      await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 60000 })
      await page.evaluate(() => document.fonts.ready)
      const samples = []
      for (const y of [0, 40, 56, 80, 160, 600, 580, 550, 160, 80, 40, 0]) {
        await page.evaluate(y => window.scrollTo({ top: y, behavior: 'instant' }), y)
        await settle()
        const metrics = await headerMetrics()
        assert.equal(metrics.nav.position, 'fixed', `${name}: header is fixed`)
        assert.equal(metrics.nav.top, 0, `${name}: header must not slide with scroll`)
        assert.equal(metrics.nav.height, 56, `${name}: header height stays stable`)
        assert(Math.abs(metrics.nav.right - width) <= 1, `${name}: header follows the screen, not overflowing Notes`)
        assert(metrics.menu && metrics.menu.right <= width && metrics.menu.top >= 0 && metrics.menu.bottom <= 56, `${name}: navigation remains on screen`)
        if (metrics.tools) assert(metrics.tools.left >= 0 && metrics.tools.right <= width && metrics.tools.top >= 0 && metrics.tools.bottom <= 56, `${name}: tools occupy the same header row`)
        if (metrics.local) assert.equal(metrics.local.top, 56, `${name}: local menu cannot overlap the header`)
        assert.equal(metrics.emptyLocalVisible, false, `${name}: no empty bar appears at a scroll threshold`)
        samples.push(metrics)
      }
      await page.evaluate(() => window.scrollTo({ top: 600, behavior: 'instant' }))
      await settle()
      await page.screenshot({ path: `${output}/fixed-${name}-${width}.png` })
      // A menu that scrolls away or shifts horizontally cannot be reopened here.
      await page.click('.VPNavBarHamburger')
      await page.waitForSelector('.VPNavScreen', { visible: true })
      const screen = await page.$eval('.VPNavScreen', element => { const r = element.getBoundingClientRect(); return { top: r.top, right: r.right } })
      assert.equal(screen.top, 56)
      assert(Math.abs(screen.right - width) <= 1)
      await page.click('.VPNavBarHamburger')
      await page.waitForSelector('.VPNavScreen', { hidden: true })
      results.push({ name, width, samples: samples.length, fixedHeader: true, menuAtScroll: true })
      console.log('PASS stable mobile header', width, name)
    }
  }

  // Exercise the native scrolling path, not only programmatic scroll positions.
  await page.setViewport({ width: 375, height: 812, isMobile: true, hasTouch: true })
  await page.goto(base + '/toan-cho-ai/', { waitUntil: 'networkidle0', timeout: 60000 })
  const client = await page.createCDPSession()
  await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }))
  await client.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: 150, y: 680 }] })
  for (const y of [620, 550, 480, 410, 340, 270]) {
    await client.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x: 150, y }] })
    await settle()
    assert.equal((await headerMetrics()).nav.top, 0)
  }
  await client.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] })
  await page.waitForFunction(() => scrollY > 150)
  const lowerY = await page.evaluate(() => scrollY)
  await client.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: 150, y: 240 }] })
  for (const y of [310, 380, 450, 520, 590, 660]) {
    await client.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x: 150, y }] })
    await settle()
    assert.equal((await headerMetrics()).nav.top, 0)
  }
  await client.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] })
  await page.waitForFunction(previous => scrollY < previous, {}, lowerY)
  results.push({ name: 'native-touch-scroll-both-directions', width: 375, fixedHeader: true })
  await page.click('.study-tools-trigger')
  await page.waitForSelector('.study-tools-panel', { visible: true })
  const toolsPanel = await page.$eval('.study-tools-panel', element => { const r = element.getBoundingClientRect(); return { top: r.top, bottom: r.bottom, left: r.left, right: r.right } })
  assert(toolsPanel.top >= 56 && toolsPanel.bottom <= 812 && toolsPanel.left >= 0 && toolsPanel.right <= 375, JSON.stringify(toolsPanel))
  await page.keyboard.press('Escape')
  await page.waitForSelector('.study-tools-panel', { hidden: true })
  results.push({ name: 'tools-panel-below-stable-header', width: 375, toolsPanel })
  await page.click('.VPLocalNav .menu')
  await page.waitForSelector('.VPSidebar.open')
  await page.keyboard.press('Escape')
  await page.waitForFunction(() => !document.querySelector('.VPSidebar.open'))
  results.push({ name: 'sidebar-opens-from-second-navigation-row', width: 375 })
  assert.deepEqual(errors, [])
  console.log(`PASS ${results.length} mobile header scenarios, zero runtime errors.`)
} finally {
  await writeFile(`${output}/results.json`, JSON.stringify({ results, errors }, null, 2))
  await browser.close()
}
