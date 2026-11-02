import {readFile,mkdir,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'

const output=`qa/math-ai-visuals/runs/slack-svg-${new Date().toISOString().replace(/[^0-9]/g,'')}`
await mkdir(output,{recursive:true})
const files=['slack-lift-2d','slack-lift-3d'].map(name=>`../math-ai-visual-content/docs/toan-cho-ai/bai-giang/img/lec-02/${name}.svg`)
const browser=await puppeteer.launch({headless:true,userDataDir:'qa/math-ai-visuals/browser-profile',executablePath:process.env.CHROME_PATH||'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const page=await browser.newPage(),results=[],issues=[],sources={}
try{
 for(const file of files){
  const source=await readFile(file)
  sources[file]=createHash('sha256').update(source).digest('hex')
  for(const width of [294,400]){
   await page.setViewport({width:width+20,height:600})
   await page.setContent(`<style>body{margin:10px}svg{display:block;width:${width}px;height:auto}</style>${source.toString().replace(/<\?xml[^>]*>/,'')}`)
   await page.evaluate(()=>document.fonts.ready)
   const found=await page.evaluate(()=>{
    const svg=document.querySelector('svg'),box=svg.viewBox.baseVal,bad=[]
    const labels=[...svg.querySelectorAll('text')].map(el=>({text:el.textContent,bounds:el.getBBox(),client:el.getBoundingClientRect()}))
    for(const label of labels){
     const b=label.bounds
     if(b.x<0||b.y<0||b.x+b.width>box.width||b.y+b.height>box.height)bad.push({type:'text-outside',text:label.text,box:{x:b.x,y:b.y,width:b.width,height:b.height}})
    }
    for(let i=0;i<labels.length;i++)for(let j=i+1;j<labels.length;j++){
     const a=labels[i],b=labels[j],w=Math.min(a.client.right,b.client.right)-Math.max(a.client.left,b.client.left),h=Math.min(a.client.bottom,b.client.bottom)-Math.max(a.client.top,b.client.top)
     if(w>1.5&&h>1.5)bad.push({type:'label-overlap',labels:[a.text,b.text],w,h})
    }
    return bad
   })
   issues.push(...found.map(issue=>({file,width,...issue})))
   await (await page.$('svg')).screenshot({path:`${output}/${file.split('/').at(-1).replace('.svg','')}-${width}.png`})
   results.push({file,width,issues:found.length})
  }
  assert.equal(createHash('sha256').update(await readFile(file)).digest('hex'),sources[file],'SVG changed during verification')
 }
}finally{
 await browser.close()
 await writeFile(`${output}/report.json`,JSON.stringify({scope:'Actual Chrome font bounds, overlap and rendered static SVG; no interaction claims',sources,results,issues},null,2))
}
console.log(JSON.stringify({output,checks:results.length,issues},null,2))
assert.equal(issues.length,0,'SVG labels need correction; inspect the retained report')
