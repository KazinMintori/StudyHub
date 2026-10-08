import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import puppeteer from 'puppeteer'
import { courseCatalog } from '../docs/.vitepress/course-catalog.mjs'
import { lectureSlides } from '../docs/.vitepress/lecture-model.mjs'

const base = process.env.QA_URL || 'http://127.0.0.1:5174'
const browser = await puppeteer.launch({ headless: true, ...(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {}) })
const page = await browser.newPage(), errors = [], results = []
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
page.on('pageerror', error => errors.push(error.message))
await mkdir('qa/math-format', { recursive: true })
async function go(path) {
  await page.goto(base + path, { waitUntil: 'networkidle0', timeout: 120000 })
  await page.waitForFunction(() => !document.querySelector('.lecture-header') || document.querySelector('.lecture-tabs a[aria-current]'))
}
async function rendered(context) {
  const raw = await page.$$eval('.math-text', elements => elements.filter(element => /\$|\\(?:frac|sqrt|nabla|begin|partial)\b/.test(element.textContent)).map(element => element.textContent))
  assert.deepEqual(raw, [], `${context}: raw TeX visible`)
  assert.equal(await page.$$eval('[data-mml-node="merror"], [data-mjx-error]', elements => elements.length), 0, `${context}: math error`)
}
async function theme(dark) {
  await page.evaluate(dark => document.documentElement.classList.toggle('dark', dark), dark)
}
try {
  await page.setViewport({ width: 1440, height: 1000 })
  let slides = 0
  for (const course of courseCatalog) for (const lesson of course.lessons) {
    const cards = lectureSlides(course, lesson)
    if (!cards.length) continue
    await go(`/${course.id}/bai-giang/${lesson.slug}.html#slides`)
    await page.waitForSelector('.course-slide')
    for (let index = 0; index < cards.length; index++) {
      await rendered(`${course.id}/${lesson.slug} slide ${index + 1}`)
      if (index + 1 < cards.length) {
        await page.click('.slide-controls button:last-child')
        await page.waitForFunction(title => document.querySelector('.course-slide h2')?.textContent === title, {}, cards[index + 1].title)
      }
      slides++
    }
  }
  results.push(`All ${slides} slide cards render without raw TeX or math errors`)
  console.log('PASS', results.at(-1))
  for (const width of [375, 768, 1440]) for (const dark of [false, true]) {
    await page.setViewport({ width, height: 1000 })
    await go('/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang.html#kien-thuc-can-co')
    await page.evaluate(dark => { document.documentElement.classList.toggle('dark', dark); document.querySelectorAll('.foundation-entry details').forEach(element => { element.open = true }) }, dark)
    await rendered(`foundations ${width}/${dark}`)
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1), false, 'page overflow')
    assert(await page.$('#nen-tang-ma-tran-psd .foundation-notation [data-mml-node="mtable"]'))
    assert(await page.$('#nen-tang-dao-ham-rieng [data-mml-node="mfrac"]'))
    const card = await page.$('#nen-tang-ma-tran-psd')
    const notation = await card.$('.foundation-notation')
    await notation.screenshot({ path: `qa/math-format/matrix-${width}-${dark ? 'dark' : 'light'}.png` })
    await go('/wiki/dao-ham-rieng.html')
    await theme(dark)
    await rendered('partial derivative Wiki')
    await page.$$eval('.vp-doc h2', headings => headings.find(heading => heading.textContent.startsWith('Ví dụ'))?.scrollIntoView({ block: 'center', behavior: 'instant' }))
    await page.screenshot({ path: `qa/math-format/derivative-${width}-${dark ? 'dark' : 'light'}.png` })
  }
  results.push('Matrices and derivative fractions at 375, 768 and 1440 px in light and dark themes')
  await page.setViewport({ width: 375, height: 1000 })
  await go('/xu-ly-du-lieu/bai-giang/bai-03-numpy.html')
  assert.match(await page.$eval('.numpy-broadcast', element => element.textContent), /ndim = 1/)
  assert.match(await page.$eval('.numpy-broadcast', element => element.textContent), /shape = \(2,\)/)
  const numpy = await page.$('.numpy-broadcast')
  await numpy.screenshot({ path: 'qa/math-format/numpy-mobile.png' })
  await page.$eval('.broadcast-math', element => { element.open = true })
  const matrix = await page.$('.broadcast-display math')
  assert(matrix, 'Broadcasting uses mathematical matrix notation')
  const broadcast = await page.$('.broadcast-display')
  await broadcast.screenshot({ path: 'qa/math-format/broadcast-mobile.png' })
  assert.deepEqual(await page.$$eval('.broadcast-display mtable', elements => elements.map(table => [table.querySelectorAll('mtr').length, table.querySelector('mtr').querySelectorAll('mtd').length])), [[3, 2], [3, 2], [3, 2]])
  const axis = await page.$eval('.broadcast-display math > mrow', row => {
    const boxes = [...row.children].filter(element => element.localName === 'mo' || element.localName === 'mrow').map(element => ({ kind: element.localName, text: element.textContent, rect: element.getBoundingClientRect().toJSON() }))
    return boxes.map(box => ({ kind: box.kind, text: box.text, center: box.rect.y + box.rect.height / 2 }))
  })
  assert.deepEqual(axis.filter(box => box.kind === 'mo').map(box => box.text), ['+', '='])
  const matrixCenter = axis.find(box => box.kind === 'mrow').center
  assert(axis.filter(box => box.kind === 'mo').every(box => Math.abs(box.center - matrixCenter) < 6), 'Operators must share the mathematical axis of the matrices')
  await page.$eval('.illustration-range input', input => { input.value = '-10'; input.dispatchEvent(new Event('input', { bubbles: true })) })
  await page.waitForSelector('.broadcast-display mtd mo')
  assert(await page.$('.broadcast-display mtd mo'), 'Negative entries use a mathematical minus sign')
  results.push('NumPy shape and ndim are distinct; mathematical addition uses three 3-by-2 matrices')
  assert.deepEqual(errors, [])
  await writeFile('qa/math-format/results.json', JSON.stringify({ results, errors }, null, 2))
  results.forEach(result => console.log('PASS', result))
} finally { await browser.close() }
