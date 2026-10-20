import puppeteer from 'puppeteer'
import { mkdir, writeFile } from 'node:fs/promises'
import { course } from '../../src/content/courses/xac-suat-thong-ke/course.mjs'

const base = process.env.QA_URL || 'http://127.0.0.1:5173'
const output = process.env.QA_OUTPUT || 'C:/Users/Ai/.codex/tmp/xstk-qa'
const widths = (process.env.QA_WIDTHS || '360,375,768,1280').split(',').map(Number)
const tabs = (process.env.QA_TABS || 'notes,bai-tap').split(',')
const selected = process.env.QA_LESSONS?.split(',')
const lessons = selected ? course.lessons.filter(l => selected.some(s => l.slug.startsWith(s))) : course.lessons
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true })
const page = await browser.newPage()
page.setDefaultTimeout(60000)
const runtimeErrors = [], results = []
page.on('pageerror', error => runtimeErrors.push({ url: page.url(), message: error.message }))
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
try {
  for (const lesson of lessons) {
    const response = await page.goto(`${base}/xac-suat-thong-ke/bai-giang/${lesson.slug}`, { waitUntil: 'networkidle0', timeout: 120000 })
    await page.waitForFunction(() => !!document.querySelector('#app')?.__vue_app__, { timeout: 60000 })
    await page.waitForSelector('.lecture-header h1')
    for (const tab of tabs) {
      await page.$eval(`.lecture-tabs a[href$="#${tab}"]`, element => element.click())
      await page.waitForFunction(tab => !!document.querySelector(`.lecture-tabs a[href$="#${tab}"][aria-current="page"]`), {}, tab)
      await page.waitForNetworkIdle({ idleTime: 200, timeout: 10000 }).catch(() => {})
      await page.evaluate(() => {
      document.querySelectorAll('.vp-doc details,.lecture-panels details').forEach(el => { el.open = true })
      document.querySelectorAll('.vp-doc img').forEach(el => { el.loading = 'eager' })
      })
      await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))))
      await page.waitForNetworkIdle({ idleTime: 150, timeout: 10000 }).catch(() => {})
      await page.evaluate(() => document.fonts.ready)
      await page.evaluate(async () => {
        const images = [...document.querySelectorAll('.main > .vp-doc img')].filter(el => el.getClientRects().length && el.getBoundingClientRect().width)
        await Promise.all(images.map(el => Promise.race([
          el.decode().catch(() => {}),
          new Promise(resolve => setTimeout(resolve, 10000)),
        ])))
      })
    const slideCount = tab === 'slides' && process.env.QA_ALL_SLIDES === '1' ? course.slides.filter(slide => slide.note === lesson.slug).length : 1
    for (let frame = 0; frame < slideCount; frame++) {
      if (frame) {
        await page.$eval('.slide-controls button:last-child', element => element.click())
        await page.waitForFunction(frame => document.querySelector('.course-slide .eyebrow')?.textContent.includes(`Thẻ ôn tập ${frame + 1} /`), {}, frame)
      }
    for (const width of widths) {
      await page.setViewport({ width, height: 900, deviceScaleFactor: 1 })
      const metrics = await page.evaluate(() => {
        const visible = el => !!(el.getBoundingClientRect().width && el.getBoundingClientRect().height)
        const math = [...document.querySelectorAll('.main > .vp-doc mjx-container,.lecture-panels mjx-container')].filter(visible)
        const overflowingMath = math.flatMap(el => {
          const svg = el.querySelector('svg')
          const rect = svg?.getBoundingClientRect()
          const host = el.closest('.static-math,.math-text') || el.parentElement
          const bounds = host.getBoundingClientRect()
          const inTable = !!el.closest('table')
          if (!rect || (rect.width <= bounds.width + 2 && (inTable || (rect.right <= innerWidth + 1 && rect.left >= -1)))) return []
          return [{ tex: el.querySelector('mjx-assistive-mml')?.textContent || svg?.getAttribute('data-tex') || '', display: el.getAttribute('display'), width: Math.round(rect.width), available: Math.round(bounds.width), x: Math.round(rect.x), heading: (() => { let n = host; while(n) { if (/^H[2-4]$/.test(n.tagName)) return n.textContent; n = n.previousElementSibling || n.parentElement } return '' })() }]
        })
        return {
          pageOverflow: document.documentElement.scrollWidth > innerWidth + 2,
          documentWidth: document.documentElement.scrollWidth,
          h1Count: document.querySelectorAll('h1').length,
          compileOverlay: document.querySelector('vite-error-overlay')?.shadowRoot?.textContent.slice(0, 800) || '',
          mathCount: math.length,
          overflowingMath,
          mathErrors: [...document.querySelectorAll('[data-mml-node="merror"],mjx-merror')].map(el => el.textContent),
          rawContainers: [...document.querySelectorAll('.main > .vp-doc p')].filter(el => visible(el) && /^\s*:::/.test(el.textContent)).map(el => el.textContent.slice(0, 120)),
          accidentalHtmlCode: [...document.querySelectorAll('.main > .vp-doc pre')].filter(el => visible(el) && /^\s*<\/?(?:img|ul|ol|li|div|p)\b/i.test(el.textContent)).map(el => el.textContent.slice(0, 120)),
          brokenImages: [...document.querySelectorAll('.main > .vp-doc img')].filter(el => el.getClientRects().length && el.getBoundingClientRect().width && (!el.complete || !el.naturalWidth)).map(el => el.getAttribute('src')),
          assistiveVisible: [...document.querySelectorAll('mjx-assistive-mml')].some(visible),
          mathScrollbars: math.filter(el => /auto|scroll/.test(getComputedStyle(el).overflowX) || /auto|scroll/.test(getComputedStyle(el).overflowY)).length,
          exerciseCount: document.querySelectorAll('.main > .vp-doc .exercise').length,
          notesPanelExists: !!document.querySelector('.main > .vp-doc .lecture-notes-content'),
          exercisePanelExists: !!document.querySelector('.main > .vp-doc .lecture-exercises-content'),
          exerciseTextLength: document.querySelector('.main > .vp-doc .lecture-exercises-content')?.textContent.trim().length || 0,
          textOverflow: [...document.querySelectorAll('.lecture-panels :is(h2,h3,h4,p,li),.main > .vp-doc :is(h2,h3,h4,p,li)')].filter(el => visible(el) && !el.closest('table,pre,.table-scroll') && el.scrollWidth > el.clientWidth + 3).map(el => el.textContent.slice(0, 140)),
          foldedSolutions: document.querySelectorAll('.main > .vp-doc details').length,
        }
      })
      const result = { slug: lesson.slug, tab, frame: frame + 1, width, status: response.status(), ...metrics }
      results.push(result)
      await writeFile(`${output}/report.json`, JSON.stringify({ results, runtimeErrors }, null, 2))
      console.log(JSON.stringify({ slug: lesson.slug, tab, width, pageOverflow: result.pageOverflow, mathOverflow: result.overflowingMath.length, mathErrors: result.mathErrors.length, rawContainers: result.rawContainers.length, brokenImages: result.brokenImages.length }))
      if (process.env.QA_SCREENSHOTS === '1' && (width === 375 || width === 1280)) {
        await page.screenshot({ path: `${output}/${lesson.slug}-${tab}-${width}.png`, fullPage: false })
      }
    }
    }
    }
  }
  await writeFile(`${output}/report.json`, JSON.stringify({ results, runtimeErrors }, null, 2))
  const failures = results.filter(r => r.status >= 400 || r.pageOverflow || r.h1Count !== 1 || r.compileOverlay || r.overflowingMath.length || r.mathErrors.length || r.rawContainers.length || r.accidentalHtmlCode.length || r.brokenImages.length || r.assistiveVisible || r.mathScrollbars || r.textOverflow.length || (r.tab === 'bai-tap' && (!r.exercisePanelExists || r.exerciseTextLength < 80)))
  console.log(`Checked ${lessons.length} lessons, ${tabs.length} tabs at ${widths.length} widths: ${failures.length} failing cases, ${runtimeErrors.length} runtime errors. ${output}/report.json`)
  if (failures.length || runtimeErrors.length) process.exitCode = 1
} finally {
  await browser.close()
}
