<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3} from '../services/foundation-geometry.mjs'
import {fractionalVertices as vertices,fractionalValue,cooperTransform,cooperFromScreen,projectToPolygon} from '../services/fractional-geometry.mjs'

const flatSvg=ref(null),spaceSvg=ref(null),point=ref([2,2]),yaw=ref(32)
const flat=makeView({x0:0,x1:7,y0:-.5,y1:5.5,width:360,height:300,pad:30})
const flatView=computed(()=>flat)
const camera=computed(()=>({yaw:yaw.value,pitch:32,scale:170,origin:[yaw.value===50?190:170,184]}))
const P=p=>project3(p,camera.value),image=computed(()=>cooperTransform(point.value))
const spaceView=computed(()=>({x0:1,x1:6,y0:0,y1:4,toWorld:(x,y)=>cooperFromScreen([x,y],P)}))
const move=(_,p)=>{point.value=projectToPolygon(p)}
const flatDrag=createDragger(flatSvg,flatView,move,{step:.05})
const spaceDrag=createDragger(spaceSvg,spaceView,move,{step:.05})
const plane=[[0,0,1],[1,0,0],[.425,1.15,0],[0,1.15,.425]]
const residuals=computed(()=>{const [a,b,z]=image.value;return [-a+z,-b,a+b-6*z,b-4*z]})
const result=computed(()=>image.value[0]+2*image.value[1]+2*image.value[2])
</script>
<template>
 <figure class="study-lab" aria-label="Phép đổi biến Charnes–Cooper từ hai biến sang ba biến">
  <figcaption class="lab-title">Cùng một điểm, hai hệ biến: x trong R² và (y₁, y₂, z) trong R³</figcaption>
  <p class="lab-lead">Kéo chấm tím trên một trong hai hình. Điểm ở hình kia tự cập nhật. Tứ giác sau phép đổi biến nằm trên mặt phẳng y₁ + 0.5y₂ + z = 1, không phải một khối có thể tích.</p>
  <div class="cooper-pair">
   <div><p class="panel-title">Miền x ban đầu</p>
    <svg ref="flatSvg" viewBox="0 0 360 300" role="group" aria-label="Điểm x kéo được trong tứ giác hai chiều" @pointermove="flatDrag.move" @pointerup="flatDrag.end" @pointercancel="flatDrag.end" @lostpointercapture="flatDrag.end">
     <line x1="25" :y1="flat.sy(0)" x2="330" :y2="flat.sy(0)" class="lab-axis"/>
     <line :x1="flat.sx(0)" y1="24" :x2="flat.sx(0)" y2="270" class="lab-axis"/>
     <text x="332" :y="flat.sy(0)+25">x₁</text><text :x="flat.sx(0)+10" y="23">x₂</text>
     <polygon :points="vertices.map(p=>flat.point(p).join(',')).join(' ')" class="lab-region"/>
     <circle v-for="(v,i) in vertices" :key="i" :cx="flat.sx(v[0])" :cy="flat.sy(v[1])" r="4" class="lab-dot"/>
     <circle :cx="flat.sx(point[0])" :cy="flat.sy(point[1])" r="6" class="lab-dot-accent"/>
     <circle :cx="flat.sx(point[0])" :cy="flat.sy(point[1])" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Điểm x trước phép đổi biến" :aria-valuetext="fmtPoint(point,4)" @pointerdown="flatDrag.start('x',$event)" @keydown="flatDrag.key('x',point,$event)"/>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh x bằng nút</summary><LabPointControls :svg="flatSvg"/></details>
   </div>
   <div><p class="panel-title">Miền (y₁, y₂, z) sau đổi biến</p>
    <svg ref="spaceSvg" viewBox="0 0 360 300" role="group" aria-label="Điểm sau đổi biến kéo được trên mặt phẳng trong không gian ba chiều" @pointermove="spaceDrag.move" @pointerup="spaceDrag.end" @pointercancel="spaceDrag.end" @lostpointercapture="spaceDrag.end">
     <polygon :points="plane.map(p=>P(p).join(',')).join(' ')" class="plane"/>
     <line v-for="(end,i) in [[1.2,0,0],[0,1.15,0],[0,0,1.05]]" :key="i" :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(end)[0]" :y2="P(end)[1]" class="lab-axis"/>
     <text :x="P([1.2,0,0])[0]" :y="P([1.2,0,0])[1]+23" text-anchor="end">y₁</text>
     <text :x="P([0,1.15,0])[0]-12" :y="P([0,1.15,0])[1]+20" text-anchor="end">y₂</text>
     <text :x="P([0,0,1.05])[0]+10" :y="P([0,0,1.05])[1]">z</text>
     <polygon :points="vertices.map(p=>P(cooperTransform(p)).join(',')).join(' ')" class="transformed"/>
     <line :x1="P(image)[0]" :y1="P(image)[1]" :x2="P([image[0],image[1],0])[0]" :y2="P([image[0],image[1],0])[1]" class="lab-guide"/>
     <circle v-for="(v,i) in vertices" :key="i" :cx="P(cooperTransform(v))[0]" :cy="P(cooperTransform(v))[1]" r="4" class="lab-dot"/>
     <circle :cx="P(image)[0]" :cy="P(image)[1]" r="6" class="lab-dot-accent"/>
     <circle :cx="P(image)[0]" :cy="P(image)[1]" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Điểm trên mặt phẳng chuẩn hóa" :aria-valuetext="fmtPoint(image,5)" @pointerdown="spaceDrag.start('x',$event)" @keydown="spaceDrag.key('x',point,$event)"/>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm trên mặt bằng nút</summary><LabPointControls :svg="spaceSvg"/></details>
   </div>
  </div>
  <div class="lab-buttons"><button type="button" @click="point=[1,4]">Nghiệm cực đại</button><button type="button" @click="point=[6,0]">Nghiệm cực tiểu</button><button type="button" @click="point=[2,2]">Điểm ở trong miền</button><button type="button" @click="yaw=yaw===32?50:32">Đổi góc nhìn R³</button></div>
  <div class="lab-readout" role="status">
   <p>x = {{fmtPoint(point,4)}}. Sau đổi biến, (y₁, y₂, z) = {{fmtPoint(image,5)}}. Chia hai tọa độ đầu cho z thu lại x ban đầu.</p>
   <p>Chuẩn hóa y₁ + 0.5y₂ + z = {{fmt(image[0]+image[1]/2+image[2],6)}}. Bốn vế trái của ràng buộc LP, theo thứ tự trong bài, là {{residuals.map(v=>fmt(v,5)).join(', ')}} và đều không dương trong dung sai 10⁻⁹.</p>
   <p>Tỉ số gốc f(x) = {{fmt(fractionalValue(point),6)}}. Mục tiêu tuyến tính y₁ + 2y₂ + 2z = {{fmt(result,6)}}.</p>
   <p>Trong tứ giác bị chặn này, z luôn từ 1/7 đến 1/2. Vì vậy mọi điểm của miền LP đều có z &gt; 0 và khôi phục được một điểm x hữu hạn. Các cạnh vẫn thẳng, nhưng trung điểm thường không được biến thành trung điểm.</p>
   <p>Đổi góc nhìn chỉ đổi phép chiếu lên màn hình. Kéo trên hình R³ giữ điểm trên mặt phẳng chuẩn hóa. Phím và nút thay đổi x₁ hoặc x₂ rồi tính lại cả ba tọa độ, không thay riêng z để phá đẳng thức.</p>
  </div>
 </figure>
</template>
<style scoped>
svg{touch-action:pan-y pinch-zoom}
svg text{font-size:18px}
.cooper-pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem}
.panel-title{font-weight:600;text-align:center}
.plane{fill:var(--vang-soft);stroke:var(--vang);stroke-width:1;fill-opacity:.5}
.transformed{fill:var(--tim-soft);stroke:var(--tim);stroke-width:1.5}
svg :is(line,polygon,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
@media(max-width:1050px){.cooper-pair{grid-template-columns:1fr}}
</style>
