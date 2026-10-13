import {readFile,writeFile,mkdir} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {sourcesTopics,sourcesSlides} from '../docs/.vitepress/physics-sources-course.mjs'
import {sourcesConcepts,sourcesWikiDetails,sourcesWikiConnections} from '../docs/.vitepress/physics-sources-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const review=JSON.parse(await readFile('raw_materials/physics/chapter-28-review.json','utf8'))
const numeric=JSON.parse(await readFile('qa/physics/chapter28/numeric-checks.json','utf8'))
assert.equal(numeric.status,'passed');assert.equal(numeric.detailedSolutions,116)
const raw='raw_materials/physics/translations/chapter-28',dir='docs/vat-ly-2/bai-giang'
const lesson=physics2Course.lessons.find(l=>l.sourceChapter===28),slug=lesson.slug
lesson.status=review.status==='content-complete'?'ready':'draft'
lesson.prerequisites=['vector','tich-co-huong','dien-tich','dong-dien','dien-truong','dinh-luat-gauss','tu-truong','luc-tu-tren-dien-tich','momen-tu','momen-dong-luong','tich-phan']
lesson.supportingConcepts=Object.keys(sourcesConcepts).filter(id=>!lesson.prerequisites.includes(id))
lesson.topicGroups=sourcesTopics;lesson.hasChapterExercises=true
physics2Course.slides=[...physics2Course.slides.filter(s=>s.note!==slug),...sourcesSlides]
await writeFile('docs/.vitepress/physics-courses.mjs','// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
const pages=[["dien-tich-chuyen-dong-tu-truong","01-dien-tich-chuyen-dong.md","28.1",918,921],["tu-truong-biot-savart","02-phan-tu-dong-dien.md","28.2",921,923],["tu-truong-day-thang","03-day-thang.md","28.3",923,926],["luc-tu-hai-day","04-luc-hai-day.md","28.4",926,927],["tu-truong-vong-day","05-vong-day-tron.md","28.5",927,930],["dinh-luat-ampere","06-dinh-luat-ampere.md","28.6",930,933],["ung-dung-ampere","07-ung-dung-ampere.md","28.7",933,937],["vat-lieu-tu","08-vat-lieu-tu.md","28.8",937,941]]
await mkdir(`${dir}/${slug}`,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=sourcesTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(t.title)}\ndescription: ${JSON.stringify(t.question)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${section}, trang ${start}–${end}.\n`)
}
const exercises=["10-luyen-tap-huong-dan.md","11-cau-hoi-thao-luan.md","12-bai-tap-01-30.md","13-bai-tap-31-60.md","14-bai-tong-hop-61-75.md","15-nang-cao-mcat.md","16-dap-so.md"]
const include=file=>`<!--@include: ../../../${raw}/${file}-->\n\n`
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: ${JSON.stringify(lesson.title)}\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ${lesson.status}\nhasChapterExercises: true\ndescription: "Từ trường do điện tích chuyển động, Biot–Savart, dây thẳng, vòng dây, định luật Ampere và vật liệu từ."\n---\n\n<div class="lecture-notes-content">\n\n${include('00-mo-dau.md')}<TopicMap />\n\n${include('09-tom-tat.md')}## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 28, trang 918–952.\n\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Nguồn của từ trường">\n\n${exercises.map(include).join('')}## Tài liệu tham khảo\n\nYoung & Freedman, ấn bản 15, chương 28, trang 943–952 và phụ lục đáp số A-17.\n\n</div>\n`)
for(const [id,c]of Object.entries(sourcesConcepts)){
 const full=sourcesWikiDetails[id],reference=full.slice(full.indexOf('\n\nTài liệu tham khảo:')).replace(/^\n\nTài liệu tham khảo:\s*/,'')
 const detail=full.replace(/\n\nTài liệu tham khảo:[\s\S]*$/,'')
 const related=sourcesWikiConnections[id].map(key=>{assert(concepts[key],key);return `- [${concepts[key].name}](./${key}.md)`}).join('\n')
 await writeFile(`docs/wiki/${id}.md`,`---\ntitle: ${JSON.stringify(c.name)}\nwikiTerm: ${id}\nprev: false\nnext: false\n---\n\n# ${c.name}\n\n${c.definition}\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n${detail}\n\n## Ví dụ\n\n${c.example}\n\n## Khi nào cần dùng?\n\n${c.use}\n\n## Câu hỏi ôn lại\n\n${c.question}\n\n<details><summary>Xem đáp án</summary>\n\n${c.answer}\n\n</details>\n\n## Thuật ngữ liên quan\n\n${related}\n\n## Tài liệu tham khảo\n\n${reference}\n`)
}
const mf='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(mf,'utf8')),ch=m.chapters.find(c=>c.chapter===28)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/09-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:'authored-and-reviewed'}))
ch.status=review.renderReview==='passed'?'complete':'content-complete'
ch.completionReview='raw_materials/physics/chapter-28-review.json';ch.pendingSourceUnits=ch.status==='complete'?[]:['direct-browser-render-review']
await writeFile(mf,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter28: 8 topics, 116 detailed solutions, 11 slides, strict cheatsheet and 16 Wiki entries. Status:',ch.status)
