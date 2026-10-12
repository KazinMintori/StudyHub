// Headless integration tests against the local study site. Never attaches to a
// user's browser or opens an external website.
import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,writeFile} from 'node:fs/promises'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'

const base=process.env.QA_URL||'http://127.0.0.1:5175'
const chapters=process.env.QA_CHAPTERS?process.env.QA_CHAPTERS.split(',').map(Number):[21,22,23]
assert(/^http:\/\/127\.0\.0\.1:\d+$/.test(base),'QA target must be localhost')
const browser=await puppeteer.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const page=await browser.newPage(),errors=[],results=[],overflow=[]
page.on('pageerror',e=>errors.push(e.message))
await page.evaluateOnNewDocument(()=>sessionStorage.setItem('studyhub_welcome_seen','1'))
await mkdir('qa/physics/browser',{recursive:true})
async function go(path){
 console.log('Inspecting',path)
 const response=await page.goto(base+path,{waitUntil:'domcontentloaded',timeout:45000})
 assert([200,304].includes(response.status()),`${path}: HTTP ${response.status()}`)
 await page.waitForSelector('.lecture-tabs, .topic-header',{timeout:30000})
 await page.evaluate(()=>document.fonts.ready)
}
async function inspect(label){
 const found=await page.evaluate(()=>{
  document.querySelectorAll('.vp-doc details').forEach(e=>e.open=true)
  const nodes=[...document.querySelectorAll('mjx-container')].filter(e=>e.getBoundingClientRect().width>0)
  const math=nodes.flatMap(e=>{
   const r=e.getBoundingClientRect(),s=e.querySelector('svg')?.getBoundingClientRect(),style=getComputedStyle(e)
   const scroll=['auto','scroll'].includes(style.overflowX)&&e.scrollWidth>e.clientWidth+1
   return r.right>innerWidth+2||r.left< -2||(s&&s.width>r.width+2)||scroll?[{tex:e.textContent.slice(0,180),width:r.width,svg:s?.width,left:r.left,right:r.right,scroll}]:[]
  })
  const images=[...document.querySelectorAll('.vp-doc img')].filter(i=>i.getBoundingClientRect().width>0).filter(i=>i.complete&&!i.naturalWidth).map(i=>i.src)
  const unrendered=[...document.querySelectorAll('.math-text')].filter(e=>e.getBoundingClientRect().width>0).flatMap(e=>[...e.childNodes].filter(n=>n.nodeType===Node.TEXT_NODE).map(n=>n.textContent).filter(t=>/\$[^$]+\$|\\begin\{|\\frac\{/.test(t)))
  return {math,images,unrendered,documentOverflow:document.documentElement.scrollWidth>innerWidth+2,mathErrors:document.querySelectorAll('mjx-merror,[data-mml-node="merror"]').length}
 })
 if(found.math.length||found.documentOverflow||found.images.length||found.mathErrors||found.unrendered.length)overflow.push({label,...found})
 results.push(label)
}
try{
 for(const width of [360,375,1440]){
  await page.setViewport({width,height:900})
  for(const chapter of chapters){
   const lesson=physics2Course.lessons.find(l=>l.sourceChapter===chapter)
   const path=`/vat-ly-2/bai-giang/${lesson.slug}.html`
   await go(path)
   const tabs=await page.$$eval('.lecture-tabs a',es=>es.map(e=>e.textContent.replace(/\d+/g,'').trim()))
   assert.equal(tabs[tabs.indexOf('Bài tập')+1],'Cheatsheet')
   if(!lesson.hasChapterExercises){
    await inspect(`${width}/chapter23/notes-draft`)
    for(const topic of lesson.topicGroups.flatMap(g=>g.topics)){
     await go(`/vat-ly-2/bai-giang/${lesson.slug}/${topic.slug}.html`)
     await inspect(`${width}/chapter23/${topic.slug}`)
    }
    continue
   }
   assert(await page.$eval('.lecture-exercises-content',e=>getComputedStyle(e).display==='none'))
   await inspect(`${width}/chapter${chapter}/notes`)
   await page.click('.lecture-tabs a[href$="#bai-tap"]')
   await page.waitForFunction(()=>getComputedStyle(document.querySelector('.lecture-exercises-content')).display!=='none')
   assert(await page.$eval('.lecture-notes-content',e=>getComputedStyle(e).display==='none'))
   const first=await page.$('.lecture-exercises-content details')
   assert(first)
   // Notes inspection only opens visible/hidden SSR details, so restore the
   // default collapsed exercise state before testing the click.
   await page.evaluate(()=>document.querySelectorAll('.lecture-exercises-content details').forEach(e=>e.open=false))
   assert.equal(await first.evaluate(e=>e.open),false)
   await first.$eval('summary',e=>e.click())
   assert.equal(await first.evaluate(e=>e.open),true)
   const body=await first.evaluate(e=>e.textContent)
   assert(body.includes('Tóm tắt đề bài:')&&body.includes('Hướng đi:'),body.slice(0,100))
   await inspect(`${width}/chapter${chapter}/exercises`)
   if(width===375)await page.screenshot({path:`qa/physics/browser/chapter${chapter}-exercises-mobile.png`,fullPage:false})
   await page.reload({waitUntil:'domcontentloaded'})
   await page.waitForSelector('.lecture-tabs')
   assert.equal(new URL(page.url()).hash,'#bai-tap')
   assert(await page.$eval('.lecture-exercises-content',e=>getComputedStyle(e).display!=='none'))
   for(const part of ['cheatsheet','kien-thuc-can-co','slides']){
    await page.click(`.lecture-tabs a[href$="#${part}"]`)
    await page.waitForFunction(part=>document.querySelector(`.lecture-tabs a[href$="#${part}"]`)?.getAttribute('aria-current')==='page',{},part)
    await inspect(`${width}/chapter${chapter}/${part}`)
    if(width===375&&part==='cheatsheet')await page.screenshot({path:`qa/physics/browser/chapter${chapter}-cheatsheet-mobile.png`,fullPage:false})
   }
   for(const topic of lesson.topicGroups.flatMap(g=>g.topics)){
    await go(`/vat-ly-2/bai-giang/${lesson.slug}/${topic.slug}.html`)
    assert.equal(await page.$eval('.topic-header h1',e=>e.textContent),topic.title)
    await inspect(`${width}/chapter${chapter}/${topic.slug}`)
   }
  }
 }
 assert.deepEqual(errors,[])
 await writeFile(`qa/physics/browser/results${chapters.includes(23)?'-chapter23':''}.json`,JSON.stringify({base,checks:results.length,results,errors,overflow},null,2)+'\n')
 console.log(JSON.stringify({checks:results.length,errors,overflow},null,2))
 assert.equal(overflow.length,0,'Math, image or document overflow')
}finally{await browser.close()}
