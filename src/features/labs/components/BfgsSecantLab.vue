<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'

const svg=ref(null),step=ref([1,0.75]),curvature=ref(2)
const view=ref(makeView({x0:-3.4,x1:3.4,y0:-3.4,y1:3.4,width:400,height:350,pad:34}))
const change=computed(()=>[step.value[0],curvature.value*step.value[1]])
const product=computed(()=>step.value[0]*change.value[0]+step.value[1]*change.value[1])
const updated=computed(()=>{
  if(product.value<=1e-10)return null
  const s=step.value,y=change.value,rho=1/product.value
  const factor=s.map((si,i)=>y.map((yj,j)=>Number(i===j)-rho*si*yj))
  const matrix=factor.map((row,i)=>factor.map((other,j)=>row[0]*other[0]+row[1]*other[1]+rho*s[i]*s[j]))
  return matrix.map(row=>row[0]*y[0]+row[1]*y[1])
})
const drag=createDragger(svg,view,(_,point)=>{
  step.value=point.map(x=>Math.max(-1.4,Math.min(1.4,x)))
},{step:0.05})
</script>

<template>
  <figure class="study-lab" aria-label="Điều kiện độ cong và cập nhật cát tuyến BFGS">
    <figcaption class="lab-title">BFGS lấy thông tin độ cong từ hai gradient</figcaption>
    <p class="lab-lead">Với f(x₁, x₂) = (x₁² + c·x₂²)/2, kéo đầu mút vàng của bước s. Đoạn tím nét đứt nối gốc đến đầu mút vuông, biểu diễn độ đổi gradient y. Thử đổi dấu c và kéo theo trục dọc.</p>
    <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Đầu mút của bước s kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="34" x2="366" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="34" y2="316" class="lab-axis" />
      <line :x1="view.sx(0)" :y1="view.sy(0)" :x2="view.sx(change[0])" :y2="view.sy(change[1])" class="secant-change" />
      <line :x1="view.sx(0)" :y1="view.sy(0)" :x2="view.sx(step[0])" :y2="view.sy(step[1])" class="secant-step" />
      <rect :x="view.sx(change[0])-5" :y="view.sy(change[1])-5" width="10" height="10" class="secant-end" />
      <circle :cx="view.sx(step[0])" :cy="view.sy(step[1])" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(step[0])" :cy="view.sy(step[1])" r="32" class="lab-handle secant-hit" tabindex="0" role="slider"
        aria-label="Bước s của BFGS" :aria-valuetext="fmtPoint(step)" @pointerdown="drag.start('s',$event)" @keydown="drag.key('s',step,$event)" />
      <text x="11" y="24">Tọa độ 2</text><text x="300" y="338">Tọa độ 1</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bước s bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="curvature===2" @click="curvature=2">c = 2</button>
      <button type="button" :aria-pressed="curvature===0" @click="curvature=0">c = 0</button>
      <button type="button" :aria-pressed="curvature===-2" @click="curvature=-2">c = −2</button>
      <button type="button" @click="step=[0,1]">Bước dọc</button>
      <button type="button" @click="step=[1,0]">Bước ngang</button>
    </div>
    <div class="lab-readout" role="status">
      <p>s = {{fmtPoint(step)}}. y = {{fmtPoint(change)}}. yᵀs = {{fmt(product,4)}}.</p>
      <p v-if="updated">Từ M = I, phép cập nhật cho M mới nhân y bằng {{fmtPoint(updated,4)}}, trùng với s đến sai số làm tròn.</p>
      <p v-else>Điều kiện độ cong dương không đạt ở độ chính xác đang dùng. Mô phỏng giữ ma trận ban đầu.</p>
    </div>
  </figure>
</template>

<style scoped>
.secant-change { stroke: var(--tim); stroke-width: 1.8; stroke-dasharray: 4 4; }
.secant-step { stroke: var(--vang); stroke-width: 1.6; }
.secant-end { fill: var(--tim); }
.secant-hit { fill: transparent !important; stroke: transparent; }
.secant-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
