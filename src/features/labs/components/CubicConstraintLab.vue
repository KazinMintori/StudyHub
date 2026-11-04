<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3} from '../services/foundation-geometry.mjs'

const svg=ref(null),axis=ref(0),coordinate=ref(0)
const camera={yaw:34,pitch:29,scale:54,origin:[200,178]}
const project=p=>project3(p,camera)
const vector=t=>[0,1,2].map(i=>i===axis.value?t:0)
const point=computed(()=>vector(coordinate.value))
const origin=project([0,0,0])
const direction=computed(()=>project(vector(1)).map((x,i)=>x-origin[i]))
const handle=computed(()=>project(point.value))
const view=ref({x0:0,x1:400,y0:-350,y1:0,toWorld:(x,y)=>[x,-y]})
const drag=createDragger(svg,view,(_,p)=>{
  const d=direction.value
  const t=((p[0]-origin[0])*d[0]+(-p[1]-origin[1])*d[1])/(d[0]**2+d[1]**2)
  coordinate.value=Math.max(-2,Math.min(1,Math.round(t*20)/20))
},{step:5})
const sphere=[0,1,2].map(fixed=>Array.from({length:81},(_,i)=>{
  const p=[0,0,0],angle=2*Math.PI*i/80
  p[(fixed+1)%3]=2*Math.cos(angle)
  p[(fixed+2)%3]=2*Math.sin(angle)
  return project(p).join(',')
}).join(' '))
const endpoints=computed(()=>[-2,1].map(t=>project(vector(t))))
const minima=[[ -2,0,0],[0,-2,0],[0,0,-2]]
</script>

<template>
  <figure class="study-lab" aria-label="Điểm KKT và nghiệm toàn cục của mục tiêu tổng lập phương">
    <figcaption class="lab-title">Điểm KKT tại gốc có thể đi theo hướng giảm khả thi</figcaption>
    <p class="lab-lead">Quả cầu có bán kính 2. Ba vòng nét đứt là các lát qua tâm. Mô phỏng chỉ cho thử điểm trên từng trục, với tọa độ t từ −2 đến 1 để đồng thời thỏa tổng tọa độ không quá 1. Kéo điểm vàng dọc trục đang chọn.</p>
    <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Tọa độ t kéo trên một trục trong R3"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polyline v-for="(curve,i) in sphere" :key="i" :points="curve" class="cubic-sphere" />
      <line :x1="endpoints[0][0]" :y1="endpoints[0][1]" :x2="endpoints[1][0]" :y2="endpoints[1][1]" class="cubic-axis" />
      <circle v-for="(p,i) in minima" :key="i" :cx="project(p)[0]" :cy="project(p)[1]" r="7" class="cubic-minimum" />
      <circle :cx="handle[0]" :cy="handle[1]" r="7" class="lab-dot-warn" />
      <circle :cx="handle[0]" :cy="handle[1]" r="32" class="lab-handle cubic-hit" tabindex="0" role="slider"
        aria-label="Điểm thử dọc trục" :aria-valuetext="fmtPoint(point,3)" aria-valuemin="-2" aria-valuemax="1"
        @pointerdown="drag.start('point',$event)" @keydown="drag.key('point',[handle[0],-handle[1]],$event)" />
      <text x="20" y="26">Quả cầu trong R³</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button v-for="i in [0,1,2]" :key="i" type="button" :aria-pressed="axis===i" @click="axis=i">Trục x{{i+1}}</button>
      <button type="button" @click="coordinate=0">Gốc thỏa KKT</button>
      <button type="button" @click="coordinate=-0.2">Đi một đoạn âm nhỏ</button>
      <button type="button" @click="coordinate=-2">Nghiệm toàn cục trên trục</button>
    </div>
    <div class="lab-readout" role="status">
      <p>x = {{fmtPoint(point,3)}}. Mục tiêu tổng lập phương = {{fmt(coordinate**3,5)}}. Tổng bình phương = {{fmt(coordinate**2,4)}}, tổng tọa độ = {{fmt(coordinate,4)}}.</p>
      <p v-if="coordinate===0">Tại gốc, gradient bằng 0 và các nhân tử bằng 0 thỏa KKT. Đi sang t âm nhỏ làm mục tiêu giảm ngay.</p>
      <p v-if="coordinate===-2">Điểm đạt cận dưới −8. Nhân tử quả cầu μ = 3, nhân tử tổng λ = 0.</p>
      <p>Ba vòng xanh là ba nghiệm toàn cục. Cận toàn cục trong lời giải còn xét toàn bộ giao của quả cầu và nửa không gian.</p>
    </div>
  </figure>
</template>

<style scoped>
.cubic-sphere { fill: none; stroke: var(--ink-3); stroke-width: 1.2; stroke-dasharray: 4 4; }
.cubic-axis { stroke: var(--tim); stroke-width: 1.7; }
.cubic-minimum { fill: var(--paper); stroke: var(--xanh); stroke-width: 1.8; }
.cubic-hit { fill: transparent !important; stroke: transparent; }
.cubic-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
