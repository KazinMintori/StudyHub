// Refresh only the isolated course checkout owned by this review. This does not
// export into the shared cache or change a pin in the main working directory.
import {readFile,writeFile,lstat} from 'node:fs/promises'
import path from 'node:path'
import {execFileSync} from 'node:child_process'
import {digest,matchesPath,safePath,verifyPackage} from '../content/course-repositories.mjs'
const directory=path.resolve('../math-ai-visual-content')
const lock=JSON.parse(await readFile('config/course-repositories.json','utf8'))
const course=lock.courses.find(course=>course.id==='toan-cho-ai')
const manifestPath=path.join(directory,'studyhub-course.json')
const previous=JSON.parse(await readFile(manifestPath,'utf8'))
if(previous.id!==course?.id)throw Error('Unexpected course checkout')
const git=args=>execFileSync('git',['-C',directory,...args],{windowsHide:true}).toString().split('\0').filter(Boolean)
const names=[...new Set([...git(['ls-files','-z']),...git(['ls-files','--others','--exclude-standard','-z'])])].filter(file=>course.paths.some(pattern=>matchesPath(file,pattern))).sort()
for(const file of Object.keys(previous.files))if(!names.includes(file))throw Error('Preserve unexpectedly missing package source: '+file)
const files={},updatedAt={},changed=[],now=Date.now()
for(const file of names){
 safePath(file)
 const target=path.join(directory,file),stat=await lstat(target)
 if(!stat.isFile()||stat.isSymbolicLink())throw Error('Only real authored files are supported: '+file)
 if(stat.size>50*1024*1024)throw Error('Unexpected oversized course file: '+file)
 files[file]=digest(await readFile(target))
 const same=previous.files[file]===files[file]
 updatedAt[file]=same&&previous.updatedAt?.[file]||now
 if(!same)changed.push(file)
}
if(process.argv.includes('--write')){
 await writeFile(manifestPath,JSON.stringify({version:1,id:course.id,files,updatedAt},null,2)+'\n')
 await verifyPackage(course,directory)
}
console.log(JSON.stringify({mode:process.argv.includes('--write')?'updated-and-verified':'preview',course:course.id,files:names.length,changed:changed.length},null,2))
