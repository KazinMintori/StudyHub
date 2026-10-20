import assert from 'node:assert/strict'
import { readFile, mkdir, writeFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import puppeteer from 'puppeteer'

const root = fileURLToPath(new URL('../', import.meta.url))
const base = process.env.QA_URL || 'http://127.0.0.1:5187'
const output = process.env.QA_OUTPUT || `${root}/qa/data-exam/browser`
const widths = (process.env.QA_WIDTHS || '360,1280').split(',').map(Number)
const draft = process.env.QA_DRAFT === '1'
const selectedIds = process.env.QA_IDS ? new Set(process.env.QA_IDS.split(',')) : null
await mkdir(output, { recursive: true })
const browser = await puppeteer.launch({headless:true,executablePath:process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe'})
const report = {pages:[],failures:[],errors:[]}
try {
  const page = await browser.newPage()
  page.on('pageerror', error => report.errors.push(error.message))
  await page.evaluateOnNewDocument(() => sessionStorage.setItem('studyhub_welcome_seen','1'))
  for (const width of widths) {
    await page.setViewport({width,height:900})
    for (let number=1;number<=8;number++) {
      const lesson=String(number).padStart(2,'0')
      const bank=JSON.parse(await readFile(`${root}/src/content/courses/xu-ly-du-lieu/exam/bai-${lesson}.json`,'utf8'))
      const source=JSON.parse(await readFile(`${root}/raw_materials/xu-ly-du-lieu/exam/banks/bai-${lesson}.json`,'utf8'))
      const selectedQuestions=bank.questions.filter(question=>!selectedIds||selectedIds.has(question.id))
      if(!selectedQuestions.length) continue
      const response=await page.goto(`${base}/xu-ly-du-lieu/on-thi/bai-${lesson}.html`,{waitUntil:'networkidle2',timeout:60000})
      assert(response.ok())
      await page.waitForSelector('.exam-question__id-tag')
      await page.evaluate(key=>sessionStorage.removeItem(key),`studyhub_exam_session_lesson_${lesson}`)
      await page.reload({waitUntil:'networkidle2'})
      await page.evaluate(()=>document.fonts.ready)
      for (const question of selectedQuestions) {
        const raw=source.questions.find(q=>q.id===question.id)
        await page.evaluate(q=>{
          const url=new URL(location.href)
          url.search=new URLSearchParams({mode:q.kind,cau:q.id}).toString()
          history.replaceState(null,'',url)
          dispatchEvent(new PopStateEvent('popstate'))
        },question)
        await page.waitForFunction(id=>document.querySelector('.exam-question__id-tag')?.textContent.trim()===id,{},question.id)
        assert.equal(await page.$$eval('.exam-question-card',nodes=>nodes.length),1)
        const before=await page.evaluate(q=>{
          const expected=document.createElement('div');expected.innerHTML=q.promptHtml
          return {actual:document.querySelector('.exam-question__prompt').textContent,expected:expected.textContent,
            code:[...document.querySelectorAll('.exam-question__prompt pre code')].map(code=>code.textContent.trimEnd()),
            optionCodes:[...document.querySelectorAll('.exam-choice__html')].map(node=>[...node.querySelectorAll('pre code')].map(code=>code.textContent.trimEnd())),
            revealed:document.querySelectorAll('.exam-choice__explanation').length,
            detailsOpen:document.querySelector('.exam-essay__details')?.open}
        },question)
        assert.equal(before.actual,before.expected,`${question.id}: complete prompt`)
        const literalCode = await page.evaluate(q => {
          const expected = document.createElement('div'); expected.innerHTML=q.promptHtml
          const codes = node => [...node.querySelectorAll('code')].map(n=>n.textContent)
          return {actual:codes(document.querySelector('.exam-question__prompt')),expected:codes(expected)}
        }, question)
        assert.deepEqual(literalCode.actual,literalCode.expected,`${question.id}: every inline and fenced prompt literal`)
        assert.equal((before.actual.match(/\$/g)||[]).length,(raw.promptMarkdown.match(/\$/g)||[]).length,`${question.id}: literal currency/regex dollar signs preserved`)
        const codes=[...raw.promptMarkdown.matchAll(/^```[^\r\n]*\r?\n(.*?)^```[ \t]*$/gms)].map(m=>m[1].replace(/\r\n/g,'\n').trimEnd())
        assert.deepEqual(before.code,codes,`${question.id}: code text and indentation preserved`)
        if(question.kind==='quiz') {
          const optionCodes=raw.options.map(option=>[...option.markdown.matchAll(/^```[^\r\n]*\r?\n(.*?)^```[ \t]*$/gms)].map(m=>m[1].replace(/\r\n/g,'\n').trimEnd()))
          assert.deepEqual(before.optionCodes,optionCodes,`${question.id}: all option code blocks preserved`)
          const optionLiterals=await page.evaluate(q=>{
            const codes=n=>[...n.querySelectorAll('code')].map(c=>c.textContent)
            return {actual:[...document.querySelectorAll('.exam-choice__html')].map(codes),expected:q.options.map(o=>{const n=document.createElement('div');n.innerHTML=o.html;return codes(n)})}
          },question)
          assert.deepEqual(optionLiterals.actual,optionLiterals.expected,`${question.id}: every option literal including quotes, commas and operators`)
          assert.equal(before.revealed,0,`${question.id}: no answer before choosing`)
          assert.deepEqual(await page.$$eval('.exam-choice__key-label',nodes=>nodes.map(n=>n.textContent.trim())),['A.','B.','C.','D.'])
          if(question===bank.questions[0]) await page.screenshot({path:`${output}/bai-${lesson}-${width}-quiz.png`})
          await page.$eval('.exam-choice__radio',node=>node.click())
          if(!draft) assert.equal(await page.$$eval('.exam-choice__explanation',nodes=>nodes.length),4,`${question.id}: explain all options`)
          assert.equal(await page.$$eval('.exam-choice.is-correct',nodes=>nodes.length),1)
          if(question===bank.questions[0]) await page.screenshot({path:`${output}/bai-${lesson}-${width}-feedback.png`})
          assert.equal(await page.$eval('.exam-quiz-notes__summary',node=>node.textContent.trim()),'Xem lời giải')
          assert.equal(await page.$eval('.exam-quiz-notes',node=>node.open),false)
          await page.$eval('.exam-quiz-notes',node=>{node.open=true})
          if(!draft) {
            const headings=await page.$$eval('.exam-quiz-notes__content h3',nodes=>nodes.map(n=>n.textContent.trim()).filter(text=>/^Phương án [A-D]$/.test(text)))
            assert.deepEqual(headings,['Phương án A','Phương án B','Phương án C','Phương án D'],`${question.id}: complete expanded explanations visible`)
          }
        } else {
          assert.equal(before.detailsOpen,false,`${question.id}: essay answer initially hidden`)
          await page.$eval('.exam-essay__details',node=>{node.open=true})
          assert(await page.$eval('.exam-essay__answer',node=>node.getClientRects().length>0),`${question.id}: answer opens`)
          if(question.id===bank.questions.find(q=>q.kind==='essay').id) await page.screenshot({path:`${output}/bai-${lesson}-${width}-essay.png`})
          const answerCodes=[...raw.answerMarkdown.matchAll(/^```[^\r\n]*\r?\n(.*?)^```[ \t]*$/gms)].map(m=>m[1].replace(/\r\n/g,'\n').trimEnd())
          const actualCodes=await page.$$eval('.exam-essay__answer pre code',nodes=>nodes.map(node=>node.textContent.trimEnd()))
          assert.deepEqual(actualCodes.slice(0,answerCodes.length),answerCodes,`${question.id}: full original solution code preserved`)
        }
        const layout=await page.evaluate(()=>{
          const visible=node=>Boolean(node.getClientRects().length)
          return {
            docWidth:document.documentElement.scrollWidth,viewport:innerWidth,
            mathErrors:[...document.querySelectorAll('.exam-practice mjx-merror')].filter(visible).map(n=>n.textContent),
            unexpandedHtml:document.querySelectorAll('.exam-practice [v-html], .exam-practice .static-math:empty').length,
            mathOverflow:[...document.querySelectorAll('.exam-practice mjx-container')].filter(visible).filter(n=>{const r=n.getBoundingClientRect();return r.left<0||r.right>innerWidth+1||n.scrollWidth>n.clientWidth+2}).map(n=>n.textContent.slice(0,120)),
            codeOverflow:[...document.querySelectorAll('.exam-practice pre')].filter(visible).filter(n=>{const r=n.getBoundingClientRect();return r.left<-1||r.right>innerWidth+1||!['auto','scroll'].includes(getComputedStyle(n).overflowX)&&n.scrollWidth>n.clientWidth+2}).length,
            smallCode:[...document.querySelectorAll('.exam-practice pre code')].filter(visible).filter(n=>parseFloat(getComputedStyle(n).fontSize)<14).length,
            lowercaseAfterColon:[...document.querySelectorAll('.exam-question-card p, .exam-question-card li, .exam-question-card h3, .exam-question-card th, .exam-question-card td')].filter(visible).flatMap(node=>{
              const copy=node.cloneNode(true)
              for(const code of copy.querySelectorAll('code, pre, mjx-container')) code.replaceWith('CODE')
              return [...copy.textContent.matchAll(/:\s*[“‘(]*\p{Ll}[^\s,.;]*/gu)].map(match=>match[0])
            }),
          }
        })
        const record={width,lesson,id:question.id,...layout}
        report.pages.push(record)
        if(layout.docWidth>width+1||layout.mathErrors.length||layout.mathOverflow.length||layout.unexpandedHtml||layout.codeOverflow||layout.smallCode||layout.lowercaseAfterColon.length) report.failures.push(record)
      }
      console.log(`Checked ${selectedQuestions.length} questions in lesson ${lesson} at ${width}px`)
    }
  }
} finally {
  await browser.close()
  await writeFile(`${output}/report.json`,JSON.stringify(report,null,2)+'\n')
}
assert.equal(report.failures.length,0,`${report.failures.length} question render failures; see report.json`)
assert.equal(report.errors.length,0,report.errors.join('\n'))
console.log(`PASS ${report.pages.length} question/viewport checks.`)
