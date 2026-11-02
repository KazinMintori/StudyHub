import {spawn} from 'node:child_process'
let server
const base='http://127.0.0.1:5199'
const run=file=>new Promise((resolve,reject)=>{const child=spawn(process.execPath,[file],{stdio:'inherit',windowsHide:true,env:{...process.env,QA_URL:base}});child.once('error',reject);child.once('exit',code=>code===0?resolve():reject(Error(file+' exited '+code)))})
try{
 let ready=false;try{ready=(await fetch(base,{signal:AbortSignal.timeout(1000)})).ok}catch{}
 if(!ready){server=spawn(process.execPath,['node_modules/vitepress/bin/vitepress.js','dev','docs','--port','5199','--host','127.0.0.1','--strictPort'],{stdio:'ignore',windowsHide:true});for(let i=0;i<80;i++){try{if((await fetch(base,{signal:AbortSignal.timeout(1500)})).ok){ready=true;break}}catch{}await new Promise(r=>setTimeout(r,500))}}
 if(!ready)throw Error('Dev server did not become ready')
 const file=process.argv[2]
 if(!['predicate-notes','predicate-review','predicate-logic'].includes(file))throw Error('Choose predicate-notes, predicate-review or predicate-logic')
 await run('scripts/qa/'+file+'.mjs')
}finally{server?.kill()}
