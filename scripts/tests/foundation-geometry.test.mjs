import test from 'node:test'
import assert from 'node:assert/strict'
import { project3, unprojectPlane, leastNormExample, dot, svdStages, norm2, curvatureModel, lineParameter, planeParameters, projectToHyperplane, planeBoxSection, pNorm3, ellipsoidGauge, rotate2, trigonometricSlabWorst, lineFitSpace, boxWorstCase, ellipsoidResource, standardNormalCdf, ridgeScalar, minimaxRatio, minimaxRatioLevel, geometricProgramOptimum, equalityQpExample, resourceSensitivity, chebyshevCertificate, entropyMoment, cappedWaterChannel, weightedCappedWaterfill, weightedWaterDual, cycleFiveModel, perronCertificate } from '../../src/features/labs/services/foundation-geometry.mjs'
const near = (a, b) => assert(Math.abs(a - b) < 1e-9, `${a} != ${b}`)

test('Perron vector ratios certify the matrix radius and distinguish improving a design from improving its bound',()=>{
 for(const t of [.25,.5,1,2,3,4])for(const r of [.25,.5,1,2,4]){
  const row=perronCertificate(t,r)
  assert(row.radius>=.5-1e-9&&row.upper>=row.radius-1e-9)
  row.image.forEach((v,i)=>assert(v<=row.upper*row.vector[i]+1e-9))
  near(perronCertificate(t,t).gap,0)
  near(row.matrix[0][0]*row.matrix[1][1]-row.matrix[0][1]*row.matrix[1][0],0)
 }
 near(perronCertificate(2,1).radius,.625)
 near(perronCertificate(2,1).upper,.75)
 assert.throws(()=>perronCertificate(0,1),RangeError)
 assert.throws(()=>perronCertificate(1,Infinity),RangeError)
})

test('all cycle sign assignments obey the cut identity and lifting; the rank-two optimum attains the dual bound',()=>{
 let optimum=Infinity,count=0
 for(let mask=0;mask<32;mask++){
  const signs=Array.from({length:5},(_,i)=>(mask&(1<<i))?1:-1)
  const row=cycleFiveModel(signs,signs.map(s=>s===1?0:Math.PI))
  near(row.relaxed,row.integerValue);near(row.relaxedCut,row.cuts)
  assert.equal(row.rank,1)
  signs.forEach((s,i)=>near(signs[(i+4)%5]+signs[(i+1)%5]+row.nu[i]*s,0))
  if(row.integerValue<optimum){optimum=row.integerValue;count=1}else if(row.integerValue===optimum)count++
  assert(row.cuts<=Math.floor(row.cutUpper))
 }
 near(optimum,-6);assert.equal(count,10)
 const row=cycleFiveModel([1,-1,1,-1,1],Array.from({length:5},(_,i)=>4*Math.PI*i/5))
 near(row.relaxed,row.dual);assert.equal(row.rank,2)
 row.gram.forEach((r,i)=>near(r[i],1))
 for(let seed=0;seed<30;seed++){
  const trial=cycleFiveModel([1,1,1,1,1],Array.from({length:5},(_,i)=>Math.sin(seed+i)*Math.PI))
  assert(trial.relaxed>=trial.dual-1e-9)
 }
})

test('capped water channel value is a minimum for negative, zero and positive multipliers',()=>{
 for(const [alpha,weight,cap]of [[1,2,1],[2,1,2],[5,2,1]])for(const nu of [-1,0,.25,1/3,.4,.5,.75,1,2,3]){
  const row=cappedWaterChannel(alpha,weight,cap,nu)
  assert(row.x>=0&&row.x<=cap)
  for(let step=0;step<=100;step++){
   const x=cap*step/100
   assert(-weight*Math.log(alpha+x)+nu*x>=row.value-1e-9)
  }
 }
})

test('weighted water allocation, multiplier interval and global shadow-price bounds agree',()=>{
 for(const budget of [.05,.5,1,1.2,1.5,2,3,3.5,3.95]){
  const row=weightedCappedWaterfill(budget)
  near(row.point.reduce((s,v)=>s+v,0),budget)
  assert(row.point.every((v,i)=>v>=0&&v<=[1,2,1][i]))
  for(const nu of [row.nu[0],(row.nu[0]+row.nu[1])/2,row.nu[1]]){
   const dual=weightedWaterDual(budget,nu)
   near(dual.total,budget);near(dual.value,row.value)
   for(const other of [.1,.9,1,1.1,1.5,2,3,3.9])assert(weightedCappedWaterfill(other).value>=row.value-nu*(other-budget)-1e-9)
  }
  for(const nu of [-1,0,.2,.75,1.5,2.1])assert(weightedWaterDual(budget,nu).value<=row.value+1e-9)
 }
 assert.deepEqual(weightedCappedWaterfill(1).nu,[.5,1])
 const h=1e-6,v=weightedCappedWaterfill(1).value
 assert(Math.abs((v-weightedCappedWaterfill(1-h).value)/h+1)<1e-5)
 assert(Math.abs((weightedCappedWaterfill(1+h).value-v)/h+.5)<1e-5)
 assert.throws(()=>weightedCappedWaterfill(4),RangeError)
})

test('Chebyshev bound is feasible over its whole segment and matches all primal residuals at optimum',()=>{
 for(const w0 of [-1.5,-.5,0,1])for(const w1 of [-.5,1,2])for(const t of [-.25,0,.25]){
  const row=chebyshevCertificate([w0,w1],t)
  assert(row.norm<=1+1e-9)
  near(row.nu.reduce((s,v)=>s+v,0),0)
  near(row.nu[1]+2*row.nu[2],0)
  assert(row.dual<=row.value+1e-9)
  near(-dot(row.nu,row.residual),row.dual)
 }
 near(chebyshevCertificate([-.5,1],.25).gap,0)
})

test('entropy primal line, normalized exponential family and dual bound retain their distinct constraints',()=>{
 const optimum=10*Math.log(2)/7-Math.log(7)
 for(const t of [3/7+.001,.5,4/7,.7,5/7-.001])for(const eta of [-2,-Math.log(2),0,1]){
  const row=entropyMoment(t,eta)
  assert(row.point.every(v=>v>0))
  near(row.point.reduce((s,v)=>s+v,0),1)
  near(row.point[1]+2*row.point[2],10/7)
  near(row.induced.reduce((s,v)=>s+v,0),1)
  assert(row.induced.every(v=>v>0))
  assert(row.dual<=optimum+1e-9&&optimum<=row.value+1e-9)
  row.induced.forEach((p,i)=>near(Math.log(p)+1+row.tau+eta*i,0))
 }
 const row=entropyMoment(4/7,-Math.log(2))
 near(row.gap,0);near(row.mean,10/7)
 near(entropyMoment(.5,0).mean,1)
})

test('resource parameter model obeys KKT, both thresholds and the global sensitivity bound',()=>{
 for(const budget of [.05,.5,1,1.5,2,2.2,3,4.5]){
  const row=resourceSensitivity(budget)
  assert(row.point.every(v=>v>=0)&&row.slack>=-1e-9)
  assert(row.lambda>=0&&row.mu.every(v=>v>=0))
  near(row.point[0]-2+row.lambda-row.mu[0],0)
  near(row.point[1]-1+row.lambda-row.mu[1],0)
  near(row.lambda*row.slack,0)
  row.point.forEach((v,i)=>near(v*row.mu[i],0))
  for(let other=.05;other<=4.5;other+=.05){
   assert(resourceSensitivity(other).value>=row.value-row.lambda*(other-budget)-1e-9)
  }
  const h=1e-6
  const derivative=(resourceSensitivity(budget+h).value-resourceSensitivity(budget-h).value)/(2*h)
  assert(Math.abs(derivative+row.lambda)<1e-5)
 }
 assert.deepEqual(resourceSensitivity(1).point,[1,0])
 assert.deepEqual(resourceSensitivity(3).point,[2,1])
 near(resourceSensitivity(2.2).value,.16)
 assert.throws(()=>resourceSensitivity(0),RangeError)
})

test('equality QP keeps every dragged primal point feasible and every dual bound below the true optimum',()=>{
 for(const t of [-.8,-.25,0,.4,.8])for(const nu1 of [-3,-.25,0,1.5])for(const nu2 of [-3,-1.25,0,1.5]){
  const row=equalityQpExample(t,[nu1,nu2])
  row.residual.forEach(value=>near(value,0))
  near(row.value,11/8+2*t*t)
  assert(row.dual<=11/8+1e-9)
  assert(row.primalError<=row.gap+1e-9)
 }
 const optimal=equalityQpExample(0,[-.25,-1.25])
 near(optimal.gap,0)
 near(equalityQpExample(-.25,[0,-1]).gap,.25)
})

test('parameterized GP retains its product and changes active bound at the dimension-dependent threshold',()=>{
 for(let n=2;n<=6;n++)for(const a of [.25,1,2,8]){
  const row=geometricProgramOptimum(n,a)
  near(row.product,1)
  assert(row.point[0]>=a)
  row.point.forEach(x=>assert(x>0))
  const costs=row.point.map((x,i)=>x*row.weights[i])
  costs.slice(1).forEach(x=>near(x,costs[1]))
  if(a<row.threshold)costs.forEach(x=>near(x,row.threshold))
  else near(row.point[0],a)
 }
 geometricProgramOptimum(3,1).point.forEach((value,i)=>near(value,[2,1,.5][i]))
 geometricProgramOptimum(3,8).point.forEach((value,i)=>near(value,[8,.5,.25][i]))
 near(geometricProgramOptimum(3,8).value,10)
 assert.throws(()=>geometricProgramOptimum(1,1),RangeError)
 assert.throws(()=>geometricProgramOptimum(3,0),RangeError)
})

test('minimax ratio interval is equivalent to both inequalities and bisection retains the optimum',()=>{
 const value=2*Math.sqrt(6)-4,s=(Math.sqrt(6)-1)/2
 near(minimaxRatio(s).value,value)
 for(let tau=.5;tau<=1.5;tau+=.01){
  const level=minimaxRatioLevel(tau)
  if(level.feasible){
   for(const candidate of [level.lower,(level.lower+level.upper)/2,level.upper])assert(minimaxRatio(candidate).value<=tau+1e-9)
  }
  for(let candidate=0;candidate<=1;candidate+=.01){
   const inside=level.feasible&&candidate>=level.lower-1e-9&&candidate<=level.upper+1e-9
   assert.equal(inside,minimaxRatio(candidate).value<=tau+1e-9)
  }
 }
 let lo=.5,hi=1.5
 for(let step=0;step<6;step++){
  const tau=(lo+hi)/2
  if(minimaxRatioLevel(tau).feasible)hi=tau;else lo=tau
  assert(lo<=value&&value<=hi)
 }
 near(hi-lo,1/64)
 assert(minimaxRatio(.9).value>(minimaxRatio(.8).value+minimaxRatio(1).value)/2)
})

test('scalar ridge supports the whole open Pareto front and keeps endpoint distinctions',()=>{
 assert.equal(ridgeScalar(0).gamma,Infinity)
 assert.equal(ridgeScalar(2).gamma,0)
 for(const w of [.01,.1,.5,1,1.5,1.99]){
  const row=ridgeScalar(w),best=row.f1+row.gamma*row.f2
  near(10/(5+row.gamma),w)
  near(1+row.f2/4-row.f1/20,w)
  for(let candidate=-1;candidate<=3;candidate+=.05){
   const trial=ridgeScalar(candidate)
   assert(trial.f1+row.gamma*trial.f2>=best-1e-9)
  }
 }
})

test('box uncertainty worst-case margin matches every corner, including zero coordinates',()=>{
 for(const w of [[1,1],[1,-1],[0,1],[0,0],[-2,.3]])for(const epsilon of [0,.5,1.2]){
  const row=boxWorstCase(w,[2,1],epsilon)
  const values=[[-1,-1],[-1,1],[1,-1],[1,1]].map(c=>dot(w,c.map((v,i)=>[2,1][i]+v*epsilon)))
  near(row.margin,Math.min(...values))
  near(row.margin,dot(w,[2,1])-row.penalty)
 }
})

test('ellipsoid support maximizer is attainable and produces the same SOC/SDP decision',()=>{
 for(const x of [[0,0],[3,3],[16/5,9/5],[5,0],[.2,4],[-1,2]]){
  const row=ellipsoidResource(x)
  near(dot(row.coefficient,x),row.worst)
  assert(Math.hypot(...row.u)<=1+1e-9)
  for(let i=0;i<360;i++){
   const angle=i*Math.PI/180,a=[5+3*Math.cos(angle),5+4*Math.sin(angle)]
   assert(dot(a,x)<=row.worst+1e-9)
  }
  assert.equal(row.worst<=37+1e-9,row.eigenvalues.every(v=>v>=-1e-9))
 }
 near(ellipsoidResource([16/5,9/5]).worst,37)
 near(ellipsoidResource([3,3]).worst,45)
})

test('normal CDF has correct symmetry, tail limits and reference quantiles',()=>{
 near(standardNormalCdf(0),.5)
 assert.equal(standardNormalCdf(Infinity),1)
 assert.equal(standardNormalCdf(-Infinity),0)
 for(const [eta,q]of [[.9,1.2815515655446004],[.95,1.6448536269514722],[.99,2.3263478740408408]]){
  assert(Math.abs(standardNormalCdf(q)-eta)<1e-7)
  const x=10/(2+.3*q)
  assert(Math.abs(standardNormalCdf((10-2*x)/(.3*x))-eta)<1e-7)
 }
 for(let z=-8;z<=8;z+=.1){near(standardNormalCdf(z)+standardNormalCdf(-z),1);assert(standardNormalCdf(z+.1)>=standardNormalCdf(z))}
})

test('least-squares prediction plane has the orthogonal foot and invertible drag at every supported yaw', () => {
  const optimum = lineFitSpace(1.5, 5/6)
  near(optimum.value, 1/6)
  optimum.normalResidual.forEach(value => near(value, 0))
  for (const a of [0, .5, 1.5, 2]) for (const c of [-.5, 0, 5/6, 1.5]) {
    const row = lineFitSpace(a,c)
    near(row.value, optimum.value + dot(row.prediction.map((v,i)=>v-optimum.prediction[i]), row.prediction.map((v,i)=>v-optimum.prediction[i])))
    for (let yaw=-45;yaw<=10;yaw+=5) {
      const P=p=>project3(p,{yaw,pitch:30,scale:42,origin:[200,240]})
      const parameters=planeParameters(P(row.prediction),P([0,0,0]),P([0,1,2]),P([1,1,1]))
      assert(parameters, `Plane became edge-on at ${yaw}`)
      near(parameters[0],a);near(parameters[1],c)
      const origin=P([0,0,0]),u=P([0,1,2]).map((v,i)=>v-origin[i]),v=P([1,1,1]).map((v,i)=>v-origin[i])
      // Lower bound on the smaller singular value of the screen Jacobian.
      // Invertibility alone would permit unusably sensitive near-edge-on views.
      assert(Math.abs(u[0]*v[1]-u[1]*v[0])/Math.hypot(...u,...v)>20)
    }
  }
})

test('restricted 3D drag inverse returns the same point over the supported camera range', () => {
  for (const yaw of [-180, -70, 0, 35, 180]) for (const pitch of [20, 30, 65]) for (const p of [[-1.2, 1.2, 0], [1, -1, 0], [0, 0, 0]]) {
    const camera = { yaw, pitch, scale: 70, origin: [200, 180] }
    const result = unprojectPlane(project3(p, camera), p[2], camera)
    result.forEach((v, i) => near(v, p[i]))
  }
})
test('all dragged least-norm examples remain feasible and obey the Pythagorean identity', () => {
  for (const dim of [2, 3]) for (let t = -1.2; t <= 1.21; t += .1) {
    const e = leastNormExample(dim, t)
    e.residual.forEach(v => near(v, 0))
    near(e.squared, e.minimum + e.extra)
    near(dot(e.closest, e.kernel), 0)
  }
})
test('SVD rotations preserve length and a zero singular value removes a direction', () => {
  const stages = svdStages([.8, .6])
  near(norm2(stages[0]), norm2(stages[1]))
  near(norm2(stages[2]), norm2(stages[3]))
  near(svdStages([1, 1], [1.6, 0])[2][1], 0)
  for (const p of [[1, 0], [0, 1], [.8, .6]]) assert(norm2(svdStages(p).at(-1)) <= 1.6 + 1e-9)
})
test('Schur envelope is an actual minimum in the eliminated variable', () => {
  for (const c of [-1, 0, 1, 4]) for (const y of [-1, 0, .8]) {
    const m = curvatureModel('schur', c), minimum = m.value([-y, y])
    near(minimum, (c - 1) * y * y)
    for (const x of [-1.2, -.3, 0, .9, 1.2]) assert(m.value([x, y]) >= minimum - 1e-9)
  }
})
test('direct affine drag recovers the parameter and ignores the orthogonal displacement', () => {
  const a=[1,1], b=[4,3], d=[3,2]
  for(const t of [-1,0,.5,1,2]) {
    const point=a.map((v,i)=>v+t*d[i])
    near(lineParameter(point,a,b),t)
    near(lineParameter([point[0]-2,point[1]+3],a,b),t)
  }
  assert.equal(lineParameter([1,2],[0,0],[0,0]),null)
})
test('projected affine-plane drag recovers both free parameters at supported camera angles', () => {
  const origin=[1,1,1], a=[-2,1,0], b=[-3,0,1]
  const at=(s,t)=>origin.map((v,i)=>v+s*a[i]+t*b[i])
  for(const yaw of [-45,0,20,45]) {
    const P=p=>project3(p,{yaw,pitch:35,scale:38,origin:[200,210]})
    for(const [s,t] of [[0,0],[.2,-.15],[-.5,.5],[.5,-.5]]) {
      const p=at(s,t), result=planeParameters(P(p),P(origin),P(at(1,0)),P(at(0,1)))
      near(result[0],s);near(result[1],t);near(dot([1,2,3],p),6)
    }
  }
})
test('3D foot lies on its plane, displacement is normal and signed distance has correct orientation',()=>{
 for(const a of [[1,-2,2],[1,0,0],[0,0,1]]) for(const b of [-6,0,6]) for(const x of [[1,1,1],[-2,.5,2],[0,0,0]]){
   const {signed,foot}=projectToHyperplane(x,a,b)
   near(dot(a,foot),b)
   near(norm2(x.map((v,i)=>v-foot[i])),Math.abs(signed))
   near(dot(a,x)-b,signed*norm2(a))
 }
 assert.throws(()=>projectToHyperplane([0,0,0],[0,0,0],1),RangeError)
})
test('plane viewport section is a plane polygon inside the drawing box, including degeneracy',()=>{
 for(const a of [[1,-2,2],[1,0,0],[0,0,1],[1,1,1]])for(const b of [-6,0,2.5,6]){
  const points=planeBoxSection(a,b,2.5)
  points.forEach(p=>{near(dot(a,p),b);assert(p.every(v=>Math.abs(v)<=2.5+1e-9))})
 }
 assert.equal(planeBoxSection([1,0,0],6).length,0)
 assert.equal(planeBoxSection([1,0,0],2.5).length,4)
})
test('norm balls have the expected three-dimensional vertices and nesting',()=>{
 for(const p of [[1,0,0],[0,-1,0],[0,0,1]])for(const q of [1,2,Infinity])near(pNorm3(p,q),1)
 near(pNorm3([1,1,1],Infinity),1);near(pNorm3([1,1,1],1),3)
 for(let i=0;i<40;i++){
  const x=[Math.sin(i),Math.cos(i*2),Math.sin(i*3)]
  assert(pNorm3(x,Infinity)<=pNorm3(x,2)+1e-9)
  assert(pNorm3(x,2)<=pNorm3(x,1)+1e-9)
 }
})
test('rotated ellipsoid gauge matches each principal radius and handles a collapsed axis',()=>{
 const radii=[1.5,.9,.6]
 for(const angle of [0,.3,1])for(let axis=0;axis<3;axis++){
  const local=[0,0,0];local[axis]=radii[axis]
  const point=[...rotate2(local.slice(0,2),angle),local[2]]
  near(ellipsoidGauge(point,radii,angle),1)
 }
 assert.equal(ellipsoidGauge([0,0,.1],[1.5,.9,0]),Infinity)
 near(ellipsoidGauge([.75,0,0],[1.5,.9,0]),.5)
})
test('trigonometric slab feasibility checks an interior extremum as well as endpoints',()=>{
 const result=trigonometricSlabWorst([1.2,-.4])
 near(result.value,.85);near(Math.cos(result.t),.75)
 for(const point of [[0,0],[.5,.5],[2,-1],[-1,.2],[1.2,-.4]]){
   const exact=trigonometricSlabWorst(point),maximum=Math.abs(exact.value)
   for(let i=0;i<=4000;i++){
     const t=-Math.PI/3+i*Math.PI/6000
     const sampled=point[0]*Math.cos(t)+point[1]*Math.cos(2*t)
     assert(Math.abs(sampled)<=maximum+1e-9)
   }
 }
})
