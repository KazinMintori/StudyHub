import {closestOnSegment,insideConvexPolygon} from './convex-geometry.mjs'

export const fractionalVertices=[[1,0],[6,0],[2,4],[1,4]]
export const fractionalDenominator=([x,y])=>x+y/2+1
export const fractionalNumerator=([x,y])=>x+2*y+2
export const fractionalValue=p=>fractionalNumerator(p)/fractionalDenominator(p)
export function cooperTransform(p){const d=fractionalDenominator(p);return [p[0]/d,p[1]/d,1/d]}
export function cooperInverse([y1,y2,z]){return z>0?[y1/z,y2/z]:null}
export function projectToPolygon(point,vertices=fractionalVertices){
 const area=vertices.reduce((sum,p,i)=>sum+p[0]*vertices[(i+1)%vertices.length][1]-p[1]*vertices[(i+1)%vertices.length][0],0)
 if(insideConvexPolygon(point,area<0?[...vertices].reverse():vertices,1e-12))return [...point]
 let best
 for(let i=0;i<vertices.length;i++){
  const candidate=closestOnSegment(point,vertices[i],vertices[(i+1)%vertices.length])
  if(!best||candidate.distance<best.distance)best=candidate
 }
 return best.point
}
export function fractionalSection(t,mode='max'){
 const sign=mode==='max'?1:-1,output=[]
 const g=p=>sign*(fractionalNumerator(p)-t*fractionalDenominator(p))
 for(let i=0;i<fractionalVertices.length;i++){
  const p=fractionalVertices[i],q=fractionalVertices[(i+1)%fractionalVertices.length],a=g(p),b=g(q)
  if(a>=-1e-10)output.push([...p])
  if(a*b<0){const weight=a/(a-b);output.push(p.map((v,j)=>v+weight*(q[j]-v)))}
 }
 return output.filter((p,i)=>output.findIndex(q=>Math.hypot(p[0]-q[0],p[1]-q[1])<1e-9)===i)
}

// Invert the affine orthographic projection restricted to y1 + y2/2 + z = 1.
// Clamp in the visible polygon before inversion: its z is bounded away from zero.
export function cooperFromScreen(point,project){
 const polygon=fractionalVertices.map(p=>project(cooperTransform(p)))
 const target=projectToPolygon(point,polygon),origin=project([0,0,1])
 const a=project([1,0,0]).map((v,i)=>v-origin[i])
 const b=project([0,1,.5]).map((v,i)=>v-origin[i])
 const u=target.map((v,i)=>v-origin[i]),det=a[0]*b[1]-a[1]*b[0]
 if(Math.abs(det)<1e-10)throw Error('The camera projects the normalization plane onto a line')
 const y1=(u[0]*b[1]-u[1]*b[0])/det,y2=(a[0]*u[1]-a[1]*u[0])/det
 return projectToPolygon(cooperInverse([y1,y2,1-y1-y2/2]))
}
