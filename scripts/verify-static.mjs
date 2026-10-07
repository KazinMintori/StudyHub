import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { writeFile } from 'node:fs/promises'
import http from 'node:http'
import path from 'node:path'

const browser = await puppeteer.launch({ headless: true })
const page = await browser.newPage(), errors = []
page.on('pageerror', error => errors.push(error.message))
const base = process.env.STATIC_QA_URL || 'http://127.0.0.1:8080'
try {
  await page.goto(base, { waitUntil: 'networkidle0' }); await page.waitForSelector('.study-home')
  const links = await page.$$eval('a[href]', els => [...new Set(els.map(el => el.getAttribute('href')).filter(href => href?.startsWith('/') && !href.includes('#')))])
  for (const path of links) {
    const status = await new Promise((resolve, reject) => http.get(base + path, response => { response.resume(); response.on('end', () => resolve(response.statusCode)) }).on('error', reject))
    assert.equal(status, 200, path)
  }
  const firstLesson = await page.$eval('.start-panel a', el => el.getAttribute('href'))
  assert(firstLesson.endsWith('.html'))
  await page.goto(base + firstLesson, { waitUntil: 'networkidle0' }); await page.waitForSelector('.lesson-actions')
  await page.waitForSelector('.mermaid svg'); assert(await page.$('mjx-container'))
  await page.click('.lesson-actions button'); assert(await page.$('.lesson-actions button[aria-pressed=true]'))
  await page.goto(base + '/goc-hoc-tap.html#notes', { waitUntil: 'networkidle0' }); await page.waitForSelector('#notes textarea:not([disabled])')
  assert.equal(await page.$eval('#notes', el => getComputedStyle(el).display !== 'none'), true)
  await page.reload({ waitUntil: 'networkidle0' }); assert.equal(await page.$eval('#notes', el => getComputedStyle(el).display !== 'none'), true)
  const client = await browser.target().createCDPSession(); await client.send('Browser.setDownloadBehavior', { behavior: 'allow', downloadPath: path.resolve('qa'), eventsEnabled: true })
  const download = new Promise((resolve, reject) => {
    const timeout = setTimeout(() => reject(new Error('Markdown download timed out')), 10000)
    client.on('Browser.downloadProgress', event => { if (event.state === 'completed') { clearTimeout(timeout); resolve() } })
  })
  await page.$eval('#notes .study-button.primary', button => button.click()); await download
  const { readFile } = await import('node:fs/promises'); assert((await readFile('qa/StudyHub-general.md', 'utf8')).includes('Ghi chú học tập'))
  assert.deepEqual(errors, [])
  await writeFile('qa/static-results.json', JSON.stringify({ linksChecked: links.length, directLesson: true, toolsReload: true, noteDownload: true, errors }, null, 2))
  console.log(`Production passed: ${links.length} internal links, direct lesson loading, MathJax, Mermaid, completion, tools reload and Markdown download; no runtime errors.`)
} finally { await browser.close() }
