import {closestOnSegment,closestPolygons,clipPolygon,insideConvexPolygon} from './convex-geometry.mjs'

const clamp=(v,lo,hi)=>Math.min(hi,Math.max(lo,v))
export function quadraticBox(center,rho=0){
 if(Math.abs(rho)>1)throw RangeError('This lab requires a positive semidefinite quadratic')
 const value=p=>{const [a,b]=p.map((v,i)=>v-center[i]);return a*a+2*rho*a*b+b*b}
 const candidates=[]
 if(center.every(v=>v>=0&&v<=2))candidates.push([...center])
 for(const fixed of [0,2]){
  candidates.push([fixed,clamp(center[1]-rho*(fixed-center[0]),0,2)])
  candidates.push([clamp(center[0]-rho*(fixed-center[1]),0,2),fixed])
 }
 const unique=candidates.filter((p,i)=>candidates.findIndex(q=>Math.hypot(p[0]-q[0],p[1]-q[1])<1e-10)===i)
 const minimum=Math.min(...unique.map(value)),best=unique.filter(p=>Math.abs(value(p)-minimum)<1e-9).sort((a,b)=>a[0]-b[0]||a[1]-b[1])
 const point=best.reduce((a,p)=>a.map((v,i)=>v+p[i]/best.length),[0,0])
 return {value,minimum,best,point,gradient:[2*(point[0]-center[0]+rho*(point[1]-center[1])),2*(point[1]-center[1]+rho*(point[0]-center[0]))]}
}
export function convexPolygonDistance(a,b){
 let intersection=a.map(p=>[...p])
 for(let i=0;i<b.length;i++){
  const p=b[i],q=b[(i+1)%b.length],normal=[q[1]-p[1],p[0]-q[0]]
  intersection=clipPolygon(intersection,normal,normal[0]*p[0]+normal[1]*p[1])
 }
 if(intersection.length){const p=intersection.reduce((s,q)=>s.map((v,i)=>v+q[i]/intersection.length),[0,0]);return {p,q:[...p],distance:0,squared:0,intersection}}
 const result=closestPolygons(a,b)
 return {...result,squared:result.distance**2,intersection:[]}
}
export function cubeDistance(lower){
 const p=[],q=[]
 for(const start of lower){
  if(start>1){p.push(1);q.push(start)}
  else if(start+1<0){p.push(0);q.push(start+1)}
  else{const common=(Math.max(0,start)+Math.min(1,start+1))/2;p.push(common);q.push(common)}
 }
 const squared=p.reduce((s,v,i)=>s+(v-q[i])**2,0)
 return {p,q,squared,distance:Math.sqrt(squared)}
}
export const variancePolygon=[[0,0],[.5,0],[.75,.25],[.5,.5]]
export function projectVariancePoint(point){
 if(insideConvexPolygon(point,variancePolygon))return [...point]
 let best
 for(let i=0;i<variancePolygon.length;i++){
  const candidate=closestOnSegment(point,variancePolygon[i],variancePolygon[(i+1)%variancePolygon.length])
  if(!best||candidate.distance<best.distance)best=candidate
 }
 return best.point
}
export function distributionVariance([p0,p4]){
 const p2=1-p0-p4,mean=2*p2+4*p4,second=4*p2+16*p4
 return {p:[p0,p2,p4],mean,second,variance:second-mean*mean}
}
export const fitData=[[1,2],[2,3.5],[3,5.5],[4,7]]
export const fittedIntercept=slope=>4.5-2.5*slope
export const fittedError=slope=>5*(slope-1.7)**2+.05
// Variance is expressed in squared percentage points, so its square root is a percent.
export const portfolioVariance=w=>225*w*w-30*w*(1-w)+25*(1-w)**2
export const portfolioReturn=w=>4+6*w
export function portfolioMinimum(target){
 if(target>10)return null
 const weight=Math.max(1/7,(target-4)/6)
 return {weight,variance:portfolioVariance(weight),expected:portfolioReturn(weight)}
}
