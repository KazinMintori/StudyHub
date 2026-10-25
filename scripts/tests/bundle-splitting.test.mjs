import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile, readdir, writeFile, unlink } from 'node:fs/promises'
import path from 'node:path'
import { isDeepStrictEqual } from 'node:util'
import { fileURLToPath, pathToFileURL } from 'node:url'
import { cheatsheets } from '../../src/features/lecture/services/cheatsheet-service.mjs'
import { cheatsheetLoaders } from '../../src/features/lecture/services/cheatsheet-loaders.mjs'
import { courseCatalog } from '../../src/content/catalog.mjs'
import { liteCourse, renderLiteCatalogModule, HEAVY_COURSE_FIELDS } from '../build/lite-catalog-plugin.mjs'
import { dropUnusedPreloads } from '../build/page-preloads.mjs'
import { mathTextPlugin, CLIENT_UNUSED_EXPORT } from '../math-text-plugin.mjs'
import { mathSegments } from '../../src/core/math/services/math-text.mjs'

const root = path.resolve(fileURLToPath(new URL('../../', import.meta.url)))

test('lazy cheatsheet loaders cover exactly the registered cheatsheets', async () => {
  assert.deepEqual(Object.keys(cheatsheetLoaders).sort(), Object.keys(cheatsheets).sort())
  for (const [key, load] of Object.entries(cheatsheetLoaders)) {
    assert.equal(await load(), cheatsheets[key], `${key} loads a different object`)
  }
})

test('client catalog keeps navigation fields and drops slide decks', async () => {
  for (const course of courseCatalog) {
    const lite = liteCourse(course)
    for (const field of HEAVY_COURSE_FIELDS) assert.equal(field in lite, false)
    for (const [key, value] of Object.entries(course)) {
      if (!HEAVY_COURSE_FIELDS.includes(key)) assert.equal(lite[key], value, `${course.id}.${key}`)
    }
  }
  const code = await renderLiteCatalogModule()
  const json = code.match(/JSON\.parse\((".*")\)/s)[1]
  const lite = JSON.parse(JSON.parse(json))
  assert.deepEqual(lite.map(course => course.id), courseCatalog.map(course => course.id))
  assert.deepEqual(lite.map(course => course.lessons.map(lesson => lesson.slug)), courseCatalog.map(course => course.lessons.map(lesson => lesson.slug)))
  assert(code.length < 400_000, `client catalog grew to ${code.length} bytes`)
})

test('Mermaid preload is kept only on pages with a diagram', () => {
  const head = '<link rel="modulepreload" href="/StudyHub/assets/chunks/framework.abc.js">\n    <link rel="modulepreload" href="/StudyHub/assets/chunks/mermaid-render.Ab-12.js">'
  assert.equal(dropUnusedPreloads(`${head}<div>no diagram</div>`).includes('mermaid-render'), false)
  assert.equal(dropUnusedPreloads(`${head}<div>no diagram</div>`).includes('framework.abc.js'), true)
  assert.equal(dropUnusedPreloads(`${head}<div class="mermaid"></div>`).includes('mermaid-render'), true)
})

async function evaluateTransformed(file, ssr) {
  const plugin = mathTextPlugin()
  const absolute = path.join(root, file)
  const out = plugin.transform(await readFile(absolute, 'utf8'), absolute, { ssr })
  const temporary = path.join(path.dirname(absolute), `.bundle-test-${process.pid}-${path.basename(file)}`)
  const registry = {}
  globalThis.__bundleTestMath = registry
  await writeFile(temporary, out.code.replace("import { renderedMath as studyRenderedMath } from 'virtual:study-math-renderer';", 'const studyRenderedMath = globalThis.__bundleTestMath;'))
  try {
    return { module: await import(pathToFileURL(temporary).href), math: registry, code: out.code }
  } finally {
    await unlink(temporary)
  }
}

test('export-scoped math keeps module data identical', async () => {
  for (const file of ['docs/.vitepress/physics-foundations.mjs', 'docs/.vitepress/xstk-foundations.mjs', 'docs/.vitepress/physics-dc-course.mjs']) {
    const original = await import(pathToFileURL(path.join(root, file)).href)
    const { module, code } = await evaluateTransformed(file, true)
    for (const key of Object.keys(original)) {
      if (typeof original[key] !== 'function') assert(isDeepStrictEqual(module[key], original[key]), `${file}: ${key}`)
    }
    assert.match(code, /\/\*#__PURE__\*\/__studyWithMath\(/)
  }
})

test('every generated Physics1 cheatsheet formula has a compiled math entry', async () => {
  const { module, math } = await evaluateTransformed('docs/.vitepress/physics1-priority-course.mjs', false)
  let checked = 0
  for (const [chapter, course] of Object.entries(module.physics1PriorityCourseData)) {
    const formulas = course.cheatsheet.sections.flatMap(section =>
      section.items.flatMap(item => (item.formulaRows || []).map(row => row.formula)))
    for (const formula of formulas) {
      for (const segment of mathSegments(formula).filter(part => part.startsWith('$'))) {
        assert(math[segment]?.includes('<mjx-container'), 'Chapter '+chapter+': Missing compiled '+segment)
        checked++
      }
    }
  }
  assert(checked > 100, 'The check must cover all seven chapter cheatsheets')
})

test('client bundles skip rendered math for server-only Wiki article bodies', async () => {
  const server = await evaluateTransformed('docs/.vitepress/physics-dc-foundations.mjs', true)
  const client = await evaluateTransformed('docs/.vitepress/physics-dc-foundations.mjs', false)
  assert(Object.keys(client.math).length < Object.keys(server.math).length)
  // Browser code never reads these exports.
  const sources = []
  async function walk(directory) {
    for (const entry of await readdir(directory, { withFileTypes: true })) {
      const file = path.join(directory, entry.name)
      if (entry.isDirectory()) await walk(file)
      else if (/\.(vue|js|mjs)$/.test(entry.name) && !/\.test\./.test(entry.name)) sources.push(file)
    }
  }
  await walk(path.join(root, 'src'))
  await walk(path.join(root, 'docs/.vitepress/theme'))
  for (const file of sources) {
    const text = await readFile(file, 'utf8')
    for (const name of text.match(/\b\w+WikiDetails\b|\bwikiDetails\b/g) || []) {
      assert.equal(CLIENT_UNUSED_EXPORT.test(name) || name === 'wikiDetails', false, `${path.relative(root, file)} reads ${name}`)
    }
  }
})

test('new Physics1 chapter modules compile every formula and variable legend', async () => {
  for (const chapter of [1,3,4,5,6,7,8,12,13]) {
    const nn=String(chapter).padStart(2,'0')
    const {module,math}=await evaluateTransformed('docs/.vitepress/physics1-remaining-ch'+nn+'-course.mjs',false)
    const data=module['physics1RemainingChapter'+chapter+'Parent']
    let checked=0
    for(const section of data.cheatsheet.sections)for(const item of section.items){
      const values=[...(item.formulaRows||[]).map(row=>row.formula),...(item.variables||[])]
      for(const value of values)for(const segment of mathSegments(value).filter(part=>part.startsWith('$'))){
        assert(math[segment]?.includes('<mjx-container'),'Chapter '+chapter+': Uncompiled '+segment)
        checked++
      }
    }
    assert(checked>=20,'Each new chapter must contain its full formula sheet')
  }
})

test('theme entry does not statically import data-heavy modules', async () => {
  const theme = await readFile(path.join(root, 'src/app/theme.mjs'), 'utf8')
  const layout = await readFile(path.join(root, 'src/app/StudyLayout.vue'), 'utf8')
  for (const source of [theme, layout]) {
    assert.doesNotMatch(source, /^import .*(Wiki(Index|Usage|Footer)|LegacyCourseRoute|concepts\.mjs|wiki-content\.mjs|cheatsheet-service)/m)
  }
  const model = await readFile(path.join(root, 'src/features/lecture/services/lecture-model.mjs'), 'utf8')
  assert.doesNotMatch(model, /cheatsheet-service/)
  const panels = await readFile(path.join(root, 'src/features/lecture/controllers/useLecturePanels.js'), 'utf8')
  assert.doesNotMatch(panels, /concepts\.mjs|course-labs\.mjs/)
  const preview = await readFile(path.join(root, 'src/features/wiki/controllers/useTermPreview.js'), 'utf8')
  assert.doesNotMatch(preview, /^import .*(concepts|wiki-content)\.mjs/m)
})
