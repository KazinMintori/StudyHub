import assert from 'node:assert/strict'
import {readFile,access} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {buildThemeConfig} from '../src/features/course/services/build-navigation.mjs'

const root='raw_materials/xu-ly-du-lieu/bai-tap-lon'
const manifest=JSON.parse(await readFile(`${root}/source-manifest.json`,'utf8'))
for(const source of manifest){
 const bytes=await readFile(`${root}/${source.file}`)
 assert.equal(bytes.length,source.bytes)
 assert.equal(createHash('sha256').update(bytes).digest('hex'),source.sha256)
}
const coverage=JSON.parse(await readFile(`${root}/coverage.json`,'utf8'))
const brief=await readFile('docs/xu-ly-du-lieu/bai-tap-lon/index.md','utf8')
assert.equal(coverage.sourceSha256,manifest.find(s=>s.file==='project-airbnb.html').sha256)
assert.equal(new Set(coverage.requirements.map(r=>r.id)).size,coverage.requirements.length)
for(const requirement of coverage.requirements){
 assert(requirement.requirement.trim())
 assert(brief.includes(requirement.targetHeading),`${requirement.id}: target heading`)
 for(const marker of requirement.presentMarkers)assert(brief.includes(marker),`${requirement.id}: missing ${marker}`)
}
for(const file of ['index.md','thuc-hanh.md']){
 const body=await readFile(`docs/xu-ly-du-lieu/bai-tap-lon/${file}`,'utf8')
 assert.equal((body.match(/^# /gm)||[]).length,1,`${file}: one page title`)
 assert(body.includes('section: project'))
 assert(!/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(body),`${file}: no escape corruption`)
 for(const match of body.matchAll(/^import .*? from '([^']+)'/gm)){
  const path=await import('node:path')
  await access(path.resolve('docs/xu-ly-du-lieu/bai-tap-lon',match[1]))
 }
}
const sidebar=buildThemeConfig({courseCatalog:[{id:'xu-ly-du-lieu',name:'Dữ liệu',lessons:[]}],wikiGroups:[],concepts:{}}).sidebar['/xu-ly-du-lieu/'][0].items
assert.equal(sidebar[sidebar.findIndex(item=>item.text==='Ôn thi')+1].text,'Bài tập lớn')
console.log(`PASS preserved source hashes,${coverage.requirements.length} mapped requirements,2 pages and project navigation. Marker coverage does not prove semantic completeness.`)
