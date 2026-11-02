import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import puppeteer from 'puppeteer'
import { courseCatalog } from '../../src/content/catalog.mjs'
import { isExtendedCourse } from '../../src/content/collections.mjs'

const base = (process.env.QA_URL || 'http://127.0.0.1:5173').replace(/\/$/, '')
const basePath = new URL(base).pathname.replace(/\/$/, '')
const output = process.env.QA_OUTPUT || 'qa/assessment-navigation'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true })
const errors = [], results = []
let page
try {
  for (const width of [1440, 375]) {
    // A fresh document must start at home. Starting at the exam itself hides
    // the missing-CSS defect because its HTML links its own batch stylesheet.
    page = await browser.newPage()
    page.setDefaultTimeout(60000)
    await page.setViewport({ width, height: 900 })
    page.on('pageerror', error => errors.push(error.message))
    await page.evaluateOnNewDocument(() => {
      sessionStorage.setItem('studyhub_welcome_seen', '1')
      window.assessmentDocument = Math.random()
    })
    await page.goto(base + '/', { waitUntil: 'networkidle0', timeout: 90000 })
    const documentId = await page.evaluate(() => window.assessmentDocument)
    async function follow(route, selector) {
      const href = basePath + route
      const previousTitle = await page.title()
      await page.evaluate(href => {
        const link = [...document.querySelectorAll('a[href]')].find(el => el.getAttribute('href') === href)
        if (!link) throw Error('Missing navigation link: ' + href)
        link.click()
      }, href)
      await page.waitForFunction(path => location.pathname === path, {}, new URL(base + route).pathname)
      // History changes before VitePress commits its destination component.
      // Lists on consecutive courses share selectors, so wait for the new
      // page title as well instead of accidentally checking the old cards.
      await page.waitForFunction(title => document.title !== title, {}, previousTitle)
      await page.waitForSelector(selector)
      await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))))
      assert.equal(await page.evaluate(() => window.assessmentDocument), documentId, 'navigation must keep the document')
    }
    async function cards(selector, minimum = 1) {
      const inspected = await page.$$eval(selector, elements => elements.map(el => {
        const css = getComputedStyle(el)
        return { text: el.textContent.trim().slice(0, 100), border: parseFloat(css.borderTopWidth), radius: parseFloat(css.borderRadius), padding: parseFloat(css.paddingTop), height: el.getBoundingClientRect().height }
      }))
      assert(inspected.length >= minimum, `${selector}: missing cards`)
      for (const card of inspected) assert(card.border > 0 && card.radius > 0 && card.padding >= 8 && card.height >= 44, `${page.url()}: unstyled card ${JSON.stringify(card)}`)
      assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `overflow at ${page.url()}`)
      results.push({ width, url: page.url(), selector, cards: inspected.length })
    }
    for (const course of courseCatalog) {
      if (isExtendedCourse(course)) await follow('/hoc-lieu-mo-rong/', '.extended-library')
      await follow(`/${course.id}/`, course.id === 'triet-hoc-mac-lenin' ? '.philosophy-topic-link' : '.lecture-row')
      await cards(course.id === 'triet-hoc-mac-lenin' ? '.philosophy-topic-link' : '.lecture-row')
      await follow('/', '.study-home')
    }
    await follow('/xu-ly-du-lieu/', '.lecture-row')
    await follow('/xu-ly-du-lieu/de-thi/', '.lecture-row')
    await cards('.lecture-row', 6)
    await follow('/xu-ly-du-lieu/de-thi/de-1.html', '.exam-choice__radio')
    assert.equal(await page.$eval('.exam-practice', el => getComputedStyle(el).maxWidth), '860px')
    await cards('.exam-choice', 4)
    await page.screenshot({ path: `${output}/data-paper-${width}.png` })
    await page.click('.exam-choice__radio')
    await page.waitForSelector('.exam-choice.is-selected')
    await page.click('.exam-nav-btn--next')
    await page.waitForFunction(() => location.search.includes('D1-002'))
    await follow('/xu-ly-du-lieu/de-thi/', '.lecture-row')
    await follow('/xu-ly-du-lieu/on-thi/', '.lecture-row')
    await cards('.lecture-row', 8)
    await follow('/xu-ly-du-lieu/on-thi/bai-01.html', '.exam-choice__radio')
    await cards('.exam-choice', 4)
    await follow('/', '.study-home')
    await follow('/triet-hoc-mac-lenin/', '.philosophy-topic-link')
    await follow('/triet-hoc-mac-lenin/on-thi/', '.exam-bank')
    await cards('.exam-bank', 3)
    for (const [chapter, count] of [[1, 6], [2, 8], [3, 8]]) {
      await follow(`/triet-hoc-mac-lenin/on-thi/chuong-${chapter}.html`, '.practice-test-list')
      await cards('.practice-test-list li > a', count)
      assert.equal(await page.$eval('.practice-test-list', el => getComputedStyle(el).display), 'grid')
      await page.screenshot({ path: `${output}/philosophy-chapter-${chapter}-${width}.png` })
      await follow(`/triet-hoc-mac-lenin/on-thi/chuong-${chapter}/bai-1.html`, '.exam-choice__radio')
      await cards('.exam-choice', 4)
      await follow(`/triet-hoc-mac-lenin/on-thi/chuong-${chapter}.html`, '.practice-test-list')
      await follow('/triet-hoc-mac-lenin/on-thi/', '.exam-bank')
    }
    await follow('/triet-hoc-mac-lenin/on-thi/de-thi/', '.papers-grid')
    await cards('.papers-grid li > a', 21)
    await cards('.paper-reference')
    await page.close()
  }
  assert.deepEqual(errors, [])
  console.log(`PASS ${results.length} card-layout checks: All course directories, Data exams and Philosophy practice, after SPA navigation at 1440px and 375px`)
} catch (error) {
  await page?.screenshot({ path: `${output}/failure.png` }).catch(() => {})
  errors.push(error.message)
  throw error
} finally {
  await writeFile(`${output}/results.json`, JSON.stringify({ results, errors }, null, 2))
  await browser.close()
}
