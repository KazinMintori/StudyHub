import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {acTopics,acSlides} from '../docs/.vitepress/physics-ac-course.mjs'
import {acConcepts,acWikiDetails,acWikiConnections} from '../docs/.vitepress/physics-ac-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'

const complete=process.argv.includes('--complete')
const numeric=JSON.parse(await readFile('qa/physics/chapter31/theory-numeric-checks.json','utf8'))
assert.equal(numeric.status,'passed')
assert.equal(Object.keys(numeric.examples).length,9)
if(complete){
 const bundle=JSON.parse(await readFile('qa/physics/chapter31/numeric-checks.json','utf8'))
 assert.equal(bundle.status,'passed')
 assert.equal(bundle.detailedSolutions,104)
}
const raw='raw_materials/physics/translations/chapter-31',dir='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(l=>l.sourceChapter===31))
const slug=lesson.slug
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['dao-ham','tich-phan','dao-dong-dieu-hoa','dien-tro','dien-dung','cuon-cam','quy-tac-kirchhoff','dinh-luat-faraday','ho-cam','dong-dien-dich','dien-ke','tu-tre']
lesson.supportingConcepts=Object.keys(acConcepts)
lesson.topicGroups=acTopics
lesson.hasChapterExercises=complete
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const decl=ast.body.find(n=>n.declaration?.declarations?.some(d=>d.id.name==='physics2Course')).declaration.declarations.find(d=>d.id.name==='physics2Course').init
const props=Object.fromEntries(decl.properties.map(p=>[p.key.name??p.key.value,p.value]))
const target=props.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===31))
const slides=[...physics2Course.slides.filter(s=>s.note!==slug),...acSlides]
const edits=[{start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)},{start:props.slides.start,end:props.slides.end,text:JSON.stringify(slides,null,2)}]
for(const edit of edits.sort((a,b)=>b.start-a.start))source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
await writeFile(catalog,source)
const pages=[
 ['gian-do-pha-hieu-dung','01-gian-do-pha-hieu-dung.md','31.1',1018,1021],
 ['dien-tro-dien-khang','02-dien-tro-dien-khang.md','31.2',1022,1026],
 ['mach-rlc-noi-tiep','03-mach-rlc-noi-tiep.md','31.3',1027,1030],
 ['cong-suat-xoay-chieu','04-cong-suat-xoay-chieu.md','31.4',1031,1033],
 ['cong-huong','05-cong-huong.md','31.5',1034,1036],
 ['may-bien-ap','06-may-bien-ap.md','31.6',1036,1039]
]
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const reference=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
const inc=file=>'<!--@include: ../../../'+raw+'/'+file+'-->\n\n'
await mkdir(dir+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=acTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(dir+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:t.title,description:t.question})+'\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+reference('mục '+section,start,end)+'\n')
}
const exercises=['10-luyen-tap-huong-dan.md','11-cau-hoi-thao-luan.md','12-bai-tap-01-36.md','13-bai-tap-37-65.md','15-nang-cao-mcat.md','16-dap-so.md']
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:complete,description:'Giản đồ pha, hiệu dụng, điện kháng, mạch RLC, công suất, cộng hưởng và máy biến áp.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+inc('00-mo-dau.md')+'<TopicMap />\n\n'+inc('09-tom-tat.md')+'## Tài liệu tham khảo\n\n'+reference('chương 31',1018,1047)+'\n\n</div>\n'
if(complete)chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Dòng điện xoay chiều">\n\n'+exercises.map(inc).join('')+'## Tài liệu tham khảo\n\n'+reference('chương 31',1041,1047)+'\n\n</div>\n'
await writeFile(dir+'/'+slug+'.md',chapter)
for(const [id,c]of Object.entries(acConcepts)){
 const detail=acWikiDetails[id].replace(/\n\nTài liệu tham khảo:[\s\S]*$/,'')
 const related=acWikiConnections[id].map(key=>{
  assert(concepts[key],key)
  return '- ['+concepts[key].name+'](./'+key+'.md)'
 }).join('\n')
 const page=front({title:c.name,wikiTerm:id,prev:false,next:false})+'\n# '+c.name+'\n\n'+c.definition+'\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n'+detail+'\n\n## Ví dụ\n\n'+c.example+'\n\n## Khi nào cần dùng?\n\n'+c.use+'\n\n## Câu hỏi ôn lại\n\n'+c.question+'\n\n<details><summary>Xem đáp án</summary>\n\n'+c.answer+'\n\n</details>\n\n## Thuật ngữ liên quan\n\n'+related+'\n\n## Tài liệu tham khảo\n\n'+reference('chương 31',1018,1040)+'\n'
 await writeFile('docs/wiki/'+id+'.md',page)
}
const path='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(path,'utf8')),ch=m.chapters.find(c=>c.chapter===31)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/09-tom-tat.md',destination:'notes'}].map(f=>({...f,status:'authored-source-reviewed-render-pending'}))
if(complete)ch.fragments.push(...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap',status:'authored-and-reviewed'})))
ch.status=complete?'content-complete':'theory-authored'
ch.pendingSourceUnits=complete?['direct-browser-render-review']:['guided-practice','bridging-problem','discussion-questions','exercises-31.1-31.65','challenge-31.66-31.68','mcat-31.69-31.72','odd-answers','direct-browser-render-review']
await writeFile(path,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter31 '+(complete?'complete content':'theory draft')+': six topics,11 slides,six Cheatsheet groups and10 Wiki entries.')
