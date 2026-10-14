import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {emWaveTopics,emWaveSlides} from '../docs/.vitepress/physics-emwave-course.mjs'
import {emWaveConcepts} from '../docs/.vitepress/physics-emwave-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'

const complete=process.argv.includes('--complete')
if(complete){
 const numeric=JSON.parse(await readFile('qa/physics/chapter32/numeric-checks.json','utf8'))
 assert.equal(numeric.status,'passed')
 assert.equal(numeric.endSolutions,82)
 assert.equal(numeric.examples,7)
}
const raw='raw_materials/physics/translations/chapter-32',dir='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(l=>l.sourceChapter===32)),slug=lesson.slug
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['dao-ham','dao-ham-rieng','tich-phan','tich-co-huong','dao-dong-dieu-hoa','song','pha-song','dong-luong-vat-ly','cong-nang-luong','dien-truong','tu-truong','thong-luong','dinh-luat-faraday','dong-dien-dich']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=Object.keys(emWaveConcepts)
lesson.topicGroups=emWaveTopics
lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const decl=ast.body.find(n=>n.declaration?.declarations?.some(d=>d.id.name==='physics2Course')).declaration.declarations.find(d=>d.id.name==='physics2Course').init
const props=Object.fromEntries(decl.properties.map(p=>[p.key.name??p.key.value,p.value]))
const target=props.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===32))
const slides=[...physics2Course.slides.filter(s=>s.note!==slug),...emWaveSlides]
for(const edit of [{start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)},{start:props.slides.start,end:props.slides.end,text:JSON.stringify(slides,null,2)}].sort((a,b)=>b.start-a.start))source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
await writeFile(catalog,source)
const pages=[
 ['maxwell-song-dien-tu','01-maxwell-song-dien-tu.md','32.1',1048,1052],
 ['song-phang-van-toc-anh-sang','02-song-phang-van-toc-anh-sang.md','32.2',1052,1057],
 ['song-hinh-sin','03-song-hinh-sin.md','32.3',1057,1061],
 ['nang-luong-dong-luong','04-nang-luong-dong-luong.md','32.4',1061,1066],
 ['song-dung-dien-tu','05-song-dung-dien-tu.md','32.5',1066,1069]
]
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const reference=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
const inc=file=>'<!--@include: ../../../'+raw+'/'+file+'-->\n\n'
await mkdir(dir+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=emWaveTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await readFile(raw+'/'+file,'utf8')
 await writeFile(dir+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:t.title,description:t.question})+'\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+reference('mục '+section,start,end)+'\n')
}
const exercises=['10-luyen-tap-huong-dan.md','11-cau-hoi-thao-luan.md','12-bai-tap-01-29.md','13-bai-tap-30-48.md','14-bai-tap-49-53.md','15-mcat.md','16-dap-so.md']
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,description:'Maxwell, sóng phẳng, sóng hình sin, năng lượng, động lượng, áp suất bức xạ và sóng đứng.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+inc('00-mo-dau.md')+'<TopicMap />\n\n'+inc('09-tom-tat.md')+'## Tài liệu tham khảo\n\n'+reference('chương 32',1048,1076)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Sóng điện từ">\n\n'+exercises.map(inc).join('')+'## Tài liệu tham khảo\n\n'+reference('chương 32',1070,1076)+'\n\n- ICNIRP, [Statement on the Guidelines for Limiting Exposure to Time-Varying Electric, Magnetic, and Electromagnetic Fields](https://www.icnirp.org/cms/upload/publications/ICNIRPStatementEMF.pdf), *Health Physics* 97(3), 257–258 (2009).\n- ICNIRP, [Guidelines for Limiting Exposure to Time-Varying Electric and Magnetic Fields (1 Hz to 100 kHz)](https://www.icnirp.org/cms/upload/publications/ICNIRPLFgdl.pdf), *Health Physics* 99(6), 818–836 (2010).\n\n</div>\n'
await writeFile(dir+'/'+slug+'.md',chapter)
const path='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(path,'utf8')),ch=m.chapters.find(c=>c.chapter===32)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/09-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:complete?'authored-source-reviewed-render-pending':'authored-under-review'}))
ch.status=complete?'content-complete':'authored-under-review'
ch.pendingSourceUnits=['direct-browser-render-review']
await writeFile(path,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter32: Five topics,10 slides,82 end solutions. Status='+lesson.status)
