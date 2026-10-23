import{writeFile}from'node:fs/promises'
import assert from'node:assert/strict'
import{concepts}from'../docs/.vitepress/concepts.mjs'
import{physics1PriorityConcepts as records,physics1PriorityWikiDetails as details,physics1PriorityWikiConnections as connections}from'../docs/.vitepress/physics1-priority-foundations.mjs'
const front=values=>['---',...Object.entries(values).map(([k,v])=>k+': '+JSON.stringify(v)),'---',''].join('\n')
for(const[id,c]of Object.entries(records)){
 assert(concepts[id]&&details[id]&&connections[id],id)
 const related=connections[id].map(key=>{assert(concepts[key],key);return'- ['+concepts[key].name+'](./'+key+'.md)'}).join('\n')
 const source=front({title:c.name,wikiTerm:id,prev:false,next:false})+'\n# '+c.name+'\n\n'+c.definition+'\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n'+details[id]+'\n\n## Ví dụ\n\n'+c.example+'\n\n## Khi nào cần dùng?\n\n'+c.use+'\n\n## Câu hỏi ôn lại\n\n'+c.question+'\n\n<details><summary>Xem đáp án</summary>\n\n'+c.answer+'\n\n</details>\n\n## Thuật ngữ liên quan\n\n'+related+'\n\n## Tài liệu tham khảo\n\nYoung & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 9–11 và 17–20.\n'+(id==='diem-ba'?'\n[BIPM: Kelvin](https://www.bipm.org/en/si-base-units/kelvin).\n':'')
 await writeFile('docs/wiki/'+id+'.md',source)
}
console.log('Materialized '+Object.keys(records).length+' new rotation/thermal Wiki pages.')
