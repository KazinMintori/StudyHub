import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,writeFile,readdir} from 'node:fs/promises'
const base=process.env.QA_URL||'http://127.0.0.1:5198',out='raw_materials/bieu-dien-tri-thuc/reviews/bai-06/notes-browser'
await mkdir(out,{recursive:true});const browser=await puppeteer.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'}),checks=[],errors=[],issues=[]
try{
 const p=await browser.newPage();p.on('pageerror',e=>errors.push(e.message))
 async function metrics(width,route){await p.evaluate(()=>document.fonts.ready);const r=await p.evaluate(()=>({page:document.documentElement.scrollWidth,mathErrors:document.querySelectorAll('[data-mjx-error]').length,overflow:[...document.querySelectorAll('mjx-container')].filter(e=>e.checkVisibility()).flatMap(e=>{const s=e.querySelector('svg')?.getBoundingClientRect(),r=e.parentElement.getBoundingClientRect();return s&&(s.width>r.width+2||s.right>innerWidth+1||s.left<0)?[{text:e.textContent,parentWidth:r.width,svgWidth:s.width,left:s.left,right:s.right}]:[]})}));if(r.page>width+1||r.mathErrors||r.overflow.length)issues.push({width,route,...r});checks.push({width,route});console.log(width,route,JSON.stringify({overflow:r.overflow.length,page:r.page,mathErrors:r.mathErrors}))}
 for(const width of [1280,375,360]){
  await p.setViewport({width,height:900})
  for(const slug of ['05-tim-kiem-cuc-bo','05-csp']){
   const root='/bieu-dien-tri-thuc/bai-giang/'+slug,topics=['',...(await readdir('docs'+root)).filter(x=>x.endsWith('.md')).map(x=>x.slice(0,-3))]
   for(const topic of topics){const route=root+(topic?'/'+topic:'')+'.html';await p.goto(base+route,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForSelector('.vp-doc',{timeout:60000});if(topic)await p.waitForSelector('.vp-doc mjx-container',{timeout:60000});await p.evaluate(()=>document.querySelectorAll('.vp-doc details').forEach(e=>e.open=true));await metrics(width,route);if(width===375&&!topic)await p.screenshot({path:out+'/'+slug+'-375.png',fullPage:true})}
   for(const tab of ['slides','cheatsheet','kien-thuc-can-co']){const route=root+'.html#'+tab;await p.goto(base+route,{waitUntil:'networkidle0',timeout:120000});await p.waitForFunction(()=>!!document.querySelector('#app')?.__vue_app__);await metrics(width,route)}
  }
 }
 await writeFile(out+'/results.json',JSON.stringify({checks,issues,errors},null,2)+'\n');assert.deepEqual(errors,[]);assert.deepEqual(issues,[]);console.log(`PASS ${checks.length} Notes/tab checks`)
}finally{await browser.close()}
