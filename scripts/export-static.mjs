import { cp, mkdir, readdir, writeFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const root = fileURLToPath(new URL('../', import.meta.url))
const source = path.join(root, 'docs/.vitepress/dist')
// Keep the root index.html usable by ordinary static servers, as in the original project.
// VitePress remains the editable source of the site under docs/.
for (const entry of await readdir(source, { withFileTypes: true })) {
  await cp(path.join(source, entry.name), path.join(root, entry.name), { recursive: true, force: true })
}
await mkdir(path.join(root, 'dist'), { recursive: true })
await cp(source, path.join(root, 'dist'), { recursive: true, force: true })
await writeFile(path.join(root, '.static-export.json'), JSON.stringify({ files: (await readdir(source)), generated: new Date().toISOString() }, null, 2))
console.log('Static site exported to dist/ and root index.html.')
