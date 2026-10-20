import puppeteer from 'puppeteer'
import { mkdir, readdir, readFile, writeFile } from 'node:fs/promises'
import path from 'node:path'
import { pathToFileURL } from 'node:url'

const directories = process.argv.slice(2)
if (!directories.length) directories.push(...['co-dien-refined', 'co-dien-bayes'].map(name => `docs/xac-suat-thong-ke/bai-giang/img/${name}`))
const output = process.env.QA_OUTPUT || 'C:/Users/Ai/.codex/tmp/xstk-figures'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true })
const page = await browser.newPage()
const results = []
try {
  for (const directory of directories) {
    for (const name of (await readdir(directory)).filter(name => name.endsWith('.svg')).sort()) {
      const file = path.resolve(directory, name)
      const svg = await readFile(file, 'utf8')
      const viewBox = svg.match(/viewBox=["']\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)/)
      if (!viewBox || /(?:\bNaN\b|\bInfinity\b)/.test(svg)) throw new Error(`Invalid diagram geometry: ${file}`)
      const height = Math.round(640 * Number(viewBox[2]) / Number(viewBox[1]))
      await page.setViewport({ width: 640, height, deviceScaleFactor: 1 })
      await page.goto(pathToFileURL(file).href)
      await page.evaluate(() => document.fonts.ready)
      const clippedText = await page.evaluate(() => [...document.querySelectorAll('text')].flatMap(element => {
        const rect = element.getBoundingClientRect()
        return rect.left < -2 || rect.right > innerWidth + 2 || rect.top < -2 || rect.bottom > innerHeight + 2
          ? [{ text: element.textContent, left: Math.round(rect.left), right: Math.round(rect.right), top: Math.round(rect.top), bottom: Math.round(rect.bottom) }]
          : []
      }))
      const collisions = await page.evaluate(() => {
        const labels = [...document.querySelectorAll('text')].filter(el => !el.closest('defs')).map(el => ({ text: el.textContent, rect: el.getBoundingClientRect() }))
        const textText = [], textStroke = []
        for (let i = 0; i < labels.length; i++) for (let j = i + 1; j < labels.length; j++) {
          const a = labels[i].rect, b = labels[j].rect
          const w = Math.min(a.right, b.right) - Math.max(a.left, b.left)
          const h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top)
          if (w > 3 && h > 3) textText.push([labels[i].text, labels[j].text])
        }
        for (const shape of document.querySelectorAll('path,polyline,line,polygon,circle,ellipse')) {
          if (shape.closest('defs') || !shape.getTotalLength) continue
          const style = getComputedStyle(shape)
          if (style.stroke === 'none' || Number.parseFloat(style.strokeWidth) < .75) continue
          const matrix = shape.getScreenCTM(), length = shape.getTotalLength()
          if (!matrix || !length) continue
          const points = []
          for (let d = 0; d <= length; d += 3) {
            const point = shape.getPointAtLength(d)
            points.push({ x: matrix.a * point.x + matrix.c * point.y + matrix.e, y: matrix.b * point.x + matrix.d * point.y + matrix.f })
          }
          for (const label of labels) {
            const r = label.rect
            if (points.some(p => p.x > r.left + 1 && p.x < r.right - 1 && p.y > r.top + 1 && p.y < r.bottom - 1)) textStroke.push(label.text)
          }
        }
        return { textText, textStroke: [...new Set(textStroke)] }
      })
      const png = path.join(output, `${results.length + 1}-${name.replace('.svg', '.png')}`)
      await page.screenshot({ path: png })
      results.push({ file, png, width: 640, height, clippedText, ...collisions })
    }
  }
  await writeFile(path.join(output, 'manifest.json'), JSON.stringify(results, null, 2))
  console.log(`Rendered ${results.length} SVG figures for visual review in ${output}`)
} finally { await browser.close() }
