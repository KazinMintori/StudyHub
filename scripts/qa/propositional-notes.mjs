import puppeteer from 'puppeteer'
import {mkdir,writeFile} from 'node:fs/promises'
import {spawn} from 'node:child_process'
import assert from 'node:assert/strict'
const base=process.env.QA_URL||'http://127.0.0.1:5196',root='/bieu-dien-tri-thuc/bai-giang/07-logic-menh-de'
const topics=['','ngon-ngu-va-ngu-nghia','he-qua-va-mo-hinh','tuong-duong-va-cnf','suy-luan-tien','hop-giai-phan-chung','sld-va-lua-chon-phuong-phap']
const out='raw_materials/bieu-dien-tri-thuc/reviews/bai-07/notes-browser';await mkdir(out,{recursive:true})
let browser,server;const checks=[],issues=[],errors=[]
try{
 if(!process.env.QA_URL){server=spawn(process.execPath,['node_modules/vitepress/bin/vitepress.js','dev','docs','--port','5196','--host','127.0.0.1','--strictPort'],{windowsHide:true,stdio:'ignore'});let ready=false;for(let i=0;i<60;i++){try{if((await fetch(base,{signal:AbortSignal.timeout(1500)})).ok){ready=true;break}}catch{};await new Promise(r=>setTimeout(r,500))}assert.ok(ready)}
 browser=await puppeteer.launch({headless:true,executablePath:process.env.CHROME_PATH||'C:/Program Files/Google/Chrome/Application/chrome.exe'})
 const p=await browser.newPage();p.on('pageerror',e=>errors.push(e.message))
 async function metrics(width,route){
  await p.evaluate(()=>document.fonts.ready)
  const r=await p.evaluate(()=>({page:document.documentElement.scrollWidth,mathErrors:document.querySelectorAll('[data-mjx-error]').length,overflow:[...document.querySelectorAll('mjx-container')].filter(e=>e.checkVisibility()).flatMap(e=>{const s=e.querySelector('svg')?.getBoundingClientRect(),r=e.parentElement.getBoundingClientRect();return s&&(s.width>r.width+2||s.right>innerWidth+1||s.left<0)?[{text:e.textContent,parentWidth:r.width,svgWidth:s.width,left:s.left,right:s.right}]:[]})}))
  if(r.page>width+1||r.mathErrors||r.overflow.length)issues.push({width,route,...r});checks.push({width,route});console.log(width,route,JSON.stringify({overflow:r.overflow.length,page:r.page,mathErrors:r.mathErrors}))
 }
 for(const width of [1280,375,360]){
  await p.setViewport({width,height:900})
  for(const topic of topics){
   const route=root+(topic?'/'+topic:'')+'.html';await p.goto(base+route,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForSelector('.vp-doc',{timeout:60000});if(topic)await p.waitForSelector('.vp-doc mjx-container',{timeout:60000});await p.evaluate(()=>document.querySelectorAll('.vp-doc details').forEach(e=>e.open=true));await metrics(width,route)
   if(width===375&&topic==='hop-giai-phan-chung')await p.screenshot({path:out+'/resolution-notes-375.png',fullPage:true})
  }
  for(const tab of ['slides','cheatsheet','kien-thuc-can-co']){
   const route=root+'.html#'+tab;await p.goto(base+route,{waitUntil:'networkidle0',timeout:120000});await p.waitForFunction(()=>!!document.querySelector('#app')?.__vue_app__);await metrics(width,route)
  }
 }
 await writeFile(out+'/results.json',JSON.stringify({checks,issues,errors},null,2)+'\n');console.log('Notes and tabs:',checks.length,'checks;',issues.length,'layout issues')
 assert.deepEqual(errors,[]);assert.deepEqual(issues,[])
}finally{await browser?.close();server?.kill()}
