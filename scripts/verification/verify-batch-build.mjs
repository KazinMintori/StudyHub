// A four-page fixture runs on GitHub before the full site build. It checks
// hydration and navigation between independently compiled batches.
import { mkdir, mkdtemp, writeFile, readFile, rm } from 'node:fs/promises'
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
let browser, server
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
export default { base:'/StudyHub/', title:'Kiểm tra chia đợt', lastUpdated:false, ignoreDeadLinks:true,
  head:[['link',{rel:'icon',href:'/StudyHub/figure.svg'}]],
  markdown:{math:true,config:md=>md.use(staticMathPlugin)},
  themeConfig:{nav:[{text:'Đến B',link:'/b'}]}, buildConcurrency:1 }
`)
  const interactive = `
<script setup>
import { ref } from 'vue'
const count=ref(0)
</script>
<button id="counter" @click="count++">{{ count }}</button>
`
  for (const [name, target] of [['index', 'b'], ['a', 'c'], ['b', 'a'], ['c', 'a']]) {
    await writeFile(path.join(docs, name + '.md'), `# Trang ${name}\n\n[Chuyển trang](/${target})\n\n$$\nE=mc^2\n$$\n\n<details><summary>Lời giải</summary><p>Điện thế bằng công trên điện tích.</p></details>\n\n![Hình: Tọa độ và năng lượng](/figure.svg)\n\n${interactive}`)
  }
  await writeFile(path.join(docs, 'public/figure.svg'), '<svg xmlns="http://www.w3.org/2000/svg" width="50" height="20"><text x="1" y="15">Energy</text></svg>')
  await writeFile(path.join(docs, 'public/embedded.html'), '<p>Tài liệu nhúng</p>')
  const plan = await planBuild(await resolveConfig(docs, 'build', 'production'), { maxPages: 2 })
  if (plan.batches.length !== 2) throw new Error('Fixture must have two batches')
  const planFile = path.join(fixture, 'plan.json')
  await writeFile(planFile, JSON.stringify(plan))
  const state = { pageMap: {}, files: new Map(), icons: new Set() }
  for (let index = 0; index < plan.batches.length; index++) {
    const batch = path.join(fixture, 'batch-' + index)
    await run(['scripts/build/build-batch-worker.mjs', 'batch', docs, planFile, String(index), batch])
    await mergeBatch(batch, output, state)
  }
  await finalizeBatches(output, plan, state)
  if (await readFile(path.join(output, 'embedded.html'), 'utf8') !== '<p>Tài liệu nhúng</p>') throw new Error('Public HTML changed')
  // Serve the emitted files without rebuilding them.
  server = await preview({ configFile:false, root:docs, base:'/StudyHub/', build:{outDir:output}, preview:{host:'127.0.0.1',port:0} })
  const port = server.httpServer.address().port
  browser = await puppeteer.launch({ executablePath:process.env.PUPPETEER_EXECUTABLE_PATH || '/usr/bin/google-chrome', headless:true, args:['--no-sandbox'] })
  const page = await browser.newPage()
  const errors = []
  page.on('pageerror', error => errors.push(error.message))
  page.on('console', message => { if (message.type() === 'error' || /hydration.*mismatch/i.test(message.text())) errors.push(message.text()) })
  await page.goto(`http://127.0.0.1:${port}/StudyHub/a.html`, {waitUntil:'networkidle0'})
  await page.waitForSelector('.static-math svg')
  await page.click('#counter')
  await page.waitForFunction(() => document.querySelector('#counter').textContent === '1')
  await page.evaluate(() => { window.fixtureNavigationMarker = 'same-document' })
  await page.click('.vp-doc a[href$="/c.html"]')
  await page.waitForFunction(() => location.pathname.endsWith('/c.html') && document.querySelector('.vp-doc h1')?.textContent.includes('Trang c'))
  if (await page.evaluate(() => window.fixtureNavigationMarker) !== 'same-document') throw new Error('Cross-batch navigation reloaded the document')
  await page.waitForSelector('.static-math svg')
  await page.click('#counter')
  await page.waitForFunction(() => document.querySelector('#counter').textContent === '1')
  await page.click('.vp-doc details summary')
  if (!await page.$eval('.vp-doc details', node => node.open)) throw new Error('Solution disclosure failed')
  if (!await page.$eval('.vp-doc img', node => node.complete && node.naturalWidth > 0)) throw new Error('Figure failed to load')
  if (errors.length) throw new Error(errors.join('\n'))
  console.log('Batched build fixture passed: Both routes, SPA navigation, hydration, math, figure and collapsed solution')
} finally {
  await browser?.close()
  if (server) await new Promise(resolve => server.httpServer.close(resolve))
  await rm(fixture, { recursive:true, force:true })
}
