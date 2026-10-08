import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir,writeFile } from 'node:fs/promises'
import { mathAiCourse as course } from '../docs/.vitepress/math-ai-course.mjs'
import { lectureConceptIds } from '../docs/.vitepress/lecture-model.mjs'

const base=process.env.QA_URL||'http://127.0.0.1:5174'
const browser=await puppeteer.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{})})
const page=await browser.newPage(),errors=[],results=[],failedResources=[]
await page.setCacheEnabled(false)
page.on('pageerror',e=>errors.push(e.message))
page.on('response',response=>{if(response.status()>=400&&response.url().startsWith(base)&&/\.(js|css|woff2?)(?:\?|$)/.test(response.url()))failedResources.push({url:response.url(),status:response.status()})})
await mkdir('qa/math-ai',{recursive:true})
async function go(path){const response=await page.goto(base+path,{waitUntil:'networkidle0',timeout:120000});if(response)assert([200,304].includes(response.status()));await page.waitForFunction(()=>!document.querySelector('.lecture-header')||document.querySelector('.lecture-tabs a[aria-current]'))}
async function check(name,fn){await fn();results.push(name);console.log('PASS',name)}
try{
  await page.setViewport({width:1440,height:1000})
  await go('/toan-cho-ai/')
  await check('Exact eight lecture titles and numbering 00–07',async()=>{
    assert.deepEqual(await page.$$eval('.lecture-list .course-number,.lecture-list .lesson-number',els=>els.map(e=>Number(e.textContent.trim()))),course.lessons.map(l=>l.number))
    assert.deepEqual(await page.$$eval('.lecture-list h3',els=>els.map(e=>e.textContent.trim())),course.lessons.map(l=>l.title))
    const sidebarLinks=await page.$$eval('.VPSidebar a[href*="/toan-cho-ai/bai-giang/"]',els=>els.map(e=>e.textContent.trim()))
    assert.deepEqual(sidebarLinks,course.lessons.map(l=>`Lecture ${String(l.number).padStart(2,'0')}. ${l.title}`))
  })
  await page.screenshot({path:'qa/math-ai/course-desktop.png',fullPage:true})
  for(const lesson of course.lessons){
    const url=`/toan-cho-ai/bai-giang/${lesson.slug}.html`
    await check(`Lecture ${lesson.number}: Notes, Slides, foundations and exercises`,async()=>{
      await go(url+'#notes')
      assert.equal(await page.$eval('.lecture-header h1',el=>el.textContent),lesson.title)
      assert.match(await page.$eval('.chapter-num,.lecture-meta',el=>el.textContent.trim()),new RegExp(`Bài\\s+0?${lesson.number}(?:\\s|·|$)`))
      assert.equal(await page.$$eval('h1',els=>els.length),1)
      assert(await page.$('.vp-doc mjx-container'))
      assert.equal(await page.$$eval('.vp-doc details > summary',els=>els.filter(e=>e.textContent.startsWith('Lời giải')).length),3)
      assert.equal(await page.$$eval('mjx-merror,[data-mml-node="merror"]',els=>els.length),0)
      await page.click('.lecture-tabs a[href$="#slides"]');await page.waitForSelector('.course-slide')
      assert.equal(await page.$eval('.main > .vp-doc',el=>getComputedStyle(el).display),'none')
      if(course.slides.filter(s=>s.note===lesson.slug).length>1){const previous=await page.$eval('.course-slide h2',el=>el.textContent);await page.click('.slide-controls button:last-child');await page.waitForFunction(previous=>document.querySelector('.course-slide h2')?.textContent!==previous,{},previous)}
      await page.click('.lecture-tabs a[href$="#kien-thuc-can-co"]');await page.waitForSelector('.lecture-foundations')
      assert.equal(await page.$$eval('.foundation-entry',els=>els.length),lectureConceptIds(lesson).length)
      assert.equal(await page.$$eval('.foundation-entry',els=>els.filter(el=>/\$|\\frac|\\nabla/.test(el.textContent)).length),0)
      if(await page.$('.lecture-tabs a[href$="#bai-tap"]')){
        await page.click('.lecture-tabs a[href$="#bai-tap"]');await page.waitForSelector('.lecture-exercises')
        await page.click('.lecture-exercises > a')
      }else await go(url+'#bai-tap-tu-luyen')
      await page.waitForFunction(()=>location.hash==='#bai-tap-tu-luyen'&&document.querySelector('.lecture-tabs a[aria-current]')?.textContent==='Notes')
      assert(await page.$('#bai-tap-tu-luyen'))
      assert.notEqual(await page.$eval('.main > .vp-doc',el=>getComputedStyle(el).display),'none')
    })
  }
  await check('Existing lesson addresses and reading progress are retained',async()=>{
    await go('/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html')
    await page.waitForFunction(()=>JSON.parse(localStorage.getItem('studyhub_last_lesson')||'null')?.path?.endsWith('/bai-giang/bai-01-nhap-mon-toi-uu.html'))
    await go('/toan-cho-ai/notes/bai-02-tap-loi.html');await page.waitForFunction(()=>location.pathname.endsWith('/bai-giang/bai-02-tap-loi.html'))
  })
  await check('Interactive models recompute and reset state',async()=>{
    await go('/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html#notes')
    await page.$eval('.math-lab input',el=>{el.value='1.2';el.dispatchEvent(new Event('input',{bubbles:true}))})
    assert.match(await page.$eval('.math-lab [role=status]',el=>el.textContent),/ngoài đoạn/)
    await go('/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange.html#notes')
    await page.$eval('.math-lab input',el=>{el.value='0';el.dispatchEvent(new Event('input',{bubbles:true}))})
    assert.match(await page.$eval('.math-lab [role=status]',el=>el.textContent),/1\.0000/)
    await go('/toan-cho-ai/bai-giang/bai-04-gradient-newton.html#notes')
    await page.select('.math-lab select','newton');await page.click('.math-lab button:nth-child(2)')
    assert.match(await page.$eval('.math-lab [role=status]',el=>el.textContent),/f = 0\.0000/)
    await page.select('.math-lab select','adam');assert.match(await page.$eval('.math-lab [role=status]',el=>el.textContent),/Bước 0/)
    await go('/toan-cho-ai/bai-giang/bai-07-quy-hoach-tuyen-tinh-va-dong.html#notes')
    for(let i=0;i<3;i++)await page.click('.math-lab:last-of-type .lab-buttons button:last-child')
    assert.match(await page.$eval('.math-lab:last-of-type [role=status]',el=>el.textContent),/V\(S\)=4/)
    await page.select('.math-lab:last-of-type select','true')
    for(let i=0;i<3;i++)await page.click('.math-lab:last-of-type .lab-buttons button:last-child')
    assert.match(await page.$eval('.math-lab:last-of-type [role=status]',el=>el.textContent),/V\(S\)=6/)
  })
  for(const width of [375,768,1440])for(const dark of [false,true]){
    await page.setViewport({width,height:1000})
    for(const lesson of course.lessons){
      await go(`/toan-cho-ai/bai-giang/${lesson.slug}.html#notes`)
      await page.evaluate(dark=>document.documentElement.classList.toggle('dark',dark),dark)
      assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`${width}, dark=${dark}, lecture ${lesson.number}`)
      if([1,4,6,7].includes(lesson.number)){
        const labs=await page.$$('.math-lab');for(let i=0;i<labs.length;i++)await labs[i].screenshot({path:`qa/math-ai/lab-${lesson.number}-${i}-${width}-${dark?'dark':'light'}.png`})
      }
    }
    await go('/toan-cho-ai/');assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth))
    results.push(`No page overflow: all eight lectures at ${width}px ${dark?'dark':'light'}`)
  }
  for(const id of ['hessian','ma-tran-psd','he-phuong-trinh','tap-loi','ham-loi','kkt']){
    await go(`/wiki/${id}.html`);await page.waitForSelector('.vp-doc h2');assert.equal(await page.$$eval('mjx-merror,[data-mml-node="merror"]',els=>els.length),0)
  }
  assert.deepEqual(errors,[])
  assert.deepEqual(failedResources,[])
  await writeFile('qa/math-ai/browser-results.json',JSON.stringify({base,results,errors,failedResources},null,2))
  console.log(`${results.length} groups passed; zero browser exceptions.`)
}catch(error){
  await page.screenshot({path:'qa/math-ai/failure.png',fullPage:true}).catch(()=>{})
  await writeFile('qa/math-ai/browser-failure.json',JSON.stringify({url:page.url(),error:String(error),results,errors,failedResources},null,2))
  throw error
}finally{await browser.close()}
