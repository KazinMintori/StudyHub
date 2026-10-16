import {readFile,writeFile,mkdir,access} from 'node:fs/promises'
import path from 'node:path'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
import {cheatsheets} from '../docs/.vitepress/cheatsheets.mjs'
import {lectureParts} from '../docs/.vitepress/lecture-model.mjs'
import {courseCatalog} from '../docs/.vitepress/course-catalog.mjs'

const manifest=JSON.parse(await readFile('raw_materials/physics/translation-manifest.json','utf8'))
const exists=async f=>{try{await access(f);return true}catch{return false}}
async function expand(file,seen=new Set()) {
 if(seen.has(file))return ''
 seen.add(file)
 let text=(await readFile(file,'utf8')).replace(/^::: exercise (Q|VP)\s+(?=\d+\.)/gm,'::: exercise $1')
 for(const m of [...text.matchAll(/<!--@include:\s*([^>]+?)\s*-->/g)]) {
  const f=path.normalize(path.join(path.dirname(file),m[1]))
  text=text.replace(m[0],await exists(f)?await expand(f,seen):'MISSING_INCLUDE:'+f)
 }
 return text
}
const rows=[]
for(const course of [physics1Course,physics2Course])for(const lesson of course.lessons) {
 const ch=manifest.chapters.find(c=>c.chapter===lesson.sourceChapter)
 const mainFile=`docs/${course.id}/bai-giang/${lesson.slug}.md`
 const main=await expand(mainFile)
 const topics=(lesson.topicGroups||[]).flatMap(g=>g.topics)
 const texts=[main]
 for(const t of topics)texts.push(await expand(`docs/${course.id}/bai-giang/${lesson.slug}/${t.slug}.md`))
 const all=texts.join('\n')
 let source=''
 for(let p=ch.pdfStart;p<=ch.pdfEnd;p++)source+=await readFile(`qa/physics/full-source/pdf-${String(p).padStart(4,'0')}.txt`,'utf8')+'\n'
 const exercisesStart=source.search(/^EXERCISES\s*$/m)
 const endSource=exercisesStart>=0?source.slice(exercisesStart):source
 // Extracted PDF columns may put a problem number in the middle of a line.
 const sourceNumbers=[...endSource.matchAll(new RegExp(`(?<![\\w.])${ch.chapter}\\.(\\d{1,3})(?!\\d)`,'g'))].map(m=>Number(m[1])).filter(n=>n<=500)
 const expectedExercises=Math.max(0,...sourceNumbers)
 const prompts=[...all.matchAll(new RegExp(`^::: exercise ${ch.chapter}\\.(\\d+)(?:\\s|\\.|$)`,'gm'))].map(m=>Number(m[1]))
 const solutionBlocks=[...all.matchAll(/<!-- detailed-solution:([^>]+) -->\s*::: solution[^\n]*\n([\s\S]*?)\n:::/g)].map(m=>({id:m[1],body:m[2]}))
 // A valid collapsed solution does not require an invisible authoring marker.
 // Also inspect actual details containers following each numbered prompt.
 const exerciseText=main.includes('<div class="lecture-exercises-content"')?main.split('<div class="lecture-exercises-content"')[1]:all
 const htmlPromptPattern=new RegExp(`^### ((?:Q|VP)?${ch.chapter}\\.\\d+(?:\\.\\d+)?|Bài tập cầu nối)(?=\\s|$)[^\\n]*\\n`,'gm')
 const htmlPrompts=[...exerciseText.matchAll(htmlPromptPattern)]
 for(let i=0;i<htmlPrompts.length;i++){
  const prompt=htmlPrompts[i]
  const id=prompt[1]==='Bài tập cầu nối'?`Bài cầu nối ${ch.chapter}`:prompt[1]
  if(new RegExp(`^${ch.chapter}\\.\\d+$`).test(id)){
   const number=Number(id.split('.')[1])
   if(!prompts.includes(number))prompts.push(number)
  }
  const section=exerciseText.slice(prompt.index,htmlPrompts[i+1]?.index??exerciseText.length)
  const detail=section.match(/<details(?:\s[^>]*)?>\s*<summary>[^<]*<\/summary>([\s\S]*?)<\/details>/)
  if(detail&&!solutionBlocks.some(s=>s.id===id))solutionBlocks.push({id,body:detail[1]})
 }
 const promptPattern=`^::: exercise ((?:Bài )?(?:Q|VP)?${ch.chapter}\\.\\d+(?:\\.\\d+)?|Bài (?:cầu nối|tổng hợp) ${ch.chapter}(?:\\.\\d+)?)\\b[^\\n]*\\n`
 const promptBlocks=[...exerciseText.matchAll(new RegExp(promptPattern,'gm'))]
 for(let i=0;i<promptBlocks.length;i++){
  const p=promptBlocks[i]
  const id=p[1].replace(/^Bài (?=\d)/,'')
  if(solutionBlocks.some(s=>s.id===id))continue
  const section=exerciseText.slice(p.index,promptBlocks[i+1]?.index??exerciseText.length)
  const detail=section.match(/^::: (?:details|solution)[^\n]*\n([\s\S]*?)\n:::/m)
  if(detail){
   const existing=solutionBlocks.find(s=>s.body.trim()===detail[1].trim())
   if(existing)existing.aliases=[...(existing.aliases||[]),id]
   else solutionBlocks.push({id,body:detail[1]})
  }
 }
 const missing=Array.from({length:expectedExercises},(_,i)=>i+1).filter(n=>!prompts.includes(n))
 const malformed=solutionBlocks.filter(m=>!m.body.includes('**Tóm tắt đề bài:**')||!m.body.includes('**Hướng đi:**')||!/^\s*- /m.test(m.body)).map(m=>m.id)
 const unsolved=prompts.filter(n=>!solutionBlocks.some(m=>m.id===`${ch.chapter}.${n}`))
 const allPromptIds=[...promptBlocks.map(p=>p[1].replace(/^Bài (?=\d)/,'')),...htmlPrompts.map(p=>p[1]==='Bài tập cầu nối'?`Bài cầu nối ${ch.chapter}`:p[1])]
 const sourceDiscussionIds=[...new Set([...source.matchAll(new RegExp(`\\bQ\\s*${ch.chapter}\\.\\d+\\b`,'g'))].map(m=>m[0].replace(/\s+/g,'')))]
 const sourceVariationIds=[...new Set([...source.matchAll(new RegExp(`\\bVP\\s*${ch.chapter}\\.\\d+\\.\\d+\\b`,'g'))].map(m=>m[0].replace(/\s+/g,'')))]
 const missingDiscussionIds=sourceDiscussionIds.filter(id=>!allPromptIds.includes(id))
 const missingVariationIds=sourceVariationIds.filter(id=>!allPromptIds.includes(id))
 const unsolvedPromptIds=allPromptIds.filter(id=>!solutionBlocks.some(s=>s.id===id||s.aliases?.includes(id)))
 const outsideExercises=main.split('<div class="lecture-exercises-content"')[0]
 const misplaced=new RegExp(`^(?:::: exercise |### )(?:Q|VP)?${ch.chapter}\\.\\d`,'m').test(outsideExercises)
 const prereqs=[...(lesson.prerequisites||[]),...(lesson.supportingConcepts||[])]
 const badWiki=[]
 for(const id of prereqs)if(!concepts[id]||!await exists(`docs/wiki/${id}.md`))badWiki.push(id)
 const sheet=cheatsheets[`${course.id}/${lesson.slug}`]
 const sheetItems=sheet?.sections?.flatMap(s=>s.items||[])||[]
 const sheetExtra=sheetItems.some(i=>i.example||i.warning||i.correct||i.code)
 const forbidden=[...all.replace(/<!--[\s\S]*?-->/g,'').matchAll(/(?:theo sách|sách dùng|nguyên tác|bản dịch của|tiến độ bản dịch|ảnh lấy từ sách)/gi)].map(m=>m[0])
 const review=ch.completionReview&&await exists(ch.completionReview)?JSON.parse(await readFile(ch.completionReview,'utf8')):null
 const status={sourceComplete:ch.status==='complete'&&ch.pendingSourceUnits.length===0,
  endExercisesPresent:expectedExercises>0&&missing.length===0,
  endDiscussionQuestionsPresent:missingDiscussionIds.length===0,
  guidedPracticePresent:missingVariationIds.length===0,
  separateExerciseTab:lesson.hasChapterExercises===true&&!misplaced,
  exerciseSolutionFormat:prompts.length>0&&unsolved.length===0&&unsolvedPromptIds.length===0&&malformed.length===0,
  cheatsheetOnlyDefinitionsPropertiesFormulas:Boolean(sheet)&&!sheetExtra,
  slidesPresent:course.slides.some(s=>s.note===lesson.slug),
  foundationsAndWikiRegistered:badWiki.length===0,
  independentVietnamesePresentation:forbidden.length===0,
  sourceFiguresCaptionsAndSemanticReview:Boolean(review&&(review.status==='content-complete'||review.status==='complete')),
  renderedMobileReview:review?.renderReview==='passed'}
 rows.push({course:course.id,chapter:ch.chapter,slug:lesson.slug,title:lesson.title,
  expectedExercises,exercisePrompts:prompts.length,detailedSolutions:solutionBlocks.length,
  missingExerciseNumbers:missing,missingDiscussionIds,missingVariationIds,unsolvedExerciseNumbers:unsolved,unsolvedPromptIds,malformedSolutions:malformed,
  missingWiki:badWiki,forbiddenPhrases:forbidden,pendingSourceUnits:ch.pendingSourceUnits,status})
}
const cheatIndex=lectureParts.findIndex(p=>p.id==='cheatsheet')
const shared={courseOrder:courseCatalog.findIndex(c=>c.id==='vat-ly-2')===courseCatalog.findIndex(c=>c.id==='vat-ly-1')+1,
 cheatsheetImmediatelyAfterExercises:cheatIndex>0&&lectureParts[cheatIndex-1].id==='bai-tap'}
const report={generatedAt:new Date().toISOString(),scope:'44 lectures in Physics 1 and Physics 2',
 status:rows.every(r=>Object.values(r.status).every(v=>v===true))?'complete':'incomplete',shared,lectures:rows}
await mkdir('qa/physics',{recursive:true})
await writeFile('qa/physics/requirements-audit.json',JSON.stringify(report,null,2)+'\n')
const lines=['# Rà yêu cầu cho các bài giảng vật lý','',
 'Phạm vi: 20 chương Vật lý đại cương 1 và 24 chương Vật lý đại cương 2.',
 'Đây là hồ sơ nội bộ. Kiểm tra cấu trúc không thay thế đối chiếu từng đoạn, hình và lập luận với tài liệu.', '',
 '| Môn | Chương | Bài giảng | Đề cuối chương | Lời giải chi tiết | Nội dung nguồn |',
 '| --- | --- | --- | --- | --- | --- |',
 ...rows.map(r=>`| ${r.course} | ${r.chapter} | ${r.title} | ${r.exercisePrompts}/${r.expectedExercises} | ${r.detailedSolutions} | ${r.status.sourceComplete?'Đủ theo hồ sơ':'Còn thiếu hoặc chưa rà xong'} |`),'',
 '## Kết luận','',
 'Chưa thể xác nhận tất cả bài giảng đáp ứng toàn bộ yêu cầu. JSON đi kèm ghi riêng bài thiếu nội dung, bài tập, khung lời giải, Cheatsheet, Slides, Wiki và các bước rà chưa làm. Không chứng nhận đủ nội dung chỉ từ mục lục hoặc build thành công.','']
await writeFile('raw_materials/physics/requirements-audit.md',lines.join('\n'))
console.log(JSON.stringify({scope:rows.length,status:report.status,
 sourceComplete:rows.filter(r=>r.status.sourceComplete).length,
 separateExercises:rows.filter(r=>r.status.separateExerciseTab).length,
 fullExerciseSolutionFormat:rows.filter(r=>r.status.exerciseSolutionFormat).length,
 explicitCheatsheets:rows.filter(r=>r.status.cheatsheetOnlyDefinitionsPropertiesFormulas).length,shared},null,2))
