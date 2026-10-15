import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {interferenceTopics,interferenceSlides} from '../docs/.vitepress/physics-interference-course.mjs'
import {interferenceConcepts} from '../docs/.vitepress/physics-interference-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const complete=process.argv.includes('--complete')
if(complete){
 const accepted=JSON.parse(await readFile('qa/physics/chapter35/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed');assert.equal(accepted.endSolutions,91);assert.equal(accepted.examples,7)
}
const raw='raw_materials/physics/translations/chapter-35',dir='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(l=>l.sourceChapter===35)),slug=lesson.slug
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['song','pha-song','vector-pha','chiet-suat','phan-cuc-thang','cuong-do-buc-xa','don-vi']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=Object.keys(interferenceConcepts)
lesson.topicGroups=interferenceTopics;lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const decl=ast.body.find(n=>n.declaration?.declarations?.some(d=>d.id.name==='physics2Course')).declaration.declarations.find(d=>d.id.name==='physics2Course').init
const props=Object.fromEntries(decl.properties.map(p=>[p.key.name??p.key.value,p.value]))
const target=props.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===35))
const slides=[...physics2Course.slides.filter(s=>s.note!==slug),...interferenceSlides]
const pages=[
 ['giao-thoa-nguon-ket-hop','01-giao-thoa-nguon-ket-hop.md','35.1',1160,1162],
 ['giao-thoa-hai-nguon','02-giao-thoa-hai-nguon.md','35.2',1163,1166],
 ['cuong-do-giao-thoa','03-cuong-do-giao-thoa.md','35.3',1166,1169],
 ['giao-thoa-mang-mong','04-giao-thoa-mang-mong.md','35.4',1170,1175],
 ['giao-thoa-ke-michelson','05-giao-thoa-ke-michelson.md','35.5',1175,1176]
]
const exercises=['10-luyen-tap-huong-dan.md','11-cau-hoi-thao-luan.md','12-bai-tap-01-17.md','13-bai-tap-18-31.md','14-bai-tap-32-44.md','15-bai-tap-45-53.md','16-bai-tap-nang-cao.md','17-mcat.md','18-dap-so.md']
for(const f of ['00-mo-dau.md',...pages.map(p=>p[1]),'09-tom-tat.md',...exercises])await readFile(raw+'/'+f,'utf8')
for(const edit of [{start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)},{start:props.slides.start,end:props.slides.end,text:JSON.stringify(slides,null,2)}].sort((a,b)=>b.start-a.start))source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([k,v])=>k+': '+JSON.stringify(v)),'---',''].join('\n')
const ref=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
const inc=f=>'<!--@include: ../../../'+raw+'/'+f+'-->\n\n'
await mkdir(dir+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=interferenceTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(dir+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:t.title,description:t.question})+'\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+ref('mục '+section,start,end)+'\n')
}
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,description:'Nguồn kết hợp, thí nghiệm Young, cường độ giao thoa, màng mỏng và giao thoa kế Michelson.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+inc('00-mo-dau.md')+'<TopicMap />\n\n'+inc('09-tom-tat.md')+'## Tài liệu tham khảo\n\n'+ref('chương 35',1159,1184)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Giao thoa">\n\n'+exercises.map(inc).join('')+'## Tài liệu tham khảo\n\n'+ref('chương 35',1178,1184)+'\n\n</div>\n'
await writeFile(dir+'/'+slug+'.md',chapter)
const path='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(path,'utf8')),ch=m.chapters.find(c=>c.chapter===35)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/09-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:complete?'authored-source-reviewed-render-pending':'authored-under-review'}))
ch.status=complete?'content-complete':'authored-under-review';ch.pendingSourceUnits=['final-source-image-and-browser-review']
await writeFile(path,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter35: Five topics,10 slides,91 end solutions. Status='+lesson.status)
