<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'
import {clipSegment} from '../services/svg-clipping.mjs'

const rawSvg=ref(null),centeredSvg=ref(null),slope=ref(0)
const samples=[[0,1],[1,2],[2,2]]
const mean=[1,5/3]
const raw=makeView({x0:-0.5,x1:2.5,y0:-0.5,y1:3.8,width:400,height:320,pad:34})
const centered=makeView({x0:-1.5,x1:1.5,y0:-2.65,y1:1.65,width:400,height:320,pad:34})
const slopeView=ref({x0:0,x1:0,y0:-0.8,y1:1.4,toWorld:()=>[0,0]})
function slopeControls(svg,canvas,pivotY){
  const view=computed(()=>({...slopeView.value,toWorld:(_,y)=>[0,canvas.wy(y)-pivotY]}))
  return createDragger(svg,view,(_,point)=>{slope.value=point[1]},{step:0.05})
}
const rawDrag=slopeControls(rawSvg,raw,mean[1])
const centeredDrag=slopeControls(centeredSvg,centered,0)
const intercept=computed(()=>mean[1]-slope.value*mean[0])
const residuals=computed(()=>samples.map(([x,y])=>slope.value*x+intercept.value-y))
const loss=computed(()=>residuals.value.reduce((sum,value)=>sum+value*value,0)/3)
const panels=computed(()=>[
  {id:'raw',view:raw,drag:rawDrag,title:'Dữ liệu gốc',origin:mean,points:samples},
  {id:'centered',view:centered,drag:centeredDrag,title:'Đã trừ trung bình',origin:[0,0],points:samples.map(([x,y])=>[x-mean[0],y-mean[1]])},
].map(panel=>{
  const {view,origin}=panel
  const value=x=>origin[1]+slope.value*(x-origin[0])
  const segment=clipSegment([[view.x0,value(view.x0)],[view.x1,value(view.x1)]],view)
  return {...panel,drawnLine:segment.map(p=>view.point(p)),value,handle:view.point([origin[0]+1,value(origin[0]+1)])}
}))
function attach(id,element){(id==='raw'?rawSvg:centeredSvg).value=element}
</script>

<template>
  <figure class="study-lab" aria-label="Trừ trung bình và khử hệ số chặn trong hồi quy">
    <figcaption class="lab-title">Mỗi hệ số góc có một hệ số chặn tối ưu</figcaption>
    <p class="lab-lead">Kéo chấm vàng lên hoặc xuống trong một trong hai hình. Ở hình dữ liệu gốc, đường khớp luôn đi qua điểm trung bình màu xanh. Sau khi trừ trung bình, điểm đó chuyển về gốc. Các đoạn tím nét đứt đo phần dư theo phương đứng.</p>
    <div class="lab-pair">
      <svg v-for="panel in panels" :key="panel.id" :ref="element=>attach(panel.id,element)" viewBox="0 0 400 320"
        role="group" :aria-label="panel.title" @pointermove="panel.drag.move" @pointerup="panel.drag.end"
        @pointercancel="panel.drag.end" @lostpointercapture="panel.drag.end">
        <line x1="34" x2="366" :y1="panel.view.sy(0)" :y2="panel.view.sy(0)" class="lab-axis" />
        <line :x1="panel.view.sx(0)" :x2="panel.view.sx(0)" y1="34" y2="286" class="lab-axis" />
        <line :x1="panel.drawnLine[0][0]" :y1="panel.drawnLine[0][1]" :x2="panel.drawnLine[1][0]" :y2="panel.drawnLine[1][1]" class="centered-line" />
        <g v-for="([x,y],i) in panel.points" :key="i">
          <line :x1="panel.view.sx(x)" :x2="panel.view.sx(x)" :y1="panel.view.sy(y)" :y2="panel.view.sy(panel.value(x))" class="centered-residual" />
          <circle :cx="panel.view.sx(x)" :cy="panel.view.sy(y)" r="5" class="lab-dot" />
        </g>
        <circle :cx="panel.view.sx(panel.origin[0])" :cy="panel.view.sy(panel.origin[1])" r="7" class="centered-mean" />
        <circle :cx="panel.handle[0]" :cy="panel.handle[1]" r="7" class="lab-dot-warn" />
        <circle :cx="panel.handle[0]" :cy="panel.handle[1]" r="31" class="lab-handle centered-hit" tabindex="0" role="slider"
          :aria-label="'Hệ số góc, '+panel.title" :aria-valuetext="fmt(slope,3)" :aria-valuenow="slope" aria-valuemin="-0.8" aria-valuemax="1.4"
          @pointerdown="panel.drag.start('slope',$event)" @keydown="panel.drag.key('slope',[0,slope],$event)" />
        <text x="18" y="24">{{panel.title}}</text><text x="369" y="307">x</text>
      </svg>
    </div>
    <details class="lab-tasks"><summary>Điều chỉnh ở hình dữ liệu gốc</summary><LabPointControls :svg="rawSvg" axes="y" /></details>
    <details class="lab-tasks"><summary>Điều chỉnh ở hình đã trừ trung bình</summary><LabPointControls :svg="centeredSvg" axes="y" /></details>
    <div class="lab-buttons">
      <button type="button" @click="slope=0">Đường nằm ngang</button>
      <button type="button" @click="slope=0.5">Hệ số góc tối ưu</button>
      <button type="button" @click="slope=1">Hệ số góc bằng 1</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Hệ số góc a₁ = {{fmt(slope,4)}}. Hệ số chặn a₀ = 5/3 − a₁ = {{fmt(intercept,4)}}.</p>
      <p>Phần dư dự đoán trừ quan sát là {{fmtPoint(residuals,4)}} ở cả hai hình. Mất mát bình phương trung bình = {{fmt(loss,6)}}.</p>
      <p>Tổng phần dư bằng 0. Đây là điều kiện tối ưu theo hệ số chặn khi giữ hệ số góc cố định. Để tối ưu cả hai hệ số, chọn a₁ = 0,5.</p>
    </div>
  </figure>
</template>

<style scoped>
.centered-line { stroke: var(--xanh); stroke-width: 1.6; }
.centered-residual { stroke: var(--tim); stroke-width: 1.4; stroke-dasharray: 4 4; }
.centered-mean { fill: var(--paper); stroke: var(--xanh); stroke-width: 1.8; }
.centered-hit { fill: transparent !important; stroke: transparent; }
.centered-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
