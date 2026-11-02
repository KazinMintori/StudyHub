<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import MathMatrix from '../../../core/math/components/MathMatrix.vue'
import {makeView,createDragger,fmt} from '../controllers/svg-drag.js'
const svg=ref(null),t=ref(.3),limit=1/Math.sqrt(2)
const view=ref(makeView({x0:-.9,x1:.9,y0:-4.2,y1:.4,width:400,height:300,pad:32}))
const determinant=computed(()=>1-2*t.value*t.value)
const positive=computed(()=>Math.abs(t.value)<limit-1e-10)
const singular=computed(()=>Math.abs(Math.abs(t.value)-limit)<1e-10)
const value=computed(()=>positive.value?Math.log(determinant.value):null)
const matrix=computed(()=>[[1+t.value,t.value],[t.value,1-t.value]])
const eigen=computed(()=>[1+Math.SQRT2*t.value,1-Math.SQRT2*t.value])
const plotY=computed(()=>value.value===null?0:Math.max(view.value.y0,value.value))
const curve=Array.from({length:241},(_,i)=>{const x=-limit+.006+(2*limit-.012)*i/240;return view.value.point([x,Math.log(1-2*x*x)]).join(',')}).join(' ')
const drag=createDragger(svg,view,(_,p)=>{t.value=p[0]},{step:.025})
</script>
<template>
 <figure class="study-lab" aria-label="Log định thức và hình ellipse của ma trận xác định dương">
  <figcaption class="lab-title">Log det: Đi tới biên xác định dương thì một bán trục co về 0</figcaption>
  <p class="lab-lead">X(t) = I + tV với V có hai trị riêng ±√2. Kéo điểm trên đồ thị theo trục t. Khung ellipse biểu diễn xᵀX(t)⁻¹x ≤ 1, vì vậy bán trục là căn bậc hai của trị riêng X.</p>
  <div class="lab-pair">
   <svg viewBox="0 0 400 300" role="img" aria-label="Ellipse có ma trận hình dạng X và hai bán trục chính">
    <line x1="45" x2="355" y1="150" y2="150" class="lab-axis"/><line x1="200" x2="200" y1="25" y2="275" class="lab-axis"/>
    <circle cx="200" cy="150" r="80" class="unit"/>
    <g v-if="positive||singular" transform="rotate(-22.5 200 150)"><ellipse cx="200" cy="150" :rx="80*Math.sqrt(Math.max(0,eigen[0]))" :ry="80*Math.sqrt(Math.max(0,eigen[1]))" class="lab-region"/><line :x1="200-80*Math.sqrt(Math.max(0,eigen[0]))" :x2="200+80*Math.sqrt(Math.max(0,eigen[0]))" y1="150" y2="150" class="lab-accent"/><line x1="200" x2="200" :y1="150-80*Math.sqrt(Math.max(0,eigen[1]))" :y2="150+80*Math.sqrt(Math.max(0,eigen[1]))" class="lab-good"/></g>
    <text v-else x="200" y="145" text-anchor="middle">X không xác định dương</text><text x="200" y="284" text-anchor="middle">{{singular?'Ellipse giới hạn suy biến':positive?'Ellipse hình dạng X':'Không vẽ ellipse bằng căn trị riêng âm'}}</text>
   </svg>
   <svg ref="svg" viewBox="0 0 400 300" role="group" aria-label="Hàm lõm log của một trừ hai t bình phương trên miền xác định" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <line x1="32" x2="368" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis"/>
    <line v-for="x in [-limit,limit]" :key="x" :x1="view.sx(x)" :x2="view.sx(x)" y1="32" y2="268" class="lab-guide"/>
    <polyline :points="curve" class="lab-accent"/><circle :cx="view.sx(t)" :cy="view.sy(plotY)" r="8" :class="positive?'lab-dot-accent':'lab-dot-bad'"/><circle :cx="view.sx(t)" :cy="view.sy(plotY)" r="28" class="lab-handle hit" tabindex="0" role="slider" aria-label="Tham số t của ma trận X" :aria-valuetext="fmt(t,4)" @pointerdown="drag.start('t',$event)" @keydown="drag.key('t',[t,plotY],$event)"/>
    <text x="200" y="28" text-anchor="middle">g(t) = log det X(t)</text><text x="200" y="290" text-anchor="middle">−1/√2 &lt; t &lt; 1/√2</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-buttons"><button type="button" @click="t=0">Ma trận đơn vị</button><button type="button" @click="t=.5">t = 1/2</button><button type="button" @click="t=limit">Chạm biên PSD</button><button type="button" @click="t=.85">Ra ngoài miền</button></div>
  <div class="lab-readout" role="status"><MathMatrix :rows="matrix.map(row=>row.map(v=>Number(v.toFixed(4))))" label="Ma trận X đối xứng phụ thuộc tham số t"/><p>t = {{fmt(t,4)}}, trị riêng {{eigen.map(v=>fmt(v,4)).join(' và ')}}, det X = {{fmt(determinant,6)}}.</p><p v-if="positive">log det X = {{fmt(value,6)}}. Diện tích ellipse chia diện tích hình tròn đơn vị bằng √det X = {{fmt(Math.sqrt(determinant),6)}}. Khi t tiến tới biên từ phía trong, log det tiến tới −∞.</p><p v-else class="is-bad">{{singular?'X nửa xác định dương nhưng suy biến, det X = 0.':'X có một trị riêng âm.'}} Hàm log det trên miền ma trận xác định dương không xác định ở đây. Điểm kéo được đặt trên trục ngang để bạn đưa t trở lại, không phải giá trị g(t).</p><p>Đường tròn nét đứt là trường hợp X = I để so kích thước. Vượt miền của log det không biến thành một phần đồ thị mới.</p></div>
 </figure>
</template>
<style scoped>
svg text{font-size:19px;pointer-events:none}.unit{fill:none;stroke:var(--ink-3);stroke-width:1;stroke-dasharray:4 4}svg :is(line,ellipse,polyline),svg circle:not(.hit){pointer-events:none}.hit{fill:transparent!important;stroke:transparent}.hit:focus-visible{stroke:var(--vang)}
</style>
