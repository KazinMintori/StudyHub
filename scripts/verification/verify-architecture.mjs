import { readdir, readFile, access } from 'node:fs/promises'
import path from 'node:path'
import assert from 'node:assert/strict'
import { parseAst } from 'rollup/parseAst'
import { fileURLToPath } from 'node:url'

const root = path.resolve(fileURLToPath(new URL('../../', import.meta.url)))
const exists = async file => { try { await access(file); return true } catch { return false } }
async function* files(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name)
    if (entry.isDirectory()) yield* files(file)
    else if (entry.isFile()) yield file
  }
}
const errors = []
const exportedNames = new Map()
async function resolveModule(file, spec) {
  const target = path.resolve(path.dirname(file), spec)
  for (const candidate of [target, ...['.js','.mjs','.vue'].map(ext => target + ext)]) {
    if (await exists(candidate)) return candidate
  }
  return null
}
function declaredNames(node) {
  if (!node) return []
  if (node.type === 'Identifier') return [node.name]
  if (node.type === 'ObjectPattern') return node.properties.flatMap(p => declaredNames(p.value || p.argument))
  if (node.type === 'ArrayPattern') return node.elements.flatMap(declaredNames)
  return []
}
async function moduleExports(file) {
  if (exportedNames.has(file)) return exportedNames.get(file)
  const names = new Set()
  exportedNames.set(file, names)
  if (file.endsWith('.vue')) { names.add('default'); return names }
  if (!/\.m?js$/.test(file)) return names
  const ast = parseAst(await readFile(file, 'utf8'))
  for (const node of ast.body) {
    if (node.type === 'ExportDefaultDeclaration') names.add('default')
    if (node.type === 'ExportNamedDeclaration') {
      for (const spec of node.specifiers || []) names.add(spec.exported.name || spec.exported.value)
      if (node.declaration?.type === 'VariableDeclaration') {
        for (const item of node.declaration.declarations) for (const name of declaredNames(item.id)) names.add(name)
      } else if (node.declaration?.id) names.add(node.declaration.id.name)
    }
  }
  for (const node of ast.body) if (node.type === 'ExportAllDeclaration' && node.source.value.startsWith('.')) {
    const target = await resolveModule(file, node.source.value)
    if (target) for (const name of await moduleExports(target)) if (name !== 'default') names.add(name)
  }
  return names
}
let modules = 0, manifests = 0
for await (const file of files(path.join(root, 'src'))) {
  const relative = path.relative(root, file).replaceAll('\\', '/')
  const source = await readFile(file, 'utf8')
  if (relative.endsWith('/content.json')) {
    const manifest = JSON.parse(source)
    // Explicit null means this course omits an optional panel. Missing fields,
    // unresolved assets and empty paths still fail verification.
    const panels = [manifest.slides, manifest.cheatsheet].filter(file => file !== null)
    for (const sourceFile of [manifest.notes, ...panels, ...manifest.topics.map(t => t.source), ...manifest.fragments, ...(manifest.assets || []).filter(a => !a.external).map(a => a.source)]) {
      if (!sourceFile) { errors.push(`${relative}: Unresolved local asset`); continue }
      if (!await exists(path.join(root, sourceFile))) errors.push(`${relative}: Missing content source ${sourceFile}`)
    }
    manifests++
    continue
  }
  if (!/\.(vue|m?js)$/.test(file) || /(?:__tests__|\/tests\/|\.test\.)/.test(relative)) continue
  const script = relative.endsWith('.vue') ? source.match(/<script(?:\s+setup)?[^>]*>([\s\S]*?)<\/script>/)?.[1] : source
  if (!script) continue
  const ast = parseAst(script)
  modules++
  for (const node of ast.body) {
    if (!['ImportDeclaration', 'ExportNamedDeclaration', 'ExportAllDeclaration'].includes(node.type) || !node.source) continue
    const spec = node.source.value
    if (relative.includes('/services/') && (['vue', 'vitepress'].includes(spec) || spec.startsWith('vitepress/') || /\.vue$|\/controllers\//.test(spec))) errors.push(`${relative}: Service imports UI/controller ${spec}`)
    if (relative.startsWith('src/core/') && /(?:^|\/)features\//.test(spec)) errors.push(`${relative}: Core imports a feature ${spec}`)
    if (relative.startsWith('src/content/') && (['vue', 'vitepress'].includes(spec) || /\.vue$|\/controllers\//.test(spec))) errors.push(`${relative}: Content imports UI ${spec}`)
    if (spec.startsWith('.')) {
      const target = await resolveModule(file, spec)
      if (!target) errors.push(`${relative}: Missing import ${spec}`)
      else if (/\.m?js$/.test(target)) {
        const exported = await moduleExports(target)
        for (const imported of node.specifiers || []) {
          const name = imported.type === 'ImportDefaultSpecifier' ? 'default' : imported.imported?.name || imported.imported?.value
          if (name && !exported.has(name)) errors.push(`${relative}: ${spec} has no export ${name}`)
        }
      }
    }
  }
}
assert.deepEqual(errors, [], errors.join('\n'))
console.log(`PASS ${modules} modules: Resolved imports and service/core/content dependency boundaries; ${manifests} complete lecture ownership indexes.`)
