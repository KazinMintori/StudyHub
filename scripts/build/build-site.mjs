import { open, readFile, unlink } from 'node:fs/promises'
import { spawn } from 'node:child_process'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.resolve(fileURLToPath(new URL('../../', import.meta.url)))
const lockPath = path.join(root, 'docs/.vitepress/.studyhub-build.lock')
const owner = JSON.stringify({ pid: process.pid, started: new Date().toISOString() })
const heapMb = process.env.GITHUB_ACTIONS === 'true' ? 12288 : 8192

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
try {
  await run(['scripts/sync-courses.mjs'])
  await run(['--max-old-space-size=' + heapMb, 'node_modules/vitepress/bin/vitepress.js', 'build', 'docs', ...process.argv.slice(2)])
} finally {
  if (await readFile(lockPath, 'utf8').catch(() => null) === owner) await unlink(lockPath)
}
