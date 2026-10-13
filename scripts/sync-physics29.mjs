import {readFile,writeFile,mkdir} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {parseAst} from 'rollup/parseAst'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {inductionTopics,inductionSlides} from '../docs/.vitepress/physics-induction-course.mjs'
import {inductionConcepts,inductionWikiDetails,inductionWikiConnections} from '../docs/.vitepress/physics-induction-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const numeric=JSON.parse(await readFile('qa/physics/chapter29/numeric-checks.json','utf8'))
assert.equal(numeric.status,'passed');assert.equal(numeric.detailedSolutions,108)
const review=JSON.parse(await readFile('raw_materials/physics/chapter-29-review.json','utf8'))
const raw='raw_materials/physics/translations/chapter-29',dir='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(l=>l.sourceChapter===29)),slug=lesson.slug
lesson.status=review.status==='content-complete'?'ready':'draft'
lesson.prerequisites=['vector','tich-vo-huong','tich-co-huong','dao-ham','tich-phan','dien-truong-bao-toan','suat-dien-dong','luc-tu-tren-dien-tich','momen-tu','dien-dung','ong-day-dien','dinh-luat-ampere']
lesson.supportingConcepts=['tu-thong',...Object.keys(inductionConcepts).filter(id=>!lesson.prerequisites.includes(id))]
lesson.topicGroups=inductionTopics;lesson.hasChapterExercises=true
// Replace only the chapter29 object and its slide records. Other course entries
// retain their source text, including concurrent formatting edits.
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const node=ast.body.find(n=>n.declaration?.declarations?.some(d=>d.id.name==='physics2Course')).declaration.declarations.find(d=>d.id.name==='physics2Course').init
const props=Object.fromEntries(node.properties.map(p=>[p.key.name??p.key.value,p.value]))
const target=props.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===29))
const slides=[...physics2Course.slides.filter(s=>s.note!==slug),...inductionSlides]
for(const edit of [{start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)},{start:props.slides.start,end:props.slides.end,text:JSON.stringify(slides,null,2)}].sort((a,b)=>b.start-a.start))source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
await writeFile(catalog,source)
const pages=[['thi-nghiem-cam-ung','01-hien-tuong-cam-ung.md','29.1',954,955],['dinh-luat-faraday','02-dinh-luat-faraday.md','29.2',955,962],['dinh-luat-lenz','03-dinh-luat-lenz.md','29.3',962,964],['suat-dien-dong-chuyen-dong','04-suat-dien-dong-chuyen-dong.md','29.4',965,967],['dien-truong-cam-ung','05-dien-truong-cam-ung.md','29.5',967,969],['dong-dien-foucault','06-dong-dien-foucault.md','29.6',969,970],['dong-dien-dich-maxwell','07-dong-dien-dich-maxwell.md','29.7',970,974],['sieu-dan','08-sieu-dan.md','29.8',975,976]]
await mkdir(`${dir}/${slug}`,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=inductionTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(t.title)}\ndescription: ${JSON.stringify(t.question)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${section}, trang ${start}–${end}.\n`)
}
const exercises=['10-luyen-tap-huong-dan.md','11-cau-hoi-thao-luan.md','12-bai-tap-01-30.md','13-bai-tap-31-60.md','14-bai-tong-hop-61-66.md','15-nang-cao-mcat.md','16-dap-so.md']
const include=file=>`<!--@include: ../../../${raw}/${file}-->\n\n`
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: ${JSON.stringify(lesson.title)}\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ${lesson.status}\nhasChapterExercises: true\ndescription: "Cảm ứng điện từ, Faraday, Lenz, suất điện động chuyển động, điện trường cảm ứng, dòng Fu-cô, Maxwell và siêu dẫn."\n---\n\n<div class="lecture-notes-content">\n\n${include('00-mo-dau.md')}<TopicMap />\n\n${include('09-tom-tat.md')}## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 29, trang 953–987.\n\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Cảm ứng điện từ">\n\n${exercises.map(include).join('')}## Tài liệu tham khảo\n\nYoung & Freedman, ấn bản 15, chương 29, trang 978–987 và phụ lục đáp số A-18.\n\n</div>\n`)
for(const [id,c]of Object.entries(inductionConcepts)){
 const full=inductionWikiDetails[id],reference=full.slice(full.indexOf('\n\nTài liệu tham khảo:')).replace(/^\n\nTài liệu tham khảo:\s*/,'')
 const detail=full.replace(/\n\nTài liệu tham khảo:[\s\S]*$/,'')
 const related=inductionWikiConnections[id].map(key=>{assert(concepts[key],key);return `- [${concepts[key].name}](./${key}.md)`}).join('\n')
 await writeFile(`docs/wiki/${id}.md`,`---\ntitle: ${JSON.stringify(c.name)}\nwikiTerm: ${id}\nprev: false\nnext: false\n---\n\n# ${c.name}\n\n${c.definition}\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n${detail}\n\n## Ví dụ\n\n${c.example}\n\n## Khi nào cần dùng?\n\n${c.use}\n\n## Câu hỏi ôn lại\n\n${c.question}\n\n<details><summary>Xem đáp án</summary>\n\n${c.answer}\n\n</details>\n\n## Thuật ngữ liên quan\n\n${related}\n\n## Tài liệu tham khảo\n\n${reference}\n`)
}
const mf='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(mf,'utf8')),ch=m.chapters.find(c=>c.chapter===29)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/09-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:'authored-and-reviewed'}))
ch.status=review.renderReview==='passed'?'complete':'content-complete'
ch.completionReview='raw_materials/physics/chapter-29-review.json';ch.pendingSourceUnits=ch.status==='complete'?[]:['direct-browser-render-review']
await writeFile(mf,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter29: eight topics, 108 detailed solutions, 12 slides, strict Cheatsheet and 16 Wiki entries. Status:',ch.status)
