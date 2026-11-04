export const columnNames=['x','y','s₁','s₂']
export const basisPairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
const columns=[[1,1],[1,0],[1,0],[0,1]]

export function basisSolution(pair,capacity){
  const [i,j]=pair
  const [a,c]=columns[i]
  const [b,d]=columns[j]
  const determinant=a*d-b*c
  if(determinant===0)return {kind:'singular'}
  const x=[0,0,0,0]
  x[i]=(d*capacity-b*2)/determinant
  x[j]=(a*2-c*capacity)/determinant
  if(x[i]<0||x[j]<0)return {kind:'infeasible',x}
  return {kind:x[i]===0||x[j]===0?'degenerate':'feasible',x}
}

export function resourceVertices(capacity){
  const right=Math.min(2,capacity)
  return [[0,0],[right,0],[right,capacity-right],[0,capacity]]
}
