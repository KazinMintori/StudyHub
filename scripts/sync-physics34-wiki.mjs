import {writeFile} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {concepts} from '../docs/.vitepress/concepts.mjs'
import {physicsWikiDetails,physicsWikiConnections} from '../docs/.vitepress/physics-foundations.mjs'
import {geometricOpticsConcepts,geometricOpticsWikiDetails,geometricOpticsWikiConnections} from '../docs/.vitepress/physics-geometric-optics-foundations.mjs'
const front=data=>['---',...Object.entries(data).map(([key,value])=>key+': '+JSON.stringify(value)),'---',''].join('\n')
const entries={...geometricOpticsConcepts}
for(const [id,c] of Object.entries(entries)){
 const detail=(geometricOpticsWikiDetails[id]??physicsWikiDetails[id]).replace(/\n\nTài liệu tham khảo:[\s\S]*$/,'')
 const related=(geometricOpticsWikiConnections[id]??physicsWikiConnections[id]).map(key=>{
  assert(concepts[key],key)
  return '- ['+concepts[key].name+'](./'+key+'.md)'
 }).join('\n')
 const source=front({title:c.name,wikiTerm:id,prev:false,next:false})+'\n# '+c.name+'\n\n'+c.definition+
  '\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n'+detail+
  '\n\n## Ví dụ\n\n'+c.example+'\n\n## Khi nào cần dùng?\n\n'+c.use+
  '\n\n## Câu hỏi ôn lại\n\n'+c.question+'\n\n<details><summary>Xem đáp án</summary>\n\n'+c.answer+
  '\n\n</details>\n\n## Thuật ngữ liên quan\n\n'+related+
  '\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 34, trang 1110–1147.\n'
 await writeFile('docs/wiki/'+id+'.md',source)
}
console.log('Materialized '+Object.keys(entries).length+' optics Wiki entries with validated related concepts.')
