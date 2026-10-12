import {readFile,writeFile} from 'node:fs/promises'
const file='raw_materials/physics/translation-manifest.json'
const manifest=JSON.parse(await readFile(file,'utf8')),ch=manifest.chapters.find(c=>c.chapter===23)
const dir='raw_materials/physics/translations/chapter-23'
ch.status='in-progress'
ch.fragments=[['chapter-opening','00-mo-dau.md'],['23.1','01-the-nang-dien.md'],['23.2','02-dien-the.md'],['23.3','03-tinh-dien-the.md'],['23.4','04-mat-dang-the.md'],['23.5','05-gradient-dien-the.md']].map(([sourceUnit,file])=>({sourceUnit,file:dir+'/'+file,status:'authored-awaiting-figures-and-final-semantic-review',destination:sourceUnit==='chapter-opening'?'notes':'topic'}))
ch.pendingSourceUnits=['all-original-figures-and-captions','chapter-summary','guided-practice','discussion-questions','all-end-of-chapter-exercises-and-problems','appendix-odd-answers','site-integration-and-render-review','final-semantic-review']
await writeFile(file,JSON.stringify(manifest,null,2)+'\n')
console.log('Recorded chapter23 theory progress; chapter remains incomplete.')
