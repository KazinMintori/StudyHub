import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
const lesson=physics2Course.lessons.find(l=>l.sourceChapter===23),slug=lesson.slug
const raw='raw_materials/physics/translations/chapter-23',dir='docs/vat-ly-2/bai-giang'
const topics=[
 ['the-nang-dien','Thế năng điện','01-the-nang-dien.md',747,753],
 ['dien-the','Điện thế và hiệu điện thế','02-dien-the.md',754,759],
 ['tinh-dien-the','Tính điện thế của các phân bố nguồn','03-tinh-dien-the.md',760,764],
 ['mat-dang-the','Mặt đẳng thế và vật dẫn','04-mat-dang-the.md',764,767],
 ['gradient-dien-the','Gradient điện thế','05-gradient-dien-the.md',767,769]
]
lesson.status='draft'
lesson.prerequisites=['cong-nang-luong','dien-truong','tich-phan','gradient']
lesson.supportingConcepts=['dien-the','dinh-luat-gauss','vat-dan-cach-dien']
lesson.topicGroups=[{title:'Thế năng và điện thế',topics:topics.slice(0,2).map(([slug,title])=>({slug,title}))},
 {title:'Tính toán và hình học điện thế',topics:topics.slice(2).map(([slug,title])=>({slug,title}))}]
await mkdir(`${dir}/${slug}`,{recursive:true})
for(const [topic,title,file,start,end] of topics){
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(title)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 23, trang ${start}–${end}.\n`)
}
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: "Điện thế"\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: draft\ndescription: "Thế năng điện, hiệu điện thế, tính điện thế, mặt đẳng thế và gradient điện thế."\n---\n\n<!--@include: ../../../${raw}/00-mo-dau.md-->\n\n<TopicMap />\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 23, trang 747–780.\n`)
await writeFile('docs/.vitepress/physics-courses.mjs','// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
console.log('Integrated chapter23 theory for reading. Full chapter remains draft until end material and review are complete.')
