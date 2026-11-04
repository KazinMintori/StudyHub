<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'
import {clipSegment} from '../services/svg-clipping.mjs'

const svg=ref(null),time=ref(0.5)
const input=makeView({x0:0.5,x1:2.5,y0:-0.2,y1:1.8,width:400,height:340,pad:36})
const output=makeView({x0:-0.2,x1:1.2,y0:-1,y1:7,width:400,height:340,pad:36})
const point=t=>[1+t,t*t]
const value=t=>(1+t)**2+2*t**4
const path=Array.from({length:81},(_,i)=>input.point(point(i/80)).join(',')).join(' ')
const graph=Array.from({length:81},(_,i)=>output.point([i/80,value(i/80)]).join(',')).join(' ')
const position=computed(()=>point(time.value))
const slope=computed(()=>2*(1+time.value)+8*time.value**3)
const velocity=computed(()=>[1,2*time.value])
const gradient=computed(()=>[2*position.value[0],4*position.value[1]])
const contributions=computed(()=>gradient.value.map((g,i)=>g*velocity.value[i]))
const view=ref(output)
const drag=createDragger(svg,view,(_,p)=>{time.value=Math.max(0,Math.min(1,p[0]))},{step:0.025})
const tangent=computed(()=>{
  const y=t=>value(time.value)+slope.value*(t-time.value)
  return clipSegment([[0,y(0)],[1,y(1)]],output).map(p=>output.point(p).join(',')).join(' ')
})
</script>

<template>
  <figure class="study-lab" aria-label="Quy tắc chuỗi dọc đường cong có hai tọa độ">
    <figcaption class="lab-title">Hai nhánh tọa độ cùng đóng góp vào tốc độ đổi mục tiêu</figcaption>
    <p class="lab-lead">Đường đi có φ(t) = (1 + t, t²), với 0 ≤ t ≤ 1. Hàm mục tiêu là f(x, y) = x² + 2y². Kéo điểm vàng ở đồ thị g(t) phía sau để theo dõi vị trí trên đường đi và tiếp tuyến của g.</p>
    <div class="lab-pair">
      <svg viewBox="0 0 400 340" role="img" aria-label="Đường đi của hai tọa độ x và y">
        <polyline :points="path" class="chain-path" />
        <circle :cx="input.sx(position[0])" :cy="input.sy(position[1])" r="7" class="lab-dot-warn" />
        <text x="20" y="26">Đường φ(t) trong R²</text>
        <text x="368" y="326">x</text><text x="12" y="50">y</text>
      </svg>
      <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Tham số t kéo được trên đồ thị mục tiêu dọc đường"
        @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
        <line x1="36" x2="364" :y1="output.sy(0)" :y2="output.sy(0)" class="lab-axis" />
        <line :x1="output.sx(0)" :x2="output.sx(0)" y1="36" y2="304" class="lab-axis" />
        <polyline :points="graph" class="chain-value" />
        <polyline :points="tangent" class="chain-tangent" />
        <circle :cx="output.sx(time)" :cy="output.sy(value(time))" r="7" class="lab-dot-warn" />
        <circle :cx="output.sx(time)" :cy="output.sy(value(time))" r="32" class="lab-handle chain-hit" tabindex="0" role="slider"
          aria-label="Tham số đường đi t" :aria-valuetext="fmt(time,3)" aria-valuemin="0" aria-valuemax="1"
          @pointerdown="drag.start('t',$event)" @keydown="drag.key('t',[time,value(time)],$event)" />
        <text x="20" y="26">g(t) = f(φ(t))</text><text x="369" y="327">t</text>
      </svg>
    </div>
    <details class="lab-tasks"><summary>Điều chỉnh t bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" @click="time=0">t = 0</button>
      <button type="button" @click="time=0.5">t = 0,5</button>
      <button type="button" @click="time=1">t = 1</button>
    </div>
    <div class="lab-readout" role="status">
      <p>t = {{fmt(time,3)}}, φ(t) = {{fmtPoint(position,3)}}. Vận tốc φ′ = {{fmtPoint(velocity,3)}}.</p>
      <p>Gradient tại φ(t) = {{fmtPoint(gradient,3)}}.</p>
      <p>Nhánh x góp {{fmt(contributions[0],4)}}, nhánh y góp {{fmt(contributions[1],4)}}. Tổng g′(t) = {{fmt(slope,4)}}.</p>
      <p>Khai triển trực tiếp cho g(t) = (1 + t)² + 2t⁴ và g′(t) = 2(1 + t) + 8t³, cùng kết quả với quy tắc chuỗi.</p>
    </div>
  </figure>
</template>

<style scoped>
.chain-path { stroke: var(--xanh); fill: none; stroke-width: 1.8; }
.chain-value { stroke: var(--tim); fill: none; stroke-width: 1.8; }
.chain-tangent { stroke: var(--ink-3); fill: none; stroke-width: 1.4; stroke-dasharray: 4 4; }
.chain-hit { fill: transparent !important; stroke: transparent; }
.chain-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
