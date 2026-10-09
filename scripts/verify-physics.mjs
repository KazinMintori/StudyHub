// Verify honest translation progress and structural integrity, not semantic completeness.
import assert from 'node:assert/strict'
import { readFile, access } from 'node:fs/promises'
import path from 'node:path'
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import { physics1Course, physics2Course } from '../docs/.vitepress/physics-courses.mjs'
const manifest=JSON.parse(await readFile('raw_materials/physics/translation-manifest.json','utf8'))
const md=new MarkdownIt({html:true}).use(mathjax)
const root=process.cwd()
async function expand(file) {
  let text=(await readFile(file,'utf8')).replace(/\r\n/g,'\n')
  for(const match of [...text.matchAll(/<!--@include:\s*([^>]+?)\s*-->/g)]) {
    const target=path.resolve(path.dirname(file),match[1])
    assert(target.startsWith(root+path.sep),'Include outside repository')
    text=text.replace(match[0],await expand(target))
  }
  return text
}
let translated=0,complete=0,images=0
assert.equal(manifest.chapters.length,44)
assert.equal(manifest.chapters.at(-1).printedEnd,1524)
for(const [course,count,start] of [[physics1Course,20,1],[physics2Course,24,21]]) {
  assert.equal(course.contentPolicy,'full-source-translation')
  assert.equal(course.lessons.length,count)
  assert.deepEqual(course.lessons.map(l=>l.sourceChapter),Array.from({length:count},(_,i)=>start+i))
  assert.deepEqual(course.parts.flatMap(p=>p.lessons),course.lessons.map(l=>l.slug))
  for(const lesson of course.lessons) {
    const chapter=manifest.chapters.find(c=>c.chapter===lesson.sourceChapter)
    const file=path.resolve('docs',course.id,'bai-giang',lesson.slug+'.md')
    const raw=await readFile(file,'utf8'),source=await expand(file)
    if(chapter.pendingSourceUnits.length) {
      assert.equal(lesson.status,'draft','Incomplete source presented as ready')
      assert(raw.includes('lessonStatus: draft'))
      assert.equal(course.slides.filter(s=>s.note===lesson.slug).length,0,'Old summaries remain in Slides')
    } else if(chapter.status==='complete')complete++
    assert(!/Ví dụ dưới đây do người soạn đặt|Các bài tập dưới đây do người soạn đặt/.test(source))
    assert(!/@\{\w+\}/.test(source))
    const html=md.render(source.replace(/^---[\s\S]*?---/,''))
    assert(!/data-mjx-error|<merror/.test(html),`Invalid math in ${file}`)
    for(const match of source.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)) {
      await access(path.resolve(path.dirname(file),match[1]));images++
    }
    translated+=chapter.fragments.length
  }
}
const first=await expand(path.resolve('docs/vat-ly-1/bai-giang/01-don-vi-vector.md'))
for(let n=1;n<=25;n++)assert(first.includes(`\\tag{1.${n}}`),`Missing source equation 1.${n}`)
for(let n=1;n<=11;n++)assert(first.includes(`### Ví dụ 1.${n} —`),`Missing original Example 1.${n}`)
for(let n=1;n<=26;n++)assert(first.includes(`::: exercise Q1.${n}\n`),`Missing discussion Q1.${n}`)
for(let n=1;n<=94;n++)assert(new RegExp(`::: exercise 1\\.${n}(?: |\\n)`).test(first),`Missing original Exercise/Problem 1.${n}`)
const second=await expand(path.resolve('docs/vat-ly-1/bai-giang/02-chuyen-dong-thang.md'))
for(let n=1;n<=18;n++)assert(second.includes(`\\tag{2.${n}}`),`Missing source equation 2.${n}`)
for(let n=1;n<=9;n++)assert(second.includes(`### Ví dụ 2.${n} —`),`Missing original Example 2.${n}`)
for(let n=1;n<=22;n++)assert(second.includes(`::: exercise Q2.${n}\n`),`Missing discussion Q2.${n}`)
for(let n=1;n<=92;n++)assert(new RegExp(`::: exercise 2\\.${n}(?: |\\n)`).test(second),`Missing original Exercise/Problem 2.${n}`)
for(const section of [5,7,8])for(let n=1;n<=4;n++)assert(second.includes(`::: exercise VP2.${section}.${n}\n`))
assert.equal(physics1Course.lessons.find(l=>l.sourceChapter===2).status,'ready')
assert.equal(physics1Course.slides.filter(s=>s.note==='02-chuyen-dong-thang').length,6)
console.log(`Verified ${translated} translated fragments, 44 chapter routes, ${images} image references and accurate draft status.`)
console.log(`Complete chapters: ${complete}. End-of-chapter exercises and other pending source units are not certified complete.`)
