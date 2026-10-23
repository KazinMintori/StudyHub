// Keep each prompt and its closed solution together. The reading passage is
// repeated when its questions cross a group boundary.
import {mathRelationLayoutIssues} from '../verification/math-relation-layout.mjs'
export function splitPhysicsExercises(source, { chapter, kind, size = 6 }) {
 if(!Number.isInteger(chapter)||chapter<1||!Number.isInteger(size)||size<1)throw Error('Invalid exercise grouping options')
 const text=source.replace(/\r\n/g,'\n')
 const mathIssues=mathRelationLayoutIssues(text)
 if(mathIssues.length)throw Error('Malformed math relation layout in '+kind+': '+JSON.stringify(mathIssues))
 const pattern=new RegExp('^### ((?:(?:VP|Q)?'+chapter+'\\.\\d+(?:\\.\\d+)?)|Bài tập cầu nối)(?=\\s|:|$)[^\\n]*\\n','gm')
 const headings=[...text.matchAll(pattern)]
 if(!headings.length)throw Error('No exercise headings: '+kind)
 const passages=[]
 const extractPassage=(section,startAt)=>{
  const marker=section.search(/^## Đọc hiểu khoa học:/m)
  if(marker<0)return section
  passages.push({startAt,markdown:section.slice(marker)})
  return section.slice(0,marker).trim()
 }
 const prefix=extractPassage(text.slice(0,headings[0].index).trim(),0)
 const blocks=headings.map((h,i)=>{
  let body=text.slice(h.index,headings[i+1]?.index??text.length).trim()
  body=extractPassage(body,i+1)
  if((body.match(/<details(?:\s[^>]*)?>/g)||[]).length!==1
   ||(body.match(/<\/details>/g)||[]).length!==1
   ||/<details\s+open\b/.test(body))throw Error('Expected one closed solution: '+h[1])
  return {id:h[1],body,index:i}
 })
 if(new Set(blocks.map(b=>b.id)).size!==blocks.length)throw Error('Duplicate exercise ID')
 const groups=[]
 for(let i=0;i<blocks.length;i+=size){
  const part=blocks.slice(i,i+size),first=part[0].id,last=part.at(-1).id
  let insertedPassage
  const content=part.map(b=>{
   const passage=passages.filter(p=>b.index>=p.startAt).at(-1)
   if(passage&&insertedPassage!==passage){insertedPassage=passage;return passage.markdown+'\n\n'+b.body}
   return b.body
  })
  groups.push({
   id:kind+'-'+String(groups.length+1).padStart(2,'0'),
   title:kind==='bridge'?'Bài tập cầu nối':kind==='guided'?'Luyện tập '+first+'–'+last:kind==='discussion'?'Thảo luận '+first+'–'+last:'Bài '+first+'–'+last,
   ids:part.map(b=>b.id),
   markdown:[prefix,...content].filter(Boolean).join('\n\n')+'\n'
  })
 }
 return groups
}
