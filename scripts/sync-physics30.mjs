import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {parseAst} from 'rollup/parseAst'
import assert from 'node:assert/strict'
import {physics2Course} from '../docs/.vitepress/physics-courses.mjs'
import {inductanceTopics,inductanceSlides} from '../docs/.vitepress/physics-inductance-course.mjs'
import {inductanceConcepts,inductanceWikiDetails,inductanceWikiConnections} from '../docs/.vitepress/physics-inductance-foundations.mjs'
import {concepts} from '../docs/.vitepress/concepts.mjs'
const numeric=JSON.parse(await readFile('qa/physics/chapter30/numeric-checks.json','utf8'))
assert.equal(numeric.status,'passed');assert.equal(numeric.detailedSolutions,104)
const raw='raw_materials/physics/translations/chapter-30',dir='docs/vat-ly-2/bai-giang'
const lesson=structuredClone(physics2Course.lessons.find(l=>l.sourceChapter===30)),slug=lesson.slug
lesson.status='ready'
lesson.prerequisites=['dao-ham','tich-phan','dao-dong-dieu-hoa','dao-dong-tat-dan','dien-dung','mat-do-nang-luong-dien-truong','quy-tac-kirchhoff','ong-day-dien','do-tu-tham','dinh-luat-faraday','dinh-luat-lenz','dien-truong-bao-toan']
lesson.supportingConcepts=Object.keys(inductanceConcepts)
lesson.topicGroups=inductanceTopics;lesson.hasChapterExercises=true
const catalog='docs/.vitepress/physics-courses.mjs'
let source=await readFile(catalog,'utf8')
const ast=parseAst(source)
const node=ast.body.find(n=>n.declaration?.declarations?.some(d=>d.id.name==='physics2Course')).declaration.declarations.find(d=>d.id.name==='physics2Course').init
const props=Object.fromEntries(node.properties.map(p=>[p.key.name??p.key.value,p.value]))
const target=props.lessons.elements.find(e=>e.properties.some(p=>(p.key.name??p.key.value)==='sourceChapter'&&p.value.value===30))
const slides=[...physics2Course.slides.filter(s=>s.note!==slug),...inductanceSlides]
for(const edit of [{start:target.start,end:target.end,text:JSON.stringify(lesson,null,2)},{start:props.slides.start,end:props.slides.end,text:JSON.stringify(slides,null,2)}].sort((a,b)=>b.start-a.start))source=source.slice(0,edit.start)+edit.text+source.slice(edit.end)
await writeFile(catalog,source)
const pages=[['ho-cam','01-ho-cam.md','30.1',988,991],['tu-cam-cuon-cam','02-tu-cam.md','30.2',992,995],['nang-luong-tu-truong','03-nang-luong-tu-truong.md','30.3',995,998],['mach-rl','04-mach-rl.md','30.4',998,1002],['mach-lc','05-mach-lc.md','30.5',1002,1006],['mach-rlc','06-mach-rlc.md','30.6',1007,1008]]
await mkdir(`${dir}/${slug}`,{recursive:true})
for(const [topic,file,section,start,end]of pages){
 const t=inductanceTopics.flatMap(g=>g.topics).find(t=>t.slug===topic)
 await writeFile(`${dir}/${slug}/${topic}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\ntopic: ${topic}\nsection: topic\ntitle: ${JSON.stringify(t.title)}\ndescription: ${JSON.stringify(t.question)}\n---\n\n<!--@include: ../../../../${raw}/${file}-->\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục ${section}, trang ${start}–${end}.\n`)
}
const exercises=['10-luyen-tap-huong-dan.md','11-cau-hoi-thao-luan.md','12-bai-tap-01-30.md','13-bai-tap-31-60.md','14-bai-tong-hop-61-68.md','15-nang-cao-mcat.md','16-dap-so.md']
const include=file=>`<!--@include: ../../../${raw}/${file}-->\n\n`
await writeFile(`${dir}/${slug}.md`,`---\ncourse: vat-ly-2\nlecture: ${slug}\nsection: lecture\ntitle: ${JSON.stringify(lesson.title)}\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ready\nhasChapterExercises: true\ndescription: "Hỗ cảm, tự cảm, năng lượng từ trường, mạch RL, LC và RLC, cùng lời giải chi tiết phần cuối chương."\n---\n\n<div class="lecture-notes-content">\n\n${include('00-mo-dau.md')}<TopicMap />\n\n${include('09-tom-tat.md')}## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 30, trang 988–1017.\n\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Điện cảm">\n\n${exercises.map(include).join('')}## Tài liệu tham khảo\n\nYoung & Freedman, ấn bản 15, chương 30, trang 1010–1017 và phụ lục đáp số A-18.\n\n</div>\n`)
for(const [id,c]of Object.entries(inductanceConcepts)){
 const full=inductanceWikiDetails[id],reference=full.slice(full.indexOf('\n\nTài liệu tham khảo:')).replace(/^\n\nTài liệu tham khảo:\s*/,'')
 const detail=full.replace(/\n\nTài liệu tham khảo:[\s\S]*$/,'')
 const related=inductanceWikiConnections[id].map(key=>{assert(concepts[key],key);return `- [${concepts[key].name}](./${key}.md)`}).join('\n')
 await writeFile(`docs/wiki/${id}.md`,`---\ntitle: ${JSON.stringify(c.name)}\nwikiTerm: ${id}\nprev: false\nnext: false\n---\n\n# ${c.name}\n\n${c.definition}\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n${detail}\n\n## Ví dụ\n\n${c.example}\n\n## Khi nào cần dùng?\n\n${c.use}\n\n## Câu hỏi ôn lại\n\n${c.question}\n\n<details><summary>Xem đáp án</summary>\n\n${c.answer}\n\n</details>\n\n## Thuật ngữ liên quan\n\n${related}\n\n## Tài liệu tham khảo\n\n${reference}\n`)
}
const mf='raw_materials/physics/translation-manifest.json',m=JSON.parse(await readFile(mf,'utf8')),ch=m.chapters.find(c=>c.chapter===30)
ch.fragments=[{sourceUnit:'chapter-opening',file:raw+'/00-mo-dau.md',destination:'notes'},...pages.map(([topic,file,sourceUnit,start,end])=>({sourceUnit,file:raw+'/'+file,destination:'topic:'+topic,printedPages:[start,end]})),{sourceUnit:'chapter-summary',file:raw+'/09-tom-tat.md',destination:'notes'},...exercises.map(file=>({sourceUnit:file.replace(/\.md$/,''),file:raw+'/'+file,destination:'bai-tap'}))].map(f=>({...f,status:'authored-and-reviewed'}))
ch.status='content-complete';ch.completionReview='raw_materials/physics/chapter-30-review.json';ch.pendingSourceUnits=['direct-browser-render-review']
await writeFile(mf,JSON.stringify(m,null,2)+'\n')
console.log('Integrated chapter30: six topics,104 detailed solutions,11 slides,six Cheatsheet groups and12 Wiki entries; render review pending.')
