import assert from 'node:assert/strict'
import { readFile, readdir } from 'node:fs/promises'
import { mathjax } from 'mathjax-full/js/mathjax.js'
import { TeX } from 'mathjax-full/js/input/tex.js'
import { SVG } from 'mathjax-full/js/output/svg.js'
import { liteAdaptor } from 'mathjax-full/js/adaptors/liteAdaptor.js'
import { RegisterHTMLHandler } from 'mathjax-full/js/handlers/html.js'
import { AllPackages } from 'mathjax-full/js/input/tex/AllPackages.js'
import { AssistiveMmlHandler } from 'mathjax-full/js/a11y/assistive-mml.js'
import { concepts } from '../../docs/.vitepress/concepts.mjs'
import { courseCatalog } from '../../docs/.vitepress/course-catalog.mjs'
import { wikiDetails } from '../../docs/.vitepress/wiki-content.mjs'
import { mathLabels } from '../../docs/.vitepress/math-labels.mjs'
import { mathSegments, renderMathText } from '../../docs/.vitepress/math-text.mjs'
import { mathTextPlugin } from '../math-text-plugin.mjs'

assert.equal(renderMathText('<img src=x onerror=alert(1)>', {}), '&lt;img src=x onerror=alert(1)&gt;')
assert.equal(renderMathText('Với $x^2$ và $y$.', { '$x^2$': '<math>x²</math>', '$y$': '<math>y</math>' }), 'Với <math>x²</math> và <math>y</math>.')
assert.equal(renderMathText('$unknown$', {}), '$unknown$')
assert.deepEqual(mathSegments('A $$\nA^T A\n$$ B'), ['A ', '$$\nA^T A\n$$', ' B'])

const adaptor = liteAdaptor()
AssistiveMmlHandler(RegisterHTMLHandler(adaptor))
const document = mathjax.document('', { InputJax: new TeX({ packages: AllPackages }), OutputJax: new SVG({ fontCache: 'none' }) })
const checked = new Set()
function check(source, location) {
  for (const segment of mathSegments(source)) {
    if (!segment.startsWith('$') || checked.has(segment)) continue
    const display = segment.startsWith('$$'), delimiter = display ? 2 : 1
    assert(!/\^\\frac/.test(segment), `${location}: a quotient was attached to an exponent; use an explicit numerator and denominator`)
    const html = adaptor.outerHTML(document.convert(segment.slice(delimiter, -delimiter), { display }))
    assert(!/data-mjx-error|data-mml-node="merror"/.test(html), `${location}: ${segment}`)
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
async function walk(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    if (entry.name.startsWith('.')) continue
    const file = `${dir}/${entry.name}`
    if (entry.isDirectory()) await walk(file)
    else if (entry.name.endsWith('.md')) {
      const text = (await readFile(file, 'utf8')).replace(/^```[^\n]*\n[\s\S]*?^```/gm, '').replace(/`[^`\n]*`/g, '')
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
console.log(`PASS: ${checked.size} unique formulas across all Markdown, catalogs, concepts and interactive labels; safe text rendering and build compilation.`)
