import assert from 'node:assert/strict'
import puppeteer from 'puppeteer'
import { mkdir, writeFile } from 'node:fs/promises'

const base = process.env.QA_URL || 'http://127.0.0.1:5175'
const output = 'qa/data-algorithms-04-06'
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({ headless: true, ...(process.env.PUPPETEER_EXECUTABLE_PATH ? { executablePath: process.env.PUPPETEER_EXECUTABLE_PATH } : {}) })
const page = await browser.newPage(), results = [], errors = []
page.on('pageerror', error => errors.push(error.message))
await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
const pages = [
  ['bai-04-pagerank-theo-chu-de-lien-ket-rac-va-hits', '.rank-lab'],
  ['bai-05-bieu-dien-tuong-dong-shingling-va-minhash', '.minhash-lab'],
  ['bai-06-tim-cap-tuong-dong-bang-lsh', '.lsh-lab']
]
async function go(route) {
  const response = await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 120000 })
  assert.ok(response?.ok(), `HTTP ${response?.status()} at ${route}`)
  await page.waitForFunction(() => Boolean(document.querySelector('#app')?.__vue_app__))
  await page.evaluate(() => document.fonts.ready)
}
async function metrics(label) {
  const value = await page.evaluate(() => ({
    width: document.documentElement.clientWidth,
    pageWidth: document.documentElement.scrollWidth,
    mathErrors: document.querySelectorAll('mjx-merror,[data-mjx-error]').length,
    overflow: [...document.querySelectorAll('mjx-container')].filter(el => el.checkVisibility() && el.scrollWidth > el.clientWidth + 1)
      .map(el => ({ text: el.textContent.slice(0, 160), width: el.clientWidth, contentWidth: el.scrollWidth })),
    visibleAssistiveMath: [...document.querySelectorAll('mjx-assistive-mml')].filter(el => el.checkVisibility()).length
  }))
  results.push({ label, ...value })
}
async function range(selector, value) {
  await page.$eval(selector, (el, v) => { el.value = String(v); el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })) }, value)
}
try {
  for (const width of [360, 375, 1280]) {
    await page.setViewport({ width, height: 900 })
    for (const [slug, lab] of pages) {
      await go(`/giai-thuat-du-lieu/bai-giang/${slug}.html`)
      await page.waitForSelector(lab)
      assert.equal(await page.$$eval('.lecture-header h1', items => items.length), 1)
      assert.ok(await page.$$eval('.vp-doc .exercise', items => items.length) >= 4, `${slug}: exercises`)
      await page.evaluate(() => document.querySelectorAll('.vp-doc details').forEach(el => { el.open = true }))
      await metrics(`${slug} Notes, all solutions open, ${width}px`)
      const element = await page.$(lab)
      const cropStyle = await page.addStyleTag({ content: '.VPNav,.VPLocalNav,.mobile-lecture-nav{visibility:hidden!important}' })
      await element.screenshot({ path: `${output}/${slug}-${width}-lab.png` })
      await cropStyle.evaluate(el => el.remove())
      if (width === 375) {
        await page.click('.lecture-tabs a[href$="#cheatsheet"]')
        await page.waitForSelector('.lecture-cheatsheet .cheatsheet-card')
        await metrics(`${slug} Cheatsheet, ${width}px`)
        assert.ok(await page.$$eval('.cheatsheet-card', items => items.length) >= 2)
        await page.click('.lecture-tabs a[href$="#kien-thuc-can-co"]')
        await page.waitForSelector('.lecture-foundations .foundation-entry')
        await metrics(`${slug} Foundations, ${width}px`)
        assert.ok(await page.$$eval('.foundation-group', items => items.length) >= 2, `${slug}: supporting concepts`)
      }
    }
  }

  await go(`/giai-thuat-du-lieu/bai-giang/${pages[0][0]}.html`)
  await page.waitForSelector('.rank-lab')
  await page.select('.rank-lab select', 'A')
  await range('.rank-lab input[type=range]', 0)
  await page.waitForFunction(() => [...document.querySelectorAll('.rank-row output')].map(x => x.textContent.trim()).join(',') === '1,0,0,0')
  await page.click('.rank-lab input[type=checkbox]')
  assert.match(await page.$eval('.rank-lab .lab-readout', el => el.textContent), /tổng điểm là 1/)
  const beta = await page.$('.rank-lab input[type=range]')
  await beta.focus(); await page.keyboard.press('ArrowRight')
  await page.waitForFunction(() => document.querySelector('.rank-lab input[type=range]').value === '0.05')
  results.push({ label: 'PageRank teleport, dangling toggle and keyboard range input', status: 'passed' })

  await go(`/giai-thuat-du-lieu/bai-giang/${pages[1][0]}.html`)
  await page.waitForSelector('.minhash-lab .lab-readout')
  assert.match(await page.$eval('.minhash-lab .lab-readout', el => el.textContent), /72\/120/)
  const selected = await page.$$('.minhash-lab fieldset:first-of-type input:checked')
  for (const checkbox of selected) await checkbox.click()
  await page.waitForFunction(() => document.querySelector('.minhash-lab .lab-readout')?.textContent.includes('ít nhất một'))
  results.push({ label: 'MinHash exhaustive collision count and empty-set handling', status: 'passed' })

  await go(`/giai-thuat-du-lieu/bai-giang/${pages[2][0]}.html`)
  await page.waitForSelector('.lsh-lab .lab-readout')
  const before = await page.$eval('.lsh-lab .lab-readout', el => el.textContent)
  await range('.lsh-lab .lab-controls label:last-child input', 0.5)
  assert.equal(await page.$eval('.lsh-lab .lab-readout', el => el.textContent), before)
  await range('.lsh-lab .lab-controls label:first-child input', 1)
  assert.notEqual(await page.$eval('.lsh-lab .lab-readout', el => el.textContent), before)
  results.push({ label: 'LSH verification threshold stays separate from candidate probability', status: 'passed' })

  await page.setViewport({ width: 375, height: 900 })
  for (const id of ['pagerank-ca-nhan-hoa', 'trustrank', 'hits', 'shingling', 'jaccard', 'minhash', 'lsh', 'phan-dai-minhash']) {
    await go(`/wiki/${id}.html`)
    await metrics(`Wiki ${id}, 375px`)
  }
  await go('/giai-thuat-du-lieu/')
  for (const [slug] of pages) assert.ok(await page.$(`a[href*="${slug}"]`), `${slug} missing from course overview`)
  const layoutFailures = results.filter(x => x.mathErrors || x.pageWidth > x.width + 1 || x.overflow?.length || x.visibleAssistiveMath)
  assert.deepEqual(layoutFailures, [], 'Layout or math failures; see browser-report.json')
  assert.deepEqual(errors, [], 'Browser runtime errors')
  console.log(`PASS: ${results.length} layout, math and interaction checks; no browser runtime errors`)
} finally {
  await writeFile(`${output}/browser-report.json`, JSON.stringify({ results, errors }, null, 2) + '\n')
  await browser.close()
}
