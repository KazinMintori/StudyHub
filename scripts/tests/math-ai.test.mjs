import test from 'node:test'
import assert from 'node:assert/strict'
import { mix, optimizerTrace, dualCertificate, solveSmallLP, bellmanTrace } from '../../docs/.vitepress/theme/math-ai.mjs'
const near=(a,b,tolerance=1e-9)=>assert(Math.abs(a-b)<=tolerance,`${a} != ${b}`)

test('Affine segment endpoints, midpoint, extrapolation and the chord gap',()=>{
  const a=[-1,1],b=[2,-1]
  assert.deepEqual(mix(a,b,1),a);assert.deepEqual(mix(a,b,0),b)
  assert.deepEqual(mix(a,b,.5),[.5,0]);near(mix(a,b,1.2)[0],-1.6)
  for(let i=0;i<=20;i++){const t=i/20,z=-t+2*(1-t),chord=t+4*(1-t);near(chord-z*z,9*t*(1-t));assert(chord>=z*z-1e-12)}
})
test('Primal and dual gap are nonnegative and vanish at the certificate',()=>{
  for(const x of [-2,0,1])for(let i=0;i<=40;i++)assert(dualCertificate(i/10,x).gap>=-1e-12)
  assert.deepEqual(dualCertificate(2),{primal:1,dual:1,gap:0,minimizer:1})
  near(dualCertificate(0).gap,1);assert.throws(()=>dualCertificate(-1));assert.throws(()=>dualCertificate(2,2))
})
test('Gradient converges below its curvature threshold and diverges above it',()=>{
  const converging=optimizerTrace({rate:.15,kappa:10,steps:100})
  near(converging[1].value,6.445)
  assert(converging.at(-1).value<1e-12)
  const edge=optimizerTrace({rate:.2,kappa:10});near(edge.at(-1).x[1],2)
  assert(optimizerTrace({rate:.25,kappa:10}).at(-1).value>1000)
  assert.deepEqual(optimizerTrace({method:'newton'})[1].x,[0,0])
})
test('Momentum and Nesterov use different gradient locations after the first step',()=>{
  const params={rate:.1,kappa:1,start:[-1,0],momentum:.9,steps:2}
  const heavy=optimizerTrace({...params,method:'momentum'}),nesterov=optimizerTrace({...params,method:'nesterov'})
  near(heavy[1].x[0],-.9);near(heavy[2].x[0],-.72)
  near(nesterov[1].x[0],-.9);near(nesterov[2].x[0],-.729)
})
test('Adam bias correction recovers the signed first gradient and its square',()=>{
  const row=optimizerTrace({method:'adam',steps:1,rate:.1,start:[2,-2],kappa:1})[1]
  near(row.m[0]/.1,2);near(row.v[0]/.001,4)
  near(row.x[0],1.9,1e-8);near(row.x[1],-1.9,1e-8)
  for(const method of ['gd','momentum','nesterov','adagrad','rmsprop','adam','newton']){
    const zeros=optimizerTrace({method,start:[0,0]})
    assert(zeros.every(r=>r.x.every(x=>Number.isFinite(x)&&x===0)))
  }
})
test('Small LP finds all optimal vertices, including a whole optimal face',()=>{
  assert.equal(solveSmallLP().value,10);assert.deepEqual(solveSmallLP().optimal,[[2,2]])
  assert.deepEqual(solveSmallLP([1,1]).optimal,[[2,2],[0,4]])
  assert.equal(solveSmallLP([0,0]).optimal.length,4)
  assert.deepEqual(solveSmallLP([-1,-1]).optimal,[[0,0]])
})
test('Bellman recursion recovers both shortest and longest paths on a DAG',()=>{
  const min=bellmanTrace().at(-1)
  assert.deepEqual(min.values,{T:0,B:1,A:3,S:4})
  assert.deepEqual(min.actions,{T:null,B:'T',A:'B',S:'A'})
  const max=bellmanTrace(undefined,undefined,undefined,true).at(-1)
  assert.deepEqual(max.values,{T:0,B:1,A:5,S:6})
  assert.throws(()=>bellmanTrace(undefined,['S','A','B','T']))
})
