import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {relativityTopics,relativitySlides} from '../docs/.vitepress/physics-relativity-course.mjs'
import {relativityConcepts} from '../docs/.vitepress/physics-relativity-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const complete=process.argv.includes('--complete')
if(complete){
 const accepted=JSON.parse(await readFile('qa/physics/chapter37/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed');assert.equal(accepted.endSolutions,102);assert.equal(accepted.examples,11)
}
const raw='raw_materials/physics/translations/chapter-37',dir='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(l=>l.sourceChapter===37)),slug=lesson.slug
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['vector','van-toc-vat-ly','dong-luong-vat-ly','cong-nang-luong','song']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=Object.keys(relativityConcepts)
lesson.topicGroups=relativityTopics;lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const decl=ast.body.find(n=>n.declaration?.declarations?.some(d=>d.id.name==='physics2Course')).declaration.declarations.find(d=>d.id.name==='physics2Course').init
const props=Object.fromEntries(decl.properties.map(p=>[p.key.name??p.key.value,p.value]))
const target=props.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===37))
const slides=[...physics2Course.slides.filter(s=>s.note!==slug),...relativitySlides]
const pages=[['bat-bien-dinh-luat', '01-bat-bien-dinh-luat.md', '37.1', 1217, 1220], ['tinh-tuong-doi-dong-thoi', '02-tinh-tuong-doi-dong-thoi.md', '37.2', 1220, 1222], ['gian-thoi-gian', '03-gian-thoi-gian.md', '37.3', 1222, 1227], ['co-chieu-dai', '04-co-chieu-dai.md', '37.4', 1227, 1231], ['bien-doi-lorentz', '05-bien-doi-lorentz.md', '37.5', 1231, 1235], ['doppler-dien-tu', '06-doppler-dien-tu.md', '37.6', 1235, 1236], ['dong-luong-tuong-doi', '07-dong-luong-tuong-doi.md', '37.7', 1237, 1239], ['cong-nang-luong-tuong-doi', '08-cong-nang-luong-tuong-doi.md', '37.8', 1239, 1242], ['newton-va-tuong-doi-rong', '09-newton-va-tuong-doi-rong.md', '37.9', 1243, 1244]]
const exercises=['11-luyen-tap-huong-dan.md', '12-cau-hoi-thao-luan.md', '13-bai-tap-01-13.md', '14-bai-tap-14-24.md', '15-bai-tap-25-39.md', '16-bai-tap-40-54.md', '17-bai-tap-55-62.md', '18-bai-tap-du-lieu-nang-cao.md', '19-mcat.md']
for(const f of ['00-mo-dau.md',...pages.map(p=>p[1]),'10-tom-tat.md',...exercises])await readFile(raw+'/'+f,'utf8')
for(const edit of [{start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)},{start:props.slides.start,end:props.slides.end,text:JSON.stringify(slides,null,2)}].sort((a,b)=>b.start-a.start))source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([k,v])=>k+': '+JSON.stringify(v)),'---',''].join('\n')
const ref=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
const inc=f=>'<!--@include: ../../../'+raw+'/'+f+'-->\n\n'
await mkdir(dir+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=relativityTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(dir+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:t.title,description:t.question})+'\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+ref('mục '+section,start,end)+'\n')
}
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,description:'Không thời gian, Lorentz, Doppler, động lượng, năng lượng và những ý niệm của thuyết tương đối rộng.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+inc('00-mo-dau.md')+'<TopicMap />\n\n'+inc('10-tom-tat.md')+'## Tài liệu tham khảo\n\n'+ref('chương 37',1217,1252)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Thuyết tương đối">\n\n'+exercises.map(inc).join('')+'## Tài liệu tham khảo\n\n'+ref('chương 37',1245,1252)+'\n\n</div>\n'
await writeFile(dir+'/'+slug+'.md',chapter)
const path='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(path,'utf8')),ch=m.chapters.find(c=>c.chapter===37)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/10-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:complete?'authored-source-reviewed-render-pending':'authored-under-review'}))
ch.status=complete?'content-complete':'authored-under-review';ch.pendingSourceUnits=['final-source-image-and-browser-review']
await writeFile(path,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter37: Nine topics,12 slides,102 end solutions. Status='+lesson.status)
