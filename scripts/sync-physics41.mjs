import {readFile,writeFile,mkdir,access} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {atomicStructureTopics,atomicStructureSlides} from '../docs/.vitepress/physics-atomic-structure-course.mjs'
import {atomicStructureConcepts} from '../docs/.vitepress/physics-atomic-structure-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'

const complete=process.argv.includes('--complete')
const raw='raw_materials/physics/translations/chapter-41',directory='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(item=>item.sourceChapter===41)),slug=lesson.slug
const topics=[
 ['schrodinger-ba-chieu','01-schrodinger-ba-chieu.md','41.1',1360,1362],
 ['hop-ba-chieu','02-hop-ba-chieu.md','41.2',1362,1367],
 ['nguyen-tu-hydro','03-nguyen-tu-hydro.md','41.3',1367,1375],
 ['hieu-ung-zeeman','04-hieu-ung-zeeman.md','41.4',1375,1378],
 ['spin-electron','05-spin-electron.md','41.5',1378,1385],
 ['nguyen-tu-nhieu-electron','06-nguyen-tu-nhieu-electron.md','41.6',1385,1392],
 ['pho-tia-x','07-pho-tia-x.md','41.7',1392,1395],
 ['roi-luong-tu','08-roi-luong-tu.md','41.8',1395,1398],
]
const endFiles=['09-luyen-tap-huong-dan.md','10-cau-hoi-thao-luan.md','11-bai-tap-01-22.md',
 '12-bai-tap-23-38.md','13-bai-tap-39-54.md','14-bai-tap-55-69.md','15-mcat.md','16-bai-tap-cau-noi.md']
const present=[]
for(const file of endFiles){
 try{await access(raw+'/'+file);present.push(file)}catch(error){if(error.code!=='ENOENT')throw error}
}
for(const file of ['00-mo-dau.md',...topics.map(row=>row[1]),'17-tom-tat.md'])await readFile(raw+'/'+file,'utf8')
if(complete){
 const accepted=JSON.parse(await readFile('qa/physics/chapter41/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed')
 assert.equal(accepted.endSolutions,111)
 assert.equal(accepted.examples,11)
 assert.equal(accepted.sourceReviewed,true)
 assert.equal(accepted.browserReview,'passed')
 assert.equal(present.length,endFiles.length)
}
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['dao-ham-rieng','tich-phan','ham-song-luong-tu','phuong-trinh-schrodinger',
 'hat-trong-hop-luong-tu','dao-dong-tu-dieu-hoa-luong-tu','phep-do-luong-tu',
 'dinh-luat-gauss','luong-cuc-tu','song-dung-dien-tu','mo-hinh-bohr','photon']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=Object.keys(atomicStructureConcepts)
lesson.topicGroups=atomicStructureTopics
lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const declaration=ast.body.find(node=>node.declaration?.declarations?.some(item=>item.id.name==='physics2Course')).declaration.declarations.find(item=>item.id.name==='physics2Course').init
const properties=Object.fromEntries(declaration.properties.map(property=>[property.key.name??property.key.value,property.value]))
const target=properties.lessons.elements.find(element=>element.properties.some(property=>(property.key.name??property.key.value)==='sourceChapter'&&property.value.value===41))
const slides=[...physics2Course.slides.filter(item=>item.note!==slug),...atomicStructureSlides]
const indent=(value,spaces)=>JSON.stringify(value,null,2).split('\n').map((line,index)=>index?' '.repeat(spaces)+line:line).join('\n')
for(const edit of [{start:target.start,end:target.end,text:indent(lesson,4)},{start:properties.slides.start,end:properties.slides.end,text:indent(slides,2)}].sort((a,b)=>b.start-a.start)){
 source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
}
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const reference=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
await mkdir(directory+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of topics){
 const item=atomicStructureTopics.flatMap(group=>group.topics).find(item=>item.slug===topic)
 assert(item,topic)
 await writeFile(directory+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:item.title,description:item.question})+
  '\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+reference('mục '+section,start,end)+'\n')
}
const include=file=>'<!--@include: ../../../'+raw+'/'+file+'-->\n\n'
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,
 prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,
 description:'Phương trình ba chiều, hộp lượng tử, hydro, Zeeman, spin, Pauli, phổ tia X và rối lượng tử.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+include('00-mo-dau.md')+'<TopicMap />\n\n'+
 include('17-tom-tat.md')+'## Tài liệu tham khảo\n\n'+reference('chương 41',1360,1407)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Cấu trúc nguyên tử">\n\n'+
 present.map(include).join('')+'## Tài liệu tham khảo\n\n'+reference('chương 41',1400,1407)+'\n\n</div>\n'
await writeFile(directory+'/'+slug+'.md',chapter)
const manifestPath='raw_materials/physics/translation-manifest.json',manifest=JSON.parse(await readFile(manifestPath,'utf8'))
const entry=manifest.chapters.find(item=>item.chapter===41);assert(entry)
entry.fragments=[
 {sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},
 ...topics.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),
 {sourceUnit:'chapter-summary',file:raw+'/17-tom-tat.md',destination:'notes'},
 ...present.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'})),
].map(item=>({...item,status:complete?'authored-source-reviewed':'authored-under-review'}))
entry.status=complete?'complete':'authored-under-review'
entry.pendingSourceUnits=complete?[]:endFiles.filter(file=>!present.includes(file)).map(file=>'end:'+file).concat('independent-source-numeric-and-browser-review')
if(complete)entry.completionReview='raw_materials/physics/chapter-41-review.json'
await writeFile(manifestPath,JSON.stringify(manifest,null,2)+'\n')
console.log('Integrated chapter41: Eight topics,12slides,'+present.length+'/8end fragments. Status='+lesson.status)
