import {readFile,writeFile,mkdir,mkdtemp,rm} from 'node:fs/promises'
import {spawn} from 'node:child_process'
import {tmpdir} from 'node:os'
import {join,resolve} from 'node:path'
import {createHash} from 'node:crypto'
import {splitPhysicsExercises} from './physics-exercise-groups.mjs'
import {publishedPhysicsExerciseChapters,physicsExerciseConfigs,physicsExerciseFiles,validatePhysicsExerciseIds} from './physics-exercise-config.mjs'
const selected=process.argv.slice(2).map(Number)
if(selected.some(chapter=>!Number.isInteger(chapter)||!physicsExerciseConfigs[chapter]))throw Error('Unconfigured exercise chapter')
for(const chapter of selected.length?selected:publishedPhysicsExerciseChapters){
const chapterLabel=String(chapter).padStart(2,'0')
const directory=resolve('docs/public/physics-exercises/ch'+chapterLabel)
await mkdir(directory,{recursive:true})
const files=physicsExerciseFiles(chapter)
const groups=[],sources=[]
for(const[kind,file]of files){
 const path='raw_materials/physics/translations/chapter-'+chapterLabel+'/'+file
 const source=await readFile(path,'utf8')
 sources.push({file:path,sha256:createHash('sha256').update(source).digest('hex')})
 groups.push(...splitPhysicsExercises(source,{chapter,kind,size:6}))
}
const total=validatePhysicsExerciseIds(chapter,groups)
const temporary=await mkdtemp(join(tmpdir(),'studyhub-physics-exercises-'))
try{
 for(const group of groups){
  const input=join(temporary,group.id+'.json')
  // The original fragments resolve figures from a topic or the chapter page.
  group.markdown=group.markdown.replace(new RegExp('(?:\\.\\./|\\./)img/young-'+chapterLabel+'/','g'),'/vat-ly-1/bai-giang/img/young-'+chapterLabel+'/')
  await writeFile(input,JSON.stringify(group))
  await new Promise((done,fail)=>{
   const child=spawn(process.execPath,['--max-old-space-size=512','scripts/content/render-physics-exercise-group.mjs',input,join(directory,group.id+'.json')],{stdio:'inherit',windowsHide:true})
   child.once('error',fail);child.once('exit',code=>code===0?done():fail(Error('Group render failed: '+group.id)))
  })
  console.log('Rendered '+group.title)
 }
 // Publish the index only after every complete group was rendered successfully.
 await writeFile(join(directory,'index.json'),JSON.stringify({chapter,sources,total,groups:groups.map(({markdown,...g})=>g)}))
}finally{
 // This exact directory was created above by mkdtemp and is owned by this run.
 await rm(temporary,{recursive:true,force:true})
}
}
