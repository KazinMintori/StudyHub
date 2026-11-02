// Clip display geometry without changing the numerical function values.
export function clipSegment([p,q],{x0,x1,y0,y1}){
 if(![...p,...q,x0,x1,y0,y1].every(Number.isFinite))return null
 let lower=0,upper=1
 for(const [start,delta,min,max]of [[p[0],q[0]-p[0],x0,x1],[p[1],q[1]-p[1],y0,y1]]){
  if(Math.abs(delta)<1e-12){if(start<min||start>max)return null;continue}
  const a=(min-start)/delta,b=(max-start)/delta
  lower=Math.max(lower,Math.min(a,b));upper=Math.min(upper,Math.max(a,b))
  if(lower>upper)return null
 }
 return [lower,upper].map(t=>p.map((value,i)=>value+t*(q[i]-value)))
}

export function clipPolyline(points,box){
 const output=[]
 for(let i=1;i<points.length;i++){
  const segment=clipSegment([points[i-1],points[i]],box)
  if(!segment)continue
  const previous=output.at(-1),end=previous?.at(-1)
  if(end&&Math.hypot(end[0]-segment[0][0],end[1]-segment[0][1])<1e-8)previous.push(segment[1])
  else output.push(segment)
 }
 return output
}
