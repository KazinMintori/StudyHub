import {readFile,readdir,writeFile,mkdir} from 'node:fs/promises'
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
const md=new MarkdownIt().use(mathjax)
const dir='raw_materials/physics/translations/chapter-21'
const findings=[]
let display=0,inline=0
for(const name of await readdir(dir)) {
 if(!name.endsWith('.md'))continue
 const source=await readFile(dir+'/'+name,'utf8')
 for(const m of source.matchAll(/\$\$([\s\S]*?)\$\$/g)) {
  display++
  const html=md.render('$$\n'+m[1].trim()+'\n$$')
  const width=Number(html.match(/(?:min-width:\s*|width=")([\d.]+)ex/)?.[1]||0)
  if(/data-mjx-error|<merror/.test(html)||width>32) findings.push({file:name,line:source.slice(0,m.index).split('\n').length,widthEx:width,kind:'display',invalid:/data-mjx-error|<merror/.test(html),tex:m[1].trim()})
 }
 const stripped=source.replace(/\$\$[\s\S]*?\$\$/g,'')
 for(const m of stripped.matchAll(/(?<!\$)\$([^\n$]+)\$(?!\$)/g)) {
  inline++
  const html=md.renderInline('$'+m[1]+'$')
  const width=Number(html.match(/width="([\d.]+)ex/)?.[1]||0)
  if(/data-mjx-error|<merror/.test(html)||width>38)findings.push({file:name,line:stripped.slice(0,m.index).split('\n').length,widthEx:width,kind:'inline',tex:m[1]})
 }
}
await mkdir('qa/physics/chapter21',{recursive:true})
await writeFile('qa/physics/chapter21/math-audit.json',JSON.stringify({display,inline,findings},null,2)+'\n')
console.log(JSON.stringify({display,inline,wideOrInvalid:findings.length},null,2))
for(const f of findings)console.log(`${f.file}:${f.line} ${f.kind} ${f.widthEx}ex ${f.tex.replace(/\s+/g,' ').slice(0,120)}`)
