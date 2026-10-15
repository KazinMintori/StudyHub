import { cp, mkdir, writeFile, readdir, readFile, lstat, rm } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import path from 'node:path'
import { buildPaths } from '../config/build.mjs'

const root = path.resolve(fileURLToPath(new URL('../', import.meta.url)))
// Normal builds and GitHub Pages use only the VitePress output.
const source = path.join(root, buildPaths.output)
const destination = path.join(root, buildPaths.explicitExport)
if (destination === root || !destination.startsWith(root + path.sep)) throw new Error('Export must stay inside the repository.')
async function verifyNoLinks(directory) {
  const stat = await lstat(directory)
  if (stat.isSymbolicLink()) throw new Error(`Refusing an export link/junction: ${directory}`)
  if (stat.isDirectory()) for (const entry of await readdir(directory)) await verifyNoLinks(path.join(directory, entry))
}
let existing
try { existing = await readdir(destination) } catch (error) { if (error.code !== 'ENOENT') throw error }
if (existing?.length) {
  const marker = JSON.parse(await readFile(path.join(destination, '.studyhub-generated.json'), 'utf8'))
  if (marker.source !== buildPaths.output) throw new Error('Export directory has no matching generated-output marker.')
  await verifyNoLinks(destination)
  await rm(destination, { recursive: true })
} else if (existing) await verifyNoLinks(destination)
await mkdir(destination, { recursive: true })
await cp(source, destination, { recursive: true, force: true })
await writeFile(path.join(destination, '.studyhub-generated.json'), JSON.stringify({
  source: buildPaths.output,
  generated: new Date().toISOString()
}, null, 2))
console.log(`Static site exported explicitly to ${buildPaths.explicitExport}/.`)
