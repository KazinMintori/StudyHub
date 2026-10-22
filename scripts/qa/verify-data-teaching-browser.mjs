// Course-only development render checks. This does not build the static site.
import assert from 'node:assert/strict'
import { readFile, readdir, mkdir, writeFile } from 'node:fs/promises'
import puppeteer from 'puppeteer'

const base = process.env.QA_URL || 'http://127.0.0.1:5193'
assert(/^http:\/\/127\.0\.0\.1:\d+$/.test(base))
const directory = 'raw_materials/xu-ly-du-lieu/worked-examples'
const sources = await Promise.all((await readdir(directory))
  .filter(name => name.endsWith('.json') && name !== 'verified-results.json')
  .map(async name => JSON.parse(await readFile(`${directory}/${name}`, 'utf8'))))
const output = 'qa/data-teaching-20261022/browser'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true,
  executablePath: process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe' })
const report = { rows: [], errors: [], failures: [], diagrams: [] }
try {
  const page = await browser.newPage()
  page.on('pageerror', error => report.errors.push(error.message))
  await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
  for (const width of (process.env.QA_WIDTHS || '360,375,768,1280').split(',').map(Number)) {
    await page.setViewport({ width, height: 940 })
    for (const source of sources) {
      const response = await page.goto(`${base}/xu-ly-du-lieu/bai-giang/${source.slug}.html#notes`,
        { waitUntil: 'networkidle2', timeout: 120000 })
      assert(response?.ok(), source.slug)
      await page.waitForSelector('.lecture-notes-content .custom-block')
      // Compare settled colors, rather than a frame midway through theme transitions.
      await page.addStyleTag({ content: '*,*::before,*::after{transition:none!important;animation:none!important}' })
      await page.evaluate(async () => {
        for (const image of document.querySelectorAll('.lecture-notes-content img')) image.loading = 'eager'
        await Promise.all([...document.querySelectorAll('.lecture-notes-content img')].map(image => image.decode().catch(() => {})))
        await document.fonts.ready
        const font = getComputedStyle(document.querySelector('.lecture-notes-content p')).font
        await document.fonts.load(font, 'Ánh xạ, dữ liệu, kết quả')
      })
      for (const dark of [false, true]) {
        await page.evaluate(value => document.documentElement.classList.toggle('dark', value), dark)
        const row = await page.evaluate(({ sections }) => {
          const problems = []
          const area = document.querySelector('.lecture-notes-content')
          for (const section of sections) {
            const block = [...area.querySelectorAll('.custom-block')].find(el =>
              el.querySelector('.custom-block-title')?.textContent.trim() === `Ví dụ: ${section.title}`)
            if (!block) { problems.push(`${section.id}: Missing example`); continue }
            const code = block.querySelector('div.language-python pre code')?.textContent
            if (code?.trimEnd() !== section.code.trimEnd()) problems.push(`${section.id}: Changed code characters`)
            for (const table of block.querySelectorAll('table')) {
              const columns = table.querySelectorAll('thead th').length
              if (!columns || [...table.querySelectorAll('tbody tr')].some(tr => tr.children.length !== columns))
                problems.push(`${section.id}: Unequal table columns`)
              for (const cell of table.querySelectorAll('td,th')) {
                const style = getComputedStyle(cell)
                if (['hidden', 'clip'].includes(style.overflowX) && cell.scrollWidth > cell.clientWidth + 2)
                  problems.push(`${section.id}: Clipped table cell`)
              }
            }
            const text = block.innerText
            if (/\uFFFD|\^M/.test(text)) problems.push(`${section.id}: Broken text encoding`)
            for (const image of block.querySelectorAll('img')) {
              const box = image.getBoundingClientRect()
              if (!image.complete || !image.naturalWidth || box.width < 200)
                problems.push(`${section.id}: Missing or unreadably small image`)
            }
          }
          const visible = el => el.getBoundingClientRect().width > 0
          const math = [...area.querySelectorAll('mjx-container')].filter(visible)
          const mathOverflow = math.filter(el => {
            const box = el.getBoundingClientRect(), svg = el.querySelector('svg')?.getBoundingClientRect()
            return box.left < -2 || box.right > innerWidth + 2 ||
              (svg && svg.width > box.width + 2) ||
              (['auto', 'scroll'].includes(getComputedStyle(el).overflowX) && el.scrollWidth > el.clientWidth + 2)
          }).map(el => el.textContent.slice(0, 100))
          if (mathOverflow.length) problems.push(...mathOverflow.map(text => `Math overflow: ${text}`))
          if (area.querySelector('mjx-merror,[data-mml-node="merror"],[data-mjx-error]')) problems.push('Invalid math')
          if (document.documentElement.scrollWidth > innerWidth + 2) problems.push('Page overflow')
          const font = getComputedStyle(area.querySelector('p')).font
          return { problems, tables: area.querySelectorAll('table').length,
            examples: sections.length, math: math.length, font,
            fontReady: document.fonts.check(font, 'Ánh xạ, dữ liệu, kết quả') }
        }, source)
        report.rows.push({ slug: source.slug, width, dark, ...row })
        if (row.problems.length || !row.fontReady) report.failures.push(report.rows.at(-1))
        if ([360, 1280].includes(width) && ['bai-04-lam-quen-pandas', 'bai-08-ghep-bang-chuyen-dang'].includes(source.slug)) {
          const title = source.sections.find(s => s.illustration)?.title || source.sections[0].title
          const target = await page.evaluateHandle(title => {
            const block = [...document.querySelectorAll('.custom-block')].find(el =>
              el.querySelector('.custom-block-title')?.textContent.trim() === `Ví dụ: ${title}`)
            return block?.querySelector('table') || block
          }, title)
          await page.waitForFunction(() => document.fonts.status === 'loaded')
          await target.asElement().screenshot({ path: `${output}/${source.slug}-${width}-${dark ? 'dark' : 'light'}.png` })
          await target.dispose()
        }
      }
      console.log(`Checked ${width}px ${source.slug}`)
    }
  }
  for (const name of ['series-map', 'dataframe-apply', 'concat-alignment', 'groupby-shape']) {
    await page.goto(`${base}/xu-ly-du-lieu/bai-giang/img/function-examples/${name}.svg`)
    const result = await page.evaluate(() => {
      const svg = document.querySelector('svg'), box = svg.viewBox.baseVal
      return [...svg.querySelectorAll('text')].flatMap(el => {
        const b = el.getBBox()
        return b.x < 0 || b.y < 0 || b.x + b.width > box.width || b.y + b.height > box.height
          ? [el.textContent] : []
      })
    })
    report.diagrams.push({ name, clippedText: result })
    if (result.length) report.failures.push({ name, clippedText: result })
    await page.setViewport({ width: 360, height: 900 })
    await (await page.$('svg')).screenshot({ path: `${output}/${name}.png` })
  }
} finally {
  await writeFile(`${output}/report.json`, JSON.stringify(report, null, 2) + '\n')
  await browser.close()
}
assert.equal(report.errors.length, 0, JSON.stringify(report.errors))
assert.equal(report.failures.length, 0, JSON.stringify(report.failures, null, 2))
console.log(`${report.rows.length} responsive/theme cases passed`)
