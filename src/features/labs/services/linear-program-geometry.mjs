import {dot} from './convex-geometry.mjs'

export const lpShapes={
 bounded:{label:'Ngũ giác bị chặn',vertices:[[.5,.5],[3.5,.5],[4.5,2.2],[2.8,3.8],[.8,3]],rays:[]},
 unbounded:{label:'Đa diện có hai tia',vertices:[[.5,2.5],[1.5,.8],[3.5,.5]],rays:[{from:0,d:[-.3,1]},{from:2,d:[1,.1]}]},
 strip:{label:'Dải không có đỉnh',vertices:[],rays:[]},
 infeasible:{label:'Hai điều kiện mâu thuẫn',vertices:[],rays:[]}
}

function supportingHalfspace(point,direction,inside){
 let a=[direction[1],-direction[0]],b=dot(a,point)
 if(dot(a,inside)>b){a=a.map(x=>-x);b=-b}
 return {a,b}
}
export function lpHalfspaces(key){
 if(!lpShapes[key])throw new RangeError('Unknown displayed LP')
 if(key==='strip')return [{a:[1,-1],b:1},{a:[-1,1],b:1}]
 if(key==='infeasible')return [{a:[1,0],b:0},{a:[-1,0],b:-1}]
 const {vertices,rays}=lpShapes[key],inside=[0,1].map(i=>vertices.reduce((sum,p)=>sum+p[i],0)/vertices.length)
 const pairs=vertices.slice(1).map((p,i)=>[vertices[i],p])
 if(!rays.length)pairs.push([vertices.at(-1),vertices[0]])
 const constraints=pairs.map(([p,q])=>supportingHalfspace(p,q.map((v,i)=>v-p[i]),inside))
 for(const ray of rays)constraints.push(supportingHalfspace(vertices[ray.from],ray.d,inside))
 return constraints
}

export function planarLp(key,c){
 if(!lpShapes[key]||c.length!==2||!c.every(Number.isFinite))throw new RangeError('Invalid displayed LP')
 if(key==='infeasible')return {status:'infeasible',certificate:'x1<=0 and x1>=1'}
 const scale=Math.max(1,...c.map(Math.abs)),tolerance=1e-10*scale
 if(key==='strip'){
  const along=c[0]+c[1]
  if(Math.abs(along)>tolerance)return {status:'unbounded',point:[0,0],ray:[-Math.sign(along),-Math.sign(along)],slope:-Math.abs(along),tolerance}
  if(Math.abs(c[0])<=tolerance)return {status:'optimal',value:0,dimension:2,whole:true,best:[],point:[0,0],flatRays:[[1,1],[-1,-1]],tolerance}
  const difference=-Math.sign(c[0])
  return {status:'optimal',value:-Math.abs(c[0]),dimension:1,point:[difference,0],lineDirection:[1,1],best:[],tolerance}
 }
 const {vertices,rays}=lpShapes[key],bad=rays.find(ray=>dot(c,ray.d)<-tolerance)
 if(bad)return {status:'unbounded',point:vertices[bad.from],ray:bad.d,slope:dot(c,bad.d),tolerance}
 const values=vertices.map(p=>dot(c,p)),value=Math.min(...values)
 const best=values.map((v,i)=>Math.abs(v-value)<=tolerance?i:-1).filter(i=>i>=0)
 const flatRays=rays.filter(ray=>Math.abs(dot(c,ray.d))<=tolerance).map(ray=>ray.d)
 const whole=c.every(v=>Math.abs(v)<=tolerance)
 return {status:'optimal',value,best,point:vertices[best[0]],flatRays,whole,dimension:whole?2:best.length>1||flatRays.length?1:0,tolerance}
}

export function cubeLp(c){
 if(c.length!==3||!c.every(Number.isFinite))throw new RangeError('Need three finite coefficients')
 const tolerance=1e-10*Math.max(1,...c.map(Math.abs))
 const free=c.map((v,i)=>Math.abs(v)<=tolerance?i:-1).filter(i=>i>=0)
 const vertices=Array.from({length:8},(_,i)=>[0,1,2].map(j=>(i>>j)&1))
 const best=vertices.map((p,i)=>c.every((v,j)=>Math.abs(v)<=tolerance||p[j]===(v<0?1:0))?i:-1).filter(i=>i>=0)
 return {vertices,best,dimension:free.length,free,point:c.map(v=>v<0?1:0),value:c.reduce((sum,v)=>sum+Math.min(0,v),0),tolerance}
}
