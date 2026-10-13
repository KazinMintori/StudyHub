import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import {writeFile,mkdir} from 'node:fs/promises'
import {startPhysicsPreview} from './physics-qa-server.mjs'
import {electrostaticsConcepts} from '../docs/.vitepress/physics-electrostatics-foundations.mjs'
import {gaussConcepts} from '../docs/.vitepress/physics-gauss-foundations.mjs'
import {potentialConcepts} from '../docs/.vitepress/physics-potential-foundations.mjs'
import {capacitanceConcepts} from '../docs/.vitepress/physics-capacitance-foundations.mjs'
import {currentConcepts} from '../docs/.vitepress/physics-current-foundations.mjs'
import {dcConcepts} from '../docs/.vitepress/physics-dc-foundations.mjs'
import {magneticConcepts} from '../docs/.vitepress/physics-magnetic-foundations.mjs'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {sourcesConcepts} from '../docs/.vitepress/physics-sources-foundations.mjs'
const preview=await startPhysicsPreview()
const browser=await puppeteer.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const page=await browser.newPage(),results=[],errors=[]
page.on('pageerror',error=>errors.push(error.message))
await page.evaluateOnNewDocument(()=>sessionStorage.setItem('studyhub_welcome_seen','1'))
const readyConcepts=[physics1Course,physics2Course].flatMap(course=>course.lessons.filter(lesson=>lesson.status==='ready').flatMap(lesson=>[...(lesson.prerequisites||[]),...(lesson.supportingConcepts||[])]))
const ids=[...new Set([...Object.keys({...electrostaticsConcepts,...gaussConcepts,...potentialConcepts,...capacitanceConcepts,...currentConcepts,...dcConcepts,...magneticConcepts,...sourcesConcepts}),...readyConcepts])]
try{
 for(const width of [320,375,1440]){
  await page.setViewport({width,height:900})
  for(const id of ids){
   const response=await page.goto(`${preview.url}/wiki/${id}.html`,{waitUntil:'domcontentloaded',timeout:45000})
   assert.equal(response.status(),200,id)
   await page.waitForSelector('.vp-doc h1')
   await page.evaluate(()=>document.fonts.ready)
   const failures=await page.evaluate(()=>{
    document.querySelectorAll('.vp-doc details').forEach(e=>e.open=true)
    const bad=[...document.querySelectorAll('mjx-container')].filter(e=>e.getBoundingClientRect().width>0).flatMap(e=>{
     const r=e.getBoundingClientRect(),svg=e.querySelector('svg')?.getBoundingClientRect(),s=getComputedStyle(e)
     return r.right>innerWidth+2||r.left< -2||svg?.width>r.width+2||(['auto','scroll'].includes(s.overflowX)&&e.scrollWidth>e.clientWidth+1)
      ?[{text:e.textContent,width:r.width,svg:svg?.width}]:[]
    })
    return {bad,documentOverflow:document.documentElement.scrollWidth>innerWidth+2,mathErrors:document.querySelectorAll('mjx-merror,[data-mml-node="merror"]').length}
   })
   results.push({id,width,...failures})
  }
 }
 await mkdir('qa/physics/wiki',{recursive:true})
 const failed=results.filter(r=>r.bad.length||r.documentOverflow||r.mathErrors)
 await writeFile('qa/physics/wiki/browser-results.json',JSON.stringify({checks:results.length,errors,failed},null,2)+'\n')
 assert.deepEqual(errors,[])
 assert.deepEqual(failed,[])
 console.log('Passed',results.length,'Physics Wiki views at 320, 375 and 1440 px.')
}finally{await browser.close();await preview.close()}
