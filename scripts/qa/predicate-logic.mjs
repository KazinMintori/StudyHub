import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,writeFile} from 'node:fs/promises'
const base=process.env.QA_URL||'http://127.0.0.1:5199',out='raw_materials/bieu-dien-tri-thuc/reviews/bai-08/browser'
await mkdir(out,{recursive:true});const browser=await puppeteer.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'}),checks=[],errors=[]
try{
 const p=await browser.newPage();p.on('pageerror',e=>errors.push(e.message));const finish=s=>p.$eval(s+' .step-slider input',e=>{e.value=e.max;e.dispatchEvent(new Event('input',{bubbles:true}))})
 for(const width of [1280,375,360]){
  await p.setViewport({width,height:900});await p.goto(base+'/agy-plans/predicate08-preview.html',{waitUntil:'domcontentloaded',timeout:120000});await p.waitForSelector('.predicate-resolution .predicate-status',{timeout:120000})
  await p.select('.predicate-quantifier .predicate-settings select','identity');await finish('.predicate-quantifier');assert.match(await p.$eval('.predicate-quantifier .predicate-status',e=>e.textContent),/Kết quả Đúng/);await p.select('.predicate-quantifier .predicate-settings label:nth-child(2) select','ea');await finish('.predicate-quantifier');assert.match(await p.$eval('.predicate-quantifier .predicate-status',e=>e.textContent),/Kết quả Sai/);checks.push(`${width}: mixed quantifier countermodel`)
  await p.select('.predicate-quantifier .predicate-settings select','empty');await p.click('.relation-grid button');assert.equal(await p.$eval('.predicate-quantifier .step-slider input',e=>e.value),'0');checks.push(`${width}: editable relation matrix resets trace`)
  for(const [id,pattern]of [['simple',/thành công/],['nested',/thành công/],['shared',/Không hợp nhất/],['occurs',/xuất hiện/],['indirect',/xuất hiện/],['apart',/thành công/],['general',/thành công/]]){await p.select('.predicate-unify > label select',id);await finish('.predicate-unify');assert.match(await p.$eval('.predicate-unify .predicate-status',e=>e.textContent),pattern)}
  await p.select('.predicate-unify > label select','nested');await finish('.predicate-unify');assert.match(await p.$eval('.unify-state',e=>e.textContent),/Mother\(John\)/);checks.push(`${width}: seven unification cases and propagated substitution`)
  for(const mode of ['forward','sld']){
   await p.select('.infer-config select',mode)
   for(const name of ['kings','students','shared','backtrack']){await p.select('.infer-config label:nth-child(2) select',name);await finish('.predicate-inference');const answer=await p.$eval('.inference-answers',e=>e.textContent);assert.match(answer,name==='shared'?/Chưa có/:name==='kings'?/John/:/An/)}
  }checks.push(`${width}: forward and SLD agree on four programs`)
  await p.select('.infer-config label:nth-child(2) select','cycle');await finish('.predicate-inference');assert.match(await p.$eval('.predicate-inference .predicate-status',e=>e.textContent),/giới hạn/);assert.match(await p.$eval('.inference-answers',e=>e.textContent),/An/);checks.push(`${width}: depth limit keeps a valid answer without claiming complete enumeration`)
  for(const name of ['kings','factoring','notTautology']){await p.select('.predicate-resolution > label select',name);await finish('.predicate-resolution');assert.match(await p.$eval('.predicate-resolution .predicate-status',e=>e.textContent),name==='notTautology'?/không phải chứng nhận/:/clause rỗng/)}checks.push(`${width}: resolution, factoring and non-tautology`)
  await p.select('.predicate-resolution > label select','kings');await finish('.predicate-resolution');const result=await p.$eval('.predicate-resolution .predicate-status',e=>e.textContent);await p.click('.predicate-resolution button[aria-label="Lùi một bước"]');await p.click('.predicate-resolution button[aria-label="Tiến một bước"]');assert.equal(await p.$eval('.predicate-resolution .predicate-status',e=>e.textContent),result)
  await p.click('.predicate-unify .search-trace-code button');await p.waitForFunction(()=>document.querySelector('.predicate-unify .search-trace-code button').textContent.includes('Đã chép'));checks.push(`${width}: copy and reversible tracing`)
  assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),false)
  // Hide the sticky site header only for element screenshots; reading layout is unchanged.
  await p.addStyleTag({content:'.VPNav{visibility:hidden}'})
  for(const selector of ['.predicate-quantifier','.predicate-unify','.predicate-inference','.predicate-resolution'])await (await p.$(selector)).screenshot({path:`${out}/${selector.slice(1)}-${width}.png`})
 }
 await p.$eval('.unify-input input',e=>{e.value='f(';e.dispatchEvent(new Event('input',{bubbles:true}))});await p.click('.unify-input button');await p.waitForSelector('.predicate-unify [role="alert"]');checks.push('Invalid term rejected')
 await p.$eval('.knowledge-input',e=>e.open=true);await p.$eval('.knowledge-input textarea',e=>{e.value='{}';e.dispatchEvent(new Event('input',{bubbles:true}))});await p.click('.knowledge-input button');await p.waitForSelector('.knowledge-input [role="alert"]');checks.push('Invalid knowledge base rejected')
 await p.emulateMediaFeatures([{name:'prefers-reduced-motion',value:'reduce'}]);await p.reload({waitUntil:'domcontentloaded'});await p.waitForSelector('.motion-note');await p.focus('.predicate-quantifier button[aria-label="Tiến một bước"]');await p.keyboard.press('Enter');assert.equal(await p.$eval('.predicate-quantifier .step-slider input',e=>e.value),'1');checks.push('Keyboard and reduced motion')
 await p.click('.predicate-quantifier .play-toggle');await p.waitForFunction(()=>Number(document.querySelector('.predicate-quantifier .step-slider input').value)>1);await p.click('.predicate-quantifier .play-toggle');const paused=await p.$eval('.predicate-quantifier .step-slider input',e=>e.value);await new Promise(r=>setTimeout(r,1100));assert.equal(await p.$eval('.predicate-quantifier .step-slider input',e=>e.value),paused);checks.push('Play and pause use real states')
 assert.deepEqual(errors,[]);await writeFile(out+'/results.json',JSON.stringify({checks,errors},null,2)+'\n');console.log(`PASS ${checks.length} interaction checks, no runtime errors or page overflow`)
}finally{await browser.close()}
