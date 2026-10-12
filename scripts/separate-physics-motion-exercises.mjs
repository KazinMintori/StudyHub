import {readFile,writeFile} from 'node:fs/promises'
import {physics1Course,physics2Course} from '../docs/.vitepress/physics-courses.mjs'

const file='docs/vat-ly-1/bai-giang/02-chuyen-dong-thang.md'
let text=await readFile(file,'utf8')
if(!text.includes('class="lecture-exercises-content"')){
 text=text.replace('lessonStatus: ready','lessonStatus: ready\nhasChapterExercises: true')
 const front=text.indexOf('\n---\n',4)+5
 const end=text.indexOf('<!--@include: ../../../raw_materials/physics/translations/chapter-02/08-')
 const refs=text.indexOf('## Tài liệu tham khảo học thuật')
 if(front<5||end<front||refs<end)throw Error('Unexpected motion lecture structure')
 const before=text.slice(0,front),notes=text.slice(front,end),exercises=text.slice(end,refs),reference=text.slice(refs)
 text=before+'\n<div class="lecture-notes-content">\n'+notes+'\n'+reference+'\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập cuối chương Chuyển động thẳng">\n\n'+exercises+'\n</div>\n'
 await writeFile(file,text)
}
physics1Course.lessons.find(l=>l.sourceChapter===2).hasChapterExercises=true
await writeFile('docs/.vitepress/physics-courses.mjs','// Physics course catalog.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
console.log('Moved existing end-of-chapter motion exercises to the dedicated tab. Theory examples retained in Notes.')
