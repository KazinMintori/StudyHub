import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import puppeteer from 'puppeteer'

const base = process.env.QA_URL || 'http://127.0.0.1:5193'
assert(/^http:\/\/127\.0\.0\.1:\d+$/.test(base))
const out = 'qa/data-teaching-20261022/table-contrast'
await mkdir(out, { recursive: true })
const browser = await puppeteer.launch({ headless: true,
  executablePath: process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe' })
const report = []
try {
  const page = await browser.newPage()
  await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
  for (const width of [360, 375, 1280]) {
    await page.setViewport({ width, height: 940 })
    await page.goto(`${base}/xu-ly-du-lieu/bai-giang/bai-04-lam-quen-pandas.html#notes`,
      { waitUntil: 'networkidle2', timeout: 120000 })
    await page.waitForSelector('.lecture-notes-content table tbody tr')
    await page.evaluate(async () => {
      const p = document.querySelector('.lecture-notes-content p')
      await document.fonts.load(getComputedStyle(p).font, 'Chỉ mục, dữ liệu, kết quả')
    })
    for (const dark of [true, false]) {
      const result = await page.evaluate(async dark => {
        const luminance = color => {
          const rgb = color.match(/[\d.]+/g).slice(0, 3).map(Number)
          const linear = rgb.map(n => n / 255 <= 0.04045 ? n / 255 / 12.92 : ((n / 255 + 0.055) / 1.055) ** 2.4)
          return linear[0] * 0.2126 + linear[1] * 0.7152 + linear[2] * 0.0722
        }
        const cells = [...document.querySelectorAll('.lecture-notes-content table :is(td,th)')]
        document.documentElement.classList.toggle('dark', dark)
        let minimumContrast = Infinity
        const failures = []
        for (let frame = 0; frame < 35; frame++) {
          await new Promise(requestAnimationFrame)
          for (const cell of cells) {
            let current = cell, background
            while (current) {
              const color = getComputedStyle(current).backgroundColor
              if (!color.endsWith(', 0)') && color !== 'transparent') { background = color; break }
              current = current.parentElement
            }
            const a = luminance(getComputedStyle(cell).color), b = luminance(background)
            const contrast = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05)
            minimumContrast = Math.min(minimumContrast, contrast)
            if (contrast < 4.5) failures.push({ frame, text: cell.textContent, contrast })
          }
        }
        return { minimumContrast, failures }
      }, dark)
      report.push({ width, dark, ...result })
      const table = await page.evaluateHandle(() => [...document.querySelectorAll('.custom-block')]
        .find(el => el.querySelector('.custom-block-title')?.textContent.includes('Tra phí từ mã phòng'))?.querySelector('table'))
      await table.asElement().screenshot({ path: `${out}/${width}-${dark ? 'dark' : 'light'}.png` })
      await table.dispose()
    }
  }
} finally {
  await writeFile(`${out}/report.json`, JSON.stringify(report, null, 2) + '\n')
  await browser.close()
}
assert(report.length === 6 && report.every(row => !row.failures.length), JSON.stringify(report, null, 2))
console.log(JSON.stringify(report.map(({ width, dark, minimumContrast }) => ({ width, dark, minimumContrast })), null, 2))
