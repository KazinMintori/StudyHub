import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,writeFile} from 'node:fs/promises'
import {spawn} from 'node:child_process'
const base=process.env.QA_URL||'http://127.0.0.1:5196',out='raw_materials/bieu-dien-tri-thuc/reviews/bai-07/browser'
await mkdir(out,{recursive:true});let server,browser;const checks=[],errors=[]
try{
 if(!process.env.QA_URL){server=spawn(process.execPath,['node_modules/vitepress/bin/vitepress.js','dev','docs','--port','5196','--host','127.0.0.1','--strictPort'],{windowsHide:true,stdio:'ignore'});let ready=false;for(let i=0;i<60;i++){try{if((await fetch(base,{signal:AbortSignal.timeout(1500)})).ok){ready=true;break}}catch{}await new Promise(r=>setTimeout(r,500))}assert.ok(ready)}
 browser=await puppeteer.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});const p=await browser.newPage();p.on('pageerror',e=>errors.push(e.message))
 const finish=selector=>p.$eval(selector+' .step-slider input',e=>{e.value=e.max;e.dispatchEvent(new Event('input',{bubbles:true}))})
 for(const width of [1280,375,360]){
  await p.setViewport({width,height:900});await p.goto(base+'/agy-plans/logic07-preview.html',{waitUntil:'domcontentloaded',timeout:120000});await p.waitForSelector('.prop-resolution',{timeout:120000});await p.waitForSelector('.prop-model')
  for(const [id,status]of [['rain','hàm nghĩa truy vấn'],['models','hàm nghĩa truy vấn'],['unknown','không hàm nghĩa'],['converse','không hàm nghĩa'],['inconsistent','không có mô hình'],['negated','phủ định']]){
   await p.select('.prop-model select',id);await finish('.prop-model');await p.$eval('.prop-model details',e=>e.open=true)
   assert.match(await p.$eval('.prop-model details',e=>e.textContent),new RegExp(status))
  }
  checks.push(`${width}px: all six model cases, including inconsistent and unknown`)
  await p.select('.prop-model select','models');await finish('.prop-model');await (await p.$('.prop-model')).screenshot({path:`${out}/models-${width}.png`})
  await finish('.prop-cnf');assert.match(await p.$eval('.cnf-stage',e=>e.textContent),/¬P/);await p.$eval('.prop-cnf details',e=>e.open=true);assert.match(await p.$eval('.prop-cnf details',e=>e.textContent),/luôn cùng giá trị/)
  checks.push(`${width}px: CNF stages and exhaustive equivalence table`)
  for(const mode of ['forward','sld'])for(const id of ['source','cycle','backtrack','and','fact','practice']){
   await p.select('.infer-settings select',mode);await p.select('.infer-settings label:nth-child(2) select',id);await finish('.prop-inference')
   assert.match(await p.$eval('.infer-status',e=>e.textContent),['cycle','and'].includes(id)?/chưa suy ra/:/Đã chứng minh/)
  }
  checks.push(`${width}px: forward and SLD across six Horn examples`)
  await p.select('.infer-settings select','sld');await p.select('.infer-settings label:nth-child(2) select','backtrack');await finish('.prop-inference');await (await p.$('.prop-inference')).screenshot({path:`${out}/sld-${width}.png`})
  for(const [id,result]of [['rain','success'],['wumpus','success'],['unknown','saturated'],['multipivot','saturated'],['inconsistent','success']]){
   await p.select('.prop-resolution select',id);await finish('.prop-resolution');assert.match(await p.$eval('.resolution-status',e=>e.textContent),result==='success'?/clause rỗng/:/không sinh clause rỗng/)
  }
  checks.push(`${width}px: resolution proof, saturation, one pivot and inconsistent KB`)
  await p.select('.prop-resolution select','wumpus');await finish('.prop-resolution');await (await p.$('.prop-resolution')).screenshot({path:`${out}/resolution-${width}.png`})
  await p.click('.prop-resolution .prop-code button');await p.waitForFunction(()=>document.querySelector('.prop-resolution .prop-code button').textContent.includes('Đã chép'))
  const before=await p.$eval('.resolution-status',e=>e.textContent);await p.click('.prop-resolution button[aria-label="Lùi một bước"]');await p.click('.prop-resolution button[aria-label="Tiến một bước"]');assert.equal(await p.$eval('.resolution-status',e=>e.textContent),before)
  assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),false)
  checks.push(`${width}px: copy, backwards/forwards replay and no page overflow`)
 }
 await p.$eval('.model-edit',e=>e.open=true);await p.$eval('.model-edit input',e=>{e.value='P &';e.dispatchEvent(new Event('input',{bubbles:true}))});await p.click('.model-edit button');await p.waitForSelector('.model-edit [role="alert"]');checks.push('Malformed formula rejected with visible message')
 await p.$eval('.resolution-edit',e=>e.open=true);await p.$eval('.resolution-edit textarea',e=>{e.value='{}';e.dispatchEvent(new Event('input',{bubbles:true}))});await p.click('.resolution-edit button');await p.waitForSelector('.resolution-edit [role="alert"]');checks.push('Malformed resolution input rejected')
 await p.emulateMediaFeatures([{name:'prefers-reduced-motion',value:'reduce'}]);await p.reload({waitUntil:'domcontentloaded'});await p.waitForSelector('.motion-note');await p.focus('.prop-model button[aria-label="Tiến một bước"]');await p.keyboard.press('Enter');checks.push('Reduced-motion and keyboard controls')
 await p.click('.prop-model .play-toggle');await p.waitForFunction(()=>Number(document.querySelector('.prop-model .step-slider input').value)>1);await p.click('.prop-model .play-toggle');const paused=await p.$eval('.prop-model .step-slider input',e=>e.value);await new Promise(r=>setTimeout(r,1100));assert.equal(await p.$eval('.prop-model .step-slider input',e=>e.value),paused);checks.push('Play advances, pause freezes the state')
 assert.deepEqual(errors,[]);await writeFile(out+'/results.json',JSON.stringify({checks,errors},null,2)+'\n');console.log('PASS '+checks.length+' browser checks; no runtime errors')
}finally{await browser?.close();server?.kill()}
