import { readFile, readdir } from 'node:fs/promises'
import { createMathValidator } from '../verification/math-validator.mjs'
import { mathSegments } from '../../docs/.vitepress/math-text.mjs'
const validate = createMathValidator()
const directory = 'docs/bieu-dien-tri-thuc/bai-giang/01-gioi-thieu-tac-tu'
const files = [directory + '.md', ...(await readdir(directory)).filter(name => name.endsWith('.md')).map(name => directory + '/' + name)]
let count = 0
for (const file of files) for (const segment of mathSegments(await readFile(file, 'utf8'))) {
  if (!segment.startsWith('$')) continue
  const display = segment.startsWith('$$'), delimiter = display ? 2 : 1
  validate(segment.slice(delimiter, -delimiter), display, file)
  count++
}
console.log('PASS ' + count + ' math expressions in ' + files.length + ' final Notes pages.')
