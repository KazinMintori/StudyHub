import { open, readFile, unlink, mkdir, mkdtemp, rm, rename, writeFile } from 'node:fs/promises'
import { spawn } from 'node:child_process'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { mergeBatch, finalizeBatches } from './merge-batches.mjs'

if (process.env.GITHUB_ACTIONS !== 'true') {
  throw new Error('Full site builds run on GitHub Actions only. Use the lecture checker or npm run dev locally.')
}
if (process.argv.length > 2) throw new Error('The managed full build does not accept CLI overrides')

const root = path.resolve(fileURLToPath(new URL('../../', import.meta.url)))
const lockPath = path.join(root, 'docs/.vitepress/.studyhub-build.lock')
const owner = JSON.stringify({ pid: process.pid, started: new Date().toISOString() })
const heapMb = 8192

async function acquireLock() {
  try {
    const file = await open(lockPath, 'wx')
    await file.writeFile(owner)
    await file.close()
    return
  } catch (error) {
    if (error.code !== 'EEXIST') throw error
  }
  const previous = await readFile(lockPath, 'utf8')
  let record
  try { record = JSON.parse(previous) } catch { throw new Error(`Invalid build lock: ${lockPath}`) }
  if (!Number.isInteger(record.pid) || record.pid <= 0) throw new Error(`Invalid build owner: ${lockPath}`)
  try {
    process.kill(record.pid, 0)
    throw new Error(`Another StudyHub build is running (PID ${record.pid}). Wait for it to finish.`)
  } catch (error) {
    if (error.code === 'EPERM') throw new Error(`Another StudyHub build is running or its owner cannot be inspected (PID ${record.pid}). Wait for it to finish.`)
    if (error.code !== 'ESRCH') throw error
  }
  // Remove only a stale lock whose contents have not changed during inspection.
  if (await readFile(lockPath, 'utf8') !== previous) throw new Error('Build ownership changed. Retry after the running build finishes.')
  await unlink(lockPath)
  const file = await open(lockPath, 'wx')
  await file.writeFile(owner)
  await file.close()
}

function run(args) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, args, { cwd: root, stdio: 'inherit', windowsHide: true })
    child.once('error', reject)
    child.once('exit', (code, signal) => code === 0 ? resolve() : reject(new Error(`Build command failed (${signal || code}): ${args.join(' ')}`)))
  })
}

await acquireLock()
let runDirectory
try {
  await run(['scripts/sync-courses.mjs'])
  await run(['scripts/content/generate-physics-exercises.mjs'])
  const cache = path.join(root, 'docs/.vitepress/cache')
  await mkdir(cache, { recursive: true })
  runDirectory = await mkdtemp(path.join(cache, 'studyhub-build-'))
  const planFile = path.join(runDirectory, 'plan.json')
  const worker = ['--max-old-space-size=' + heapMb, 'scripts/build/build-batch-worker.mjs']
  await run([...worker, 'plan', 'docs', planFile])
  const plan = JSON.parse(await readFile(planFile, 'utf8'))
  const merged = path.join(runDirectory, 'merged')
  await mkdir(merged)
  const state = { pageMap: {}, files: new Map(), icons: new Set() }
  console.log(`Building ${plan.pages.length} pages in ${plan.batches.length} sequential batches`)
  for (let index = 0; index < plan.batches.length; index++) {
    const output = path.join(runDirectory, 'batch-' + index)
    await run([...worker, 'batch', 'docs', planFile, String(index), output])
    await mergeBatch(output, merged, state)
    await rm(output, { recursive: true })
  }
  const report = await finalizeBatches(merged, plan, state)
  const destination = path.join(root, 'docs/.vitepress/dist')
  // Both paths are fixed children of this checkout. Publish only a completely
  // merged build; failed batches never produce an uploadable dist directory.
  await rm(destination, { recursive: true, force: true })
  await rename(merged, destination)
  await writeFile(path.join(cache, 'last-build.json'), JSON.stringify({ ...report, batches: plan.batches.length }, null, 2))
  console.log(`Merged ${report.pages} pages and ${report.chunks} routes`)
} finally {
  if (runDirectory) await rm(runDirectory, { recursive: true, force: true })
  if (await readFile(lockPath, 'utf8').catch(() => null) === owner) await unlink(lockPath)
}
