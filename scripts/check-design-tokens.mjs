import { readdir, readFile } from 'node:fs/promises'
import assert from 'node:assert/strict'
const directory = 'docs/.vitepress/theme', violations = []
for (const file of await readdir(directory)) {
  if (!/\.(css|vue|js)$/.test(file) || file === 'tokens.css' || file === 'fonts.css') continue
  const text = await readFile(`${directory}/${file}`, 'utf8')
  for (const [i, line] of text.split('\n').entries()) {
    if (/(?:[:='"\s])#[\da-f]{3,8}\b/i.test(line)) violations.push(`${file}:${i+1}: hardcoded color`)
    if (/font-weight:\s*(550|650)/.test(line)) violations.push(`${file}:${i+1}: unsupported weight`)
  }
}
assert.deepEqual(violations, [], violations.join('\n'))
console.log('PASS all interface colors use design tokens')
