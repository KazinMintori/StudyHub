import assert from 'node:assert/strict'
import {readFile} from 'node:fs/promises'
import {probabilitySourceLibrary as entries} from '../docs/.vitepress/probability-source-library.mjs'

const root='docs/public/materials/xac-suat-thong-ke/embedded'
const coverage=JSON.parse(await readFile(`${root}/coverage.json`,'utf8'))
assert.equal(entries.filter(entry=>entry.notes).length,31)
assert.equal(entries.filter(entry=>entry.slides).length,28)
assert.equal(coverage.length,59)
assert.equal(new Set(entries.map(entry=>entry.id)).size,entries.length)
for(const entry of entries) {
 for(const kind of ['notes','slides']) {
  if(!entry[kind])continue
  const item=coverage.find(row=>row.id===entry.id&&row.kind===kind)
  assert(item,entry.id+' '+kind)
  assert.equal(item.source,entry[kind])
  const html=await readFile(`${root}/${item.file}`,'utf8')
  assert(html.includes(`<base href="${entry[kind]}">`))
  assert(html.includes('studyhub-source-navigation'))
  assert(html.includes('creativecommons.org/licenses/by/4.0/'))
  assert(!html.includes('googletagmanager.com'))
  assert(!/src="[^"]*stat20notes-[^/]+\/stat20notes\.js"/.test(html))
  if(kind==='notes') {
   const main=html.match(/<main\b[^>]*>[\s\S]*?<\/main>/i)?.[0]
   assert(main,entry.id)
   assert.equal((main.match(/<p\b/gi)||[]).length,item.paragraphs+1,entry.id)
  } else {
   assert.equal((html.match(/<section\b/gi)||[]).length,item.slideSections+1,entry.id)
  }
 }
}
const component=await readFile('docs/.vitepress/theme/ProbabilitySourceReader.vue','utf8')
assert(component.includes('withBase('))
const sandbox=component.match(/sandbox="([^"]+)"/)[1]
assert(sandbox.includes('allow-scripts')&&!sandbox.includes('allow-same-origin'))
console.log('PASS 31 complete Notes and 28 complete slide decks; coverage, paragraphs, slide sections, attribution and sandbox verified.')
