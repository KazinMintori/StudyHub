import puppeteer from 'puppeteer'
import {mkdir,writeFile} from 'node:fs/promises'
import assert from 'node:assert/strict'
const base=process.env.QA_URL||'http://localhost:5191'
const folder='/bieu-dien-tri-thuc/bai-giang/03-tim-kiem-kinh-nghiem'
const topics=['','ham-kinh-nghiem','tim-kiem-tham-lam','thuat-toan-a-sao','chap-nhan-duoc-va-toi-uu-tren-cay','nhat-quan-va-mo-lai-trang-thai','thiet-ke-heuristic-va-thuc-hanh']
const out='raw_materials/bieu-dien-tri-thuc/reviews/bai-03/notes-browser'
await mkdir(out,{recursive:true})
const browser=await puppeteer.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const checks=[],errors=[],overflow=[],documentOverflow=[]
try{
 const page=await browser.newPage();page.on('pageerror',e=>errors.push(e.message))
 for(const width of [1280,375,360])for(const topic of topics){
  await page.setViewport({width,height:900});await page.goto(base+folder+(topic?'/'+topic:'')+'.html',{waitUntil:'domcontentloaded',timeout:120000})
  await page.waitForSelector('.vp-doc')
  await page.waitForSelector('.vp-doc mjx-container')
  await page.evaluate(()=>document.fonts.ready)
  await page.evaluate(()=>document.querySelectorAll('.vp-doc details').forEach(e=>e.open=true))
  const bad=await page.evaluate(()=>[...document.querySelectorAll('.vp-doc mjx-container')].flatMap(e=>{
   const r=e.getBoundingClientRect(),svg=e.querySelector('svg'),s=svg?.getBoundingClientRect(),p=e.parentElement.getBoundingClientRect();
   if(r.width>p.width+2||s&&s.width>p.width+2||s&&s.right>innerWidth-2||s&&s.left<0)return [{tex:e.getAttribute('data-math-source')||e.textContent,left:r.left,width:r.width,parentWidth:p.width,svgWidth:s?.width,html:e.outerHTML.slice(0,230)}]
   return []
  }))
  overflow.push(...bad.map(b=>({width,topic,...b})))
  if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1))documentOverflow.push({topic,width,elements:await page.evaluate(()=>[...document.querySelectorAll('.vp-doc *')].filter(e=>e.getBoundingClientRect().right>innerWidth+2).slice(0,12).map(e=>({tag:e.tagName,class:e.className?.baseVal??e.className,text:e.textContent.slice(0,120),width:e.getBoundingClientRect().width,html:e.outerHTML.slice(0,300)})))})
  if(topic==='thiet-ke-heuristic-va-thuc-hanh')await page.waitForSelector('.puzzle-lab')
  if(topic==='thuat-toan-a-sao')await page.waitForSelector('.informed-lab')
  if(width===375&&['ham-kinh-nghiem','chap-nhan-duoc-va-toi-uu-tren-cay','thiet-ke-heuristic-va-thuc-hanh'].includes(topic))await page.screenshot({path:`${out}/${topic}-375.png`,fullPage:true})
  checks.push(`${width}px ${topic||'hub'}: all details opened`)
  console.log(checks.at(-1))
 }
 await writeFile(out+'/results.json',JSON.stringify({checks,errors,overflow,documentOverflow},null,2)+'\n')
 console.log(JSON.stringify({checks:checks.length,errors,overflow,documentOverflow},null,2))
 assert.deepEqual(errors,[]);assert.deepEqual(overflow,[]);assert.deepEqual(documentOverflow,[])
}finally{await browser.close()}
