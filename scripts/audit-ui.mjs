import puppeteer from 'puppeteer'
import { mkdir, writeFile, readdir, readFile } from 'node:fs/promises'
import assert from 'node:assert/strict'
const base = process.env.QA_URL || 'http://127.0.0.1:5181'
const output = 'qa/redesign'
await mkdir(output, { recursive: true })
const paths = ['/', '/toan-cho-ai/', '/bieu-dien-tri-thuc/', '/wiki/', '/wiki/gradient.html', '/guide/', '/goc-hoc-tap#flashcards', '/goc-hoc-tap#notes', '/toan-cho-ai/bai-giang/bai-02-tap-loi.html', '/giai-thuat-du-lieu/bai-giang/bai-03-pagerank-mo-hinh-va-tinh-toan.html', '/toan-cho-ai/bai-tap.html', '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html#kien-thuc-can-co']
const browser = await puppeteer.launch({ headless: true }), page = await browser.newPage()
const errors = [], results = []
page.on('pageerror', error => errors.push(error.message))
page.on('response', response => { if (response.status()>=400 && /\.(css|js|woff2?)(?:\?|$)/.test(response.url())) errors.push(`Failed asset ${response.status()}: ${response.url()}`) })
try {
  for (const width of [1440, 390]) for (const mode of ['light', 'dark']) {
    await page.setViewport({ width, height: 900 })
    await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: mode }, { name: 'prefers-reduced-motion', value: 'reduce' }])
    await page.evaluateOnNewDocument(mode => localStorage.setItem('vitepress-theme-appearance', mode), mode)
    for (let i = 0; i < paths.length; i++) {
      const path = paths[i]
      await page.goto(base + path, { waitUntil: 'networkidle0', timeout: 120000 })
      await page.evaluate(() => document.fonts.ready)
      assert(await page.evaluate(() => getComputedStyle(document.body).fontFamily.includes('Be Vietnam Pro')), 'Styles did not load')
      const metrics = await page.evaluate(() => {
        const skip = 'svg, mjx-container, pre, code, .header-anchor, .VPNavScreen, .visually-hidden, .VPSkipLink'
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT)
        const sizes = new Set(), small = [], contrast = [], families = new Set()
        let node, chars = 0, smallChars = 0
        const rgba = color => color.match(/[\d.]+/g)?.map(Number) || [0,0,0,0]
        const composite = (a, b) => { const alpha = a[3] ?? 1; return [0,1,2].map(i => a[i]*alpha+b[i]*(1-alpha)).concat(1) }
        function background(el) {
          if (!el) return document.documentElement.classList.contains('dark') ? [23,22,29,1] : [255,255,255,1]
          const color = rgba(getComputedStyle(el).backgroundColor)
          return color[3] === 1 || color.length === 3 ? color : composite(color, background(el.parentElement))
        }
        const luminance = color => color.slice(0,3).map(v => { v/=255; return v<=.04045?v/12.92:((v+.055)/1.055)**2.4 }).reduce((n,v,i)=>n+v*[.2126,.7152,.0722][i],0)
        while (node = walker.nextNode()) {
          const text = node.textContent.trim(), el = node.parentElement
          if (!text || el.closest(skip) || !el.checkVisibility({ checkOpacity: true, checkVisibilityCSS: true })) continue
          const style = getComputedStyle(el), size = parseFloat(style.fontSize)
          chars += text.length; sizes.add(Math.round(size*100)/100); families.add(style.fontFamily.split(',')[0])
          if (size < 14) smallChars += text.length
          if (size < 13) small.push({ text: text.slice(0,80), size })
          const bg=background(el), fg=composite(rgba(style.color),bg), l1=luminance(fg), l2=luminance(bg)
          const ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05)
          if (ratio < (size>=24 || (size>=18.66 && parseFloat(style.fontWeight)>=700) ? 3 : 4.5) - .05) contrast.push({ text:text.slice(0,80), ratio:Math.round(ratio*100)/100, color:style.color, background:bg })
        }
        const paragraphs=[...document.querySelectorAll('.main > .vp-doc > div > p')].filter(p=>p.textContent.length>160)
        const p=paragraphs[0], content=document.querySelector('.main > .vp-doc > div > :first-child')
        let lineChars = null
        if (p) {
          const walker=document.createTreeWalker(p,NodeFilter.SHOW_TEXT), lines=new Map()
          let n
          while(n=walker.nextNode()) { if(n.parentElement.closest('mjx-container,code'))continue;for(let i=0;i<n.length;i++) { const range=document.createRange(); range.setStart(n,i);range.setEnd(n,i+1);const rect=range.getBoundingClientRect();if(rect.height){ const y=Math.round(rect.top); lines.set(y,(lines.get(y)||0)+1) } } }
          const values=[...lines.values()]; if(values.length>1)lineChars=Math.round(values.slice(0,-1).reduce((n,v)=>n+v,0)/(values.length-1))
        }
        const fonts=[...document.fonts].filter(font=>font.status==='loaded').map(font=>font.family)
        return { overflow:document.documentElement.scrollWidth>innerWidth, scrollWidth:document.documentElement.scrollWidth, smallRatio:Math.round(smallChars/Math.max(chars,1)*1000)/10, below13:small, sizes:[...sizes].sort((a,b)=>a-b), lowContrast:contrast, fonts:[...new Set(fonts)], families:[...families], lineChars, readingWidth:p?.getBoundingClientRect().width, contentTop:content?.getBoundingClientRect().top, slideControlsBottom:document.querySelector('.slide-controls')?.getBoundingClientRect().bottom }
      })
      results.push({ path, width, mode, ...metrics })
      await page.screenshot({ path: `${output}/${i}-${width}-${mode}.png`, fullPage: false })
      console.log(`${width} ${mode} ${path}: overflow=${metrics.overflow} small=${metrics.smallRatio}% sizes=${metrics.sizes.length} contrast=${metrics.lowContrast.length} content=${metrics.contentTop?.toFixed(0)}`)
    }
  }
  await writeFile(`${output}/audit.json`, JSON.stringify({ results, errors }, null, 2))
  assert.deepEqual(errors, [], 'Browser errors')
  assert(results.every(r=>!r.overflow), 'Horizontal overflow; inspect qa/redesign/audit.json')
  assert(results.every(r=>r.below13.length===0 && r.smallRatio<=10), 'Small text; inspect audit.json')
  assert(results.every(r=>r.lowContrast.length===0), 'Low text contrast; inspect audit.json')
  assert(results.every(r=>r.sizes.length<=7), 'Too many font sizes; inspect audit.json')
  assert(results.filter(r=>r.width===390 && r.path.includes('/bai-giang/') && !r.path.includes('#')).every(r=>r.contentTop<=260), 'Mobile content begins too low')
  assert.deepEqual([...new Set(results.flatMap(r=>r.fonts))].sort(), ['Be Vietnam Pro','JetBrains Mono Variable','Source Serif 4 Variable'].sort(), 'Unexpected or unused font families')
  console.log(`PASS ${results.length} page/theme/viewport combinations`)
} finally { await browser.close() }
