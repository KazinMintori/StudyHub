import { readdir, lstat } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('../../', import.meta.url))
let skippedLinks = 0
async function measure(directory) {
  let bytes = 0, files = 0
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name)
    const stat = await lstat(file)
    if (stat.isSymbolicLink()) { skippedLinks++; continue }
    if (stat.isDirectory()) {
      const child = await measure(file)
      bytes += child.bytes; files += child.files
    } else if (stat.isFile()) { bytes += stat.size; files++ }
  }
  return { bytes, files }
}
const rows = []
for (const entry of await readdir(root, { withFileTypes: true })) {
  const file = path.join(root, entry.name)
  const stat = await lstat(file)
  if (stat.isSymbolicLink()) { skippedLinks++; continue }
  const size = stat.isDirectory() ? await measure(file) : { bytes: stat.size, files: 1 }
  rows.push({ path: entry.name, ...size })
}
rows.sort((a, b) => b.bytes - a.bytes)
const result = { root, logicalBytes: rows.reduce((n, r) => n + r.bytes, 0), skippedLinks, rows }
if (process.argv.includes('--json')) console.log(JSON.stringify(result, null, 2))
else {
  console.table(rows.map(r => ({ path: r.path, GiB: (r.bytes / 2**30).toFixed(3), files: r.files })))
  console.log(`Total logical size: ${(result.logicalBytes / 2**30).toFixed(3)} GiB. Skipped ${skippedLinks} links/junctions.`)
}
