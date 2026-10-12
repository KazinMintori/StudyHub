import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {gaussTopics,gaussSlides} from '../docs/.vitepress/physics-gauss-course.mjs'

const review=JSON.parse(await readFile('raw_materials/physics/chapter-22-review.json','utf8'))
const slug='03-dinh-luat-gauss',raw='raw_materials/physics/translations/chapter-22',dir='docs/vat-ly-2/bai-giang'
const lesson=physics2Course.lessons.find(l=>l.sourceChapter===22)
lesson.prerequisites=['dien-truong','tich-vo-huong','tich-phan','vat-dan-cach-dien']
lesson.supportingConcepts=['dien-tich','dien-thong','dinh-luat-gauss','mat-gauss','che-chan-tinh-dien']
lesson.topicGroups=gaussTopics;lesson.hasChapterExercises=true
lesson.status=review.status==='content-complete'?'ready':'draft'
physics2Course.slides=[...physics2Course.slides.filter(s=>s.note!==slug),...gaussSlides]
await writeFile('docs/.vitepress/physics-courses.mjs','// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
await mkdir(`${dir}/${slug}`,{recursive:true})
const pages=[['dien-tich-dien-thong','01-dien-tich-dien-thong.md','22.1',718,721],['tinh-dien-thong','02-tinh-dien-thong.md','22.2',721,725],['dinh-luat-gauss','03-dinh-luat-gauss.md','22.3',725,729],['ung-dung-gauss','04-ung-dung-gauss.md','22.4',729,733],['dien-tich-vat-dan','05-dien-tich-vat-dan.md','22.5',734,737]]
for(const [topic,file,section,start,end] of pages){
 const t=gaussTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(t.title)}\ndescription: ${JSON.stringify(t.question)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${section}, trang ${start}–${end}.${section==='22.1'?' Mạch trình bày điện tích và điện thông có nền tảng từ Ruth W. Chabay và Bruce A. Sherwood, *Electric and Magnetic Interactions*, John Wiley & Sons, 1994.':''}\n`)
}
const exercises=['07-luyen-tap-huong-dan.md','08-cau-hoi-thao-luan.md','09-bai-tap-01-28.md','10-bai-tong-hop-29-44.md','11-bai-tong-hop-nang-cao.md','12-dap-so.md']
const include=f=>`<!--@include: ../../../${raw}/${f}-->\n\n`
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: "Định luật Gauss"\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ${lesson.status}\nhasChapterExercises: true\ndescription: "Điện thông, định luật Gauss, đối xứng cầu, trụ, phẳng và điện tích trên vật dẫn."\n---\n\n<div class="lecture-notes-content">\n\n${include('00-mo-dau.md')}<TopicMap />\n\n${include('06-tom-tat.md')}## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 22, trang 718–746.\n\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Định luật Gauss">\n\n${exercises.map(include).join('')}## Tài liệu tham khảo phần luyện tập\n\nYoung & Freedman, ấn bản 15, chương 22, trang 739–746 và phụ lục đáp số A-14–A-15.\n\n</div>\n`)
const mf='raw_materials/physics/translation-manifest.json',manifest=JSON.parse(await readFile(mf,'utf8')),ch=manifest.chapters.find(c=>c.chapter===22)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,section,start,end])=>({sourceUnit:section,file:raw+'/'+file,printedPages:[start,end],destination:'topic:'+topic})),{sourceUnit:'chapter-summary',file:raw+'/06-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:'authored-and-self-reviewed'}))
ch.status=lesson.status==='ready'&&review.renderReview==='passed'?'complete':lesson.status==='ready'?'content-complete':'in-progress'
ch.completionReview='raw_materials/physics/chapter-22-review.json'
ch.pendingSourceUnits=ch.status==='complete'?[]:lesson.status==='ready'?['direct-browser-render-review']:['final-source-and-figures-review','numeric-verification','math-and-site-checks','direct-browser-render-review']
await writeFile(mf,JSON.stringify(manifest,null,2)+'\n')
console.log('Integrated chapter22: 5 topic pages, separate exercises and 6 review slides.')
