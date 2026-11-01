import assert from 'node:assert/strict'
import { mkdir, writeFile, readFile } from 'node:fs/promises'
import puppeteer from 'puppeteer'

const base = (process.env.QA_URL || 'http://127.0.0.1:5173').replace(/\/$/, '')
const output = 'qa/toan-ai-homework'
await mkdir(output, { recursive: true })
const expected = [
  [4,4,4,4,4,4,4,4,4,4],
  [2,3,3,3,3,3,4,5],
  [3,3,3,3,4,4,4,4],
  [4,3,4,4,4,4],
  [4,4,4,4,4,5,5,5]
]
const routes = expected.map((_,i)=>`/toan-cho-ai/problem-set/homework-0${i+1}.html`)
const results = [], errors = []
const browser = await puppeteer.launch({headless:true,args:['--no-sandbox']})
const page = await browser.newPage()
page.on('pageerror', error=>errors.push({url:page.url(),message:error.message}))
await page.evaluateOnNewDocument(()=>sessionStorage.setItem('studyhub_welcome_seen','1'))
await page.emulateMediaFeatures([{name:'prefers-reduced-motion',value:'reduce'}])
try {
  for (const [index,route] of routes.entries()) {
    const source = await readFile(`docs${route.replace('.html','.md')}`,'utf8')
    const exercises = [...source.matchAll(/^::: exercise[^\n]*\n([\s\S]*?)^:::/gm)]
    const solutions = [...source.matchAll(/^::: solution[^\n]*\n([\s\S]*?)^:::/gm)]
    assert.equal(exercises.length,expected[index].length,`Exercise coverage: ${route}`)
    assert.equal(solutions.length,exercises.length,`Solution coverage: ${route}`)
    // A label at the start of a separate paragraph, optionally bold or a heading.
    for (const [i,count] of expected[index].entries()) {
      for (const [kind,block] of [['exercise',exercises[i]],['solution',solutions[i]]]) {
        const letters = [...block[1].matchAll(/^(?:#{1,6}\s+)?(?:\*\*)?([a-e])[).](?:\*\*)?\s/gm)].map(m=>m[1])
        assert.deepEqual(letters, 'abcde'.slice(0,count).split(''),`${route} ${kind} ${i+1}: Separate complete subparts`)
      }
    }
  }
  for (const width of (process.env.QA_WIDTHS || '360,375,1440').split(',').map(Number)) {
    await page.setViewport({width,height:900})
    for (const route of routes) {
      const response = await page.goto(base+route,{waitUntil:'networkidle0',timeout:90000})
      assert(response.ok(),route)
      await page.waitForSelector('.vp-doc .exercise')
      await page.evaluate(async()=>{
        await document.fonts.ready
        document.querySelectorAll('.vp-doc details').forEach(el=>el.open=true)
        await Promise.all([...document.querySelectorAll('.vp-doc img')].map(async image=>{
          image.loading='eager'
          await image.decode().catch(()=>{})
        }))
        await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))
      })
      const metrics=await page.evaluate(()=>({
        pageWidth:document.documentElement.scrollWidth,
        errors:document.querySelectorAll('[data-mjx-error],merror,[data-mml-node="merror"]').length,
        scrollbars:[...document.querySelectorAll('.vp-doc mjx-container')].filter(el=>el.checkVisibility()&&(['auto','scroll'].includes(getComputedStyle(el).overflowX)||['auto','scroll'].includes(getComputedStyle(el).overflowY))).length,
        visibleMathML:[...document.querySelectorAll('.vp-doc mjx-assistive-mml')].filter(el=>el.checkVisibility()).length,
        overflow:[...document.querySelectorAll('.vp-doc mjx-container')].filter(el=>el.checkVisibility()).flatMap((el,index)=>{
          const svg=el.querySelector('svg'),r=svg?.getBoundingClientRect(),box=el.closest('.custom-block')||el.closest('.vp-doc')
          // Tables have their own scrolling viewport. Math itself must still
          // have no overflow or scrollbar; offscreen table cells are allowed.
          const table=el.closest('table')
          if(table && table.scrollWidth>table.clientWidth+1)return []
          const b=box.getBoundingClientRect()
          const style=getComputedStyle(box)
          const left=b.left+parseFloat(style.paddingLeft)+parseFloat(style.borderLeftWidth)
          const right=b.right-parseFloat(style.paddingRight)-parseFloat(style.borderRightWidth)
          if(!r || r.width<1)return []
          return el.scrollWidth>el.clientWidth+2 || r.left<left-2 || r.right>right+2 || r.left<0 || r.right>innerWidth+1
            ? [{index,left:r.left,right:r.right,container:el.clientWidth,scroll:el.scrollWidth,formula:el.textContent.slice(0,220)}] : []
        }),
        estimates:/phút đọc|thời gian đọc|tổng cộng khoảng \d+ phút/i.test(document.body.innerText),
        images:[...document.querySelectorAll('.vp-doc img')].map(el=>({src:el.getAttribute('src'),ok:el.complete&&el.naturalWidth>0}))
      }))
      results.push({width,route,...metrics})
      const failed=metrics.pageWidth>width+1||metrics.errors||metrics.scrollbars||metrics.visibleMathML||metrics.overflow.length||metrics.estimates||metrics.images.some(im=>!im.ok)
      if ((width===360&&route===routes[0])||(width===1440&&route===routes[4])) await page.screenshot({path:`${output}/homework-${width}.png`,fullPage:false})
      console.log(`${failed?'FAIL':'PASS'} ${width}px ${route}`)
    }
    // Exercise the shared header, topic map, course overview and sidebar too.
    for(const route of ['/','/toan-cho-ai/','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/bai-toan-toi-uu.html']){
      await page.goto(base+route,{waitUntil:'networkidle0',timeout:90000})
      const text=await page.$eval('body',el=>el.innerText)
      assert(!/phút đọc|thời gian đọc|tổng cộng khoảng \d+ phút|Khoảng \d+ phút/i.test(text),`Reading estimate remains: ${route}`)
    }
  }
  assert.deepEqual(results.filter(r=>r.pageWidth>r.width+1||r.errors||r.scrollbars||r.visibleMathML||r.overflow.length||r.estimates||r.images.some(im=>!im.ok)),[],'All homework math must fit its actual frame')
  assert.deepEqual(errors,[])
  console.log('PASS complete source coverage, math at 360/375/1440, figures and no reading estimates')
} finally {
  await writeFile(`${output}/browser-results.json`,JSON.stringify({results,errors},null,2)+'\n')
  await browser.close()
}
