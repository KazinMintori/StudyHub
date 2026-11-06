import assert from 'node:assert/strict'
import {readFile,mkdir,writeFile} from 'node:fs/promises'
import puppeteer from 'puppeteer'

const base=process.env.QA_URL||'http://127.0.0.1:5173'
const output='qa/data-exam-additions'
await mkdir(output,{recursive:true})
const browser=await puppeteer.launch({headless:true,
  executablePath:process.env.PUPPETEER_EXECUTABLE_PATH||process.env.CHROME_PATH||'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const report={pages:[],failures:[],errors:[]}
try {
  const page=await browser.newPage()
  page.on('pageerror',e=>report.errors.push(e.message))
  await page.evaluateOnNewDocument(()=>sessionStorage.setItem('studyhub_welcome_seen','1'))
  for(const width of [360,1280]) {
    await page.setViewport({width,height:940})
    for(const lesson of ['10','11']) {
      const bank=JSON.parse(await readFile(`src/content/courses/xu-ly-du-lieu/exam/bai-${lesson}.json`,'utf8'))
      const raw=JSON.parse(await readFile(`raw_materials/xu-ly-du-lieu/exam/banks/bai-${lesson}.json`,'utf8'))
      await page.goto(`${base}/xu-ly-du-lieu/on-thi/bai-${lesson}.html`,{waitUntil:'networkidle2',timeout:120000})
      await page.waitForSelector('.exam-question__id-tag')
      await page.evaluate(dark=>{
        sessionStorage.clear()
        sessionStorage.setItem('studyhub_welcome_seen','1')
        document.documentElement.classList.toggle('dark',dark)
      },width===360)
      await page.reload({waitUntil:'networkidle2'})
      await page.evaluate(dark=>document.documentElement.classList.toggle('dark',dark),width===360)
      for(const q of bank.questions) {
        await page.evaluate(q=>{
          const url=new URL(location.href)
          url.search=new URLSearchParams({mode:q.kind,cau:q.id}).toString()
          history.replaceState(null,'',url)
          dispatchEvent(new PopStateEvent('popstate'))
        },q)
        await page.waitForFunction(id=>document.querySelector('.exam-question__id-tag')?.textContent.trim()===id,{},q.id)
        assert.equal(await page.$$eval('.exam-question-card',nodes=>nodes.length),1,q.id)
        if(q.kind==='quiz') {
          assert.deepEqual(await page.$$eval('.exam-choice__key-label',nodes=>nodes.map(n=>n.textContent.trim())),['A.','B.','C.','D.'])
          assert.equal(await page.$$eval('.exam-choice__explanation',nodes=>nodes.length),0,q.id)
          await page.$eval('.exam-choice__radio',node=>node.click())
          await page.waitForFunction(()=>document.querySelectorAll('.exam-choice__explanation').length===4)
          assert.equal(await page.$$eval('.exam-choice.is-correct',nodes=>nodes.length),1,q.id)
          assert.equal(await page.$eval('.exam-quiz-notes__summary',n=>n.textContent.trim()),'Xem lời giải')
          await page.$eval('.exam-quiz-notes',n=>{n.open=true})
          assert.deepEqual(await page.$$eval('.exam-quiz-notes__content h3',nodes=>nodes.map(n=>n.textContent.trim()).filter(t=>/^Phương án [A-D]$/.test(t))),['Phương án A','Phương án B','Phương án C','Phương án D'])
        } else {
          assert.equal(await page.$eval('.exam-essay__details',n=>n.open),false,q.id)
          await page.$eval('.exam-essay__details',n=>{n.open=true})
        }
        const original=raw.questions.find(item=>item.id===q.id)
        const result=await page.evaluate(({q,source})=>{
          const expected=document.createElement('div');expected.innerHTML=q.promptHtml
          const answer=document.createElement('div');answer.innerHTML=q.answerHtml
          const prompt=document.querySelector('.exam-question__prompt')
          const actualAnswer=document.querySelector(q.kind==='quiz'?'.exam-quiz-notes__content':'.exam-essay__answer')
          const code=node=>[...node.querySelectorAll('code')].map(n=>n.textContent)
          const visible=node=>Boolean(node.getClientRects().length)
          const plain=prompt.textContent.replace(/\s+/g,'')
          const missingBraceData=[...source.matchAll(/\{[^{}\n]*\}/g)]
            .map(match=>match[0]).filter(literal=>!plain.includes(literal.replace(/\s+/g,'')))
          return {promptMatches:prompt.textContent===expected.textContent,
            missingBraceData,
            promptCodeMatches:JSON.stringify(code(prompt))===JSON.stringify(code(expected)),
            answerCodeMatches:JSON.stringify(code(actualAnswer))===JSON.stringify(code(answer)),
            documentOverflow:document.documentElement.scrollWidth>innerWidth+2,
            mathErrors:[...document.querySelectorAll('.exam-practice mjx-merror,[data-mjx-error]')].filter(visible).length,
            badTables:[...document.querySelectorAll('.exam-practice table')].filter(visible).filter(t=>{
              const cols=t.querySelectorAll('thead th').length
              return !cols||[...t.querySelectorAll('tbody tr')].some(r=>r.children.length!==cols)
            }).length,
            mathOverflow:[...document.querySelectorAll('.exam-practice mjx-container')].filter(visible).filter(n=>{
              const b=n.getBoundingClientRect();return b.left<-1||b.right>innerWidth+1||n.scrollWidth>n.clientWidth+2
            }).length,
            brokenText:/\ufffd|\^M/.test(prompt.textContent+actualAnswer.textContent)}
        },{q,source:original.promptMarkdown})
        const row={width,lesson,id:q.id,...result};report.pages.push(row)
        if(!result.promptMatches||!result.promptCodeMatches||!result.answerCodeMatches||result.missingBraceData.length||result.documentOverflow||result.mathErrors||result.badTables||result.mathOverflow||result.brokenText)report.failures.push(row)
        if(['TN-001','TN-003','TN-004','TL-002'].some(id=>q.id.endsWith(id))) {
          const target=await page.$('.exam-question__prompt')
          await target.screenshot({path:`${output}/${q.id}-${width}.png`})
        }
      }
      console.log(`Checked ${bank.questions.length} new questions, lesson ${lesson}, ${width}px`)
    }
  }
} finally {
  await writeFile(`${output}/report.json`,JSON.stringify(report,null,2)+'\n')
  await browser.close()
}
assert.equal(report.errors.length,0,JSON.stringify(report.errors))
assert.equal(report.failures.length,0,JSON.stringify(report.failures.slice(0,12),null,2))
console.log(`PASS ${report.pages.length} new-question browser cases`)
