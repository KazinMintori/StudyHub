<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { project3,unprojectPlane,pNorm3,rotate2,ellipsoidGauge } from '../services/foundation-geometry.mjs'

const props=defineProps({type:{type:String,default:'norm'}})
const svg=ref(null),p=ref(2),xy=ref([.65,.35]),z=ref(.3),yaw=ref(30),angle=ref(25),third=ref(.6)
const radii=computed(()=>[1.5,.9,third.value]),radians=computed(()=>angle.value*Math.PI/180)
const camera=computed(()=>({yaw:yaw.value,pitch:30,scale:75,origin:[200,175]}))
const point=computed(()=>[...xy.value,z.value]),P=q=>project3(q,camera.value)
const transform=q=>props.type==='ellipsoid'?[...rotate2([q[0]*radii.value[0],q[1]*radii.value[1]],radians.value),q[2]*radii.value[2]]:q
const gauge=computed(()=>props.type==='ellipsoid'?ellipsoidGauge(point.value,radii.value,radians.value):pNorm3(point.value,p.value))
const surface=(latitude,longitude)=>{
 const q=[Math.cos(latitude)*Math.cos(longitude),Math.cos(latitude)*Math.sin(longitude),Math.sin(latitude)]
 const normalized=props.type==='norm'?q.map(v=>v/pNorm3(q,p.value)):q
 return transform(normalized)
}
const curves=computed(()=>{
 if(props.type==='norm'&&p.value!==2)return []
 const lines=[]
 for(let j=-3;j<=3;j++)lines.push(Array.from({length:97},(_,i)=>surface(j*Math.PI/8,i*Math.PI/48)))
 for(let j=0;j<12;j++)lines.push(Array.from({length:49},(_,i)=>surface(-Math.PI/2+i*Math.PI/48,j*Math.PI/6)))
 return lines
})
const faces=computed(()=>{
 if(props.type!=='norm'||p.value===2)return []
 if(p.value===1)return Array.from({length:8},(_,i)=>[[i&1?1:-1,0,0],[0,i&2?1:-1,0],[0,0,i&4?1:-1]])
 return [0,1,2].flatMap(axis=>[-1,1].map(sign=>[[-1,-1],[1,-1],[1,1],[-1,1]].map(([u,v])=>{const q=[];q[axis]=sign;q[(axis+1)%3]=u;q[(axis+2)%3]=v;return q})))
})
const slice=computed(()=>{
 if(props.type==='ellipsoid'){
  if(third.value===0&&Math.abs(z.value)>1e-8)return []
  const factor=third.value===0?1:Math.sqrt(Math.max(0,1-(z.value/third.value)**2))
  if(third.value!==0&&Math.abs(z.value)>third.value)return []
  return Array.from({length:97},(_,i)=>{const t=i*Math.PI/48;return [...rotate2([radii.value[0]*factor*Math.cos(t),radii.value[1]*factor*Math.sin(t)],radians.value),z.value]})
 }
 const height=Math.abs(z.value)
 if(height>1)return []
 if(p.value===Infinity)return [[-1,-1,z.value],[1,-1,z.value],[1,1,z.value],[-1,1,z.value]]
 const radius=(1-height**p.value)**(1/p.value)
 return Array.from({length:97},(_,i)=>{const t=i*Math.PI/48,q=[Math.cos(t),Math.sin(t)],n=pNorm3(q,p.value);return [radius*q[0]/n,radius*q[1]/n,z.value]})
})
const view=computed(()=>({x0:-1.6,x1:1.6,y0:-1.6,y1:1.6,toWorld:(x,y)=>unprojectPlane([x,y],z.value,camera.value)}))
const drag=createDragger(svg,view,(_,q)=>{xy.value=q},{step:.05,snap:.01})
const path=points=>points.map(q=>P(q).join(',')).join(' ')
const axes=[{q:[2.1,0,0],label:'x₁'},{q:[0,2.1,0],label:'x₂'},{q:[0,0,2.1],label:'x₃'}]
const names={1:'L₁',2:'L₂',Infinity:'L∞'}
</script>

<template>
 <figure class="study-lab" :aria-label="type==='ellipsoid'?'Ellipsoid ba chiều và lát cắt ngang':'Ba quả cầu chuẩn trong R³'">
  <figcaption class="lab-title">{{type==='ellipsoid'?'Ellipsoid có thể co thành một đĩa phẳng':'Hình thoi thành bát diện, hình vuông thành khối lập phương'}}</figcaption>
  <p class="lab-lead">{{type==='ellipsoid'?'Ba bán trục ban đầu là 1,5; 0,9; 0,6. Giảm bán trục thứ ba về 0 để thấy chiều affine giảm từ 3 xuống 2.':'Trong R³, quả cầu L₁ là khối bát diện, L₂ là khối cầu và L∞ là khối lập phương. Mỗi hình gồm cả phần trong, không chỉ các cạnh hay đường lưới.'}} Kéo x trong lát ngang rồi thay x₃ để thử các điểm ở độ cao khác.</p>
  <div v-if="type==='norm'" class="lab-buttons" role="group" aria-label="Chuẩn của quả cầu"><button v-for="value in [1,2,Infinity]" :key="value" type="button" :aria-pressed="p===value" @click="p=value">{{names[value]}}</button></div>
  <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Vật thể ba chiều, lát cắt ngang và điểm thử kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <g v-for="axis in axes" :key="axis.label"><line :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(axis.q)[0]" :y2="P(axis.q)[1]" class="lab-axis"/><text :x="P(axis.q)[0]+5" :y="P(axis.q)[1]+5">{{axis.label}}</text></g>
   <polygon v-for="(face,i) in faces" :key="'f'+i" :points="path(face)" class="lab-region face"/>
   <polyline v-for="(curve,i) in curves" :key="'c'+i" :points="path(curve)" class="lab-line mesh"/>
   <polygon v-if="slice.length" :points="path(slice)" class="lab-good-fill cut"/>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" :class="gauge<=1+1e-9?'lab-dot-accent':'lab-dot-bad'" pointer-events="none"/><text :x="P(point)[0]+12" :y="P(point)[1]-12">x</text>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="32" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Điểm x trong lát cắt ngang" :aria-valuetext="fmtPoint(point)" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',xy,$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <p class="lab-legend"><span class="legend-accent">Biên vật thể</span><span class="legend-good">Phần giao với lát ngang</span><span class="legend-bad">Điểm ở ngoài</span></p>
  <div class="lab-controls"><label>x₃ = {{fmt(z)}}<input v-model.number="z" type="range" min="-1.5" max="1.5" step=".05"/></label><label>Góc nhìn quanh x₃: {{yaw}}°<input v-model.number="yaw" type="range" min="-90" max="90" step="5"/></label><label v-if="type==='ellipsoid'">Bán trục thứ ba: {{fmt(third)}}<input v-model.number="third" type="range" min="0" max="1.5" step=".05"/></label><label v-if="type==='ellipsoid'">Xoay vật thể quanh x₃: {{angle}}°<input v-model.number="angle" type="range" min="0" max="90" step="5"/></label></div>
  <div class="lab-buttons"><button type="button" @click="z=0">Lát qua tâm</button><button type="button" @click="xy=[0,0];z=0">Đưa x về tâm</button></div>
  <div class="lab-readout" role="status"><p>x = {{fmtPoint(point)}}. {{gauge<=1+1e-9?'Điểm thuộc vật thể.':'Điểm nằm ngoài vật thể.'}}</p><p v-if="type==='norm'">‖x‖₁ = {{fmt(pNorm3(point,1))}}, ‖x‖₂ = {{fmt(pNorm3(point,2))}}, ‖x‖∞ = {{fmt(pNorm3(point,Infinity))}}. Điều kiện của quả cầu đang chọn là ‖x‖{{p===Infinity?'∞':p}} ≤ 1.</p><template v-else><p>Bình phương ba bán trục là {{fmt(2.25)}}, {{fmt(.81)}} và {{fmt(third*third)}}. Đây là các trị riêng của ma trận định hình P.</p><p v-if="third===0">Ellipsoid suy biến nằm trong mặt phẳng x₃ = 0. P không khả nghịch, nên phải dùng biểu diễn ảnh của quả cầu đơn vị để mô tả nó.</p><p v-else>Trong hệ trục riêng, căn của dạng toàn phương bằng {{fmt(gauge)}}. Điểm thuộc ellipsoid khi đại lượng này không vượt quá 1.</p></template><p>{{slice.length?'Lát ngang đang cắt vật thể.':'Lát ngang không có điểm chung với vật thể.'}} Hình 3D là phép chiếu vuông góc, không thể suy ra độ dài trực tiếp từ góc nhìn trên màn hình.</p></div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>{{type==='norm'?'Giữ x rồi đổi chuẩn. Tính chất thuộc quả cầu có thay đổi không?':'Giữ điểm có x₃ khác 0 rồi giảm bán trục thứ ba. Khi nào điểm ra ngoài?'}}</li><li>Chọn lát qua tâm. Hình cắt giống hình hai chiều nào đã học?</li><li>{{type==='norm'?'Với L∞, vì sao các lát có |x₃| nhỏ hơn 1 đều là hình vuông cùng kích thước?':'Giảm bán trục thứ ba về 0. Vì sao nội tương đối của đĩa vẫn khác rỗng dù thể tích ba chiều bằng 0?'}}</li></ol></details>
 </figure>
</template>

<style scoped>
.face{fill-opacity:.09;stroke-width:1.3}
.mesh{opacity:.48;stroke-width:1.2}
.cut{fill-opacity:.35}
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
</style>
