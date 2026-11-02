import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,writeFile} from 'node:fs/promises'
import {spawn} from 'node:child_process'
import path from 'node:path'
const base=process.env.QA_URL||'http://127.0.0.1:5194',out='raw_materials/bieu-dien-tri-thuc/reviews/bai-04/browser'
await mkdir(out,{recursive:true})
let server,browser;const checks=[],errors=[]
try{
 if(!process.env.QA_URL){
  server=spawn(process.execPath,['node_modules/vitepress/bin/vitepress.js','dev','docs','--port','5194','--host','127.0.0.1','--strictPort'],{cwd:process.cwd(),windowsHide:true,stdio:'ignore'})
  let ready=false
  for(let i=0;i<60;i++){try{if((await fetch(base,{signal:AbortSignal.timeout(1500)})).ok){ready=true;break}}catch{};await new Promise(r=>setTimeout(r,500))}
  assert.ok(ready,'Preview must start')
 }
 browser=await puppeteer.launch({headless:true,executablePath:process.env.CHROME_PATH||'C:/Program Files/Google/Chrome/Application/chrome.exe'})
 const page=await browser.newPage();page.on('pageerror',e=>errors.push(e.message))
 const finish=()=>page.$eval('.adversarial-lab .step-slider input',e=>{e.value=e.max;e.dispatchEvent(new Event('input',{bubbles:true}))})
 for(const width of [1280,375,360]){
  await page.setViewport({width,height:900});await page.goto(base+'/agy-plans/adversarial-preview.html',{waitUntil:'domcontentloaded',timeout:120000});await page.waitForSelector('.adversarial-lab',{timeout:120000});await page.waitForSelector('.ttt-lab',{timeout:120000});console.log('Loaded preview '+width+'px')
  for(const mode of ['minimax','alphabeta']){
   await page.select('.game-settings select',mode)
   for(const [id,value]of [['classic',3],['small',8],['deep',10],['hidden',10],['equal',5],['negative',-4],['horizon',1],['opponent',10]]){
    await page.select('.game-settings label:nth-child(2) select',id);await finish()
    assert.match(await page.$eval('.game-result',e=>e.textContent),new RegExp('Giá trị gốc: '+value+'\\.'))
   }
   checks.push(`${width}px ${mode}: all eight input trees`)
  }
  await page.select('.game-settings select','alphabeta');await page.select('.game-settings label:nth-child(2) select','hidden');await finish()
  await page.$eval('.tree-list',e=>e.open=true)
  assert.match(await page.$eval('.tree-list',e=>e.textContent),/R12 · MAX≥ 100/)
  assert.match(await page.$eval('.game-stack',e=>e.textContent),/Đã đánh giá 5 nút/)
  await page.select('.game-settings label:nth-child(3) select','reverse');await finish();assert.match(await page.$eval('.game-result',e=>e.textContent),/Giá trị gốc: 10/)
  await page.select('.game-settings label:nth-child(3) select','original')
  await page.select('.game-settings label:nth-child(2) select','horizon');await page.select('.game-settings label:nth-child(4) select','1');await finish();assert.match(await page.$eval('.game-result',e=>e.textContent),/Giá trị gốc: 5/)
  await page.select('.game-settings label:nth-child(4) select','2');await finish();assert.match(await page.$eval('.game-result',e=>e.textContent),/Giá trị gốc: 1/)
  checks.push(`${width}px: bounds, pruning, reversed order and depth reversal`)
  const before=await page.$eval('.game-status',e=>e.textContent);await page.click('.adversarial-lab button[aria-label="Lùi một bước"]');await page.click('.adversarial-lab button[aria-label="Tiến một bước"]');assert.equal(await page.$eval('.game-status',e=>e.textContent),before)
  await page.click('.game-code .code-title button');await page.waitForFunction(()=>document.querySelector('.game-code .code-title button').textContent.includes('Đã chép'))
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),false)
  await (await page.$('.adversarial-lab')).screenshot({path:`${out}/tree-${width}.png`})
  checks.push(`${width}px: replay, clipboard and no page overflow`)
  await page.select('.ttt-settings select','win');await page.click('.ttt-actions button');assert.match(await page.$eval('.ttt-status',e=>e.textContent),/X đã thắng/)
  await page.click('.ttt-actions button:nth-child(2)');assert.match(await page.$eval('.ttt-status',e=>e.textContent),/Lượt X/)
  await page.select('.ttt-settings select','block');await page.click('.ttt-actions button');assert.equal(await page.$eval('.ttt-board button:nth-child(3)',e=>e.textContent),'O')
  await page.select('.ttt-settings select','empty')
  for(let i=0;i<9;i++)await page.click('.ttt-actions button')
  assert.match(await page.$eval('.ttt-status',e=>e.textContent),/Ván đấu hòa/)
  await (await page.$('.ttt-lab')).screenshot({path:`${out}/tic-tac-toe-${width}.png`})
  checks.push(`${width}px: win, block, undo and optimal self-play draw`)
 }
 await page.$eval('.game-edit',e=>e.open=true);await page.$eval('.game-edit textarea',e=>{e.value='[]';e.dispatchEvent(new Event('input',{bubbles:true}))});await page.click('.game-edit button');await page.waitForSelector('.game-edit [role="alert"]');checks.push('Invalid custom tree rejected')
 await page.$eval('.ttt-edit',e=>e.open=true);await page.$eval('.ttt-edit input',e=>{e.value='OOOXXX...';e.dispatchEvent(new Event('input',{bubbles:true}))});await page.click('.ttt-edit button');await page.waitForSelector('.ttt-edit [role="alert"]');checks.push('Unreachable tic-tac-toe board rejected')
 await page.emulateMediaFeatures([{name:'prefers-reduced-motion',value:'reduce'}]);await page.reload({waitUntil:'networkidle0'});await page.waitForSelector('.motion-note')
 await page.focus('.adversarial-lab button[aria-label="Tiến một bước"]');await page.keyboard.press('Enter');checks.push('Reduced motion and keyboard step controls')
 await page.click('.adversarial-lab .play-toggle');await page.waitForFunction(()=>Number(document.querySelector('.adversarial-lab .step-slider input').value)>1);await page.click('.adversarial-lab .play-toggle')
 const paused=await page.$eval('.adversarial-lab .step-slider input',e=>e.value);await new Promise(r=>setTimeout(r,1200));assert.equal(await page.$eval('.adversarial-lab .step-slider input',e=>e.value),paused);checks.push('Play and pause preserve state')
 assert.deepEqual(errors,[])
 await writeFile(out+'/results.json',JSON.stringify({checks,errors},null,2)+'\n');console.log(`PASS ${checks.length} browser checks, no runtime errors`)
}finally{await browser?.close();server?.kill()}
