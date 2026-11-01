import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { readFile, mkdir, writeFile } from 'node:fs/promises'
import { normalizeFillAnswer } from '../../src/features/philosophy/services/fill-session.mjs'
const base=process.env.QA_BASE_URL || 'http://127.0.0.1:5174'
const browser=await puppeteer.launch({headless:true,executablePath:process.env.PUPPETEER_EXECUTABLE_PATH||undefined,args:process.env.GITHUB_ACTIONS==='true'?['--no-sandbox']:[]})
const page=await browser.newPage(),errors=[]
page.on('pageerror',error=>errors.push(error.message))
await page.evaluateOnNewDocument(()=>sessionStorage.setItem('studyhub_welcome_seen','1'))
await mkdir('qa/philosophy-formats',{recursive:true})
async function open(path,selector) {
 const response=await page.goto(base+path,{waitUntil:'domcontentloaded',timeout:90000})
 assert.equal(response.status(),200,path)
 await page.waitForSelector(selector,{timeout:90000})
}
async function clickButton(text) {
 for(const button of await page.$$('button'))if((await button.evaluate(el=>el.textContent.trim()))===text)return button.click()
 throw Error(`Missing button ${text}`)
}
try {
 for(const width of [1440,375,360]) {
  await page.setViewport({width,height:1000})
  await open('/triet-hoc-mac-lenin/on-thi/','.exam-bank')
  await page.evaluate(()=>{localStorage.clear();sessionStorage.setItem('studyhub_welcome_seen','1')})
  assert.equal(await page.$$eval('.exam-bank-actions a',els=>els.length),6)
  for(const chapter of [1,2,3]) {
   const bank=JSON.parse(await readFile(`src/content/courses/triet-hoc-mac-lenin/exam/fill/chuong-${chapter}.json`,'utf8'))
   await open(`/triet-hoc-mac-lenin/on-thi/chuong-${chapter}/dien-tu.html`,'.fill-input')
   assert.equal(await page.$$eval('h1',els=>els.length),1)
   await clickButton('Trả lời')
   await page.waitForSelector('.fill-validation')
   assert.equal(await page.$('.fill-result'),null)
   for(const input of await page.$$('.fill-input'))await input.type('sai')
   await clickButton('Trả lời');await page.waitForSelector('.fill-result.is-wrong')
   await clickButton('Thử lại')
   const inputs=await page.$$('.fill-input')
   for(const [index,input] of inputs.entries())await input.type(normalizeFillAnswer(bank.questions[0].blanks[index].answer))
   await page.keyboard.press('Enter');await page.waitForSelector('.fill-result.is-correct')
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`Fill ${chapter} overflow ${width}`)
   await page.reload({waitUntil:'domcontentloaded'});await page.waitForSelector('.fill-result.is-correct')
   if(chapter===2)await page.screenshot({path:`qa/philosophy-formats/fill-${width}.png`,fullPage:true})
   await clickButton('Tiếp theo');await page.waitForFunction(()=>document.querySelector('.fill-question-heading')?.textContent.includes('2'))
  }
  await open('/triet-hoc-mac-lenin/on-thi/de-thi/','.papers-grid')
  assert.equal(await page.$$eval('.papers-grid li',els=>els.length),21)
  assert((await page.$$eval('.paper-reference',els=>els.length))>=10)
  await page.select('select','Đại học Bách khoa Hà Nội (HUST)')
  assert.equal(await page.$$eval('.paper-reference',els=>els.length),3)
  await page.select('select','')
  if(width===1440)await page.screenshot({path:'qa/philosophy-formats/papers.png'})
  const bank=JSON.parse(await readFile('src/content/courses/triet-hoc-mac-lenin/exam/papers/tong-hop-01.json','utf8'))
  await open('/triet-hoc-mac-lenin/on-thi/de-thi/tong-hop-01.html','.paper-option input')
  await page.click(`.paper-option input[value="${bank.questions[0].correctKey}"]`)
  assert.equal(await page.$('.exam-choice__explanation'),null)
  assert.equal(await page.$('.paper-result'),null)
  await clickButton('Tiếp theo →');await page.waitForFunction(()=>document.querySelector('.paper-question h2')?.textContent.includes('2 /'))
  await page.reload({waitUntil:'domcontentloaded'});await page.waitForFunction(()=>document.querySelector('.paper-question h2')?.textContent.includes('2 /'))
  await clickButton('Nộp bài');await page.waitForSelector('.paper-confirm')
  assert((await page.$eval('.paper-confirm',el=>el.textContent)).includes('59'))
  await clickButton('Xác nhận nộp bài');await page.waitForSelector('.paper-result')
  assert((await page.$eval('.paper-score',el=>el.textContent)).includes('0.17'))
  await clickButton('Xem bài làm và lời giải');await page.waitForSelector('.exam-choice.is-correct')
  assert.equal(await page.$$eval('.exam-choice__user-badge',els=>els.length),0,'Unanswered questions must not gain a fabricated selection')
  assert.equal(await page.$$eval('.exam-choice__explanation',els=>els.length),4)
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`Paper review overflow ${width}`)
  await page.screenshot({path:`qa/philosophy-formats/paper-review-${width}.png`})
  console.log(`PASS ${width}px: Three chapter fill banks, exact grading/retry/reload, paper catalog and source filter, submit/review with unanswered items`)
 }
 assert.deepEqual(errors,[])
}catch(error){
 await writeFile('qa/philosophy-formats/failure.json',JSON.stringify({message:error.message,errors,url:page.url(),page:await page.$eval('body',el=>el.textContent.slice(0,2500)).catch(()=>null)},null,2))
 await page.screenshot({path:'qa/philosophy-formats/failure.png'}).catch(()=>{})
 throw error
}finally{await browser.close()}
