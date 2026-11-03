<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt} from '../controllers/svg-drag.js'
import {portfolioVariance as variance,portfolioReturn as expected,portfolioMinimum} from '../services/qp-geometry.mjs'
const svg=ref(null),weight=ref(.5),target=ref(7),selected=ref('weight')
const curve=makeView({x0:-.05,x1:1.05,y0:0,y1:240,width:360,height:278,pad:35})
const rail=makeView({x0:3.5,x1:10.5,y0:0,y1:1,width:360,height:1,pad:30})
const view=computed(()=>selected.value==='weight'?{x0:0,x1:1,y0:0,y1:1,toWorld:x=>[curve.wx(x),0]}:{x0:3.5,x1:10.5,y0:0,y1:1,toWorld:x=>[rail.wx(x),0]})
const drag=createDragger(svg,view,(name,p)=>{if(name==='weight')weight.value=p[0];else target.value=p[0]},{step:.025})
const line=Array.from({length:101},(_,i)=>curve.point([i/100,variance(i/100)]).join(',')).join(' ')
const optimum=computed(()=>portfolioMinimum(target.value))
const threshold=computed(()=>Math.max(0,Math.min(1,(target.value-4)/6)))
const feasible=computed(()=>expected(weight.value)>=target.value-1e-9)
function start(name,event){selected.value=name;drag.start(name,event)}
function key(name,current,event){selected.value=name;drag.key(name,[current,0],event)}
function choose(r,w){target.value=r;weight.value=w}
</script>
<template>
 <figure class="study-lab" aria-label="Danh mục Markowitz hai tài sản, giới hạn lợi suất và phương sai">
  <figcaption class="lab-title">Đổi tỉ lệ vốn, giữ phân phối lợi suất của hai tài sản</figcaption>
  <p class="lab-lead">Kéo điểm trên parabol để đổi tỉ lệ w đầu tư vào A. Kéo chấm trên thước để đổi lợi suất tối thiểu. Miền xanh là các tỉ lệ đạt yêu cầu. Mô hình dùng đúng số liệu A, B trong bài, không phải dữ liệu thị trường.</p>
  <svg ref="svg" viewBox="0 0 360 365" role="group" aria-label="Phương sai lồi theo tỉ lệ vốn và thước lợi suất tối thiểu" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <rect v-if="target<=10" :x="curve.sx(threshold)" y="35" :width="curve.sx(1)-curve.sx(threshold)" height="208" class="feasible"/>
   <line x1="28" :y1="curve.sy(0)" x2="332" :y2="curve.sy(0)" class="lab-axis"/><line :x1="curve.sx(0)" y1="23" :x2="curve.sx(0)" y2="250" class="lab-axis"/>
   <text x="53" y="23">Phương sai (%²)</text><text x="331" y="267">w</text><text :x="curve.sx(0)" y="267" text-anchor="middle">0</text><text :x="curve.sx(1)" y="267" text-anchor="middle">1</text>
   <polyline :points="line" class="curve"/>
   <circle v-if="optimum" :cx="curve.sx(optimum.weight)" :cy="curve.sy(optimum.variance)" r="8" class="optimum"/>
   <circle :cx="curve.sx(weight)" :cy="curve.sy(variance(weight))" r="5" :class="feasible?'lab-dot-accent':'lab-dot-bad'"/>
   <circle :cx="curve.sx(weight)" :cy="curve.sy(variance(weight))" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Tỉ lệ vốn w đầu tư vào A" :aria-valuetext="fmt(weight,5)" @pointerdown="start('weight',$event)" @keydown="key('weight',weight,$event)"/>
   <text x="180" y="300" text-anchor="middle">Lợi suất tối thiểu (%)</text><line x1="30" y1="328" x2="330" y2="328" class="lab-axis"/><text x="30" y="358">3.5</text><text x="330" y="358" text-anchor="end">10.5</text>
   <circle :cx="rail.sx(target)" cy="328" r="6" class="lab-dot-warn"/>
   <circle :cx="rail.sx(target)" cy="328" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Lợi suất tối thiểu trên thước" :aria-valuetext="fmt(target,5)" @pointerdown="start('target',$event)" @keydown="key('target',target,$event)"/>
  </svg>
  <div class="lab-buttons"><button type="button" @click="choose(4,1/7)">Danh mục ít rủi ro nhất</button><button type="button" @click="choose(7,.5)">Yêu cầu ít nhất 7%</button><button type="button" @click="choose(10.5,.5)">Yêu cầu không khả thi</button><button type="button" @click="choose(4,0)">Chỉ tài sản B</button><button type="button" @click="choose(4,1)">Chỉ tài sản A</button></div>
  <details class="lab-tasks"><summary>Đổi tỉ lệ hoặc yêu cầu bằng nút</summary><LabPointControls :svg="svg" axes="x"/></details>
  <div class="lab-readout" role="status">
   <p>w = {{fmt(weight,5)}}. Lợi suất kỳ vọng = {{fmt(expected(weight),4)}}%, độ lệch chuẩn = {{fmt(Math.sqrt(variance(weight)),4)}}%. Điểm đang chọn {{feasible?'đạt':'chưa đạt'}} yêu cầu {{fmt(target,3)}}%.</p>
   <p v-if="optimum">Nghiệm QP có w* = {{fmt(optimum.weight,6)}}, lợi suất kỳ vọng {{fmt(optimum.expected,4)}}%, độ lệch chuẩn {{fmt(Math.sqrt(optimum.variance),4)}}%.</p>
   <p v-else>Bất khả thi: Không tỉ lệ vốn không âm nào tạo lợi suất kỳ vọng vượt 10% trong mô hình hai tài sản này.</p>
   <p>Phương sai v(w) = 280w² − 80w + 25, đo bằng bình phương điểm phần trăm. Đạo hàm bậc hai là 560 &gt; 0, nên v lồi theo tỉ lệ vốn. Đây là biến khác với xác suất phân phối trong mô phỏng trước, nơi phương sai là hàm lõm.</p>
  </div>
 </figure>
</template>
<style scoped>
svg text{font-size:18px}
.feasible{fill:var(--xanh-soft)}
.curve{fill:none;stroke:var(--tim);stroke-width:1.8}
.optimum{fill:var(--xanh);fill-opacity:.7}
svg :is(line,polyline,rect,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
