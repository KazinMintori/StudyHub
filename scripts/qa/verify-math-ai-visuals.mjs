import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
import { readFile } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { spawn } from 'node:child_process'
import { createWriteStream } from 'node:fs'
import path from 'node:path'
import {inspectDiagramClarity} from './math-ai-diagram-clarity.mjs'

const base = process.env.QA_URL || 'http://127.0.0.1:5195'
const output = 'qa/math-ai-visuals'
await mkdir(output, { recursive: true })
const runId=new Date().toISOString().replace(/[^0-9]/g,'')
const evidencePath=`${output}/runs/${runId}`
await mkdir(evidencePath,{recursive:true})
let devProcess
if(process.env.QA_START_DEV==='1') {
  let reachable=false
  try{reachable=(await fetch(base,{signal:AbortSignal.timeout(2000)})).ok}catch(error){
    if(['EACCES','EPERM'].includes(error.cause?.code)){
      const reason={verifiedAt:new Date().toISOString(),phase:'localhost-access',code:error.cause.code,message:'The sandbox denied localhost access. No browser verification was performed.'}
      await writeFile(`${output}/bootstrap-error.json`,JSON.stringify(reason,null,2))
      throw Error(reason.message)
    }
  }
  if(!reachable){
    const url=new URL(base),log=createWriteStream(`${output}/qa-dev.log`,{flags:'a'})
    devProcess=spawn(process.execPath,[path.resolve('node_modules/vitepress/bin/vitepress.js'),'dev','docs','--host',url.hostname,'--port',url.port,'--strictPort'],{cwd:process.cwd(),windowsHide:true,stdio:['ignore','pipe','pipe']})
    devProcess.stdout.pipe(log);devProcess.stderr.pipe(log)
    process.once('exit',()=>devProcess?.kill())
    const deadline=Date.now()+90000
    while(Date.now()<deadline){
      if(devProcess.exitCode!==null)throw Error(`QA dev server exited ${devProcess.exitCode}; inspect qa-dev.log`)
      try{if((await fetch(base,{signal:AbortSignal.timeout(2000)})).ok){reachable=true;break}}catch{}
      await new Promise(resolve=>setTimeout(resolve,500))
    }
    if(!reachable)throw Error('QA dev server did not become ready; inspect qa-dev.log')
  }
}
const browser = await puppeteer.launch({ headless: true, userDataDir: `${output}/browser-profile`, executablePath: process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe' })
const page = await browser.newPage(), errors = [], results = [], issues = [], interactions = []
page.on('pageerror', e => errors.push(e.message))
page.on('response', response => {
  if (response.status() >= 400 && response.url().startsWith(base) && /\.(?:m?js|css|woff2?)(?:\?|$)/.test(response.url())) errors.push(`HTTP ${response.status()}: ${response.url()}`)
})
await page.evaluateOnNewDocument(() => { try { sessionStorage.setItem('studyhub_welcome_seen', '1') } catch {} })
await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])
const routes = [
  ['lecture00', '/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang.html'],
  ['least-norm', '/toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang/he-thieu-xac-dinh-va-giai-tich-ma-tran.html'],
  ['affine', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/duong-thang-va-tap-affine.html'],
  ['relint', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/noi-tuong-doi.html'],
  ['hyperplane', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/sieu-phang-va-nua-khong-gian.html'],
  ['cone', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/non-loi.html'],
  ['psd', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/non-psd.html'],
  ['norm', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/chuan-va-non-chuan.html'],
  ['ellipsoid', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/qua-cau-va-ellipsoid.html'],
  ['polyhedron', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/da-dien-va-don-hinh.html']
  ,['introduction', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/bai-toan-toi-uu.html']
  ,['models', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/hai-lop-bai-toan-kinh-dien.html']
  ,['operations', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/phep-toan-giu-tinh-loi.html']
  ,['robust', '/toan-cho-ai/bai-giang/bai-02-tap-loi/quy-hoach-non-bac-hai.html']
  ,['pareto', '/toan-cho-ai/bai-giang/bai-02-tap-loi/toi-uu-vector-va-danh-doi.html']
  ,['minimax', '/toan-cho-ai/bai-giang/bai-02-tap-loi/toi-uu-tua-loi.html']
  ,['gp', '/toan-cho-ai/bai-giang/bai-02-tap-loi/quy-hoach-hinh-hoc.html']
  ,['equality-qp', '/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange/qp-dang-thuc-va-mien-doi-ngau.html']
  ,['sensitivity', '/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange/rang-buoc-thua-va-do-nhay.html']
  ,['certificates', '/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange/chung-chi-chebyshev-va-doi-ngau-entropy.html']
  ,['slater-gap', '/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange/slater-khe-ho-va-doi-bieu-dien.html']
  ,['weighted-water', '/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange/water-filling-co-trong-so-va-tran.html']
  ,['odd-cycle', '/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange/max-cut-chu-trinh-le-va-sdp.html']
].filter(([name]) => !process.env.QA_CASES || process.env.QA_CASES.split(',').includes(name))
async function sourceManifest() {
  const paths = [
    ...routes.map(([,route])=>'docs'+route.replace(/\.html$/,'.md')),
    ...['AffinePlaneLab','AffineLab','RelintLab','NormBallLab','PredictionSpaceLab','SvdGeometryLab','QuadraticSpaceLab','LeastNormLab','GaussianGeometryLab','LikelihoodLab','HyperplaneLab','HyperplaneSpaceLab','Cone3DLab','ConeLab','NormSpaceLab','PsdLab','PolyhedronLab','SimplexSpaceLab','LeastSquaresSpaceLab','OptimumLab','LifeguardLab','LocalGlobalLab','SlabLab','AffineImageLab','LabPointControls'].map(name=>`src/features/labs/components/${name}.vue`),
    ...['FitLab','RobustBoxLab','RobustEllipsoidLab','RobustLPLab','ChanceConstraintLab','RidgeParetoLab','MinimaxRatioLab','GpParameterLab','EqualityQpDualLab','ResourceSensitivityLab','RedundantMultiplierLab','ChebyshevCertificateLab','EntropyDualLab','SlaterGapLab','WeightedWaterfillLab','OddCycleSdpLab','PerronGpLab'].map(name=>`src/features/labs/components/${name}.vue`),'src/core/math/components/MathMatrix.vue','src/features/labs/services/foundation-geometry.mjs','src/features/labs/services/convex-geometry.mjs','src/features/labs/services/diagram-labels.mjs','src/features/labs/controllers/svg-drag.js','src/app/styles/labs.css','docs/.vitepress/theme/tokens.css','scripts/qa/verify-math-ai-visuals.mjs','scripts/qa/math-ai-diagram-clarity.mjs'
  ]
  for(const [,route]of routes){
    const notes='docs'+route.replace(/\.html$/,'.md'),source=await readFile(notes,'utf8')
    const references=[...[...source.matchAll(/!\[[^\]]*\]\(<?([^\s)>]+)/g)].map(m=>m[1]),...[...source.matchAll(/<img\b[^>]*\bsrc=["']([^"']+)/g)].map(m=>m[1])]
    for(const reference of references){
      if(/^(?:https?:|data:|\/\/)/i.test(reference))continue
      const asset=decodeURIComponent(reference.split(/[?#]/)[0])
      const absolute=asset.startsWith('/')?path.resolve('docs/public','.'+asset):path.resolve(path.dirname(notes),asset)
      const relative=path.relative(process.cwd(),absolute).replaceAll('\\','/')
      if(!relative.startsWith('docs/'))throw Error('Image escaped documentation workspace: '+reference)
      paths.push(relative)
    }
  }
  return Object.fromEntries(await Promise.all([...new Set(paths)].map(async file=>[file,createHash('sha256').update(await readFile(file)).digest('hex')])))
}
const sourcesAtStart=await sourceManifest()

async function inspect(label) {
  const found = await page.evaluate(targetWidth => {
    document.querySelectorAll('.vp-doc details:not(.lab-tasks)').forEach(e => { e.open = true })
    const bad = []
    for (const el of document.querySelectorAll('.vp-doc mjx-container')) {
      const r = el.getBoundingClientRect(), s = el.querySelector('svg')?.getBoundingClientRect()
      if (!r.width) continue
      const parent = el.parentElement.getBoundingClientRect()
      const clipped = s && (s.width > r.width + 2 || r.right > targetWidth + 2 || r.left < -2)
      const scrolling = el.scrollWidth > el.clientWidth + 2 && /auto|scroll/.test(getComputedStyle(el).overflowX)
      if (clipped || scrolling) bad.push({ type: 'math', text: el.querySelector('mjx-assistive-mml')?.textContent || el.textContent, width: r.width, svg: s?.width, available: parent.width })
    }
    if (document.documentElement.scrollWidth > targetWidth + 2) bad.push({ type: 'page-overflow', width: document.documentElement.scrollWidth,expected:targetWidth })
    for(const element of document.querySelectorAll('.vp-doc math.math-matrix')){
      const rect=element.getBoundingClientRect()
      if(rect.width&&(rect.right>targetWidth+2||rect.left < -2))bad.push({type:'matrix-overflow',text:element.textContent,width:rect.width})
    }
    if (document.querySelector('mjx-merror,[data-mml-node="merror"]')) bad.push({ type: 'math-error' })
    for (const svg of document.querySelectorAll('.study-lab > svg,.study-lab > .lab-pair > svg')) {
      const vb = svg.viewBox.baseVal
      const outside = [...svg.querySelectorAll('text,polyline,polygon')].filter(e => {
        if (!e.getClientRects().length) return false
        const b = e.getBBox()
        return b.x < -2 || b.y < -2 || b.x + b.width > vb.width + 2 || b.y + b.height > vb.height + 2
      }).map(e => ({ tag: e.tagName, text: e.textContent, box: { x: e.getBBox().x, y: e.getBBox().y, w: e.getBBox().width, h: e.getBBox().height } }))
      if (outside.length) bad.push({ type: 'diagram-bounds', lab: svg.closest('figure').getAttribute('aria-label'), outside })
    }
    return bad
  },page.viewport().width)
  issues.push(...found.map(x => ({ label, ...x })))
  issues.push(...(await page.evaluate(inspectDiagramClarity)).map(x=>({label,...x})))
}

async function interact(touch) {
  const labs = await page.$$('figure.study-lab')
  for (let i = 0; i < labs.length; i++) {
    const lab = labs[i], handles = await lab.$$('.lab-handle')
    if(!handles.length&&await lab.$('input,select')){
      issues.push({label:page.url(),type:'interactive-lab-without-direct-handle',lab:await lab.evaluate(e=>e.getAttribute('aria-label')),width:page.viewport().width})
    }
    for (const [handleIndex, handle] of handles.entries()) {
    await page.evaluate(()=>document.activeElement?.blur())
    await handle.evaluate(e => e.scrollIntoView({ block: 'center', behavior: 'instant' }))
    await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))))
    await handle.evaluate(e => window.scrollTo({ top: scrollY + e.getBoundingClientRect().top - (visualViewport.offsetTop+visualViewport.height/2), behavior: 'instant' }))
    await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))))
    const before = await handle.evaluate(e => e.getAttribute('aria-valuetext'))
    const box = await handle.evaluate(e => { const r = e.getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height } })
    if (!box) continue
    const clientPoint={x:box.x+box.width/2,y:box.y+box.height/2}
    await handle.evaluate(e=>{
      window.__labPointerAbort?.abort()
      window.__labPointerAbort=new AbortController()
      window.__labPointerEvents=[]
      for(const type of ['pointerdown','pointermove','pointerup','pointercancel','lostpointercapture'])e.addEventListener(type,event=>{
        if(type!=='pointermove'||event.buttons||e.hasPointerCapture(event.pointerId))window.__labPointerEvents.push({type,pointerType:event.pointerType,trusted:event.isTrusted,captured:e.hasPointerCapture(event.pointerId)})
      },{signal:window.__labPointerAbort.signal})
    })
    const visual=await page.evaluate(()=>({x:visualViewport.offsetLeft,y:visualViewport.offsetTop}))
    const x=clientPoint.x-(touch?visual.x:0),y=clientPoint.y-(touch?visual.y:0)
    const hit = await page.evaluate(({ x, y }) => { const el = document.elementFromPoint(x, y); return el?.outerHTML.slice(0, 300) }, clientPoint)
    assert(await handle.evaluate((e,p)=>document.elementFromPoint(p.x,p.y)?.closest('.lab-handle')===e,clientPoint),`Handle is covered by another element: ${hit}`)
    const initialScroll=await page.evaluate(()=>scrollY)
    // Grab slightly away from the center, then send a zero-displacement move.
    // The point should retain its position inside the larger touch target.
    const grabX=x+Math.min(7,box.width/5),grabY=y-Math.min(5,box.height/5)
    if (touch) {
      const client = await page.createCDPSession()
      await client.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x:grabX, y:grabY }] })
      await client.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x:grabX, y:grabY }] })
      await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(resolve)))
      const stationary=await handle.evaluate(e=>{const r=e.getBoundingClientRect();return [r.x+r.width/2,r.y+r.height/2]})
      assert(Math.hypot(stationary[0]-clientPoint.x,stationary[1]-clientPoint.y)<2.5,`Point jumped at off-center touch: lab ${i}`)
      await client.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x: grabX + 24, y: grabY - 21 }] })
      await client.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] })
      await client.detach()
    } else {
      await page.mouse.move(grabX,grabY);await page.mouse.down();await page.mouse.move(grabX,grabY)
      await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(resolve)))
      const stationary=await handle.evaluate(e=>{const r=e.getBoundingClientRect();return [r.x+r.width/2,r.y+r.height/2]})
      assert(Math.hypot(stationary[0]-clientPoint.x,stationary[1]-clientPoint.y)<2.5,`Point jumped at off-center mouse grab: lab ${i}`)
      await page.mouse.move(grabX+24,grabY-21,{steps:6});await page.mouse.up()
    }
    const after = await handle.evaluate(e => e.getAttribute('aria-valuetext'))
    if (after === before) {
      await page.screenshot({ path: `${evidencePath}/drag-failure.png` })
      const viewport = await page.evaluate(() => ({ width:innerWidth,height:innerHeight,scrollY,visual:{width:visualViewport.width,height:visualViewport.height,scale:visualViewport.scale,top:visualViewport.offsetTop} }))
      console.log(JSON.stringify({ lab: i, url: page.url(), box, hit, before, after,viewport }))
    }
    assert.notEqual(after, before, `Direct ${touch ? 'touch' : 'mouse'} drag did not move lab ${i}`)
    const events=await page.evaluate(()=>window.__labPointerEvents)
    assert(events.some(e=>e.type==='pointerdown'&&e.pointerType===(touch?'touch':'mouse')&&e.trusted),'Expected real input pointer events')
    assert(events.some(e=>e.type==='pointermove'&&e.captured),`Pointer was not captured during drag: ${page.url()}, lab ${i}, handle ${handleIndex}, ${JSON.stringify(events)}`)
    assert(Math.abs((await page.evaluate(()=>scrollY))-initialScroll)<2,'Dragging a handle scrolled the page')
    interactions.push({url:page.url(),width:page.viewport().width,input:touch?'touch':'mouse',lab:i,handle:handleIndex,before,after,offCenterGrab:true,pageStayedStill:true,events})
    await handle.evaluate(e => e.focus())
    for (const key of ['ArrowUp', 'ArrowDown', 'ArrowRight', 'ArrowLeft']) {
      await page.keyboard.press(key)
      if (await handle.evaluate(e => e.getAttribute('aria-valuetext')) !== after) break
    }
    const keyed = await handle.evaluate(e => e.getAttribute('aria-valuetext'))
    assert.notEqual(keyed, after, `Keyboard did not move lab ${i}`)
    const canvasId=await handle.evaluate(e=>e.closest('svg').id)
    const buttons = canvasId ? await lab.$$(`.lab-point-controls[aria-controls="${canvasId}"] .lab-point-directions button:not([disabled])`) : []
    if (buttons.length) {
      const button=buttons[0]
      await button.evaluate(e => { const details = e.closest('details'); if (details) details.open = true })
      await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))))
      const beforeButton=await handle.evaluate(e=>e.getAttribute('aria-valuetext'))
      for(const direction of buttons){
        await direction.evaluate(e=>e.scrollIntoView({block:'center',behavior:'instant'}))
        const box=await direction.evaluate(e=>{const r=e.getBoundingClientRect();return{x:r.x+r.width/2,y:r.y+r.height/2,width:r.width,height:r.height}})
        assert(box.width>0&&box.height>0,'Direction button is hidden after opening its controls')
        if(touch){
          const offset=await page.evaluate(()=>({x:visualViewport.offsetLeft,y:visualViewport.offsetTop}))
          await page.touchscreen.tap(box.x-offset.x,box.y-offset.y)
        }else{await page.mouse.click(box.x,box.y)}
        if(await handle.evaluate(e=>e.getAttribute('aria-valuetext'))!==beforeButton)break
      }
      assert.notEqual(await handle.evaluate(e=>e.getAttribute('aria-valuetext')),beforeButton,`Direction buttons did not move the selected handle: lab ${i}, handle ${handleIndex}`)
      results.push(`alternative-button-${i}`)
      await button.evaluate(e => { e.blur(); const details = e.closest('details'); if (details) details.open = false })
    }
    results.push(`${touch ? 'touch' : 'mouse'}-drag-${i}-${handleIndex}`)
    }
  }
}

async function checkPageScroll(touch) {
  const diagrams=await page.$$('.study-lab > svg,.study-lab > .lab-pair > svg')
  for(const [index,svg]of diagrams.entries()){
    await page.evaluate(()=>document.activeElement?.blur())
    await svg.evaluate(e=>e.scrollIntoView({block:'center',behavior:'instant'}))
    const point=await svg.evaluate(e=>{
      const r=e.getBoundingClientRect(),v=visualViewport
      for(const [u,w]of [[.12,.15],[.85,.15],[.85,.8],[.12,.8]]){
        const x=r.x+r.width*u,y=r.y+r.height*w,hit=document.elementFromPoint(x,y)
        if(hit&&e.contains(hit)&&!hit.closest('.lab-handle,[role="button"]'))return{x:x-v.offsetLeft,y:y-v.offsetTop}
      }
      return null
    })
    assert(point,'No empty canvas location found for page scrolling')
    const before=await page.evaluate(()=>scrollY)
    if(touch){
      const client=await page.createCDPSession()
      await client.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[point]})
      for(let step=1;step<=6;step++){
        await client.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:point.x,y:point.y-step*15}]})
        await new Promise(resolve=>setTimeout(resolve,20))
      }
      await client.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});await client.detach()
    }else{await page.mouse.move(point.x,point.y);await page.mouse.wheel({deltaY:90})}
    await new Promise(resolve=>setTimeout(resolve,300))
    const after=await page.evaluate(()=>scrollY)
    assert(after>before+20,`Page cannot scroll over empty diagram ${index} with ${touch?'touch':'wheel'}`)
    interactions.push({url:page.url(),width:page.viewport().width,input:touch?'touch':'mouse',diagram:index,emptyCanvasScroll:after-before})
  }
}

async function checkCycleButtons(touch){
 const buttons=await page.$$('figure.study-lab circle[role="button"]')
 assert.equal(buttons.length,5,'Expected five directly selectable graph vertices')
 for(const [index,button]of buttons.entries()){
  await button.evaluate(e=>e.scrollIntoView({block:'center',behavior:'instant'}))
  const before=await button.evaluate(e=>e.getAttribute('aria-pressed'))
  const point=await button.evaluate(e=>{const r=e.getBoundingClientRect();return{x:r.x+r.width/2,y:r.y+r.height/2}})
  if(touch){
   const offset=await page.evaluate(()=>({x:visualViewport.offsetLeft,y:visualViewport.offsetTop}))
   await page.touchscreen.tap(point.x-offset.x,point.y-offset.y)
  }else{await page.mouse.click(point.x,point.y)}
  assert.notEqual(await button.evaluate(e=>e.getAttribute('aria-pressed')),before,`Vertex ${index} did not change group`)
  await button.evaluate(e=>e.focus());await page.keyboard.press('Space')
  assert.equal(await button.evaluate(e=>e.getAttribute('aria-pressed')),before,`Keyboard did not restore vertex ${index}`)
  interactions.push({url:page.url(),width:page.viewport().width,input:touch?'touch':'mouse',graphVertex:index,toggleAndKeyboardRestore:true})
 }
}

async function clickControl(button,touch){
 await page.evaluate(()=>document.activeElement?.blur())
 await button.evaluate(e=>e.scrollIntoView({block:'center',behavior:'instant'}))
 const p=await button.evaluate(e=>{const r=e.getBoundingClientRect();return{x:r.x+r.width/2,y:r.y+r.height/2}})
 if(touch){const v=await page.evaluate(()=>({x:visualViewport.offsetLeft,y:visualViewport.offsetTop}));await page.touchscreen.tap(p.x-v.x,p.y-v.y)}
 else await page.mouse.click(p.x,p.y)
 await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))))
}
async function exercisePresets(name,touch){
 const labs=await page.$$('figure.study-lab')
 const cases={
  'equality-qp':[[0,'Đưa x về tối ưu'],[0,'Đưa ν về tối ưu']],
  sensitivity:[[0,'Chỉ dùng hai ràng buộc đầu'],[0,'Chỉ dùng ràng buộc thứ ba'],[1,'b = 1'],[1,'b = 3'],[1,'b = 2.2, neo tại 2']],
  certificates:[[0,'Đường tối ưu'],[0,'Chứng chỉ tối ưu'],[1,'Phân phối tối ưu'],[1,'Nhân tử tối ưu']],
  'slater-gap':[[0,'u = −0.5'],[0,'u = 0'],[0,'u = 0.5'],[0,'u = 0']],
  'weighted-water':[[0,'P = 1, ν = 0.75'],[0,'P = 1.5'],[0,'P = 3'],[0,'Chọn một nhân tử tối ưu'],[0,'P = 1, ν = 0.75']],
  'odd-cycle':[[0,'Tất cả cùng nhóm'],[0,'Đưa phân hoạch thành Gram hạng 1'],[0,'Một phân hoạch tối ưu'],[0,'Vector SDP tối ưu']]
 }[name]||[]
 for(const [index,label]of cases){
  const buttons=await labs[index].$$('.lab-buttons button')
  let found
  for(const button of buttons)if(await button.evaluate((e,label)=>e.textContent.trim()===label,label)){found=button;break}
  assert(found,`Missing preset ${label}`)
  await clickControl(found,touch)
  await inspect(`${name}-${page.viewport().width}-${touch?'touch':'mouse'}-preset-${label}`)
  interactions.push({url:page.url(),width:page.viewport().width,input:touch?'touch':'mouse',preset:label,lab:index,readout:await labs[index].$eval('.lab-readout',e=>e.innerText)})
 }
 if(name==='equality-qp'){
  const select=await labs[0].$('.lab-controls select'),options=await select.$$eval('option',rows=>rows.map(e=>e.value))
  for(const option of options){await select.select(option);await inspect(`${name}-${page.viewport().width}-select-${option}`);results.push(`${name}-coordinate-${option}`)}
 }
 if(name==='weighted-water'){
  const checkbox=await labs[0].$('input[type=checkbox]')
  await clickControl(checkbox,touch);await inspect(`${name}-normalized-levels`)
 }
 if(name==='equality-qp')assert((await labs[0].$eval('.lab-readout',e=>e.innerText)).includes('khoảng rộng 0.00000'),'QP optimal presets did not close the certificate')
 if(name==='certificates'){
  assert((await labs[0].$eval('.lab-readout',e=>e.innerText)).includes('chứng nhận là 0.0000'),'Chebyshev presets did not close the certificate')
  assert((await labs[1].$eval('.lab-readout',e=>e.innerText)).includes('độ rộng 0.000000'),'Entropy presets did not close the certificate')
 }
 if(name==='odd-cycle')assert((await labs[0].$eval('.lab-readout',e=>e.innerText)).includes('bằng 0.000000'),'SDP optimal preset did not reach its certified bound')
}

try {
  for (const theme of (process.env.QA_THEMES || 'light,dark').split(',')) for (const width of (process.env.QA_WIDTHS || '360,375,1440').split(',').map(Number)) {
    const touch=process.env.QA_INPUT?process.env.QA_INPUT==='touch':width<600
    await page.setViewport({ width, height:Number(process.env.QA_HEIGHT||900),hasTouch:touch,isMobile:touch })
    for (const [name, route] of routes) {
      const response = await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 120000 })
      assert.equal(response.status(), 200)
      await page.waitForSelector('.study-lab .lab-handle', { timeout: 60000 })
      await page.evaluate(() => document.fonts.ready)
      await page.evaluate(theme => document.documentElement.classList.toggle('dark', theme === 'dark'), theme)
      await inspect(`${name}-${width}-${theme}-initial`)
      if(!process.env.QA_LAYOUT_ONLY){await interact(touch);if(name==='odd-cycle')await checkCycleButtons(touch);await checkPageScroll(touch);await exercisePresets(name,touch)}
      // Exercise 3D/2D mode switches and singular/degenerate presets via controls.
      if (name === 'lecture00') {
        for (const text of ['Vector dự đoán trong R³', 'Miền đầu vào R²', 'Mặt mật độ trong R³']) {
          const button = await page.$(`button::-p-text(${text})`)
          assert(button, text); await button.click()
        }
      } else if (name === 'least-norm') {
        await (await page.$('button::-p-text(R²: Một đường thẳng)')).click()
      }
      await inspect(`${name}-${width}-${theme}-alternate`)
      if (name === 'lecture00' && width === 375 && theme === 'light') {
        for (const imageName of ['cholesky-process', 'dense-and-banded']) {
          const figure=await page.$(`.vp-doc img[src$="/${imageName}.svg"]`)
          assert(figure, imageName)
          await figure.evaluate(e=>e.scrollIntoView({block:'center',behavior:'instant'}))
          await figure.screenshot({path:`${evidencePath}/${imageName}-375.png`})
        }
      }
      const labs = await page.$$('figure.study-lab')
      for (let i = 0; i < labs.length; i++) {
       const panels=await labs[i].$$(':scope > svg,:scope > .lab-pair > svg')
       for(const [panelIndex,diagram]of panels.entries()){
        await diagram.evaluate(e => e.scrollIntoView({ block: 'center', behavior: 'instant' }))
        const box = await diagram.evaluate(e => { const r = e.getBoundingClientRect(); return { x: r.left + scrollX, y: r.top + scrollY, width: r.width, height: r.height } })
        await page.screenshot({ path: `${evidencePath}/${name}-${width}-${theme}-diagram${i}${panelIndex?'-panel'+panelIndex:''}.png`, clip: box, captureBeyondViewport: true })
       }
      }
      results.push(`${name}-${width}-${theme}`)
      console.log(`Verified ${name}, ${width}px, ${touch?'touch':'mouse'}, ${theme}`)
    }
  }
} catch(error) {
  errors.push(`Verification aborted: ${error.message}`)
  throw error
} finally {
  const sources=await sourceManifest()
  if(JSON.stringify(sources)!==JSON.stringify(sourcesAtStart)) errors.push('Source changed during browser verification; rerun the affected cases against a fixed source snapshot.')
  const report=JSON.stringify({base,evidencePath,viewportHeight:Number(process.env.QA_HEIGHT||900),inputOverride:process.env.QA_INPUT||null,mode:process.env.QA_LAYOUT_ONLY?'layout-only':'interaction-and-layout',verifiedAt:new Date().toISOString(),sources,results,interactions,errors,issues},null,2)
  const latest=`${output}/browser-results${process.env.QA_CASES?'-'+process.env.QA_CASES.replaceAll(',','-'):''}${process.env.QA_LAYOUT_ONLY?'-layout':''}.json`
  try{await writeFile(`${evidencePath}/previous-report.json`,await readFile(latest))}catch(error){if(error.code!=='ENOENT')throw error}
  await writeFile(`${evidencePath}/report.json`,report)
  await writeFile(latest,report)
  await browser.close()
  devProcess?.kill()
}
console.log(JSON.stringify({ checks: results.length, errors:errors.length, issues:issues.length,details:output }, null, 2))
assert.equal(errors.length,0,'Runtime/resource errors; inspect browser-results JSON')
assert.equal(issues.length,0,'Layout problems; inspect browser-results JSON')
