import test from 'node:test'
import assert from 'node:assert/strict'
import {lpShapes,lpHalfspaces,planarLp,cubeLp} from '../../src/features/labs/services/linear-program-geometry.mjs'
const dot=(a,b)=>a.reduce((sum,v,i)=>sum+v*b[i],0)

test('displayed finite optima bound all convex combinations and recession rays',()=>{
 for(const key of ['bounded','unbounded']){
  const shape=lpShapes[key],constraints=lpHalfspaces(key)
  for(const p of shape.vertices)assert(constraints.every(({a,b})=>dot(a,p)<=b+1e-10))
  for(const ray of shape.rays)assert(constraints.every(({a})=>dot(a,ray.d)<=1e-10))
  for(const c of [[1,1],[-1,-1],[0,1],[1,0],[0,0]]){
   const result=planarLp(key,c)
   if(result.status==='optimal'){
    for(let i=0;i<shape.vertices.length;i++)for(let j=0;j<shape.vertices.length;j++){
     const p=shape.vertices[i].map((v,k)=>(v+2*shape.vertices[j][k])/3)
     assert(dot(c,p)>=result.value-1e-10)
     for(const ray of shape.rays)assert(dot(c,p.map((v,k)=>v+17*ray.d[k]))>=result.value-1e-10)
    }
   }else{
    assert(result.slope<0)
    for(const t of [0,1,100]){
     const p=result.point.map((v,k)=>v+t*result.ray[k])
     assert(constraints.every(({a,b})=>dot(a,p)<=b+1e-9))
     assert(Math.abs(dot(c,p)-dot(c,result.point)-t*result.slope)<1e-9)
    }
   }
  }
 }
})

test('flat edges, entire feasible regions and a strip without vertices are distinct',()=>{
 assert.deepEqual(planarLp('bounded',[-1.6,-1.7]).best,[2,3])
 assert.equal(planarLp('bounded',[0,0]).dimension,2)
 const strip=planarLp('strip',[1,-1])
 assert.equal(strip.value,-1);assert.deepEqual(strip.lineDirection,[1,1])
 assert.equal(planarLp('strip',[-1,-1]).status,'unbounded')
 assert.equal(planarLp('infeasible',[0,0]).status,'infeasible')
})

test('cube optimal sets have the predicted dimensions and bound every interior point',()=>{
 for(const c of [[1,2,3],[1,2,0],[1,0,0],[0,0,0],[-1,1,-1]]){
  const result=cubeLp(c)
  assert.equal(result.best.length,2**result.dimension)
  for(const index of result.best)assert.equal(dot(c,result.vertices[index]),result.value)
  for(const x of [0,.2,.5,1])for(const y of [0,.2,.5,1])for(const z of [0,.2,.5,1])assert(dot(c,[x,y,z])>=result.value-1e-12)
 }
})
