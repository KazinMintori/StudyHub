import {readFile,stat} from 'node:fs/promises'
import {createServer} from 'node:http'
import {resolve,extname,sep} from 'node:path'
export async function startPhysicsPreview(){
 const root=resolve('docs/.vitepress/dist')
 const types={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.webp':'image/webp','.woff2':'font/woff2','.woff':'font/woff','.ico':'image/x-icon'}
 const server=createServer(async(req,res)=>{
  try{
   const path=decodeURIComponent(new URL(req.url,'http://127.0.0.1').pathname)
   let file=resolve(root,'.'+path)
   if(file!==root&&!file.startsWith(root+sep)){res.writeHead(403);res.end();return}
   if((await stat(file)).isDirectory())file=resolve(file,'index.html')
   const body=req.method==='HEAD'?undefined:await readFile(file)
   res.writeHead(200,{'Content-Type':types[extname(file)]||'application/octet-stream'})
   res.end(body)
  }catch{res.writeHead(404);res.end()}
 })
 await new Promise(done=>server.listen(0,'127.0.0.1',done))
 return {url:`http://127.0.0.1:${server.address().port}`,close:()=>new Promise(done=>server.close(done))}
}
