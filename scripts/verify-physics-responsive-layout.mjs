import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,writeFile} from 'node:fs/promises'
import {startPhysicsPreview} from './physics-qa-server.mjs'
const preview=process.env.QA_URL?null:await startPhysicsPreview()
const base=process.env.QA_URL||preview.url
assert(/^http:\/\/127\.0\.0\.1:\d+$/.test(base))
const browser=await puppeteer.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const page=await browser.newPage(),results=[],errors=[]
page.on('pageerror',error=>errors.push(error.message))
await page.evaluateOnNewDocument(()=>sessionStorage.setItem('studyhub_welcome_seen','1'))
await mkdir('qa/physics/responsive-layout',{recursive:true})
async function inspect(label){
 const data=await page.evaluate(()=>{
  document.querySelectorAll('.vp-doc details').forEach(e=>e.open=true)
  const math=[...document.querySelectorAll('mjx-container')].filter(e=>e.getBoundingClientRect().width>0)
  const failures=math.flatMap(e=>{
   const r=e.getBoundingClientRect(),svg=e.querySelector('svg')?.getBoundingClientRect(),style=getComputedStyle(e)
   return r.left< -1||r.right>innerWidth+1||svg?.width>r.width+1||(['auto','scroll'].includes(style.overflowX)&&e.scrollWidth>e.clientWidth+1)
     ?[{text:e.textContent.slice(0,100),width:r.width,svg:svg?.width,left:r.left,right:r.right}]:[]
  })
  const tabs=[...document.querySelectorAll('.lecture-tabs a')].map(a=>{
   const r=a.getBoundingClientRect()
   return {text:a.textContent,width:r.width,left:r.left,right:r.right,height:r.height}
  })
  const rows=[...document.querySelectorAll('.formula-row')].map(row=>{
   const label=row.querySelector('.formula-label')?.getBoundingClientRect(),value=row.querySelector('.formula-value')?.getBoundingClientRect()
   return {label:label?{left:label.left,right:label.right,top:label.top,bottom:label.bottom}:null,value:value?{left:value.left,right:value.right,top:value.top,bottom:value.bottom}:null}
  })
  const numbers=[...document.querySelectorAll('.static-math-numbered')].map(block=>{
   const body=block.querySelector('.static-math-body').getBoundingClientRect(),number=block.querySelector('.equation-number').getBoundingClientRect()
   return {bodyBottom:body.bottom,bodyRight:body.right,numberTop:number.top,numberLeft:number.left}
  })
  return {failures,tabs,rows,numbers,mathCount:math.length,documentWidth:document.documentElement.scrollWidth,viewport:innerWidth}
 })
 if(data.failures.length)console.log(JSON.stringify({label,failures:data.failures}))
 assert(data.documentWidth<=data.viewport+1,label)
 if(data.viewport<768)for(const tab of data.tabs){assert(tab.left>=0&&tab.right<=data.viewport&&tab.height>=44,label+tab.text)}
 for(const row of data.rows)if(row.label&&row.value){
  const stacked=row.value.top>=row.label.bottom-1
  const beside=row.value.left>=row.label.right-1
  assert(stacked||beside,label+' overlapping label and formula')
 }
 if(data.viewport<=600)for(const n of data.numbers)assert(n.numberTop>=n.bodyBottom-1,label+' equation number overlapping formula')
 results.push({label,...data})
}
try{
 for(const [course,slug] of [['vat-ly-2','02-dien-the'],['vat-ly-1','02-chuyen-dong-thang'],['vat-ly-2','03-dinh-luat-gauss'],['vat-ly-2','01-dien-truong-coulomb'],['vat-ly-2','04-tu-dien-dien-moi'],['vat-ly-2','05-dong-dien-dien-tro'],['vat-ly-2','06-mach-dien-mot-chieu'],['vat-ly-2','07-tu-truong-luc-tu']]){
  await page.setViewport({width:1440,height:1100})
  await page.goto(`${base}/${course}/bai-giang/${slug}.html#cheatsheet`,{waitUntil:'domcontentloaded',timeout:45000})
  await page.waitForSelector('.lecture-cheatsheet .cheatsheet-card')
  await page.evaluate(()=>document.fonts.ready)
  // Resize the same loaded page, including desktop -> phone -> desktop.
  for(const width of [1440,375,1024,360,768,320,600]){
   await page.setViewport({width,height:1100})
   await page.evaluate(()=>new Promise(done=>requestAnimationFrame(()=>requestAnimationFrame(done))))
   await page.waitForFunction(()=>innerWidth>=960||!document.querySelector('.VPSidebar')||document.querySelector('.VPSidebar').getBoundingClientRect().right<=1,{timeout:3000})
   await inspect(`${slug}/${width}`)
   if(width===375||width===1440){
    await page.evaluate(()=>scrollTo(0,0))
    await page.screenshot({path:`qa/physics/responsive-layout/${slug}-${width}.png`,fullPage:false})
   }
  }
 }
 await page.goto(`${base}/vat-ly-2/bai-giang/02-dien-the/the-nang-dien.html`,{waitUntil:'domcontentloaded',timeout:45000})
 await page.waitForSelector('.static-math-numbered')
 for(const width of [1440,375,768,320]){
  await page.setViewport({width,height:1100})
  await page.evaluate(()=>new Promise(done=>requestAnimationFrame(()=>requestAnimationFrame(done))))
  await page.waitForFunction(()=>innerWidth>=960||!document.querySelector('.VPSidebar')||document.querySelector('.VPSidebar').getBoundingClientRect().right<=1,{timeout:3000})
  await inspect(`numbered-notes/${width}`)
  if(width===375){await page.evaluate(()=>scrollTo(0,0));await page.screenshot({path:'qa/physics/responsive-layout/numbered-notes-375.png',fullPage:false})}
 }
 assert.deepEqual(errors,[])
 const failures=results.filter(r=>r.failures.length)
 await writeFile('qa/physics/responsive-layout/results.json',JSON.stringify({status:failures.length?'failed':'passed',checks:results.length,errors,results},null,2)+'\n')
 assert.deepEqual(failures,[])
 console.log('Passed',results.length,'live viewport transitions, formula layout and equation-number checks.')
}finally{await browser.close();await preview?.close()}
