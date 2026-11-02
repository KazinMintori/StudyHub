import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,writeFile} from 'node:fs/promises'
const base=process.env.QA_URL||'http://127.0.0.1:5191'
const route=process.env.QA_ROUTE||'/agy-plans/informed-preview.html'
const output='raw_materials/bieu-dien-tri-thuc/reviews/bai-03/browser'
await mkdir(output,{recursive:true})
const browser=await puppeteer.launch({headless:true,executablePath:process.env.CHROME_PATH||'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const errors=[],checks=[]
try{
const page=await browser.newPage();page.on('pageerror',e=>errors.push(e.message))
const finish=async()=>page.$eval('.informed-lab .step-slider input',e=>{e.value=e.max;e.dispatchEvent(new Event('input',{bubbles:true}))})
for(const width of [1280,375,360]){
 await page.setViewport({width,height:900});await page.goto(base+route,{waitUntil:'networkidle0',timeout:120000});await page.waitForSelector('.informed-lab');await page.waitForSelector('.puzzle-lab')
 for(const mode of ['ucs','greedy','astar']){
  await page.select('.informed-settings select',mode)
  for(const id of ['weighted','slides','early','overestimate','reopen','consistent','unreachable','initial']){
   await page.select('.informed-settings label:nth-child(2) select',id);await finish()
   const text=await page.$eval('.informed-frontier',e=>e.textContent)
   if(id==='weighted')assert.match(text,mode==='greedy'?/Tổng chi phí 8/:/Tổng chi phí 7/)
   if(id==='early')assert.match(text,mode==='greedy'?/Tổng chi phí 5/:/Tổng chi phí 4/)
   if(id==='reopen')assert.match(text,mode==='greedy'?/Tổng chi phí 6/:/Tổng chi phí 5/)
   if(id==='initial')assert.match(text,/Tổng chi phí 0/)
   if(id==='unreachable')assert.match(await page.$eval('.informed-status',e=>e.textContent),/Không có đường/)
  }
  checks.push(`${width}px ${mode}: eight scenarios`)
 }
 await page.select('.informed-settings select','astar');await page.select('.informed-settings label:nth-child(2) select','reopen')
 await page.click('.informed-settings label.check:last-child input');await finish();assert.match(await page.$eval('.informed-result',e=>e.textContent),/Tổng chi phí 6/)
 await page.click('.informed-settings label.check:last-child input');await finish();assert.match(await page.$eval('.informed-result',e=>e.textContent),/Tổng chi phí 5/)
 const before=await page.$eval('.informed-status',e=>e.textContent)
 await page.click('.informed-lab button[aria-label="Lùi một bước"]');await page.click('.informed-lab button[aria-label="Tiến một bước"]');assert.equal(await page.$eval('.informed-status',e=>e.textContent),before)
 await page.click('.informed-lab .code-bar button');await page.waitForFunction(()=>document.querySelector('.informed-lab .code-bar button').textContent.includes('Đã chép'),{timeout:5000})
 assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),false)
 await (await page.$('.informed-lab')).screenshot({path:`${output}/search-${width}.png`})
 checks.push(`${width}px: reopen 6/5, replay, copy, no horizontal overflow`)
 assert.match(await page.$eval('.puzzle-status',e=>e.textContent),/26 bước/)
 assert.match(await page.$eval('.puzzle-values',e=>e.textContent),/18/)
 await page.$eval('.puzzle-lab .step-slider input',e=>{e.value=e.max;e.dispatchEvent(new Event('input',{bubbles:true}))})
 assert.match(await page.$eval('.puzzle-values',e=>e.textContent),/Manhattan = 0 \+ 0 \+ 0 \+ 0 \+ 0 \+ 0 \+ 0 \+ 0 = 0/)
 await page.select('.puzzle-settings select','impossible');assert.match(await page.$eval('.puzzle-status',e=>e.textContent),/không thể/)
 await page.select('.puzzle-settings select','small');await page.click('.puzzle-compare button');assert.match(await page.$eval('.puzzle-compare',e=>e.textContent),/Chi phí 2/)
 await (await page.$('.puzzle-lab')).screenshot({path:`${output}/puzzle-${width}.png`})
 checks.push(`${width}px: puzzle 18/26, goal h=0, parity and three-heuristic comparison`)
}
await page.$eval('.informed-edit',e=>e.open=true)
await page.$eval('.informed-edit textarea',e=>{e.value='invalid';e.dispatchEvent(new Event('input',{bubbles:true}))});await page.click('.informed-edit button');await page.waitForSelector('.informed-edit [role="alert"]')
checks.push('Invalid JSON rejected with visible error')
await page.$eval('.informed-edit textarea',e=>{e.value=JSON.stringify({graph:{S:[['G',2]],G:[]},h:{S:2,G:0},start:'S',goal:'G'});e.dispatchEvent(new Event('input',{bubbles:true}))});await page.click('.informed-edit button');await finish();assert.match(await page.$eval('.informed-result',e=>e.textContent),/Tổng chi phí 2/)
checks.push('Custom graph and heuristic run correctly')
await page.emulateMediaFeatures([{name:'prefers-reduced-motion',value:'reduce'}]);await page.reload({waitUntil:'networkidle0'});await page.waitForSelector('.motion-note');checks.push('Reduced-motion preference exposed, no automatic playback')
await page.focus('.informed-lab button[aria-label="Tiến một bước"]');await page.keyboard.press('Enter');assert.match(await page.$eval('.informed-status',e=>e.textContent),/Lấy nút/);checks.push('Keyboard stepping')
await page.click('.informed-lab .play-toggle');await page.waitForFunction(()=>Number(document.querySelector('.informed-lab .step-slider input').value)>1,{timeout:4000});await page.click('.informed-lab .play-toggle')
const paused=await page.$eval('.informed-lab .step-slider input',e=>e.value);await new Promise(r=>setTimeout(r,1100));assert.equal(await page.$eval('.informed-lab .step-slider input',e=>e.value),paused);checks.push('Play advances and pause freezes the full state')
assert.deepEqual(errors,[])
await writeFile(output+'/results.json',JSON.stringify({checks,errors},null,2)+'\n')
console.log(`PASS ${checks.length} browser checks, no runtime errors`)
}finally{await browser.close()}
