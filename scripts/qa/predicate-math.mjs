import {readFile,readdir} from 'node:fs/promises'
import {createMathValidator} from '../verification/math-validator.mjs'
import {mathSegments} from '../../docs/.vitepress/math-text.mjs'
const root='docs/bieu-dien-tri-thuc/bai-giang/08-logic-vi-tu',files=[root+'.md',...(await readdir(root)).filter(x=>x.endsWith('.md')).map(x=>root+'/'+x)],validate=createMathValidator();let count=0
for(const file of files)for(const segment of mathSegments(await readFile(file,'utf8'))){if(!segment.startsWith('$'))continue;const display=segment.startsWith('$$'),n=display?2:1;try{validate(segment.slice(n,-n),display,file);count++}catch(e){console.error(file,JSON.stringify(segment));throw e}}
console.log(`PASS ${count} math expressions across ${files.length} Notes pages`)
