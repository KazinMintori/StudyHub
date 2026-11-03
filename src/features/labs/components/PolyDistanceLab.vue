<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {convexPolygonDistance} from '../services/qp-geometry.mjs'
import {clipSegment} from '../services/svg-clipping.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'
const svg=ref(null),center=ref([4.5,2.2])
const a=[[.5,.5],[2.5,.8],[2,2.6],[.6,2]],shape=[[-.8,-.6],[.9,-.4],[.6,.9],[-.7,.7]]
const b=computed(()=>shape.map(p=>p.map((v,i)=>v+center.value[i])))
const result=computed(()=>convexPolygonDistance(a,b.value))
const flat=makeView({x0:-.7,x1:6.9,y0:-.8,y1:5.8,width:360,height:320,pad:28}),P=flat.point
const view=computed(()=>({...flat,x0:.3,x1:5.8,y0:.2,y1:4.7}))
const drag=createDragger(svg,view,(_,p)=>{center.value=p},{step:.05})
const bisector=computed(()=>{
 if(result.value.distance<1e-10)return null
 const {p,q}=result.value,m=p.map((v,i)=>(v+q[i])/2),d=[-(q[1]-p[1]),q[0]-p[0]]
 return clipSegment([-20,20].map(t=>m.map((v,i)=>v+t*d[i])),flat)
})
const labels=computed(()=>placePointLabels([{key:'a',text:'P₁',point:P([1.3,1.4])},{key:'b',text:'P₂',point:P(center.value)}],{width:360,height:320,reserved:[result.value.p,result.value.q,center.value].map(p=>{const [x,y]=P(p);return{x:x-9,y:y-9,width:18,height:18}})}))
</script>
<template>
 <figure class="study-lab" aria-label="QP khoảng cách giữa hai đa giác lồi">
  <figcaption class="lab-title">QP trả về d², còn độ dài đoạn nối là d</figcaption>
  <p class="lab-lead">Kéo chấm tím ở P₂ để tịnh tiến đa giác. Hai chấm vàng là một cặp gần nhau nhất. Khi hai miền giao nhau, chấm xanh đánh dấu một điểm chung thật sự.</p>
  <svg ref="svg" viewBox="0 0 360 320" role="group" aria-label="Hai đa giác, cặp điểm tối ưu và đường phân tách đã cắt đúng khung" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <polygon :points="a.map(p=>P(p).join(',')).join(' ')" class="lab-region"/>
   <polygon :points="b.map(p=>P(p).join(',')).join(' ')" class="second"/>
   <line v-if="bisector" :x1="P(bisector[0])[0]" :y1="P(bisector[0])[1]" :x2="P(bisector[1])[0]" :y2="P(bisector[1])[1]" class="lab-guide"/>
   <line :x1="P(result.p)[0]" :y1="P(result.p)[1]" :x2="P(result.q)[0]" :y2="P(result.q)[1]" class="shortest"/>
   <circle v-for="(p,i) in result.distance>1e-10?[result.p,result.q]:[result.p]" :key="i" :cx="P(p)[0]" :cy="P(p)[1]" r="5" :class="result.distance>1e-10?'lab-dot-warn':'common'"/>
   <text v-for="(label,id) in labels" :key="id" :x="label.x" :y="label.y" :text-anchor="label.anchor">{{id==='a'?'P₁':'P₂'}}</text>
   <circle :cx="P(center)[0]" :cy="P(center)[1]" r="6" class="lab-dot-accent"/>
   <circle :cx="P(center)[0]" :cy="P(center)[1]" r="27" class="lab-handle hit" role="slider" tabindex="0" aria-label="Vị trí tịnh tiến của P2" :aria-valuetext="fmtPoint(center,4)" @pointerdown="drag.start('center',$event)" @keydown="drag.key('center',center,$event)"/>
  </svg>
  <div class="lab-buttons"><button type="button" @click="center=[4.5,2.2]">Hai miền rời nhau</button><button type="button" @click="center=[1.4,1.4]">Hai miền giao nhau</button><button type="button" @click="center=[3.3,1.4]">Cho hai đỉnh chạm nhau</button></div>
  <details class="lab-tasks"><summary>Dịch P₂ bằng nút</summary><LabPointControls :svg="svg"/></details>
  <p class="lab-legend"><span class="legend-accent">P₁</span><span class="legend-good">P₂</span><span class="legend-warn">Đoạn ngắn nhất</span></p>
  <div class="lab-readout" role="status">
   <p>Giá trị tối ưu QP d² = {{fmt(result.squared,6)}}. Khoảng cách Euclid d = {{fmt(result.distance,6)}}.</p>
   <p>Một cặp tối ưu là {{fmtPoint(result.p,4)}} và {{fmtPoint(result.q,4)}}. {{result.distance<1e-10?'Hai miền có điểm chung.':'Đường nét đứt là đường trung trực phân tách hai miền.'}}</p>
   <p>Độ dài được tính từ tọa độ toán học. Hai trục dùng cùng một tỉ lệ, nên góc vuông ở cặp điểm trên cạnh được giữ đúng trên hình. Cặp điểm tối ưu không nhất thiết duy nhất. So sánh hình học dùng dung sai 10⁻¹⁰.</p>
  </div>
 </figure>
</template>
<style scoped>
svg text{font-size:18px}
.second{fill:var(--xanh-soft);stroke:var(--xanh);stroke-width:1.5}
.common{fill:var(--xanh)}
.shortest{stroke:var(--vang);stroke-width:2}
svg :is(line,polygon,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
