import {readFile,writeFile,mkdir,access} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {matterWavesTopics,matterWavesSlides} from '../docs/.vitepress/physics-matter-waves-course.mjs'
import {matterWavesConcepts} from '../docs/.vitepress/physics-matter-waves-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const complete=process.argv.includes('--complete')
const raw='raw_materials/physics/translations/chapter-39',dir='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(l=>l.sourceChapter===39)),slug=lesson.slug
const pages=[
 ['song-electron','01-song-electron.md','39.1',1279,1285],
 ['nguyen-tu-hat-nhan-pho','02-nguyen-tu-hat-nhan-pho.md','39.2',1285,1289],
 ['muc-nang-luong-bohr','03-muc-nang-luong-bohr.md','39.3',1290,1300],
 ['laser','04-laser.md','39.4',1300,1302],
 ['pho-lien-tuc','05-pho-lien-tuc.md','39.5',1303,1308],
 ['bat-dinh-vat-chat','06-bat-dinh-vat-chat.md','39.6',1308,1310]
]
const endFiles=['07-luyen-tap-huong-dan.md','08-cau-hoi-thao-luan.md','09-bai-tap-01-15.md','10-bai-tap-16-30.md','11-bai-tap-31-45.md','12-bai-tap-46-60.md','13-bai-tap-61-75.md','14-bai-tap-76-87.md','15-mcat.md','16-bai-tap-cau-noi.md']
const presentEnd=[]
for(const name of endFiles){
 try{await access(raw+'/'+name);presentEnd.push(name)}catch(error){if(error.code!=='ENOENT')throw error}
}
if(complete){
 assert.equal(presentEnd.length,endFiles.length,'All exercise fragments must exist before readiness')
 const accepted=JSON.parse(await readFile('qa/physics/chapter39/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed')
 assert.equal(accepted.endSolutions,126)
 assert.equal(accepted.examples,10)
 assert.equal(accepted.sourceReviewed,true)
}
for(const file of ['00-mo-dau.md',...pages.map(p=>p[1]),'17-tom-tat.md'])await readFile(raw+'/'+file,'utf8')
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['cong-nang-luong','dong-luong-vat-ly','momen-dong-luong','song','nhieu-xa-anh-sang','electron-volt','photon','dong-luong-tuong-doi','nang-luong-nghi','nhiet-do-tuyet-doi']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=Object.keys(matterWavesConcepts)
lesson.topicGroups=matterWavesTopics
lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const decl=ast.body.find(n=>n.declaration?.declarations?.some(d=>d.id.name==='physics2Course')).declaration.declarations.find(d=>d.id.name==='physics2Course').init
const props=Object.fromEntries(decl.properties.map(p=>[p.key.name??p.key.value,p.value]))
const target=props.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===39))
const slides=[...physics2Course.slides.filter(s=>s.note!==slug),...matterWavesSlides]
const indented=(value,base)=>JSON.stringify(value,null,2).split('\n').map((line,index)=>index?' '.repeat(base)+line:line).join('\n')
for(const edit of [{start:target.start,end:target.end,text:indented(lesson,4)},{start:props.slides.start,end:props.slides.end,text:indented(slides,2)}].sort((a,b)=>b.start-a.start)){
 source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
}
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const ref=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
const inc=name=>'<!--@include: ../../../'+raw+'/'+name+'-->\n\n'
await mkdir(dir+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end] of pages){
 const t=matterWavesTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 assert(t,topic)
 await writeFile(dir+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:t.title,description:t.question})+'\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+ref('mục '+section,start,end)+'\n')
}
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,description:'Sóng de Broglie, nguyên tử hạt nhân, mức năng lượng, mô hình Bohr, laser, bức xạ vật đen và bất định.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+inc('00-mo-dau.md')+'<TopicMap />\n\n'+inc('17-tom-tat.md')+'## Tài liệu tham khảo\n\n'+ref('chương 39',1279,1320)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Tính sóng của hạt">\n\n'+presentEnd.map(inc).join('')+'## Tài liệu tham khảo\n\n'+ref('chương 39',1312,1320)+'\n\n</div>\n'
await writeFile(dir+'/'+slug+'.md',chapter)
const path='raw_materials/physics/translation-manifest.json',manifest=JSON.parse(await readFile(path,'utf8')),ch=manifest.chapters.find(c=>c.chapter===39)
assert(ch)
ch.fragments=[
 {sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},
 ...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),
 {sourceUnit:'chapter-summary',file:raw+'/17-tom-tat.md',destination:'notes'},
 ...presentEnd.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))
].map(f=>({...f,status:complete?'authored-source-reviewed-render-pending':'authored-under-review'}))
ch.status=complete?'content-complete':'authored-under-review'
ch.pendingSourceUnits=complete?['final-source-image-and-browser-review']:endFiles.filter(file=>!presentEnd.includes(file)).map(file=>'end:'+file).concat('independent-source-numeric-and-browser-review')
await writeFile(path,JSON.stringify(manifest,null,2)+'\n')
console.log('Integrated chapter39: Six theory topics,12 slides; '+presentEnd.length+'/10 end fragments. Status='+lesson.status)
