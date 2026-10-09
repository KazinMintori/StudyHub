import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile, unlink } from 'node:fs/promises'
import { electricField, fieldLines } from '../docs/.vitepress/theme/electric-field.mjs'

// Run with npm run dev in another terminal; QA_URL can use a different dev port.
// Run this before the production build so its temporary page stays out of the build.
const base = process.env.QA_URL || 'http://127.0.0.1:5173'
const output = 'qa/simulations'
await mkdir(output, { recursive: true })
// The gradient component is currently documented but not embedded in a lesson.
// Exercise it on a temporary dev page and remove that page after the run.
const fixture = `simulation-qa-${Date.now()}`
let fixtureCreated = false
const positive = [{ x: 230, y: 180, q: 1 }]
assert(electricField(positive, 370, 180).ex > 0)
assert(electricField([{ ...positive[0], q: -1 }], 370, 180).ex < 0)
assert.equal(electricField([...positive, { x: 510, y: 180, q: 1 }], 370, 180).magnitude, 0)
assert(electricField([...positive, { x: 510, y: 180, q: -1 }], 370, 180).ex > 0)
assert.deepEqual(fieldLines([]), [])
for (const charges of [positive, [{ ...positive[0], q: -1 }], [...positive, { x: 510, y: 180, q: -1 }]]) {
  const lines = fieldLines(charges)
  assert(lines.length > 0)
  assert(lines.every(line => !/NaN|Infinity/.test(line)))
  for (const line of lines) {
    const [a, b] = line.match(/[-\d.]+,[-\d.]+/g).slice(0, 2).map(p => p.split(',').map(Number))
    const field = electricField(charges, ...a)
    assert((b[0] - a[0]) * field.ex + (b[1] - a[1]) * field.ey > 0, 'Field line must follow E')
  }
}

const browser = await puppeteer.launch({ headless: true })
const page = await browser.newPage(), errors = []
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
page.on('pageerror', e => errors.push(e.message))
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms))
const go = async path => {
  await page.goto(base + path, { waitUntil: 'networkidle0' })
}
const click = async (selector, text) => {
  await page.$eval(selector, (root, text) => {
    const button = [...root.querySelectorAll('button')].find(b => b.textContent.trim() === text)
    if (!button || button.disabled) throw Error(`Unavailable button: ${text}`)
    button.click()
  }, text)
}
const step = () => page.$eval('.simulation-controls input', el => Number(el.value))
const setInput = (selector, value) => page.$eval(selector, (el, value) => {
  el.value = value; el.dispatchEvent(new Event('input', { bubbles: true }))
}, String(value))
const showControls = async () => {
  await page.locator('.simulation-controls').scroll()
  await sleep(150)
}
try {
  await writeFile(`docs/${fixture}.md`, '<CodeIllustration type="gradient" />\n', { flag: 'wx' })
  fixtureCreated = true
  await page.setViewport({ width: 1280, height: 900 })
  await go('/bieu-dien-tri-thuc/bai-giang/02-tim-kiem-mu.html')
  await showControls()
  assert.equal(await step(), 0, 'No autoplay on mount')
  await click('.simulation-controls', 'Tiếp →')
  assert.equal(await step(), 1)
  assert.equal(await page.$eval('circle.current + text', el => el.textContent), 'A')
  await click('.simulation-controls', '← Lùi')
  assert.equal(await step(), 0)
  await page.select('.playback-speed select', '2')
  await click('.simulation-controls', 'Phát')
  await page.waitForFunction(() => document.querySelector('.simulation-controls input').value >= 2)
  await click('.simulation-controls', 'Tạm dừng')
  const paused = await step(); await sleep(650); assert.equal(await step(), paused)
  await page.select('.illustration-toolbar select', 'dfs')
  assert.equal(await step(), 0, 'Changing algorithm resets playback')
  await click('.simulation-controls', 'Phát')
  await page.waitForFunction(() => document.querySelector('.simulation-controls input').value === '6')
  assert.equal(await page.$eval('.play-toggle', el => el.getAttribute('aria-pressed')), 'false')
  assert.match(await page.$eval('.trace-state', el => el.textContent), /A → B → D → E → C → F/)
  await click('.simulation-controls', 'Phát lại')
  await page.evaluate(() => scrollTo(0, 0))
  await page.waitForFunction(() => document.querySelector('.play-toggle').getAttribute('aria-pressed') === 'false')
  await showControls()
  const offscreen = await step(); await sleep(600); assert.equal(await step(), offscreen)
  console.log('PASS search: stepping, pause, speed, reset, finish, replay, offscreen pause')

  await go('/toan-cho-ai/bai-giang/bai-04-gradient-newton.html')
  await showControls()
  await page.select('.lab-inputs select', 'newton')
  await click('.simulation-controls', 'Tiếp →')
  assert.match(await page.$eval('.math-lab [role=status]', el => el.textContent), /\(0.0000, 0.0000\)/)
  assert.equal(await page.$eval('.active-marker', el => el.getAttribute('cx')), '190')
  await setInput('.simulation-controls input', 20)
  assert.equal(await step(), 20)
  await click('.simulation-controls', 'Phát lại')
  await page.select('.lab-inputs select', 'gd')
  assert.equal(await step(), 0)
  assert.equal(await page.$eval('.play-toggle', el => el.getAttribute('aria-pressed')), 'false')
  await page.screenshot({ path: `${output}/optimizer-desktop.png` })
  console.log('PASS optimizer: Newton result, seeking, reset on parameter change')

  await go(`/${fixture}.html`)
  await showControls()
  await setInput('.simulation-controls input', 4)
  assert.match(await page.$eval('.trace-state', el => el.textContent), /0.2592/)
  await setInput('.illustration-range input', 1.2)
  assert.equal(await step(), 0)
  await setInput('.simulation-controls input', 10)
  assert.equal(await page.$('.gradient-marker'), null, 'Out-of-range point must not remain on chart')
  assert(await page.$('.gradient-notice'))
  console.log('PASS gradient: current iterate values, divergence warning, parameter reset')

  await go('/toan-cho-ai/bai-giang/bai-07-quy-hoach-tuyen-tinh-va-dong.html')
  await showControls()
  await setInput('.simulation-controls input', 3)
  assert.match(await page.$eval('.math-lab:last-of-type [role=status]', el => el.textContent), /V\(S\)=4/)
  await page.select('.math-lab:last-of-type select', 'true')
  assert.equal(await step(), 0)
  await setInput('.simulation-controls input', 3)
  assert.match(await page.$eval('.math-lab:last-of-type [role=status]', el => el.textContent), /V\(S\)=6/)
  console.log('PASS Bellman: min/max values and reset')

  await go('/giai-thuat-du-lieu/bai-giang/bai-02-mapreduce-va-xu-ly-du-lieu-lon.html')
  await showControls()
  await setInput('.simulation-controls input', 2)
  assert.match(await page.$eval('.map-output', el => el.textContent), /uet: 2/)
  await setInput('.map-input input', '')
  assert.equal(await step(), 0)
  assert.equal(await page.$eval('.play-toggle', el => el.disabled), true)
  console.log('PASS MapReduce: counts, input reset, empty input')

  await go('/goc-hoc-tap#simulation')
  await page.locator('.field-canvas').scroll()
  await sleep(150)
  const initialLines = await page.$$eval('.field-lines .field-flow', els => els.length)
  assert(initialLines > 0)
  await click('.field-display-options', 'Chạy chỉ báo chiều')
  assert.equal(await page.$eval('.field-flow', el => getComputedStyle(el).animationPlayState), 'running')
  await click('.field-display-options', 'Tạm dừng')
  const position = await page.$eval('.charge-positive', el => {
    const p = el.ownerSVGElement.createSVGPoint(); p.x = +el.getAttribute('cx'); p.y = +el.getAttribute('cy')
    const point = p.matrixTransform(el.getScreenCTM()); return { x: point.x, y: point.y }
  })
  await page.mouse.move(position.x, position.y); await page.mouse.down()
  await page.mouse.move(position.x + 35, position.y - 20, { steps: 5 }); await page.mouse.up()
  assert.notEqual(await page.$eval('.charge-positive', el => el.getAttribute('cx')), '230')
  assert.equal(await page.$$eval('.field-charge', els => els.length), 2, 'Dragging must not add a charge')
  await page.locator('.charge-editor').scroll()
  await setInput('.charge-editor input', 270)
  assert.equal(await page.$eval('.charge-positive', el => el.getAttribute('cx')), '270')
  await page.select('.field-preset select', 'positive')
  assert.equal(await page.$$eval('.field-charge', els => els.length), 1)
  await click('.field-simulation', 'Xóa tất cả')
  assert.equal(await page.$$eval('.field-lines path', els => els.length), 0)
  await click('.field-simulation', 'Thêm ở giữa')
  assert.equal(await page.$$eval('.field-charge', els => els.length), 1)
  await page.select('.field-preset select', 'dipole')
  await page.locator('.field-canvas').scroll()
  await page.screenshot({ path: `${output}/field-desktop.png` })
  await click('.field-display-options', 'Chạy chỉ báo chiều')
  await page.$eval('.workspace-tabs a', a => a.click())
  await page.waitForFunction(() => document.querySelector('.field-display-options button').getAttribute('aria-pressed') === 'false')
  console.log('PASS field: motion, drag, keyboard inputs, presets, clear, hidden-tab pause')

  for (const width of [375, 768, 1280, 1920]) for (const mode of ['light', 'dark']) {
    await page.setViewport({ width, height: 900 })
    await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }, { name: 'prefers-color-scheme', value: mode }])
    await page.evaluateOnNewDocument(mode => localStorage.setItem('vitepress-theme-appearance', mode), mode)
    for (const [name, path, selector] of [
      ['search', '/bieu-dien-tri-thuc/bai-giang/02-tim-kiem-mu.html', '.simulation-controls'],
      ['optimizer', '/toan-cho-ai/bai-giang/bai-04-gradient-newton.html', '.simulation-controls'],
      ['field', '/goc-hoc-tap#simulation', '.field-canvas']
    ]) {
      await go(path); await page.locator(selector).scroll(); await sleep(100)
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `${name}: overflow at ${width}`)
      if (name === 'field') {
        assert.equal(await page.$eval('.field-flow', el => getComputedStyle(el).animationName), 'none')
        assert.equal(await page.$eval('.field-display-options button', el => el.disabled), true)
      } else {
        assert(await page.$('.motion-note'))
        assert.equal(await page.$eval(name === 'optimizer' ? '.active-marker' : '.code-illustration circle', el => getComputedStyle(el).transitionDuration), '0s')
      }
      await page.screenshot({ path: `${output}/${name}-${width}-${mode}.png` })
    }
  }
  assert.deepEqual(errors, [])
  console.log('PASS responsive/light/dark/reduced motion: 24 combinations; no browser errors')
} finally {
  try { await browser.close() } finally { if (fixtureCreated) await unlink(`docs/${fixture}.md`) }
}
