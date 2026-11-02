// The feasibility oracle uses only the trial level and the displayed box.
// It never reads the analytic optimum or a precomputed threshold.
export function ratioBox(dimension=2){
 if(dimension!==2&&dimension!==3)throw new RangeError('Expected dimension 2 or 3')
 return dimension===2?[[-1,1.5],[1,3]]:[[-1,1.5],[1,3],[-1,1]]
}

export function distanceRatio(point){
 if(!Array.isArray(point)||![2,3].includes(point.length)||!point.every(Number.isFinite))throw new RangeError('Expected a finite point in R2 or R3')
 const numerator=point.reduce((sum,value)=>sum+value*value,0)
 const denominator=(point[0]-4)**2+point.slice(1).reduce((sum,value)=>sum+value*value,0)
 return denominator===0?Infinity:Math.sqrt(numerator/denominator)
}

export function apolloniusBoxLevel(level,dimension=2){
 if(!Number.isFinite(level)||level<0||level>1)throw new RangeError('Expected 0 <= level <= 1')
 const bounds=ratioBox(dimension)
 if(level===1){
  const candidate=bounds.map(([lo,hi])=>Math.max(lo,Math.min(hi,0)))
  return {level,bounds,center:null,radius:null,candidate,ratio:distanceRatio(candidate),residual:8*candidate[0]-16,status:'feasible',tolerance:0,kind:'halfspace'}
 }
 const factor=1-level*level
 const center=Array.from({length:dimension},(_,i)=>i===0?-4*level*level/factor:0)
 const radius=4*level/factor
 const candidate=center.map((value,i)=>Math.max(bounds[i][0],Math.min(bounds[i][1],value)))
 const squaredA=candidate.reduce((sum,value)=>sum+value*value,0)
 const squaredB=(candidate[0]-4)**2+candidate.slice(1).reduce((sum,value)=>sum+value*value,0)
 const residual=squaredA-level*level*squaredB
 const tolerance=1e-10*(1+squaredA+level*level*squaredB)
 const status=residual < -tolerance?'feasible':residual > tolerance?'infeasible':'boundary'
 return {level,bounds,center,radius,candidate,ratio:distanceRatio(candidate),residual,status,tolerance,kind:'ball'}
}
