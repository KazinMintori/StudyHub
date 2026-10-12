import { readFile, writeFile, mkdir } from 'node:fs/promises'
import path from 'node:path'
import { physics1Course, physics2Course } from '../docs/.vitepress/physics-courses.mjs'
import { electrostaticsTopics, electrostaticsSlides } from '../docs/.vitepress/physics-electrostatics-course.mjs'
import { physicsMotionSlides } from '../docs/.vitepress/physics-motion-course.mjs'

const slug='01-dien-truong-coulomb'
const lesson=physics2Course.lessons.find(l=>l.sourceChapter===21)
if(!physics1Course.slides.some(s=>s.note==='02-chuyen-dong-thang'))physics1Course.slides.push(...physicsMotionSlides)
lesson.prerequisites=['vector','tich-vo-huong','tich-co-huong','luc','can-bang-co-hoc','duong-dong-chat-luu']
lesson.supportingConcepts=['dien-tich','dien-truong','vat-dan-cach-dien','phan-cuc-dien','luong-cuc-dien','don-vi','tich-phan']
lesson.hasChapterExercises=true
lesson.topicGroups=electrostaticsTopics
const review=JSON.parse(await readFile('raw_materials/physics/chapter-21-review.json','utf8'))
const contentComplete=review.status==='content-complete'&&review.exercises===101&&review.detailedSolutionBoxes===137
lesson.status=contentComplete?'ready':'draft'
physics2Course.description='Điện từ học, quang học và vật lý hiện đại, từ điện tích và điện trường đến hạt cơ bản và vũ trụ học.'
physics2Course.slides=[...physics2Course.slides.filter(s=>s.note!==slug),...electrostaticsSlides]
const moduleFile='docs/.vitepress/physics-courses.mjs'
await writeFile(moduleFile,'// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')

const sourceDir='raw_materials/physics/translations/chapter-21'
const noteDir='docs/vat-ly-2/bai-giang'
const pages=[['dien-tich','01-dien-tich.md',679,682],['vat-dan-cach-dien','02-vat-dan-cach-dien.md',682,684],['dinh-luat-coulomb','03-dinh-luat-coulomb.md',685,690],['dien-truong-luc-dien','04-dien-truong-luc-dien.md',690,694],['tinh-dien-truong','05-tinh-dien-truong.md',694,699],['duong-suc-dien','06-duong-suc-dien.md',700,701],['luong-cuc-dien','07-luong-cuc-dien.md',701,705]]
await mkdir(path.join(noteDir,slug),{recursive:true})
for(const [topicSlug,file,start,end] of pages) {
  const topic=electrostaticsTopics.flatMap(g=>g.topics).find(t=>t.slug===topicSlug)
  const rawFile=path.join(sourceDir,file)
  let text=await readFile(rawFile,'utf8')
  text=text.replace(/\]\(img\/young-21\//g,'](../img/young-21/')
  await writeFile(rawFile,text)
  await writeFile(path.join(noteDir,slug,topicSlug+'.md'),`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topicSlug}\nsection: topic\ntitle: ${JSON.stringify(topic.title)}\ndescription: ${JSON.stringify(topic.question)}\n---\n\n<!--@include: ../../../../${sourceDir}/${file}-->\n\n## Tài liệu tham khảo\n\nHugh D. Young và Roger A. Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 21, mục ${topic.source}, trang ${start}–${end}.\n`)
}
const exercises=['09-luyen-tap-huong-dan.md','10-cau-hoi-thao-luan.md','11-bai-tap-01-30.md','12-bai-tap-31-56.md','13-bai-tong-hop-57-80.md','14-bai-tong-hop-81-92.md','15-bai-nang-cao-mcat.md','16-dap-an-cuoi-chuong.md','17-dap-so-bai-le.md']
const include=file=>`<!--@include: ../../../${sourceDir}/${file}-->\n\n`
await writeFile(path.join(noteDir,slug+'.md'),`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: "Điện tích và điện trường"\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ${lesson.status}\nhasChapterExercises: true\ndescription: "Điện tích, lực Coulomb, điện trường, các phân bố điện tích và lưỡng cực điện."\n---\n\n<div class="lecture-notes-content">\n\n${include('00-mo-dau.md')}<TopicMap />\n\n${include('08-tom-tat.md')}## Tài liệu tham khảo\n\nHugh D. Young và Roger A. Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 21, trang 678–717.\n\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Điện tích và điện trường">\n\n${exercises.map(include).join('')}## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 21, trang 707–717 và đáp số phụ lục A-14–A-15.\n\n</div>\n`)
const manifestFile='raw_materials/physics/translation-manifest.json'
const manifest=JSON.parse(await readFile(manifestFile,'utf8'))
const chapter=manifest.chapters.find(c=>c.chapter===21)
chapter.fragments=[
 {sourceUnit:'chapter-opening',file:sourceDir+'/00-mo-dau.md',destination:'notes'},
 ...pages.map(([topicSlug,file,start,end])=>({sourceUnit:electrostaticsTopics.flatMap(g=>g.topics).find(t=>t.slug===topicSlug).source,file:sourceDir+'/'+file,printedPages:[start,end],destination:'topic:'+topicSlug})),
 {sourceUnit:'chapter-summary',file:sourceDir+'/08-tom-tat.md',destination:'notes'},
 ...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:sourceDir+'/'+file,destination:'bai-tap'}))
].map(f=>({...f,status:contentComplete?'authored-and-self-reviewed':'authored-awaiting-final-review'}))
chapter.status=contentComplete&&review.renderReview==='passed'?'complete':contentComplete?'content-complete':'in-progress'
chapter.completionReview='raw_materials/physics/chapter-21-review.json'
chapter.pendingSourceUnits=chapter.status==='complete'?[]:contentComplete?['direct-browser-render-review']:['final-source-audit','figures-and-captions-review','numeric-verification','site-integration-and-render-review']
await writeFile(manifestFile,JSON.stringify(manifest,null,2)+'\n')
console.log('Integrated chapter21: 7 topic pages, separate end-of-chapter exercise content and 6 review slides.')
