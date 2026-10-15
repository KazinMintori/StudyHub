import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {photonTopics,photonSlides} from '../docs/.vitepress/physics-photon-course.mjs'
import {photonConcepts} from '../docs/.vitepress/physics-photon-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const complete=process.argv.includes('--complete')
if(complete){
 const accepted=JSON.parse(await readFile('qa/physics/chapter38/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed');assert.equal(accepted.endSolutions,75);assert.equal(accepted.examples,7)
}
const raw='raw_materials/physics/translations/chapter-38',dir='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(l=>l.sourceChapter===38)),slug=lesson.slug
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['cong-nang-luong','dong-luong-vat-ly','electron-volt','song','song-dien-tu','nhieu-xa-khe-don','dong-luong-tuong-doi','nang-luong-nghi']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=['photon',...Object.keys(photonConcepts)]
lesson.topicGroups=photonTopics;lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const decl=ast.body.find(n=>n.declaration?.declarations?.some(d=>d.id.name==='physics2Course')).declaration.declarations.find(d=>d.id.name==='physics2Course').init
const props=Object.fromEntries(decl.properties.map(p=>[p.key.name??p.key.value,p.value]))
const target=props.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===38))
const slides=[...physics2Course.slides.filter(s=>s.note!==slug),...photonSlides]
const pages=[['quang-dien', '01-quang-dien.md', '38.1', 1253, 1259], ['phat-tia-x', '02-phat-tia-x.md', '38.2', 1259, 1262], ['compton-tao-cap', '03-compton-tao-cap.md', '38.3', 1262, 1265], ['luong-tinh-bat-dinh', '04-luong-tinh-bat-dinh.md', '38.4', 1266, 1272]]
const exercises=['06-luyen-tap-huong-dan.md', '07-cau-hoi-thao-luan.md', '08-bai-tap-01-12.md', '09-bai-tap-13-23.md', '10-bai-tap-24-31.md', '11-bai-tap-32-37.md', '12-bai-tap-nang-cao.md', '13-mcat.md']
for(const f of ['00-mo-dau.md',...pages.map(p=>p[1]),'05-tom-tat.md',...exercises])await readFile(raw+'/'+f,'utf8')
for(const edit of [{start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)},{start:props.slides.start,end:props.slides.end,text:JSON.stringify(slides,null,2)}].sort((a,b)=>b.start-a.start))source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([k,v])=>k+': '+JSON.stringify(v)),'---',''].join('\n')
const ref=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
const inc=f=>'<!--@include: ../../../'+raw+'/'+f+'-->\n\n'
await mkdir(dir+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=photonTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(dir+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:t.title,description:t.question})+'\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+ref('mục '+section,start,end)+'\n')
}
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,description:'Photon, quang điện, phát tia X, Compton, tạo cặp, lưỡng tính sóng–hạt và bất định.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+inc('00-mo-dau.md')+'<TopicMap />\n\n'+inc('05-tom-tat.md')+'## Tài liệu tham khảo\n\n'+ref('chương 38',1253,1278)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Photon">\n\n'+exercises.map(inc).join('')+'## Tài liệu tham khảo\n\n'+ref('chương 38',1273,1278)+'\n\n</div>\n'
await writeFile(dir+'/'+slug+'.md',chapter)
const path='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(path,'utf8')),ch=m.chapters.find(c=>c.chapter===38)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/05-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:complete?'authored-source-reviewed-render-pending':'authored-under-review'}))
ch.status=complete?'content-complete':'authored-under-review';ch.pendingSourceUnits=['final-source-image-and-browser-review']
await writeFile(path,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter38: Four topics,12 slides,75 end solutions. Status='+lesson.status)
