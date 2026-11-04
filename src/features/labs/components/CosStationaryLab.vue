<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,makeView} from '../controllers/svg-drag.js'

const svg=ref(null),probe=ref(0.7)
const view=ref(makeView({x0:-2.3,x1:2.3,y0:-4,y1:4,width:400,height:340,pad:36}))
const curve=Array.from({length:121},(_,i)=>{
  const x=-2+i/30
  return view.value.point([x,Math.sin(x)]).join(',')
}).join(' ')
const derivative=computed(()=>7*probe.value/4-Math.sin(probe.value))
const reduced=computed(()=>7*probe.value**2/8+Math.cos(probe.value))
const drag=createDragger(svg,view,(_,p)=>{
  probe.value=Math.max(-1.8,Math.min(1.8,p[0]))
},{step:0.05})
</script>

<template>
  <figure class="study-lab" aria-label="Phương trình điểm dừng của bài toán có cos">
    <figcaption class="lab-title">Điểm giao của sin x và đường thẳng 7x/4</figcaption>
    <p class="lab-lead">Sau khi khử hai biến còn lại, mục tiêu là F(x) = 7x²/8 + cos x. Kéo điểm vàng dọc đường sin. Đoạn đứng nối tới đường tím cho thấy độ lệch giữa hai vế của phương trình điểm dừng.</p>
    <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Hoành độ x kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="36" x2="364" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="36" y2="304" class="lab-axis" />
      <polyline :points="curve" class="cos-sine" />
      <line :x1="view.sx(-2)" :y1="view.sy(-3.5)" :x2="view.sx(2)" :y2="view.sy(3.5)" class="cos-linear" />
      <line :x1="view.sx(probe)" :x2="view.sx(probe)" :y1="view.sy(Math.sin(probe))" :y2="view.sy(7*probe/4)" class="cos-gap" />
      <circle :cx="view.sx(probe)" :cy="view.sy(Math.sin(probe))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(probe)" :cy="view.sy(Math.sin(probe))" r="32" class="lab-handle cos-hit" tabindex="0" role="slider"
        aria-label="Hoành độ x của bài toán cos" :aria-valuetext="fmt(probe,3)" aria-valuemin="-1.8" aria-valuemax="1.8"
        @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',[probe,Math.sin(probe)],$event)" />
      <text x="16" y="25">Giá trị</text><text x="367" y="328">x</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh x bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" @click="probe=0">Điểm dừng tại 0</button>
      <button type="button" @click="probe=1">Thử x = 1</button>
      <button type="button" @click="probe=-1">Thử x = −1</button>
    </div>
    <div class="lab-readout" role="status">
      <p>x = {{fmt(probe,4)}}. Đạo hàm F′ = 7x/4 − sin x = {{fmt(derivative,5)}}. F(x) = {{fmt(reduced,5)}}.</p>
      <p>Đạo hàm bậc hai tại x là {{fmt(1.75-Math.cos(probe),5)}} và luôn ít nhất 3/4 trên toàn trục số.</p>
      <p>Bất đẳng thức |sin x| ≤ |x| cho thấy hai đường chỉ cắt nhau tại 0 vì 7/4 lớn hơn 1.</p>
    </div>
  </figure>
</template>

<style scoped>
.cos-sine { stroke: var(--xanh); fill: none; stroke-width: 1.8; }
.cos-linear { stroke: var(--tim); stroke-width: 1.8; }
.cos-gap { stroke: var(--ink-3); stroke-width: 1.4; stroke-dasharray: 4 3; }
.cos-hit { fill: transparent !important; stroke: transparent; }
.cos-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
