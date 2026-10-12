import {spawn} from 'node:child_process'
// Review builds keep the same pages, hydration and asset graph. Avoid spending
// memory minifying the very large scientific pages during local verification.
const child=spawn(process.execPath,['--max-old-space-size=8192','./node_modules/vitepress/bin/vitepress.js','build','docs'],{
 stdio:'inherit',env:{...process.env,STUDYHUB_REVIEW_BUILD:'1'}
})
child.on('error',error=>{console.error(error);process.exitCode=1})
child.on('exit',(code,signal)=>{process.exitCode=code??(signal?1:0)})
