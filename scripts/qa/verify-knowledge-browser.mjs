import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import { course } from '../../src/content/courses/bieu-dien-tri-thuc/course.mjs'

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:5188'
const output = 'qa/knowledge-09-11'
await mkdir(output, { recursive: true })
for (let attempt = 0; attempt < 60; attempt++) {
  const ready = await fetch(base + '/@vite/client', { signal: AbortSignal.timeout(2000) }).then(response => response.ok, () => false)
  if (ready) break
  if (attempt === 59) throw Error('Preview did not become ready')
  await new Promise(resolve => setTimeout(resolve, 1000))
}
const browser = await puppeteer.launch({
  headless: true,
  executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe',
  args: ['--no-sandbox']
})
const results = [], issues = [], errors = []
const root = '/bieu-dien-tri-thuc/bai-giang/'
try {
  const page = await browser.newPage()
  page.on('pageerror', error => errors.push(error.message))
  const goto = async route => {
    const response = await page.goto(base + root + route + '.html', { waitUntil: 'networkidle0', timeout: 120000 })
    assert.equal(response.status(), 200, route)
    await page.waitForSelector('.vp-doc')
    await page.evaluate(() => document.documentElement.classList.remove('dark'))
  }
  const finish = async selector => {
    await page.$eval(selector + ' input[type=range]', element => {
      element.value = element.max
      element.dispatchEvent(new Event('input', { bubbles: true }))
    })
  }
  const setRange = async (selector, value) => {
    await page.$eval(selector, (element, next) => {
      element.value = next
      element.dispatchEvent(new Event('input', { bubbles: true }))
    }, value)
  }
  for (const width of [375, 1440]) {
    await page.setViewport({ width, height: 950 })
    for (const lesson of course.lessons.filter(lesson => [9, 10, 11].includes(lesson.number))) {
      const routes = [lesson.slug, ...lesson.topicGroups.flatMap(group => group.topics.map(topic => lesson.slug + '/' + topic.slug))]
      for (const route of routes) {
        await goto(route)
        if (route === lesson.slug) {
          const count = course.slides.filter(slide => slide.note === lesson.slug).length
          await page.waitForSelector('.knowledge-review select')
          assert.equal(await page.$$eval('.knowledge-review option', elements => elements.length), count)
          for (let index = 0; index < count; index++) {
            await page.select('.knowledge-review select', String(index))
            assert((await page.$eval('.knowledge-review article h3', element => element.textContent)).length > 0)
          }
        }
        const overflow = await page.evaluate(() => {
          const content = document.querySelector('.vp-doc')
          const bounds = content.getBoundingClientRect()
          const math = [...content.querySelectorAll('mjx-container')].filter(element => {
            const rect = element.getBoundingClientRect()
            const svg = element.querySelector('svg')
            return rect.width > bounds.width + 2 || (svg && svg.getBoundingClientRect().width > bounds.width + 2)
          }).map(element => element.textContent.slice(0, 80))
          return { page: document.documentElement.scrollWidth > innerWidth + 2, math }
        })
        if (overflow.page || overflow.math.length) issues.push({ width, route, ...overflow })
        results.push({ width, route, kind: 'page' })
      }
    }
    await goto('09-prolog/sld-va-quay-lui')
    const prolog = 'section[aria-label="Vết chạy quay lui trong Prolog"]'
    await finish(prolog)
    assert.equal(await page.$eval(prolog + ' dd:last-child', element => element.textContent), 'charlie, olivia, jack')
    await page.click(prolog + ' input[type=checkbox]')
    await finish(prolog)
    assert.equal(await page.$eval(prolog + ' dd:last-child', element => element.textContent), 'charlie, olivia')
    await setRange(prolog + ' input[type=range]', 4)
    assert.match(await page.$eval(prolog, element => element.textContent), /thất bại|Arthur|arthur/)
    await goto('09-prolog/so-hoc-va-dieu-kien')
    await finish('.prolog-recursion')
    assert.match(await page.$eval('.prolog-recursion', element => element.textContent), /G = 5/)
    await page.select('.prolog-recursion select', 'last')
    await finish('.prolog-recursion')
    assert.match(await page.$eval('.prolog-recursion', element => element.textContent), /X = 7/)
    await goto('10-bieu-dien-tri-thuc/su-kien-va-thoi-gian')
    const interval = 'section[aria-label="Quan hệ giữa hai khoảng thời gian"]'
    const observed = new Set()
    for (const [start, length] of [[0,1],[2,3],[3,3],[5,3],[6,2],[6,3],[5,4],[4,5],[5,5],[4,6],[6,4],[9,1],[10,1]]) {
      await setRange(interval + ' label:nth-child(1) input', start)
      await setRange(interval + ' label:nth-child(2) input', length)
      observed.add(await page.$eval(interval + ' strong', element => element.textContent))
    }
    assert.equal(observed.size, 13)
    await goto('10-bieu-dien-tri-thuc/ca-the-lop-va-bo-phan')
    const ontology = 'section[aria-label="Suy luận thành viên qua lớp cha"]'
    await finish(ontology)
    assert.match(await page.$eval(ontology + ' ul', element => element.textContent), /Động vật/)
    await page.click(ontology + ' input[type=checkbox]')
    await finish(ontology)
    assert.doesNotMatch(await page.$eval(ontology + ' ul', element => element.textContent), /Động vật/)
    await goto('11-mdp/lap-gia-tri')
    await setRange('.mdp-grid .simulation-controls input[type=range]', 2)
    assert.match(await page.$eval('.mdp-grid .mdp-cells', element => element.textContent), /0.7200/)
    await page.select('.mdp-settings label:nth-child(4) select', 'entry')
    await setRange('.mdp-grid .simulation-controls input[type=range]', 1)
    assert.match(await page.$eval('.mdp-grid .mdp-cells', element => element.textContent), /0.8000/)
    await (await page.$('.mdp-grid')).screenshot({ path: output + '/mdp-' + width + '.png' })
    await goto('11-mdp/lap-chinh-sach')
    await finish('.mdp-policy')
    assert.match(await page.$eval('.mdp-policy', element => element.textContent), /10.0000/)
    await page.select('.mdp-policy select', '0.5')
    await finish('.mdp-policy')
    assert.match(await page.$eval('.mdp-policy', element => element.textContent), /3.0000/)
    await page.evaluate(() => document.documentElement.classList.add('dark'))
    await (await page.$('.mdp-policy')).screenshot({ path: output + '/policy-dark-' + width + '.png' })
    await page.evaluate(() => document.documentElement.classList.remove('dark'))
    results.push({ width, kind: 'interactions', checks: 13 + 8 })
    console.log(width + 'px pages and interactions passed')
  }
  await writeFile(output + '/browser.json', JSON.stringify({ base, results, issues, errors }, null, 2))
  assert.deepEqual(errors, [])
  assert.deepEqual(issues, [])
} finally {
  await browser.close()
}
