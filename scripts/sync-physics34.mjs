import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {geometricOpticsTopics,geometricOpticsSlides} from '../docs/.vitepress/physics-geometric-optics-course.mjs'
import {geometricOpticsConcepts} from '../docs/.vitepress/physics-geometric-optics-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const complete=process.argv.includes('--complete')
if(complete){
 const accepted=JSON.parse(await readFile('qa/physics/chapter34/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed');assert.equal(accepted.endSolutions,148);assert.equal(accepted.examples,14)
}
const raw='raw_materials/physics/translations/chapter-34',dir='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(l=>l.sourceChapter===34)),slug=lesson.slug
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['tia-sang','phan-xa-guong','chiet-suat','dinh-luat-snell','don-vi']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=Object.keys(geometricOpticsConcepts)
lesson.topicGroups=geometricOpticsTopics;lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const decl=ast.body.find(n=>n.declaration?.declarations?.some(d=>d.id.name==='physics2Course')).declaration.declarations.find(d=>d.id.name==='physics2Course').init
const props=Object.fromEntries(decl.properties.map(p=>[p.key.name??p.key.value,p.value]))
const target=props.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===34))
const slides=[...physics2Course.slides.filter(s=>s.note!==slug),...geometricOpticsSlides]
const pages=[
 ['guong-phang','01-guong-phang.md','34.1',1110,1113],
 ['guong-cau','02-guong-cau.md','34.2',1114,1122],
 ['khuc-xa-mat-cau','03-khuc-xa-mat-cau.md','34.3',1122,1126],
 ['thau-kinh-mong','04-thau-kinh-mong.md','34.4',1127,1135],
 ['may-anh','05-may-anh.md','34.5',1135,1138],
 ['mat','06-mat.md','34.6',1138,1142],
 ['kinh-lup','07-kinh-lup.md','34.7',1142,1143],
 ['kinh-hien-vi-thien-van','08-kinh-hien-vi-thien-van.md','34.8',1143,1147]
]
const exercises=['10-luyen-tap-huong-dan.md','11-cau-hoi-thao-luan.md','12-bai-tap-01-39.md','13-bai-tap-40-65.md','14-bai-tap-66-83.md','15-bai-tap-84-103.md','16-bai-tap-nang-cao.md','17-mcat.md','18-dap-so.md']
for(const f of ['00-mo-dau.md',...pages.map(p=>p[1]),'09-tom-tat.md',...exercises])await readFile(raw+'/'+f,'utf8')
for(const edit of [{start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)},{start:props.slides.start,end:props.slides.end,text:JSON.stringify(slides,null,2)}].sort((a,b)=>b.start-a.start))source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([k,v])=>k+': '+JSON.stringify(v)),'---',''].join('\n')
const ref=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
const inc=f=>'<!--@include: ../../../'+raw+'/'+f+'-->\n\n'
await mkdir(dir+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=geometricOpticsTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(dir+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:t.title,description:t.question})+'\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+ref('mục '+section,start,end)+'\n')
}
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,description:'Gương phẳng, gương cầu, khúc xạ tại mặt cầu, thấu kính mỏng, máy ảnh, mắt, kính lúp, kính hiển vi và kính thiên văn.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+inc('00-mo-dau.md')+'<TopicMap />\n\n'+inc('09-tom-tat.md')+'## Tài liệu tham khảo\n\n'+ref('chương34',1110,1158)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Quang hình học">\n\n'+exercises.map(inc).join('')+'## Tài liệu tham khảo\n\n'+ref('chương34',1149,1158)+'\n\n</div>\n'
await writeFile(dir+'/'+slug+'.md',chapter)
const path='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(path,'utf8')),ch=m.chapters.find(c=>c.chapter===34)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/09-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:complete?'authored-source-reviewed-render-pending':'authored-under-review'}))
ch.status=complete?'content-complete':'authored-under-review';ch.pendingSourceUnits=['final-source-image-and-browser-review']
await writeFile(path,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter34: Eight topics,12 slides,148 end solutions. Status='+lesson.status)
