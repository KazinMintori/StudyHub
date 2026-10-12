import {readFile,writeFile,mkdir,access} from 'node:fs/promises'
import path from 'node:path'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
import {cheatsheets} from '../docs/.vitepress/cheatsheets.mjs'
import {lectureParts} from '../docs/.vitepress/lecture-model.mjs'

const manifest=JSON.parse(await readFile('raw_materials/physics/translation-manifest.json','utf8'))
const exists=async f=>{try{await access(f);return true}catch{return false}}
async function expand(file,seen=new Set()) {
 if(seen.has(file))return ''
 seen.add(file)
 let text=await readFile(file,'utf8')
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
 const sourceNumbers=[...source.matchAll(new RegExp(`^${ch.chapter}\\.(\\d+)\\s`,'gm'))].map(m=>Number(m[1]))
 const expectedExercises=Math.max(0,...sourceNumbers)
 const prompts=[...all.matchAll(new RegExp(`^::: exercise ${ch.chapter}\\.(\\d+)(?:\\s|$)`,'gm'))].map(m=>Number(m[1]))
 const missing=Array.from({length:expectedExercises},(_,i)=>i+1).filter(n=>!prompts.includes(n))
 const solutionBlocks=[...all.matchAll(/<!-- detailed-solution:([^>]+) -->\s*::: solution[^\n]*\n([\s\S]*?)\n:::/g)]
 const malformed=solutionBlocks.filter(m=>!m[2].includes('**Tóm tắt đề bài:**')||!m[2].includes('**Hướng đi:**')||!/^\s*- /m.test(m[2])).map(m=>m[1])
 const unsolved=prompts.filter(n=>!solutionBlocks.some(m=>m[1]===`${ch.chapter}.${n}`))
 const outsideExercises=main.split('<div class="lecture-exercises-content"')[0]
 const misplaced=new RegExp(`^::: exercise (?:Q|VP)?${ch.chapter}\\.`,'m').test(outsideExercises)
 const prereqs=[...(lesson.prerequisites||[]),...(lesson.supportingConcepts||[])]
 const badWiki=[]
 for(const id of prereqs)if(!concepts[id]||!await exists(`docs/wiki/${id}.md`))badWiki.push(id)
 const sheet=cheatsheets[`${course.id}/${lesson.slug}`]
 const sheetItems=sheet?.sections?.flatMap(s=>s.items||[])||[]
 const sheetExtra=sheetItems.some(i=>i.example||i.warning||i.correct||i.code)
 const forbidden=[...all.replace(/<!--[\s\S]*?-->/g,'').matchAll(/(?:theo sách|sách dùng|nguyên tác|bản dịch của|tiến độ bản dịch|ảnh lấy từ sách)/gi)].map(m=>m[0])
 const status={sourceComplete:ch.status==='complete'&&ch.pendingSourceUnits.length===0,
  endExercisesPresent:expectedExercises>0&&missing.length===0,
  separateExerciseTab:lesson.hasChapterExercises===true&&!misplaced,
  exerciseSolutionFormat:prompts.length>0&&unsolved.length===0&&malformed.length===0,
  cheatsheetOnlyDefinitionsPropertiesFormulas:Boolean(sheet)&&!sheetExtra,
  slidesPresent:course.slides.some(s=>s.note===lesson.slug),
  foundationsAndWikiRegistered:badWiki.length===0,
  independentVietnamesePresentation:forbidden.length===0,
  sourceFiguresCaptionsAndSemanticReview:ch.completionReview||null,
  renderedMobileReview:'Requires direct browser review. Static checks do not certify this.'}
 rows.push({course:course.id,chapter:ch.chapter,slug:lesson.slug,title:lesson.title,
  expectedExercises,exercisePrompts:prompts.length,detailedSolutions:solutionBlocks.length,
  missingExerciseNumbers:missing,unsolvedExerciseNumbers:unsolved,malformedSolutions:malformed,
  missingWiki:badWiki,forbiddenPhrases:forbidden,pendingSourceUnits:ch.pendingSourceUnits,status})
}
const cheatIndex=lectureParts.findIndex(p=>p.id==='cheatsheet')
const shared={courseOrder:physics1Course.id==='vat-ly-1'&&physics2Course.id==='vat-ly-2',
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
