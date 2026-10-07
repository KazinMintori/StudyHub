import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import { courseCatalog } from '../docs/.vitepress/course-catalog.mjs'
const base = process.env.QA_URL || 'http://127.0.0.1:5181'
const browser = await puppeteer.launch({ headless: true }), page = await browser.newPage(), results = [], errors = []
page.on('pageerror', error => errors.push(error.message))
const go = async path => { const response = await page.goto(base + path, { waitUntil: 'networkidle0', timeout: 120000 }); if(response)assert([200,304].includes(response.status()), path); await page.evaluate(()=>document.fonts.ready) }
async function check(name, action) { await action(); results.push(name); console.log('PASS', name) }
try {
  await page.setViewport({ width: 1440, height: 900 })
  await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
  await go('/')
  await check('Catalog counts and accent-insensitive course filtering', async () => {
    assert.equal(await page.$$eval('.course-row', rows => rows.length), courseCatalog.length)
    await page.type('.course-search input', 'xu ly du lieu'); assert.equal(await page.$$eval('.course-row', rows => rows.length), 1)
  })
  await check('Global search finds Đạo hàm without accents', async () => {
    await page.click('.DocSearch-Button'); await page.waitForSelector('.VPLocalSearchBox input')
    await page.type('.VPLocalSearchBox input', 'dao ham')
    await page.waitForFunction(()=>[...document.querySelectorAll('.VPLocalSearchBox a[href]')].some(a=>a.getAttribute('href').includes('/wiki/dao-ham.html')), { timeout: 30000 })
    await page.keyboard.press('Escape')
  })
  for (const course of courseCatalog) await check(`${course.id}: ordered lessons and single destination per row`, async () => {
    await go(`/${course.id}/`)
    assert.equal(await page.$$eval('.lecture-list > article', rows=>rows.length), course.lessons.length)
    assert(await page.$$eval('.lecture-list > article', rows=>rows.every(row=>row.querySelectorAll('a').length===1)))
  })
  const course = courseCatalog.find(c=>c.id==='toan-cho-ai'), lesson=course.lessons.find(l=>l.slug==='bai-01-nhap-mon-toi-uu')
  const path = `/${course.id}/bai-giang/${lesson.slug}.html`
  await check('Foundation disclosure and understanding persist under original storage keys', async () => {
    await go(path+'#kien-thuc-can-co'); await page.waitForSelector('.foundation-entry')
    assert.equal(await page.$$eval('.foundation-entry', rows=>rows.length), lesson.prerequisites.length)
    assert.equal(await page.$eval('.foundation-entry details', details=>details.open), false)
    await page.click('.foundation-entry summary'); assert(await page.$eval('.foundation-entry details', details=>details.open))
    await page.click('.foundation-entry input'); await page.reload({waitUntil:'networkidle0'})
    assert(await page.$('.foundation-entry input:checked'))
    assert(await page.evaluate(id=>!!localStorage.getItem(`studyhub_foundations_${id}`),course.id))
  })
  await check('Completion, reading bookmark and mobile resume preserve learning progress', async () => {
    await page.setViewport({width:390,height:900})
    await go(path+'#notes'); await page.click('.lesson-actions button')
    assert(await page.$('.lesson-actions button[aria-pressed=true]'))
    const headingId = await page.$eval('.main > .vp-doc h2[id]', heading=>{heading.scrollIntoView();return heading.id})
    await page.waitForFunction(id=>JSON.parse(localStorage.getItem('studyhub_last_lesson'))?.heading===id,{},headingId)
    const saved = await page.evaluate(()=>JSON.parse(localStorage.getItem('studyhub_last_lesson')))
    await go('/')
    assert.match(await page.$eval('.resume-panel', el=>el.textContent), /Đang học dở/)
    assert(await page.$eval('.resume-panel a', (el,id)=>el.getAttribute('href').endsWith('#'+id),saved.heading))
    await page.click('.resume-panel a'); await page.waitForFunction(()=>!!location.hash && document.querySelector('.lecture-tabs a[aria-current]')?.textContent.trim()==='Notes')
  })
  await check('Compact mobile header retains sidebar and article outline access', async () => {
    await go(path+'#notes')
    await page.click('.mobile-lecture-nav > button'); await page.waitForSelector('.VPSidebar.open')
    await page.keyboard.press('Escape'); await page.waitForFunction(()=>!document.querySelector('.VPSidebar.open'))
    await page.click('.mobile-lecture-nav summary'); assert(await page.$eval('.mobile-lecture-nav details',d=>d.open))
    assert(await page.$$eval('.mobile-lecture-nav details nav a',links=>links.length>0))
  })
  await check('Former exercise-tab address opens Notes', async () => { await go(path+'#bai-tap'); await page.waitForFunction(()=>location.hash==='#notes'); assert(await page.$('.lecture-tabs a[href$="#notes"][aria-current]')) })
  await check('Support opens only from footer and closes with Escape', async () => {
    await go('/'); assert.equal(await page.$('.coffee-btn'),null)
    await page.click('.site-footer button'); await page.waitForSelector('.coffee-dialog[open]')
    await page.keyboard.press('Escape'); assert.equal(await page.$('.coffee-dialog[open]'),null)
  })
  await check('Wiki search ignores accents and retains full definitions and lecture backlinks', async () => {
    await go('/wiki/'); await page.type('.wiki-filters input','dao ham rieng'); assert(await page.$('.wiki-entry-list a[href$="/dao-ham-rieng.html"]'))
    await go('/wiki/gradient.html'); assert(await page.$('.wiki-usage-top a[href*="bai-giang"]')); assert(await page.$('mjx-container'))
  })
  await check('Notes save safely and the timer lives in the study workspace', async () => {
    await go('/goc-hoc-tap#notes'); await page.waitForSelector('#notes textarea:not([disabled])')
    const content='# Kiểm thử\n\n**Ghi chú**\n\n<script>alert(1)</script>'
    await page.$eval('#notes textarea',(el,value)=>{el.value=value;el.dispatchEvent(new Event('input',{bubbles:true}))},content)
    await page.reload({waitUntil:'networkidle0'}); assert.equal(await page.$eval('#notes textarea',e=>e.value),content)
    await go('/goc-hoc-tap#focus'); assert(await page.$eval('.timer-display',e=>e.textContent.trim()==='25:00'))
    await page.evaluate(()=>[...document.querySelectorAll('#focus button')].find(b=>b.textContent.trim()==='Bắt đầu').click())
    await page.waitForFunction(()=>document.querySelector('.timer-display').textContent.trim()!=='25:00')
    await page.reload({waitUntil:'networkidle0'}); assert(await page.evaluate(()=>[...document.querySelectorAll('#focus button')].some(b=>b.textContent.trim()==='Tạm dừng')))
    await go('/'); assert.equal(await page.$('.timer-display'),null)
  })
  await check('Theme-aware Mermaid diagrams and visible image captions', async () => {
    await page.setViewport({width:1440,height:900}); await go('/bieu-dien-tri-thuc/bai-giang/02-tim-kiem-mu.html')
    await page.waitForSelector('.mermaid svg', {timeout:60000}); const first=await page.$eval('.mermaid svg',e=>e.outerHTML)
    await page.click('.VPNavBarAppearance button'); await page.waitForFunction(first=>document.querySelector('.mermaid svg')?.outerHTML!==first,{},first)
    await go('/giai-thuat-du-lieu/bai-giang/bai-03-pagerank-mo-hinh-va-tinh-toan.html'); assert(await page.$('.lecture-figure figcaption'))
  })
  assert.deepEqual(errors,[])
  await mkdir('qa/redesign',{recursive:true}); await writeFile('qa/redesign/behavior.json',JSON.stringify({results,errors},null,2))
  console.log(`${results.length} behavior checks passed; Slides excluded.`)
} finally { await browser.close() }
