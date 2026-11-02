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
  ['optimization-overview','/toan-cho-ai/bai-giang/bai-02-tap-loi.html'],
  ['duality-overview','/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange.html'],
  ['equivalence','/toan-cho-ai/bai-giang/bai-02-tap-loi/bai-toan-tuong-duong.html'],
  ['elimination','/toan-cho-ai/bai-giang/bai-02-tap-loi/khu-rang-buoc-va-toi-uu-tung-phan.html'],
  ['function-operations','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/phep-toan-giu-tinh-loi-cua-ham.html'],
  ['optimality','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/dieu-kien-toi-uu.html'],
  ['ml-models','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/tinh-loi-trong-mo-hinh-hoc-may.html'],
  ['local-global','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/cuc-bo-va-toan-cuc.html'],
  ['known-functions','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/cac-ham-loi-quen-thuoc.html'],
  ['convex-function','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/ham-loi.html'],
  ['epigraph','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/epigraph-tap-muc-duoi-jensen.html'],
  ['first-order','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/dieu-kien-bac-nhat.html'],
  ['second-order','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/dieu-kien-bac-hai.html'],
  ['perspective','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/phoi-canh-va-phan-tuyen-tinh.html'],
  ['order','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/bat-dang-thuc-tong-quat.html'],
  ['separation','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/sieu-phang-phan-tach-va-tua.html'],
  ['dual-cone','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/non-doi-ngau.html'],
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
    'src/features/labs/components/SlackLiftLab.vue','src/features/labs/components/MaxEpigraphLab.vue',
    'src/features/labs/components/EliminationLab.vue',
    'src/features/labs/components/SensorWeightsLab.vue',
    'src/features/labs/components/BisectionLab.vue','src/features/labs/components/MinimaxRatioLab.vue','src/features/labs/services/apollonius-feasibility.mjs',
    ...['AffinePlaneLab','AffineLab','RelintLab','NormBallLab','PredictionSpaceLab','SvdGeometryLab','QuadraticSpaceLab','LeastNormLab','GaussianGeometryLab','LikelihoodLab','HyperplaneLab','HyperplaneSpaceLab','Cone3DLab','ConeLab','NormSpaceLab','PsdLab','PolyhedronLab','SimplexSpaceLab','LeastSquaresSpaceLab','OptimumLab','LifeguardLab','LocalGlobalLab','SlabLab','AffineImageLab','LabPointControls'].map(name=>`src/features/labs/components/${name}.vue`),
    ...['EquivalenceLab','EnvelopeLab','CompositionLab','OptimalityLab','LogisticLab','LogDetLab','PowerLab','SoftmaxLab','FunctionLab','ConvexSurfaceLab','ElboLab','Restrict2DLab','GradientCutLab','HessianMapLab','PerspectiveLab','PerspectiveSpaceLab','ConditionalMixLab','SeparationLab','SeparationGapLab','XorLiftLab','OrderLab','ConeClosureLab','FitLab','RobustBoxLab','RobustEllipsoidLab','RobustLPLab','ChanceConstraintLab','RidgeParetoLab','MinimaxRatioLab','GpParameterLab','EqualityQpDualLab','ResourceSensitivityLab','RedundantMultiplierLab','ChebyshevCertificateLab','EntropyDualLab','SlaterGapLab','WeightedWaterfillLab','OddCycleSdpLab','PerronGpLab'].map(name=>`src/features/labs/components/${name}.vue`),'src/core/math/components/MathMatrix.vue','src/features/site/components/FeedbackWidget.vue','src/features/labs/services/foundation-geometry.mjs','src/features/labs/services/convex-geometry.mjs','src/features/labs/services/diagram-labels.mjs','src/features/labs/services/svg-clipping.mjs','src/features/labs/controllers/svg-drag.js','src/app/styles/labs.css','docs/.vitepress/theme/tokens.css','scripts/qa/verify-math-ai-visuals.mjs','scripts/qa/math-ai-diagram-clarity.mjs'
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
    for(const img of document.querySelectorAll('.vp-doc img')){
      const rect=img.getBoundingClientRect()
      if(!img.complete||!img.naturalWidth)bad.push({type:'image-unloaded',source:img.getAttribute('src')})
      if(rect.width&&(rect.left < -2||rect.right>targetWidth+2))bad.push({type:'image-overflow',source:img.getAttribute('src'),width:rect.width})
    }
    for(const element of document.querySelectorAll('.vp-doc math.math-matrix')){
      const rect=element.getBoundingClientRect()
      if(rect.width&&(rect.right>targetWidth+2||rect.left < -2))bad.push({type:'matrix-overflow',text:element.textContent,width:rect.width})
    }
    if (document.querySelector('mjx-merror,[data-mml-node="merror"]')) bad.push({ type: 'math-error' })
    for(const matrix of document.querySelectorAll('math.math-matrix'))if(/NaN|undefined/.test(matrix.textContent))bad.push({type:'matrix-invalid-number',text:matrix.textContent})
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

async function interact(touch,onlyLab=null) {
  const labs = await page.$$('figure.study-lab')
  for (let i = 0; i < labs.length; i++) {
    if(onlyLab!==null&&onlyLab!==i)continue
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
    const finalScroll=await page.evaluate(()=>scrollY)
    if(Math.abs(finalScroll-initialScroll)>=2){
      const diagnostic={url:page.url(),lab:i,handle:handleIndex,initialScroll,finalScroll,box,before,after,events,viewport:await page.evaluate(()=>({height:innerHeight,visualHeight:visualViewport.height,visualTop:visualViewport.offsetTop,scale:visualViewport.scale,active:document.activeElement?.outerHTML.slice(0,250)}))}
      await writeFile(`${evidencePath}/scroll-during-drag.json`,JSON.stringify(diagnostic,null,2))
      console.log(JSON.stringify(diagnostic))
    }
    assert(Math.abs(finalScroll-initialScroll)<2,'Dragging a handle scrolled the page')
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
  minimax:[
   [0,'Miền X trong R²'],[0,'Thử t = 0.125'],[0,'Thử t = 0.25'],[0,'Đưa P tới điểm chứng Q'],[0,'Thử mức tiếp xúc'],[0,'Thử t = 1'],
   [0,'Bắt đầu lại'],[0,'Chia đôi tới độ rộng 0.01'],
   [0,'Khối X trong R³'],[0,'Lát x₃ = −1'],[0,'Lát x₃ = 1'],[0,'Lát x₃ = 0'],[0,'Thử t = 0.125'],[0,'Thử t = 0.25'],[0,'Đưa P tới điểm chứng Q'],[0,'Thử mức tiếp xúc'],[0,'Thử t = 1'],
   [0,'Bắt đầu lại'],[0,'Chia đôi tới độ rộng 0.01'],
   [1,'Bắt đầu lại'],[1,'Chia đôi bước tiếp'],[1,'Chia đôi bước tiếp'],[1,'Chia đôi bước tiếp'],[1,'Chia đôi bước tiếp'],[1,'Xem điểm tối ưu chính xác']
  ],
  elimination:[
   [0,'Phương sai (1, 2, 3)'],[0,'Trọng số tối ưu'],[0,'Ví dụ có trọng số âm'],[0,'Thêm điều kiện trọng số không âm'],[0,'Chia đều ba trọng số'],
   [0,'Cảm biến thứ ba nhiễu lớn'],[0,'Trọng số tối ưu'],[0,'Phương sai (1, 2, 3)'],
   [1,'Ví dụ x₁ + x₂ = 1'],[1,'Đưa z tới nghiệm'],[1,'Đi qua nghiệm tự do'],[1,'Pháp tuyến ngang'],[1,'Pháp tuyến dọc']
  ],
  equivalence:[
   [1,'Đầu vào R, cung trong R²'],[1,'Kéo A'],[1,'Kéo B'],[1,'Cho B trùng A'],[1,'Hai điểm đối xứng'],
   [1,'Đầu vào R², mặt trong R³'],[1,'Kéo A'],[1,'Kéo B'],[1,'Cho B trùng A'],[1,'Hai điểm đối xứng'],
   [2,'Đầu vào R, epigraph trong R²'],[2,'Đặt t sát đồ thị'],[2,'Nghiệm tối ưu'],[2,'Dưới giá trị tối ưu'],[2,'Nâng t lên 5'],
   [2,'Đầu vào R², epigraph trong R³'],[2,'Đổi góc nhìn'],[2,'Nghiệm tối ưu'],[2,'Dưới giá trị tối ưu'],[2,'Nâng t lên 5'],[2,'Đặt t sát đồ thị']
  ],
  optimality:[[0,'Đặt x vào nghiệm'],[0,'Đi một bước gradient có chiếu']],
  'ml-models':[[0,'Dữ liệu tách được, λ = 0'],[0,'Thêm ridge λ = 0.05'],[0,'Đặt (a, b) vào nghiệm'],[0,'Dữ liệu chồng lấn']],
  'known-functions':[[0,'a = −1'],[0,'a = 0'],[0,'a = 1/2'],[0,'a = 1'],[0,'a = 2'],[2,'Ma trận đơn vị'],[2,'t = 1/2'],[2,'Chạm biên PSD'],[2,'Ra ngoài miền']],
  'convex-function':[[1,'Yên ngựa vi phạm dây cung'],[1,'Cái bát lồi']],
  epigraph:[[2,'q = (0.5, 0.5)'],[2,'q = (0.1, 0.9)'],[2,'Hậu nghiệm (0.25, 0.75)'],[2,'Một xác suất bằng 0']],
  perspective:[[2,'Hai khối lượng bằng nhau'],[2,'Biến cố có xác suất 0'],[2,'Ví dụ 5/9']],
  separation:[[1,'Chỉ phân tách không ngặt'],[1,'Ngặt, khoảng cách bằng 0'],[1,'Mạnh, có dải đệm'],[2,'Tựa tại đỉnh'],[2,'Tựa giữa cạnh'],[4,'R³: Thêm đặc trưng tích'],[4,'R²: XOR chưa tách được']],
  'dual-cone':[[1,'K*: Có cả biên'],[1,'K**: Bao đóng của K'],[1,'K: Thiếu hai tia biên'],[1,'Điểm trên tia biên'],[1,'Điểm trong K'],[1,'Gốc thuộc cả ba nón']],
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
  if(name==='minimax'&&index===0){
   const text=await labs[index].$eval('.lab-readout',e=>e.innerText)
   if(label==='Thử t = 0.125')assert(text.includes('Ngay cả điểm tốt nhất trong X cũng không đạt mức.'),'The low ratio level must be infeasible')
   if(label==='Thử t = 0.25')assert(text.includes('Có điểm chứng khả thi.'),'The upper ratio trial must have a real feasible witness')
   if(label==='Thử mức tiếp xúc')assert(text.includes('Cần xét dung sai'),'Near-contact oracle must report its numeric uncertainty')
   if(label==='Thử t = 1')assert(text.includes('nửa không gian'),'The level-one limit must be handled as a halfspace')
   if(label==='Chia đôi tới độ rộng 0.01'){
    assert(text.includes('[0.234375, 0.242188]'),'The geometric bisection did not retain the verified bracket')
    assert(text.includes('sau 7 bước'),'The initial unit interval should need seven bisections')
   }
   if(label.startsWith('Miền X')||label.startsWith('Khối X')||label.startsWith('Lát x₃'))await interact(touch,index)
  }
  if(name==='elimination'){
   const readout=await labs[index].$eval('.lab-readout',e=>e.innerText)
   if(index===0&&label==='Ví dụ có trọng số âm')assert(readout.includes('−0.2000'),'The negative-weight example must preserve an explicit negative weight')
   if(index===0&&label==='Thêm điều kiện trọng số không âm')assert(readout.includes('Điểm bị giữ trong tam giác không âm.'),'The nonnegative condition must be active: '+readout)
   if(index===0&&label==='Trọng số tối ưu')assert(/Phương sai tổng hợp = (0\.545455|0\.666223)/.test(readout),'Inverse-variance weights must match the independent optimum')
   if(label==='Đưa z tới nghiệm')assert(readout.includes('f(x*) = 2.667'),'The exact normalized constraint should recover objective 8/3')
   if(label==='Đi qua nghiệm tự do')assert(readout.includes('f(x*) = 0.000'),'Passing through the unconstrained optimum must give zero loss')
   if(label.startsWith('Pháp tuyến')||label==='Ví dụ x₁ + x₂ = 1'||index===0)await interact(touch,index)
  }
  if(name==='equivalence'){
   const readout=await labs[index].$eval('.lab-readout',e=>e.innerText)
   if(index===1&&label==='Cho B trùng A')assert(readout.includes('G − M = 0.0000'),'Coincident points must close the lifting gap')
   if(index===2&&label==='Nghiệm tối ưu'){
    assert(readout.includes('P thỏa cả ba ràng buộc.'),'The epigraph optimum must be feasible')
    assert(readout.includes('0.000, 0.000, 1.750'),'The epigraph optimum has the wrong active constraints')
   }
   if(index===2&&label==='Dưới giá trị tối ưu')assert(readout.includes('Không có x khả thi'),'A level below 2.25 cannot be feasible')
   if(label.startsWith('Đầu vào')||label.startsWith('Kéo ')||label==='Cho B trùng A'){
    await interact(touch,index)
   }
  }
  await inspect(`${name}-${page.viewport().width}-${touch?'touch':'mouse'}-preset-${label}`)
  const panels=await labs[index].$$(':scope > svg,:scope > .lab-pair > svg')
  for(const [panelIndex,diagram]of panels.entries()){
    await diagram.evaluate(e=>e.scrollIntoView({block:'center',behavior:'instant'}))
    const stateName=label.replace(/[^\p{L}\p{N}-]+/gu,'-').slice(0,85)
    const theme=await page.evaluate(()=>document.documentElement.classList.contains('dark')?'dark':'light')
    await diagram.screenshot({path:`${evidencePath}/${name}-${page.viewport().width}-${theme}-preset-${stateName}-${panelIndex}.png`})
  }
  if(name==='odd-cycle'&&label==='Đưa phân hoạch thành Gram hạng 1'){
   const select=await labs[index].$('.lab-point-options select'),handle=(await labs[index].$$('.lab-handle'))[0]
   await select.evaluate(e=>{e.closest('details').open=true})
   await select.select('0')
   const before=await handle.evaluate(e=>e.getAttribute('aria-valuetext'))
   const up=await labs[index].$('.lab-point-directions button[aria-label="Dịch điểm lên trên"]')
   await clickControl(up,touch)
   assert.notEqual(await handle.evaluate(e=>e.getAttribute('aria-valuetext')),before,'Cannot adjust an individual vector when its endpoint overlaps the others')
   await select.evaluate(e=>{e.blur();e.closest('details').open=false})
   await inspect(`${name}-separate-one-coincident-vector`)
   interactions.push({url:page.url(),width:page.viewport().width,input:touch?'touch':'mouse',coincidentVectorSelector:true})
  }
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

async function exerciseFunctionChoices(name,touch){
 if(!['convex-function','epigraph','first-order','second-order','function-operations','ml-models'].includes(name))return
 const selects=await page.$$('figure.study-lab .lab-controls select')
 for(const [index,select]of selects.entries()){
  const original=await select.evaluate(e=>e.value)
  const options=await select.$$eval('option',rows=>rows.map(e=>e.value))
  for(const option of options){
   await select.select(option)
   await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))))
   assert.equal(await select.evaluate(e=>e.value),option)
   await inspect(`${name}-${page.viewport().width}-function-${index}-${option}`)
   results.push(`${name}-function-${index}-${option}`)
  }
  await select.select(original)
 }
}

try {
  for (const theme of (process.env.QA_THEMES || 'light,dark').split(',')) for (const width of (process.env.QA_WIDTHS || '360,375,1440').split(',').map(Number)) {
    const touch=process.env.QA_INPUT?process.env.QA_INPUT==='touch':width<600
    await page.setViewport({ width, height:Number(process.env.QA_HEIGHT||900),hasTouch:touch,isMobile:touch })
    for (const [name, route] of routes) {
      const response = await page.goto(base + route, { waitUntil: 'networkidle0', timeout: 120000 })
      assert.equal(response.status(), 200)
      const overview=['optimization-overview','duality-overview'].includes(name)
      await page.waitForSelector(process.env.QA_LAYOUT_ONLY||overview?'.vp-doc, vite-error-overlay':'.study-lab .lab-handle, vite-error-overlay', { timeout: 60000 })
      assert(!await page.$('vite-error-overlay'),`Preview compilation failed at ${route}; inspect qa-dev.log`)
      await page.evaluate(() => document.fonts.ready)
      await page.$$eval('.vp-doc img',images=>Promise.all(images.map(img=>{img.loading='eager';return img.decode().catch(()=>{})})))
      await page.evaluate(theme => document.documentElement.classList.toggle('dark', theme === 'dark'), theme)
      await inspect(`${name}-${width}-${theme}-initial`)
      if(!process.env.QA_LAYOUT_ONLY&&!overview){await interact(touch);if(name==='odd-cycle')await checkCycleButtons(touch);await checkPageScroll(touch);await exercisePresets(name,touch);await exerciseFunctionChoices(name,touch)}
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
      if(name==='equivalence'&&width===375){
        for(const imageName of ['slack-lift-2d','slack-lift-3d']){
          const figure=await page.$(`.vp-doc img[src$="/${imageName}.svg"]`)
          assert(figure,imageName)
          await figure.evaluate(e=>e.scrollIntoView({block:'center',behavior:'instant'}))
          await figure.screenshot({path:`${evidencePath}/${imageName}-375-${theme}.png`})
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
