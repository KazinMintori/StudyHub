// Sync only this task's course edits into its ignored QA assembly. A differing
// destination is accepted only if a pinned package or an earlier QA snapshot
// proves its exact bytes; otherwise preserve it and stop before any writes.
import { readFile,writeFile,mkdir,readdir,copyFile } from 'node:fs/promises'
import { execFileSync } from 'node:child_process'
import { createHash } from 'node:crypto'
import path from 'node:path'
const root=process.cwd(),source=path.resolve('../math-ai-visual-content'),output=path.resolve('qa/math-ai-visuals')
const hash=data=>createHash('sha256').update(data).digest('hex')
const optional=file=>readFile(file).catch(e=>{if(e.code==='ENOENT')return null;throw e})
const manifest=JSON.parse(await readFile(path.join(source,'studyhub-course.json'),'utf8'))
if(manifest.id!=='toan-cho-ai')throw Error('Expected the Toán cho AI source checkout')
const records={}
for(const [file,digest]of Object.entries(manifest.files)) records[file]=new Set([digest])
// During a merge the package file can already describe the incoming version.
// The immutable current HEAD remains proof of the pinned/previous source bytes.
const baseline=JSON.parse(execFileSync('git',['-C',source,'show','HEAD:studyhub-course.json'],{encoding:'utf8',windowsHide:true}))
if(baseline.id!==manifest.id)throw Error('Unexpected baseline course package')
for(const [file,digest]of Object.entries(baseline.files))(records[file]||=new Set()).add(digest)
await mkdir(output,{recursive:true})
const ledgerPath=path.join(output,'course-sync-ledger.json')
const previous=JSON.parse((await optional(ledgerPath))?.toString()||'{}')
for(const [file,digest]of Object.entries(previous)) (records[file]||=new Set()).add(digest)
for(const name of await readdir(output)){
 if(!/^browser-results.*\.json$/.test(name))continue
 const record=JSON.parse(await readFile(path.join(output,name),'utf8'))
 for(const [file,digest]of Object.entries(record.sources||{}))(records[file]||=new Set()).add(digest)
}
const git=args=>execFileSync('git',['-C',source,...args],{encoding:'utf8',windowsHide:true}).split(/\r?\n/).filter(Boolean)
const names=[...new Set([...git(['diff','--name-only','HEAD']),...git(['ls-files','--others','--exclude-standard'])])]
 .filter(file=>/^(?:docs\/toan-cho-ai\/|docs\/public\/materials\/toan-cho-ai\/|src\/content\/courses\/toan-cho-ai\/)/.test(file))
const plan=[]
for(const file of names){
 if(file.includes('..')||file.includes('\\'))throw Error('Unsafe source path')
 const from=await readFile(path.join(source,file)),to=await optional(path.join(root,file)),digest=hash(from)
 if(to&&hash(to)===digest){previous[file]=digest;continue}
 if(to&&!records[file]?.has(hash(to)))throw Error(`Preserve unknown destination edits: ${file}`)
 plan.push({file,from,to,digest})
}
if(process.argv.includes('--write')){
 for(const item of plan){
  if(item.to){const backup=path.join(output,'source-snapshots',hash(item.to)+path.extname(item.file));await mkdir(path.dirname(backup),{recursive:true});if(!await optional(backup))await writeFile(backup,item.to)}
  const target=path.join(root,item.file);await mkdir(path.dirname(target),{recursive:true});await writeFile(target,item.from);previous[item.file]=item.digest
 }
 await writeFile(ledgerPath,JSON.stringify(previous,null,2)+'\n')
}
console.log(JSON.stringify({mode:process.argv.includes('--write')?'updated':'preview',files:plan.map(p=>p.file),preservedSnapshots:plan.filter(p=>p.to).length},null,2))
