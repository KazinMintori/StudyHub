// Integrate reviewed source fragments. Never infer completeness from file counts.
import {readFile,writeFile,mkdir,access} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics1Course} from '../docs/.vitepress/physics-courses.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
import {publishedPhysicsExerciseChapters} from './content/physics-exercise-config.mjs'

const chapters=process.argv.slice(2).filter(x=>/^\d+$/.test(x)).map(Number)
assert(chapters.length,'Pass explicit chapter numbers')
assert(chapters.every(n=>[1,3,4,5,6,7,8,12,13,14,15,16].includes(n)),'Not a remaining chapter')
const complete=process.argv.includes('--complete')
const pad=n=>String(n).padStart(2,'0')
const front=data=>'---\n'+Object.entries(data).map(([k,v])=>k+': '+JSON.stringify(v)).join('\n')+'\n---\n\n'
const catalogPath='docs/.vitepress/physics-courses.mjs'
let catalog=await readFile(catalogPath,'utf8')
const ast=parseAst(catalog)
const object=ast.body.flatMap(n=>n.declaration?.declarations||[]).find(d=>d.id.name==='physics1Course').init
const properties=Object.fromEntries(object.properties.map(p=>[p.key.name??p.key.value,p.value]))
const edits=[]
let slides=physics1Course.slides.filter(s=>!chapters.some(n=>physics1Course.lessons.find(l=>l.sourceChapter===n).slug===s.note))
const manifestPath='raw_materials/physics/translation-manifest.json'
const manifest=JSON.parse(await readFile(manifestPath,'utf8'))
for(const n of chapters){
 const nn=pad(n),entry=manifest.chapters.find(c=>c.chapter===n)
 const data=(await import(`../docs/.vitepress/physics1-remaining-ch${nn}.mjs`))[`physics1RemainingChapter${n}`]
 const old=physics1Course.lessons.find(l=>l.sourceChapter===n),raw=`raw_materials/physics/translations/chapter-${nn}`
 assert(data&&old&&entry,n)
 assert.equal(data.topics.length,entry.sections.length,'Every original section needs a destination')
 assert(data.cheatsheet?.sections?.length,'Missing reviewed formula sheet')
 for(const id of [...data.prerequisites,...data.supportingConcepts])assert(concepts[id],'Unknown concept: '+id)
 const coverage=JSON.parse(await readFile(`raw_materials/physics/reviews/ch${nn}-remaining-exercises-coverage.json`,'utf8'))
 const exercise=coverage.exerciseConfig
 assert(exercise&&exercise.files?.length&&exercise.numbered>0,'Parent must record reconciled exerciseConfig in coverage before integration')
 const topicFiles=data.topics.map(t=>t.file)
 const openingFile=data.openingFile||'00-mo-dau.md'
 const summaryFile=data.summaryFile||(n===1?'11-tom-tat.md':'17-tom-tat.md')
 const files=[openingFile,...topicFiles,summaryFile,...exercise.files.map(([,f])=>f),...(data.answerFile?[data.answerFile]:[])]
 const contents=await Promise.all(files.map(f=>readFile(raw+'/'+f,'utf8')))
 if(complete){
  assert(publishedPhysicsExerciseChapters.includes(n),'GitHub must generate this chapter exercise index before marking ready')
  const gate=JSON.parse(await readFile(`qa/physics1-remaining/ch${nn}/completion-gate.json`,'utf8'))
  assert(gate.status==='passed'&&gate.sourceReviewed===true&&gate.numericReview==='passed'&&gate.browserReview==='passed','All independent review gates required')
  for(const [i,file]of files.entries())assert.equal(createHash('sha256').update(contents[i]).digest('hex'),gate.reviewedFileHashes[raw+'/'+file],'File changed after review: '+file)
 }
 const groups=[{title:old.title,topics:data.topics.map(({file,...topic})=>topic)}]
 const lesson={...old,prerequisites:data.prerequisites,supportingConcepts:data.supportingConcepts,topicGroups:groups,hasChapterExercises:true,status:complete?'ready':'draft'}
 const target=properties.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===n))
 assert(target)
 edits.push({start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)})
 // Internal legacy catalog records keep authoring validators compatible. The
 // application no longer exports or renders a Slides tab or presentation view.
 slides.push(...data.cheatsheet.sections.map(s=>({note:old.slug,title:s.title,bullets:s.items?.map(i=>i.description).filter(Boolean).slice(0,4)||[],formula:s.items?.find(i=>i.formula)?.formula||s.items?.find(i=>i.formulaRows?.length)?.formulaRows[0].formula||''})))
 const directory='docs/vat-ly-1/bai-giang/'+old.slug
 await mkdir(directory,{recursive:true})
 for(const t of data.topics){
  assert(/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(t.slug),'Invalid topic slug')
  const extraReferences=(data.topicReferences?.[t.source]||[]).map(reference=>`\n[${reference.title}](${reference.url}).\n`).join('')
  await writeFile(directory+'/'+t.slug+'.md',front({course:'vat-ly-1',lecture:old.slug,topic:t.slug,section:'topic',title:t.title,description:t.question})+`<!--@include: ../../../../${raw}/${t.file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${t.source}.\n`+extraReferences)
 }
 const inc=file=>`<!--@include: ../../../${raw}/${file}-->\n\n`
 let main=front({course:'vat-ly-1',lecture:old.slug,section:'lecture',title:old.title,prerequisites:lesson.prerequisites,lessonStatus:lesson.status,hasChapterExercises:true,sourceTranslation:'full',description:data.topics.map(t=>t.title).join(', ')+'.'})
 main+='<div class="lecture-notes-content">\n\n'+inc(openingFile)+'<TopicMap />\n\n'+inc(summaryFile)+'## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương '+n+'.\n\n</div>\n\n'
 main+='<div class="lecture-exercises-content" aria-label="Bài tập cuối chương '+old.title+'">\n\n<ChapterExercises :chapter="'+n+'" />\n\n'+(data.answerFile?inc(data.answerFile):'')+'## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương '+n+'.\n\n</div>\n'
 await writeFile(directory+'.md',main)
 entry.status=complete?'complete':'authored-under-review'
 entry.fragments=files.map(file=>({sourceUnit:data.topics.find(t=>t.file===file)?.source??file.replace(/\.md$/,''),file:raw+'/'+file,destination:exercise.files.some(([,f])=>f===file)||file===data.answerFile?'bai-tap':topicFiles.includes(file)?'topic':'notes',status:complete?'source-reviewed-and-render-verified':'draft-under-review'}))
 entry.pendingSourceUnits=complete?[]:['independent-source-numeric-and-browser-review']
 if(complete)entry.completionReview=`raw_materials/physics/chapter-${nn}-review.json`
 console.log('Integrated chapter',n,'as',lesson.status)
}
edits.push({start:properties.slides.start,end:properties.slides.end,text:JSON.stringify(slides,null,2)})
for(const edit of edits.sort((a,b)=>b.start-a.start))catalog=catalog.slice(0,edit.start)+edit.text+catalog.slice(edit.end)
await writeFile(catalogPath,catalog)
await writeFile(manifestPath,JSON.stringify(manifest,null,2)+'\n')
