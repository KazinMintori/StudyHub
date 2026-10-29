import { lstat, readFile, readdir, rm, symlink } from 'node:fs/promises'
import { spawn } from 'node:child_process'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { git, syncCourses, validateLock } from '../content/course-repositories.mjs'

const root = fileURLToPath(new URL('../../', import.meta.url))
async function exists(file) { try { await lstat(file); return true } catch (error) { if (error.code === 'ENOENT') return false; throw error } }
async function noLinks(file) {
  const info = await lstat(file)
  if (info.isSymbolicLink()) throw Error(`Preserve link/junction: ${file}`)
  if (info.isDirectory()) for (const entry of await readdir(file)) await noLinks(path.join(file, entry))
}
async function remove(relative, workspaceRoot = root) {
  const target = path.resolve(workspaceRoot, relative)
  if (!target.startsWith(path.resolve(workspaceRoot) + path.sep)) throw Error('Cleanup outside workspace refused')
  if (!await exists(target)) return
  await noLinks(target)
  await rm(target, { recursive: true })
  console.log(`Removed ${relative}`)
}
export async function cleanWorkspace({ workspaceRoot = root } = {}) {
  // These are disposable caches, never authored course files or QA evidence.
  for (const relative of ['docs/.vitepress/cache', 'docs/.vitepress/.temp']) await remove(relative, workspaceRoot)
  const lock = validateLock(JSON.parse(await readFile(path.join(workspaceRoot, 'config/course-repositories.json'), 'utf8')))
  for (const course of lock.courses) {
    const relative = `.course-repositories/${course.id}`
    const directory = path.join(workspaceRoot, relative)
    if (!await exists(directory)) continue
    if ((await git(['status', '--porcelain', '--untracked-files=all'], { cwd: directory })).trim()) {
      console.log(`Preserved edited course checkout: ${course.id}`)
      continue
    }
    // Also retain clean but unpublished local commits.
    const head = (await git(['rev-parse', 'HEAD'], { cwd: directory })).trim()
    if (head !== course.revision) { console.log(`Preserved unpinned course checkout: ${course.id}`); continue }
    const published = (await git(['ls-remote', 'origin', 'refs/heads/main'], { cwd: directory })).split(/\s/)[0]
    if (published !== head) { console.log(`Preserved checkout without matching remote proof: ${course.id}`); continue }
    await remove(relative, workspaceRoot)
  }
}
function run(args, forwardSignals = false) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, args, { cwd: root, stdio: 'inherit', windowsHide: true, env: { ...process.env, PUPPETEER_SKIP_DOWNLOAD: 'true' } })
    const stop = () => child.kill('SIGINT')
    if (forwardSignals) { process.on('SIGINT', stop); process.on('SIGTERM', stop) }
    const finish = () => { if (forwardSignals) { process.off('SIGINT', stop); process.off('SIGTERM', stop) } }
    child.once('error', error => { finish(); reject(error) })
    child.once('exit', (code, signal) => { finish(); code === 0 || signal === 'SIGINT' || signal === 'SIGTERM' ? resolve() : reject(Error(`Command failed: ${code ?? signal}`)) })
  })
}
async function prepare() {
  if (!await exists(path.join(root, 'node_modules/vitepress/bin/vitepress.js'))) {
    const common = (await git(['rev-parse', '--git-common-dir'], {cwd:root})).trim()
    const primary = path.dirname(path.resolve(root, common))
    const primaryModules = path.join(primary, 'node_modules')
    const sameLock = primary !== path.resolve(root) && await exists(primaryModules) && (await readFile(path.join(root,'package-lock.json'))).equals(await readFile(path.join(primary,'package-lock.json')))
    if (sameLock && !await exists(path.join(root,'node_modules'))) {
      await symlink(primaryModules, path.join(root,'node_modules'), process.platform === 'win32' ? 'junction' : 'dir')
      console.log('Reusing the primary checkout dependency installation')
    } else {
      if (!process.env.npm_execpath) throw Error('Run through npm run workspace:prepare')
      await run([process.env.npm_execpath, 'ci'])
    }
  }
  await syncCourses({ root })
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const command = process.argv[2]
  if (command === 'clean') await cleanWorkspace()
  else if (command === 'prepare') await prepare()
  else if (command === 'dev') {
    try {
      await prepare()
      await run([path.join(root, 'node_modules/vitepress/bin/vitepress.js'), 'dev', 'docs', ...process.argv.slice(3)], true)
    } finally { await cleanWorkspace() }
  } else throw Error('Use prepare, clean or dev')
}
