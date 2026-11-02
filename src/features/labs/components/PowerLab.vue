<script setup>
import {computed,ref,useId} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {makeView,createDragger,fmt} from '../controllers/svg-drag.js'
const a=ref(.5),svg=ref(null),clip=useId()+'-power'
const graph=makeView({x0:0,x1:3,y0:-.4,y1:4,width:400,height:300,pad:28})
const view=ref(makeView({x0:-2,x1:3,y0:-.6,y1:6.5,width:400,height:300,pad:28}))
const f=x=>x**a.value,curvature=computed(()=>a.value*(a.value-1))
const curve=computed(()=>Array.from({length:600},(_,i)=>{const x=.005+2.995*i/599;return [x,f(x)]}).filter(p=>p[1]>=graph.y0&&p[1]<=graph.y1).map(p=>graph.point(p).join(',')).join(' '))
const parabola=Array.from({length:201},(_,i)=>{const t=-2+5*i/200;return view.value.point([t,t*(t-1)]).join(',')}).join(' ')
const u=.4,v=2.6,mid=1.5,gap=computed(()=>(f(u)+f(v))/2-f(mid))
const kind=computed(()=>Math.abs(curvature.value)<1e-10?'Vừa lồi vừa lõm':curvature.value>0?'Lồi':'Lõm')
const drag=createDragger(svg,view,(_,p)=>{a.value=p[0]},{step:.1})
</script>
<template>
 <figure class="study-lab" aria-label="Họ hàm lũy thừa x mũ a trên nửa trục dương">
  <figcaption class="lab-title">Lũy thừa xᵃ: Lồi hay lõm tùy số mũ</figcaption>
  <p class="lab-lead">Kéo điểm trên đồ thị a(a − 1) để đổi số mũ a. Hai khung xếp dọc trên điện thoại: Một khung cho hàm, một khung cho dấu đạo hàm bậc hai.</p>
  <div class="lab-pair">
   <svg viewBox="0 0 400 300" role="img" aria-label="Đồ thị lũy thừa và dây cung nối hai đầu vào cố định">
    <defs><clipPath :id="clip"><rect x="0" y="0" width="400" height="300"/></clipPath></defs>
    <line x1="28" x2="372" :y1="graph.sy(0)" :y2="graph.sy(0)" class="lab-axis"/>
    <g :clip-path="`url(#${clip})`"><polyline :points="curve" class="lab-line"/><line :x1="graph.sx(u)" :y1="graph.sy(f(u))" :x2="graph.sx(v)" :y2="graph.sy(f(v))" class="lab-accent"/><line :x1="graph.sx(mid)" :x2="graph.sx(mid)" :y1="graph.sy(f(mid))" :y2="graph.sy((f(u)+f(v))/2)" :class="gap>=0?'lab-good':'lab-bad'"/></g>
    <text x="35" y="28">f(x) = xᵃ</text><text :x="graph.sx(1)" y="289">1</text><text :x="graph.sx(2)" y="289">2</text>
   </svg>
   <svg ref="svg" viewBox="0 0 400 300" role="group" aria-label="Parabol của hệ số a nhân a trừ 1 với điểm số mũ kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <rect :x="view.sx(0)" y="28" :width="view.sx(1)-view.sx(0)" height="244" class="shade"/><line x1="28" x2="372" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis"/><polyline :points="parabola" class="lab-line"/>
    <circle :cx="view.sx(a)" :cy="view.sy(curvature)" r="8" class="lab-dot-warn"/><circle :cx="view.sx(a)" :cy="view.sy(curvature)" r="28" class="lab-handle hit" tabindex="0" role="slider" aria-label="Số mũ a" :aria-valuetext="fmt(a,4)" @pointerdown="drag.start('a',$event)" @keydown="drag.key('a',[a,curvature],$event)"/>
    <text x="32" y="28">a(a − 1)</text><text :x="view.sx(0)-6" y="290">0</text><text :x="view.sx(1)-6" y="290">1</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-buttons"><button type="button" @click="a=-1">a = −1</button><button type="button" @click="a=0">a = 0</button><button type="button" @click="a=.5">a = 1/2</button><button type="button" @click="a=1">a = 1</button><button type="button" @click="a=2">a = 2</button></div>
  <div class="lab-controls"><label>Số mũ a = {{fmt(a)}}<input v-model.number="a" type="range" min="-2" max="3" step=".1"/></label></div>
  <div class="lab-readout" role="status"><p>a(a − 1) = {{fmt(curvature,4)}}. Vì x &gt; 0, thừa số xᵃ⁻² dương, nên dấu của f'' là dấu hệ số này. Hàm đang {{kind.toLowerCase()}}.</p><p>Dây cung tại trung điểm của 0.4 và 2.6 trừ giá trị đồ thị bằng {{fmt(gap,4)}}. Giá trị dương ứng với dây cung ở trên, giá trị âm ứng với dây cung ở dưới.</p><p>Khung chỉ cắt phần đồ thị vượt độ cao đang xem. Các giá trị tính toán không bị kẹp theo mép khung. Tại a = 0 hoặc a = 1, đạo hàm bậc hai bằng 0 trên toàn miền.</p></div>
 </figure>
</template>
<style scoped>
svg text{font-size:20px;pointer-events:none}.shade{fill:var(--do-soft);opacity:.6}svg :is(line,rect,polyline),svg circle:not(.hit){pointer-events:none}.hit{fill:transparent!important;stroke:transparent}.hit:focus-visible{stroke:var(--vang)}
</style>
