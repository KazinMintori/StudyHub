// Structural coverage is necessary, but never certifies semantic source review.
import {readFile,readdir,access} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {physics1Course} from '../../docs/.vitepress/physics-courses.mjs'
import {mathRelationLayoutIssues} from './math-relation-layout.mjs'

const chapter=Number(process.argv[2])
assert([1,3,4,5,6,7,8,12,13,14,15,16].includes(chapter),'Pass a remaining chapter')
const nn=String(chapter).padStart(2,'0'),raw=`raw_materials/physics/translations/chapter-${nn}`
const inventory=JSON.parse(await readFile(`qa/physics1-remaining/source/ch${nn}/inventory.json`,'utf8'))
const data=(await import(`../../docs/.vitepress/physics1-remaining-ch${nn}.mjs`))[`physics1RemainingChapter${chapter}`]
const coverage=JSON.parse(await readFile(`raw_materials/physics/reviews/ch${nn}-remaining-exercises-coverage.json`,'utf8'))
assert(data?.topics?.length===inventory.sections.length,'Missing source section')
assert(coverage.exerciseConfig?.files,'Reconcile original exercise inventory first')
const files=[data.openingFile||'00-mo-dau.md',...data.topics.map(t=>t.file),data.summaryFile||(chapter===1?'11-tom-tat.md':'17-tom-tat.md'),...coverage.exerciseConfig.files.map(([,file])=>file),...(data.answerFile?[data.answerFile]:[])]
const text=await Promise.all(files.map(file=>readFile(raw+'/'+file,'utf8')))
const joined=text.join('\n')
const findings=[]
const check=(condition,kind,details)=>{if(!condition)findings.push({kind,details})}
for(const section of inventory.sections)check(data.topics.some(t=>t.source===section.id),'missing-section',section.id)
for(const id of inventory.examples)check(new RegExp('^(?:::: example |#{2,6} )Ví dụ(?:\\s+(?:định tính|khái niệm))?\\s+'+id.replace('.','\\.')+'(?=\\D|$)','mi').test(joined),'missing-teaching-example',id)
const exerciseIds=[]
for(const [kind,file]of coverage.exerciseConfig.files){
 const source=await readFile(raw+'/'+file,'utf8')
 const pattern=new RegExp('^### ((?:VP|Q)?'+chapter+'\\.\\d+(?:\\.\\d+)?|Bài tập cầu nối)(?=\\s|:|$)[^\\n]*','gm')
 const starts=[...source.matchAll(pattern)]
 check(starts.length>0,'empty-exercise-fragment',file)
 for(const [i,match]of starts.entries()){
  const body=source.slice(match.index,starts[i+1]?.index??source.length)
  exerciseIds.push(match[1])
  check((body.match(/<details(?:\s[^>]*)?>/g)||[]).length===1&&(body.match(/<\/details>/g)||[]).length===1&&!/<details\s+open\b/.test(body),'solution-not-closed',match[1])
  for(const label of ['Tóm tắt đề bài','Hướng đi','Lời giải'])check(body.includes(label),'missing-solution-stage',{id:match[1],label})
  const solution=body.split(/<summary>[^]*?<\/summary>/)[1]?.split('</details>')[0]||''
  check(solution.trim().length>=150,'solution-needs-substantive-review',match[1])
 }
}
const unique=new Set(exerciseIds)
check(unique.size===exerciseIds.length,'duplicate-exercise-id',exerciseIds.filter((id,i)=>exerciseIds.indexOf(id)!==i))
const maximum=chapter===1?94:inventory.numberedMax
for(let i=1;i<=maximum;i++)check(unique.has(`${chapter}.${i}`),'missing-numbered-exercise',`${chapter}.${i}`)
for(const id of [...inventory.discussionDetected,...inventory.guidedDetected])check(unique.has(id),'missing-question-or-variation',id)
check(unique.has('Bài tập cầu nối'),'missing-bridge')
let images=0
for(const [i,source]of text.entries()){
 for(const issue of mathRelationLayoutIssues(source))findings.push({file:files[i],...issue})
 check(!/\b(?:TODO|TBD)\b|\[Chưa có|lời giải sẽ|đang biên soạn/i.test(source),'placeholder',files[i])
 check(!/theo sách|sách dùng|ảnh nguyên gốc|hình nguyên gốc|bản dịch của|tiến độ bản dịch/i.test(source),'internal-source-editorial-prose',files[i])
 for(const match of source.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)){
  const figure=match[1].match(/young-\d+\/[^\s)]+/)
  check(Boolean(figure),'nonstandard-figure-path',match[1]);if(!figure)continue
  await access('docs/vat-ly-1/bai-giang/img/'+figure[0]);images++
 }
}
const report={status:findings.length?'failed':'passed',scope:'Structural and source-ID coverage only. Source meaning, numerical correctness, crop integrity and actual viewport layout require separate review.',chapter,sections:data.topics.length,examples:inventory.examples.length,exerciseIds:unique.size,imageReferences:images,findings}
console.log(JSON.stringify(report,null,2))
if(findings.length)process.exitCode=1
