import { createHash } from 'node:crypto'
import { spawn } from 'node:child_process'
import { readFile, writeFile, mkdir, lstat, readdir, copyFile, unlink, chmod } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

export const repositoryRoot = fileURLToPath(new URL('../../', import.meta.url))
export const digest = data => createHash('sha256').update(data).digest('hex')
const optionalRead = file => readFile(file).catch(error => { if (error.code === 'ENOENT') return null; throw error })

export function safePath(value) {
  if (typeof value !== 'string' || !value || /[\\:\x00-\x1f]/.test(value) || value.startsWith('/') || value.split('/').some(part => !part || part === '.' || part === '..' || part.endsWith('.') || part.endsWith(' ') || /^(?:\.git|node_modules|con|prn|aux|nul|com\d|lpt\d)(?:\.|$)/i.test(part))) throw Error(`Invalid course path: ${value}`)
  return value
}

export function matchesPath(file, pattern) {
  const escaped = pattern.split('**').map(segment => segment.split('*').map(value => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('[^/]*')).join('.*')
  return new RegExp(`^${escaped}$`).test(file)
}

export function validateLock(lock) {
  if (lock?.version !== 1 || !Array.isArray(lock.courses) || !lock.courses.length) throw Error('Invalid course repository lock')
  const ids = new Set(), repositories = new Set()
  for (const course of lock.courses) {
    if (!/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/.test(course.id) || ids.has(course.id)) throw Error('Invalid or duplicate course ID')
    if (!/^[A-Za-z0-9-]+\/[A-Za-z0-9_.-]+$/.test(course.repository) || repositories.has(course.repository)) throw Error('Invalid or duplicate course repository')
    if (!/^[a-f0-9]{40}$/.test(course.revision)) throw Error(`Pin a full commit SHA for ${course.id}`)
    if (!Array.isArray(course.paths) || !course.paths.length) throw Error(`Missing owned paths for ${course.id}`)
    for (const pattern of course.paths) {
      safePath(pattern)
      if (!['docs/', 'src/content/courses/', 'raw_materials/'].some(prefix => pattern.startsWith(prefix)) || pattern.startsWith('docs/.vitepress/theme/') || pattern === 'docs/.vitepress/config.mjs') throw Error(`Course cannot own application code: ${pattern}`)
    }
    ids.add(course.id); repositories.add(course.repository)
  }
  return lock
}

export async function verifyPackage(course, directory) {
  const manifest = JSON.parse(await readFile(path.join(directory, 'studyhub-course.json'), 'utf8'))
  if (manifest.version !== 1 || manifest.id !== course.id || !manifest.files || Array.isArray(manifest.files)) throw Error(`Invalid package for ${course.id}`)
  const files = []
  const checked = new Set()
  for (const [file, hash] of Object.entries(manifest.files)) {
    safePath(file)
    if (!course.paths.some(pattern => matchesPath(file, pattern)) || !/^[a-f0-9]{64}$/.test(hash)) throw Error(`Unowned or invalid file: ${file}`)
    const absolute = path.join(directory, file)
    await assertNoLinks(directory, file, checked)
    const data = await readFile(absolute)
    if (digest(data) !== hash) throw Error(`Content checksum mismatch: ${file}`)
    const updatedAt = manifest.updatedAt?.[file]
    if (updatedAt != null && (!Number.isFinite(updatedAt) || updatedAt <= 0)) throw Error(`Invalid source timestamp: ${file}`)
    files.push({ file, hash, source: absolute, ...(updatedAt ? { updatedAt } : {}) })
  }
  if (!files.some(entry => entry.file === `src/content/courses/${course.id}/course.mjs`) || !files.some(entry => entry.file.startsWith(`docs/${course.id}/`))) throw Error(`Incomplete package: ${course.id}`)
  return files
}

async function assertNoLinks(root, file, checked = new Set()) {
  let current = root
  for (const segment of safePath(file).split('/')) {
    current = path.join(current, segment)
    if (checked.has(current)) continue
    const stat = await lstat(current).catch(error => { if (error.code === 'ENOENT') return null; throw error })
    if (stat?.isSymbolicLink()) throw Error(`Symlinks are not supported: ${file}`)
    if (stat) checked.add(current)
  }
}

// Plan every write before touching the working copy. A local edit is never
// replaced by a newer pin, and a missing private repository never falls back.
export async function planInstall(root, entries, previous = {}) {
  const files = new Map(), operations = []
  const checked = new Set()
  for (const entry of entries) {
    safePath(entry.file)
    if (files.has(entry.file)) throw Error(`Two courses own ${entry.file}`)
    files.set(entry.file, entry.hash)
    await assertNoLinks(root, entry.file, checked)
    const current = await optionalRead(path.join(root, entry.file))
    const hash = current && digest(current)
    if (hash === entry.hash) continue
    if (hash && hash !== previous[entry.file]) throw Error(`Local edits must be exported before syncing: ${entry.file}`)
    operations.push({ ...entry, action: 'copy' })
  }
  for (const [file, hash] of Object.entries(previous)) {
    safePath(file)
    if (files.has(file)) continue
    await assertNoLinks(root, file, checked)
    const current = await optionalRead(path.join(root, file))
    if (current && digest(current) !== hash) throw Error(`Locally edited file was removed upstream: ${file}`)
    if (current) operations.push({ file, action: 'delete' })
  }
  return { operations, files: Object.fromEntries(files) }
}

export function git(args, { cwd = repositoryRoot, env = process.env } = {}) {
  return new Promise((resolve, reject) => {
    const child = spawn('git', args, { cwd, env: { ...env, GIT_TERMINAL_PROMPT: '0', GCM_INTERACTIVE: 'never' }, windowsHide: true, stdio: ['ignore', 'pipe', 'pipe'] })
    const output = [], errors = []
    child.stdout.on('data', chunk => output.push(chunk)); child.stderr.on('data', chunk => errors.push(chunk))
    child.once('error', reject)
    child.once('exit', code => code === 0 ? resolve(Buffer.concat(output).toString()) : reject(Error(`Git ${args[0]} failed (${code}): ${Buffer.concat(errors).toString().slice(-1500)}`)))
  })
}

export async function syncCourses({ root = repositoryRoot, check = false } = {}) {
  const lock = validateLock(JSON.parse(await readFile(path.join(root, 'config/course-repositories.json'), 'utf8')))
  const cache = path.join(root, '.course-repositories')
  await mkdir(cache, { recursive: true })
  const keys = JSON.parse(process.env.COURSE_DEPLOY_KEYS || '{}')
  const entries = [], secrets = []
  try {
    for (const course of lock.courses) {
      const directory = path.join(cache, course.id)
      await mkdir(directory, { recursive: true })
      let env = process.env
      let remote = `https://github.com/${course.repository}.git`
      if (keys[course.id]) {
        const identity = path.join(cache, `${course.id}.key`)
        secrets.push(identity)
        await writeFile(identity, keys[course.id], { mode: 0o600 }); await chmod(identity, 0o600)
        const knownHosts = path.join(cache, 'known_hosts')
        if (!await optionalRead(knownHosts)) {
          const response = await fetch('https://api.github.com/meta')
          if (!response.ok) throw Error('Cannot verify GitHub SSH host keys')
          const meta = await response.json()
          await writeFile(knownHosts, meta.ssh_keys.map(key => `[ssh.github.com]:443 ${key}`).join('\n') + '\n')
        }
        env = { ...process.env, GIT_SSH_COMMAND: `ssh -i "${identity.replaceAll('\\', '/')}" -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes -o UserKnownHostsFile="${knownHosts.replaceAll('\\', '/')}" -p 443` }
        remote = `git@ssh.github.com:${course.repository}.git`
      }
      if (!await lstat(path.join(directory, '.git')).catch(() => null)) await git(['init', '--quiet'], { cwd: directory, env })
      await git(['config', 'core.autocrlf', 'false'], { cwd: directory, env })
      await git(['config', 'core.longpaths', 'true'], { cwd: directory, env })
      if ((await git(['status', '--porcelain'], { cwd: directory, env })).trim()) throw Error(`Commit course repository edits first: ${course.id}`)
      await git(['fetch', '--quiet', '--depth=1', remote, course.revision], { cwd: directory, env })
      const revision = (await git(['rev-parse', 'FETCH_HEAD'], { cwd: directory, env })).trim()
      if (revision !== course.revision) throw Error(`Unexpected revision: ${course.id}`)
      const tree = await git(['ls-tree', '-r', revision], { cwd: directory, env })
      if (tree.split('\n').some(line => line && !line.startsWith('100644 blob ') && !line.startsWith('100755 blob '))) throw Error(`Unsupported repository entry: ${course.id}`)
      await git(['-c', 'core.autocrlf=false', 'checkout', '--quiet', '--detach', revision], { cwd: directory, env })
      entries.push(...await verifyPackage(course, directory))
      console.log(`Verified ${course.id} @ ${revision.slice(0, 12)}`)
    }
    const statePath = path.join(cache, 'installed.json')
    const previous = JSON.parse((await optionalRead(statePath))?.toString() || '{}')
    const plan = await planInstall(root, entries, previous.files)
    if (check && plan.operations.length) throw Error(`${plan.operations.length} course files need synchronization`)
    if (!check) {
      for (const entry of plan.operations) {
        const target = path.join(root, entry.file)
        if (entry.action === 'delete') await unlink(target)
        else { await mkdir(path.dirname(target), { recursive: true }); await copyFile(entry.source, target) }
      }
      await writeFile(statePath, JSON.stringify({ files: plan.files, updatedAt: Object.fromEntries(entries.filter(entry => entry.updatedAt).map(entry => [entry.file, entry.updatedAt])) }, null, 2) + '\n')
    }
    console.log(`${check ? 'Checked' : 'Synchronized'} ${entries.length} files across ${lock.courses.length} private course repositories`)
    return plan
  } finally {
    for (const secret of secrets) await unlink(secret).catch(() => {})
  }
}

export async function exportCourse(id, { root = repositoryRoot } = {}) {
  const lock = validateLock(JSON.parse(await readFile(path.join(root, 'config/course-repositories.json'), 'utf8')))
  const course = lock.courses.find(course => course.id === id)
  if (!course) throw Error(`Unknown course: ${id}`)
  const directory = path.join(root, '.course-repositories', id)
  if ((await git(['status', '--porcelain'], { cwd: directory })).trim()) throw Error('Commit or preserve edits in the course checkout before exporting')
  const previous = JSON.parse(await readFile(path.join(directory, 'studyhub-course.json'), 'utf8'))
  const candidates = new Set()
  async function collect(relative) {
    await assertNoLinks(root, relative)
    const stat = await lstat(path.join(root, relative)).catch(error => { if (error.code === 'ENOENT') return null; throw error })
    if (!stat) return
    if (stat.isDirectory()) {
      for (const entry of await readdir(path.join(root, relative))) await collect(`${relative}/${entry}`)
    } else if (course.paths.some(pattern => matchesPath(relative, pattern))) {
      // Original source PDFs are kept locally; export only explicitly tracked
      // binaries rather than accidentally uploading large ignored textbooks.
      if (!/\.(?:pdf|pptx)$/i.test(relative) || relative in previous.files) candidates.add(relative)
    }
  }
  for (const pattern of course.paths) {
    const wildcard = pattern.indexOf('*')
    const relative = wildcard < 0 ? pattern : pattern.slice(0, pattern.lastIndexOf('/', wildcard))
    await collect(relative)
  }
  const files = {}
  for (const file of [...candidates].sort()) {
    const data = await readFile(path.join(root, file))
    if (data.length > 50 * 1024 * 1024) throw Error(`Use external document storage for files over 50 MiB: ${file}`)
    files[file] = digest(data)
  }
  if (!files[`src/content/courses/${id}/course.mjs`]) throw Error('Cannot export an incomplete course')
  for (const file of Object.keys(previous.files)) if (!files[file]) await unlink(path.join(directory, safePath(file)))
  for (const file of Object.keys(files)) {
    await assertNoLinks(directory, file)
    await mkdir(path.dirname(path.join(directory, file)), { recursive: true })
    await copyFile(path.join(root, file), path.join(directory, file))
  }
  const updatedAt = Object.fromEntries(Object.entries(files).map(([file, hash]) => [file, previous.files[file] === hash && previous.updatedAt?.[file] || Date.now()]))
  await writeFile(path.join(directory, 'studyhub-course.json'), JSON.stringify({ version: 1, id, files, updatedAt }, null, 2) + '\n')
  console.log(`Exported ${Object.keys(files).length} files to .course-repositories/${id}. Review, commit and push there, then update the main repository pin.`)
}

export async function pinCourse(id, revision, { root = repositoryRoot } = {}) {
  const lockPath = path.join(root, 'config/course-repositories.json')
  const lock = JSON.parse(await readFile(lockPath, 'utf8'))
  const course = lock.courses.find(course => course.id === id)
  if (!course) throw Error(`Unknown course: ${id}`)
  course.revision = revision
  validateLock(lock)
  const directory = path.join(root, '.course-repositories', id)
  if ((await git(['rev-parse', revision], { cwd: directory })).trim() !== revision) throw Error('Commit is not present in the course checkout')
  const manifest = JSON.parse(await git(['show', `${revision}:studyhub-course.json`], { cwd: directory }))
  if (manifest.id !== id) throw Error('The commit belongs to a different course')
  await writeFile(lockPath, JSON.stringify(lock, null, 2) + '\n')
  console.log(`Pinned ${id} to ${revision}. Run npm run courses:sync before verifying the main repository.`)
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const args = process.argv.slice(2)
  if (args[0] === 'export' && args.length === 2) await exportCourse(args[1])
  else if (args[0] === 'pin' && args.length === 3) await pinCourse(args[1], args[2])
  else if (args.length === 0 || args.length === 1 && args[0] === '--check') await syncCourses({ check: args.includes('--check') })
  else throw Error('Usage: course-repositories.mjs [--check | export <course> | pin <course> <commit>]')
}
