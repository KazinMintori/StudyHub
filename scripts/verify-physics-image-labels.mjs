import {readFile,readdir,access,writeFile} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {physicsImageLabels} from '../docs/.vitepress/physics-image-labels.mjs'
import path from 'node:path'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {readMarkdownIncludes} from './read-markdown-includes.mjs'
const source=JSON.parse(await readFile('qa/physics/image-labels-source.json','utf8'))
const ignored={'young-21/hinh-21-2':'Process steps described directly in caption without English callout list.',
 'young-21/hinh-21-22':'Adjacent body text clipped into the source crop, not an image label.',
 'young-21/hinh-21-23':'Mathematical component names, explained with the formula in Notes.',
 'young-21/hinh-21-31':'Mathematical distance annotation.',
 'young-21/hinh-p21-96':'Stray prose from the following problem.',
 'young-21/tom-tat-chong-chat':'Mathematical component names.',
 'young-21/tom-tat-luong-cuc':'Mathematical distance annotation.'}
let pairs=0
for(const [key,labels] of Object.entries(physicsImageLabels)){
 const chapter=key.match(/young-(\d+)/)[1]
 await access(`docs/vat-ly-2/bai-giang/img/${key}.png`)
 const sources=await readdir(`raw_materials/physics/translations/chapter-${chapter}`)
 const text=(await Promise.all(sources.filter(f=>f.endsWith('.md')).map(f=>readFile(`raw_materials/physics/translations/chapter-${chapter}/${f}`,'utf8')))).join('\n')
 assert(text.includes(key),`Unused image annotation: ${key}`)
 const seen=new Set()
 for(const [vi,en] of labels){
  assert(vi.length&&en.length,key)
  assert(/^[A-ZÀ-ỸĐ]/u.test(vi.replace(/^\((?:[a-z]|\d+)\)\s*/,'')),`${key}: Caption starts uppercase`)
  const normalized=en.toLowerCase().replace(/\s+/g,' ').trim()
  assert(!seen.has(normalized),`${key}: Duplicate label ${en}`)
  seen.add(normalized);pairs++
 }
}
const unannotated=Object.entries(source).filter(([key,item])=>item.text&&!physicsImageLabels[key]&&!ignored[key]).map(([key])=>key)
assert.deepEqual(unannotated,[])
await writeFile('qa/physics/image-label-review.json',JSON.stringify({status:'passed',annotatedImages:Object.keys(physicsImageLabels).length,distinctLabelsPerImage:pairs,unannotated,ignored},null,2)+'\n')
console.log('Verified',Object.keys(physicsImageLabels).length,'caption glossaries;',pairs,'labels, each explained once per image.')
// VitePress resolves included Markdown's images from the destination page.
// Check that location explicitly, including nested topic pages.
let references=0
for(const lesson of physics2Course.lessons.filter(l=>l.status==='ready')){
 const base=`docs/vat-ly-2/bai-giang/${lesson.slug}`
 const files=[base+'.md',...(lesson.topicGroups||[]).flatMap(g=>g.topics).map(t=>`${base}/${t.slug}.md`)]
 for(const file of files){
  const source=await readMarkdownIncludes(file)
  for(const match of source.matchAll(/!\[[^\]]*\]\(([^)]+young-\d+\/[^)]+)\)/g)){
   await access(path.resolve(path.dirname(file),match[1]))
   references++
  }
 }
}
console.log('Verified',references,'figure paths from their final lecture and topic locations.')
