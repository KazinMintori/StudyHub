import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,writeFile} from 'node:fs/promises'
const base=process.env.QA_URL||'http://127.0.0.1:5198',out='raw_materials/bieu-dien-tri-thuc/reviews/bai-06/browser'
await mkdir(out,{recursive:true});const browser=await puppeteer.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'}),checks=[],errors=[]
try{
 const p=await browser.newPage();p.on('pageerror',e=>errors.push(e.message))
 const finish=s=>p.$eval(s+' .step-slider input',e=>{e.value=e.max;e.dispatchEvent(new Event('input',{bubbles:true}))})
 const set=(s,v)=>p.select(s,v)
 for(const width of [1280,375,360]){
  await p.setViewport({width,height:900});await p.goto(base+'/agy-plans/local-csp-preview.html',{waitUntil:'domcontentloaded',timeout:120000});await p.waitForSelector('.csp-arc .arc-status',{timeout:120000})
  for(const mode of ['hill','anneal','tabu','beam']){await set('.local-landscape .local-settings select',mode);await finish('.local-landscape');assert.ok((await p.$eval('.local-landscape .local-status',e=>e.textContent)).length>10)}checks.push(`${width}: four landscape algorithms`)
  await set('.local-landscape .local-settings select','hill');await finish('.local-landscape');assert.match(await p.$eval('.local-status',e=>e.textContent),/cục bộ/)
  await p.click('.local-landscape button[aria-label="Lùi một bước"]');await p.click('.local-landscape button[aria-label="Tiến một bước"]');assert.match(await p.$eval('.local-status',e=>e.textContent),/cục bộ/);checks.push(`${width}: reversible trace`)
  for(const mode of ['hill','anneal','minconflicts']){await set('.queen-settings label:nth-child(2) select',mode);await finish('.local-queens');assert.ok((await p.$eval('.queen-status',e=>e.textContent)).length>5)}
  await p.click('.queen-board button[aria-label^="Cột 1, hàng 1"]');assert.equal(await p.$eval('.local-queens .step-slider input',e=>e.value),'0');checks.push(`${width}: three queen algorithms and editable board`)
  await finish('.tsp-two-opt');assert.match(await p.$eval('.tsp-status',e=>e.textContent),/14\.000/);checks.push(`${width}: 2-opt crossing tour 16 to 14`)
  await finish('.genetic-search');assert.match(await p.$eval('.genetic-status',e=>e.textContent),/8 thế hệ/);await p.$eval('.ox-panel',e=>e.open=true);const child=await p.$$eval('.ox-panel > div:last-of-type .genes span',e=>e.map(x=>Number(x.textContent)));assert.deepEqual(child,[5,8,7,2,1,6,3,4]);checks.push(`${width}: GA generations and permutation OX`)
  await set('.csp-search .csp-settings select','triangle')
  for(const method of ['none','fc','mac']){await set('.csp-search .csp-settings label:nth-child(2) select',method);await finish('.csp-search');assert.match(await p.$eval('.csp-status',e=>e.textContent),/vô nghiệm/)}checks.push(`${width}: plain, FC and MAC prove triangle unsatisfiable`)
  await set('.csp-search .csp-settings select','queens');await finish('.csp-search');assert.match(await p.$eval('.csp-status',e=>e.textContent),/đầy đủ/);checks.push(`${width}: complete queen assignment`)
  await set('.csp-search .csp-settings select','crossword');await finish('.csp-search');assert.match(await p.$eval('.csp-status',e=>e.textContent),/đầy đủ/);assert.match(await p.$eval('.csp-search .csp-domains',e=>e.textContent),/NON/);checks.push(`${width}: crossword candidate and crossing constraints`)
  await set('.csp-arc .arc-settings select','triangle');await finish('.csp-arc');assert.match(await p.$eval('.arc-status',e=>e.textContent),/chưa chứng minh/)
  await set('.csp-arc .arc-settings select','chain');await finish('.csp-arc');assert.deepEqual(await p.$$eval('.csp-arc .domain-values',es=>es.map(e=>[...e.querySelectorAll('span:not(.deleted)')].map(x=>x.textContent))),[['1'],['2'],['3']]);checks.push(`${width}: AC-3 triangle counterexample and chain fixed point`)
  await set('.csp-arc .arc-settings select','tree');await set('.csp-arc .arc-settings label:nth-child(2) select','tree');await finish('.csp-arc');assert.match(await p.$eval('.arc-status',e=>e.textContent),/một nghiệm/)
  await set('.csp-arc .arc-settings select','triangle');await p.waitForSelector('.csp-arc [role="alert"]');checks.push(`${width}: tree solver succeeds and refuses a cycle`)
  await p.click('.local-landscape .search-trace-code button');await p.waitForFunction(()=>document.querySelector('.local-landscape .search-trace-code button').textContent.includes('Đã chép'));checks.push(`${width}: syntax listing copy`)
  assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),false)
  for(const selector of ['.local-landscape','.local-queens','.tsp-two-opt','.genetic-search','.csp-search'])await (await p.$(selector)).screenshot({path:`${out}/${selector.slice(1)}-${width}.png`})
 }
 await p.$eval('.csp-input',e=>e.open=true);await p.$eval('.csp-input textarea',e=>{e.value='{}';e.dispatchEvent(new Event('input',{bubbles:true}))});await p.click('.csp-input button');await p.waitForSelector('.csp-input [role="alert"]');checks.push('Invalid CSP rejected')
 await p.emulateMediaFeatures([{name:'prefers-reduced-motion',value:'reduce'}]);await p.reload({waitUntil:'domcontentloaded'});await p.waitForSelector('.motion-note');await p.focus('.local-landscape button[aria-label="Tiến một bước"]');await p.keyboard.press('Enter');assert.equal(await p.$eval('.local-landscape .step-slider input',e=>e.value),'1');checks.push('Keyboard and reduced motion')
 await p.click('.local-landscape .play-toggle');await p.waitForFunction(()=>Number(document.querySelector('.local-landscape .step-slider input').value)>1);await p.click('.local-landscape .play-toggle');const paused=await p.$eval('.local-landscape .step-slider input',e=>e.value);await new Promise(r=>setTimeout(r,1100));assert.equal(await p.$eval('.local-landscape .step-slider input',e=>e.value),paused);checks.push('Play and pause use the same trace')
 await p.emulateMediaFeatures([{name:'prefers-color-scheme',value:'light'}]);await p.evaluate(()=>{localStorage.removeItem('vitepress-theme-appearance');document.documentElement.classList.remove('dark')});await p.setViewport({width:1280,height:1000});await p.reload({waitUntil:'networkidle0'});await p.waitForSelector('.csp-arc .arc-status');await (await p.$('.local-landscape')).screenshot({path:out+'/landscape-light-1280.png'});await (await p.$('.csp-arc')).screenshot({path:out+'/arc-light-1280.png'});checks.push('Light palette rendering')
 assert.deepEqual(errors,[]);await writeFile(out+'/results.json',JSON.stringify({checks,errors},null,2)+'\n');console.log(`PASS ${checks.length} interaction checks, no page overflow or runtime errors`)
}finally{await browser.close()}
