<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,makeView} from '../controllers/svg-drag.js'
import {clipSegment} from '../services/svg-clipping.mjs'

const svg=ref(null),end=ref(1.2)
const start=-1
const view=ref(makeView({x0:-2.4,x1:2.4,y0:-0.7,y1:4,width:400,height:320,pad:32}))
const curve=x=>x*x
const points=Array.from({length:81},(_,i)=>{
  const x=-1.95+i*3.9/80
  return view.value.point([x,curve(x)]).join(',')
}).join(' ')
const middle=computed(()=>(start+end.value)/2)
const slope=computed(()=>start+end.value)
const tangent=computed(()=>{
  const y=x=>curve(middle.value)+slope.value*(x-middle.value)
  return clipSegment([[view.value.x0,y(view.value.x0)],[view.value.x1,y(view.value.x1)]],view.value).map(p=>view.value.point(p).join(',')).join(' ')
})
const drag=createDragger(svg,view,(_,p)=>{end.value=Math.max(-0.85,Math.min(1.8,p[0]))},{step:0.05})
</script>

<template>
  <figure class="study-lab" aria-label="Dây cung và tiếp tuyến trong định lý giá trị trung bình">
    <figcaption class="lab-title">Độ dốc trung bình xuất hiện tại một điểm ở giữa</figcaption>
    <p class="lab-lead">Kéo chấm vàng dọc đồ thị f(x) = x². Đoạn tím nối hai đầu mút. Tiếp tuyến xanh nét đứt song song với đoạn tím.</p>
    <svg ref="svg" viewBox="0 0 400 320" role="group" aria-label="Điểm cuối của dây cung kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="32" x2="368" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="32" y2="288" class="lab-axis" />
      <polyline :points="points" class="mean-curve" />
      <polyline :points="tangent" class="mean-tangent" />
      <line :x1="view.sx(start)" :y1="view.sy(curve(start))" :x2="view.sx(end)" :y2="view.sy(curve(end))" class="mean-chord" />
      <circle :cx="view.sx(start)" :cy="view.sy(curve(start))" r="5" class="lab-dot-accent" />
      <circle :cx="view.sx(middle)" :cy="view.sy(curve(middle))" r="5" class="lab-dot-good" />
      <circle :cx="view.sx(end)" :cy="view.sy(curve(end))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(end)" :cy="view.sy(curve(end))" r="32" class="lab-handle mean-hit" tabindex="0" role="slider"
        aria-label="Hoành độ điểm cuối dây cung" :aria-valuetext="fmt(end,3)" :aria-valuenow="end" aria-valuemin="-0.85" aria-valuemax="1.8"
        @pointerdown="drag.start('end',$event)" @keydown="drag.key('end',[end,curve(end)],$event)" />
      <text x="15" y="23">f(x)</text><text x="369" y="307">x</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm cuối bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" @click="end=1">Dây cung nằm ngang</button>
      <button type="button" @click="end=-0.75">Hai đầu mút gần nhau</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Đầu trái ở x₀ = −1. Đầu phải ở x = {{fmt(end,3)}}. Độ dốc dây cung = {{fmt(slope,4)}}.</p>
      <p>Tiếp tuyến tại z = {{fmt(middle,4)}} có độ dốc 2z = {{fmt(2*middle,4)}}. Riêng với hàm bình phương, z là trung điểm.</p>
    </div>
  </figure>
</template>

<style scoped>
.mean-curve { fill: none; stroke: var(--ink-3); stroke-width: 1.5; }
.mean-chord { stroke: var(--tim); stroke-width: 1.7; }
.mean-tangent { fill: none; stroke: var(--xanh); stroke-width: 1.7; stroke-dasharray: 5 4; }
.mean-hit { fill: transparent !important; stroke: transparent; }
.mean-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
