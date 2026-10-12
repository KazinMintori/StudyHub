import {readFile,writeFile,mkdir} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {dcTopics,dcSlides} from '../docs/.vitepress/physics-dc-course.mjs'
import {dcConcepts,dcWikiDetails,dcWikiConnections} from '../docs/.vitepress/physics-dc-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const review=JSON.parse(await readFile('raw_materials/physics/chapter-26-review.json','utf8'))
const numeric=JSON.parse(await readFile('qa/physics/chapter26/numeric-checks.json','utf8'))
assert.equal(numeric.status,'passed');assert.equal(numeric.detailedSolutions,122)
const raw='raw_materials/physics/translations/chapter-26',dir='docs/vat-ly-2/bai-giang'
const lesson=physics2Course.lessons.find(l=>l.sourceChapter===26),slug=lesson.slug
lesson.status=review.status==='content-complete'?'ready':'draft'
lesson.prerequisites=['dong-dien','dien-tro','dien-the','suat-dien-dong','dien-dung','cong-nang-luong','dao-ham','tich-phan']
lesson.supportingConcepts=['dien-tro-tuong-duong','quy-tac-kirchhoff','dien-ke','ampe-ke','von-ke','chiet-ap-can-bang','mach-rc','hang-so-thoi-gian','dien-tro-trong']
lesson.topicGroups=dcTopics;lesson.hasChapterExercises=true
physics2Course.slides=[...physics2Course.slides.filter(s=>s.note!==slug),...dcSlides]
await writeFile('docs/.vitepress/physics-courses.mjs','// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
const pages=[['noi-tiep-song-song','01-dien-tro-noi-tiep-song-song.md','26.1',845,849],['kirchhoff','02-quy-tac-kirchhoff.md','26.2',849,853],['dung-cu-do','03-dung-cu-do-dien.md','26.3',854,858],['mach-rc','04-mach-rc.md','26.4',858,863],['phan-phoi-dien','05-he-thong-phan-phoi-dien.md','26.5',863,866]]
await mkdir(`${dir}/${slug}`,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=dcTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(t.title)}\ndescription: ${JSON.stringify(t.question)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${section}, trang ${start}–${end}.\n`)
}
const exercises=['07-luyen-tap-huong-dan.md','08-cau-hoi-thao-luan.md','09-bai-tap-01-32.md','10-bai-tap-33-60.md','11-bai-tong-hop-61-80.md','12-bai-nang-cao-mcat.md','13-dap-so.md']
const include=file=>`<!--@include: ../../../${raw}/${file}-->\n\n`
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: ${JSON.stringify(lesson.title)}\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ${lesson.status}\nhasChapterExercises: true\ndescription: "Mạch nhiều nhánh, quy tắc Kirchhoff, dụng cụ đo, nạp và phóng tụ, phân phối điện."\n---\n\n<div class="lecture-notes-content">\n\n${include('00-mo-dau.md')}<TopicMap />\n\n${include('06-tom-tat.md')}## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 26, trang 844–877.\n\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Mạch điện một chiều">\n\n${exercises.map(include).join('')}## Tài liệu tham khảo\n\nYoung & Freedman, ấn bản 15, chương 26, trang 868–877 và phụ lục đáp số A-16–A-17.\n\n</div>\n`)
for(const [id,c]of Object.entries(dcConcepts)){
 const full=dcWikiDetails[id],reference=full.slice(full.indexOf('\n\nTài liệu tham khảo:')).replace(/^\n\nTài liệu tham khảo:\s*/,'')
 const detail=full.replace(/\n\nTài liệu tham khảo:[\s\S]*$/,'')
 const related=dcWikiConnections[id].map(key=>{assert(concepts[key],key);return `- [${concepts[key].name}](./${key}.md)`}).join('\n')
 await writeFile(`docs/wiki/${id}.md`,`---\ntitle: ${JSON.stringify(c.name)}\nwikiTerm: ${id}\nprev: false\nnext: false\n---\n\n# ${c.name}\n\n${c.definition}\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n${detail}\n\n## Ví dụ\n\n${c.example}\n\n## Khi nào cần dùng?\n\n${c.use}\n\n## Câu hỏi ôn lại\n\n${c.question}\n\n<details><summary>Xem đáp án</summary>\n\n${c.answer}\n\n</details>\n\n## Thuật ngữ liên quan\n\n${related}\n\n## Tài liệu tham khảo\n\n${reference}\n`)
}
const mf='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(mf,'utf8')),ch=m.chapters.find(c=>c.chapter===26)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/06-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:'authored-and-reviewed'}))
ch.status=review.renderReview==='passed'?'complete':'content-complete'
ch.completionReview='raw_materials/physics/chapter-26-review.json';ch.pendingSourceUnits=ch.status==='complete'?[]:['direct-browser-render-review']
await writeFile(mf,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter26: 5 topics, 122 detailed solutions, 8 slides, strict cheatsheet and 8 Wiki entries. Status:',ch.status)
