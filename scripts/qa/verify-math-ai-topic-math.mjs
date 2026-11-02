// Source-only preflight for edited topics. SVG ex widths guide line breaks;
// this never substitutes for browser layout/scrollbar verification.
import {readFile,readdir,mkdir,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import path from 'node:path'
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import {mathSegments} from '../../docs/.vitepress/math-text.mjs'
import {createMathValidator} from '../verification/math-validator.mjs'
import {createMarkdownRenderer} from 'vitepress'
import config from '../../docs/.vitepress/config.mjs'
import {mathTokens,swallowedMarkdown} from '../math-integrity.mjs'
const root=process.cwd(),base='docs/toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange'
const files=process.argv.slice(2).length?process.argv.slice(2):(await readdir(base)).filter(name=>name.endsWith('.md')).map(name=>`${base}/${name}`)
const md=new MarkdownIt().use(mathjax),validate=createMathValidator(),issues=[],sources={}
const pageRenderer=await createMarkdownRenderer(path.resolve('docs'),config.markdown)
let formulas=0
for(const name of files){
 const resolved=path.resolve(name)
 if(!resolved.startsWith(path.join(root,'docs')+path.sep))throw Error('Only workspace documentation can be inspected')
 const data=await readFile(resolved),source=data.toString('utf8')
 sources[name]=createHash('sha256').update(data).digest('hex')
 for(const token of mathTokens(pageRenderer.parse(source,{path:resolved,relativePath:name.slice(5)}))){
  if(swallowedMarkdown(token))issues.push({file:name,type:'markdown-swallowed-by-math',line:(token.map?.[0]||0)+1})
 }
 for(const segment of mathSegments(source)){
  if(!segment.startsWith('$'))continue
  const display=segment.startsWith('$$'),delimiter=display?2:1,tex=segment.slice(delimiter,-delimiter)
  try{validate(tex,display,name)}catch(error){issues.push({file:name,type:'invalid-tex',message:error.message})}
  const width=Number(/width="([\d.]+)ex"/.exec(md.render(segment))?.[1]||0)
  if(width>(display?36:38))issues.push({file:name,type:'width-preflight',width,display,tex})
  // A minus at the start of a cases branch or an independent inequality is
  // not a continued right-hand side. Flag only an aligned continuation that
  // starts at an arithmetic operator and has no relation of its own.
  if(display)for(const block of tex.matchAll(/\\begin\{aligned\}([\s\S]*?)\\end\{aligned\}/g)){
   for(const continuation of block[1].matchAll(/\\\\\s*\n\s*&\s*[+\-]([^\n]*)/g)){
    if(!/(?:=|<|>|\\(?:le|ge|leq|geq|approx|iff|implies)\b)/.test(continuation[1]))issues.push({file:name,type:'break-at-arithmetic-operator',tex})
   }
  }
  formulas++
 }
}
const report={verifiedAt:new Date().toISOString(),scope:'Source formula validity and width preflight only; browser QA pending',formulas,sources,issues}
await mkdir('qa/math-ai-visuals',{recursive:true})
const label=process.argv.length===2?'lecture03':files.length===1?path.basename(files[0],'.md'):'selected'
const timestamp=report.verifiedAt.replace(/[^0-9]/g,'')
const reportText=JSON.stringify(report,null,2)
await writeFile(`qa/math-ai-visuals/topic-math-preflight-${label}-${timestamp}.json`,reportText)
await writeFile(`qa/math-ai-visuals/topic-math-preflight-${label}.json`,reportText)
console.log(JSON.stringify({files:files.length,formulas,issues},null,2))
if(issues.length)process.exitCode=1
