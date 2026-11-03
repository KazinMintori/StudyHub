<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3,unprojectPlane} from '../services/foundation-geometry.mjs'
import {cubeDistance} from '../services/qp-geometry.mjs'
const svg=ref(null),lower=ref([2.5,2,1.6])
const camera={yaw:32,pitch:28,scale:55,origin:[147,194]},P=p=>project3(p,camera)
const vertices=offset=>Array.from({length:8},(_,i)=>[0,1,2].map(j=>offset[j]+((i>>j)&1)))
const a=vertices([0,0,0]),b=computed(()=>vertices(lower.value))
const faces=[[0,1,3,2],[0,2,6,4],[0,1,5,4],[4,5,7,6],[1,3,7,5],[2,3,7,6]]
const edges=Array.from({length:8},(_,i)=>[1,2,4].filter(bit=>(i&bit)===0).map(bit=>[i,i|bit])).flat()
const anchor=computed(()=>[lower.value[0]+.5,lower.value[1]+.5,lower.value[2]])
const view=computed(()=>({x0:0,x1:3.25,y0:0,y1:3.25,toWorld:(x,y)=>unprojectPlane([x,y],lower.value[2],camera)}))
const drag=createDragger(svg,view,(_,p)=>{lower.value=[p[0]-.5,p[1]-.5,lower.value[2]]},{step:.05})
const model=computed(()=>cubeDistance(lower.value))
function choose(p){lower.value=p}
</script>
<template>
 <figure class="study-lab" aria-label="Khoảng cách giữa hai khối lập phương trong R3">
  <figcaption class="lab-title">Ba chiều: Khe hở theo từng trục hợp thành độ dài nào?</figcaption>
  <p class="lab-lead">Khối tím là [0, 1]³. Khối xanh là một bản tịnh tiến của nó. Kéo chấm tím ở đáy khối xanh để đổi hai tọa độ đầu, dùng nút để đổi độ cao. Đoạn vàng nối một cặp điểm gần nhau nhất.</p>
  <svg ref="svg" viewBox="0 0 360 340" role="group" aria-label="Hai khối, đoạn khoảng cách và điểm điều khiển trên đáy khối thứ hai" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <template v-for="(cube,index) in [a,b]" :key="index">
    <polygon v-for="(face,i) in faces" :key="i" :points="face.map(k=>P(cube[k]).join(',')).join(' ')" :class="index?'b-face':'a-face'"/>
    <line v-for="([i,j],k) in edges" :key="k" :x1="P(cube[i])[0]" :y1="P(cube[i])[1]" :x2="P(cube[j])[0]" :y2="P(cube[j])[1]" :class="index?'b-edge':'a-edge'"/>
   </template>
   <line v-for="(end,i) in [[3.8,0,0],[0,3.8,0],[0,0,3]]" :key="i" :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(end)[0]" :y2="P(end)[1]" class="lab-axis"/>
   <text :x="P([3.8,0,0])[0]+5" :y="P([3.8,0,0])[1]+18">x₁</text><text :x="P([0,3.8,0])[0]-8" :y="P([0,3.8,0])[1]+20" text-anchor="end">x₂</text><text :x="P([0,0,3])[0]+8" :y="P([0,0,3])[1]">x₃</text>
   <line :x1="P(model.p)[0]" :y1="P(model.p)[1]" :x2="P(model.q)[0]" :y2="P(model.q)[1]" class="gap"/>
   <circle v-for="(p,i) in model.distance>1e-10?[model.p,model.q]:[model.p]" :key="i" :cx="P(p)[0]" :cy="P(p)[1]" r="5" class="lab-dot-warn"/>
   <circle :cx="P(anchor)[0]" :cy="P(anchor)[1]" r="6" class="lab-dot-accent"/>
   <circle :cx="P(anchor)[0]" :cy="P(anchor)[1]" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Vị trí đáy khối xanh trên mặt phẳng ngang" :aria-valuetext="fmtPoint(lower,4)" @pointerdown="drag.start('box',$event)" @keydown="drag.key('box',anchor,$event)"/>
  </svg>
  <div class="lab-buttons"><button type="button" @click="choose([2.5,2,1.6])">Cách nhau theo ba trục</button><button type="button" @click="choose([2,.2,.2])">Hai mặt gần nhất</button><button type="button" @click="choose([1,0,0])">Hai mặt chạm nhau</button><button type="button" @click="choose([.3,.3,.3])">Hai khối giao nhau</button></div>
  <div class="lab-buttons" role="group" aria-label="Độ cao đáy khối xanh"><button v-for="height in [0,.5,2]" :key="height" type="button" @click="lower=[lower[0],lower[1],height]">Đáy x₃ = {{height}}</button></div>
  <details class="lab-tasks"><summary>Dịch khối xanh bằng nút</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-readout" role="status">
   <p>Góc dưới khối xanh = {{fmtPoint(lower,4)}}. QP sáu biến cho d² = {{fmt(model.squared,6)}}, còn d = {{fmt(model.distance,6)}}.</p>
   <p>Một cặp điểm tối ưu là {{fmtPoint(model.p,4)}} và {{fmtPoint(model.q,4)}}. {{model.distance<1e-10?'Hai khối có điểm chung.':'Các khe hở khác 0 kết hợp theo định lý Pythagoras.'}}</p>
   <p>Với hai mặt song song, có thể có cả một họ cặp điểm tối ưu. Hình chỉ chọn một cặp đại diện. Phép chiếu R³ lên màn hình không giữ mọi góc và độ dài, vì vậy đọc số từ tọa độ thay vì đo đoạn trên màn hình.</p>
  </div>
 </figure>
</template>
<style scoped>
svg text{font-size:18px}
.a-face{fill:var(--tim-soft);fill-opacity:.12;stroke:none}
.b-face{fill:var(--xanh-soft);fill-opacity:.16;stroke:none}
.a-edge{stroke:var(--tim);stroke-width:1.1}
.b-edge{stroke:var(--xanh);stroke-width:1.1}
.gap{stroke:var(--vang);stroke-width:2}
svg :is(line,polygon,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
