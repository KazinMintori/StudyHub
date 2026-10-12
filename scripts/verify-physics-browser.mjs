// Headless integration tests against the local study site. Never attaches to a
// user's browser or opens an external website.
import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,writeFile} from 'node:fs/promises'
import {readFile,stat} from 'node:fs/promises'
import {createServer} from 'node:http'
import {resolve,extname,sep} from 'node:path'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {physicsImageLabels} from '../docs/.vitepress/physics-image-labels.mjs'

let base=process.env.QA_URL,server
if(!base){
 const root=resolve(process.env.QA_DIST||'docs/.vitepress/dist')
 const types={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.woff2':'font/woff2','.woff':'font/woff','.ico':'image/x-icon'}
 server=createServer(async(req,res)=>{
  try{
   const path=decodeURIComponent(new URL(req.url,'http://127.0.0.1').pathname)
   let file=resolve(root,'.'+path)
   if(file!==root&&!file.startsWith(root+sep)){res.writeHead(403);res.end();return}
   if((await stat(file)).isDirectory())file=resolve(file,'index.html')
   res.writeHead(200,{'Content-Type':types[extname(file)]||'application/octet-stream'})
   res.end(req.method==='HEAD'?undefined:await readFile(file))
  }catch{res.writeHead(404);res.end()}
 })
 await new Promise(done=>server.listen(0,'127.0.0.1',done))
 base=`http://127.0.0.1:${server.address().port}`
}
const chapters=process.env.QA_CHAPTERS?process.env.QA_CHAPTERS.split(',').map(Number):[21,22,23]
assert(/^http:\/\/127\.0\.0\.1:\d+$/.test(base),'QA target must be localhost')
const browser=await puppeteer.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const page=await browser.newPage(),errors=[],results=[],overflow=[],verifiedImages=new Set()
page.on('pageerror',e=>errors.push(e.message))
await page.evaluateOnNewDocument(()=>sessionStorage.setItem('studyhub_welcome_seen','1'))
await mkdir('qa/physics/browser',{recursive:true})
async function go(path){
 console.log('Inspecting',path)
 const response=await page.goto(base+path,{waitUntil:'domcontentloaded',timeout:45000})
 assert([200,304].includes(response.status()),`${path}: HTTP ${response.status()}`)
 await page.waitForSelector('.lecture-tabs, .topic-header',{timeout:30000})
 await page.evaluate(()=>document.fonts.ready)
 const sources=await page.$$eval('.vp-doc img',es=>es.map(e=>e.src))
 await Promise.all([...new Set(sources)].filter(src=>!verifiedImages.has(src)).map(async src=>{
  if(src.startsWith('data:image/')){verifiedImages.add(src);return}
  assert.equal(new URL(src).origin,base,'Exercise illustrations must be local assets')
  const response=await fetch(src,{method:'HEAD'})
  assert(response.ok,`Image HTTP ${response.status}: ${src}`)
  verifiedImages.add(src)
 }))
 const captions=await page.$$eval('.lecture-figure',figures=>figures.map(f=>({alt:f.querySelector('img')?.alt,caption:f.querySelector('figcaption')?.textContent,labels:f.querySelector('.figure-labels')?.textContent})))
 for(const item of captions){
  assert(item.caption?.startsWith(item.alt),'Vietnamese caption must appear below the image: '+JSON.stringify(item))
  if(item.labels)for(const [vi,en] of Object.values(physicsImageLabels).flat()){
   const pair=`${vi} (${en})`
   if(item.labels.includes(pair))assert.equal(item.labels.split(pair).length-1,1,`Repeated caption label ${pair}`)
  }
 }
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
 for(const width of (process.env.QA_WIDTHS||'320,360,375,1440').split(',').map(Number)){
  await page.setViewport({width,height:900})
  for(const chapter of chapters){
   const lesson=physics2Course.lessons.find(l=>l.sourceChapter===chapter)
   const path=`/vat-ly-2/bai-giang/${lesson.slug}.html`
   await go(path)
   const tabs=await page.$$eval('.lecture-tabs a',es=>es.map(e=>e.textContent.replace(/\d+/g,'').trim()))
   assert.equal(tabs[tabs.indexOf('Bài tập')+1],'Cheatsheet')
   if(!lesson.hasChapterExercises){
    await inspect(`${width}/chapter${chapter}/notes-draft`)
    for(const topic of lesson.topicGroups.flatMap(g=>g.topics)){
     await go(`/vat-ly-2/bai-giang/${lesson.slug}/${topic.slug}.html`)
     await inspect(`${width}/chapter${chapter}/${topic.slug}`)
    }
    continue
   }
   assert(await page.$eval('.lecture-exercises-content',e=>getComputedStyle(e).display==='none'))
   assert.equal(await page.$$eval('.lecture-exercises-content details',es=>es.some(e=>e.open)),false,'Solutions must initially be collapsed')
   await inspect(`${width}/chapter${chapter}/notes`)
   await page.click('.lecture-tabs a[href$="#bai-tap"]')
   await page.waitForFunction(()=>{
    const notes=document.querySelector('.lecture-notes-content')
    const exercises=document.querySelector('.lecture-exercises-content')
    return document.querySelector('.Layout.lecture-exercises-layout')
      &&getComputedStyle(notes).display==='none'
      &&getComputedStyle(exercises).display!=='none'
   })
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
    if(part==='slides'){
     const slideData=physics2Course.slides.filter(s=>s.note===lesson.slug)
     assert(slideData.length>0,'Ready Physics2 lecture needs review cards')
     for(let index=0;index<slideData.length;index++){
      assert.equal(await page.$eval('.course-slide h2',e=>e.textContent),slideData[index].title)
      await inspect(`${width}/chapter${chapter}/slide-${index+1}`)
      if(index+1<slideData.length)await page.click('.slide-controls button:last-child')
     }
     assert(await page.$eval('.slide-controls button:last-child',e=>e.disabled))
    }
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
 await writeFile(`qa/physics/browser/results${chapters.length===1?'-chapter'+chapters[0]:'-all'}.json`,JSON.stringify({base,checks:results.length,verifiedImages:verifiedImages.size,results,errors,overflow},null,2)+'\n')
 console.log(JSON.stringify({checks:results.length,errors,overflow},null,2))
 assert.equal(overflow.length,0,'Math, image or document overflow')
}finally{await browser.close();if(server)await new Promise(done=>server.close(done))}
