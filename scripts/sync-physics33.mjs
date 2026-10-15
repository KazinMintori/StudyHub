import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {opticsTopics,opticsSlides} from '../docs/.vitepress/physics-optics-course.mjs'
import {opticsConcepts} from '../docs/.vitepress/physics-optics-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'

const complete=process.argv.includes('--complete')
if(complete){
 const accepted=JSON.parse(await readFile('qa/physics/chapter33/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed')
 assert.equal(accepted.endSolutions,102)
 assert.equal(accepted.examples,6)
}
const raw='raw_materials/physics/translations/chapter-33',dir='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(l=>l.sourceChapter===33)),slug=lesson.slug
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['song','pha-song','vector','dao-ham','dao-dong-dieu-hoa','song-dien-tu','cuong-do-buc-xa']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=['chiet-suat','dinh-luat-snell','phan-cuc-thang',...Object.keys(opticsConcepts)]
lesson.topicGroups=opticsTopics
lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const decl=ast.body.find(n=>n.declaration?.declarations?.some(d=>d.id.name==='physics2Course')).declaration.declarations.find(d=>d.id.name==='physics2Course').init
const props=Object.fromEntries(decl.properties.map(p=>[p.key.name??p.key.value,p.value]))
const target=props.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===33))
const slides=[...physics2Course.slides.filter(s=>s.note!==slug),...opticsSlides]
for(const edit of [{start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)},{start:props.slides.start,end:props.slides.end,text:JSON.stringify(slides,null,2)}].sort((a,b)=>b.start-a.start))source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
const pages=[
 ['ban-chat-anh-sang','01-ban-chat-anh-sang.md','33.1',1077,1079],
 ['phan-xa-khuc-xa','02-phan-xa-khuc-xa.md','33.2',1079,1085],
 ['phan-xa-toan-phan','03-phan-xa-toan-phan.md','33.3',1085,1088],
 ['tan-sac','04-tan-sac.md','33.4',1088,1090],
 ['phan-cuc','05-phan-cuc.md','33.5',1090,1097],
 ['tan-xa-anh-sang','06-tan-xa-anh-sang.md','33.6',1097,1098],
 ['nguyen-ly-huygens','07-nguyen-ly-huygens.md','33.7',1099,1101]
]
const exercises=['10-luyen-tap-huong-dan.md','11-cau-hoi-thao-luan.md','12-bai-tap-01-35.md','13-bai-tap-36-58.md','14-nang-cao-59-61.md','15-mcat.md','16-dap-so.md']
for(const file of ['00-mo-dau.md',...pages.map(p=>p[1]),'09-tom-tat.md',...exercises])await readFile(raw+'/'+file,'utf8')
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const reference=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
const inc=file=>'<!--@include: ../../../'+raw+'/'+file+'-->\n\n'
await mkdir(dir+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=opticsTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(dir+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:t.title,description:t.question})+'\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+reference('mục '+section,start,end)+'\n')
}
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,description:'Bản chất ánh sáng, phản xạ, khúc xạ, phản xạ toàn phần, tán sắc, phân cực, tán xạ và nguyên lý Huygens.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+inc('00-mo-dau.md')+'<TopicMap />\n\n'+inc('09-tom-tat.md')+'## Tài liệu tham khảo\n\n'+reference('chương 33',1077,1109)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Bản chất và sự truyền ánh sáng">\n\n'+exercises.map(inc).join('')+'## Tài liệu tham khảo\n\n'+reference('chương 33',1102,1109)+'\n\n</div>\n'
await writeFile(dir+'/'+slug+'.md',chapter)
const path='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(path,'utf8')),ch=m.chapters.find(c=>c.chapter===33)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/09-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:complete?'authored-source-reviewed-render-pending':'authored-under-review'}))
ch.status=complete?'content-complete':'authored-under-review'
ch.pendingSourceUnits=['final-source-image-and-browser-review']
await writeFile(path,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter33: Seven topics,11 slides,102 end solutions. Status='+lesson.status)
