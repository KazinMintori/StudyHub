import assert from 'node:assert/strict'
import { readdir, readFile } from 'node:fs/promises'
import { concepts } from '../../docs/.vitepress/concepts.mjs'
import { courseCatalog } from '../../docs/.vitepress/course-catalog.mjs'
import { wikiDetails } from '../../docs/.vitepress/wiki-content.mjs'
import { mathLabels } from '../../docs/.vitepress/math-labels.mjs'
import { cheatsheets } from '../../docs/.vitepress/cheatsheets.mjs'
import { mathSegments, renderMathText } from '../../docs/.vitepress/math-text.mjs'
import { mathTextPlugin } from '../math-text-plugin.mjs'
import { readMarkdownIncludes } from '../read-markdown-includes.mjs'
import { createMathValidator } from '../verification/math-validator.mjs'

assert.equal(renderMathText('<img src=x onerror=alert(1)>', {}), '&lt;img src=x onerror=alert(1)&gt;')
assert.equal(renderMathText('Với $x^2$ và $y$.', { '$x^2$': '<math>x²</math>', '$y$': '<math>y</math>' }), 'Với <math>x²</math> và <math>y</math>.')
assert.equal(renderMathText('$unknown$', {}), '$unknown$')
assert.deepEqual(mathSegments('A $$\nA^T A\n$$ B'), ['A ', '$$\nA^T A\n$$', ' B'])

const validateMath = createMathValidator()
const checked = new Set()
function check(source, location) {
  for (const segment of mathSegments(source)) {
    if (!segment.startsWith('$') || checked.has(segment)) continue
    const display = segment.startsWith('$$'), delimiter = display ? 2 : 1
    assert(!/\^\\frac/.test(segment), `${location}: a quotient was attached to an exponent; use an explicit numerator and denominator`)
    validateMath(segment.slice(delimiter, -delimiter), display, location.startsWith('docs/') ? location.slice(5) : '')
    checked.add(segment)
  }
}
for (const [id, term] of Object.entries(concepts)) for (const field of ['definition', 'example', 'use', 'question', 'answer', 'notation']) {
  if (!term[field]) continue
  const prose = mathSegments(term[field]).filter((_, i) => i % 2 === 0).join('')
  assert(!/[⎡⎣√∂ᵀ̂₀-₉²³∇Σ∑‖]/.test(prose), `${id}.${field}: unformatted math`)
  check(term[field], `${id}.${field}`)
}
for (const course of courseCatalog) for (const slide of course.slides) for (const value of [slide.formula, slide.example, ...slide.bullets]) check(value, `${course.id}/${slide.note}`)
for (const [id, source] of Object.entries(wikiDetails)) check(source, `wikiDetails.${id}`)
for (const source of Object.values(mathLabels)) check(source, 'interactive label')
function checkStrings(value, location) {
  if (typeof value === 'string') check(value, location)
  else if (value && typeof value === 'object') {
    for (const [key, child] of Object.entries(value)) checkStrings(child, `${location}.${key}`)
  }
}
// Formula rows, variable definitions and comparison tables are MathText too.
for (const [key, cs] of Object.entries(cheatsheets)) checkStrings(cs, `cheatsheet.${key}`)
async function walk(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    if (entry.name.startsWith('.')) continue
    const file = `${dir}/${entry.name}`
    if (entry.isDirectory()) await walk(file)
    else if (entry.name.endsWith('.md')) {
      const text = (await readMarkdownIncludes(file)).replace(/^```[^\n]*\n[\s\S]*?^```/gm, '').replace(/`[^`\n]*`/g, '')
      check(text, file)
    }
  }
}
await walk('docs')
const plugin = mathTextPlugin()
const expression = '$\\nabla f=\\frac{1}{2}$'
const transformed = plugin.transform(`export const example=${JSON.stringify(expression)}`, '/course-catalog.mjs').code
assert(transformed.includes(JSON.stringify(expression)), 'TeX backslashes must survive JavaScript string decoding')
assert(transformed.includes('mjx-assistive-mml'), 'Compiled math must retain assistive MathML')
assert(transformed.includes('data-mml-node=\\"mfrac\\"'), 'Fractions must be typeset')
const dedicatedCheatsheet = plugin.transform(`export const example=${JSON.stringify(expression)}`, '/docs/.vitepress/physics1-cheatsheets.mjs')
assert(dedicatedCheatsheet?.code.includes('studyRenderedMath'), 'Dedicated subject cheatsheets must register their rendered formulas')
assert(dedicatedCheatsheet.code.includes('data-mml-node=\\"mfrac\\"'), 'Lazy-loaded cheatsheets must carry typeset formulas')
const dataLab = plugin.transform(`export const lab={tasks:[{explanation:${JSON.stringify(expression)}}]}`, '/docs/.vitepress/labs/xu-ly-du-lieu/lab-08.mjs')
assert(dataLab?.code.includes('data-mml-node=\\"mfrac\\"'), 'Data lab explanations must register their rendered formulas')
for (const file of ['docs/.vitepress/physics1-cheatsheets.mjs', ...['06', '08', '10'].map(id => `docs/.vitepress/labs/xu-ly-du-lieu/lab-${id}.mjs`)]) {
  const compiled = plugin.transform(await readFile(file, 'utf8'), '/' + file)
  assert(compiled?.code.includes('studyRenderedMath'), `${file}: Actual lazy data must register compiled math`)
  assert(compiled.code.includes('data-mml-node='), `${file}: Actual formulas must be typeset, not just preserved as source strings`)
}
console.log(`PASS: ${checked.size} unique formulas across all Markdown, catalogs, concepts and interactive labels; safe text rendering and build compilation.`)
