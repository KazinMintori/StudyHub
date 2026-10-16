import {readFile,writeFile,mkdir,access} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {nuclearTopics,nuclearSlides} from '../docs/.vitepress/physics-nuclear-course.mjs'
import {nuclearConcepts} from '../docs/.vitepress/physics-nuclear-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'

const complete=process.argv.includes('--complete')
const raw='raw_materials/physics/translations/chapter-43',directory='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(item=>item.sourceChapter===43)),slug=lesson.slug
const topics=[
 ['tinh-chat-hat-nhan','01-tinh-chat-hat-nhan.md','43.1',1442,1447],
 ['nang-luong-lien-ket','02-nang-luong-lien-ket.md','43.2',1447,1452],
 ['on-dinh-va-phong-xa','03-on-dinh-va-phong-xa.md','43.3',1452,1459],
 ['hoat-do-va-chu-ky-ban-ra','04-hoat-do-va-chu-ky-ban-ra.md','43.4',1459,1463],
 ['tac-dung-sinh-hoc','05-tac-dung-sinh-hoc.md','43.5',1463,1466],
 ['phan-ung-hat-nhan','06-phan-ung-hat-nhan.md','43.6',1466,1468],
 ['phan-hach','07-phan-hach.md','43.7',1468,1472],
 ['nhiet-hach','08-nhiet-hach.md','43.8',1472,1474],
]
const endFiles=['09-luyen-tap-huong-dan.md','10-cau-hoi-thao-luan.md','11-bai-tap-01-32.md',
 '12-bai-tap-33-48.md','13-bai-tap-49-64.md','14-bai-tap-65-72.md','15-mcat.md','16-bai-tap-cau-noi.md']

const present=[]
for(const file of endFiles){
 try{await access(raw+'/'+file);present.push(file)}catch(error){if(error.code!=='ENOENT')throw error}
}
for(const file of ['00-mo-dau.md',...topics.map(row=>row[1]),'17-tom-tat.md'])await readFile(raw+'/'+file,'utf8')
if(complete){
 const accepted=JSON.parse(await readFile('qa/physics/chapter43/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed')
 assert.equal(accepted.endSolutions,110)
 assert.equal(accepted.examples,13)
 assert.equal(accepted.sourceReviewed,true)
 assert.equal(accepted.browserReview,'passed')
 assert.equal(present.length,endFiles.length)
}
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['photon','thuyet-tuong-doi-hep','cong-nang-luong','dong-luong-vat-ly',
 'spin-luong-tu','nguyen-ly-pauli','xuyen-ham-luong-tu','dao-ham','tich-phan']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=Object.keys(nuclearConcepts)
lesson.topicGroups=nuclearTopics
lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const declaration=ast.body.find(node=>node.declaration?.declarations?.some(item=>item.id.name==='physics2Course')).declaration.declarations.find(item=>item.id.name==='physics2Course').init
const properties=Object.fromEntries(declaration.properties.map(property=>[property.key.name??property.key.value,property.value]))
const target=properties.lessons.elements.find(element=>element.properties.some(property=>(property.key.name??property.key.value)==='sourceChapter'&&property.value.value===43))
const slides=[...physics2Course.slides.filter(item=>item.note!==slug),...nuclearSlides]
const indent=(value,spaces)=>JSON.stringify(value,null,2).split('\n').map((line,index)=>index?' '.repeat(spaces)+line:line).join('\n')
for(const edit of [{start:target.start,end:target.end,text:indent(lesson,4)},{start:properties.slides.start,end:properties.slides.end,text:indent(slides,2)}].sort((a,b)=>b.start-a.start)){
 source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
}
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const reference=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
await mkdir(directory+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of topics){
 const item=nuclearTopics.flatMap(group=>group.topics).find(item=>item.slug===topic)
 assert(item,topic)
 await writeFile(directory+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:item.title,description:item.question})+
  '\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+reference('mục '+section,start,end)+'\n'+
  (section==='43.4'?'\n- [NNDC: Potassium-40 decay data](https://www.nndc.bnl.gov/nudat3/getdecaydataset.jsp?dsid=40k+ec+decay+%281.248eP9+y%29&nucleus=40AR).\n':''))
}
const include=file=>'<!--@include: ../../../'+raw+'/'+file+'-->\n\n'
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,
 prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,
 description:'Thành phần và liên kết hạt nhân, các kênh phóng xạ, hoạt độ, tác dụng bức xạ, phản ứng, phân hạch và nhiệt hạch.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+include('00-mo-dau.md')+'<TopicMap />\n\n'+
 include('17-tom-tat.md')+'## Tài liệu tham khảo\n\n'+reference('chương 43',1442,1482)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Vật lý hạt nhân">\n\n'+
 present.map(include).join('')+'## Tài liệu tham khảo\n\n'+reference('chương 43',1476,1482)+'\n\n</div>\n'
await writeFile(directory+'/'+slug+'.md',chapter)
const manifestPath='raw_materials/physics/translation-manifest.json',manifest=JSON.parse(await readFile(manifestPath,'utf8'))
const entry=manifest.chapters.find(item=>item.chapter===43);assert(entry)
entry.fragments=[
 {sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},
 ...topics.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),
 {sourceUnit:'chapter-summary',file:raw+'/17-tom-tat.md',destination:'notes'},
 ...present.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'})),
].map(item=>({...item,status:complete?'authored-source-reviewed':'authored-under-review'}))
entry.status=complete?'complete':'authored-under-review'
entry.pendingSourceUnits=complete?[]:endFiles.filter(file=>!present.includes(file)).map(file=>'end:'+file).concat('independent-source-numeric-and-browser-review')
if(complete)entry.completionReview='raw_materials/physics/chapter-43-review.json'
await writeFile(manifestPath,JSON.stringify(manifest,null,2)+'\n')
console.log('Integrated chapter43: Eight topics,12slides,'+present.length+'/8end fragments. Status='+lesson.status)
