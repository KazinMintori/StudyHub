import { assertMathIntegrity, physicsEquationTag } from './math-integrity.mjs'

// Keep MathJax's exact SVG/MathML output in a single Vue HTML binding. Parsing
// every SVG path as a Vue node makes textbook-sized pages consume gigabytes.
export function staticMathPlugin(md, { vueBinding = true } = {}) {
 const cache=new Map()
 for(const [rule,tag] of [['math_inline','span'],['math_block','div']]){
  const render=md.renderer.rules[rule]
  if(!render)throw new Error(`Math renderer missing: ${rule}`)
  md.renderer.rules[rule]=(...args)=>{
   const [tokens,index,,env]=args,token=tokens[index]
   const validatedRender=()=>{
    const html=render(...args)
    assertMathIntegrity(token,html,env)
    return html
   }
   if(!vueBinding)return validatedRender()
   const cachedRender=()=>{
    // Explicit labels and references may depend on other equations.
    if(/\\(?:label|ref|eqref)\b/.test(token.content))return validatedRender()
    const key=rule+'\0'+token.content
    if(!cache.has(key))cache.set(key,validatedRender())
    return cache.get(key)
   }
   const numbered=rule==='math_block' ? physicsEquationTag(token.content,env?.relativePath) : null
   if(numbered){
    const content=token.content
    let html
    try{token.content=content.replace(numbered[0],'');html=cachedRender()}
    finally{token.content=content}
    const expression=md.utils.escapeHtml(JSON.stringify(html))
    return `<div class="static-math static-math-numbered"><div class="static-math-body" v-html="${expression}"></div><span class="equation-number" aria-label="Công thức ${numbered[1]}">(${numbered[1]})</span></div>`
   }
   const html=cachedRender()
   const expression=md.utils.escapeHtml(JSON.stringify(html))
   return `<${tag} class="static-math" v-html="${expression}"></${tag}>`
  }
 }
}
