// Runs in the page, so SVG text measurements use the actual loaded browser font.
// It checks labels and unusually heavy strokes. Geometric intersections can be
// mathematically necessary; judging overall density still requires viewing PNGs.
export function inspectDiagramClarity(){
 const issues=[]
 const visible=e=>{const s=getComputedStyle(e);return s.display!=='none'&&s.visibility!=='hidden'&&Number(s.opacity)!==0}
 const intersects=(a,b)=>({w:Math.min(a.right,b.right)-Math.max(a.left,b.left),h:Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)})
 for(const [index,svg]of [...document.querySelectorAll('.study-lab > svg,.study-lab > .lab-pair > svg')].entries()){
  const frame=svg.getBoundingClientRect()
  if(!frame.width||!frame.height)continue
  const lab=svg.closest('figure').getAttribute('aria-label')
  const labels=[...svg.querySelectorAll('text')].filter(e=>e.textContent.trim()&&visible(e)).map(e=>({element:e,text:e.textContent,box:e.getBoundingClientRect()}))
  for(let i=0;i<labels.length;i++)for(let j=i+1;j<labels.length;j++){
   const a=labels[i],b=labels[j],overlap=intersects(a.box,b.box)
   if(overlap.w>1.5&&overlap.h>1.5)issues.push({type:'diagram-label-overlap',lab,diagram:index,labels:[a.text,b.text],overlap})
  }
  for(const label of labels){
   const size=parseFloat(getComputedStyle(label.element).fontSize),matrix=label.element.getScreenCTM()
   const scale=matrix?Math.hypot(matrix.c,matrix.d):1
   if(size*scale<10)issues.push({type:'diagram-small-label',lab,diagram:index,text:label.text,pixels:size*scale})
  }
  for(const element of svg.querySelectorAll('line,path,polyline,polygon')){
   if(element.closest('.lab-handle')||!visible(element))continue
   const style=getComputedStyle(element)
   if(style.stroke==='none'||style.stroke==='transparent'||/rgba\([^)]*,\s*0\)/.test(style.stroke)||Number(style.strokeOpacity)===0)continue
   const matrix=element.getScreenCTM(),scale=matrix?Math.max(Math.hypot(matrix.a,matrix.b),Math.hypot(matrix.c,matrix.d)):1
   const pixels=parseFloat(style.strokeWidth)*scale
   if(pixels/Math.min(frame.width,frame.height)>.018)issues.push({type:'diagram-heavy-stroke',lab,diagram:index,tag:element.tagName,pixels})
  }
 }
 return issues
}
