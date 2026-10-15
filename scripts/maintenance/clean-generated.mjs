import { lstat, readdir, rm } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { artifactPolicy } from '../../config/artifacts.mjs'

const root = path.resolve(fileURLToPath(new URL('../../', import.meta.url)))
const apply = process.argv.includes('--apply')
async function rejectLinks(file) {
  const stat = await lstat(file)
  if (stat.isSymbolicLink()) throw new Error(`Refusing a link/junction: ${file}`)
  if (stat.isDirectory()) for (const entry of await readdir(file)) await rejectLinks(path.join(file, entry))
}
for (const relative of artifactPolicy.generated) {
  const target = path.resolve(root, relative)
  if (target === root || !target.startsWith(root + path.sep)) throw new Error(`Unsafe artifact path: ${relative}`)
  for (const protectedPath of artifactPolicy.protected) {
    const protectedTarget = path.resolve(root, protectedPath)
    if (target === protectedTarget || target.startsWith(protectedTarget + path.sep) || protectedTarget.startsWith(target + path.sep)) throw new Error(`Protected path overlap: ${relative}`)
  }
  try { await lstat(target) } catch (error) { if (error.code === 'ENOENT') continue; throw error }
  await rejectLinks(target)
  if (apply) await rm(target, { recursive: true })
  console.log(`${apply ? 'Removed' : 'Would remove'} ${relative}`)
}
if (!apply) console.log('Dry run. Stop local builds before running with --apply. Physics QA and authored sources are outside this cleanup scope.')
