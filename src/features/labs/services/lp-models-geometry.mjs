import {polyhedronInBox} from './convex-geometry.mjs'

export const chebyshevShapes={
 pentagon:[{a:[-1,0],b:0},{a:[0,-1],b:0},{a:[1,2],b:8},{a:[3,1],b:12},{a:[-1,1],b:3}],
 rectangle:[{a:[-1,0],b:0},{a:[0,-1],b:0},{a:[1,0],b:4},{a:[0,1],b:2}],
 empty:[{a:[-1,0],b:-2},{a:[0,-1],b:0},{a:[1,0],b:1},{a:[0,1],b:2}]
}
export function solveLinearSystem(matrix,rhs){
 const n=rhs.length,a=matrix.map((row,i)=>[...row,rhs[i]])
 for(let col=0;col<n;col++){
  let pivot=col
  for(let i=col+1;i<n;i++)if(Math.abs(a[i][col])>Math.abs(a[pivot][col]))pivot=i
  if(Math.abs(a[pivot][col])<1e-11)return null
  ;[a[col],a[pivot]]=[a[pivot],a[col]]
  const value=a[col][col]
  for(let j=col;j<=n;j++)a[col][j]/=value
  for(let i=0;i<n;i++)if(i!==col){const factor=a[i][col];for(let j=col;j<=n;j++)a[i][j]-=factor*a[col][j]}
 }
 return a.map(row=>row[n])
}

// Used only with the displayed positively spanning normal families. Their
// feasible polygons are bounded, so enumerating triples is valid at this size.
export function chebyshevModel(constraints){
 const rows=constraints.map(({a,b})=>({a:[...a,Math.hypot(...a)],b})).concat([{a:[0,0,-1],b:0}])
 const feasible=[]
 for(let i=0;i<rows.length;i++)for(let j=i+1;j<rows.length;j++)for(let k=j+1;k<rows.length;k++){
  const selected=[rows[i],rows[j],rows[k]],point=solveLinearSystem(selected.map(row=>row.a),selected.map(row=>row.b))
  if(point&&rows.every(row=>row.a.reduce((s,v,index)=>s+v*point[index],0)<=row.b+1e-8))feasible.push(point)
 }
 if(!feasible.length)return null
 const radius=Math.max(0,...feasible.map(point=>point[2])),centers=[]
 for(const point of feasible)if(Math.abs(point[2]-radius)<1e-7&&!centers.some(other=>Math.hypot(other[0]-point[0],other[1]-point[1])<1e-7))centers.push(point.slice(0,2))
 return {radius,centers,center:[0,1].map(i=>centers.reduce((s,p)=>s+p[i],0)/centers.length)}
}
export function polygonCentroid(constraints){
 const polygon=polyhedronInBox(constraints,[-100,100,-100,100])
 if(polygon.length<3)return null
 let area=0,x=0,y=0
 for(let i=0;i<polygon.length;i++){
  const p=polygon[i],q=polygon[(i+1)%polygon.length],cross=p[0]*q[1]-q[0]*p[1]
  area+=cross;x+=(p[0]+q[0])*cross;y+=(p[1]+q[1])*cross
 }
 return Math.abs(area)<1e-10?null:[x/(3*area),y/(3*area)]
}
export const momentTriangle=[[0,0],[1/6,0],[0,1/12]]
export function momentDistribution(s,t){return [.5-s-3*t,3*s+8*t,.5-3*s-6*t,s,t]}
export function probabilitySummary(p){
 return {sum:p.reduce((a,b)=>a+b,0),mean:p.reduce((a,b,i)=>a+i*b,0),second:p.reduce((a,b,i)=>a+i*i*b,0),tail:p[3]+p[4]}
}
