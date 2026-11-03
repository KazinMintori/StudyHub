<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {quadraticBox} from '../services/qp-geometry.mjs'
import {clipPolyline,clipSegment} from '../services/svg-clipping.mjs'
import {project3} from '../services/foundation-geometry.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'
const svg=ref(null),center=ref([3,1]),rho=ref(.6)
const flat=makeView({x0:-1.5,x1:3.5,y0:-1.5,y1:3.5,width:360,height:320,pad:30})
const view=computed(()=>({...flat,x0:-1,x1:3,y0:-1,y1:3})),P=flat.point
const drag=createDragger(svg,view,(_,p)=>{center.value=p},{step:.05})
const model=computed(()=>quadraticBox(center.value,rho.value)),corners=[[0,0],[2,0],[2,2],[0,2]]
const contours=computed(()=>{
 const lines=[]
 for(const level of [.25,1,2.5,model.value.minimum].filter((v,i,a)=>v>1e-8&&a.indexOf(v)===i)){
  if(rho.value===1){
   for(const sign of [-1,1]){
    const sum=center.value[0]+center.value[1]+sign*Math.sqrt(level),line=clipSegment([[-10,sum+10],[10,sum-10]],flat)
    if(line)lines.push({level,points:line.map(p=>P(p).join(',')).join(' ')})
   }
  }else{
   const points=Array.from({length:161},(_,i)=>{
    const angle=i*Math.PI/80,dy=Math.sqrt(level/(1-rho.value**2))*Math.sin(angle)
    return [center.value[0]+Math.sqrt(level)*Math.cos(angle)-rho.value*dy,center.value[1]+dy]
   })
   for(const line of clipPolyline(points,flat))lines.push({level,points:line.map(p=>P(p).join(',')).join(' ')})
  }
 }
 return lines
})
const ceiling=computed(()=>Math.max(1,...corners.map(model.value.value)))
const camera={yaw:32,pitch:28,scale:88,origin:[180,210]}
const S=(p,z=0)=>project3([p[0]-1,p[1]-1,z],camera)
const surface=p=>S(p,1.35*model.value.value(p)/ceiling.value)
const mesh=computed(()=>{
 const lines=[]
 for(const fixed of [0,.4,.8,1.2,1.6,2])for(const axis of [0,1])lines.push(Array.from({length:33},(_,i)=>surface(axis===0?[fixed,i/16]:[i/16,fixed]).join(',')).join(' '))
 return lines
})
const labels=computed(()=>placePointLabels([{key:'c',text:'C',point:P(center.value)},{key:'x',text:'x*',point:P(model.value.point)}],{width:360,height:320,reserved:[center.value,model.value.point].map(p=>{const [x,y]=P(p);return{x:x-9,y:y-9,width:18,height:18}})}))
function choose(p,r=.6){center.value=p;rho.value=r}
</script>
<template>
 <figure class="study-lab" aria-label="Hình học QP lồi trên hình vuông với đồ thị trong R3">
  <figcaption class="lab-title">Tâm C có thể ở ngoài miền, còn nghiệm x* ở đâu?</figcaption>
  <p class="lab-lead">Kéo tâm C trên hình đường mức. Miền quyết định là hình vuông [0, 2]². Mục tiêu là (x₁ − C₁)² + 2ρ(x₁ − C₁)(x₂ − C₂) + (x₂ − C₂)². Điểm xanh là nghiệm thực sự, không phải kết quả kẹp từng tọa độ của C.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 360 320" role="group" aria-label="Tâm kéo được, đường mức và nghiệm QP trên hình vuông" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <polygon :points="corners.map(p=>P(p).join(',')).join(' ')" class="lab-region"/>
    <polyline v-for="(line,i) in contours" :key="i" :points="line.points" :class="Math.abs(line.level-model.minimum)<1e-8?'optimal-level':'contour'"/>
    <line v-if="model.best.length>1&&rho===1" :x1="P(model.best[0])[0]" :y1="P(model.best[0])[1]" :x2="P(model.best.at(-1))[0]" :y2="P(model.best.at(-1))[1]" class="optimal-set"/>
    <circle :cx="P(model.point)[0]" :cy="P(model.point)[1]" r="6" class="optimum"/>
    <circle :cx="P(center)[0]" :cy="P(center)[1]" r="5" class="lab-dot-accent"/>
    <text v-for="(label,id) in labels" :key="id" :x="label.x" :y="label.y" :text-anchor="label.anchor">{{id==='c'?'C':'x*'}}</text>
    <text :x="flat.sx(0)" y="304">0</text><text :x="flat.sx(2)" y="304">2</text><text x="22" :y="flat.sy(2)">2</text>
    <circle :cx="P(center)[0]" :cy="P(center)[1]" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Tâm C của hàm toàn phương" :aria-valuetext="fmtPoint(center,4)" @pointerdown="drag.start('center',$event)" @keydown="drag.key('center',center,$event)"/>
   </svg>
   <svg viewBox="0 0 360 320" role="img" aria-label="Đồ thị mục tiêu trên cùng hình vuông trong R3, hai biến đầu vào và một trục giá trị">
    <polygon :points="corners.map(p=>S(p).join(',')).join(' ')" class="floor"/>
    <polyline v-for="(line,i) in mesh" :key="i" :points="line" class="mesh"/>
    <line v-for="(end,i) in [[2.35,1,0],[1,2.35,0],[1,1,1.7]]" :key="i" :x1="S([1,1])[0]" :y1="S([1,1])[1]" :x2="S(end,end[2])[0]" :y2="S(end,end[2])[1]" class="lab-axis"/>
    <text :x="S([2.35,1])[0]+6" :y="S([2.35,1])[1]+20">x₁</text>
    <text :x="S([1,2.35])[0]-9" :y="S([1,2.35])[1]+22" text-anchor="end">x₂</text>
    <text :x="S([1,1],1.7)[0]+10" :y="S([1,1],1.7)[1]">f</text>
    <line :x1="S(model.point)[0]" :y1="S(model.point)[1]" :x2="surface(model.point)[0]" :y2="surface(model.point)[1]" class="lab-guide"/>
    <circle :cx="surface(model.point)[0]" :cy="surface(model.point)[1]" r="6" class="optimum"/>
   </svg>
  </div>
  <div class="lab-buttons"><button type="button" @click="choose([1,1])">Nghiệm trong miền</button><button type="button" @click="choose([3,1])">Nghiệm giữa cạnh</button><button type="button" @click="choose([3,-1],0)">Nghiệm tại đỉnh</button><button type="button" @click="choose([1,1],1)">PSD suy biến, nhiều nghiệm</button></div>
  <details class="lab-tasks"><summary>Di chuyển tâm C bằng nút</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-readout" role="status">
   <p>C = {{fmtPoint(center,4)}}, ρ = {{fmt(rho,2)}}. Một nghiệm x* = {{fmtPoint(model.point,5)}}, giá trị tối ưu = {{fmt(model.minimum,6)}}.</p>
   <p v-if="rho<1">Hai trị riêng của Hessian là {{fmt(2*(1-rho),3)}} và {{fmt(2*(1+rho),3)}}, đều dương. Nghiệm trong hình vuông là duy nhất.</p>
   <p v-else>Khi ρ = 1, f = (x₁ + x₂ − C₁ − C₂)². Nếu đường x₁ + x₂ = C₁ + C₂ cắt hình vuông thành một đoạn, mọi điểm trên đoạn đều tối ưu. Chấm xanh là một đại diện.</p>
   <p>Hình R³ là đồ thị của hàm hai biến, không phải bài toán ba biến quyết định. Trục đứng được co theo hệ số {{fmt(1.35/ceiling,5)}} để giữ toàn bộ mặt trong khung. Lưới mảnh chỉ vẽ phần đồ thị trên miền khả thi.</p>
  </div>
 </figure>
</template>
<style scoped>
svg text{font-size:18px}
.contour{fill:none;stroke:var(--ink-3);stroke-width:1}
.optimal-level{fill:none;stroke:var(--vang);stroke-width:1.7}
.optimal-set{stroke:var(--xanh);stroke-width:2.5}
.optimum{fill:var(--xanh)}
.floor{fill:var(--tim-soft);stroke:var(--tim);stroke-width:1}
.mesh{fill:none;stroke:var(--ink-2);stroke-width:.85}
svg :is(line,polyline,polygon,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
