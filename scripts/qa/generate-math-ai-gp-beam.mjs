import {mkdir,writeFile} from 'node:fs/promises'
import path from 'node:path'
import {project3,dot} from '../../src/features/labs/services/foundation-geometry.mjs'
const output=path.resolve('../math-ai-visual-content/docs/toan-cho-ai/bai-giang/img/lec-02/gp-cantilever-comparison.svg')
const colors={ink:'#1f1c2b',muted:'#6b6580',rule:'#dedae8',paper:'#fafafc',purple:'#5a37a8',purpleSoft:'#eee9fb',green:'#1d6b45',greenSoft:'#e6f4ec',red:'#b42318'}
const camera={yaw:35,pitch:28,scale:85,origin:[140,140]},P=p=>project3(p,camera)
const degrees=Math.PI/180,depth=[Math.sin(35*degrees)*Math.cos(28*degrees),Math.cos(35*degrees)*Math.cos(28*degrees),Math.sin(28*degrees)]
const polygon=(points,fill)=>`<polygon points="${points.map(p=>P(p).map(v=>v.toFixed(2)).join(',')).join(' ')}" fill="${fill}" stroke="${colors.ink}" stroke-width="1.2"/>`
const text=(x,y,value,size=20)=>`<text x="${x}" y="${y}" font-size="${size}" fill="${colors.ink}" font-family="sans-serif">${value}</text>`
function panel(label,width,height,offset){
 const widths=[1,width],heights=[1,height],faces=[]
 for(let i=1;i<=2;i++){
  const x=2-i,w=widths[i-1]/2,h=heights[i-1]/2
  const vertices=Array.from({length:8},(_,j)=>[x+(j&1?1:0),j&2?w:-w,j&4?h:-h])
  for(const indices of [[0,1,3,2],[4,5,7,6],[0,1,5,4],[2,3,7,6],[0,2,6,4],[1,3,7,5]]){
   const points=indices.map(j=>vertices[j]),mean=[0,1,2].map(k=>points.reduce((s,p)=>s+p[k],0)/4)
   faces.push({points,depth:dot(mean,depth),fill:i===2?colors.purpleSoft:colors.greenSoft})
  }
 }
 const clamp=polygon([[0,-width/2-.1,-height/2-.1],[0,width/2+.1,-height/2-.1],[0,width/2+.1,height/2+.1],[0,-width/2-.1,height/2+.1]],'#dedae8')
 const load=P([2,0,0]),end=P([2,0,-.6]),volume=1+width*height
 const deflection=.004+.028/(width*height**3),stress=Math.max(6,12/(width*height**2))
 return `<g transform="translate(0 ${offset})">${text(12,24,label)}${clamp}${faces.sort((a,b)=>a.depth-b.depth).map(f=>polygon(f.points,f.fill)).join('')}${[1,2].map(i=>{const point=P([2-i+.5,widths[i-1]/2,0]);return text(point[0]-5,point[1]+6,i)}).join('')}<circle cx="${load[0]}" cy="${load[1]}" r="3" fill="${colors.red}"/><line x1="${load[0]}" y1="${load[1]}" x2="${end[0]}" y2="${end[1]}" stroke="${colors.red}" stroke-width="2" marker-end="url(#force)"/>${text(end[0]+10,end[1]+6,'F')}${text(12,275,`V = ${volume} · y₁ = ${deflection.toFixed(4)} · σ lớn nhất = ${stress}`,18)}</g>`
}
const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="400" height="910" viewBox="0 0 400 910" role="img" aria-labelledby="title desc"><title id="title">So sánh tăng chiều rộng và chiều cao ở đoạn sát ngàm</title><desc id="desc">Dầm hai đoạn dài một đơn vị, E bằng 1000 và F bằng 1. Dầm đồng đều có thể tích 2, độ võng 0.032. Tăng gấp đôi chiều rộng đoạn 2 cho thể tích 3 và độ võng 0.018. Tăng gấp đôi chiều cao đoạn 2 cũng có thể tích 3 nhưng độ võng 0.0075. Cả hai phương án sau có ứng suất lớn nhất bằng 6.</desc><defs><marker id="force" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="${colors.red}"/></marker></defs><rect width="400" height="910" fill="${colors.paper}"/>${panel('A. Đồng đều: w₂ = 1, h₂ = 1',1,1,0)}<line x1="12" y1="300" x2="388" y2="300" stroke="${colors.rule}"/>${panel('B. Tăng rộng: w₂ = 2, h₂ = 1',2,1,305)}<line x1="12" y1="605" x2="388" y2="605" stroke="${colors.rule}"/>${panel('C. Tăng cao: w₂ = 1, h₂ = 2',1,2,610)}</svg>`
await mkdir(path.dirname(output),{recursive:true});await writeFile(output,svg)
console.log('Generated deterministic GP beam comparison SVG')
