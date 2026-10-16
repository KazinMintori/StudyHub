import {readFile,writeFile,mkdir,access} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {particlesCosmologyTopics,particlesCosmologySlides} from '../docs/.vitepress/physics-particles-cosmology-course.mjs'
import {particlesCosmologyConcepts} from '../docs/.vitepress/physics-particles-cosmology-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'

const complete=process.argv.includes('--complete')
const raw='raw_materials/physics/translations/chapter-44',directory='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(item=>item.sourceChapter===44)),slug=lesson.slug
const topics=[
 ['lich-su-hat-co-ban','01-lich-su-hat-co-ban.md','44.1',1483,1488],
 ['may-gia-toc-va-detector','02-may-gia-toc-va-detector.md','44.2',1488,1492],
 ['hat-va-tuong-tac','03-hat-va-tuong-tac.md','44.3',1492,1498],
 ['quark-va-gluon','04-quark-va-gluon.md','44.4',1499,1502],
 ['mo-hinh-chuan','05-mo-hinh-chuan.md','44.5',1502,1505],
 ['vu-tru-gian-no','06-vu-tru-gian-no.md','44.6',1505,1511],
 ['khoi-dau-thoi-gian','07-khoi-dau-thoi-gian.md','44.7',1511,1518],
]
const endFiles=['09-luyen-tap-huong-dan.md','10-cau-hoi-thao-luan.md','11-bai-tap-01-30.md',
 '12-bai-tap-31-45.md','13-bai-tap-46-56.md','15-mcat.md','16-bai-tap-cau-noi.md']

const present=[]
for(const file of endFiles){
 try{await access(raw+'/'+file);present.push(file)}catch(error){if(error.code!=='ENOENT')throw error}
}
for(const file of ['00-mo-dau.md',...topics.map(row=>row[1]),'17-tom-tat.md'])await readFile(raw+'/'+file,'utf8')
if(complete){
 const accepted=JSON.parse(await readFile('qa/physics/chapter44/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed')
 assert.equal(accepted.endSolutions,85)
 assert.equal(accepted.examples,12)
 assert.equal(accepted.sourceReviewed,true)
 assert.equal(accepted.browserReview,'passed')
 assert.equal(present.length,endFiles.length)
}
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['thuyet-tuong-doi-hep','photon','phan-ra-phong-xa','nhiet-do-tuyet-doi',
 'dong-luong-vat-ly','chuyen-dong-hat-trong-tu-truong','spin-luong-tu','nguyen-ly-pauli','dao-ham','tich-phan']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=Object.keys(particlesCosmologyConcepts)
lesson.topicGroups=particlesCosmologyTopics
lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const declaration=ast.body.find(node=>node.declaration?.declarations?.some(item=>item.id.name==='physics2Course')).declaration.declarations.find(item=>item.id.name==='physics2Course').init
const properties=Object.fromEntries(declaration.properties.map(property=>[property.key.name??property.key.value,property.value]))
const target=properties.lessons.elements.find(element=>element.properties.some(property=>(property.key.name??property.key.value)==='sourceChapter'&&property.value.value===44))
const slides=[...physics2Course.slides.filter(item=>item.note!==slug),...particlesCosmologySlides]
const indent=(value,spaces)=>JSON.stringify(value,null,2).split('\n').map((line,index)=>index?' '.repeat(spaces)+line:line).join('\n')
for(const edit of [{start:target.start,end:target.end,text:indent(lesson,4)},{start:properties.slides.start,end:properties.slides.end,text:indent(slides,2)}].sort((a,b)=>b.start-a.start)){
 source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
}
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const reference=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
await mkdir(directory+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of topics){
 const item=particlesCosmologyTopics.flatMap(group=>group.topics).find(item=>item.slug===topic)
 assert(item,topic)
 await writeFile(directory+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:item.title,description:item.question})+
  '\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+reference('mục '+section,start,end)+'\n'+
  (section==='44.1'?'\n- [National Cancer Institute: Fludeoxyglucose F 18](https://www.cancer.gov/publications/dictionaries/cancer-drug/def/fludeoxyglucose-f-18).\n- [PubChem: Fludeoxyglucose (18F)](https://pubchem.ncbi.nlm.nih.gov/compound/Fludeoxyglucose-_18F).\n':'')+
  (section==='44.4'?'\n- [Fermilab: Discovery of the Bottom Quark](https://www.fnal.gov/pub/inquiring/physics/discoveries/bottom_quark.html).\n':''))
}
const include=file=>'<!--@include: ../../../'+raw+'/'+file+'-->\n\n'
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,
 prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,
 description:'Phản hạt, máy gia tốc, tương tác, quark, mô hình chuẩn, vũ trụ giãn nở và lịch sử vũ trụ sơ khai.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+include('00-mo-dau.md')+'<TopicMap />\n\n'+
 include('17-tom-tat.md')+'## Tài liệu tham khảo\n\n'+reference('chương 44',1483,1524)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Vật lý hạt và vũ trụ học">\n\n'+
 present.map(include).join('')+'## Tài liệu tham khảo\n\n'+reference('chương 44',1520,1524)+'\n\n</div>\n'
await writeFile(directory+'/'+slug+'.md',chapter)
const manifestPath='raw_materials/physics/translation-manifest.json',manifest=JSON.parse(await readFile(manifestPath,'utf8'))
const entry=manifest.chapters.find(item=>item.chapter===44);assert(entry)
entry.fragments=[
 {sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},
 ...topics.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),
 {sourceUnit:'chapter-summary',file:raw+'/17-tom-tat.md',destination:'notes'},
 ...present.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'})),
].map(item=>({...item,status:complete?'authored-source-reviewed':'authored-under-review'}))
entry.status=complete?'complete':'authored-under-review'
entry.pendingSourceUnits=complete?[]:endFiles.filter(file=>!present.includes(file)).map(file=>'end:'+file).concat('independent-source-numeric-and-browser-review')
if(complete)entry.completionReview='raw_materials/physics/chapter-44-review.json'
await writeFile(manifestPath,JSON.stringify(manifest,null,2)+'\n')
console.log('Integrated chapter44: Seven topics,12slides,'+present.length+'/7end fragments. Status='+lesson.status)
