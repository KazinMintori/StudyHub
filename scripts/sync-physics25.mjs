import {readFile,writeFile,mkdir} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {currentTopics,currentSlides} from '../docs/.vitepress/physics-current-course.mjs'
import {currentConcepts,currentWikiDetails,currentWikiConnections} from '../docs/.vitepress/physics-current-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const review=JSON.parse(await readFile('raw_materials/physics/chapter-25-review.json','utf8'))
const numeric=JSON.parse(await readFile('qa/physics/chapter25/numeric-checks.json','utf8'))
assert.equal(numeric.status,'passed');assert.equal(numeric.detailedSolutions,119)
const raw='raw_materials/physics/translations/chapter-25',dir='docs/vat-ly-2/bai-giang'
const lesson=physics2Course.lessons.find(l=>l.sourceChapter===25),slug=lesson.slug
lesson.status=review.status==='content-complete'?'ready':'draft'
lesson.prerequisites=['dien-tich','dien-the','dien-truong','cong-nang-luong','dan-nhiet','tich-phan']
lesson.supportingConcepts=['dong-dien','mat-do-dong-dien','dien-tro-suat','do-dan-dien','dien-tro','suat-dien-dong','dien-tro-trong','nhiet-do-tuyet-doi','do-ben-dien-moi']
lesson.topicGroups=currentTopics;lesson.hasChapterExercises=true
physics2Course.slides=[...physics2Course.slides.filter(s=>s.note!==slug),...currentSlides]
await writeFile('docs/.vitepress/physics-courses.mjs','// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
const pages=[
 ['dong-dien','01-dong-dien.md','25.1',813,816],
 ['dien-tro-suat','02-dien-tro-suat.md','25.2',816,819],
 ['dien-tro','03-dien-tro.md','25.3',819,822],
 ['suat-dien-dong','04-suat-dien-dong.md','25.4',822,827],
 ['nang-luong-cong-suat','05-nang-luong-cong-suat.md','25.5',828,832],
 ['dan-dien-kim-loai','06-mo-hinh-dan-dien-kim-loai.md','25.6',832,835]
]
await mkdir(`${dir}/${slug}`,{recursive:true})
for(const [topic,file,section,start,end] of pages){
 const t=currentTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(t.title)}\ndescription: ${JSON.stringify(t.question)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${section}, trang ${start}–${end}.\n`)
}
const exercises=['08-luyen-tap-huong-dan.md','09-cau-hoi-thao-luan.md','10-bai-tap-01-30.md','11-bai-tap-31-58.md','12-bai-tong-hop-59-78.md','13-bai-nang-cao-mcat.md','14-dap-so.md']
const include=file=>`<!--@include: ../../../${raw}/${file}-->\n\n`
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: ${JSON.stringify(lesson.title)}\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ${lesson.status}\nhasChapterExercises: true\ndescription: "Dòng điện, chuyển động trôi, điện trở suất, nguồn thực và năng lượng trong mạch điện."\n---\n\n<div class="lecture-notes-content">\n\n${include('00-mo-dau.md')}<TopicMap />\n\n${include('07-tom-tat.md')}## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 25, trang 812–843.\n\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Dòng điện, điện trở và suất điện động">\n\n${exercises.map(include).join('')}## Tài liệu tham khảo\n\nYoung & Freedman, ấn bản 15, chương 25, trang 836–843 và phụ lục đáp số A-16.\n\n</div>\n`)
await mkdir('docs/wiki',{recursive:true})
for(const [id,c] of Object.entries(currentConcepts)){
 const full=currentWikiDetails[id]
 const reference=full.slice(full.indexOf('\n\nTài liệu tham khảo:')).replace(/^\n\nTài liệu tham khảo:\s*/,'')
 const detail=full.replace(/\n\nTài liệu tham khảo:[\s\S]*$/,'')
 const related=currentWikiConnections[id].map(key=>{assert(concepts[key],key);return `- [${concepts[key].name}](./${key}.md)`}).join('\n')
 await writeFile(`docs/wiki/${id}.md`,`---\ntitle: ${JSON.stringify(c.name)}\nwikiTerm: ${id}\nprev: false\nnext: false\n---\n\n# ${c.name}\n\n${c.definition}\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n${detail}\n\n## Ví dụ\n\n${c.example}\n\n## Khi nào cần dùng?\n\n${c.use}\n\n## Câu hỏi ôn lại\n\n${c.question}\n\n<details><summary>Xem đáp án</summary>\n\n${c.answer}\n\n</details>\n\n## Thuật ngữ liên quan\n\n${related}\n\n## Tài liệu tham khảo\n\n${reference}\n`)
}
const mf='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(mf,'utf8')),ch=m.chapters.find(c=>c.chapter===25)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/07-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:'authored-and-reviewed'}))
ch.status=review.renderReview==='passed'?'complete':'content-complete'
ch.completionReview='raw_materials/physics/chapter-25-review.json'
ch.pendingSourceUnits=ch.status==='complete'?[]:['direct-browser-render-review']
await writeFile(mf,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter25: 6 topics, 119 detailed solutions, 8 slides, strict cheatsheet and 8 Wiki entries. Status:',ch.status)
