import {readFile,writeFile,mkdir,access} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {moleculesTopics,moleculesSlides} from '../docs/.vitepress/physics-molecules-course.mjs'
import {moleculesConcepts} from '../docs/.vitepress/physics-molecules-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'

const complete=process.argv.includes('--complete')
const raw='raw_materials/physics/translations/chapter-42',directory='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(item=>item.sourceChapter===42)),slug=lesson.slug
const topics=[
 ['lien-ket-phan-tu','01-lien-ket-phan-tu.md','42.1',1408,1411],
 ['pho-phan-tu','02-pho-phan-tu.md','42.2',1411,1415],
 ['cau-truc-chat-ran','03-cau-truc-chat-ran.md','42.3',1415,1418],
 ['dai-nang-luong','04-dai-nang-luong.md','42.4',1418,1421],
 ['mo-hinh-electron-tu-do','05-mo-hinh-electron-tu-do.md','42.5',1421,1425],
 ['chat-ban-dan','06-chat-ban-dan.md','42.6',1425,1428],
 ['thiet-bi-ban-dan','07-thiet-bi-ban-dan.md','42.7',1428,1433],
 ['sieu-dan','08-sieu-dan.md','42.8',1433,1433],
]
const endFiles=['09-luyen-tap-huong-dan.md','10-cau-hoi-thao-luan.md','11-bai-tap-01-22.md',
 '12-bai-tap-23-38.md','13-bai-tap-39-50.md','14-bai-tap-51-55.md','15-mcat.md','16-bai-tap-cau-noi.md']

const present=[]
for(const file of endFiles){
 try{await access(raw+'/'+file);present.push(file)}catch(error){if(error.code!=='ENOENT')throw error}
}
for(const file of ['00-mo-dau.md',...topics.map(row=>row[1]),'17-tom-tat.md'])await readFile(raw+'/'+file,'utf8')
if(complete){
 const accepted=JSON.parse(await readFile('qa/physics/chapter42/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed')
 assert.equal(accepted.endSolutions,95)
 assert.equal(accepted.examples,9)
 assert.equal(accepted.sourceReviewed,true)
 assert.equal(accepted.browserReview,'passed')
 assert.equal(present.length,endFiles.length)
}
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['nguyen-ly-pauli','cau-hinh-electron','dao-dong-tu-dieu-hoa-luong-tu',
 'ham-song-luong-tu','hat-trong-hop-ba-chieu','photon','nhiet-do-tuyet-doi','tich-phan','dien-truong']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=Object.keys(moleculesConcepts)
lesson.topicGroups=moleculesTopics
lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const declaration=ast.body.find(node=>node.declaration?.declarations?.some(item=>item.id.name==='physics2Course')).declaration.declarations.find(item=>item.id.name==='physics2Course').init
const properties=Object.fromEntries(declaration.properties.map(property=>[property.key.name??property.key.value,property.value]))
const target=properties.lessons.elements.find(element=>element.properties.some(property=>(property.key.name??property.key.value)==='sourceChapter'&&property.value.value===42))
const slides=[...physics2Course.slides.filter(item=>item.note!==slug),...moleculesSlides]
const indent=(value,spaces)=>JSON.stringify(value,null,2).split('\n').map((line,index)=>index?' '.repeat(spaces)+line:line).join('\n')
for(const edit of [{start:target.start,end:target.end,text:indent(lesson,4)},{start:properties.slides.start,end:properties.slides.end,text:indent(slides,2)}].sort((a,b)=>b.start-a.start)){
 source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
}
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const reference=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
await mkdir(directory+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of topics){
 const item=moleculesTopics.flatMap(group=>group.topics).find(item=>item.slug===topic)
 assert(item,topic)
 await writeFile(directory+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:item.title,description:item.question})+
  '\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+reference('mục '+section,start,end)+'\n')
}
const include=file=>'<!--@include: ../../../'+raw+'/'+file+'-->\n\n'
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,
 prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,
 description:'Liên kết và phổ phân tử, cấu trúc tinh thể, dải năng lượng, electron tự do, bán dẫn và siêu dẫn.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+include('00-mo-dau.md')+'<TopicMap />\n\n'+
 include('17-tom-tat.md')+'## Tài liệu tham khảo\n\n'+reference('chương 42',1408,1441)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Phân tử và vật chất ngưng tụ">\n\n'+
 present.map(include).join('')+'## Tài liệu tham khảo\n\n'+reference('chương 42',1434,1441)+'\n\n</div>\n'
await writeFile(directory+'/'+slug+'.md',chapter)
const manifestPath='raw_materials/physics/translation-manifest.json',manifest=JSON.parse(await readFile(manifestPath,'utf8'))
const entry=manifest.chapters.find(item=>item.chapter===42);assert(entry)
entry.fragments=[
 {sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},
 ...topics.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),
 {sourceUnit:'chapter-summary',file:raw+'/17-tom-tat.md',destination:'notes'},
 ...present.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'})),
].map(item=>({...item,status:complete?'authored-source-reviewed':'authored-under-review'}))
entry.status=complete?'complete':'authored-under-review'
entry.pendingSourceUnits=complete?[]:endFiles.filter(file=>!present.includes(file)).map(file=>'end:'+file).concat('independent-source-numeric-and-browser-review')
if(complete)entry.completionReview='raw_materials/physics/chapter-42-review.json'
await writeFile(manifestPath,JSON.stringify(manifest,null,2)+'\n')
console.log('Integrated chapter42: Eight topics,12slides,'+present.length+'/8end fragments. Status='+lesson.status)
