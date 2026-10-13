import {readFile,writeFile,mkdir} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {magneticTopics,magneticSlides} from '../docs/.vitepress/physics-magnetic-course.mjs'
import {magneticConcepts,magneticWikiDetails,magneticWikiConnections} from '../docs/.vitepress/physics-magnetic-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const review=JSON.parse(await readFile('raw_materials/physics/chapter-27-review.json','utf8'))
const numeric=JSON.parse(await readFile('qa/physics/chapter27/numeric-checks.json','utf8'))
assert.equal(numeric.status,'passed');assert.equal(numeric.detailedSolutions,116)
const raw='raw_materials/physics/translations/chapter-27',dir='docs/vat-ly-2/bai-giang'
const lesson=physics2Course.lessons.find(l=>l.sourceChapter===27),slug=lesson.slug
lesson.status=review.status==='content-complete'?'ready':'draft'
lesson.prerequisites=['vector','tich-co-huong','dien-tich','dong-dien','luc','momen-luc','momen-quan-tinh','cong-nang-luong','dao-ham','tich-phan']
lesson.supportingConcepts=Object.keys(magneticConcepts)
lesson.topicGroups=magneticTopics;lesson.hasChapterExercises=true
physics2Course.slides=[...physics2Course.slides.filter(s=>s.note!==slug),...magneticSlides]
await writeFile('docs/.vitepress/physics-courses.mjs','// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
const pages=[["tu-tinh","01-tu-tinh.md","27.1",878,880],["tu-truong","02-tu-truong.md","27.2",880,884],["duong-suc-tu-thong","03-duong-suc-tu-thong.md","27.3",884,888],["chuyen-dong-hat","04-chuyen-dong-hat.md","27.4",888,891],["ung-dung-hat","05-ung-dung.md","27.5",891,893],["luc-len-day","06-luc-tu-len-day.md","27.6",893,896],["vong-day-mo-men","07-vong-day-mo-men.md","27.7",897,902],["dong-co-dien","08-dong-co-dien.md","27.8",902,904],["hall","09-hieu-ung-hall.md","27.9",904,906]]
await mkdir(`${dir}/${slug}`,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=magneticTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(t.title)}\ndescription: ${JSON.stringify(t.question)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${section}, trang ${start}–${end}.\n`)
}
const exercises=["11-luyen-tap-huong-dan.md","12-cau-hoi-thao-luan.md","13-bai-tap-01-30.md","14-bai-tap-31-60.md","15-bai-tong-hop-61-80.md","16-bai-nang-cao-mcat.md","17-dap-so.md"]
const include=file=>`<!--@include: ../../../${raw}/${file}-->\n\n`
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: ${JSON.stringify(lesson.title)}\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ${lesson.status}\nhasChapterExercises: true\ndescription: "Lực từ, từ thông, quỹ đạo hạt, lực và mômen lên vòng dây, động cơ điện và hiệu ứng Hall."\n---\n\n<div class="lecture-notes-content">\n\n${include('00-mo-dau.md')}<TopicMap />\n\n${include('10-tom-tat.md')}## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 27, trang 878–917.\n\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Từ trường và lực từ">\n\n${exercises.map(include).join('')}## Tài liệu tham khảo\n\nYoung & Freedman, ấn bản 15, chương 27, trang 907–917 và phụ lục đáp số A-17.\n\n</div>\n`)
for(const [id,c]of Object.entries(magneticConcepts)){
 const full=magneticWikiDetails[id],reference=full.slice(full.indexOf('\n\nTài liệu tham khảo:')).replace(/^\n\nTài liệu tham khảo:\s*/,'')
 const detail=full.replace(/\n\nTài liệu tham khảo:[\s\S]*$/,'')
 const related=magneticWikiConnections[id].map(key=>{assert(concepts[key],key);return `- [${concepts[key].name}](./${key}.md)`}).join('\n')
 await writeFile(`docs/wiki/${id}.md`,`---\ntitle: ${JSON.stringify(c.name)}\nwikiTerm: ${id}\nprev: false\nnext: false\n---\n\n# ${c.name}\n\n${c.definition}\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n${detail}\n\n## Ví dụ\n\n${c.example}\n\n## Khi nào cần dùng?\n\n${c.use}\n\n## Câu hỏi ôn lại\n\n${c.question}\n\n<details><summary>Xem đáp án</summary>\n\n${c.answer}\n\n</details>\n\n## Thuật ngữ liên quan\n\n${related}\n\n## Tài liệu tham khảo\n\n${reference}\n`)
}
const mf='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(mf,'utf8')),ch=m.chapters.find(c=>c.chapter===27)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/10-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:'authored-and-reviewed'}))
ch.status=review.renderReview==='passed'?'complete':'content-complete'
ch.completionReview='raw_materials/physics/chapter-27-review.json';ch.pendingSourceUnits=ch.status==='complete'?[]:['direct-browser-render-review']
await writeFile(mf,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter27: 9 topics, 116 detailed solutions, 12 slides, strict cheatsheet and 11 Wiki entries. Status:',ch.status)
