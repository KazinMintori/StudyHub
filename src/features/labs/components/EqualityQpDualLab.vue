<script setup>
import { computed,ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger,makeView,fmt,fmtPoint } from '../controllers/svg-drag.js'
import { equalityQpExample,project3,lineParameter } from '../services/foundation-geometry.mjs'
const svg=ref(null),dualSvg=ref(null),t=ref(-.25),nu=ref([0,-1]),space=ref('weighted')
const closest=[.25,.75,1.25],direction=[1,-1,1],camera={yaw:35,pitch:30,scale:57,origin:[200,235]}
const display=p=>space.value==='weighted'?[p[0],Math.SQRT2*p[1],p[2]]:p
const P=p=>project3(display(p),camera),W=p=>project3(p,camera)
const at=t=>closest.map((v,i)=>v+t*direction[i])
const row=computed(()=>equalityQpExample(t.value,nu.value))
const dragView=computed(()=>({x0:-.8,x1:.8,y0:0,y1:0,toWorld:(x,y)=>[lineParameter([x,y],P(closest),P(at(1)))??t.value,0]}))
const drag=createDragger(svg,dragView,(_,p)=>{t.value=p[0]},{step:.025,snap:.005})
const dualView=ref(makeView({x0:-3,x1:1.5,y0:-3,y1:1.5,width:400,height:400,pad:30})),D=p=>dualView.value.point(p)
const dualDrag=createDragger(dualSvg,dualView,(_,p)=>{nu.value=p},{step:.05,snap:.01})
const circles=computed(()=>{
 const radius=Math.sqrt(2*row.value.value)
 return [0,1,2].map(axis=>Array.from({length:97},(_,i)=>{
  const angle=i*Math.PI/48,p=axis===0?[radius*Math.cos(angle),radius*Math.sin(angle),0]:axis===1?[radius*Math.cos(angle),0,radius*Math.sin(angle)]:[0,radius*Math.cos(angle),radius*Math.sin(angle)]
  return W(space.value==='weighted'?p:[p[0],p[1]/Math.SQRT2,p[2]]).join(',')
 }).join(' '))
})
const contours=[.125,.5,1].map(delta=>Array.from({length:97},(_,i)=>{
 const angle=i*Math.PI/48,u=Math.sqrt(delta)*Math.cos(angle),v=Math.sqrt(2*delta)*Math.sin(angle)
 return D([-.25+(u+v)/Math.SQRT2,-1.25+(u-v)/Math.SQRT2]).join(',')
}).join(' '))
const axes=[[2.8,0,0],[0,2.8,0],[0,0,2.8]]
</script>

<template>
 <figure class="study-lab" aria-label="QP có đẳng thức trong R³ và chứng nhận đối ngẫu hai nhân tử">
  <figcaption class="lab-title">Nghiệm khả thi cho cận trên, nhân tử cho cận dưới</figcaption>
  <p class="lab-lead">Kéo điểm trên đường nghiệm ở hình đầu. Kéo bộ nhân tử ν ở hình sau. Hai điểm được điều chỉnh độc lập, nên có thể thấy khoảng chứng nhận thu hẹp từ cả hai phía.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Đường nghiệm hai đẳng thức trong không gian ba chiều và nghiệm tối ưu" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <polyline v-for="(circle,i) in circles" :key="i" :points="circle" class="lab-guide"/>
    <g v-for="(axis,i) in axes" :key="i"><line :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(axis)[0]" :y2="P(axis)[1]" class="lab-axis"/><text :x="P(axis)[0]+7" :y="P(axis)[1]+7">{{space==='weighted'?'y':'x'}}{{i+1}}</text></g>
    <line :x1="P(at(-1.15))[0]" :y1="P(at(-1.15))[1]" :x2="P(at(1.15))[0]" :y2="P(at(1.15))[1]" class="lab-accent"/>
    <line :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(closest)[0]" :y2="P(closest)[1]" class="lab-good"/>
    <circle :cx="P(closest)[0]" :cy="P(closest)[1]" r="6" class="lab-dot-hollow"/><text :x="P(closest)[0]-31" :y="P(closest)[1]-14">{{space==='weighted'?'y*':'x*'}}</text>
    <circle :cx="P(row.point)[0]" :cy="P(row.point)[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="P(row.point)[0]" :cy="P(row.point)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Điểm x trên đường nghiệm của hai đẳng thức" :aria-valuetext="`t = ${fmt(t,3)}, x = ${fmtPoint(row.point,3)}`" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',[t,0],$event)"/>
    <text x="12" y="23">Miền khả thi trong R³</text>
   </svg>
   <svg ref="dualSvg" viewBox="0 0 400 400" role="group" aria-label="Hai nhân tử ν và các đường đồng mức của hàm đối ngẫu lõm" @pointermove="dualDrag.move" @pointerup="dualDrag.end" @pointercancel="dualDrag.end" @lostpointercapture="dualDrag.end">
    <line x1="30" x2="370" :y1="dualView.sy(0)" :y2="dualView.sy(0)" class="lab-axis"/><line :x1="dualView.sx(0)" :x2="dualView.sx(0)" y1="30" y2="370" class="lab-axis"/>
    <polyline v-for="(contour,i) in contours" :key="i" :points="contour" class="lab-guide"/>
    <circle :cx="D([-.25,-1.25])[0]" :cy="D([-.25,-1.25])[1]" r="6" class="lab-dot-hollow"/><text :x="D([-.25,-1.25])[0]-31" :y="D([-.25,-1.25])[1]-13">ν*</text>
    <circle :cx="D(nu)[0]" :cy="D(nu)[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="D(nu)[0]" :cy="D(nu)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Bộ nhân tử đẳng thức ν" :aria-valuetext="fmtPoint(nu,3)" @pointerdown="dualDrag.start('nu',$event)" @keydown="dualDrag.key('nu',nu,$event)"/>
    <text x="12" y="23">Không gian nhân tử R²</text><text x="343" :y="dualView.sy(0)+24">ν₁</text><text :x="dualView.sx(0)+12" y="48">ν₂</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="x"/><LabPointControls :svg="dualSvg"/></details>
  <div class="lab-controls"><label>Tọa độ của hình ba chiều<select v-model="space"><option value="weighted">y = (x₁, √2x₂, x₃): Mặt mức là cầu</option><option value="original">x: Mặt mức là ellipsoid</option></select></label></div>
  <div class="lab-buttons"><button type="button" @click="t=0">Đưa x về tối ưu</button><button type="button" @click="nu=[-.25,-1.25]">Đưa ν về tối ưu</button><button type="button" @click="t=-.25;nu=[0,-1]">Cặp chứng nhận ban đầu</button></div>
  <div class="lab-readout" role="status">
   <p>x = {{fmtPoint(row.point,3)}}. Hai sai số đẳng thức Ax − b = {{fmtPoint(row.residual,4)}}. Giá trị gốc f(x) = {{fmt(row.value,5)}}.</p>
   <p>ν = {{fmtPoint(nu,3)}} cho cận dưới g(ν) = {{fmt(row.dual,5)}}. Nghiệm tối ưu bị kẹp trong [{{fmt(row.dual,5)}}, {{fmt(row.value,5)}}], khoảng rộng {{fmt(row.gap,5)}}.</p>
   <p>Giá trị tối ưu chính xác là 11/8. Sai số thật của điểm x đang chọn là {{fmt(row.primalError,5)}}, không vượt quá độ rộng khoảng chứng nhận.</p>
   <p>Trong tọa độ y, mục tiêu bằng một nửa bình phương khoảng cách tới gốc. Đường nghiệm tiếp xúc mặt cầu nhỏ nhất tại y*. Trong tọa độ x, chi phí của x₂ nặng gấp đôi nên phải đọc mặt mức ellipsoid, không coi nghiệm là điểm có chuẩn Euclid nhỏ nhất của x.</p>
   <p>Các vòng nét đứt ở hình phải có mức g thấp dần khi rời ν*. Chúng không phải các ràng buộc của nhân tử. Mọi ν trong R² đều cho cận hữu hạn ở ví dụ này vì Hessian dương xác định.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Giữ x rồi cải thiện ν. Vì sao nghiệm khả thi không đổi nhưng khoảng chứng nhận hẹp hơn?</li><li>Giữ ν rồi đưa x về tối ưu. Cận dưới đã bằng cận trên chưa?</li><li>Đổi hai hệ tọa độ. Vì sao cùng một mức chi phí hiện thành cầu hoặc ellipsoid?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
