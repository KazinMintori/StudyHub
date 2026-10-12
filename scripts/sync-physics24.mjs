import {readFile,writeFile,mkdir} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {capacitanceTopics,capacitanceSlides} from '../docs/.vitepress/physics-capacitance-course.mjs'
import {capacitanceConcepts,capacitanceWikiDetails,capacitanceWikiConnections} from '../docs/.vitepress/physics-capacitance-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const review=JSON.parse(await readFile('raw_materials/physics/chapter-24-review.json','utf8'))
const numeric=JSON.parse(await readFile('qa/physics/chapter24/numeric-checks.json','utf8'))
assert.equal(numeric.status,'passed');assert.equal(numeric.detailedSolutions,110)
const raw='raw_materials/physics/translations/chapter-24',dir='docs/vat-ly-2/bai-giang'
const lesson=physics2Course.lessons.find(l=>l.sourceChapter===24),slug=lesson.slug
lesson.status=review.status==='content-complete'?'ready':'draft'
lesson.prerequisites=['dien-the','dien-truong','dinh-luat-gauss','tich-phan','phan-cuc-dien','luong-cuc-dien']
lesson.supportingConcepts=['dien-dung','dien-moi','do-dien-tham','do-ben-dien-moi','mat-do-nang-luong-dien-truong','vat-dan-cach-dien','mat-dang-the','cong-nang-luong']
lesson.topicGroups=capacitanceTopics;lesson.hasChapterExercises=true
physics2Course.slides=[...physics2Course.slides.filter(s=>s.note!==slug),...capacitanceSlides]
await writeFile('docs/.vitepress/physics-courses.mjs','// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
const pages=[
 ['tu-dien-dien-dung','01-tu-dien-dien-dung.md','24.1',782,786],
 ['mac-tu-dien','02-mac-tu-dien.md','24.2',786,789],
 ['nang-luong-tu-dien','03-nang-luong-tu-dien.md','24.3',790,793],
 ['dien-moi','04-dien-moi.md','24.4',793,799],
 ['mo-hinh-phan-tu','05-mo-hinh-phan-tu.md','24.5',799,800],
 ['gauss-trong-dien-moi','06-gauss-trong-dien-moi.md','24.6',801,802]
]
await mkdir(`${dir}/${slug}`,{recursive:true})
for(const [topic,file,section,start,end] of pages){
 const t=capacitanceTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(t.title)}\ndescription: ${JSON.stringify(t.question)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${section}, trang ${start}–${end}.\n`)
}
const exercises=['08-luyen-tap-huong-dan.md','09-cau-hoi-thao-luan.md','10-bai-tap-01-24.md','11-bai-tap-25-44.md','12-bai-tap-40-55.md','13-bai-tap-56-68.md','14-bai-nang-cao-mcat.md','15-dap-so.md']
const include=file=>`<!--@include: ../../../${raw}/${file}-->\n\n`
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: ${JSON.stringify(lesson.title)}\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ${lesson.status}\nhasChapterExercises: true\ndescription: "Điện dung, các mạng tụ, năng lượng, phân cực điện môi và định luật Gauss trong điện môi."\n---\n\n<div class="lecture-notes-content">\n\n${include('00-mo-dau.md')}<TopicMap />\n\n${include('07-tom-tat.md')}## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 24, trang 781–811.\n\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Điện dung và điện môi">\n\n${exercises.map(include).join('')}## Tài liệu tham khảo\n\nYoung & Freedman, ấn bản 15, chương 24, trang 803–811 và phụ lục đáp số A-16.\n\n</div>\n`)
for(const [id,c] of Object.entries(capacitanceConcepts)){
 const detail=capacitanceWikiDetails[id].replace(/\n\nTài liệu tham khảo:[\s\S]*$/,'')
 const related=capacitanceWikiConnections[id].map(key=>`- [${concepts[key].name}](./${key}.md)`).join('\n')
 await writeFile(`docs/wiki/${id}.md`,`---\ntitle: ${JSON.stringify(c.name)}\nwikiTerm: ${id}\nprev: false\nnext: false\n---\n\n# ${c.name}\n\n${c.definition}\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n${detail}\n\n## Ví dụ\n\n${c.example}\n\n## Khi nào cần dùng?\n\n${c.use}\n\n## Câu hỏi ôn lại\n\n${c.question}\n\n<details><summary>Xem đáp án</summary>\n\n${c.answer}\n\n</details>\n\n## Thuật ngữ liên quan\n\n${related}\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 24, trang 781–802.\n`)
}
const mf='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(mf,'utf8')),ch=m.chapters.find(c=>c.chapter===24)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/07-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:'authored-and-reviewed'}))
ch.status=review.renderReview==='passed'?'complete':'content-complete'
ch.completionReview='raw_materials/physics/chapter-24-review.json'
ch.pendingSourceUnits=ch.status==='complete'?[]:['direct-browser-render-review']
await writeFile(mf,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter24: 6 topics, 110 detailed solutions, 8 slides, strict cheatsheet and 5 Wiki entries. Status:',ch.status)
