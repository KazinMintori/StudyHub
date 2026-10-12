import {readFile,readdir,writeFile,mkdir} from 'node:fs/promises'
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
const md=new MarkdownIt().use(mathjax),findings=[]
let display=0,inline=0
function inspect(source,file){
 for(const m of source.matchAll(/\$\$([\s\S]*?)\$\$/g)){
  display++;const html=md.render('$$\n'+m[1].trim().replace(/\\tag\{[\d.]+\}/g,'')+'\n$$')
  const width=Number(html.match(/(?:min-width:\s*|width=")([\d.]+)ex/)?.[1]||0)
  const invalid=/data-mjx-error|<merror/.test(html)
  if(invalid||width>32)findings.push({file,line:source.slice(0,m.index).split('\n').length,kind:'display',widthEx:width,invalid,tex:m[1].trim()})
 }
 const stripped=source.replace(/\$\$[\s\S]*?\$\$/g,'')
 for(const m of stripped.matchAll(/(?<!\$)\$([^\n$]+)\$(?!\$)/g)){
  inline++;const html=md.renderInline('$'+m[1]+'$'),width=Number(html.match(/width="([\d.]+)ex/)?.[1]||0)
  const invalid=/data-mjx-error|<merror/.test(html)
  if(invalid||width>38)findings.push({file,line:stripped.slice(0,m.index).split('\n').length,kind:'inline',widthEx:width,invalid,tex:m[1]})
 }
}
const chapters=process.argv.slice(2).length?process.argv.slice(2):['21','22']
for(const chapter of chapters){
 const dir=`raw_materials/physics/translations/chapter-${chapter}`
 for(const name of await readdir(dir))if(name.endsWith('.md'))inspect(await readFile(dir+'/'+name,'utf8'),dir+'/'+name)
}
function walk(value,name){
 if(typeof value==='string')inspect(value,name)
 else if(Array.isArray(value))value.forEach((v,i)=>walk(v,`${name}[${i}]`))
 else if(value&&typeof value==='object')for(const [k,v]of Object.entries(value))walk(v,`${name}.${k}`)
}
for(const name of ['physics-electrostatics-course','physics-electrostatics-foundations','physics-gauss-course','physics-gauss-foundations','physics-potential-course','physics-potential-foundations'])walk(await import(`../docs/.vitepress/${name}.mjs`),name)
await mkdir('qa/physics',{recursive:true})
await writeFile('qa/physics/math-audit.json',JSON.stringify({display,inline,findings},null,2)+'\n')
console.log(JSON.stringify({display,inline,invalid:findings.filter(f=>f.invalid).length,wide:findings.filter(f=>f.widthEx>(f.kind==='inline'?38:34)).length},null,2))
for(const f of findings)if(f.widthEx>(f.kind==='inline'?38:34)||f.invalid)console.log(`${f.file}:${f.line} ${f.kind} ${f.widthEx} ${f.tex.replace(/\s+/g,' ').slice(0,165)}`)
