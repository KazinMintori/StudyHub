import {writeFile} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {concepts} from '../docs/.vitepress/concepts.mjs'
import {atomicStructureConcepts,atomicStructureWikiDetails,atomicStructureWikiConnections} from '../docs/.vitepress/physics-atomic-structure-foundations.mjs'
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const lookup={...concepts,...atomicStructureConcepts}
for(const[id,concept]of Object.entries(atomicStructureConcepts)){
 const detail=atomicStructureWikiDetails[id]
 assert(detail&&atomicStructureWikiConnections[id],id)
 const related=atomicStructureWikiConnections[id].map(key=>{
  assert(lookup[key],key)
  return '- ['+lookup[key].name+'](./'+key+'.md)'
 }).join('\n')
 const source=front({title:concept.name,wikiTerm:id,prev:false,next:false})+'\n# '+concept.name+'\n\n'+concept.definition+
 '\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n'+detail+
 '\n\n## Ví dụ\n\n'+concept.example+'\n\n## Khi nào cần dùng?\n\n'+concept.use+
 '\n\n## Câu hỏi ôn lại\n\n'+concept.question+'\n\n<details><summary>Xem đáp án</summary>\n\n'+concept.answer+
 '\n\n</details>\n\n## Thuật ngữ liên quan\n\n'+related+
 '\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 41, trang 1360–1398.\n'
 await writeFile('docs/wiki/'+id+'.md',source)
}
console.log('Materialized20 validated chapter41 Wiki pages.')
