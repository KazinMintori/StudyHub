import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir } from 'node:fs/promises'

const base = process.env.QA_URL || 'http://127.0.0.1:5181'
const browser = await puppeteer.launch({ headless: true })
const errors = []
const paths = ['/', '/toan-cho-ai/', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html', '/wiki/gradient.html', '/goc-hoc-tap.html', '/guide/']
const focusState = element => {
  const style = getComputedStyle(element)
  return { active: document.activeElement === element, outline: style.outlineStyle }
}

try {
  await mkdir('qa/focus', { recursive: true })
  for (const theme of ['light', 'dark']) {
    for (const width of [1280, 375]) {
      const page = await browser.newPage()
      page.on('pageerror', error => errors.push(error.message))
      await page.setViewport({ width, height: 900 })
      await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: theme }, { name: 'prefers-reduced-motion', value: 'reduce' }])
      await page.evaluateOnNewDocument(theme => {
        localStorage.setItem('vitepress-theme-appearance', theme)
        sessionStorage.removeItem('studyhub_welcome_seen')
      }, theme)
      for (const path of paths) {
        // Reproduce first-visit welcome dismissal on every page with a heading.
        const response = await page.goto(base + path, { waitUntil: 'domcontentloaded', timeout: 120000 })
        assert([200, 304].includes(response.status()), path)
        await page.waitForSelector('.welcome-screen[open]')
        const heading = await page.$('main h1, .VPContent h1')
        assert(heading, path)
        const originalTabindex = await heading.evaluate(el => el.getAttribute('tabindex'))
        if (width === 375) await page.keyboard.press('Enter')
        else await page.click('.welcome-start')
        await page.waitForFunction(() => !document.querySelector('.welcome-screen[open]'))
        const state = await heading.evaluate(focusState)
        assert(state.active, `${path}: welcome restores reading focus`)
        assert.equal(state.outline, 'none', `${path}: heading has no automatic rectangle`)
        if (path === '/') await page.screenshot({ path: `qa/focus/after-${theme}-${width}.png` })

        // A keyboard user still sees the branded focus indicator on real controls.
        await page.keyboard.press('Tab')
        const button = await page.$('.site-introduction-links button')
        await button.focus()
        const control = await button.evaluate(focusState)
        assert(control.active)
        assert.equal(control.outline, 'solid', `${path}: keyboard focus is visible`)
        assert(await button.evaluate(el => {
          const probe = document.createElement('span')
          probe.style.color = 'var(--tim)'
          el.append(probe)
          const match = getComputedStyle(probe).color === getComputedStyle(el).outlineColor
          probe.remove()
          return match
        }), `${path}: control uses theme focus color, not native black`)
        assert.equal(await heading.evaluate(el => el.getAttribute('tabindex')), originalTabindex, `${path}: original tabindex is preserved`)

        // Reopening from the footer returns focus to the invoking button.
        await page.keyboard.press('Enter')
        await page.waitForSelector('.welcome-screen[open]')
        await page.keyboard.press('Escape')
        await page.waitForFunction(() => !document.querySelector('.welcome-screen[open]'))
        assert(await button.evaluate(el => el === document.activeElement), `${path}: modal restores invoking control`)

        // Skip-to-content must keep navigation focus without framing the whole page.
        await page.$eval('.VPSkipLink', el => el.focus())
        await page.keyboard.press('Enter')
        const content = await page.$eval('#VPContent', focusState)
        assert(content.active, `${path}: skip link focuses content`)
        assert.equal(content.outline, 'none', `${path}: skip target has no automatic rectangle`)
        console.log(`PASS ${theme} ${width}px ${path}: welcome, keyboard controls, modal restore, skip link`)
      }
      await page.close()
    }
  }
  assert.deepEqual(errors, [])
  console.log('All focus regression checks passed.')
} finally {
  await browser.close()
}
