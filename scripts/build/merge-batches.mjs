import { readFile, writeFile, readdir, mkdir, copyFile } from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'

export async function* filesIn(directory, prefix = '') {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const name = path.posix.join(prefix, entry.name)
    if (entry.isDirectory()) yield* filesIn(path.join(directory, entry.name), name)
    else if (entry.isFile()) yield name
    else throw new Error(`Unexpected build output: ${name}`)
  }
}

const digest = data => createHash('sha256').update(data).digest('hex')

export function replacePageMap(html, pageMap) {
  // Match a JSON string literal, not arbitrary script text. Preserve site data
  // and all other head/body scripts byte for byte.
  const pattern = /window\.__VP_HASH_MAP__=JSON\.parse\("(?:[^"\\]|\\.)*"\);/g
  const matches = [...html.matchAll(pattern)]
  if (matches.length !== 1) throw new Error(`Expected one VitePress page map, found ${matches.length}`)
  const json = JSON.stringify(JSON.stringify(pageMap)).replaceAll('<', '\\u003c')
  return html.replace(pattern, () => `window.__VP_HASH_MAP__=JSON.parse(${json});`)
}

export async function mergeBatch(source, target, state) {
  const batchFiles = []
  for await (const file of filesIn(source)) batchFiles.push(file)
  const surfaceFiles = batchFiles.filter(file => /\/framework-surface\.[^/]+\.json$/.test(file))
  if (surfaceFiles.length > 1) throw new Error('A batch must have exactly one shared framework')
  if (surfaceFiles.length) {
    const framework = JSON.parse(await readFile(path.join(source, surfaceFiles[0]), 'utf8'))
    if (!Array.isArray(framework.exports) || !/^assets\/chunks\/framework-shared\.[a-f0-9]+\.js$/.test(framework.alias)) throw new Error('Invalid shared framework surface')
    if (state.sharedFramework) {
      if (state.sharedFramework.alias !== framework.alias || framework.exports.some(name => !state.sharedFramework.exports.includes(name))) throw new Error('Incompatible framework exports across build batches')
    } else state.sharedFramework = framework
  }
  const pageMap = JSON.parse(await readFile(path.join(source, 'hashmap.json'), 'utf8'))
  for (const [key, value] of Object.entries(pageMap)) {
    if (state.pageMap[key] && state.pageMap[key] !== value && key !== '404.md') throw new Error(`Conflicting page hash: ${key}`)
    // Keep the first 404 together with its matching HTML and page hash.
    state.pageMap[key] ??= value
  }
  for (const file of batchFiles) {
    if (file === 'hashmap.json') continue
    const data = await readFile(path.join(source, file))
    if (file === 'vp-icons.css') {
      state.icons.add(data.toString())
      continue
    }
    const hash = digest(data)
    if (state.files.has(file)) {
      if (file === '404.html') continue
      if (file === state.sharedFramework?.alias) continue
      if (state.files.get(file) !== hash) throw new Error(`Build output collision: ${file}`)
      continue
    }
    state.files.set(file, hash)
    const destination = path.join(target, file)
    await mkdir(path.dirname(destination), { recursive: true })
    await copyFile(path.join(source, file), destination)
  }
}

export function replaceFrameworkPreloads(html, framework) {
  if (!framework) return html
  const name = path.posix.basename(framework.alias)
  return html.replace(/(href="[^"\n]*\/chunks\/)framework\.[^/"\n]+\.js"/g, (_, prefix) => `${prefix}${name}"`)
}

export async function finalizeBatches(target, plan, state) {
  const pageMap = Object.fromEntries(Object.entries(state.pageMap).sort(([a], [b]) => a.localeCompare(b, 'en')))
  const rendered = new Set(['404.html'])
  const chunks = new Set()
  for (const file of state.files.keys()) {
    if (!file.startsWith(plan.assetsDir + '/')) continue
    const match = file.slice(plan.assetsDir.length + 1).match(/^(.*\.md)\.([^.]+)(\.lean)?\.js$/)
    // VitePress lowercases map keys but preserves source filename case in its
    // emitted chunks. Hash strings remain case-sensitive.
    if (match) chunks.add(match[1].toLowerCase() + '\0' + match[2] + (match[3] || ''))
  }
  for (const page of plan.pages) {
    const alias = plan.rewrites[page] || page
    const html = alias.replace(/\.md$/, '.html')
    if (!state.files.has(html)) throw new Error(`Missing rendered page: ${html}`)
    rendered.add(html)
  }
  for (const [key, hash] of Object.entries(pageMap)) {
    for (const suffix of ['.js', '.lean.js']) {
      const file = `${plan.assetsDir}/${key}.${hash}${suffix}`
      if (!chunks.has(key + '\0' + hash + (suffix === '.lean.js' ? '.lean' : ''))) throw new Error(`Missing page chunk: ${file}`)
    }
  }
  for (const file of rendered) {
    if (!state.files.has(file)) continue
    const location = path.join(target, file)
    await writeFile(location, replaceFrameworkPreloads(replacePageMap(await readFile(location, 'utf8'), pageMap), state.sharedFramework))
  }
  await writeFile(path.join(target, 'hashmap.json'), JSON.stringify(pageMap))
  await writeFile(path.join(target, 'vp-icons.css'), [...state.icons].join('\n'))
  return { pages: plan.pages.length, chunks: Object.keys(pageMap).length }
}
