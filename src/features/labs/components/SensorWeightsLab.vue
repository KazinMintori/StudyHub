<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3,planeParameters} from '../services/foundation-geometry.mjs'
import {clipPolyline} from '../services/svg-clipping.mjs'
import {insideConvexPolygon,closestOnSegment} from '../services/convex-geometry.mjs'

const flatSvg=ref(null),planeSvg=ref(null),z=ref([.25,.25]),nonnegative=ref(false),noisy=ref(false)
const variances=computed(()=>[1,2,noisy.value?1000:3])
const base=[1,0,0],first=[-1,1,0],second=[-1,0,1]
const at=p=>[1-p[0]-p[1],p[0],p[1]]
const weights=computed(()=>at(z.value))
const variance=w=>w.reduce((sum,value,i)=>sum+variances.value[i]*value*value,0)
const value=computed(()=>variance(weights.value))
const optimum=computed(()=>{const inverse=variances.value.map(value=>1/value),sum=inverse.reduce((a,b)=>a+b,0);return inverse.map(value=>value/sum)})
const minimum=computed(()=>variance(optimum.value))
const camera={yaw:22,pitch:33,scale:104,origin:[170,234]}
const P=w=>project3(w,camera)
const flat=makeView({x0:-.2,x1:1.05,y0:-.2,y1:1.05,width:360,height:330,pad:34})
const flatView=computed(()=>flat)
const triangle=[[0,0],[1,0],[0,1]]
const planeView=computed(()=>({x0:-.2,x1:1.05,y0:-.2,y1:1.05,toWorld:(x,y)=>planeParameters([x,y],P(base),P([0,1,0]),P([0,0,1]))||z.value}))
function move(_,point){
 if(nonnegative.value&&!insideConvexPolygon(point,triangle)){
  const candidates=triangle.map((a,i)=>closestOnSegment(point,a,triangle[(i+1)%3]).point)
  candidates.sort((a,b)=>Math.hypot(a[0]-point[0],a[1]-point[1])-Math.hypot(b[0]-point[0],b[1]-point[1]))
  point=candidates[0]
 }
 z.value=point
}
const flatDrag=createDragger(flatSvg,flatView,move,{step:.025})
const planeDrag=createDragger(planeSvg,planeView,move,{step:.025})
const poly=points=>points.map(p=>p.join(',')).join(' ')
const contourLevels=[.02,.08,.2,.5]
const contours=computed(()=>{
 const [v1,v2,v3]=variances.value,l00=Math.sqrt(v1+v2),l10=v1/l00,l11=Math.sqrt(v1+v3-l10*l10)
 return contourLevels.map(level=>{
  const points=Array.from({length:161},(_,i)=>{
   const angle=i*Math.PI/80,q1=Math.sqrt(level)*Math.cos(angle),q2=Math.sqrt(level)*Math.sin(angle),d2=q2/l11,d1=(q1-l10*d2)/l00
   return [optimum.value[1]+d1,optimum.value[2]+d2]
  })
  return clipPolyline(points,{x0:-.2,x1:1.05,y0:-.2,y1:1.05})
 })
})
const planeCorners=[[-.2,-.2],[1.05,-.2],[1.05,1.05],[-.2,1.05]]
function restrict(){nonnegative.value=!nonnegative.value;move('z',z.value)}
function putOptimum(){z.value=optimum.value.slice(1)}
</script>

<template>
 <figure class="study-lab" aria-label="Ba trọng số cảm biến trên mặt phẳng tổng bằng một và tọa độ sau khử biến">
  <figcaption class="lab-title">Ba trọng số, hai hướng tự do và một nghiệm phương sai nhỏ nhất</figcaption>
  <p class="lab-lead">Kéo điểm tím trên mặt phẳng hoặc trên hình tọa độ z. Hai hình mô tả cùng một bộ trọng số. Ta đã khử x₁ bằng công thức x₁ = 1 − z₁ − z₂, với z₁ = x₂ và z₂ = x₃.</p>
  <div class="lab-buttons" role="group" aria-label="Dữ liệu và điều kiện của ba cảm biến">
   <button type="button" @click="noisy=false">Phương sai (1, 2, 3)</button>
   <button type="button" @click="noisy=true">Cảm biến thứ ba nhiễu lớn</button>
   <button type="button" @click="putOptimum">Trọng số tối ưu</button>
   <button type="button" @click="z=[1/3,1/3]">Chia đều ba trọng số</button>
   <button type="button" @click="nonnegative=false;z=[.8,.4]">Ví dụ có trọng số âm</button>
   <button type="button" :aria-pressed="nonnegative" @click="restrict">Thêm điều kiện trọng số không âm</button>
  </div>
  <div class="lab-pair">
   <svg ref="planeSvg" viewBox="0 0 360 330" role="group" aria-label="Mặt phẳng x1 cộng x2 cộng x3 bằng một, điểm trọng số và tam giác không âm" @pointermove="planeDrag.move" @pointerup="planeDrag.end" @pointercancel="planeDrag.end" @lostpointercapture="planeDrag.end">
    <polygon :points="poly(planeCorners.map(p=>P(at(p))))" class="plane"/>
    <line v-for="(axis,index) in [[1.35,0,0],[0,1.35,0],[0,0,1.35]]" :key="index" :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(axis)[0]" :y2="P(axis)[1]" class="lab-axis"/>
    <polygon :points="poly(triangle.map(p=>P(at(p))))" :class="nonnegative?'simplex-active':'simplex'"/>
    <g v-for="(segments,index) in contours" :key="index"><polyline v-for="(points,j) in segments" :key="j" :points="poly(points.map(p=>P(at(p))))" class="contour"/></g>
    <circle :cx="P(optimum)[0]" :cy="P(optimum)[1]" r="5" class="lab-dot-warn"/>
    <circle :cx="P(weights)[0]" :cy="P(weights)[1]" r="7" class="lab-dot-accent"/>
    <circle :cx="P(weights)[0]" :cy="P(weights)[1]" r="27" class="lab-handle hit" role="slider" tabindex="0" aria-label="Trọng số trên mặt phẳng trong R³" :aria-valuetext="fmtPoint(weights,4)" @pointerdown="planeDrag.start('z',$event)" @keydown="planeDrag.key('z',z,$event)"/>
    <text :x="P([1.35,0,0])[0]+9" :y="P([1.35,0,0])[1]+14">x₁</text>
    <text :x="P([0,1.35,0])[0]-26" :y="P([0,1.35,0])[1]+18">x₂</text>
    <text :x="P([0,0,1.35])[0]+9" :y="P([0,0,1.35])[1]">x₃</text>
   </svg>
   <svg ref="flatSvg" viewBox="0 0 360 330" role="group" aria-label="Tọa độ tự do z1 và z2, các đường mức phương sai và điểm kéo được" @pointermove="flatDrag.move" @pointerup="flatDrag.end" @pointercancel="flatDrag.end" @lostpointercapture="flatDrag.end">
    <polygon :points="poly(triangle.map(p=>flat.point(p)))" :class="nonnegative?'simplex-active':'simplex'"/>
    <line x1="28" :y1="flat.sy(0)" x2="330" :y2="flat.sy(0)" class="lab-axis"/>
    <line :x1="flat.sx(0)" y1="28" :x2="flat.sx(0)" y2="304" class="lab-axis"/>
    <g v-for="(segments,index) in contours" :key="index"><polyline v-for="(points,j) in segments" :key="j" :points="poly(points.map(flat.point))" class="contour"/></g>
    <circle :cx="flat.sx(optimum[1])" :cy="flat.sy(optimum[2])" r="5" class="lab-dot-warn"/>
    <circle :cx="flat.sx(z[0])" :cy="flat.sy(z[1])" r="7" class="lab-dot-accent"/>
    <circle :cx="flat.sx(z[0])" :cy="flat.sy(z[1])" r="27" class="lab-handle hit" role="slider" tabindex="0" aria-label="Hai tọa độ tự do z1 và z2" :aria-valuetext="fmtPoint(z,4)" @pointerdown="flatDrag.start('z',$event)" @keydown="flatDrag.key('z',z,$event)"/>
    <text x="331" :y="flat.sy(0)+24">z₁</text><text :x="flat.sx(0)+10" y="27">z₂</text>
    <text :x="flat.sx(1)-8" :y="flat.sy(0)+24">1</text><text :x="flat.sx(0)-10" :y="flat.sy(1)+5" text-anchor="end">1</text>
   </svg>
  </div>
  <p class="lab-legend"><span class="legend-accent">Trọng số đang chọn</span><span class="legend-warn">Trọng số tối ưu</span><span class="legend-good">Tam giác trọng số không âm</span><span class="legend-guide">Các đường mức phương sai</span></p>
  <details class="lab-tasks"><summary>Điều chỉnh hai tọa độ bằng nút</summary><LabPointControls :svg="planeSvg"/><LabPointControls :svg="flatSvg"/></details>
  <div class="lab-readout" role="status">
   <p>Phương sai ba cảm biến là {{variances.join(', ')}}. Trọng số x = {{fmtPoint(weights,4)}}, với tổng {{fmt(weights.reduce((a,b)=>a+b,0),6)}}.</p>
   <p>Phương sai tổng hợp = {{fmt(value,6)}}. Giá trị nhỏ nhất = {{fmt(minimum,6)}}, tại x* = {{fmtPoint(optimum,6)}}.</p>
   <p>z = {{fmtPoint(z,4)}}. Đường mức được vẽ tại các giá trị lớn hơn mức tối ưu lần lượt {{contourLevels.join(', ')}}.</p>
   <p>{{nonnegative?'Điểm bị giữ trong tam giác không âm.':'Điểm được phép ra ngoài tam giác, khi đó có thể có trọng số âm.'}} Điều kiện tổng bằng 1 luôn được giữ. Nghiệm tối ưu của mô hình độc lập, phương sai dương này tự có mọi trọng số dương, nên thêm điều kiện không âm không đổi nghiệm.</p>
   <p>Hình trái là một phần mặt phẳng trong không gian trọng số R³. Hình phải dùng hai tọa độ tự do và không có thêm ràng buộc đẳng thức. Phép chiếu 3D không bảo toàn góc, độ dài hoặc hình dạng đường mức.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Bấm trọng số tối ưu, rồi thêm điều kiện không âm. Vì sao nghiệm giữ nguyên?</li><li>Cho cảm biến thứ ba có phương sai 1000. Vì sao trọng số thứ ba nhỏ nhưng vẫn dương?</li><li>Kéo điểm ra ngoài tam giác khi chưa đặt điều kiện không âm. Tổng trọng số có đổi không?</li></ol></details>
 </figure>
</template>

<style scoped>
svg text{font-size:18px}
.plane{fill:var(--tim-soft);stroke:var(--rule);stroke-width:1}
.simplex{fill:none;stroke:var(--xanh);stroke-width:1.4;stroke-dasharray:5 4}
.simplex-active{fill:var(--xanh-soft);stroke:var(--xanh);stroke-width:1.4}
.contour{fill:none;stroke:var(--ink-2);stroke-width:1.1;opacity:.65}
svg :is(line,polyline,polygon,path,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
