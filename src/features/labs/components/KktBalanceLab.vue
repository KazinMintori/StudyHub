<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'

const svg=ref(null),target=ref([1.6,1.2])
const halfHeight=(350-64)/(2*((400-64)/6))
const view=ref(makeView({x0:-3,x1:3,y0:-halfHeight,y1:halfHeight,width:400,height:350,pad:32}))
const norm=computed(()=>Math.hypot(...target.value))
const optimum=computed(()=>norm.value>1?target.value.map(value=>value/norm.value):target.value)
const multiplier=computed(()=>Math.max(0,(norm.value-1)/2))
const gradient=computed(()=>optimum.value.map((value,i)=>value-target.value[i]))
const contribution=computed(()=>optimum.value.map(value=>2*multiplier.value*value))
const drag=createDragger(svg,view,(_,point)=>{
  target.value=[Math.max(-2.2,Math.min(2.2,point[0])),Math.max(-1.8,Math.min(1.8,point[1]))]
},{step:0.05})
const objective=computed(()=>gradient.value.reduce((sum,value)=>sum+value*value,0)/2)
</script>

<template>
  <figure class="study-lab" aria-label="Cân bằng gradient KKT trên đĩa đơn vị">
    <figcaption class="lab-title">Hai gradient cân bằng tại nghiệm nằm trên biên</figcaption>
    <p class="lab-lead">Cực tiểu hóa nửa bình phương khoảng cách từ x tới c trên đĩa đơn vị. Kéo đích c màu vàng. Vòng xanh đánh dấu nghiệm gần c nhất. Đoạn đỏ từ nghiệm tới đích biểu diễn hướng ngược gradient mục tiêu.</p>
    <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Đích c kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="32" x2="368" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="32" y2="318" class="lab-axis" />
      <circle :cx="view.sx(0)" :cy="view.sy(0)" :r="view.sx(1)-view.sx(0)" class="balance-disk" />
      <line :x1="view.sx(optimum[0])" :y1="view.sy(optimum[1])" :x2="view.sx(target[0])" :y2="view.sy(target[1])" class="balance-gradient" />
      <circle :cx="view.sx(optimum[0])" :cy="view.sy(optimum[1])" r="10" class="balance-optimum" />
      <circle :cx="view.sx(target[0])" :cy="view.sy(target[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(target[0])" :cy="view.sy(target[1])" r="32" class="lab-handle balance-hit" tabindex="0" role="slider"
        aria-label="Đích c của bài toán khoảng cách" :aria-valuetext="fmtPoint(target,3)"
        @pointerdown="drag.start('c',$event)" @keydown="drag.key('c',target,$event)" />
      <text x="14" y="24">x₂</text><text x="367" y="336">x₁</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh c bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" @click="target=[1.6,1.2]">Đích ở ngoài đĩa</button>
      <button type="button" @click="target=[0.3,0.4]">Đích ở trong đĩa</button>
      <button type="button" @click="target=[0.6,0.8]">Đích ngay trên biên</button>
    </div>
    <div class="lab-readout" role="status">
      <p>c = {{fmtPoint(target,3)}}. x tối ưu = {{fmtPoint(optimum,3)}}. Giá trị mục tiêu = {{fmt(objective,4)}}.</p>
      <p>Với g(x) = ‖x‖² − 1, nhân tử μ = {{fmt(multiplier,4)}}. Gradient mục tiêu = {{fmtPoint(gradient,4)}}. Đóng góp μ∇g = {{fmtPoint(contribution,4)}}.</p>
      <p>Tổng hai vector = {{fmtPoint(gradient.map((value,i)=>value+contribution[i]),4)}}. Tích μg(x) = {{fmt(multiplier*(optimum[0]**2+optimum[1]**2-1),4)}}.</p>
    </div>
  </figure>
</template>

<style scoped>
.balance-disk { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.5; }
.balance-gradient { stroke: var(--do); stroke-width: 1.7; }
.balance-optimum { fill: var(--paper); stroke: var(--xanh); stroke-width: 1.8; }
.balance-hit { fill: transparent !important; stroke: transparent; }
.balance-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
