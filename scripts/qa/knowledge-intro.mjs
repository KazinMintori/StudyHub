import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'

const base = process.env.QA_URL || 'http://127.0.0.1:5188'
const route = process.env.QA_ROUTE || '/bieu-dien-tri-thuc/bai-giang/01-gioi-thieu-tac-tu/khai-niem-va-tac-tu.html'
const output = 'raw_materials/bieu-dien-tri-thuc/reviews/bai-01/browser'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true, executablePath: process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe' })
const errors = [], checks = []
try {
  const page = await browser.newPage()
  page.on('pageerror', error => errors.push(error.message))
  await page.evaluateOnNewDocument(() => {
    sessionStorage.setItem('studyhub_welcome_seen', '1')
    sessionStorage.setItem('studyhub:welcome-seen', '1')
  })
  const text = () => page.$eval('.decision-explanation', e => e.textContent)
  const finish = async () => {
    for (let i = 0; i < 20; i++) {
      if (await page.$eval('.simulation-controls button[aria-label="Tiến một bước"]', e => e.disabled)) return
      await page.click('.simulation-controls button[aria-label="Tiến một bước"]')
    }
    throw Error('Simulation did not terminate')
  }
  for (const width of [1280, 375, 360]) {
    await page.setViewport({ width, height: 900, deviceScaleFactor: 1 })
    await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 120000 })
    await page.waitForSelector('.agent-decision', { timeout: 60000 })
    await page.evaluate(() => document.fonts.ready)
    await page.evaluate(() => document.documentElement.classList.remove('dark'))
    await page.click('.editor-bar button')
    assert.match(await page.$eval('.editor-bar button', e => e.textContent), /Đã chép/)
    await finish()
    assert.match(await text(), /Đường ngắn|đường ngắn/)
    await page.click('.outcome-buttons button:nth-child(2)')
    assert.match(await page.$eval('.decision-outcome', e => e.textContent), /0 điểm/)
    checks.push(`${width}px: result can be adverse after the expected-utility decision`)
    for (const [preset, expected] of [[1, /đường vòng/], [2, /đường ngắn/], [3, /đường vòng/]]) {
      await page.click(`.decision-presets button:nth-child(${preset + 1})`)
      assert.match(await text(), /Chưa xét/)
      await finish()
      assert.match(await text(), expected)
    }
    checks.push(`${width}px: all four presets and reset on input change`)
    await page.click('.simulation-controls button[aria-label="Lùi một bước"]')
    assert.equal(await page.$('.decision-outcome'), null)
    await page.click('.simulation-controls button[aria-label="Tiến một bước"]')
    assert.match(await text(), /đường vòng/)
    await page.click('.decision-presets button:nth-child(1)')
    await page.focus('input[aria-label="Xác suất thuận lợi của đường ngắn"]')
    await page.keyboard.press('ArrowRight')
    assert.equal(await page.$eval('input[aria-label="Xác suất thuận lợi của đường ngắn"]', e => e.value), '81')
    assert.match(await text(), /Chưa xét/)
    const overflow = await page.evaluate(() => {
      const root = document.querySelector('.agent-decision')
      return { page: document.documentElement.scrollWidth > innerWidth + 1, lab: root.scrollWidth > root.clientWidth + 1,
        math: [...document.querySelectorAll('mjx-container')].filter(e => e.getBoundingClientRect().width > innerWidth).length }
    })
    assert.deepEqual(overflow, { page: false, lab: false, math: 0 })
    checks.push(`${width}px: keyboard input, backward/forward replay, no horizontal overflow`)
    await page.click('.decision-presets button:nth-child(1)')
    for (let i = 0; i < 4; i++) await page.click('.simulation-controls button[aria-label="Tiến một bước"]')
    await (await page.$('.agent-decision')).screenshot({ path: `${output}/lab-${width}.png` })
  }
  await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
  await page.reload({ waitUntil: 'networkidle0' })
  await page.waitForSelector('.motion-note')
  await page.click('.simulation-controls .play-toggle')
  await page.waitForFunction(() => document.querySelector('.simulation-controls .play-toggle')?.textContent.includes('Tạm dừng'))
  await page.click('.decision-presets button:nth-child(1)')
  assert.doesNotMatch(await page.$eval('.simulation-controls .play-toggle', e => e.textContent), /Tạm dừng/)
  checks.push('Reduced-motion preference and explicit play/pause controls')
  checks.push('Selecting a preset while playing pauses and resets the calculation')
  await page.evaluate(() => document.documentElement.classList.add('dark'))
  await (await page.$('.agent-decision')).screenshot({ path: `${output}/lab-dark-360.png` })
  checks.push('Light and dark visual evidence')
  if (process.env.QA_ALL === '1') {
    const parent = '/bieu-dien-tri-thuc/bai-giang/01-gioi-thieu-tac-tu'
    const slugs = ['dsa-va-bai-toan-ai', 'khai-niem-va-tac-tu', 'lich-su-va-nen-tang', 'ung-dung-va-ai-tao-sinh', 'muc-tieu-va-trach-nhiem', 'ban-do-mon-hoc-va-tu-hoc']
    await page.goto(`${base}${parent}.html`, { waitUntil: 'networkidle0', timeout: 120000 })
    await page.waitForSelector('.topic-map a')
    assert.equal(await page.$$eval('.topic-map a', links => links.length), 6)
    checks.push('Parent topic map contains the six intended topics')
    for (const width of [1280, 375, 360]) {
      await page.setViewport({ width, height: 900, deviceScaleFactor: 1 })
      for (const slug of slugs) {
        console.log(`Checking ${width}px ${slug}`)
        await page.goto(`${base}${parent}/${slug}.html`, { waitUntil: 'networkidle0', timeout: 120000 })
        await page.waitForSelector('h1', { timeout: 90000 })
        const result = await page.evaluate(() => ({
          overflow: document.documentElement.scrollWidth > innerWidth + 1,
          badMath: [...document.querySelectorAll('[data-mjx-error], mjx-merror')].length,
          rawTex: [...document.querySelectorAll('mjx-container')].filter(e => e.scrollWidth > e.clientWidth + 2).length,
          svg: [...document.querySelectorAll('.mermaid svg')].length
        }))
        assert.equal(result.overflow, false, `${slug} page overflow at ${width}`)
        assert.equal(result.badMath, 0, `${slug} MathJax error at ${width}`)
        assert.equal(result.rawTex, 0, `${slug} formula overflow at ${width}`)
        checks.push(`${width}px: ${slug} layout and math`)
        if (width === 375) await page.screenshot({ path: `${output}/${slug}-375.png`, fullPage: false })
      }
    }
  }
  assert.deepEqual(errors, [])
  await writeFile(`${output}/report.json`, JSON.stringify({ checks, errors }, null, 2) + '\n')
  console.log(`PASS ${checks.length} browser checks; no runtime errors.`)
} finally { await browser.close() }
