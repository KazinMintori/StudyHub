import { readFile,writeFile,mkdir,access } from 'node:fs/promises'
import { parseAst } from 'rollup/parseAst'
import assert from 'node:assert/strict'
import { physics2Course } from '../docs/.vitepress/physics-courses.mjs'
import { quantumWaveTopics,quantumWaveSlides } from '../docs/.vitepress/physics-quantum-wave-course.mjs'
import { quantumWaveConcepts } from '../docs/.vitepress/physics-quantum-wave-foundations.mjs'
import { concepts } from '../docs/.vitepress/concepts.mjs'

const complete=process.argv.includes('--complete')
const raw='raw_materials/physics/translations/chapter-40',directory='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(item=>item.sourceChapter===40)),slug=lesson.slug
const topics=[
 ['ham-song-schrodinger','01-ham-song-schrodinger.md','40.1',1321,1331],
 ['hat-trong-hop','02-hat-trong-hop.md','40.2',1331,1336],
 ['gieng-the-huu-han','03-gieng-the.md','40.3',1336,1340],
 ['hang-rao-xuyen-ham','04-hang-rao-xuyen-ham.md','40.4',1340,1342],
 ['dao-dong-tu-dieu-hoa','05-dao-dong-tu-dieu-hoa.md','40.5',1343,1347],
 ['phep-do-luong-tu','06-phep-do-luong-tu.md','40.6',1347,1350],
]
const endFiles=['07-luyen-tap-huong-dan.md','08-cau-hoi-thao-luan.md','09-bai-tap-01-15.md','10-bai-tap-16-30.md','11-bai-tap-31-35.md','12-bai-tap-36-50.md','13-bai-tap-51-66.md','14-mcat.md','15-bai-tap-cau-noi.md']
const presentEnd=[]
for(const file of endFiles){
 try{await access(raw+'/'+file);presentEnd.push(file)}catch(error){if(error.code!=='ENOENT')throw error}
}
if(complete){
 assert.equal(presentEnd.length,endFiles.length)
 const accepted=JSON.parse(await readFile('qa/physics/chapter40/numeric-checks.json','utf8'))
 assert.equal(accepted.status,'passed')
 assert.equal(accepted.endSolutions,110)
 assert.equal(accepted.examples,8)
 assert.equal(accepted.sourceReviewed,true)
}
for(const file of ['00-mo-dau.md',...topics.map(row=>row[1]),'16-tom-tat.md'])await readFile(raw+'/'+file,'utf8')
lesson.status=complete?'ready':'draft'
lesson.prerequisites=['dao-ham','dao-ham-rieng','tich-phan','song','dao-dong-dieu-hoa','cong-nang-luong','dong-luong-vat-ly','photon','buoc-song-de-broglie']
for(const id of lesson.prerequisites)assert(concepts[id],id)
lesson.supportingConcepts=Object.keys(quantumWaveConcepts)
lesson.topicGroups=quantumWaveTopics
lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const declaration=ast.body.find(node=>node.declaration?.declarations?.some(item=>item.id.name==='physics2Course')).declaration.declarations.find(item=>item.id.name==='physics2Course').init
const properties=Object.fromEntries(declaration.properties.map(property=>[property.key.name??property.key.value,property.value]))
const target=properties.lessons.elements.find(element=>element.properties.some(property=>(property.key.name??property.key.value)==='sourceChapter'&&property.value.value===40))
const slides=[...physics2Course.slides.filter(item=>item.note!==slug),...quantumWaveSlides]
const indent=(value,spaces)=>JSON.stringify(value,null,2).split('\n').map((line,index)=>index?' '.repeat(spaces)+line:line).join('\n')
for(const edit of [{start:target.start,end:target.end,text:indent(lesson,4)},{start:properties.slides.start,end:properties.slides.end,text:indent(slides,2)}].sort((a,b)=>b.start-a.start)){
 source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
}
await writeFile(catalog,source)
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const reference=(section,start,end)=>'Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, '+section+', trang '+start+'–'+end+'.'
await mkdir(directory+'/'+slug,{recursive:true})
for(const [topic,file,section,start,end]of topics){
 const item=quantumWaveTopics.flatMap(group=>group.topics).find(item=>item.slug===topic)
 assert(item,topic)
 await writeFile(directory+'/'+slug+'/'+topic+'.md',front({course:'vat-ly-2',lecture:slug,topic,section:'topic',title:item.title,description:item.question})+'\n<!--@include: ../../../../'+raw+'/'+file+'-->\n\n## Tài liệu tham khảo\n\n'+reference('mục '+section,start,end)+'\n')
}
const include=file=>'<!--@include: ../../../'+raw+'/'+file+'-->\n\n'
let chapter=front({course:'vat-ly-2',lecture:slug,section:'lecture',title:lesson.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,description:'Hàm sóng, phương trình Schrödinger một chiều, hạt trong hộp, giếng hữu hạn, xuyên hầm, dao động tử và phép đo.'})
chapter+='\n<div class="lecture-notes-content">\n\n'+include('00-mo-dau.md')+'<TopicMap />\n\n'+include('16-tom-tat.md')+'## Tài liệu tham khảo\n\n'+reference('chương 40',1321,1359)+'\n\n</div>\n'
chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Hàm sóng">\n\n'+presentEnd.map(include).join('')+'## Tài liệu tham khảo\n\n'+reference('chương 40',1351,1359)+'\n\n</div>\n'
await writeFile(directory+'/'+slug+'.md',chapter)
const manifestPath='raw_materials/physics/translation-manifest.json',manifest=JSON.parse(await readFile(manifestPath,'utf8'))
const chapterEntry=manifest.chapters.find(item=>item.chapter===40)
assert(chapterEntry)
chapterEntry.fragments=[
 {sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},
 ...topics.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),
 {sourceUnit:'chapter-summary',file:raw+'/16-tom-tat.md',destination:'notes'},
 ...presentEnd.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))
].map(item=>({...item,status:complete?'authored-source-reviewed-render-pending':'authored-under-review'}))
chapterEntry.status=complete?'content-complete':'authored-under-review'
chapterEntry.pendingSourceUnits=complete?['final-source-image-and-browser-review']:endFiles.filter(file=>!presentEnd.includes(file)).map(file=>'end:'+file).concat('independent-source-numeric-and-browser-review')
await writeFile(manifestPath,JSON.stringify(manifest,null,2)+'\n')
console.log('Integrated chapter40: Six theory topics,12 slides; '+presentEnd.length+'/9 exercise fragments. Status='+lesson.status)
