import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {potentialTopics,potentialSlides} from '../docs/.vitepress/physics-potential-course.mjs'
const review=JSON.parse(await readFile('raw_materials/physics/chapter-23-review.json','utf8'))
const numeric=JSON.parse(await readFile('qa/physics/chapter23/numeric-checks.json','utf8'))
const slug='02-dien-the',raw='raw_materials/physics/translations/chapter-23',dir='docs/vat-ly-2/bai-giang'
const lesson=physics2Course.lessons.find(l=>l.sourceChapter===23)
lesson.prerequisites=['cong-nang-luong','dien-truong','tich-phan','gradient']
lesson.supportingConcepts=['dien-the','the-nang-dien','electron-volt','mat-dang-the','dinh-luat-gauss','vat-dan-cach-dien']
lesson.topicGroups=potentialTopics;lesson.hasChapterExercises=true
lesson.status=review.status==='content-complete'&&numeric.status==='passed'&&numeric.detailedSolutions===121?'ready':'draft'
physics2Course.slides=[...physics2Course.slides.filter(s=>s.note!==slug),...potentialSlides]
await writeFile('docs/.vitepress/physics-courses.mjs','// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
await mkdir(`${dir}/${slug}`,{recursive:true})
const pages=[['the-nang-dien','01-the-nang-dien.md','23.1',747,753],['dien-the','02-dien-the.md','23.2',754,759],['tinh-dien-the','03-tinh-dien-the.md','23.3',760,764],['mat-dang-the','04-mat-dang-the.md','23.4',764,767],['gradient-dien-the','05-gradient-dien-the.md','23.5',767,769]]
for(const [topic,file,section,start,end] of pages){
 const t=potentialTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(t.title)}\ndescription: ${JSON.stringify(t.question)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${section}, trang ${start}–${end}.\n`)
}
const exercises=['07-luyen-tap-huong-dan.md','08-cau-hoi-thao-luan.md','09-bai-tap-01-25.md','10-bai-tap-26-50.md','11-bai-tong-hop-51-70.md','12-bai-nang-cao-mcat.md','13-dap-so.md']
const include=f=>`<!--@include: ../../../${raw}/${f}-->\n\n`
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: "Điện thế"\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ${lesson.status}\nhasChapterExercises: true\ndescription: "Thế năng điện, hiệu điện thế, tính điện thế, mặt đẳng thế và gradient điện thế."\n---\n\n<div class="lecture-notes-content">\n\n${include('00-mo-dau.md')}<TopicMap />\n\n${include('06-tom-tat.md')}## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 23, trang 747–780.\n\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Điện thế">\n\n${exercises.map(include).join('')}## Tài liệu tham khảo\n\nYoung & Freedman, ấn bản 15, chương 23, trang 771–780 và phụ lục đáp số A-15–A-16.\n\n</div>\n`)
const mf='raw_materials/physics/translation-manifest.json',manifest=JSON.parse(await readFile(mf,'utf8')),ch=manifest.chapters.find(c=>c.chapter===23)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,section,start,end])=>({sourceUnit:section,file:raw+'/'+file,printedPages:[start,end],destination:'topic:'+topic})),{sourceUnit:'chapter-summary',file:raw+'/06-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:'authored-and-self-reviewed'}))
ch.status=lesson.status==='ready'&&review.renderReview==='passed'?'complete':lesson.status==='ready'?'content-complete':'in-progress'
ch.completionReview='raw_materials/physics/chapter-23-review.json'
ch.pendingSourceUnits=ch.status==='complete'?[]:lesson.status==='ready'?['direct-browser-render-review']:['final-semantic-and-math-review','numeric-verification','site-integration-and-render-review']
await writeFile(mf,JSON.stringify(manifest,null,2)+'\n')
console.log('Integrated chapter23: 5 topics, 121 detailed solutions, 6 slides and strict cheatsheet. Status:',ch.status)
