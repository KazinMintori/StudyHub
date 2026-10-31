// Inspect deployed chapter exercises without building or copying course assets.
import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {mkdir,readFile,writeFile} from 'node:fs/promises'
import {physics2Course} from '../../docs/.vitepress/physics-courses.mjs'

const base=process.env.QA_BASE_URL||'https://kazinmintori.github.io/StudyHub'
const output=process.env.QA_OUTPUT_DIR||'qa/physics-public-exercises'
const selected=process.argv.slice(2).map(Number)
const sourceCounts=JSON.parse(await readFile('raw_materials/physics/reviews/all44-exercise-numbering-20261028.json','utf8')).chapters
await mkdir(output,{recursive:true})
const report={status:'running',base,startedUTC:new Date().toISOString(),scope:'Actual public Physics2 prompts, numbered sequence, unit count, one closed solution with summary/direction, and opened math/images at five widths. Source counts alone do not establish semantic correctness.',chapters:[],units:0,cases:0,issues:0}
const browser=await puppeteer.launch({headless:true,...(process.env.PUPPETEER_EXECUTABLE_PATH?{executablePath:process.env.PUPPETEER_EXECUTABLE_PATH}:{executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'})})
try{for(const lesson of physics2Course.lessons.filter(l=>!selected.length||selected.includes(l.sourceChapter))){
 const chapter=lesson.sourceChapter,page=await browser.newPage(),row={chapter,slug:lesson.slug,cases:[],units:[],errors:[],requests:[]}
 const expected=sourceCounts.find(c=>c.chapter===chapter)
 try{
  page.on('pageerror',e=>row.errors.push({kind:'javascript',message:e.message}))
  page.on('response',r=>{if(r.status()>=400&&!r.url().endsWith('favicon.ico'))row.requests.push({url:r.url(),status:r.status()})})
  await page.setViewport({width:375,height:950})
  await page.goto(`${base}/vat-ly-2/bai-giang/${lesson.slug}.html#bai-tap`,{waitUntil:'domcontentloaded',timeout:120000})
  await page.waitForSelector('.lecture-exercises-content details',{visible:true,timeout:90000})
  row.assets=await page.$$eval('script[src]',ns=>ns.map(n=>n.src))
  row.initial=await page.$$eval('.lecture-exercises-content details',ns=>({count:ns.length,allClosed:ns.every(n=>!n.open)}))
  assert(row.initial.count&&row.initial.allClosed,'Missing or initially open solutions')
  row.units=await page.$eval('.lecture-exercises-content',(root,chapter)=>{
   const number=new RegExp('^((?:VP|Q)?'+chapter+'\\.\\d+(?:\\.\\d+)?)(?=$|[\\s:·•]|\\.(?!\\d))'),bridge=/Bài (?:tập )?cầu nối|Bài tổng hợp/i
   const prompts=[...root.querySelectorAll('.exercise')].filter(n=>!n.closest('details'))
   const hasBridgePrompt=prompts.some(n=>bridge.test(n.querySelector('.custom-block-title')?.textContent.trim()||''))
   const candidates=[...root.querySelectorAll('.exercise,h3')].filter(n=>!n.closest('details')&&!(n.tagName==='H3'&&n.closest('.exercise'))).map(n=>{
    const text=(n.matches('.exercise')?n.querySelector('.custom-block-title')?.textContent:n.textContent)?.trim()||''
    const id=text.replace(/^Bài\s+tập\s*:?\s*/i,'').match(number)?.[1]||(bridge.test(text)&&(n.matches('.exercise')||!hasBridgePrompt)?'Bài tập cầu nối':null)
    return {node:n,id}
   }).filter(c=>c.id)
   const h2=[...root.querySelectorAll('h2')].filter(n=>!n.closest('details'))
   return candidates.map((c,i)=>{
    const stops=[candidates[i+1]?.node,...h2.filter(h=>c.node.compareDocumentPosition(h)&Node.DOCUMENT_POSITION_FOLLOWING)].filter(Boolean)
    const stop=stops.sort((a,b)=>a===b?0:(a.compareDocumentPosition(b)&Node.DOCUMENT_POSITION_FOLLOWING?-1:1))[0]
    const range=document.createRange();range.setStartAfter(c.node)
    if(stop)range.setEndBefore(stop);else range.setEnd(root,root.childNodes.length)
    const fragment=range.cloneContents(),boxes=[...fragment.querySelectorAll('details')].filter(n=>!n.parentElement?.closest('details')),text=boxes[0]?.textContent||''
    return {id:c.id,solutionBoxes:boxes.length,initiallyClosed:boxes.every(n=>!n.open),summary:/Tóm tắt/i.test(text),direction:/Hướng đi/i.test(text),bodyLength:text.length}
   })
  },chapter)
  const ids=row.units.map(u=>u.id)
  if(ids.length!==expected.observedEndUnitsIncludingGuidedDiscussionBridge||new Set(ids).size!==ids.length)row.errors.push({kind:'unit-count-or-duplicate',actual:ids.length,expected:expected.observedEndUnitsIncludingGuidedDiscussionBridge})
  const numbered=ids.filter(id=>new RegExp('^'+chapter+'\\.\\d+$').test(id)),expectedNumbered=Array.from({length:expected.numberedPrompts},(_,i)=>`${chapter}.${i+1}`)
  if(JSON.stringify(numbered)!==JSON.stringify(expectedNumbered))row.errors.push({kind:'numbered-sequence',actual:numbered,expected:expectedNumbered})
  for(const u of row.units)if(u.solutionBoxes!==1||!u.initiallyClosed||!u.summary||!u.direction||u.bodyLength<60)row.errors.push({kind:'solution-structure',...u})
  await page.evaluate(async()=>{
   const root=document.querySelector('.lecture-exercises-content');root.querySelectorAll('details').forEach(d=>d.open=true)
   const images=[...root.querySelectorAll('img')];images.forEach(i=>i.loading='eager')
   await Promise.all(images.map(i=>i.decode().catch(()=>{})));await document.fonts.ready
  })
  for(const width of[320,360,375,768,1440]){
   await page.setViewport({width,height:950});await page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))))
   const result=await page.$eval('.lecture-exercises-content',root=>{
    const issues=[];let formulas=0
    for(const m of root.querySelectorAll('mjx-container')){
     if(!m.checkVisibility()||!m.getBoundingClientRect().width)continue
     formulas++;const svg=m.querySelector('svg');if(!svg)continue
     const b=svg.getBoundingClientRect(),holder=m.closest('p,li,td,details')||m.parentElement,h=holder.getBoundingClientRect(),css=getComputedStyle(holder),available=h.width-parseFloat(css.paddingLeft||0)-parseFloat(css.paddingRight||0)
     if(b.width>available+2||b.left< -2||b.right>innerWidth+2)issues.push({kind:'math-overflow',formula:m.querySelector('mjx-assistive-mml')?.textContent,width:b.width,available,left:b.left,right:b.right})
     if(/auto|scroll/.test(getComputedStyle(m).overflowX+' '+getComputedStyle(m).overflowY))issues.push({kind:'math-scroll'})
    }
    for(const n of root.querySelectorAll('mjx-assistive-mml'))if(getComputedStyle(n).display!=='none')issues.push({kind:'assistive-visible'})
    for(const i of root.querySelectorAll('img'))if(!i.complete||!i.naturalWidth)issues.push({kind:'missing-image',src:i.src})
    if(root.querySelector('mjx-merror,[data-mjx-error]'))issues.push({kind:'math-error'})
    if(document.documentElement.scrollWidth>innerWidth+1)issues.push({kind:'page-overflow'})
    return{issues,formulas,images:root.querySelectorAll('img').length}
   })
   row.cases.push({width,...result});if(result.issues.length)row.errors.push({width,issues:result.issues})
  }
 }catch(e){row.errors.push({kind:'runtime',message:e.stack})}
 finally{
  await page.close();row.status=row.errors.length||row.requests.length?'findings':'passed-structure-and-layout'
  await writeFile(`${output}/ch${chapter}.json`,JSON.stringify(row,null,2)+'\n')
  const brief={chapter,status:row.status,units:row.units.length,expectedUnits:expected.observedEndUnitsIncludingGuidedDiscussionBridge,cases:row.cases.length,errors:row.errors.length,requestFailures:row.requests.length}
  report.chapters.push(brief);report.units+=brief.units;report.cases+=brief.cases;report.issues+=brief.errors+brief.requestFailures
  await writeFile(output+'/summary.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(brief))
 }
}}finally{await browser.close()}
report.status=report.issues?'findings':'passed-structure-and-layout';report.completedUTC=new Date().toISOString()
await writeFile(output+'/summary.json',JSON.stringify(report,null,2)+'\n')
console.log(JSON.stringify({status:report.status,chapters:report.chapters.length,units:report.units,cases:report.cases,issues:report.issues}))
if(report.issues)process.exitCode=1
