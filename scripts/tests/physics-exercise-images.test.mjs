import test from 'node:test'
import assert from 'node:assert/strict'
import { mkdtemp, mkdir, writeFile, readFile, rm } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import path from 'node:path'
import { publishPhysicsExerciseImages } from '../content/publish-physics-exercise-images.mjs'
import { resolveExerciseHtml } from '../../src/features/lecture/services/chapter-exercises.mjs'
import { publishedPhysicsExerciseChapters, physicsExerciseFiles } from '../content/physics-exercise-config.mjs'
import { fileURLToPath } from 'node:url'

test('JSON exercise images are copied byte-for-byte and rewritten for a GitHub Pages base',async()=>{
 const root=await mkdtemp(path.join(tmpdir(),'studyhub-exercise-image-test-'))
 try{
  const folder=path.join(root,'docs/vat-ly-1/bai-giang/img/young-07')
  await mkdir(folder,{recursive:true})
  const original=Buffer.from('<svg xmlns="http://www.w3.org/2000/svg"><text>Hình gốc</text></svg>')
  await writeFile(path.join(folder,'source.svg'),original)
  const source='/vat-ly-1/bai-giang/img/young-07/source.svg'
  const html='<figure><img src="'+source+'"><figcaption>Chú thích tiếng Việt</figcaption></figure><img src="'+source+'">'
  const result=await publishPhysicsExerciseImages(html,{root})
  assert.equal(result.images.length,1)
  const image=result.images[0]
  assert.match(image.publicPath,/^\/physics-exercises\/assets\/[a-f0-9]{16}-source\.svg$/)
  assert.deepEqual(await readFile(path.join(root,'docs/public',image.publicPath)),original)
  assert.equal(result.html.includes(source),false)
  assert.match(resolveExerciseHtml(result.html,'/StudyHub/'),/src="\/StudyHub\/physics-exercises\/assets\//)
  assert(result.html.includes('Chú thích tiếng Việt'))
  assert.deepEqual(await publishPhysicsExerciseImages(html,{root}),result)
 }finally{await rm(root,{recursive:true,force:true})}
})

test('Missing and unsafe image sources stop publication before a complete index is written',async()=>{
 const root=await mkdtemp(path.join(tmpdir(),'studyhub-exercise-image-test-'))
 try{
  await assert.rejects(publishPhysicsExerciseImages('<img src="/vat-ly-1/bai-giang/img/young-07/missing.png">',{root}),/ENOENT/)
  for(const source of ['/vat-ly-1/bai-giang/img/young-07/../../outside.png','https://example.com/pic.png','/secret.png']){
   await assert.rejects(publishPhysicsExerciseImages('<img src="'+source+'">',{root}),/Unsupported exercise image/)
  }
  assert.deepEqual(await publishPhysicsExerciseImages('<p>Không có ảnh</p>',{root}),{html:'<p>Không có ảnh</p>',images:[]})
 }finally{await rm(root,{recursive:true,force:true})}
})

test('Every image used by a published exercise chapter has a supported local source',async()=>{
 const root=fileURLToPath(new URL('../../',import.meta.url)),references=new Set()
 for(const chapter of publishedPhysicsExerciseChapters){
  const nn=String(chapter).padStart(2,'0')
  for(const [,file]of physicsExerciseFiles(chapter)){
   const source=await readFile(path.join(root,'raw_materials/physics/translations/chapter-'+nn,file),'utf8')
   for(const match of source.matchAll(/!\[[^\n]*\]\(([^\s)]+)\)/g)){
    const reference=match[1].replace(/^(?:\.\.\/|\.\/)?img\//,'/vat-ly-1/bai-giang/img/')
    assert.match(reference,/^\/vat-ly-1\/bai-giang\/img\/young-\d{2}\/[a-zA-Z0-9_-]+\.(?:png|svg|webp|jpe?g)$/)
    assert((await readFile(path.join(root,'docs',reference))).length>0,reference)
    references.add(reference)
   }
  }
 }
 assert(references.size>100,'The source audit must cover all published exercise chapters')
})
