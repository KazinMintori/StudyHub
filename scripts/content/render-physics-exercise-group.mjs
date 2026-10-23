import {readFile,writeFile} from 'node:fs/promises'
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import {configureStudyMarkdown} from '../build/markdown-presentation.mjs'
const [input,output]=process.argv.slice(2)
if(!input||!output)throw Error('Pass the bounded group input and output paths')
const group=JSON.parse(await readFile(input,'utf8'))
// This is published first-party Markdown, never a response from a remote URL.
if(/<(?:script|iframe)\b|\bon\w+\s*=|javascript:/i.test(group.markdown))throw Error('Executable markup in exercise source')
const md=new MarkdownIt({html:true}).use(mathjax)
configureStudyMarkdown(md,{base:'/',vueBinding:false})
const html=md.render(group.markdown,{relativePath:'vat-ly-1/bai-giang/exercises.md'})
if(/v-html=|data-mjx-error|<merror/.test(html))throw Error('Unrendered/invalid math in '+group.id)
await writeFile(output,JSON.stringify({id:group.id,title:group.title,ids:group.ids,html}))
