import test from 'node:test'
import assert from 'node:assert/strict'
import {chebyshevShapes,chebyshevModel,momentDistribution,probabilitySummary} from '../../src/features/labs/services/lp-models-geometry.mjs'

test('the Chebyshev LP has a verified radius and an entire segment of rectangle centers',()=>{
 const first=chebyshevModel(chebyshevShapes.pentagon)
 assert(Math.abs(first.radius-(6-2*Math.sqrt(5)))<1e-10)
 for(const shape of [chebyshevShapes.pentagon,chebyshevShapes.rectangle]){
  const result=chebyshevModel(shape)
  for(const point of [...result.centers,result.center])assert(shape.every(({a,b})=>a[0]*point[0]+a[1]*point[1]+result.radius*Math.hypot(...a)<=b+1e-8))
 }
 const rectangle=chebyshevModel(chebyshevShapes.rectangle)
 assert.equal(rectangle.radius,1)
 assert.equal(rectangle.centers.length,2)
 assert.deepEqual(rectangle.center,[2,1])
 assert.equal(chebyshevModel(chebyshevShapes.empty),null)
})
test('moment parameterization preserves all equalities and the sharp tail certificate',()=>{
 for(let i=0;i<=20;i++)for(let j=0;j<=20-i;j++){
  const s=i/120,t=j/240,p=momentDistribution(s,t),result=probabilitySummary(p)
  assert(p.every(value=>value>=-1e-12))
  assert(Math.abs(result.sum-1)<1e-12&&Math.abs(result.mean-1)<1e-12&&Math.abs(result.second-2)<1e-12)
  assert(result.tail<=1/6+1e-12)
  const certificate=p.reduce((sum,v,k)=>sum+k*(k-1)*v/6,0)
  assert(Math.abs(certificate-1/6)<1e-12&&result.tail<=certificate+1e-12)
 }
 assert.equal(probabilitySummary(momentDistribution(1/6,0)).tail,1/6)
 assert.equal(probabilitySummary(momentDistribution(0,0)).tail,0)
})
