import test from 'node:test'
import assert from 'node:assert/strict'
import { mkdtemp, mkdir, writeFile, readFile, rm, lstat } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import path from 'node:path'
import { git } from '../content/course-repositories.mjs'
import { cleanWorkspace } from '../maintenance/workspace.mjs'

async function fixture(t) {
  const root = await mkdtemp(path.join(tmpdir(), 'studyhub-clean-'))
  t.after(() => rm(root, { recursive:true, force:true }))
  const directory = path.join(root, '.course-repositories/sample')
  await mkdir(directory, {recursive:true})
  const command = args => git(args, {cwd:directory})
  await command(['init','--quiet','-b','main'])
  await command(['config','user.name','Cleanup Test'])
  await command(['config','user.email','cleanup@example.invalid'])
  await writeFile(path.join(directory,'lesson.md'),'published')
  await command(['add','.'])
  await command(['commit','--quiet','-m','Published'])
  const remote = path.join(root,'remote.git')
  await git(['clone','--quiet','--bare',directory,remote])
  await command(['remote','add','origin',remote])
  const revision = (await command(['rev-parse','HEAD'])).trim()
  const lock = {version:1,courses:[{id:'sample',repository:'StudyHub/sample',revision,paths:['docs/sample/**']}]}
  await mkdir(path.join(root,'config'))
  const save = () => writeFile(path.join(root,'config/course-repositories.json'),JSON.stringify(lock))
  await save()
  await mkdir(path.join(root,'docs/.vitepress/cache'),{recursive:true})
  await writeFile(path.join(root,'docs/authored.md'),'keep my source')
  return {root,directory,command,lock,save}
}
test('cleanup removes published clean clones and caches while retaining authored sources',async t=>{
  const {root,directory}=await fixture(t)
  await cleanWorkspace({workspaceRoot:root})
  await assert.rejects(lstat(directory),{code:'ENOENT'})
  await assert.rejects(lstat(path.join(root,'docs/.vitepress/cache')),{code:'ENOENT'})
  assert.equal(await readFile(path.join(root,'docs/authored.md'),'utf8'),'keep my source')
})
test('cleanup retains modified files and clean commits that have not been published',async t=>{
  const {root,directory,command,lock,save}=await fixture(t)
  await writeFile(path.join(directory,'lesson.md'),'unpublished work')
  await cleanWorkspace({workspaceRoot:root})
  assert.equal(await readFile(path.join(directory,'lesson.md'),'utf8'),'unpublished work')
  await command(['add','.']); await command(['commit','--quiet','-m','Local only'])
  lock.courses[0].revision=(await command(['rev-parse','HEAD'])).trim(); await save()
  await cleanWorkspace({workspaceRoot:root})
  assert.equal(await readFile(path.join(directory,'lesson.md'),'utf8'),'unpublished work')
})
