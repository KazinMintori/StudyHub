import test from 'node:test'
import assert from 'node:assert/strict'
import {quadraticBox,convexPolygonDistance,cubeDistance,projectVariancePoint,distributionVariance,portfolioMinimum,portfolioVariance} from '../../src/features/labs/services/qp-geometry.mjs'
const near=(a,b)=>assert(Math.abs(a-b)<1e-8,`${a} differs from ${b}`)
test('box QP uses the coupled metric and satisfies first-order optimality on every active bound',()=>{
 for(const rho of [0,.6,1])for(const a of [-1,0,1,3])for(const b of [-1,.2,1,3]){
  const m=quadraticBox([a,b],rho)
  for(let i=0;i<2;i++){
   const x=m.point[i],g=m.gradient[i]
   assert(x>=0&&x<=2)
   if(x<1e-9)assert(g>=-1e-8)
   else if(x>2-1e-9)assert(g<=1e-8)
   else near(g,0)
  }
 }
 const edge=quadraticBox([3,1],.6);near(edge.point[0],2);near(edge.point[1],1.6);near(edge.minimum,.64)
 assert.deepEqual(quadraticBox([1,1],1).best.filter(p=>p[0]===0||p[0]===2),[[0,2],[2,0]])
})
test('polygon and cube distance return actual feasible common witnesses at overlap or contact',()=>{
 const square=[[0,0],[1,0],[1,1],[0,1]]
 for(const shift of [[.2,.3],[1,0],[3,2]]){
  const b=square.map(p=>p.map((v,i)=>v+shift[i])),m=convexPolygonDistance(square,b)
  near(m.squared,Math.max(shift[0]-1,0)**2+Math.max(shift[1]-1,0)**2)
  for(let i=0;i<2;i++){assert(m.p[i]>=-1e-9&&m.p[i]<=1+1e-9);assert(m.q[i]>=shift[i]-1e-9&&m.q[i]<=shift[i]+1+1e-9)}
 }
 for(const lower of [[2.5,2,1.6],[2,.2,.2],[1,0,0],[.3,.3,.3],[-2,0,0]]){
  const m=cubeDistance(lower)
  near(m.distance**2,m.squared)
  for(let i=0;i<3;i++){assert(m.p[i]>=0&&m.p[i]<=1);assert(m.q[i]>=lower[i]&&m.q[i]<=lower[i]+1)}
 }
})
test('distribution constraints and portfolio targets are preserved, including their exact extrema',()=>{
 for(const p of [[.5,.5],[0,0],[.75,.25],[-1,4],[4,-1],[.4,.2]]){
  const m=distributionVariance(projectVariancePoint(p));near(m.p.reduce((a,b)=>a+b,0),1)
  assert(m.p.every(v=>v>=-1e-9));assert(m.mean>=1-1e-9&&m.mean<=2+1e-9);assert(m.variance>=-1e-9&&m.variance<=4+1e-9)
 }
 near(distributionVariance([.5,.5]).variance,4);near(distributionVariance([0,0]).variance,0)
 near(portfolioMinimum(4).weight,1/7);near(portfolioMinimum(7).weight,.5);assert.equal(portfolioMinimum(10.5),null)
 for(const target of [3.5,4,7,10]){
  const m=portfolioMinimum(target)
  assert(m.expected>=target-1e-9)
  for(let i=0;i<=100;i++){const w=i/100;if(4+6*w>=target)assert(portfolioVariance(w)>=m.variance-1e-9)}
 }
})
