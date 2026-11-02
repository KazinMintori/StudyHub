import test from 'node:test'
import assert from 'node:assert/strict'
import {apolloniusBoxLevel,distanceRatio} from '../../src/features/labs/services/apollonius-feasibility.mjs'

test('box certificates work in R2 and R3 without the known optimum',()=>{
 for(const dimension of [2,3]){
  for(const level of [0,.125,.23,.25,.5,.9,1]){
   const result=apolloniusBoxLevel(level,dimension)
   assert(result.candidate.every((value,i)=>value>=result.bounds[i][0]&&value<=result.bounds[i][1]))
   assert.equal(result.status,level<=.23?'infeasible':'feasible')
   if(result.status==='feasible')assert(distanceRatio(result.candidate)<=level)
   if(result.kind==='ball'){
    // The candidate minimizes the convex quadratic on the box. Every sampled
    // point must lie above its residual, whether the trial is feasible or not.
    for(const x of [-1,-.3,.4,1.5])for(const y of [1,1.4,2,3])for(const z of dimension===3?[-1,0,1]:[0]){
     const p=dimension===3?[x,y,z]:[x,y]
     const value=p.reduce((s,v)=>s+v*v,0)-level*level*((x-4)**2+y*y+z*z)
     assert(value>=result.residual-1e-10)
    }
   }
  }
 }
})

test('near-contact classification does not silently choose a bisection branch',()=>{
 const level=Math.sqrt(5)-2
 for(const dimension of [2,3]){
  const result=apolloniusBoxLevel(level,dimension)
  assert.equal(result.status,'boundary')
  assert(Math.abs(result.residual)<=result.tolerance)
 }
})

test('the terminal upper bracket retains a genuine feasible witness',()=>{
 let lower=0,upper=1,witness=[0,1]
 for(let i=0;i<7;i++){
  const trial=(lower+upper)/2,result=apolloniusBoxLevel(trial)
  assert.notEqual(result.status,'boundary')
  if(result.status==='feasible'){upper=trial;witness=result.candidate}
  else lower=trial
  assert(distanceRatio(witness)<=upper)
 }
 assert.equal(lower,30/128)
 assert.equal(upper,31/128)
 assert(upper-lower<=.01)
})

test('the halfspace endpoint and invalid domains are handled explicitly',()=>{
 assert.equal(apolloniusBoxLevel(1).kind,'halfspace')
 for(const value of [-.1,1.01,NaN,Infinity])assert.throws(()=>apolloniusBoxLevel(value),RangeError)
 assert.throws(()=>apolloniusBoxLevel(.5,4),RangeError)
 assert.equal(distanceRatio([4,0]),Infinity)
})
