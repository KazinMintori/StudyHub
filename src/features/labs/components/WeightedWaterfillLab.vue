<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {weightedCappedWaterfill,weightedWaterDual} from '../services/foundation-geometry.mjs'
const svg=ref(null),dualSvg=ref(null),budget=ref(1),trialNu=ref(.75),normalized=ref(false)
const alpha=[1,2,5],weights=[2,1,2],caps=[1,2,1]
const row=computed(()=>weightedCappedWaterfill(budget.value)),dual=computed(()=>weightedWaterDual(budget.value,trialNu.value))
const height=(i,x)=>(alpha[i]+x)/(normalized.value?weights[i]:1),Y=y=>290-y*31
const budgetView=ref({x0:.05,x1:3.95,y0:0,y1:0,toWorld:(x)=>[(x-35)*4/330,0]})
const drag=createDragger(svg,budgetView,(_,p)=>{budget.value=p[0]},{step:.05,snap:.01})
const samples=computed(()=>Array.from({length:191},(_,i)=>{const nu=.2+i*.01;return[nu,weightedWaterDual(budget.value,nu).value-row.value.value]}))
const graph=computed(()=>{
 const depth=Math.max(.3,-Math.min(...samples.value.map(p=>p[1])))
 return makeView({x0:.1,x1:2.2,y0:-depth*1.15,y1:depth*.12,width:400,height:400,pad:30})
}),G=p=>graph.value.point(p)
const dualView=computed(()=>({...graph.value,x0:.2,x1:2.1}))
const dualDrag=createDragger(dualSvg,dualView,(_,p)=>{trialNu.value=p[0]},{step:.025,snap:.005})
const curve=computed(()=>samples.value.map(p=>G(p).join(',')).join(' '))
const difference=computed(()=>dual.value.value-row.value.value)
</script>

<template>
 <figure class="study-lab" aria-label="Water-filling có trọng số và trần, đa nghiệm nhân tử tại điểm gãy">
  <figcaption class="lab-title">Tại ngân sách 1, nghiệm phân bổ duy nhất nhưng giá bóng có cả một khoảng</figcaption>
  <p class="lab-lead">Kéo P trên thước ngân sách trong hình đầu để đổi tổng tài nguyên. Kéo ν trên đồ thị đối ngẫu ở hình sau. Cột luôn cho nghiệm phân bổ tối ưu theo P, còn ν đang thử tạo một cận dưới có thể chưa khít.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Ba kênh với mức nền, tài nguyên phân bổ, trần và ngân sách P kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <g v-for="i in [0,1,2]" :key="i">
     <rect :x="52+110*i" :y="Y(height(i,0))" width="62" :height="290-Y(height(i,0))" class="lab-region-soft"/>
     <rect :x="52+110*i" :y="Y(height(i,row.point[i]))" width="62" :height="Y(height(i,0))-Y(height(i,row.point[i]))" class="lab-good-fill"/>
     <line :x1="42+110*i" :x2="124+110*i" :y1="Y(height(i,caps[i]))" :y2="Y(height(i,caps[i]))" class="lab-bad"/>
     <text :x="56+110*i" :y="Y(height(i,caps[i]))-12">Trần</text><text :x="54+110*i" y="315">Kênh {{i+1}}</text>
    </g>
    <g v-if="normalized"><line v-for="gap in [[114,162],[224,272],[334,348]]" :key="gap[0]" :x1="gap[0]" :x2="gap[1]" :y1="Y(1/trialNu)" :y2="Y(1/trialNu)" class="lab-guide"/><text x="354" :y="Y(1/trialNu)+6">1/ν</text></g>
    <line x1="35" y1="350" x2="365" y2="350" class="lab-axis"/>
    <circle :cx="35+330*budget/4" cy="350" r="7" class="lab-dot-warn"/>
    <circle :cx="35+330*budget/4" cy="350" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Tổng ngân sách P" :aria-valuetext="'P = '+fmt(budget,3)" @pointerdown="drag.start('P',$event)" @keydown="drag.key('P',[budget,0],$event)"/>
    <text x="12" y="23">{{normalized?'Mức chuẩn hóa (αᵢ + xᵢ)/wᵢ':'Mức thô αᵢ + xᵢ'}}</text><text x="30" y="387">0</text><text x="190" y="387">2</text><text x="359" y="387">4</text><text x="375" y="354">P</text>
   </svg>
   <svg ref="dualSvg" viewBox="0 0 400 400" role="group" aria-label="Hàm đối ngẫu trừ giá trị tối ưu, đoạn nhân tử tối ưu và ν đang thử kéo được" @pointermove="dualDrag.move" @pointerup="dualDrag.end" @pointercancel="dualDrag.end" @lostpointercapture="dualDrag.end">
    <line x1="30" x2="370" :y1="graph.sy(0)" :y2="graph.sy(0)" class="lab-axis"/>
    <polyline :points="curve" class="lab-accent"/>
    <line :x1="graph.sx(row.nu[0])" :x2="graph.sx(row.nu[1])" :y1="graph.sy(0)" :y2="graph.sy(0)" class="lab-good"/>
    <circle v-for="nu in [...new Set(row.nu)]" :key="nu" :cx="graph.sx(nu)" :cy="graph.sy(0)" r="5" class="lab-dot-hollow"/>
    <circle :cx="graph.sx(trialNu)" :cy="graph.sy(difference)" r="7" class="lab-dot-warn"/>
    <circle :cx="graph.sx(trialNu)" :cy="graph.sy(difference)" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Nhân tử ngân sách ν đang thử" :aria-valuetext="`ν = ${fmt(trialNu,4)}, g = ${fmt(dual.value,5)}`" @pointerdown="dualDrag.start('nu',$event)" @keydown="dualDrag.key('nu',[trialNu,0],$event)"/>
    <text x="12" y="23">gₚ(ν) − V(P), luôn không dương</text><text x="12" :y="graph.sy(0)+6">0</text><text v-for="nu in [.5,1,1.5,2]" :key="'label'+nu" :x="graph.sx(nu)-8" y="393">{{nu}}</text><text x="375" y="393">ν</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="x"/><LabPointControls :svg="dualSvg" axes="x"/></details>
  <div class="lab-controls"><label class="lab-check"><input v-model="normalized" type="checkbox"/>Chia mức mỗi kênh cho trọng số wᵢ</label></div>
  <div class="lab-buttons"><button type="button" @click="budget=1;trialNu=.75">P = 1, ν = 0.75</button><button type="button" @click="budget=1.5">P = 1.5</button><button type="button" @click="budget=3">P = 3</button><button type="button" @click="trialNu=(row.nu[0]+row.nu[1])/2">Chọn một nhân tử tối ưu</button></div>
  <div class="lab-readout" role="status">
   <p>P = {{fmt(budget,3)}}, nghiệm duy nhất x* = {{fmtPoint(row.point,4)}}, giá trị V(P) = {{fmt(row.value,6)}}. Mức nền α = (1, 2, 5), trọng số w = (2, 1, 2), trần tài nguyên c = (1, 2, 1).</p>
   <p>Nhân tử ngân sách tối ưu {{row.nu[0]===row.nu[1]?'duy nhất':'có cả một khoảng'}}: [{{fmt(row.nu[0],5)}}, {{fmt(row.nu[1],5)}}]. Tại P = 1, mọi ν trong [1/2, 1] cho cùng cận đúng. Hai đạo hàm một phía của V lần lượt là −1 và −1/2.</p>
   <p>Với ν đang thử = {{fmt(trialNu,4)}}, nghiệm các bài toán kênh riêng là {{fmtPoint(dual.point,4)}}, có tổng {{fmt(dual.total,5)}}. {{Math.abs(dual.total-budget)<1e-8?'Tổng này khớp ngân sách, cận đối ngẫu khít.':'Tổng này chưa khớp ngân sách. Nó dùng để tính g, chưa phải một phân bổ khả thi của bài toán gốc.'}}</p>
   <p>gₚ(ν) = {{fmt(dual.value,6)}} ≤ V(P) = {{fmt(row.value,6)}}. Độ rộng chứng nhận bằng {{fmt(row.value-dual.value,6)}}. Đồ thị trừ V(P) để mức tối ưu ở 0, và tự đổi thang dọc theo P để thấy rõ phần cong cùng đoạn phẳng.</p>
   <p>Chỉ các kênh nằm giữa hai cận mới có cùng mức chuẩn hóa (αᵢ + xᵢ)/wᵢ = 1/ν. Kênh chạm 0 hoặc chạm trần không bắt buộc cùng mức. Các mức thô αᵢ + xᵢ cũng không cần bằng nhau khi trọng số khác nhau. Khi bật chuẩn hóa, các đoạn ngang ở khoảng trống đánh dấu 1/ν đang thử mà không vẽ xuyên qua cột hoặc nhãn trần.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt P = 1 rồi kéo ν từ 1/2 tới 1. Vì sao cột phân bổ không đổi và đồ thị đối ngẫu phẳng?</li><li>Đổi P qua 1.5 và 3. Kênh nào rời cận hoặc chạm trần?</li><li>Bật mức chuẩn hóa ở P = 2. Vì sao hai kênh chưa chạm cận có cùng độ cao, còn kênh đầu đã chạm trần?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
