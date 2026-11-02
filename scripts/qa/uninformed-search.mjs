import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,writeFile} from 'node:fs/promises'
const base=process.env.QA_URL||'http://127.0.0.1:5189'
const route=process.env.QA_ROUTE||'/agy-plans/search-lab-preview.html'
const output='raw_materials/bieu-dien-tri-thuc/reviews/bai-02/browser'
await mkdir(output,{recursive:true})
const browser=await puppeteer.launch({headless:true,executablePath:process.env.CHROME_PATH||'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const errors=[],checks=[]
try{
const page=await browser.newPage();page.on('pageerror',e=>errors.push(e.message))
const finish=async()=>{await page.$eval('.search-lab .step-slider input',e=>{e.value=e.max;e.dispatchEvent(new Event('input',{bubbles:true}))})}
for(const width of [1280,375,360]){
 await page.setViewport({width,height:900});await page.goto(base+route,{waitUntil:'networkidle0',timeout:120000});await page.waitForSelector('.search-lab')
 for(const mode of ['bfs','dfs','ucs','ids','dijkstra']){
  await page.select('.search-settings select',mode)
  for(const example of ['weighted','unit','early','beyond','cycle','unreachable','initial']){
   await page.select('.search-settings label:nth-child(2) select',example);await finish()
   const status=await page.$eval('.search-status',e=>e.textContent)
   assert.match(status,mode==='dijkstra'?/Đã tính xong/:example==='unreachable'?/Không tìm thấy/:/thành công/)
   const text=await page.$eval('.search-frontier',e=>e.textContent)
   if(example==='weighted')assert.match(text,['ucs','dijkstra'].includes(mode)?/Tổng chi phí 7/:/Tổng chi phí 9/)
   if(example==='early')assert.match(text,['ucs','dijkstra'].includes(mode)?/Tổng chi phí 2/:/Tổng chi phí 10/)
  }
  checks.push(`${width}px ${mode}: seven scenarios`)
 }
 await page.select('.search-settings label:nth-child(2) select','weighted');await page.select('.search-settings select','ucs')
 for(let i=0;i<6;i++)await page.click('.search-lab button[aria-label="Tiến một bước"]')
 const before=await page.$eval('.search-status',e=>e.textContent)
 await page.click('.search-lab button[aria-label="Lùi một bước"]');await page.click('.search-lab button[aria-label="Tiến một bước"]');assert.equal(await page.$eval('.search-status',e=>e.textContent),before)
 await page.click('.search-code-bar button');assert.match(await page.$eval('.search-code-bar button',e=>e.textContent),/Đã chép/)
 assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),false)
 await (await page.$('.search-lab')).screenshot({path:`${output}/lab-${width}.png`})
 checks.push(`${width}px: replay, copy and no horizontal overflow`)
 await page.select('.search-settings label:nth-child(2) select','beyond');await finish()
 assert.match(await page.$eval('.search-distances',e=>e.textContent),/C: ∞/)
 await page.select('.search-settings select','dijkstra');await finish()
 assert.match(await page.$eval('.search-distances',e=>e.textContent),/C: 8/)
 await page.$eval('.search-distances details',e=>e.open=true)
 await (await page.$('.search-distances')).screenshot({path:`${output}/ucs-dijkstra-${width}.png`})
 checks.push(`${width}px: UCS stops at the goal while Dijkstra finishes remaining distances`)
}
await page.$eval('.search-edit',e=>e.open=true)
await page.$eval('.search-edit textarea',e=>{e.value='invalid';e.dispatchEvent(new Event('input',{bubbles:true}))});await page.click('.search-edit button');await page.waitForSelector('.search-edit [role="alert"]')
checks.push('Invalid input rejected with a visible error')
await page.$eval('.search-edit textarea',e=>{e.value=JSON.stringify({S:[['A',1],['G',5]],A:[['G',1]],G:[]});e.dispatchEvent(new Event('input',{bubbles:true}))});await page.click('.search-edit button');await finish();assert.match(await page.$eval('.search-frontier',e=>e.textContent),/Tổng chi phí 2/)
checks.push('Custom graph updates and computes a new optimum')
await page.emulateMediaFeatures([{name:'prefers-reduced-motion',value:'reduce'}]);await page.select('.search-settings select','bfs');await page.click('.search-lab .play-toggle');assert.match(await page.$eval('.search-lab .play-toggle',e=>e.textContent),/Tạm dừng/);await page.select('.search-settings select','dfs');assert.doesNotMatch(await page.$eval('.search-lab .play-toggle',e=>e.textContent),/Tạm dừng/)
checks.push('Play stops when the problem changes and supports reduced motion')
if(process.env.QA_ALL==='1'){
 for(const width of [1280,375,360])for(const slug of ['mo-hinh-va-cay-tim-kiem','bfs-va-dfs','tim-kiem-chi-phi-deu','gioi-han-do-sau-va-ids','so-sanh-va-thuc-hanh']){
  await page.setViewport({width,height:900});await page.goto(base+'/bieu-dien-tri-thuc/bai-giang/02-tim-kiem-mu/'+slug+'.html',{waitUntil:'networkidle0',timeout:120000});await page.waitForSelector('h1');
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),false,slug+' '+width+' page overflow')
  assert.equal(await page.$$eval('mjx-container',items=>items.filter(e=>e.scrollWidth>e.clientWidth+2).length),0,slug+' '+width+' math overflow')
  checks.push(width+'px topic '+slug)
  if(width===375)await page.screenshot({path:output+'/'+slug+'-375.png'})
 }
}
assert.deepEqual(errors,[]);await writeFile(output+'/report.json',JSON.stringify({checks,errors},null,2)+'\n');console.log('PASS '+checks.length+' browser checks')
}finally{await browser.close()}
