// Inspect only this course on a local dev server. No static site build.
import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, readFile, writeFile } from 'node:fs/promises'

const base = process.env.QA_URL || 'http://127.0.0.1:5187'
assert(/^http:\/\/127\.0\.0\.1:\d+$/.test(base), 'Use a localhost dev server')
const { lessons } = JSON.parse(await readFile('raw_materials/xu-ly-du-lieu/authoring-contract.json', 'utf8'))
const output = 'qa/data-course'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({headless: true,
  executablePath: process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const rows = [], failures = [], errors = []
try {
  const page = await browser.newPage()
  page.on('pageerror', error => errors.push(error.message))
  await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
  for (const width of (process.env.QA_WIDTHS || '360,375,768,1280').split(',').map(Number)) {
    await page.setViewport({ width, height: 900 })
    for (const lesson of lessons) {
      const route = `/xu-ly-du-lieu/bai-giang/${lesson.slug}.html`
      const response = await page.goto(base + route + '#notes', {waitUntil: 'networkidle2', timeout: 120000})
      assert(response?.ok(), `${route}: HTTP ${response?.status()}`)
      await page.waitForSelector('.lecture-header h1', {timeout:60000})
      await page.evaluate(() => document.fonts.ready)
      assert.equal(await page.$eval('.lecture-header h1', el => el.textContent.trim()), lesson.title)
      const closed = await page.$$eval('.vp-doc details', nodes => nodes.every(node => !node.open))
      assert(closed, `${lesson.slug}: Solutions must start folded`)
      await page.$$eval('.vp-doc details', nodes => nodes.forEach(node => { node.open = true }))
      const notes = await inspect(page)
      const row = {width, chapter:lesson.chapter, notes}
      for (const tab of ['slides', 'cheatsheet', 'kien-thuc-can-co', 'bai-tap']) {
        await page.click(`.lecture-tabs a[href$="#${tab}"]`)
        await page.waitForFunction(tab => window.location.hash === '#' + tab, {}, tab)
        if (tab === 'slides') {
          await page.waitForSelector('.course-slide', {timeout:10000})
          const next = await page.$('.slide-controls button:last-child')
          assert(next, `${lesson.slug}: Missing slide controls`)
          const first = await page.$eval('.course-slide h2', el => el.textContent)
          await next.click()
          assert.notEqual(await page.$eval('.course-slide h2', el => el.textContent), first)
          await page.keyboard.press('ArrowLeft')
          assert.equal(await page.$eval('.course-slide h2', el => el.textContent), first)
        }
        if (tab === 'bai-tap') {
          await page.$$eval('.vp-doc details', nodes => nodes.forEach(node => { node.open = true }))
          const text = await page.$eval('.main > .vp-doc', el => el.innerText)
          assert(/Bài tập|Thực hành/.test(text), `${lesson.slug}: No authored exercises in chapter tab`)
          if ([360,1280].includes(width) && ['4','7','9','13','A'].includes(lesson.chapter)) {
            await page.screenshot({path:`${output}/chapter-${lesson.chapter}-${width}-exercises.png`})
          }
        }
        row[tab] = await inspect(page)
      }
      for (const [part, result] of Object.entries(row)) {
        if (result && typeof result === 'object' && (result.mathErrors || result.mathOverflow.length || result.documentOverflow || result.unrendered.length || result.missingImages.length || !result.fontReady)) {
          failures.push({width, chapter:lesson.chapter, part, result})
        }
      }
      if ([360,1280].includes(width)) {
        await page.click('.lecture-tabs a[href$="#notes"]')
        await page.screenshot({path:`${output}/chapter-${lesson.chapter}-${width}.png`})
        if (['4','7','9','A'].includes(lesson.chapter)) {
          const math = await page.$('.vp-doc mjx-container')
          if (math) {
            await math.evaluate(el => el.scrollIntoView({block:'center'}))
            await page.screenshot({path:`${output}/chapter-${lesson.chapter}-${width}-math.png`})
          }
        }
      }
      rows.push(row)
      console.log(`Checked ${width}px chapter ${lesson.chapter}`)
    }
  }
  assert.equal(errors.length, 0, 'Browser errors: ' + errors.join('; '))
  assert.equal(failures.length, 0, JSON.stringify(failures, null, 2))
} finally {
  await writeFile(`${output}/browser-report.json`, JSON.stringify({rows, failures, errors}, null, 2) + '\n')
  await browser.close()
}

async function inspect(page) {
  return page.evaluate(() => {
    const visible = el => el.getBoundingClientRect().width > 0 && el.getBoundingClientRect().height > 0
    // Inline math deliberately has line-height:0; its SVG can still overflow.
    const math = [...document.querySelectorAll('mjx-container')].filter(el => el.getBoundingClientRect().width > 0)
    const mathOverflow = math.flatMap(el => {
      const box = el.getBoundingClientRect(), svg = el.querySelector('svg')?.getBoundingClientRect()
      const style = getComputedStyle(el)
      const scroll = ['auto','scroll'].includes(style.overflowX) && el.scrollWidth > el.clientWidth + 1
      return box.left < -2 || box.right > innerWidth + 2 || (svg && svg.width > box.width + 2) || scroll
        ? [{tex:el.textContent.slice(0,160), left:box.left, right:box.right, width:box.width, svgWidth:svg?.width, scroll}] : []
    })
    const errors = [...document.querySelectorAll('mjx-merror,[data-mml-node="merror"],[data-mjx-error]')].filter(visible)
    const unrendered = [...document.querySelectorAll('.math-text')].filter(visible).flatMap(el =>
      [...el.childNodes].filter(node => node.nodeType === Node.TEXT_NODE).map(node => node.textContent).filter(text => /\$[^$]+\$|\\(?:frac|begin)\{/.test(text)))
    const missingImages = [...document.querySelectorAll('.vp-doc img')].filter(visible).filter(img => img.complete && !img.naturalWidth).map(img => img.src)
    const paragraph = [...document.querySelectorAll('.vp-doc p')].find(visible)
    const font = paragraph ? getComputedStyle(paragraph).font : getComputedStyle(document.body).font
    return {mathCount:math.length, mathErrors:errors.length, mathOverflow, unrendered, missingImages,
      documentOverflow:document.documentElement.scrollWidth > innerWidth + 2,
      font, fontReady:document.fonts.check(font, 'Trường đại học, xử lý dữ liệu, số lượng'),
      loadedFonts:[...document.fonts].filter(font => font.status === 'loaded').map(font => font.family)}
  })
}
