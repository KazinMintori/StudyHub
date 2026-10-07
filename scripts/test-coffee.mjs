import puppeteer from 'puppeteer'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const root = path.resolve(__dirname, '..')

const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] })
const page = await browser.newPage()
await page.setViewport({ width: 1280, height: 900 })

const targetUrl = 'file:///' + path.join(root, 'index.html').replace(/\\/g, '/')
console.log('Loading:', targetUrl)
await page.goto(targetUrl, { waitUntil: 'load' })
await new Promise(r => setTimeout(r, 1000))

await page.screenshot({ path: path.join(root, 'test-home.png') })
console.log('Home screenshot taken.')

const btn = await page.$('.coffee-float-btn')
if (btn) {
  console.log('Found .coffee-float-btn, clicking...')
  await btn.click()
  await new Promise(r => setTimeout(r, 800))
  await page.screenshot({ path: path.join(root, 'test-modal.png') })
  console.log('Modal screenshot taken.')
} else {
  console.log('coffee-float-btn not found')
}

await browser.close()
