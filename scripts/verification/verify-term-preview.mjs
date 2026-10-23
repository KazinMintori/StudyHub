import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import puppeteer from 'puppeteer'

const base = process.env.QA_URL || 'http://127.0.0.1:5173'
const output = 'qa/term-preview'
const topic = '/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang/he-thieu-xac-dinh-va-giai-tich-ma-tran.html'
const results = []
const browser = await puppeteer.launch({ headless: true })
await mkdir(output, { recursive: true })

async function newPage(width = 768) {
  const page = await browser.newPage()
  await page.setViewport({ width, height: 700 })
  await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
  return page
}

async function ready(page) {
  await page.goto(base + topic, { waitUntil: 'domcontentloaded', timeout: 60000 })
  await page.waitForFunction(() => document.querySelector('#app')?.__vue_app__ && document.querySelector('button.study-term'))
}

async function open(page) {
  await page.$eval('button.study-term', element => element.click())
  await page.waitForSelector('.term-preview.is-pinned', { visible: true })
  await page.waitForFunction(() => document.activeElement?.classList.contains('term-preview-close'))
}

async function settled(page) {
  await page.waitForNetworkIdle({ idleTime: 250, timeout: 60000 })
  await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))))
}

try {
  for (const dismissal of ['Escape', 'outside click']) {
    const page = await newPage()
    let held
    await page.setRequestInterception(true)
    page.on('request', request => {
      if (request.url().includes('/features/wiki/services/concept-data.mjs')) held = request
      else request.continue()
    })
    await ready(page)
    const requested = page.waitForRequest(request => request.url().includes('/features/wiki/services/concept-data.mjs')).catch(() => null)
    await page.$eval('button.study-term', element => element.click())
    // The idle warm-up may already have intercepted the dictionary request.
    if (!held) await requested
    assert.ok(held, 'The initial concept dictionary download is deliberately pending')
    if (dismissal === 'Escape') await page.keyboard.press('Escape')
    else await page.$eval('.topic-header h1', element => element.click())
    await held.continue()
    await settled(page)
    assert.equal(await page.$('.term-preview'), null, `${dismissal} cancels the pending preview`)
    await open(page)
    assert.ok(await page.$('.term-preview.is-pinned'), 'A later request still opens after cancellation')
    results.push(`Slow initial download: ${dismissal} cancels opening; the next click works`)
    await page.close()
  }

  for (const width of [375, 768, 1440]) {
    const page = await newPage(width)
    await ready(page)
    for (const dismissal of width < 1200 ? ['scrim', 'close button', 'Escape'] : ['close button', 'Escape']) {
      await open(page)
      if (dismissal === 'scrim') await page.click('.term-preview-scrim', { offset: { x: 5, y: 5 } })
      else if (dismissal === 'close button') await page.click('.term-preview-close')
      else await page.keyboard.press('Escape')
      await page.waitForSelector('.term-preview', { hidden: true })
      assert.equal(await page.evaluate(() => document.activeElement === document.querySelector('button.study-term')), true,
        `${width}px: ${dismissal} returns focus to the term button`)
      results.push(`${width}px: ${dismissal} returns keyboard focus to the term`)
    }
    await page.close()
  }
  console.log(JSON.stringify({ passed: results.length, checks: results }, null, 2))
  await writeFile(`${output}/results.json`, JSON.stringify({ passed: results.length, checks: results }, null, 2))
} finally {
  await browser.close()
}
