<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3,unprojectPlane} from '../services/foundation-geometry.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'
const svg=ref(null),kind=ref('bowl'),a=ref([-1,-.5]),b=ref([.9,.7]),theta=ref(.45)
const camera={yaw:25,pitch:32,scale:69,origin:[200,215]}
const f=p=>(p[0]**2+(kind.value==='bowl'?1:-1)*p[1]**2)/2
const P=(p,z=0)=>project3([...p,z],camera)
const mix=computed(()=>a.value.map((v,i)=>theta.value*v+(1-theta.value)*b.value[i]))
const chord=computed(()=>theta.value*f(a.value)+(1-theta.value)*f(b.value))
const gap=computed(()=>chord.value-f(mix.value))
const mesh=computed(()=>Array.from({length:9},(_,i)=>-1.4+i*.35).flatMap(fixed=>[0,1].map(axis=>Array.from({length:33},(_,j)=>{const moving=-1.4+j*2.8/32,p=axis?[moving,fixed]:[fixed,moving];return P(p,f(p)).join(',')}).join(' '))))
const view=ref({x0:-1.4,x1:1.4,y0:-1.4,y1:1.4,toWorld:(x,y)=>unprojectPlane([x,y],0,camera)})
const drag=createDragger(svg,view,(name,p)=>{if(name==='a')a.value=p;else b.value=p},{step:.1})
const labels=computed(()=>{
 const lifted=[P(a.value,f(a.value)),P(b.value,f(b.value)),P(mix.value,f(mix.value))]
 const reserved=[...lifted,P(a.value),P(b.value),P(mix.value,chord.value)].map(p=>({x:p[0]-10,y:p[1]-10,width:20,height:20}))
 return placePointLabels([{key:'a',text:'A',point:lifted[0]},{key:'b',text:'B',point:lifted[1]},{key:'mix',text:'z',point:lifted[2]}],{width:400,height:340,reserved})
})
function preset(value){kind.value=value;a.value=value==='bowl'?[-1,-.5]:[0,-1.2];b.value=value==='bowl'?[.9,.7]:[0,1.2];theta.value=.45}
</script>
<template>
 <figure class="study-lab" aria-label="Dây cung của một hàm hai biến nhìn trong R³">
  <figcaption class="lab-title">Hai đầu vào thuộc R², dây cung nằm trong R³</figcaption>
  <p class="lab-lead">Kéo hai chấm ở mặt phẳng đáy để đổi đầu vào a và b. Các điểm A, B phía trên có độ cao f(a), f(b). Đoạn thẳng AB là dây cung. So độ cao của dây với mặt hàm tại cùng đầu vào z.</p>
  <div class="lab-buttons" role="group" aria-label="Mặt hàm hai biến"><button type="button" :aria-pressed="kind==='bowl'" @click="preset('bowl')">Cái bát lồi</button><button type="button" :aria-pressed="kind==='saddle'" @click="preset('saddle')">Yên ngựa vi phạm dây cung</button></div>
  <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Mặt hàm, hai điểm trên đáy, dây cung và khoảng cách tới đồ thị" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <polygon :points="[[-1.4,-1.4],[1.4,-1.4],[1.4,1.4],[-1.4,1.4]].map(p=>P(p).join(',')).join(' ')" class="floor"/>
   <polyline v-for="(line,i) in mesh" :key="i" :points="line" class="mesh"/>
   <line :x1="P(a,f(a))[0]" :y1="P(a,f(a))[1]" :x2="P(b,f(b))[0]" :y2="P(b,f(b))[1]" class="lab-accent"/>
   <line :x1="P(mix,f(mix))[0]" :y1="P(mix,f(mix))[1]" :x2="P(mix,chord)[0]" :y2="P(mix,chord)[1]" :class="gap>=0?'lab-good':'lab-bad'"/>
   <g v-for="(p,name) in {a,b}" :key="name"><line :x1="P(p)[0]" :y1="P(p)[1]" :x2="P(p,f(p))[0]" :y2="P(p,f(p))[1]" class="lab-guide"/><circle :cx="P(p,f(p))[0]" :cy="P(p,f(p))[1]" r="5" class="lab-dot"/><text :x="labels[name].x" :y="labels[name].y" :text-anchor="labels[name].anchor">{{name.toUpperCase()}}</text><circle :cx="P(p)[0]" :cy="P(p)[1]" r="8" class="lab-dot-accent"/><circle :cx="P(p)[0]" :cy="P(p)[1]" r="28" class="lab-handle hit" tabindex="0" role="slider" :aria-label="`Đầu vào ${name} trên mặt phẳng đáy`" :aria-valuetext="fmtPoint(p,4)" @pointerdown="drag.start(name,$event)" @keydown="drag.key(name,p,$event)"/></g>
   <circle :cx="P(mix,f(mix))[0]" :cy="P(mix,f(mix))[1]" r="5" class="lab-dot-warn"/><text :x="labels.mix.x" :y="labels.mix.y" :text-anchor="labels.mix.anchor">z</text><circle :cx="P(mix,chord)[0]" :cy="P(mix,chord)[1]" r="5" class="lab-dot-hollow"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-controls"><label>θ = {{fmt(theta)}}<input v-model.number="theta" type="range" min="0" max="1" step=".05"/></label></div>
  <div class="lab-readout" role="status"><p>f(x₁, x₂) = {{kind==='bowl'?'(x₁² + x₂²)/2':'(x₁² − x₂²)/2'}}. z = θa + (1 − θ)b = {{fmtPoint(mix)}}.</p><p>Giá trị trên dây cung bằng {{fmt(chord,4)}}, còn f(z) = {{fmt(f(mix),4)}}. Hiệu dây cung trừ đồ thị là {{fmt(gap,4)}}.</p><p :class="gap>=-1e-9?'is-good':'is-bad'">{{gap>=-1e-9?'Dây cung đang nằm trên hoặc chạm đồ thị tại z.':'Dây cung đang nằm dưới đồ thị tại z, đủ để bác bỏ tính lồi.'}}</p><p>Mặt lưới chỉ là mảnh đồ thị trong khung. Với mặt yên ngựa, một số đoạn vẫn thỏa bất đẳng thức, nên không kết luận lồi chỉ từ một đoạn đạt.</p></div>
 </figure>
</template>
<style scoped>
svg text{font-size:20px;pointer-events:none}.floor{fill:var(--canvas);stroke:var(--ink-3);stroke-width:1;stroke-dasharray:4 4}.mesh{fill:none;stroke:var(--ink-3);stroke-width:.8;opacity:.6}svg :is(line,polygon,polyline),svg circle:not(.hit){pointer-events:none}.hit{fill:transparent!important;stroke:transparent}.hit:focus-visible{stroke:var(--vang)}
</style>
