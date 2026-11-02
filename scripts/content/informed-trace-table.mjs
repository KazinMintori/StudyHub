import {readFile,writeFile} from 'node:fs/promises'
import {informedExamples,traceInformed} from '../../src/features/labs/services/informed-search.mjs'
const root=process.argv[2]||'.'
const file=root+'/docs/bieu-dien-tri-thuc/bai-giang/03-tim-kiem-kinh-nghiem/thuat-toan-a-sao.md'
const frames=traceInformed(informedExamples[0]),rows=[]
for(let i=0;i<frames.length;i++)if(frames[i].phase==='take'){
 const f=frames[i],n=f.nodes[f.current],next=frames[i+1]
 rows.push(`| ${rows.length+1} | ${n.state} (${n.g}, ${n.h}, ${n.f}) | ${next.phase==='stale'?'Bỏ bản ghi cũ':next.phase==='success'?'Kiểm tra đích, dừng':'Mở rộng'} |`)
}
const table='| Lần lấy | Nút (g, h, f) | Xử lý |\n|---|---|---|\n'+rows.join('\n')
let body=await readFile(file,'utf8')
body=body.replace('<!-- VERIFIED_TRACE_TABLE -->',table)
await writeFile(file,body)
console.log('Inserted exact trace including stable-tie stale removal.')
