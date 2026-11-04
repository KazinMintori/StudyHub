<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'

const svg=ref(null),point=ref([1/3,1]),frame=ref(makeView({x0:-1.2,x1:2.4,y0:-0.8,y1:2.8,width:400,height:350,pad:36}))
const residuals=computed(()=>[point.value[0]+2*point.value[1]-3,2*point.value[0]+point.value[1]-1,point.value[0]-point.value[1]])
const sum=computed(()=>residuals.value.reduce((value,r)=>value+Math.abs(r),0))
const maximum=computed(()=>Math.max(...residuals.value.map(Math.abs)))
const drag=createDragger(svg,frame,(_,p)=>{point.value=[Math.max(-1,Math.min(2,p[0])),Math.max(-0.5,Math.min(2.5,p[1]))]},{step:0.05})
const triangle=[[-1/3,5/3],[1,1],[1/3,1/3]]
const polygon=triangle.map(p=>frame.value.point(p).join(',')).join(' ')
const bars=makeView({x0:-0.6,x1:2.6,y0:-5.5,y1:6.5,width:400,height:350,pad:36})
</script>

<template>
  <figure class="study-lab" aria-label="So sánh tổng sai số tuyệt đối với sai số cực đại">
    <figcaption class="lab-title">Cùng ba phần dư, hai cách chọn nghiệm tối ưu</figcaption>
    <p class="lab-lead">Ví dụ có ba phần dư x₁ + 2x₂ − 3, 2x₁ + x₂ − 1 và x₁ − x₂. Kéo điểm vàng trong mặt phẳng tham số. Hình bên cạnh cho thấy từng phần dư có dấu. Tam giác xanh gồm các nghiệm đạt tổng sai số tuyệt đối nhỏ nhất.</p>
    <div class="lab-pair">
      <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Vector tham số hai chiều kéo được"
        @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
        <line x1="36" x2="364" :y1="frame.sy(0)" :y2="frame.sy(0)" class="lab-axis" />
        <line :x1="frame.sx(0)" :x2="frame.sx(0)" y1="36" y2="314" class="lab-axis" />
        <polygon :points="polygon" class="norm-optimal" />
        <circle :cx="frame.sx(1/3)" :cy="frame.sy(1)" r="8" class="norm-infinity" />
        <circle :cx="frame.sx(point[0])" :cy="frame.sy(point[1])" r="7" class="lab-dot-warn" />
        <circle :cx="frame.sx(point[0])" :cy="frame.sy(point[1])" r="32" class="lab-handle norm-hit" tabindex="0" role="slider"
          aria-label="Tham số x của xấp xỉ chuẩn" :aria-valuetext="fmtPoint(point)" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',point,$event)" />
        <text x="12" y="25">x₂</text><text x="365" y="337">x₁</text>
      </svg>
      <svg viewBox="0 0 400 350" role="img" aria-label="Ba phần dư dương hoặc âm">
        <line x1="36" x2="364" :y1="bars.sy(0)" :y2="bars.sy(0)" class="lab-axis" />
        <g v-for="(r,i) in residuals" :key="i">
          <line :x1="bars.sx(i)" :x2="bars.sx(i)" :y1="bars.sy(0)" :y2="bars.sy(r)" class="norm-residual" />
          <circle :cx="bars.sx(i)" :cy="bars.sy(r)" r="5" class="lab-dot-accent" />
          <text :x="bars.sx(i)" y="336" text-anchor="middle">r{{i+1}}</text>
          <text :x="bars.sx(i)" y="27" text-anchor="middle">{{fmt(r,2)}}</text>
        </g>
      </svg>
    </div>
    <details class="lab-tasks"><summary>Điều chỉnh tham số bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" @click="point=[1/3,1]">Nghiệm chuẩn cực đại</button>
      <button type="button" @click="point=[1,1]">Một đỉnh nghiệm L₁</button>
      <button type="button" @click="point=[1/3,1/3]">Một đỉnh L₁ khác</button>
      <button type="button" @click="point=[1/3,7/9]">Điểm trong tam giác L₁</button>
    </div>
    <div class="lab-readout" role="status">
      <p>x = {{fmtPoint(point,4)}}, r = {{fmtPoint(residuals,4)}}.</p>
      <p>Tổng |r₁| + |r₂| + |r₃| = {{fmt(sum,4)}}. Sai số cực đại = {{fmt(maximum,4)}}.</p>
      <p>Với mọi x, ta có r₁ − r₂ + r₃ = −2. Do đó tổng sai số tuyệt đối ít nhất 2 và sai số cực đại ít nhất 2/3. Hình minh họa các điểm đạt hai cận này.</p>
    </div>
  </figure>
</template>

<style scoped>
.norm-optimal { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.4; }
.norm-infinity { fill: var(--paper); stroke: var(--tim); stroke-width: 1.7; }
.norm-residual { stroke: var(--tim); stroke-width: 1.8; }
.norm-hit { fill: transparent !important; stroke: transparent; }
.norm-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
