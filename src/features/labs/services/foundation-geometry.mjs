// Small, explicit models for the introductory lecture. Coordinates are mathematical,
// not screen coordinates; orthographic projection is kept separate from conclusions.
export const dot = (a, b) => a.reduce((s, v, i) => s + v * b[i], 0)
export const matvec = (a, x) => a.map(row => dot(row, x))
export const norm2 = x => Math.sqrt(dot(x, x))
// Orthogonal projection onto a line a + t(b-a). Null means the line is undefined.
export function lineParameter(point, a, b) {
  const direction = b.map((v, i) => v - a[i]), denominator = dot(direction, direction)
  return denominator < 1e-18 ? null : dot(point.map((v, i) => v - a[i]), direction) / denominator
}
export function planeParameters(point, origin, first, second) {
  const a = first.map((v,i)=>v-origin[i]), b=second.map((v,i)=>v-origin[i]), p=point.map((v,i)=>v-origin[i])
  const determinant=a[0]*b[1]-a[1]*b[0]
  if (Math.abs(determinant)<1e-10) return null
  return [(p[0]*b[1]-p[1]*b[0])/determinant,(a[0]*p[1]-a[1]*p[0])/determinant]
}
export const rotate2 = ([x, y], angle) => [x * Math.cos(angle) - y * Math.sin(angle), x * Math.sin(angle) + y * Math.cos(angle)]

export const cross3 = (a,b) => [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
export function pNorm3(point,p=2) {
  return p===Infinity?Math.max(...point.map(Math.abs)):point.reduce((s,v)=>s+Math.abs(v)**p,0)**(1/p)
}
export function ellipsoidGauge(point,radii,angle=0) {
  const local=[...rotate2(point.slice(0,2),-angle),point[2]]
  if(local.some((v,i)=>radii[i]===0&&Math.abs(v)>1e-8))return Infinity
  return Math.sqrt(local.reduce((s,v,i)=>s+(radii[i]===0?0:(v/radii[i])**2),0))
}
// For p(t)=a*cos(t)+b*cos(2t), |t|<=pi/3. With u=cos(t),
// p=2bu²+au-b on [1/2,1]. The absolute maximum is attained
// at an endpoint or the quadratic's stationary point, not a sample grid.
export function trigonometricSlabWorst([a,b]) {
  const candidates=[.5,1]
  if(Math.abs(b)>1e-14){const u=-a/(4*b);if(u>=.5&&u<=1)candidates.push(u)}
  const rows=candidates.map(u=>({t:Math.acos(u),value:2*b*u*u+a*u-b}))
  return rows.reduce((best,row)=>Math.abs(row.value)>Math.abs(best.value)?row:best)
}
export function lineFitSpace(a,c) {
  const target=[1,2,4],prediction=[c,a+c,2*a+c]
  const residual=prediction.map((v,i)=>v-target[i])
  return {target,prediction,residual,value:dot(residual,residual),normalResidual:[residual[1]+2*residual[2],residual.reduce((s,v)=>s+v,0)]}
}
export function boxWorstCase(weights, center, epsilon) {
  const perturbation=weights.map(v=>-epsilon*Math.sign(v))
  const point=center.map((v,i)=>v+perturbation[i])
  return {perturbation,point,margin:dot(weights,point),penalty:epsilon*weights.reduce((s,v)=>s+Math.abs(v),0)}
}
// Fixed two-resource example: a=(5,5)+diag(3,4)u, ||u||<=1.
export function ellipsoidResource(point) {
  const z=[3*point[0],4*point[1]],radius=Math.hypot(...z)
  const nominal=5*(point[0]+point[1]),t=37-nominal
  const u=radius>1e-12?z.map(v=>v/radius):[0,0]
  return {z,radius,nominal,t,u,coefficient:[5+3*u[0],5+4*u[1]],worst:nominal+radius,eigenvalues:[t-radius,t,t+radius]}
}
// Numerical normal CDF for the probability readout. Mathematical statements in
// the lesson use Phi itself; this approximation only draws/evaluates the lab.
export function standardNormalCdf(z) {
  if(z===Infinity)return 1
  if(z===-Infinity)return 0
  if(z===0)return .5
  const x=Math.abs(z),t=1/(1+.2316419*x)
  const polynomial=t*(.319381530+t*(-.356563782+t*(1.781477937+t*(-1.821255978+t*1.330274429))))
  const tail=Math.exp(-x*x/2)/Math.sqrt(2*Math.PI)*polynomial
  return z<0?tail:1-tail
}
export function ridgeScalar(w) {
  return {w,f1:5*(w-2)**2,f2:w*w,gamma:w===0?Infinity:5*(2-w)/w}
}
export function minimaxRatio(s) {
  const first=(2*s+1)/(s+2),second=(3-2*s)/(s+1)
  return {first,second,value:Math.max(first,second)}
}
export function minimaxRatioLevel(tau) {
  if(tau<.5||tau>1.5)throw new RangeError('The displayed level interval is [0.5, 1.5]')
  const lower=Math.max(0,(3-tau)/(2+tau)),upper=Math.min(1,(2*tau-1)/(2-tau))
  return {lower,upper,feasible:lower<=upper+1e-12}
}
export function geometricProgramOptimum(n,a) {
  if(!Number.isInteger(n)||n<2||!Number.isFinite(a)||a<=0)throw new RangeError('Need n >= 2 and a positive finite bound')
  const weights=Array.from({length:n},(_,i)=>2**i),threshold=2**((n-1)/2)
  const first=Math.max(a,threshold),common=2**(n/2)*first**(-1/(n-1))
  const point=[first,...weights.slice(1).map(c=>common/c)]
  return {weights,threshold,point,value:dot(weights,point),product:point.reduce((p,v)=>p*v,1),active:a>=threshold-1e-10}
}
export function equalityQpExample(t,nu) {
  const closest=[.25,.75,1.25],direction=[1,-1,1]
  const point=closest.map((v,i)=>v+t*direction[i]),weighted=[point[0],Math.SQRT2*point[1],point[2]]
  const value=dot(weighted,weighted)/2
  const dual=-.5*(1.5*nu[0]**2+nu[0]*nu[1]+1.5*nu[1]**2)-nu[0]-2*nu[1]
  return {point,weighted,value,dual,gap:value-dual,primalError:value-11/8,residual:[point[0]+point[1]-1,point[1]+point[2]-2]}
}
export function resourceSensitivity(budget) {
  if(!Number.isFinite(budget)||budget<=0)throw new RangeError('Budget must be positive')
  let point,lambda,mu
  if(budget<=1){point=[budget,0];lambda=2-budget;mu=[0,1-budget]}
  else if(budget<=3){point=[(budget+1)/2,(budget-1)/2];lambda=(3-budget)/2;mu=[0,0]}
  else{point=[2,1];lambda=0;mu=[0,0]}
  const value=((point[0]-2)**2+(point[1]-1)**2)/2
  return {point,lambda,mu,value,slack:budget-point[0]-point[1]}
}
export function chebyshevCertificate(parameters,t) {
  const prediction=[0,1,2].map(x=>parameters[0]+parameters[1]*x)
  const residual=prediction.map((v,i)=>v-[0,0,2][i]),nu=[t,-2*t,t]
  const norm=nu.reduce((s,v)=>s+Math.abs(v),0),value=Math.max(...residual.map(Math.abs))
  return {prediction,residual,nu,norm,value,dual:2*t,gap:value-2*t}
}
export function entropyMoment(primalThird,eta) {
  const point=[primalThird-3/7,10/7-2*primalThird,primalThird]
  const value=point.reduce((s,p)=>s+p*Math.log(p),0)
  const exponents=[0,-eta,-2*eta],shift=Math.max(...exponents)
  const shifted=exponents.map(v=>Math.exp(v-shift)),sum=shifted.reduce((a,b)=>a+b,0)
  const logZ=shift+Math.log(sum),induced=shifted.map(v=>v/sum)
  const tau=logZ-1,dual=-logZ-eta*10/7
  return {point,value,eta,tau,induced,mean:induced[1]+2*induced[2],dual,gap:value-dual}
}
export function cappedWaterChannel(alpha,weight,cap,nu) {
  const lower=weight/(alpha+cap),upper=weight/alpha
  const x=nu<=lower?cap:nu>=upper?0:weight/nu-alpha
  return {x,value:-weight*Math.log(alpha+x)+nu*x}
}
export function weightedCappedWaterfill(budget) {
  if(!Number.isFinite(budget)||budget<=0||budget>=4)throw new RangeError('Need 0 < budget < 4')
  let point,nu
  if(budget<1){point=[budget,0,0];nu=[2/(1+budget),2/(1+budget)]}
  else if(budget===1){point=[1,0,0];nu=[.5,1]}
  else if(budget<1.5){point=[1,budget-1,0];nu=[1/(budget+1),1/(budget+1)]}
  else if(budget<=3){point=[1,budget/3,2*budget/3-1];nu=[3/(budget+6),3/(budget+6)]}
  else{point=[1,budget-2,1];nu=[1/budget,1/budget]}
  const value=-[2,1,2].reduce((sum,w,i)=>sum+w*Math.log([1,2,5][i]+point[i]),0)
  return {point,nu,value}
}
export function weightedWaterDual(budget,nu) {
  const alpha=[1,2,5],weights=[2,1,2],caps=[1,2,1]
  const rows=alpha.map((a,i)=>cappedWaterChannel(a,weights[i],caps[i],nu))
  return {point:rows.map(r=>r.x),value:rows.reduce((s,r)=>s+r.value,0)-nu*budget,total:rows.reduce((s,r)=>s+r.x,0)}
}
export function cycleFiveModel(signs,angles) {
  const cuts=signs.reduce((s,v,i)=>s+(v!==signs[(i+1)%5]?1:0),0)
  const vectors=angles.map(angle=>[Math.cos(angle),Math.sin(angle)])
  const gram=vectors.map(a=>vectors.map(b=>dot(a,b)))
  const relaxed=2*signs.reduce((sum,_,i)=>sum+gram[i][(i+1)%5],0)
  const nu=signs.map((v,i)=>-v*(signs[(i+4)%5]+signs[(i+1)%5]))
  const rank=vectors.some(v=>Math.abs(vectors[0][0]*v[1]-vectors[0][1]*v[0])>1e-8)?2:1
  const phi=(1+Math.sqrt(5))/2,dual=-5*phi
  return {cuts,integerValue:10-4*cuts,vectors,gram,relaxed,nu,rank,dual,relaxedCut:(10-relaxed)/4,cutUpper:(10-dual)/4}
}
export function perronCertificate(t,r) {
  if(!Number.isFinite(t)||!Number.isFinite(r)||t<=0||r<=0)throw new RangeError('Positive finite design and certificate ratio required')
  const matrix=[[t/4,.25],[.25,1/(4*t)]],vector=[r,1]
  const image=matvec(matrix,vector),ratios=image.map((v,i)=>v/vector[i])
  const radius=(t+1/t)/4,upper=Math.max(...ratios)
  return {matrix,vector,image,ratios,radius,upper,gap:upper-radius}
}
export function projectToHyperplane(point, normal, offset) {
  const length=norm2(normal)
  if(length<1e-12) throw new RangeError('A hyperplane needs a nonzero normal')
  const signed=(dot(normal,point)-offset)/length
  return { signed, foot:point.map((v,i)=>v-signed*normal[i]/length) }
}
// Intersection of a plane with a finite drawing box. The box is a viewport,
// never an extra constraint of the mathematical halfspace.
export function planeBoxSection(normal, offset, size=2.5) {
  const vertices=Array.from({length:8},(_,i)=>[0,1,2].map(j=>(i&(1<<j))?size:-size))
  const points=[]
  const add=p=>{if(!points.some(q=>norm2(p.map((v,i)=>v-q[i]))<1e-8)) points.push(p)}
  for(let i=0;i<8;i++) for(let bit=0;bit<3;bit++) {
    const j=i^(1<<bit)
    if(i>j) continue
    const a=vertices[i],b=vertices[j],fa=dot(normal,a)-offset,fb=dot(normal,b)-offset
    if(Math.abs(fa)<1e-10) add(a)
    if(Math.abs(fb)<1e-10) add(b)
    if(fa*fb<0) add(a.map((v,k)=>v+(b[k]-v)*fa/(fa-fb)))
  }
  if(points.length<3) return points
  const center=[0,1,2].map(i=>points.reduce((s,p)=>s+p[i],0)/points.length)
  const n=normal.map(v=>v/norm2(normal)),seed=Math.abs(n[0])<.9?[1,0,0]:[0,1,0]
  const u0=cross3(n,seed),u=u0.map(v=>v/norm2(u0)),v=cross3(n,u)
  return points.sort((a,b)=>{
    const d=p=>p.map((c,i)=>c-center[i])
    return Math.atan2(dot(d(a),v),dot(d(a),u))-Math.atan2(dot(d(b),v),dot(d(b),u))
  })
}

export function project3([x, y, z], { yaw = 35, pitch = 28, scale = 54, origin = [200, 230] } = {}) {
  const a = yaw * Math.PI / 180, b = pitch * Math.PI / 180
  const u = x * Math.cos(a) - y * Math.sin(a), v = x * Math.sin(a) + y * Math.cos(a)
  return [origin[0] + scale * u, origin[1] - scale * (z * Math.cos(b) - v * Math.sin(b))]
}

// Inverse restricted to a specified horizontal plane. A screen point alone never
// determines a unique point in R³. Keep pitch away from 0 so this inverse is defined.
export function unprojectPlane([sx, sy], z, { yaw = 35, pitch = 28, scale = 54, origin = [200, 230] } = {}) {
  const a = yaw * Math.PI / 180, b = pitch * Math.PI / 180
  const u = (sx - origin[0]) / scale, h = (origin[1] - sy) / scale
  const v = (z * Math.cos(b) - h) / Math.sin(b)
  return [u * Math.cos(a) + v * Math.sin(a), -u * Math.sin(a) + v * Math.cos(a)]
}

export function svdStages(x, s = [1.6, 0.7], left = Math.PI / 6, right = -Math.PI / 6) {
  const v = rotate2(x, right), stretched = v.map((c, i) => c * s[i])
  return [[...x], v, stretched, rotate2(stretched, left)]
}

export function leastNormExample(dimension = 3, t = 0) {
  const a = dimension === 2 ? [[1, 2]] : [[1, 1, 0], [0, 1, 1]]
  const b = dimension === 2 ? [2] : [2, 4]
  const closest = dimension === 2 ? [0.4, 0.8] : [0, 2, 2]
  const kernel = dimension === 2 ? [2, -1] : [1, -1, 1]
  const x = closest.map((v, i) => v + t * kernel[i])
  return { a, b, closest, kernel, x, residual: matvec(a, x).map((v, i) => v - b[i]), squared: dot(x, x), minimum: dot(closest, closest), extra: t * t * dot(kernel, kernel) }
}

export function curvatureModel(kind, parameter = 1) {
  if (kind === 'schur') return { value: ([x, y]) => x * x + 2 * x * y + parameter * y * y, gradient: ([x, y]) => [2 * (x + y), 2 * (x + parameter * y)], hessian: [2, 2, 2 * parameter] }
  return { value: ([x, y]) => (x * x + parameter * y * y) / 2, gradient: ([x, y]) => [x, parameter * y], hessian: [1, 0, parameter] }
}
