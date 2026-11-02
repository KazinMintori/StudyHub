<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { project3,unprojectPlane,planeParameters } from '../services/foundation-geometry.mjs'
const svg=ref(null),mode=ref('probability'),xy=ref([.3,.3]),z=ref(.2),yaw=ref(30)
const origin=[0,0,0],vertices=[[1,0,0],[0,1,0],[0,0,1]]
const camera=computed(()=>({yaw:yaw.value,pitch:30,scale:125,origin:[200,210]})),P=p=>project3(p,camera.value)
const point=computed(()=>[...xy.value,mode.value==='probability'?1-xy.value[0]-xy.value[1]:z.value])
const sum=computed(()=>point.value.reduce((s,v)=>s+v,0))
const weights=computed(()=>mode.value==='probability'?point.value:[1-sum.value,...point.value])
const inside=computed(()=>weights.value.every(v=>v>=-1e-9))
const view=computed(()=>({x0:-.15,x1:1.15,y0:-.15,y1:1.15,toWorld:(x,y)=>mode.value==='probability'?planeParameters([x,y],P(vertices[2]),P(vertices[0]),P(vertices[1]))||xy.value:unprojectPlane([x,y],z.value,camera.value)}))
const drag=createDragger(svg,view,(_,p)=>{
 const total=p[0]+p[1]
 xy.value=mode.value==='probability'&&total>1.25?p.map(v=>v*1.25/total):p
},{step:.025,snap:.005})
const triangles=computed(()=>mode.value==='probability'?[vertices]:[vertices,[origin,vertices[0],vertices[1]],[origin,vertices[0],vertices[2]],[origin,vertices[1],vertices[2]]])
function change(next){mode.value=next;xy.value=[.3,.3];z.value=.2}
</script>

<template>
 <figure class="study-lab" aria-label="So sánh đơn hình xác suất và đơn hình đơn vị trong R³">
  <figcaption class="lab-title">Ba tọa độ không luôn có nghĩa là ba chiều tự do</figcaption>
  <div class="lab-buttons" role="group" aria-label="Loại đơn hình"><button type="button" :aria-pressed="mode==='probability'" @click="change('probability')">Tổng bằng 1: Tam giác</button><button type="button" :aria-pressed="mode==='unit'" @click="change('unit')">Tổng không vượt 1: Tứ diện</button></div>
  <p class="lab-lead">{{mode==='probability'?'Đơn hình xác suất có ba đỉnh e₁, e₂, e₃ và nằm trên mặt phẳng x₁ + x₂ + x₃ = 1. Kéo điểm để đổi x₁, x₂, còn x₃ được xác định bởi tổng.':'Thêm đỉnh O tạo thành tứ diện. Ba tọa độ không âm và có tổng không vượt 1. Kéo trong lát ngang rồi đổi x₃ để đi qua phần trong ba chiều.'}}</p>
  <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Các đỉnh đơn hình trong R³ và điểm kéo được, có thể ra ngoài để thử điều kiện" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <g v-for="(vertex,i) in vertices" :key="i"><line :x1="P(origin)[0]" :y1="P(origin)[1]" :x2="P(vertex.map(v=>v*1.35))[0]" :y2="P(vertex.map(v=>v*1.35))[1]" class="lab-axis"/><text :x="P(vertex.map(v=>v*1.35))[0]+5" :y="P(vertex.map(v=>v*1.35))[1]+5">x{{['₁','₂','₃'][i]}}</text></g>
   <polygon v-for="(triangle,i) in triangles" :key="'t'+i" :points="triangle.map(p=>P(p).join(',')).join(' ')" class="lab-region face"/>
   <g v-for="(vertex,i) in vertices" :key="'v'+i"><circle :cx="P(vertex)[0]" :cy="P(vertex)[1]" r="5" class="lab-dot"/><text :x="P(vertex)[0]+5" :y="P(vertex)[1]+21">e{{['₁','₂','₃'][i]}}</text></g>
   <circle :cx="P(origin)[0]" :cy="P(origin)[1]" r="4" class="lab-dot"/><text :x="P(origin)[0]-20" :y="P(origin)[1]+21">O</text>
   <line :x1="P(origin)[0]" :y1="P(origin)[1]" :x2="P(point)[0]" :y2="P(point)[1]" class="lab-guide"/>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" :class="inside?'lab-dot-accent':'lab-dot-bad'" pointer-events="none"/><text :x="P(point)[0]+12" :y="P(point)[1]-12">x</text>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="30" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Điểm x để kiểm tra thuộc đơn hình" :aria-valuetext="fmtPoint(point)" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',xy,$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/><p>Trong chế độ tam giác, trái/phải đổi x₁ và lên/xuống đổi x₂. x₃ thay đổi để giữ tổng bằng 1.</p></details>
  <div class="lab-controls"><label v-if="mode==='unit'">x₃ = {{fmt(z)}}<input v-model.number="z" type="range" min="0" max="1.2" step=".05"/></label><label>Góc nhìn quanh x₃: {{yaw}}°<input v-model.number="yaw" type="range" min="-70" max="70" step="5"/></label></div>
  <div class="lab-buttons"><button type="button" @click="xy=mode==='probability'?[1/3,1/3]:[.25,.25];z=.25">Trọng tâm</button><button type="button" @click="xy=[.8,.4];z=.2">Thử điểm ngoài</button></div>
  <div class="lab-readout" role="status"><p>x = {{fmtPoint(point)}}. Tổng ba tọa độ bằng {{fmt(sum)}}. {{inside?'Điểm thuộc đơn hình đang chọn.':'Điểm không thuộc đơn hình đang chọn.'}}</p><p>Trọng số theo {{mode==='probability'?'ba đỉnh (e₁, e₂, e₃)':'bốn đỉnh (O, e₁, e₂, e₃)'}} là {{fmtPoint(weights)}}. Tổng các trọng số bằng 1, nhưng để là tổ hợp lồi thì từng trọng số còn phải không âm.</p><p>{{mode==='probability'?'Chiều affine bằng 2. Trong R³, tam giác không có điểm trong, nhưng có nội tương đối là tam giác bỏ ba cạnh.':'Chiều affine bằng 3. Phần trong gồm các điểm có ba tọa độ dương và tổng nhỏ hơn 1.'}}</p><p>Hình dùng phép chiếu vuông góc. Xoay hình để phân biệt vị trí trong không gian với sự chồng lấp của các điểm trên màn hình.</p></div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt điểm ngoài. Trọng số nào âm và nó ứng với đỉnh nào?</li><li>Chuyển giữa hai đơn hình. Vì sao thêm một đỉnh làm chiều affine tăng thêm 1?</li><li>Trong đơn hình xác suất, tăng x₁ trong khi giữ x₂. Vì sao x₃ phải giảm?</li></ol></details>
 </figure>
</template>

<style scoped>
.face{fill-opacity:.2;stroke-width:1.8}
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
</style>
