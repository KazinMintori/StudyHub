import {writeFile} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {concepts} from '../docs/.vitepress/concepts.mjs'
import {nuclearConcepts,nuclearWikiDetails,nuclearWikiConnections} from '../docs/.vitepress/physics-nuclear-foundations.mjs'
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const lookup={...concepts,...nuclearConcepts}
for(const[id,concept]of Object.entries(nuclearConcepts)){
 const detail=nuclearWikiDetails[id]
 assert(detail&&nuclearWikiConnections[id],id)
 const related=nuclearWikiConnections[id].map(key=>{
  assert(lookup[key],key)
  return '- ['+lookup[key].name+'](./'+key+'.md)'
 }).join('\n')
 const source=front({title:concept.name,wikiTerm:id,prev:false,next:false})+'\n# '+concept.name+'\n\n'+concept.definition+
 '\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n'+detail+
 '\n\n## Ví dụ\n\n'+concept.example+'\n\n## Khi nào cần dùng?\n\n'+concept.use+
 '\n\n## Câu hỏi ôn lại\n\n'+concept.question+'\n\n<details><summary>Xem đáp án</summary>\n\n'+concept.answer+
 '\n\n</details>\n\n## Thuật ngữ liên quan\n\n'+related+
 '\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 43, trang 1442–1474.\n'
 await writeFile('docs/wiki/'+id+'.md',source)
}
console.log('Materialized21 structurally validated chapter43 Wiki pages.')
