// A four-page fixture runs on GitHub before the full site build. It checks
// hydration and navigation between independently compiled batches.
import { mkdir, mkdtemp, writeFile, readFile, rm, cp } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { spawn } from 'node:child_process'
import { preview } from 'vite'
import { resolveConfig } from 'vitepress'
import puppeteer from 'puppeteer'
import { planBuild } from '../build/page-batches.mjs'
import { mergeBatch, finalizeBatches } from '../build/merge-batches.mjs'

if (process.env.GITHUB_ACTIONS !== 'true') throw new Error('Build integration fixture runs on GitHub Actions only')
const root = fileURLToPath(new URL('../../', import.meta.url))
const temporaryRoot = path.join(root, 'tmp')
await mkdir(temporaryRoot, { recursive: true })
const fixture = await mkdtemp(path.join(temporaryRoot, 'batch-build-fixture-'))
const docs = path.join(fixture, 'docs')
const output = path.join(fixture, 'merged')
const realTheme = process.env.QA_REAL_THEME === '1'
const report = path.join(root, 'qa/batch-build-fixture')
let browser, server, page
const errors = []
const run = args => new Promise((resolve, reject) => {
  const child = spawn(process.execPath, args, { cwd: root, stdio: 'inherit', windowsHide: true })
  child.once('error', reject)
  child.once('exit', code => code === 0 ? resolve() : reject(new Error(`Fixture worker exited ${code}`)))
})
try {
  await mkdir(path.join(docs, '.vitepress'), { recursive: true })
  await mkdir(path.join(docs, 'public'), { recursive: true })
  await writeFile(path.join(docs, '.vitepress/config.mjs'), `
import { staticMathPlugin } from ${JSON.stringify(path.join(root, 'scripts/static-math-plugin.mjs').replaceAll('\\', '/'))}
import { vietnameseMathOptions } from ${JSON.stringify(path.join(root, 'scripts/math-fonts/vietnamese.mjs').replaceAll('\\', '/'))}
export default { base:'/StudyHub/', title:'Kiểm tra chia đợt', lastUpdated:false, ignoreDeadLinks:true,
  head:[['link',{rel:'icon',href:'/StudyHub/figure.svg'}]],
  markdown:{math:vietnameseMathOptions,config:md=>md.use(staticMathPlugin)},
  themeConfig:{nav:[{text:'Đến B',link:'/b'}]}, buildConcurrency:1 }
`)
  if (realTheme) {
    await mkdir(path.join(docs, '.vitepress/theme'), { recursive: true })
    await writeFile(path.join(docs, '.vitepress/theme/index.js'), `export { default } from ${JSON.stringify(path.join(root, 'src/app/theme.mjs').replaceAll('\\', '/'))}`)
    await writeFile(path.join(docs, '.vitepress/config.mjs'), `
import config from ${JSON.stringify(path.join(root, 'docs/.vitepress/config.mjs').replaceAll('\\', '/'))}
export default { ...config, base:'/StudyHub/', lastUpdated:false, srcExclude:[],
  themeConfig:{...config.themeConfig,nav:[{text:'Đến B',link:'/b'}]},buildConcurrency:1 }
`)
  }
  const interactive = name => `
<style scoped>
.batch-style-${name}{border:7px solid purple;padding:19px;display:flex}
@media(max-width:600px){.batch-style-${name}{padding:11px}}
</style>

<script setup>
import { ref } from 'vue'
import { useData } from 'vitepress'
${realTheme && name === 'a' ? `import PhilosophyPracticeChapter from ${JSON.stringify(path.join(root, 'src/features/philosophy/components/PhilosophyPracticeChapter.vue').replaceAll('\\', '/'))}` : ''}
${realTheme && name === 'b' ? `import ExamPractice from ${JSON.stringify(path.join(root, 'src/features/exam/components/ExamPractice.vue').replaceAll('\\', '/'))}
const bank = {id:'fixture',title:'Đề kiểm tra giao diện',questions:[
{id:'fixture-1',kind:'quiz',promptHtml:'<p>Chọn phương án A.</p>',correctKey:'A',options:[{key:'A',html:'<p>Phương án A</p>',explanationHtml:'<p>Đã chọn đúng.</p>'},{key:'B',html:'<p>Phương án B</p>',explanationHtml:'<p>Chọn phương án A.</p>'}]},
{id:'fixture-2',kind:'quiz',promptHtml:'<p>Câu tiếp theo.</p>',correctKey:'A',options:[{key:'A',html:'<p>Phương án A</p>'},{key:'B',html:'<p>Phương án B</p>'}]}
]}` : ''}
const count=ref(0)
const { frontmatter } = useData()
</script>
<button id="counter" @click="count++">{{ count }}</button>
<p id="frontmatter-probe">{{ frontmatter.course }}</p>
<div class="batch-style-${name}">Card ${name}</div>
${realTheme && name === 'a' ? '<PhilosophyPracticeChapter chapter-id="chuong-1" />' : ''}
${realTheme && name === 'b' ? '<ExamPractice :bank="bank" />' : ''}
`
  const vietnameseFormula = String.raw`$P(\text{một chuỗi})=p^k(1-p)^{n-k}$`
  for (const [name, target] of [['index', 'b'], ['a', 'b'], ['b', 'a'], ['C', 'a']]) {
    const course = ['b', 'C'].includes(name) ? 'toan-cho-ai' : 'bieu-dien-tri-thuc'
    await writeFile(path.join(docs, name + '.md'), `---\ncourse: ${course}\n---\n\n${realTheme ? '<CourseOverview />' : '# Trang ' + name}\n\n[Chuyển trang](/${target})\n\n$$\nE=mc^2\n$$\n\n${vietnameseFormula}\n\n<details><summary>Lời giải</summary><p>Điện thế bằng công trên điện tích.</p></details>\n\n![Hình: Tọa độ và năng lượng](/figure.svg)\n\n${interactive(name)}\n${name === 'a' ? '<div v-memo="[count]">{{ count }}</div>' : ''}`)
  }
  await writeFile(path.join(docs, 'public/figure.svg'), '<svg xmlns="http://www.w3.org/2000/svg" width="50" height="20"><text x="1" y="15">Energy</text></svg>')
  await writeFile(path.join(docs, 'public/embedded.html'), '<p>Tài liệu nhúng</p>')
  const plan = await planBuild(await resolveConfig(docs, 'build', 'production'), { maxPages: 2 })
  if (plan.batches.length !== 2) throw new Error('Fixture must have two batches')
  if (plan.batches.findIndex(batch => batch.pages.includes('a.md')) === plan.batches.findIndex(batch => batch.pages.includes('b.md'))) throw new Error('Navigation must cross batch boundaries')
  const planFile = path.join(fixture, 'plan.json')
  await writeFile(planFile, JSON.stringify(plan))
  const state = { pageMap: {}, files: new Map(), icons: new Set() }
  for (let index = 0; index < plan.batches.length; index++) {
    const batch = path.join(fixture, 'batch-' + index)
    await run(['scripts/build/build-batch-worker.mjs', 'batch', docs, planFile, String(index), batch])
    await mergeBatch(batch, output, state)
  }
  const buildReport = await finalizeBatches(output, plan, state)
  console.log('Shared stylesheet:', JSON.stringify(buildReport))
  if (await readFile(path.join(output, 'embedded.html'), 'utf8') !== '<p>Tài liệu nhúng</p>') throw new Error('Public HTML changed')
  // Serve the emitted files without rebuilding them.
  server = await preview({ configFile:false, root:docs, base:'/StudyHub/', build:{outDir:output}, preview:{host:'127.0.0.1',port:0} })
  const port = server.httpServer.address().port
  browser = await puppeteer.launch({ executablePath:process.env.PUPPETEER_EXECUTABLE_PATH || '/usr/bin/google-chrome', headless:true, args:['--no-sandbox'] })
  page = await browser.newPage()
  const frameworks = new Set()
  page.on('request', request => { if (/\/framework\.[^/]+\.js$/.test(request.url())) frameworks.add(request.url()) })
  await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen', '1'))
  page.on('pageerror', error => errors.push(error.message))
  page.on('console', message => { if (message.type() === 'error' || /hydration.*mismatch/i.test(message.text())) errors.push(message.text()) })
  async function checkStyle(name, mobile = false) {
    const style = await page.$eval(`.batch-style-${name}`, element => {
      const css = getComputedStyle(element)
      return { display: css.display, border: css.borderTopWidth, padding: css.paddingTop }
    })
    if (style.display !== 'flex' || style.border !== '7px' || style.padding !== (mobile ? '11px' : '19px')) throw Error(`Missing cross-batch CSS on ${name}: ${JSON.stringify(style)}`)
  }
  await page.goto(`http://127.0.0.1:${port}/StudyHub/a.html`, {waitUntil:'networkidle0'})
  await page.waitForSelector('.static-math svg')
  await page.waitForSelector('.static-math svg [data-c="1ED9"]')
  await checkStyle('a')
  if (await page.$('.static-math svg text')) throw Error('Vietnamese math fell back to unmeasured browser glyphs')
  await page.$eval('#counter', button => button.click())
  await page.waitForFunction(() => document.querySelector('#counter').textContent === '1')
  await page.evaluate(() => { window.fixtureNavigationMarker = 'same-document' })
  await page.$eval('.vp-doc a[href$="/b.html"]', link => link.click())
  await page.waitForFunction(() => location.pathname.endsWith('/b.html') && document.querySelector('#frontmatter-probe')?.textContent.trim() === 'toan-cho-ai')
  if (await page.evaluate(() => window.fixtureNavigationMarker) !== 'same-document') throw new Error('Cross-batch navigation reloaded the document')
  await page.waitForSelector('.static-math svg')
  await checkStyle('b')
  if (realTheme) {
    const styled = await page.$eval('.exam-practice', el => getComputedStyle(el).maxWidth === '860px')
    if (!styled) throw Error('ExamPractice lost its CSS after SPA navigation')
    await page.click('.exam-choice__radio')
    await page.waitForSelector('.exam-choice.is-selected')
    await page.click('.exam-nav-btn--next')
    await page.waitForFunction(() => location.search.includes('fixture-2'))
  }
  await page.$eval('#counter', button => button.click())
  await page.waitForFunction(() => document.querySelector('#counter').textContent === '1')
  if (realTheme && frameworks.size !== 1) throw Error('Cross-batch navigation downloaded another native Vue runtime')
  await page.$eval('.vp-doc details summary', summary => summary.click())
  if (!await page.$eval('.vp-doc details', node => node.open)) throw new Error('Solution disclosure failed')
  if (!await page.$eval('.vp-doc img', node => node.complete && node.naturalWidth > 0)) throw new Error('Figure failed to load')
  await page.reload({ waitUntil: 'networkidle0' })
  await page.waitForSelector('#frontmatter-probe')
  await page.$eval('.vp-doc a[href$="/a.html"]', link => link.click())
  await page.waitForFunction(() => location.pathname.endsWith('/a.html') && document.querySelector('#frontmatter-probe')?.textContent.trim() === 'bieu-dien-tri-thuc')
  await checkStyle('a')
  if (realTheme) {
    const cards = await page.$eval('.practice-test-list', el => getComputedStyle(el).display === 'grid' && [...el.querySelectorAll('li > a')].every(card => parseFloat(getComputedStyle(card).borderTopWidth) > 0 && parseFloat(getComputedStyle(card).borderRadius) > 0))
    if (!cards) throw Error('Philosophy practice links lost their card layout after SPA navigation')
  }
  await page.$eval('#counter', button => button.click())
  await page.waitForFunction(() => document.querySelector('#counter').textContent === '1')
  await mkdir(report, { recursive: true })
  await page.screenshot({ path: path.join(report, 'practice-cards-desktop.png'), fullPage: true })
  await page.setViewport({ width: 375, height: 900 })
  await checkStyle('a', true)
  if (realTheme) {
    const oneColumn = await page.$eval('.practice-test-list', el => getComputedStyle(el).gridTemplateColumns.split(' ').length === 1)
    if (!oneColumn) throw Error('Practice cards must use one column on a phone')
  }
  await page.screenshot({ path: path.join(report, 'practice-cards-mobile.png'), fullPage: true })
  await page.$eval('.vp-doc a[href$="/b.html"]', link => link.click())
  await page.waitForFunction(() => location.pathname.endsWith('/b.html'))
  await checkStyle('b', true)
  await page.goBack({ waitUntil: 'networkidle0' })
  await page.waitForFunction(() => location.pathname.endsWith('/a.html'))
  await checkStyle('a', true)
  if (errors.length) throw new Error(errors.join('\n'))
  console.log('Batched build fixture passed: Both cold starts, SPA navigation and Back, shared CSS, mobile cards, interactive exam, hydration, math, figure and collapsed solution')
} catch (error) {
  await mkdir(report, { recursive: true })
  const diagnostic = { message: error.message, errors, ...(page ? await page.evaluate(() => ({ url: location.href, titles: [...document.querySelectorAll('h1')].map(element => element.textContent), probe: document.querySelector('#frontmatter-probe')?.textContent, text: document.body.textContent.slice(0, 1800) })).catch(() => ({})) : {}) }
  console.error(JSON.stringify(diagnostic, null, 2))
  await writeFile(path.join(report, 'failure.json'), JSON.stringify(diagnostic, null, 2))
  await page?.screenshot({ path: path.join(report, 'failure.png') }).catch(() => {})
  await cp(output, path.join(report, 'site'), { recursive: true }).catch(() => {})
  throw error
} finally {
  await browser?.close()
  if (server) await new Promise(resolve => server.httpServer.close(resolve))
  await rm(fixture, { recursive:true, force:true })
}
