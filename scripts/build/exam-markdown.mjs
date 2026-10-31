import {createMarkdownRenderer} from 'vitepress'
import path from 'node:path'
import {configureStudyMarkdown} from './markdown-presentation.mjs'
import {examProsePlugin} from './exam-prose.mjs'
import {vietnameseMathOptions} from '../math-fonts/vietnamese.mjs'
const proseRenderers = new WeakSet()

export async function createExamMarkdownRenderer(root, { preserveProse = false } = {}) {
  const md=await createMarkdownRenderer(path.join(root,'docs'),{
    html:true,math:vietnameseMathOptions,lineNumbers:false,
    config:renderer=>configureStudyMarkdown(renderer,{base:'/'})
  })
  // VitePress shares one MarkdownIt instance. Set the prose policy per render,
  // so original exam wording stays literal while existing feedback keeps its style.
  if(!proseRenderers.has(md)){md.use(examProsePlugin);proseRenderers.add(md)}
  md.renderer.rules.html_inline=(tokens,index)=>md.utils.escapeHtml(tokens[index].content)
  md.renderer.rules.html_block=(tokens,index)=>md.utils.escapeHtml(tokens[index].content)
  return function render(text='',literalDollars=false) {
    text=text.replace(/^```python-error[ \t]*$/gm,'```python')
      .replace(/\[([^\]]+)\]\(<?[A-Z]:[/\\][^\n]*?>?\)/g,'$1')
    if(literalDollars) {
      text=text.replace(/(^```[^\n]*\n[\s\S]*?^```[ \t]*$)|(`+)([\s\S]*?)\2|\\\$|[$<>]/gm,
        match=>({'$':'\\$','<':'&lt;','>':'&gt;'})[match]||match)
    }
    let html
    try {
      md.core.ruler[preserveProse?'disable':'enable']('exam_prose_colons')
      html=md.render(text,{relativePath:'xu-ly-du-lieu/on-thi/index.md'})
    }
    catch(error){throw new Error(`Exam Markdown failed near: ${text.slice(0,300)}`,{cause:error})}
    if(/data-mjx-error|<merror\b/.test(html))throw new Error(`Invalid exam math near: ${text.slice(0,300)}`)
    const entities={quot:'"',amp:'&',lt:'<',gt:'>'}
    return html.replace(/<a\b[^>]*class="header-anchor"[^>]*>[\s\S]*?<\/a>/g,'')
      .replace(/<(span|div) class="static-math" v-html="([^"]*)"><\/\1>/g,(_,tag,expression)=>{
        const json=expression.replace(/&(quot|amp|lt|gt);/g,(_,name)=>entities[name])
        return `<${tag} class="static-math">${JSON.parse(json)}</${tag}>`
      }).replace(/<script\b[\s\S]*?<\/script>/gi,'')
  }
}
