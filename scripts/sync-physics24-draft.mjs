import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
const lesson=physics2Course.lessons.find(l=>l.sourceChapter===24),slug=lesson.slug
const raw='raw_materials/physics/translations/chapter-24',dir='docs/vat-ly-2/bai-giang'
const pages=[
 ['tu-dien-dien-dung','Tụ điện và điện dung','01-tu-dien-dien-dung.md','24.1',782,786],
 ['mac-tu-dien','Tụ mắc nối tiếp và song song','02-mac-tu-dien.md','24.2',786,789],
 ['nang-luong-tu-dien','Năng lượng của tụ và điện trường','03-nang-luong-tu-dien.md','24.3',790,793],
 ['dien-moi','Điện môi','04-dien-moi.md','24.4',793,799],
 ['mo-hinh-phan-tu','Mô hình phân tử của điện tích cảm ứng','05-mo-hinh-phan-tu.md','24.5',799,800],
 ['gauss-trong-dien-moi','Định luật Gauss trong điện môi','06-gauss-trong-dien-moi.md','24.6',801,802]
]
lesson.status='draft'
lesson.prerequisites=['dien-the','dien-truong','dinh-luat-gauss','tich-phan','phan-cuc-dien','luong-cuc-dien']
lesson.supportingConcepts=['dien-dung','vat-dan-cach-dien','mat-dang-the','cong-nang-luong']
lesson.topicGroups=[{title:'Cấu trúc, cách mắc và năng lượng',topics:pages.slice(0,3).map(([slug,title])=>({slug,title}))},{title:'Điện môi và phân cực',topics:pages.slice(3).map(([slug,title])=>({slug,title}))}]
await mkdir(`${dir}/${slug}`,{recursive:true})
for(const [topic,title,file,section,start,end] of pages){
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(title)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${section}, trang ${start}–${end}.\n`)
}
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: ${JSON.stringify(lesson.title)}\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: draft\ndescription: "Điện dung, các mạng tụ, năng lượng, phân cực điện môi và định luật Gauss trong điện môi."\n---\n\n<!--@include: ../../../${raw}/00-mo-dau.md-->\n\n<TopicMap />\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 24, trang 781–811.\n`)
await writeFile('docs/.vitepress/physics-courses.mjs','// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
const mf='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(mf,'utf8')),chapter=m.chapters.find(c=>c.chapter===24)
chapter.status='in-progress'
chapter.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,title,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]}))].map(f=>({...f,status:'theory-authored-and-numerically-checked-awaiting-full-chapter-review'}))
chapter.pendingSourceUnits=['chapter-summary','guided-practice','discussion-questions','all-end-of-chapter-exercises-and-problems','appendix-odd-answers','slides-and-cheatsheet','supporting-wiki-details','final-semantic-and-render-review']
await writeFile(mf,JSON.stringify(m,null,2)+'\n')
console.log('Chapter24 theory draft integrated: 6 sections, 12 examples, 23 numbered equations, 28 figures. Full chapter remains incomplete.')
