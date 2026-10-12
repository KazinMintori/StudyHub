// Keep MathJax's exact SVG/MathML output in a single Vue HTML binding. Parsing
// every SVG path as a Vue node makes textbook-sized pages consume gigabytes.
export function staticMathPlugin(md) {
 for(const [rule,tag] of [['math_inline','span'],['math_block','div']]){
  const render=md.renderer.rules[rule]
  if(!render)throw new Error(`Math renderer missing: ${rule}`)
  md.renderer.rules[rule]=(...args)=>{
   const [tokens,index,,env]=args,token=tokens[index]
   const numbered=rule==='math_block'&&/^vat-ly-[12]\//.test((env?.relativePath||'').replaceAll('\\','/'))
     ? token.content.match(/\\tag\{([\d.]+)\}/) : null
   if(numbered){
    const content=token.content
    let html
    try{token.content=content.replace(numbered[0],'');html=render(...args)}
    finally{token.content=content}
    const expression=md.utils.escapeHtml(JSON.stringify(html))
    return `<div class="static-math static-math-numbered"><div class="static-math-body" v-html="${expression}"></div><span class="equation-number" aria-label="Công thức ${numbered[1]}">(${numbered[1]})</span></div>`
   }
   const html=render(...args)
   const expression=md.utils.escapeHtml(JSON.stringify(html))
   return `<${tag} class="static-math" v-html="${expression}"></${tag}>`
  }
 }
}
