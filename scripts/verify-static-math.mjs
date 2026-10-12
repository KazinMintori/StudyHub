import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import {compile} from '@vue/compiler-dom'
import {decodeHTML} from 'entities'
import assert from 'node:assert/strict'
import {staticMathPlugin} from './static-math-plugin.mjs'
const ordinary=new MarkdownIt().use(mathjax)
const compact=new MarkdownIt().use(mathjax).use(staticMathPlugin)
const formulas=[String.raw`$\vec F=q\vec E$`,String.raw`$$
\begin{aligned}
V&=kq/r,\\
E_r&=-\partial V/\partial r.
\end{aligned}
$$`,String.raw`$$
E_x=\frac{\sigma}{2\varepsilon_0}
\left(1-\frac{x}{\sqrt{x^2+R^2}}\right)
$$`]
for(const source of formulas){
 const original=ordinary.render(source),wrapped=compact.render(source)
 const matches=[...wrapped.matchAll(/v-html="([^"]+)"/g)]
 assert.equal(matches.length,1)
 const html=JSON.parse(decodeHTML(matches[0][1]))
 // Inline formulas are surrounded by the paragraph renderer in both versions.
 const originalFormula=original.startsWith('<p>')?original.slice(3,-5):original
 assert.equal(html,originalFormula)
 const errors=[],output=compile(wrapped,{mode:'module',onError:error=>errors.push(error.message)})
 assert.deepEqual(errors,[])
 assert(output.code.includes('innerHTML'))
 assert(!output.code.includes('_createElementVNode("path"'))
}
console.log('Passed exact SVG/MathML preservation and Vue compilation checks for inline and display formulas.')
const numbered=String.raw`$$
W_{a\to b}=U_a-U_b
\tag{23.2}
$$`
const result=compact.render(numbered,{relativePath:'vat-ly-2/bai-giang/02-dien-the/the-nang-dien.md'})
assert(result.includes('class="equation-number"'))
assert(result.includes('>(23.2)</span>'))
const body=JSON.parse(decodeHTML(result.match(/v-html="([^"]+)"/)[1]))
assert.equal(body,ordinary.render(numbered.replace(/\\tag\{23\.2\}/,'')))
const errors=[]
compile(result,{mode:'module',onError:error=>errors.push(error.message)})
assert.deepEqual(errors,[])
assert(!compact.render(numbered,{relativePath:'toan-cho-ai/bai-giang/bai-01.md'}).includes('class="equation-number"'))
console.log('Passed responsive numbering and unchanged non-physics rendering checks.')
