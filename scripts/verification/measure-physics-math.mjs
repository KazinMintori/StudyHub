// Read-only helper for scoped workers: No files are written.
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import {readFile} from 'node:fs/promises'
import path from 'node:path'
const [directory,...files]=process.argv.slice(2)
if(!directory||!files.length)throw Error('Pass worktree and owned Markdown paths.')
const md=new MarkdownIt().use(mathjax),findings=[]
const displayLimit=Number(process.env.PHYSICS_DISPLAY_EX||28)
if(!Number.isFinite(displayLimit)||displayLimit<1||displayLimit>30)throw Error('Invalid display review limit')
let display=0,inline=0
for(const file of files){
 const source=await readFile(path.join(directory,file),'utf8')
 const lineAt=i=>source.slice(0,i).split('\n').length
 for(const [i,line] of source.split(/\r?\n/).entries()){
  if(/^\s*\$\s*$/.test(line))findings.push({file,line:i+1,kind:'isolated-single-dollar-line'})
  if(line.includes('$$')&&line!=='$$')findings.push({file,line:i+1,kind:'display-delimiter-not-own-column0-line'})
  if(/file:\/\/\/|[A-Z]:[\\/](Users|My Drive)/.test(line))findings.push({file,line:i+1,kind:'machine-local-link'})
 }
 for(const match of source.matchAll(/\$\$([\s\S]*?)\$\$/g)){
  display++;const tex=match[1].replace(/\\tag\{[^}]+\}/g,'')
  try{
   const html=md.render('$$\n'+tex.trim()+'\n$$'),width=Number(html.match(/(?:min-width:\s*|width=")([\d.]+)ex/)?.[1]||0)
   if(width>displayLimit||/<merror|data-mjx-error/.test(html))findings.push({file,line:lineAt(match.index),kind:'wide-or-invalid-display',width,tex})
  }catch(error){findings.push({file,line:lineAt(match.index),kind:'display-render-error',tex,error:String(error)})}
 }
 const rest=source.replace(/\$\$[\s\S]*?\$\$/g,m=>m.replace(/[^\n]/g,' '))
 for(const match of rest.matchAll(/(?<!\$)\$([^\n$]+)\$(?!\$)/g)){
  inline++;const tex=match[1]
  try{
   const html=md.renderInline('$'+tex+'$'),width=Number(html.match(/width="([\d.]+)ex/)?.[1]||0)
   if(width>27||/<merror|data-mjx-error/.test(html))findings.push({file,line:lineAt(match.index),kind:'wide-or-invalid-inline',width,tex})
  }catch(error){findings.push({file,line:lineAt(match.index),kind:'inline-render-error',tex,error:String(error)})}
 }
}
console.log(JSON.stringify({status:findings.length?'failed':'passed',scope:'Draft math and syntax probe; final viewport checks determine actual fit.',displayLimitEx:displayLimit,inlineLimitEx:27,display,inline,findings},null,2))
if(findings.length)process.exitCode=1
