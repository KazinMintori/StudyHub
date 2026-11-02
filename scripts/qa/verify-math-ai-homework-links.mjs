// Verify the exact anchors referenced by lectures against rendered homework DOM.
import {readFile,readdir,mkdir,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {spawn} from 'node:child_process'
import path from 'node:path'
import assert from 'node:assert/strict'
import puppeteer from 'puppeteer'
const base='http://127.0.0.1:5195',directory='docs/toan-cho-ai/bai-giang',references=[],sources={}
async function walk(directory){
 for(const entry of await readdir(directory,{withFileTypes:true})){
  const file=path.join(directory,entry.name)
  if(entry.isDirectory()){await walk(file);continue}
  if(!file.endsWith('.md'))continue
  const data=await readFile(file),source=data.toString('utf8')
  for(const match of source.matchAll(/\[[^\]]+\]\(([^\s)]+homework-\d+\.md)(#[^\s)]*)?\)/g)){
   if(/^[a-z]+:/i.test(match[1]))continue
   const target=path.resolve(path.dirname(file),match[1]),relative=path.relative(process.cwd(),target).replaceAll('\\','/')
   assert(relative.startsWith('docs/toan-cho-ai/problem-set/'),'Unexpected homework target')
   references.push({source:file.replaceAll('\\','/'),target:relative,anchor:decodeURIComponent((match[2]||'').slice(1))})
   sources[file.replaceAll('\\','/')]=createHash('sha256').update(data).digest('hex')
  }
 }
}
await walk(directory)
assert(references.length,'No lecture homework references found')
let server,browser
const results=[],issues=[],output=`qa/math-ai-visuals/runs/links-${Date.now()}`
await mkdir(output,{recursive:true})
try{
 let ready=false
 try{ready=(await fetch(base,{signal:AbortSignal.timeout(2000)})).ok}catch{}
 if(!ready){
  server=spawn(process.execPath,[path.resolve('node_modules/vitepress/bin/vitepress.js'),'dev','docs','--host','127.0.0.1','--port','5195','--strictPort'],{windowsHide:true,stdio:'ignore'})
  const deadline=Date.now()+90000
  while(Date.now()<deadline){
   if(server.exitCode!==null)throw Error('Dev server exited before link verification')
   try{if((await fetch(base,{signal:AbortSignal.timeout(2000)})).ok){ready=true;break}}catch{}
   await new Promise(resolve=>setTimeout(resolve,500))
  }
  assert(ready,'Dev server did not start')
 }
 browser=await puppeteer.launch({headless:true,userDataDir:'qa/math-ai-visuals/browser-profile',executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'})
 const page=await browser.newPage()
 for(const target of [...new Set(references.map(r=>r.target))]){
  const data=await readFile(target);sources[target]=createHash('sha256').update(data).digest('hex')
  const response=await page.goto(base+'/'+target.slice(5).replace(/\.md$/,'.html'),{waitUntil:'networkidle0',timeout:120000})
  assert.equal(response.status(),200,target)
  await page.waitForSelector('.vp-doc h2[id]',{timeout:60000})
  const ids=await page.$$eval('.vp-doc [id]',elements=>elements.map(e=>e.id))
  for(const reference of references.filter(r=>r.target===target)){
   const exists=!reference.anchor||ids.includes(reference.anchor)
   results.push({...reference,exists})
   if(!exists)issues.push({...reference,actualSectionIds:ids.filter(id=>id.startsWith('bai-'))})
  }
 }
 for(const [file,hash]of Object.entries(sources))assert.equal(createHash('sha256').update(await readFile(file)).digest('hex'),hash,'Source changed during link verification')
}finally{
 await writeFile(`${output}/report.json`,JSON.stringify({verifiedAt:new Date().toISOString(),scope:'Rendered homework routes and exact lecture anchor references',sources,results,issues},null,2))
 await browser?.close();server?.kill()
}
console.log(JSON.stringify({references:results.length,issues,details:output},null,2))
assert.equal(issues.length,0,'Homework anchors do not match the actual headings')
