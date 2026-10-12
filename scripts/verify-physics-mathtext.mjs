import {readFile,writeFile} from 'node:fs/promises'
import assert from 'node:assert/strict'
import {mathTextPlugin} from './math-text-plugin.mjs'
import {mathSegments,renderMathText} from '../docs/.vitepress/math-text.mjs'
const plugin=mathTextPlugin(),rendered={},missing=[]
const modules=['physics-motion-course','physics-electrostatics-course','physics-electrostatics-foundations','physics-gauss-course','physics-gauss-foundations','physics-potential-course','physics-potential-foundations','physics-capacitance-course','physics-capacitance-foundations','physics-current-course','physics-current-foundations']
for(const name of modules){
 const path=`docs/.vitepress/${name}.mjs`,source=await readFile(path,'utf8')
 const transformed=plugin.transform(source,path.replaceAll('\\','/'))
 const prefix='Object.assign(studyRenderedMath, '
 const data=transformed.code.slice(transformed.code.lastIndexOf(prefix)+prefix.length,-2)
 Object.assign(rendered,JSON.parse(data))
}
let references=0
function inspect(value,path){
 if(typeof value==='string'){
  for(const segment of mathSegments(value))if(segment.startsWith('$')){
   references++
   if(!rendered[segment])missing.push({path,segment})
   else assert(renderMathText(segment,rendered).includes('<mjx-container'),path)
  }
 }
 else if(Array.isArray(value))value.forEach((v,i)=>inspect(v,`${path}[${i}]`))
 else if(value&&typeof value==='object')for(const [key,v] of Object.entries(value))inspect(v,`${path}.${key}`)
}
for(const name of modules)inspect(await import(`../docs/.vitepress/${name}.mjs`),name)
assert(references>50,'Must inspect mathematical fields, not just module structure')
assert.deepEqual(missing,[])
await writeFile('qa/physics/mathtext-render-checks.json',JSON.stringify({status:'passed',references,compiledExpressions:Object.keys(rendered).length,missing},null,2)+'\n')
console.log('All',references,'formula references have SVG renderings;',Object.keys(rendered).length,'compiled expressions.')
