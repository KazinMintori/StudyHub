import puppeteer from 'puppeteer'
import assert from 'node:assert/strict'
import { mkdir,readFile,writeFile } from 'node:fs/promises'
import MarkdownIt from 'markdown-it'
import { courseCatalog } from '../docs/.vitepress/course-catalog.mjs'
import { concepts } from '../docs/.vitepress/concepts.mjs'
import { relatedConcepts,wikiDetails,wikiGroups } from '../docs/.vitepress/wiki-content.mjs'
import { lectureSlides,lectureConceptIds } from '../docs/.vitepress/lecture-model.mjs'
import { lectureParts } from '../docs/.vitepress/lecture-model.mjs'
import { termLinks } from '../docs/.vitepress/term-links.mjs'
import { searchTrace,gradientTrace,bayesCounts,wordCountTrace } from '../docs/.vitepress/theme/illustrations.js'

await mkdir('qa',{recursive:true})
const ids=Object.keys(concepts)
assert.equal(new Set(wikiGroups.flatMap(g=>g.ids)).size,ids.length)
for(const id of ids){assert(wikiDetails[id]);assert(relatedConcepts(id).length);for(const other of relatedConcepts(id))assert(concepts[other]&&other!==id);assert((await readFile(`docs/wiki/${id}.md`,'utf8')).includes('## Giải thích kỹ thuật'))}
for(const c of courseCatalog)for(const l of c.lessons){const source=await readFile(`docs/${c.id}/bai-giang/${l.slug}.md`,'utf8');assert(source.includes(`lecture: ${l.slug}`));assert(source.includes('section: lecture'));if(l.status==='ready')assert(lectureSlides(c,l).length)}
const md=new MarkdownIt().use(termLinks,'/Study_UET/')
const rendered=md.render('Gradient và đạo hàm riêng. `gradient` [vector](https://example.com)',{relativePath:'toan-cho-ai/bai-giang/example.md'})
assert(rendered.includes('data-wiki="/wiki/gradient.html"'));assert(rendered.includes('aria-haspopup="dialog"'));assert(rendered.includes('<code>gradient</code>'))
const wiki=md.render('Gradient dùng vector và đạo hàm riêng.',{relativePath:'wiki/gradient.md'})
assert(!wiki.includes('data-wiki="/wiki/gradient.html"'));assert(wiki.includes('data-wiki="/wiki/vector.html"'))
const mathParameter=md.render('tham số',{relativePath:'toan-cho-ai/bai-giang/example.md'})
const codeParameter=md.render('tham số',{relativePath:'xu-ly-du-lieu/bai-giang/example.md'})
assert(mathParameter.includes('data-term="tham-so-toan-hoc"'));assert(!mathParameter.includes('data-term="tham-so-lap-trinh"'))
assert(codeParameter.includes('data-term="tham-so-lap-trinh"'));assert(!codeParameter.includes('data-term="tham-so-toan-hoc"'))
const mathParameterWiki=md.render('Tham số của mô hình.',{relativePath:'wiki/tham-so-toan-hoc.md'})
assert(!mathParameterWiki.includes('data-term="tham-so-lap-trinh"'))
assert((await readFile('docs/wiki/gradient.md','utf8')).includes(String.fromCharCode(92)+'nabla'))
assert.deepEqual(searchTrace({A:['B','C'],B:['D'],C:[],D:[]},'dfs').at(-1).visited,['A','B','D','C'])
assert.equal(gradientTrace(2,.5,1)[1],0);assert(Math.abs(bayesCounts(.2,.8,.3).posterior-.4)<1e-10);assert.deepEqual(wordCountTrace('UET học uet').counts,[['uet',2],['học',1]])

const browser=await puppeteer.launch({headless:true}), page=await browser.newPage(), errors=[], results=[]
page.on('pageerror',e=>{errors.push(e.message);console.error(e.message)})
const base=process.env.QA_URL || 'http://127.0.0.1:8080'
async function go(path){const response=await page.goto(base+path,{waitUntil:'networkidle0',timeout:120000});if(response)assert([200,304].includes(response.status()),path);if(path.includes('/bai-giang/'))await page.waitForFunction(()=>document.querySelector('.lecture-tabs a[aria-current]')?.getAttribute('href').endsWith(location.hash||'#notes'))}
async function check(name,fn){await fn();results.push(name);console.log('PASS',name)}
async function part(id){await page.click(`.lecture-tabs a[href$="#${id}"]`);await page.waitForFunction(id=>location.hash===`#${id}`,{},id)}
async function button(text,root=''){await page.evaluate(({text,root})=>{const scope=root?document.querySelector(root):document;const b=[...scope.querySelectorAll('button')].find(el=>el.textContent.trim()===text);if(!b)throw Error('Missing button '+text);b.click()},{text,root})}
try{
 await page.setViewport({width:1440,height:1000});await page.emulateMediaFeatures([{name:'prefers-color-scheme',value:'light'},{name:'prefers-reduced-motion',value:'reduce'}])
 for(const course of courseCatalog){
  await check(`${course.id}: lectures keep all three parts together`,async()=>{
   await go(`/${course.id}/`);assert.equal(await page.$$eval('.lecture-list > article',els=>els.length),course.lessons.length)
   const lesson=course.lessons.find(l=>l.status==='ready'),path=`/${course.id}/bai-giang/${lesson.slug}.html`
   await go(path);await page.waitForSelector('.lecture-tabs');const title=await page.$eval('.lecture-header h1',el=>el.textContent)
   assert.equal(title,lesson.title);assert.equal(await page.$$eval('.lecture-tabs a',els=>els.length),lectureParts.length)
   await part('slides');await page.waitForSelector('.lecture-slides .course-slide');assert.equal(await page.evaluate(()=>getComputedStyle(document.querySelector('.main > .vp-doc')).display),'none')
   assert.equal(await page.$eval('.lecture-header h1',el=>el.textContent),title)
   if(lectureSlides(course,lesson).length>1){const before=await page.$eval('.course-slide h2',el=>el.textContent);await button('Tiếp →','.slide-controls');assert.notEqual(await page.$eval('.course-slide h2',el=>el.textContent),before)}
   await part('kien-thuc-can-co');await page.waitForSelector('.lecture-foundations');assert.equal(await page.$$eval('.lecture-foundations .foundation-entry',els=>els.length),lectureConceptIds(lesson).length)
   const hrefs=await page.$$eval('.lecture-foundations .foundation-content > a',els=>els.map(el=>el.getAttribute('href')));assert.equal(hrefs.length,lectureConceptIds(lesson).length);assert(hrefs.every(href=>href.includes('/wiki/')))
   await part('notes');assert.notEqual(await page.evaluate(()=>getComputedStyle(document.querySelector('.main > .vp-doc')).display),'none');assert.equal(await page.$eval('.lecture-header h1',el=>el.textContent),title)
   await page.reload({waitUntil:'networkidle0'});assert.equal(await page.$eval('.lecture-tabs a[aria-current]',el=>el.textContent),'Notes')
  })
 }
 await check('Wiki has dedicated articles and recursively linked technical explanations',async()=>{
  await go('/wiki/');assert.equal(await page.$$eval('.wiki-entry-list>a',els=>els.length),ids.length)
  await page.type('.wiki-filters input','dao ham rieng');assert(await page.$('.wiki-entry-list a[href$="/dao-ham-rieng.html"]'))
  await go('/wiki/gradient.html');assert.equal(await page.$eval('.vp-doc h1',el=>el.textContent.replaceAll(String.fromCharCode(8203),'').trim()),'Gradient');assert(await page.$('mjx-container'))
  assert.equal(await page.$('.vp-doc button.study-term[data-term="gradient"]'),null)
  const link=await page.$('.vp-doc p button.study-term[data-term="dao-ham-rieng"]');assert(link);await link.focus();await page.waitForSelector('#study-term-preview[role="tooltip"]');await page.keyboard.press('Escape');assert.equal(await page.$('#study-term-preview'),null)
  await link.click();await page.waitForSelector('#study-term-preview[role="dialog"]');assert.equal(await page.$eval('.vp-doc p button.study-term[data-term="dao-ham-rieng"]',el=>el.getAttribute('aria-expanded')),'true');assert(await page.$('#study-term-preview .term-preview-example'));await page.click('#study-term-preview .term-preview-wiki');await page.waitForFunction(()=>location.pathname.endsWith('/wiki/dao-ham-rieng.html'));assert(await page.$('.vp-doc p button.study-term'))
  assert(await page.$('.wiki-backlinks'));await page.goBack({waitUntil:'networkidle0'});assert.match(page.url(),/wiki\/gradient/);assert(await page.$('.wiki-backlinks a[href*="bai-giang"]'))
 })
 await check('Prerequisites are specific to each lecture and keep understood progress',async()=>{
  await go('/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html#kien-thuc-can-co');await page.waitForSelector('.lecture-foundations');assert(await page.$('#nen-tang-gradient'));assert(await page.$('#nen-tang-to-hop-loi'))
  assert.deepEqual(await page.$$eval('.foundation-group',els=>els.map(el=>el.querySelector('h3')?.textContent)),['Cần ôn trước','Tra cứu trong khi đọc'])
  assert(await page.$('#nen-tang-tham-so-toan-hoc'));assert.equal(await page.$('#nen-tang-tham-so-lap-trinh'),null)
  await page.click('#nen-tang-ma-tran-psd input');await page.reload({waitUntil:'networkidle0'});assert(await page.$('#nen-tang-ma-tran-psd input:checked'))
  await go('/toan-cho-ai/bai-giang/bai-02-tap-loi.html#kien-thuc-can-co');assert(await page.$('#nen-tang-tap-loi'));assert.equal(await page.$('#nen-tang-gradient'),null);assert(await page.$('#nen-tang-ma-tran-psd input:checked'))
 })
 await check('Old Notes, glossary and slides addresses resolve and keep reading progress',async()=>{
  await go('/');await page.evaluate(()=>localStorage.removeItem('studyhub_last_lesson'))
  await go('/bieu-dien-tri-thuc/notes/02-tim-kiem-mu.html');await page.waitForFunction(()=>location.pathname.includes('/bai-giang/'));await page.waitForFunction(()=>JSON.parse(localStorage.getItem('studyhub_last_lesson')||'null')?.path?.includes('/bai-giang/02-tim-kiem-mu.html'))
  await go('/toan-cho-ai/kien-thuc-can-co.html#gradient');await page.waitForFunction(()=>location.pathname==='/wiki/gradient.html')
  await go('/toan-cho-ai/slides.html#slide-3');await page.waitForFunction(slug=>location.pathname.includes(slug)&&location.hash==='#slides',{},courseCatalog.find(c=>c.id==='toan-cho-ai').slides[2].note)
 })
 await check('Notes retain math, diagrams and executable illustrations',async()=>{
  await go('/bieu-dien-tri-thuc/bai-giang/02-tim-kiem-mu.html#notes');assert(await page.$('mjx-container'));await page.waitForSelector('.mermaid svg');await button('Bước tiếp →','.code-illustration');assert.match(await page.$eval('.trace-state',el=>el.textContent),/Vừa thăm A/)
  const glossary=await page.$('.vp-doc p button.study-term');assert(glossary);await glossary.click();await page.waitForSelector('#study-term-preview[role="dialog"]');assert(await page.$('#study-term-preview .term-preview-wiki'))
 })
 await check('Search finds standalone Wiki articles and lecture parts',async()=>{
  await go('/');const search=await page.$('.DocSearch-Button');if(!search)return;await search.click();await page.waitForSelector('.VPLocalSearchBox input');await page.type('.VPLocalSearchBox input','Gradient')
  await page.waitForFunction(()=>[...document.querySelectorAll('.VPLocalSearchBox a[href]')].some(a=>a.getAttribute('href').includes('/wiki/gradient.html')),{timeout:30000});await page.keyboard.press('Escape')
 })
 for(const width of [375,768,1440]){
  await page.setViewport({width,height:1000})
  for(const path of ['/toan-cho-ai/','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html#slides','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html#notes','/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html#kien-thuc-can-co','/wiki/','/wiki/gradient.html']){
   await go(path);await check(`No overflow ${width}px ${path}`,async()=>assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)))
  }
  await go('/toan-cho-ai/');await page.screenshot({path:`qa/lecture-list-${width}.png`,fullPage:true})
 }
 await page.setViewport({width:1440,height:1000})
 for(const [partId,name]of [['slides','lecture-slides'],['notes','lecture-notes'],['kien-thuc-can-co','lecture-prerequisites']]){await go(`/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.html#${partId}`);await page.screenshot({path:`qa/${name}.png`,fullPage:false})}
 await go('/wiki/gradient.html');await page.screenshot({path:'qa/wiki-gradient.png',fullPage:true})
 assert.deepEqual(errors,[]);await writeFile('qa/course-results.json',JSON.stringify({results,errors,courses:courseCatalog.length,lectures:courseCatalog.reduce((n,c)=>n+c.lessons.length,0),wikiArticles:ids.length},null,2));console.log(`${results.length} browser checks and content/model checks passed.`)
}finally{await browser.close()}
