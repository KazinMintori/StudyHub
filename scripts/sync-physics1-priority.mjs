import{readFile,writeFile,mkdir,readdir,access}from'node:fs/promises'
import{parseAst}from'rollup/parseAst'
import assert from'node:assert/strict'
import{physics1PriorityCourseData as data}from'../docs/.vitepress/physics1-priority-course.mjs'
import{physics1Course}from'../docs/.vitepress/physics-courses.mjs'
import{concepts}from'../docs/.vitepress/concepts.mjs'
import{publishedPhysicsExerciseChapters,physicsExerciseConfigs}from'./content/physics-exercise-config.mjs'
const complete=process.argv.includes('--complete')
const selected=process.argv.slice(2).filter(x=>/^\d+$/.test(x)).map(Number)
const chapters=selected.length?selected:Object.keys(data).map(Number)
const limits={9:95,10:97,11:95,17:119,18:87,19:66,20:62}
const front=d=>['---',...Object.entries(d).map(([k,v])=>k+': '+JSON.stringify(v)),'---',''].join('\n')
const present=async p=>{try{await access(p);return true}catch(e){if(e.code==='ENOENT')return false;throw e}}
const catalogPath='docs/.vitepress/physics-courses.mjs'
let catalog=await readFile(catalogPath,'utf8')
const ast=parseAst(catalog)
const object=ast.body.flatMap(n=>n.declaration?.declarations||[]).find(d=>d.id.name==='physics1Course').init
const properties=Object.fromEntries(object.properties.map(p=>[p.key.name??p.key.value,p.value]))
const edits=[],allSlides=physics1Course.slides.filter(s=>!chapters.some(n=>data[n].slug===s.note))
const manifestPath='raw_materials/physics/translation-manifest.json'
const manifest=JSON.parse(await readFile(manifestPath,'utf8'))
for(const n of chapters){
 assert(data[n],n)
 const d=data[n],raw=`raw_materials/physics/translations/chapter-${String(n).padStart(2,'0')}`,directory='docs/vat-ly-1/bai-giang'
 const old=physics1Course.lessons.find(l=>l.sourceChapter===n);assert(old)
 const entry=manifest.chapters.find(c=>c.chapter===n)
 const theory=d.topics.map((t,i)=>({...t,file:`${String(i+1).padStart(2,'0')}-${t.slug}.md`,sourceId:`${n}.${i+1}`}))
 // Chapter 10 was already assigned as 1–75 and 76–97. Preserve ownership.
 const half=n===10?75:Math.ceil(limits[n]/2)
 const end=['09-luyen-tap-huong-dan.md','10-cau-hoi-thao-luan.md',`11-bai-tap-001-${String(half).padStart(3,'0')}.md`,`12-bai-tap-${String(half+1).padStart(3,'0')}-${String(limits[n]).padStart(3,'0')}.md`,'16-bai-tap-cau-noi.md']
 const files=['00-mo-dau.md',...theory.map(t=>t.file),'17-tom-tat.md',...end]
 const available=[];for(const f of files)if(await present(raw+'/'+f))available.push(f)
 if(complete){
  if(physicsExerciseConfigs[n])assert(publishedPhysicsExerciseChapters.includes(n),'Exercise groups must be enabled for GitHub before marking ready')
  const gate=JSON.parse(await readFile(`qa/physics1-priority/chapter-${String(n).padStart(2,'0')}/completion-gate.json`,'utf8'))
  assert(gate.status==='passed'&&gate.sourceReviewed===true&&gate.browserReview==='passed'&&gate.numericReview==='passed',n)
  assert.equal(available.length,files.length)
 }
 const lesson={...old,status:complete?'ready':'draft',prerequisites:d.prerequisites,supportingConcepts:d.supportingConcepts,topicGroups:d.topicGroups,hasChapterExercises:true}
 for(const id of [...lesson.prerequisites,...lesson.supportingConcepts])assert(concepts[id],id)
 const target=properties.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===n));assert(target)
 edits.push({start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)})
 allSlides.push(...d.slides)
 await mkdir(directory+'/'+d.slug,{recursive:true})
 for(const t of theory){
  if(!available.includes(t.file))continue
  const section=entry.sections.find(s=>s.id===t.sourceId);assert(section)
  const ref='Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục '+t.sourceId+'.'
  await writeFile(directory+'/'+d.slug+'/'+t.slug+'.md',front({course:'vat-ly-1',lecture:d.slug,section:'topic',topic:t.slug,title:t.title,description:t.question})+`\n<!--@include: ../../../../${raw}/${t.file}-->\n\n## Tài liệu tham khảo\n\n${ref}\n`+
   (n===17&&t.sourceId==='17.3'?'\n[BIPM: Kelvin](https://www.bipm.org/en/si-base-units/kelvin).\n':'')+
   (n===17&&t.sourceId==='17.6'?'\n[Particle Data Group: Tính chất của đồng](https://pdg.lbl.gov/2008/AtomicNuclearProperties/HTML_PAGES/029.html).\n':'')+
   (n===17&&t.sourceId==='17.7'?'\n[NASA: What Is the Greenhouse Effect?](https://science.nasa.gov/climate-change/faq/what-is-the-greenhouse-effect/).\n':''))
 }
 const inc=f=>available.includes(f)?`<!--@include: ../../../${raw}/${f}-->\n\n`:''
 let chapter=front({course:'vat-ly-1',lecture:d.slug,section:'lecture',title:old.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,sourceTranslation:'full',description:d.topics.map(t=>t.title).join(', ')+'.'})
 chapter+='\n<div class="lecture-notes-content">\n\n'+inc('00-mo-dau.md')+'<TopicMap />\n\n'+inc('17-tom-tat.md')+'## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương '+n+'.\n\n</div>\n'
 chapter+='\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương '+old.title+'">\n\n'+(physicsExerciseConfigs[n]?'<ChapterExercises :chapter="'+n+'" />\n\n':end.map(inc).join(''))+'## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương '+n+'.\n\n</div>\n'
 await writeFile(directory+'/'+d.slug+'.md',chapter)
 entry.status=complete?'complete':'authored-under-review'
 entry.fragments=available.map(file=>({sourceUnit:theory.find(t=>t.file===file)?.sourceId??file.replace(/\.md$/,''),file:raw+'/'+file,destination:end.includes(file)?'bai-tap':theory.some(t=>t.file===file)?'topic:'+theory.find(t=>t.file===file).slug:'notes',status:complete?'source-reviewed-and-render-verified':'draft-under-review'}))
 entry.pendingSourceUnits=complete?[]:files.filter(f=>!available.includes(f)).concat('independent-source-numeric-and-browser-review')
 if(complete)entry.completionReview=`raw_materials/physics/chapter-${String(n).padStart(2,'0')}-review.json`
 console.log(`Integrated draft chapter${n}: ${available.length}/${files.length}fragments; status=${lesson.status}`)
}
edits.push({start:properties.slides.start,end:properties.slides.end,text:JSON.stringify(allSlides,null,2)})
for(const e of edits.sort((a,b)=>b.start-a.start))catalog=catalog.slice(0,e.start)+e.text+catalog.slice(e.end)
await writeFile(catalogPath,catalog)
await writeFile(manifestPath,JSON.stringify(manifest,null,2)+'\n')
