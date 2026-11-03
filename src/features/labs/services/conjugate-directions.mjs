const dot=(a,b)=>a.reduce((sum,x,i)=>sum+x*b[i],0)
const addScaled=(a,b,scale)=>a.map((x,i)=>x+scale*b[i])

// The teaching examples use symmetric positive definite matrices.
export function quadraticTrace(matrix,b,start,method='cg',steps=b.length){
  const multiply=x=>matrix.map(row=>dot(row,x))
  const value=x=>dot(x,multiply(x))/2-dot(b,x)
  let x=[...start]
  let residual=addScaled(b,multiply(x),-1)
  let direction=residual
  const trace=[{x,residual,value:value(x),directions:[]}]
  const threshold=1e-12*Math.max(1,Math.hypot(...b))
  const directions=[]
  for(let k=0;k<steps;k++){
    const normSquared=dot(residual,residual)
    if(Math.sqrt(normSquared)<=threshold)break
    const product=multiply(direction)
    const alpha=dot(residual,direction)/dot(direction,product)
    x=addScaled(x,direction,alpha)
    const nextResidual=addScaled(residual,product,-alpha)
    const beta=dot(nextResidual,nextResidual)/normSquared
    const conjugacy=directions.map(previous=>dot(previous,product))
    directions.push(direction)
    trace.push({x,residual:nextResidual,value:value(x),directions:[...directions],alpha,beta,conjugacy})
    direction=method==='cg'?addScaled(nextResidual,direction,beta):nextResidual
    residual=nextResidual
  }
  return trace
}
