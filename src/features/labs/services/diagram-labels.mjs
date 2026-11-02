// Choose a short nearby label position without crowding the other annotations.
// Conservative text boxes are used here; browser QA measures the real glyphs.
export function placePointLabels(specifications,{width,height,reserved=[]}){
 const occupied=[...reserved],result={}
 const offsets=[[16,-16],[16,30],[-16,-16],[-16,30],[28,8],[-28,8],[0,-36],[0,44]]
 const overlap=(a,b)=>Math.max(0,Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x))*Math.max(0,Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y))
 for(const specification of specifications){
  const labelWidth=specification.width||Math.max(24,specification.text.length*13),labelHeight=26
  let best
  for(const [index,[dx,dy]]of offsets.entries()){
   const anchor=dx<0?'end':'start'
   let x=specification.point[0]+dx,y=specification.point[1]+dy
   x=Math.max(anchor==='end'?labelWidth+10:10,Math.min(anchor==='end'?width-10:width-labelWidth-10,x))
   y=Math.max(labelHeight+10,Math.min(height-12,y))
   const box={x:x-(anchor==='end'?labelWidth:0)-3,y:y-labelHeight,width:labelWidth+6,height:labelHeight+4}
   const area=occupied.reduce((sum,other)=>sum+overlap(box,other),0)
   const cost=area*1000+(x-specification.point[0])**2+(y-specification.point[1])**2+index*.01
   if(!best||cost<best.cost)best={x,y,anchor,box,cost}
  }
  result[specification.key]=best
  occupied.push(best.box)
 }
 return result
}
