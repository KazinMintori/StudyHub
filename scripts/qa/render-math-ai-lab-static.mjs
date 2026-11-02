// Static source geometry review, with no browser or local server. This does not
// verify browser CSS, layout, scrolling or input. Keep those QA gates separate.
import {readFile,writeFile,mkdir} from 'node:fs/promises'
import path from 'node:path'
import {pathToFileURL} from 'node:url'
import {createHash} from 'node:crypto'
import {build} from 'esbuild'
import {parse,compileScript,rewriteDefault,compileStyle} from '@vue/compiler-sfc'
const names=process.argv.slice(2)
if(!names.length||names.some(name=>!/^\w+Lab$/.test(name)))throw Error('Pass explicit component names ending in Lab')
const props=JSON.parse(process.env.QA_STATIC_PROPS||'{}'),variant=process.env.QA_STATIC_VARIANT||''
if(variant&&!/^[a-z0-9-]+$/.test(variant))throw Error('Use a simple lowercase static preview variant')
const root=process.cwd(),output=path.resolve('qa/math-ai-visuals/static-previews')
await mkdir(output,{recursive:true})
for(const name of names){
 const label=name+(variant?'--'+variant:'')
 const styles=[],sources={}
 const result=await build({
  stdin:{contents:`import {createSSRApp} from 'vue';import {renderToString} from '@vue/server-renderer';import Lab from './src/features/labs/components/${name}.vue';export const render=()=>renderToString(createSSRApp(Lab,${JSON.stringify(props)}));`,resolveDir:root},
  bundle:true,write:false,metafile:true,platform:'node',format:'esm',packages:'external',logLevel:'silent',
  plugins:[{name:'static-vue',setup(plugin){
   plugin.onLoad({filter:/\.vue$/},async({path:filename})=>{
    const source=await readFile(filename,'utf8'),relative=path.relative(root,filename).replaceAll('\\','/')
    sources[relative]=createHash('sha256').update(source).digest('hex')
    const id=createHash('sha256').update(relative).digest('hex').slice(0,8)
    const {descriptor,errors}=parse(source,{filename})
    if(errors.length)throw errors[0]
    const compiled=compileScript(descriptor,{id,inlineTemplate:true})
    for(const style of descriptor.styles){
     const css=compileStyle({source:style.content,filename,id:`data-v-${id}`,scoped:style.scoped})
     if(css.errors.length)throw css.errors[0]
     styles.push(css.code)
    }
    const script=rewriteDefault(compiled.content,'__sfc__')
    return {loader:'js',contents:`${script}\n__sfc__.__scopeId='data-v-${id}';export default __sfc__;`,resolveDir:path.dirname(filename)}
   })
  }}]
 })
 for(const input of Object.keys(result.metafile.inputs)){
  if(input.startsWith('<'))continue
  const data=await readFile(input)
  sources[input.replaceAll('\\','/')]=createHash('sha256').update(data).digest('hex')
 }
 const filename=path.join(output,`${label}.mjs`)
 await writeFile(filename,result.outputFiles[0].text)
 const module=await import(pathToFileURL(filename).href)
 const html=await module.render()
 const css=await readFile('src/app/styles/labs.css','utf8')+'\n'+styles.join('\n')
 const tokens=await readFile('docs/.vitepress/theme/tokens.css','utf8')
 for(const input of ['docs/.vitepress/theme/tokens.css','src/app/styles/labs.css'])sources[input]=createHash('sha256').update(await readFile(input)).digest('hex')
 await writeFile(path.join(output,`${label}.json`),JSON.stringify({name,props,variant,renderedAt:new Date().toISOString(),scope:'Static SVG geometry with simplified graphic CSS and generic sans-serif font; exact browser CSS, font metrics and input verification pending',html,css,tokens,sources},null,2))
 console.log(`Static SVG source rendered: ${label}`)
}
