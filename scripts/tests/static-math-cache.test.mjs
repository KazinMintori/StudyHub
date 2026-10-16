import test from 'node:test'
import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import {staticMathPlugin} from '../static-math-plugin.mjs'
function fixture(){
 const calls=[],md=new MarkdownIt()
 for(const rule of ['math_inline','math_block']){
  md.renderer.rules[rule]=(tokens,index)=>{
   calls.push({rule,content:tokens[index].content})
   if(tokens[index].content==='error')throw new Error('render failure')
   return '<svg data-formula="'+tokens[index].content+'"></svg>'
  }
 }
 md.use(staticMathPlugin)
 const render=(rule,content,env={})=>md.renderer.rules[rule]([{content}],0,{},env)
 return {md,calls,render}
}
test('identical expressions reuse rendering and keep the same binding',()=>{
 const {calls,render}=fixture()
 assert.equal(render('math_inline','x+1'),render('math_inline','x+1'))
 assert.equal(calls.length,1)
})
test('inline and display modes have separate cached results',()=>{
 const {calls,render}=fixture()
 render('math_inline','x+1');render('math_block','x+1')
 assert.equal(calls.length,2)
})
test('numbered Physics equations share expressions and retain each tag',()=>{
 const {calls,render}=fixture(),env={relativePath:'vat-ly-2/bai-giang/test.md'}
 const a=render('math_block','x=1\\tag{31.1}',env)
 const b=render('math_block','x=1\\tag{31.2}',env)
 assert.equal(calls.length,1)
 assert(a.includes('(31.1)')&&b.includes('(31.2)'))
 assert(!a.includes('\\tag'))
})
test('lettered Physics equation tags use the same separate label layout',()=>{
 const {calls,render}=fixture(),env={relativePath:'vat-ly-2/bai-giang/test.md'}
 const a=render('math_block','x=1\\tag{40.3a}',env)
 const b=render('math_block','x=1\\tag{40.3b}',env)
 assert.equal(calls.length,1)
 assert(a.includes('static-math-numbered')&&b.includes('static-math-numbered'))
 assert(a.includes('(40.3a)')&&b.includes('(40.3b)'))
 assert(!a.includes('\\tag')&&!b.includes('\\tag'))
})
test('labelled expressions bypass the cache because references can change',()=>{
 const {calls,render}=fixture()
 for(let n=0;n<2;n++)render('math_block','x=1\\label{equation}')
 assert.equal(calls.length,2)
})
test('render failure restores a numbered token and does not cache the error',()=>{
 const {md,calls}=fixture(),token={content:'error\\tag{31.1}'}
 for(let n=0;n<2;n++)assert.throws(()=>md.renderer.rules.math_block([token],0,{}, {relativePath:'vat-ly-2/a.md'}))
 assert.equal(token.content,'error\\tag{31.1}')
 assert.equal(calls.length,2)
})
test('real MathJax markup is preserved inside the escaped Vue binding',()=>{
 const plain=new MarkdownIt().use(mathjax),actual=plain.renderInline('$x^2+1$')
 const cached=new MarkdownIt().use(mathjax).use(staticMathPlugin)
 const rendered=cached.renderInline('$x^2+1$')
 const expression=rendered.match(/v-html="([^"]+)"/)[1]
 const decoded=expression.replaceAll('&quot;','"').replaceAll('&lt;','<').replaceAll('&gt;','>').replaceAll('&amp;','&')
 assert.equal(JSON.parse(decoded),actual)
 assert.equal(cached.renderInline('$x^2+1$'),rendered)
})
