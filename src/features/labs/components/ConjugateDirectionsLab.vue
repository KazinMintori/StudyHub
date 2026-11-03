<script setup>
import {computed,ref,watch} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'
import {project3,unprojectPlane} from '../services/foundation-geometry.mjs'
import {quadraticTrace} from '../services/conjugate-directions.mjs'

const svg=ref(null)
const space=ref(false),steepest=ref(false),start=ref([0,0,0]),step=ref(0)
const model2={matrix:[[3,1],[1,2]],b:[5,5],solution:[1,2]}
const model3={matrix:[[1,0,0],[0,2,0],[0,0,4]],b:[1,1,1],solution:[1,0.5,0.25]}
const model=computed(()=>space.value?model3:model2)
const trace=computed(()=>{
  const {matrix,b}=model.value
  return quadraticTrace(matrix,b,start.value.slice(0,b.length),steepest.value?'steepest':'cg',b.length)
})
const row=computed(()=>trace.value[Math.min(step.value,trace.value.length-1)])
watch([start,space,steepest],()=>{step.value=0})

const bounds={x0:-1.9,x1:3.5,y0:-1.4,y1:4.1}
const flat=makeView({...bounds,width:400,height:350,pad:34})
const camera={yaw:33,pitch:29,scale:49,origin:[174,218]}
const project=point=>space.value?project3(point,camera):flat.point(point)
const view=computed(()=>space.value?{...bounds,toWorld:(x,y)=>unprojectPlane([x,y],start.value[2],camera)}:flat)
const drag=createDragger(svg,view,(_,p)=>{
  start.value=[Math.max(-1,Math.min(2.5,p[0])),Math.max(-0.8,Math.min(3,p[1])),start.value[2]]
  step.value=0
},{step:0.05})
const poly=points=>points.map(p=>project(p).join(',')).join(' ')
const curves=computed(()=>{
  const angles=Array.from({length:81},(_,i)=>2*Math.PI*i/80)
  if(space.value){
    return [0,1,2].map(axis=>poly(angles.map(a=>{
      const offset=[0,0,0],i=(axis+1)%3,j=(axis+2)%3
      offset[i]=Math.cos(a)/Math.sqrt(model3.matrix[i][i])
      offset[j]=Math.sin(a)/Math.sqrt(model3.matrix[j][j])
      return model3.solution.map((v,k)=>v+offset[k])
    })))
  }
  return [1,3,7].map(q=>poly(angles.map(a=>{
    const dy=Math.sqrt(q/(2-1/3))*Math.sin(a)
    return [1+Math.sqrt(q/3)*Math.cos(a)-dy/3,2+dy]
  })))
})
const displayed=computed(()=>trace.value.slice(0,step.value+1))
const origin=computed(()=>project(start.value))
const solution=computed(()=>project(model.value.solution))
function changeSpace(value){
  space.value=value
  start.value=[0,0,0]
  step.value=0
}
function advance(){step.value=Math.min(step.value+1,trace.value.length-1)}
function chooseHeight(value){start.value=[start.value[0],start.value[1],value]}
</script>

<template>
  <figure class="study-lab" aria-label="Hướng liên hợp trong không gian hai và ba chiều">
    <figcaption class="lab-title">Gradient liên hợp dùng lại thông tin của hướng trước</figcaption>
    <p class="lab-lead">Kéo điểm xuất phát màu vàng rồi đi từng bước. Vòng xanh là nghiệm. Mỗi đoạn tím nối hai trạng thái liên tiếp. Trong R³, chấm kéo được di chuyển trên mặt phẳng có z cố định và ba vòng nét đứt là các lát qua tâm của một ellipsoid đồng mức.</p>
    <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Điểm xuất phát của hệ tuyến tính kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polyline v-for="(curve,i) in curves" :key="i" :points="curve" class="cg-contour" />
      <polyline v-if="displayed.length>1" :points="poly(displayed.map(r=>r.x))" class="cg-path" />
      <circle v-for="(r,i) in displayed.slice(1)" :key="i" :cx="project(r.x)[0]" :cy="project(r.x)[1]" r="4" class="lab-dot-accent" />
      <circle :cx="solution[0]" :cy="solution[1]" r="7" class="cg-solution" />
      <circle :cx="origin[0]" :cy="origin[1]" r="7" class="lab-dot-warn" />
      <circle :cx="origin[0]" :cy="origin[1]" r="32" tabindex="0" role="slider" class="lab-handle cg-hit"
        aria-label="Điểm xuất phát kéo được" :aria-valuetext="fmtPoint(start.slice(0,model.b.length))"
        @pointerdown="drag.start('start',$event)" @keydown="drag.key('start',start,$event)" />
      <text x="20" y="26">{{space?'Hệ trong R³':'Hệ trong R²'}}</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm xuất phát bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="!space" @click="changeSpace(false)">Hệ hai chiều</button>
      <button type="button" :aria-pressed="space" @click="changeSpace(true)">Hệ ba chiều</button>
      <button type="button" :aria-pressed="!steepest" @click="steepest=false">Gradient liên hợp</button>
      <button type="button" :aria-pressed="steepest" @click="steepest=true">Hướng dốc nhất</button>
      <button type="button" @click="advance">Tiến một bước</button>
      <button type="button" @click="step=0">Về điểm xuất phát</button>
      <button type="button" @click="start=[0,0,0]">Xuất phát tại gốc</button>
      <button v-if="space" type="button" @click="chooseHeight(0)">z₀ = 0</button>
      <button v-if="space" type="button" @click="chooseHeight(1)">z₀ = 1</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Bước {{step}}. Điểm hiện tại {{fmtPoint(row.x,4)}}. Chuẩn phần dư {{fmt(Math.hypot(...row.residual),6)}}. Nghiệm {{fmtPoint(model.solution)}}.</p>
      <p v-if="row.conjugacy?.length">Tích qua ma trận A với các hướng trước: {{row.conjugacy.map(v=>fmt(v,6)).join(', ')}}.</p>
      <p v-if="space">Phép chiếu có thể làm hai điểm trông gần nhau. Hãy đọc ba tọa độ và chuẩn phần dư để kiểm tra nghiệm.</p>
    </div>
  </figure>
</template>

<style scoped>
.cg-contour { stroke: var(--ink-3); fill: none; stroke-width: 1.3; stroke-dasharray: 4 4; }
.cg-path { stroke: var(--tim); fill: none; stroke-width: 1.8; }
.cg-solution { stroke: var(--xanh); fill: var(--paper); stroke-width: 1.8; }
.cg-hit { fill: transparent !important; stroke: transparent; }
.cg-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
