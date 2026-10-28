import test from 'node:test'
import assert from 'node:assert/strict'
import { mkdtemp, mkdir, writeFile, readFile, symlink, rm } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import path from 'node:path'
import { digest, git, safePath, matchesPath, validateLock, verifyPackage, planInstall, exportCourse, pinCourse } from '../content/course-repositories.mjs'

const course = { id: 'sample', repository: 'StudyHub/sample', revision: 'a'.repeat(40), paths: ['docs/sample/**', 'src/content/courses/sample/**'] }
async function fixture(t) {
  const root = await mkdtemp(path.join(tmpdir(), 'studyhub-courses-'))
  t.after(() => rm(root, { recursive: true, force: true }))
  async function put(file, value) { await mkdir(path.dirname(path.join(root, file)), { recursive: true }); await writeFile(path.join(root, file), value) }
  return { root, put }
}

test('repository pins reject branches, duplicate courses and application paths', () => {
  assert.equal(validateLock({ version: 1, courses: [course] }).courses.length, 1)
  for (const courses of [[{ ...course, revision: 'main' }], [course, course], [{ ...course, paths: ['docs/.vitepress/config.mjs'] }]]) assert.throws(() => validateLock({ version: 1, courses }))
  for (const file of ['../secrets', '/absolute', 'docs/../app', 'docs\\sample', 'C:/app', 'docs/.git/config', 'docs/CON.txt']) assert.throws(() => safePath(file))
  assert(matchesPath('docs/sample/lesson/image.svg', 'docs/sample/**'))
  assert(!matchesPath('docs/another/lesson.md', 'docs/sample/**'))
})

test('packages require complete, owned and checksum-verified sources', async t => {
  const { root, put } = await fixture(t)
  const files = { 'docs/sample/index.md': 'A lesson', 'src/content/courses/sample/course.mjs': 'export const course = {}' }
  for (const [file, value] of Object.entries(files)) await put(file, value)
  const manifest = { version: 1, id: 'sample', files: Object.fromEntries(Object.entries(files).map(([file, value]) => [file, digest(value)])) }
  await put('studyhub-course.json', JSON.stringify(manifest))
  assert.equal((await verifyPackage(course, root)).length, 2)
  await put('docs/sample/index.md', 'changed')
  await assert.rejects(verifyPackage(course, root), /checksum/)
  manifest.files['docs/.vitepress/config.mjs'] = digest('bad')
  await put('studyhub-course.json', JSON.stringify(manifest))
  await put('docs/sample/index.md', files['docs/sample/index.md'])
  await assert.rejects(verifyPackage(course, root), /Unowned/)
})

test('install planning preserves dirty content and never writes a partial update', async t => {
  const { root, put } = await fixture(t)
  const file = 'docs/sample/index.md'
  await put(file, 'local edits')
  await assert.rejects(planInstall(root, [{ file, hash: digest('new') }, { file: 'docs/sample/new.md', hash: digest('new') }], { [file]: digest('old') }), /Local edits/)
  assert.equal(await readFile(path.join(root, file), 'utf8'), 'local edits')
  await put(file, 'old')
  const plan = await planInstall(root, [{ file, hash: digest('new') }], { [file]: digest('old') })
  assert.equal(plan.operations[0].action, 'copy')
  assert.equal(await readFile(path.join(root, file), 'utf8'), 'old')
  await assert.rejects(planInstall(root, [], { [file]: digest('different') }), /Locally edited/)
  assert.equal((await planInstall(root, [], { [file]: digest('old') })).operations[0].action, 'delete')
})

test('duplicate ownership fails even when both packages have identical content', async t => {
  const { root } = await fixture(t)
  const entry = { file: 'docs/sample/index.md', hash: digest('same') }
  await assert.rejects(planInstall(root, [entry, entry]), /Two courses/)
})

test('authoring exports changed and new files, refreshes checksums and pins a committed revision', async t => {
  const { root, put } = await fixture(t)
  const directory = path.join(root, '.course-repositories/sample')
  await mkdir(directory, { recursive: true })
  await git(['init', '--quiet'], { cwd: directory })
  await put('config/course-repositories.json', JSON.stringify({ version: 1, courses: [course] }))
  const initial = { 'docs/sample/index.md': 'old', 'src/content/courses/sample/course.mjs': 'export const course = {}' }
  for (const [file, value] of Object.entries(initial)) await put('.course-repositories/sample/' + file, value)
  await put('.course-repositories/sample/studyhub-course.json', JSON.stringify({ version: 1, id: 'sample', files: Object.fromEntries(Object.entries(initial).map(([file, value]) => [file, digest(value)])) }))
  await git(['add', '.'], { cwd: directory })
  await git(['-c', 'user.name=StudyHub Test', '-c', 'user.email=test@studyhub.invalid', 'commit', '--quiet', '-m', 'Initial'], { cwd: directory })
  for (const [file, value] of Object.entries(initial)) await put(file, value)
  await put('docs/sample/index.md', 'new lesson')
  await put('docs/sample/new.md', 'new topic')
  await exportCourse('sample', { root })
  assert.equal((await verifyPackage(course, directory)).length, 3)
  assert.equal(await readFile(path.join(directory, 'docs/sample/index.md'), 'utf8'), 'new lesson')
  await assert.rejects(exportCourse('sample', { root }), /Commit or preserve/)
  await git(['add', '.'], { cwd: directory })
  await git(['-c', 'user.name=StudyHub Test', '-c', 'user.email=test@studyhub.invalid', 'commit', '--quiet', '-m', 'Update'], { cwd: directory })
  const revision = (await git(['rev-parse', 'HEAD'], { cwd: directory })).trim()
  await pinCourse('sample', revision, { root })
  assert.equal(JSON.parse(await readFile(path.join(root, 'config/course-repositories.json'), 'utf8')).courses[0].revision, revision)
})
