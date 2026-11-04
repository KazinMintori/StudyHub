<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'
import {project3} from '../services/foundation-geometry.mjs'

const resourceSvg=ref(null),pointSvg=ref(null),budget=ref(2),point=ref([1,1])
const camera={yaw:33,pitch:27,scale:62,origin:[190,230]}
const project=p=>project3(p,camera)
const physicalPoint=computed(()=>[point.value[0],point.value[1],3-point.value[0]-point.value[1]].map(v=>v*budget.value/3))
const optimum=computed(()=>budget.value<=2?[budget.value/2,budget.value/2,0]:[(budget.value+1)/3,(budget.value+1)/3,(budget.value-2)/3])
const optimumPlot=computed(()=>project(optimum.value.map(v=>v*3/budget.value)))
const plotted=computed(()=>project([point.value[0],point.value[1],3-point.value[0]-point.value[1]]))
const cost=p=>p[2]+p.reduce((sum,x)=>sum+x*x/2,0)
const lambda=computed(()=>budget.value<=2?-budget.value/2:-(budget.value+1)/3)
const mu3=computed(()=>Math.max(0,1-budget.value/2))
const view=ref(makeView({x0:0,x1:5.5,y0:-1,y1:1,width:400,height:120,pad:36}))
const resourcePoint=computed(()=>[budget.value,0])
const resourceDrag=createDragger(resourceSvg,view,(_,p)=>{budget.value=Math.max(.5,Math.min(5,p[0]))},{step:0.1})
const origin=project([0,0,3]),first=project([1,0,2]),second=project([0,1,2])
const a=first.map((x,i)=>x-origin[i]),b=second.map((x,i)=>x-origin[i]),det=a[0]*b[1]-a[1]*b[0]
const planeView=ref({x0:0,x1:3,y0:0,y1:3,toWorld:(x,y)=>[
  ((x-origin[0])*b[1]-(y-origin[1])*b[0])/det,
  (a[0]*(y-origin[1])-a[1]*(x-origin[0]))/det,
]})
const pointDrag=createDragger(pointSvg,planeView,(_,p)=>{
  point.value=[p[0],Math.max(0,Math.min(3-p[0],p[1]))]
},{step:0.05})
const polygon=[[3,0,0],[0,3,0],[0,0,3]].map(p=>project(p).join(',')).join(' ')
function chooseOptimum(){point.value=optimum.value.slice(0,2).map(v=>v*3/budget.value)}
</script>

<template>
  <figure class="study-lab" aria-label="Phân bổ tài nguyên theo tham số và ràng buộc KKT chặt">
    <figcaption class="lab-title">Tọa độ thứ ba bắt đầu tham gia sau ngưỡng r = 2</figcaption>
    <p class="lab-lead">Kéo r trên thanh phía trên. Trong tam giác, kéo điểm thử màu vàng để đổi phân bổ không âm. Tam giác dùng tọa độ đã chia cho r nên giữ cùng kích thước. Vòng xanh đánh dấu phân bổ tối ưu theo KKT.</p>
    <svg ref="resourceSvg" viewBox="0 0 400 120" role="group" aria-label="Tổng tài nguyên r kéo được"
      @pointermove="resourceDrag.move" @pointerup="resourceDrag.end" @pointercancel="resourceDrag.end" @lostpointercapture="resourceDrag.end">
      <line :x1="view.sx(.5)" :x2="view.sx(5)" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <text x="34" y="24">r = 0,5</text><text x="306" y="24">r = 5</text>
      <circle :cx="view.sx(budget)" :cy="view.sy(0)" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(budget)" :cy="view.sy(0)" r="32" class="lab-handle allocation-hit" tabindex="0" role="slider"
        aria-label="Tài nguyên r" :aria-valuetext="fmt(budget,3)" aria-valuemin="0.5" aria-valuemax="5"
        @pointerdown="resourceDrag.start('r',$event)" @keydown="resourceDrag.key('r',resourcePoint,$event)" />
    </svg>
    <svg ref="pointSvg" viewBox="0 0 400 350" role="group" aria-label="Điểm phân bổ trên đơn hình kéo được"
      @pointermove="pointDrag.move" @pointerup="pointDrag.end" @pointercancel="pointDrag.end" @lostpointercapture="pointDrag.end">
      <polygon :points="polygon" class="allocation-face" />
      <circle :cx="optimumPlot[0]" :cy="optimumPlot[1]" r="10" class="allocation-optimum" />
      <circle :cx="plotted[0]" :cy="plotted[1]" r="7" class="lab-dot-warn" />
      <circle :cx="plotted[0]" :cy="plotted[1]" r="32" class="lab-handle allocation-hit" tabindex="0" role="slider"
        aria-label="Phân bổ thử x trong R3" :aria-valuetext="fmtPoint(physicalPoint,3)" @pointerdown="pointDrag.start('x',$event)" @keydown="pointDrag.key('x',point,$event)" />
      <text x="20" y="25">Đơn hình phân bổ trong R³</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh r bằng nút</summary><LabPointControls :svg="resourceSvg" axes="x" /></details>
    <details class="lab-tasks"><summary>Điều chỉnh phân bổ bằng nút</summary><LabPointControls :svg="pointSvg" /></details>
    <div class="lab-buttons">
      <button type="button" @click="budget=1;chooseOptimum()">r = 1</button>
      <button type="button" @click="budget=2;chooseOptimum()">r = 2</button>
      <button type="button" @click="budget=3;chooseOptimum()">r = 3</button>
      <button type="button" @click="chooseOptimum">Đưa điểm thử về nghiệm</button>
    </div>
    <div class="lab-readout" role="status">
      <p>x thử = {{fmtPoint(physicalPoint,4)}}, mục tiêu {{fmt(cost(physicalPoint),4)}}. x tối ưu = {{fmtPoint(optimum,4)}}, mục tiêu {{fmt(cost(optimum),4)}}.</p>
      <p>Nhân tử đẳng thức λ = {{fmt(lambda,4)}}. Hai nhân tử đầu bằng 0, nhân tử thứ ba μ₃ = {{fmt(mu3,4)}}.</p>
      <p v-if="budget===2">Tại r = 2, x₃ = 0 và μ₃ = 0. Ràng buộc chặt vẫn có thể có nhân tử bằng 0.</p>
      <p v-else>{{budget<2?'Nghiệm tối ưu nằm trên cạnh x₃ = 0.':'Nghiệm tối ưu có cả ba tọa độ dương.'}}</p>
    </div>
  </figure>
</template>

<style scoped>
.allocation-face { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.5; }
.allocation-optimum { fill: var(--paper); stroke: var(--xanh); stroke-width: 1.8; }
.allocation-hit { fill: transparent !important; stroke: transparent; }
.allocation-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
