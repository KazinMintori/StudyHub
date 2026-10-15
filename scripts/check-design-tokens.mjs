import { readdir, readFile } from 'node:fs/promises'
import assert from 'node:assert/strict'
const violations = []
async function* sourceFiles(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const file = `${directory}/${entry.name}`
    if (entry.isDirectory()) yield* sourceFiles(file)
    else if (entry.isFile()) yield file
  }
}
for (const directory of ['docs/.vitepress/theme', 'src']) {
for await (const file of sourceFiles(directory)) {
  if (!/\.(css|vue|js)$/.test(file) || /\/(tokens|fonts)\.css$/.test(file)) continue
  const text = await readFile(file, 'utf8')
  for (const [i, line] of text.split('\n').entries()) {
    if (/(?:[:='"\s])#[\da-f]{3,8}\b/i.test(line)) violations.push(`${file}:${i+1}: hardcoded color`)
    if (/font-weight:\s*(550|650)/.test(line)) violations.push(`${file}:${i+1}: unsupported weight`)
  }
}
}
assert.deepEqual(violations, [], violations.join('\n'))
console.log('PASS all interface colors use design tokens')
