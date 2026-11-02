import puppeteer from 'puppeteer'
import { readFile,mkdir,writeFile } from 'node:fs/promises'
import path from 'node:path'
const root=path.resolve('../math-ai-visual-content'),output='qa/math-ai-visuals'
await mkdir(output,{recursive:true})
const browser=await puppeteer.launch({headless:true,userDataDir:`${output}/figure-browser-profile`,executablePath:process.env.CHROME_PATH||'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const page=await browser.newPage(),results=[]
try {
 for(const relative of process.argv.slice(2)) {
  const absolute=path.resolve(root,relative)
  if(!absolute.startsWith(root+path.sep)||!absolute.endsWith('.svg'))throw Error('Only course SVG sources are accepted')
  const source=await readFile(absolute,'utf8')
  await page.setViewport({width:360,height:900,deviceScaleFactor:1})
  await page.setContent(`<html><head><meta charset="utf-8"></head><body style="margin:0">${source}</body></html>`)
  const svg=await page.$('svg')
  const outside=await svg.evaluate(svg=>[...svg.querySelectorAll('text')].flatMap(e=>{
   const box=e.getBoundingClientRect(),frame=svg.getBoundingClientRect()
   return box.left<frame.left||box.right>frame.right||box.top<frame.top||box.bottom>frame.bottom?[e.textContent]:[]
  }))
  const name=path.basename(relative,'.svg')
  await svg.screenshot({path:`${output}/${name}-render.png`})
  results.push({source:relative,outside})
 }
 await writeFile(`${output}/figure-render-results.json`,JSON.stringify(results,null,2))
 console.log(JSON.stringify(results,null,2))
}finally{await browser.close()}
