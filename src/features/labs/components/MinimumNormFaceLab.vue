<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'
import {project3} from '../services/foundation-geometry.mjs'

const svg=ref(null),dimension=ref(3),point=ref([1,1])
const flat=makeView({x0:-0.4,x1:3.4,y0:-0.4,y1:3.4,width:400,height:350,pad:36})
const camera={yaw:33,pitch:27,scale:63,origin:[190,230]}
const actual=computed(()=>dimension.value===3?[...point.value,3-point.value[0]-point.value[1]]:[point.value[0],3-point.value[0]])
const center=computed(()=>dimension.value===3?[1,1,1]:[1.5,1.5])
const project=p=>dimension.value===3?project3(p,camera):flat.point(p)
const P=()=>project(actual.value)
const basis=computed(()=>{
  const origin=project3([0,0,3],camera),one=project3([1,0,2],camera),two=project3([0,1,2],camera)
  return {origin,a:one.map((x,i)=>x-origin[i]),b:two.map((x,i)=>x-origin[i])}
})
const view=computed(()=>({
  x0:0,x1:3,y0:0,y1:3,
  toWorld:(px,py)=>{
    if(dimension.value===2)return flat.toWorld(px,py)
    const {origin,a,b}=basis.value,dx=px-origin[0],dy=py-origin[1],det=a[0]*b[1]-a[1]*b[0]
    return [(dx*b[1]-dy*b[0])/det,(a[0]*dy-a[1]*dx)/det]
  }
}))
const drag=createDragger(svg,view,(_,p)=>{
  const first=Math.max(0,Math.min(3,p[0]))
  point.value=[first,Math.max(0,Math.min(3-first,p[1]))]
},{step:0.05})
const vertices=computed(()=>dimension.value===3?[[3,0,0],[0,3,0],[0,0,3]]:[[3,0],[0,3]])
const polygon=computed(()=>vertices.value.map(p=>project(p).join(',')).join(' '))
const length=computed(()=>Math.hypot(...actual.value))
function chooseDimension(value){dimension.value=value;point.value=value===3?[1,1]:[1.5,0]}
</script>

<template>
  <figure class="study-lab" aria-label="Toàn đoạn hoặc mặt nghiệm chuẩn L1 và nghiệm Euclid nhỏ nhất">
    <figcaption class="lab-title">Một mặt nghiệm L₁ cùng chứa điểm thưa và điểm có đủ tọa độ dương</figcaption>
    <p class="lab-lead">Tổng các tọa độ bằng 3. Kéo điểm vàng trên đoạn không âm trong R² hoặc mặt tam giác không âm trong R³. Tất cả các điểm đang cho kéo đều có chuẩn L₁ bằng 3. Vòng xanh là nghiệm Euclid nhỏ nhất.</p>
    <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Điểm không âm có tổng tọa độ bằng 3 kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polygon v-if="dimension===3" :points="polygon" class="norm-face" />
      <polyline v-else :points="polygon" class="norm-edge" />
      <line :x1="project(dimension===3?[0,0,0]:[0,0])[0]" :y1="project(dimension===3?[0,0,0]:[0,0])[1]" :x2="P()[0]" :y2="P()[1]" class="norm-radius" />
      <circle v-for="(v,i) in vertices" :key="i" :cx="project(v)[0]" :cy="project(v)[1]" r="4" class="lab-dot-accent" />
      <circle :cx="project(center)[0]" :cy="project(center)[1]" r="9" class="norm-center" />
      <circle :cx="P()[0]" :cy="P()[1]" r="7" class="lab-dot-warn" />
      <circle :cx="P()[0]" :cy="P()[1]" r="32" class="lab-handle norm-face-hit" tabindex="0" role="slider"
        aria-label="Nghiệm không âm của hệ tổng tọa độ" :aria-valuetext="fmtPoint(actual,3)"
        @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',point,$event)" />
      <text x="22" y="26">{{dimension===3?'Mặt trong R³':'Đoạn trong R²'}}</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="dimension===2" @click="chooseDimension(2)">Hai tọa độ</button>
      <button type="button" :aria-pressed="dimension===3" @click="chooseDimension(3)">Ba tọa độ</button>
      <button type="button" @click="point=[3,0]">Một nghiệm thưa</button>
      <button type="button" @click="point=dimension===3?[1,1]:[1.5,0]">Nghiệm Euclid</button>
    </div>
    <div class="lab-readout" role="status">
      <p>x = {{fmtPoint(actual,4)}}. Chuẩn L₁ = 3. Chuẩn Euclid = {{fmt(length,4)}}.</p>
      <p>Giá trị Euclid nhỏ nhất = {{fmt(3/Math.sqrt(dimension),4)}}. Dấu bằng đạt khi mọi tọa độ cùng bằng 3/{{dimension}}.</p>
      <p>Mọi điểm khả thi, kể cả điểm có tọa độ âm nằm ngoài miền đang vẽ, đều có chuẩn L₁ ít nhất 3 theo bất đẳng thức tam giác.</p>
    </div>
  </figure>
</template>

<style scoped>
.norm-face { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.5; }
.norm-edge { fill: none; stroke: var(--xanh); stroke-width: 1.8; }
.norm-radius { stroke: var(--ink-3); stroke-width: 1.3; }
.norm-center { fill: var(--paper); stroke: var(--xanh); stroke-width: 1.8; }
.norm-face-hit { fill: transparent !important; stroke: transparent; }
.norm-face-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
