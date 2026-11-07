import assert from 'node:assert/strict'
import {access,readFile} from 'node:fs/promises'

// Run against the fresh cloud build: archived source must not emit HTML routes.
for(const file of ['index.html','thuc-hanh.html','ket-qua-porto.html']) {
  const target=`docs/.vitepress/dist/xu-ly-du-lieu/bai-tap-lon/${file}`
  let exists=true
  try {await access(target)}catch(error){if(error.code==='ENOENT')exists=false;else throw error}
  assert(!exists,`Unpublished project route was generated: ${target}`)
}
const overview=await readFile('docs/.vitepress/dist/xu-ly-du-lieu/index.html','utf8')
assert(!overview.includes('/xu-ly-du-lieu/bai-tap-lon/'),'Overview still links to the unpublished project')
console.log('PASS project routes absent from published HTML and course navigation')
