import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir, writeFile } from 'node:fs/promises'
const base = process.env.QA_BASE_URL || 'http://127.0.0.1:5188'
const root = '/bieu-dien-tri-thuc/bai-giang/'
const out = 'qa/knowledge-course'
await mkdir(out, { recursive: true })
const browser = await puppeteer.launch({
  headless: true,
  executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe',
  args: ['--no-sandbox']
})
const results = [], errors = []
try {
  const p = await browser.newPage()
  p.on('pageerror', error => errors.push(error.message))
  const open = async route => { await p.goto(base + root + route + '.html', { waitUntil: 'networkidle0', timeout: 120000 }) }
  const lab = label => 'section[aria-label="' + label + '"]'
  const finish = async selector => {
    await p.waitForSelector(selector + ' .simulation-controls input[type=range]')
    await p.$eval(selector + ' .simulation-controls input[type=range]', input => {
      input.value = input.max; input.dispatchEvent(new Event('input', { bubbles: true }))
    })
  }
  const includes = async (selector, text) => {
    await p.waitForFunction((selector, text) => document.querySelector(selector)?.textContent.includes(text), {}, selector, text)
  }
  for (const width of [375,1440]) {
    await p.setViewport({ width, height: 950 })
    await open('12-hoc-tang-cuong/kham-pha-va-tong-quat')
    let selector = lab('Khám phá và khai thác hai máy')
    await p.select(selector + ' select', '0')
    await finish(selector)
    await includes(selector, '60 lượt')
    await includes(selector, '0 lượt')
    await p.select(selector + ' select', '0.3')
    await finish(selector)
    results.push({ width, example: 'epsilon zero and randomized exploration' })
    await open('13-naive-bayes/van-ban-va-lam-tron')
    selector = lab('Vết phân loại thư bằng Naive Bayes')
    await finish(selector)
    await includes(selector, '54.5%')
    await p.select(selector + ' select', '0')
    await finish(selector)
    await includes(selector, 'Không chuẩn hóa được')
    await p.select(selector + ' select', '1')
    await p.$eval(selector + ' input', input => { input.value = 'khác'; input.dispatchEvent(new Event('input',{bubbles:true})) })
    await includes(selector, 'Bỏ qua token')
    results.push({ width, example: 'Naive Bayes smoothing, zero likelihood and unknown token' })
    await open('13-naive-bayes/gaussian')
    selector = lab('Likelihood Gaussian và hậu nghiệm')
    await includes(selector, '50.0%')
    await p.select(selector + ' label:nth-child(3) select', '0.8')
    await includes(selector, '80.0%')
    results.push({ width, example: 'Gaussian likelihood and changed prior' })
    await open('14-mang-no-ron/perceptron')
    selector = lab('Vết huấn luyện Perceptron')
    await finish(selector)
    await includes(selector, '-3, 2, 1')
    await p.select(selector + ' select','XOR')
    await finish(selector)
    await includes(selector, '0, -1, 0')
    results.push({ width, example: 'AND convergence and XOR observation budget' })
    await open('14-mang-no-ron/backprop')
    selector = lab('Lan truyền thuận và ngược từng bước')
    await finish(selector)
    await p.$$eval(selector + ' button', buttons => buttons.find(button => button.textContent.includes('Cập nhật với')).click())
    await includes(selector, 'Số lần cập nhật 1')
    results.push({ width, example: 'forward, backward and parameter update' })
    await open('15-hoc-sau/cnn-va-tich-chap')
    selector = lab('Cửa sổ trượt CNN')
    await finish(selector)
    assert.deepEqual(await p.$$eval(selector + ' .output span', elements => elements.map(element => Number(element.textContent))), [1,2,3,0,0,0,0,0,0])
    await p.select(selector + ' select','pool')
    await finish(selector)
    assert.deepEqual(await p.$$eval(selector + ' .output span', elements => elements.map(element => Number(element.textContent))), [6,8,3,4])
    results.push({ width, example: 'all CNN windows and pooling outputs' })
    await open('15-hoc-sau/seq2seq-va-beam')
    selector = lab('Truy vết beam search')
    await finish(selector)
    await includes(selector, '0.180')
    await p.select(selector + ' select','2')
    await finish(selector)
    await includes(selector, 'B z EOS')
    await includes(selector, '0.400')
    results.push({ width, example: 'greedy prefix pruning and wider beam' })
    await open('15-hoc-sau/attention-va-llm')
    selector = lab('Tính attention từng bước')
    await finish(selector)
    await includes(selector, '0.5000, 1.0000')
    await p.$eval(selector + ' input[type=checkbox]', element => element.scrollIntoView({block:'center',behavior:'instant'}))
    await p.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))))
    await p.click(selector + ' input[type=checkbox]')
    assert.equal(await p.$eval(selector + ' input[type=checkbox]', element => element.checked), true)
    await finish(selector)
    await includes(selector, '1.0000, 0.0000')
    await p.$eval(selector, element => element.scrollIntoView({block:'center'}))
    await p.evaluate(() => document.documentElement.classList.add('dark'))
    await (await p.$(selector)).screenshot({ path: out + '/attention-dark-' + width + '.png' })
    await p.evaluate(() => document.documentElement.classList.remove('dark'))
    results.push({ width, example: 'attention softmax and causal mask' })
  }
  assert.deepEqual(errors, [])
  await writeFile(out + '/interactions.json', JSON.stringify({ base, results, errors },null,2))
  console.log('PASS',results.length,'interaction groups at two widths')
} finally {
  await writeFile(out + '/interactions.json', JSON.stringify({ base, results, errors },null,2))
  await browser.close()
}
