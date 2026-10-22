import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import { wikiPeople, atlasConnections } from '../../src/features/wiki/data/atlas.mjs'

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:5191'
const out = process.env.QA_OUT_DIR || 'qa/wiki-expansion-20261022'
await mkdir(`${out}/screens`, { recursive: true })
const browser = await puppeteer.launch({ headless: true })
const page = await browser.newPage(), results = [], errors = []
page.on('pageerror', error => errors.push(error.message))
await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
async function go(path, width) {
  await page.setViewport({ width, height: 950 })
  await page.goto(base + path, { waitUntil: 'networkidle0', timeout: 90000 })
  await page.evaluate(() => document.fonts.ready)
}
async function geometry(label) {
  await page.evaluate(async () => {
    await Promise.all([...document.querySelectorAll('.vp-doc img')].map(img => {
      img.loading = 'eager'
      return img.decode().catch(() => {})
    }))
  })
  const issues = await page.evaluate(() => {
    const problems = []
    if (document.documentElement.scrollWidth > innerWidth + 1) problems.push({ type: 'page-overflow', width: document.documentElement.scrollWidth })
    document.querySelectorAll('.vp-doc mjx-container > svg, .wiki-entry-card mjx-container > svg').forEach(el => {
      if (el.closest('table')) return
      const r = el.getBoundingClientRect()
      if (r.width && (r.right > innerWidth + 1 || r.left < -1)) problems.push({ type: 'math-overflow', math: el.closest('mjx-container').textContent, right: r.right, left: r.left })
    })
    document.querySelectorAll('[data-mjx-error], mjx-merror, [data-mml-node=merror]').forEach(el => problems.push({ type: 'math-render-error', message: el.textContent }))
    document.querySelectorAll('.vp-doc img').forEach(el => { if (!el.complete || !el.naturalWidth) problems.push({ type: 'broken-image', src: el.getAttribute('src') }) })
    return problems
  })
  results.push({ label, issues })
  if (issues.length) console.log('ISSUES', label, JSON.stringify(issues))
}
try {
  for (const width of [320, 375, 768, 1440]) {
    await go('/wiki/', width)
    await page.waitForSelector('.wiki-entry-card')
    assert(await page.$eval('.wiki-filters input', el => el.getBoundingClientRect().top < innerHeight))
    await geometry(`index-${width}`)
    if (width === 1440 || width === 375) await page.screenshot({ path: `${out}/screens/wiki-index-${width}.png` })
    // All 16 result pages are checked on the narrowest supported width.
    if (width === 320) {
      let current = 1
      while (!await page.$eval('.wiki-pagination button:last-child', el => el.disabled)) {
        await page.click('.wiki-pagination button:last-child')
        await page.waitForFunction(n => document.querySelector('.wiki-result-count').textContent.includes(`Trang ${n} /`), {}, ++current)
        await geometry(`index-320-page-${current}`)
      }
      assert.equal(await page.$eval('.wiki-pagination button:last-child', el => el.disabled), true)
    }
    await page.click('.wiki-view-switch button:last-child')
    assert.equal(await page.$$eval('.wiki-person-card', els => els.length), wikiPeople.length)
    await geometry(`people-${width}`)
    if (width === 1440) await page.screenshot({ path: `${out}/screens/wiki-people-${width}.png` })
    await page.type('.wiki-filters input', 'shannon')
    assert.equal(await page.$$eval('.wiki-person-card', els => els.length), 1)
    await page.click('.wiki-view-switch button:first-child')
    await page.$eval('.wiki-filters input', el => { el.value = ''; el.dispatchEvent(new Event('input', { bubbles: true })) })
    await page.type('.wiki-filters input', 'tich vo huong')
    assert(await page.$$eval('.wiki-entry-card h3', els => els.some(el => el.textContent.includes('Tích vô hướng'))))
    await geometry(`search-${width}`)
  }
  for (const dark of [false, true]) {
    await go('/wiki/', 375)
    await page.evaluate(dark => document.documentElement.classList.toggle('dark', dark), dark)
    await geometry(`color-mode-${dark ? 'dark' : 'light'}`)
    await page.screenshot({ path: `${out}/screens/wiki-${dark ? 'dark' : 'light'}-375.png` })
  }
  const repaired = ['bat-dang-thuc-jensen', 'boi-giac-goc', 'cam-khang', 'cuong-do-buc-xa', 'dao-dong-tat-dan', 'he-so-cong-suat', 'hiep-phuong-sai', 'hoc-cong-huong-dien-tu', 'lagrangian', 'mien-kha-thi', 'noi-tuong-doi', 'phan-cuc-tron', 'phan-phoi-gauss', 'quang-trinh', 'quy-hoach-dong', 'song-dung-dien-tu', 'tan-sac', 'to-hop-loi']
  const paths = [...new Set([...Object.keys(atlasConnections), ...repaired])].map(id => `/wiki/${id}.html`)
  paths.push(...wikiPeople.map(person => `/wiki/nhan-vat/${person.id}.html`), '/toan-cho-ai/doc-them/loss-landscape-va-cuc-tieu-phang.html', '/xac-suat-thong-ke/bai-giang/20-sai-lech-do-thiet-ke.html')
  for (let i = 0; i < paths.length; i++) {
    await go(paths[i], 320)
    await page.evaluate(() => document.querySelectorAll('.vp-doc details').forEach(el => { el.open = true }))
    await geometry(paths[i])
    if (i % 5 === 0) console.log('Checked article', i + 1, '/', paths.length)
    if (i === 0 || paths[i].includes('shannon')) await page.screenshot({ path: `${out}/screens/article-${i}-320.png`, fullPage: true })
  }
  await go('/wiki/hessian.html', 320)
  await page.waitForSelector('.vp-doc img[role=button]')
  await page.focus('.vp-doc img[role=button]')
  await page.keyboard.press('Enter')
  await page.waitForSelector('.diagram-dialog[open]')
  const viewer = await page.evaluate(() => {
    const dialog = document.querySelector('.diagram-dialog'), media = dialog.querySelector('.diagram-scroll')
    return { dialog: dialog.getBoundingClientRect().toJSON(), media: media.getBoundingClientRect().toJSON() }
  })
  results.push({ label: 'figure-viewer-320', issues: viewer.media.bottom > viewer.dialog.bottom ? [{ type: 'viewer-overflow', ...viewer }] : [] })
  await page.screenshot({ path: `${out}/screens/wiki-figure-zoom-320.png` })
  await page.keyboard.press('Escape')
  assert(await page.evaluate(() => document.activeElement.matches('.vp-doc img[role=button]')))
} finally {
  await browser.close()
  const failures = results.filter(result => result.issues.length)
  await writeFile(`${out}/browser-results.json`, JSON.stringify({ checks: results.length, failures, errors, results }, null, 2))
  console.log(JSON.stringify({ checks: results.length, failures: failures.length, errors }, null, 2))
  if (failures.length || errors.length) process.exitCode = 1
}
