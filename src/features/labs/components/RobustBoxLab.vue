<script setup>
import { computed,ref,watch } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger,makeView,fmt,fmtPoint } from '../controllers/svg-drag.js'
import { clipPolygon } from '../services/convex-geometry.mjs'
import { dot,boxWorstCase } from '../services/foundation-geometry.mjs'
const svg=ref(null),weightSvg=ref(null),epsilon=ref(.5),weights=ref([1,1]),noise=ref([.2,-.2]),center=[2,1]
const view=ref(makeView({x0:-.5,x1:4.5,y0:-1.5,y1:3.5,width:400,height:400,pad:30})),P=p=>view.value.point(p)
const weightView=ref(makeView({x0:-2.2,x1:2.2,y0:-2.2,y1:2.2,width:400,height:400,pad:30})),W=p=>weightView.value.point(p)
const clamp=v=>Math.max(-epsilon.value,Math.min(epsilon.value,v))
const drag=createDragger(svg,view,(_,p)=>{noise.value=p.map((v,i)=>clamp(v-center[i]))},{step:.05,snap:.01})
const weightDrag=createDragger(weightSvg,weightView,(_,p)=>{weights.value=p},{step:.05,snap:.01})
watch(epsilon,()=>{noise.value=noise.value.map(clamp)})
const worst=computed(()=>boxWorstCase(weights.value,center,epsilon.value))
const current=computed(()=>center.map((v,i)=>v+noise.value[i]))
const corners=computed(()=>[[-1,-1],[1,-1],[1,1],[-1,1]].map(p=>p.map((v,i)=>center[i]+epsilon.value*v)))
const safe=computed(()=>clipPolygon([[-.5,-1.5],[4.5,-1.5],[4.5,3.5],[-.5,3.5]],weights.value.map(v=>-v),-1))
const margin=computed(()=>dot(weights.value,current.value))
const allSafe=computed(()=>worst.value.margin>=1-1e-9)
const zeroWeight=computed(()=>Math.hypot(...weights.value)<1e-10)
function thresholdLine(){
 const w=weights.value,points=[]
 for(const x of [-.5,4.5])if(Math.abs(w[1])>1e-12){const y=(1-w[0]*x)/w[1];if(y>=-1.5&&y<=3.5)points.push([x,y])}
 for(const y of [-1.5,3.5])if(Math.abs(w[0])>1e-12){const x=(1-w[1]*y)/w[0];if(x>=-.5&&x<=4.5)points.push([x,y])}
 return points.length>=2?[points[0],points.at(-1)]:null
}
const line=computed(thresholdLine)
</script>

<template>
 <figure class="study-lab" aria-label="Nhiễu hình hộp và biên phân loại được bảo đảm">
  <figcaption class="lab-title">Một điểm nhiễu chưa đủ để bảo đảm cho cả hình hộp</figcaption>
  <p class="lab-lead">Dữ liệu gốc là x = (2, 1). Kéo điểm x + δ trong hình hộp để thử một nhiễu. Kéo vector w ở hình thứ hai để đổi bộ phân loại. Chấm rỗng đánh dấu một nhiễu xấu nhất.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Hình hộp nhiễu quanh x và điểm nhiễu kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <polygon :points="safe.map(p=>P(p).join(',')).join(' ')" class="lab-good-fill" opacity=".3"/>
    <line x1="30" x2="370" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis"/><line :x1="view.sx(0)" :x2="view.sx(0)" y1="30" y2="370" class="lab-axis"/>
    <line v-if="line" :x1="P(line[0])[0]" :y1="P(line[0])[1]" :x2="P(line[1])[0]" :y2="P(line[1])[1]" class="lab-good"/>
    <polygon :points="corners.map(p=>P(p).join(',')).join(' ')" class="lab-region"/>
    <line :x1="P(center)[0]" :y1="P(center)[1]" :x2="P(current)[0]" :y2="P(current)[1]" class="lab-guide"/>
    <circle :cx="P(center)[0]" :cy="P(center)[1]" r="5" class="lab-dot"/><text :x="P(center)[0]-17" :y="P(center)[1]-12">x</text>
    <circle :cx="P(worst.point)[0]" :cy="P(worst.point)[1]" r="10" class="lab-dot-hollow"/><text :x="Math.min(315,P(worst.point)[0]+13)" :y="P(worst.point)[1]+25">Xấu nhất</text>
    <circle :cx="P(current)[0]" :cy="P(current)[1]" r="7" :class="margin>=1?'lab-dot-accent':'lab-dot-bad'"/>
    <circle :cx="P(current)[0]" :cy="P(current)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Nhiễu δ trong hình hộp" :aria-valuetext="'δ = '+fmtPoint(noise)" @pointerdown="drag.start('noise',$event)" @keydown="drag.key('noise',current,$event)"/>
    <text x="12" y="23">Không gian dữ liệu</text><text x="346" :y="view.sy(0)+24">z₁</text><text :x="view.sx(0)+12" y="48">z₂</text>
   </svg>
   <svg ref="weightSvg" viewBox="0 0 400 400" role="group" aria-label="Vector trọng số w kéo được" @pointermove="weightDrag.move" @pointerup="weightDrag.end" @pointercancel="weightDrag.end" @lostpointercapture="weightDrag.end">
    <line x1="30" y1="200" x2="370" y2="200" class="lab-axis"/><line x1="200" y1="30" x2="200" y2="370" class="lab-axis"/>
    <line x1="200" y1="200" :x2="W(weights)[0]" :y2="W(weights)[1]" class="lab-accent"/>
    <circle :cx="W(weights)[0]" :cy="W(weights)[1]" r="7" class="lab-dot-accent"/>
    <circle :cx="W(weights)[0]" :cy="W(weights)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Trọng số w của bộ phân loại" :aria-valuetext="fmtPoint(weights)" @pointerdown="weightDrag.start('weights',$event)" @keydown="weightDrag.key('weights',weights,$event)"/>
    <text x="12" y="23">Không gian trọng số</text><text x="343" y="225">w₁</text><text x="213" y="48">w₂</text><text :x="Math.max(12,Math.min(360,W(weights)[0]+12))" :y="Math.max(48,W(weights)[1]-12)">w</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/><LabPointControls :svg="weightSvg"/></details>
  <p class="lab-legend"><span class="legend-accent">Hình hộp nhiễu</span><span class="legend-good">Nửa mặt phẳng wᵀz ≥ 1</span><span>Vòng rỗng: Một nhiễu xấu nhất</span></p>
  <div class="lab-controls"><label>Bán kính ε = {{fmt(epsilon)}}<input v-model.number="epsilon" type="range" min="0" max="1.2" step=".05"/></label></div>
  <div class="lab-buttons"><button type="button" @click="weights=[1,1]">w = (1, 1)</button><button type="button" @click="weights=[1,-1]">w = (1, −1)</button><button type="button" @click="weights=[0,0]">w = 0</button><button type="button" @click="noise=[...worst.perturbation]">Thử nhiễu xấu nhất</button></div>
  <div class="lab-readout" role="status">
   <p>w = {{fmtPoint(weights)}}, δ đang thử = {{fmtPoint(noise)}}. Biên tại điểm đang thử bằng {{fmt(margin,3)}}. {{margin>=1?'Riêng điểm này đạt yêu cầu.':'Riêng điểm này vi phạm yêu cầu.'}}</p>
   <p>Biên nhỏ nhất trên cả hộp bằng {{fmt(dot(weights,center),3)}} − {{fmt(worst.penalty,3)}} = {{fmt(worst.margin,3)}}. {{allSafe?'Mọi nhiễu trong hộp đều đạt yêu cầu.':'Có nhiễu trong hộp làm biên nhỏ hơn 1.'}}</p>
   <p>Ta chọn δᵢ = −ε sign(wᵢ). Mỗi tích wᵢδᵢ bằng −ε|wᵢ|, nên tổng mất mát biên là ε(|w₁| + |w₂|) = ε‖w‖₁. {{zeroWeight?'Với w = 0, mọi nhiễu cùng cho biên 0, nên không đạt ngưỡng 1.':'Nếu một thành phần wᵢ bằng 0, thay δᵢ không làm đổi biên và nhiễu xấu nhất có thể không duy nhất.'}}</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Chọn w = (1, −1), ε = 0.5. Vì sao dữ liệu gốc đạt ngưỡng 1 nhưng cả hộp chưa được bảo đảm?</li><li>Đổi dấu w₂. Nhiễu xấu nhất chuyển sang phía nào của hộp?</li><li>Giảm ε về 0. Vì sao hai phép kiểm tra trở thành một?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
