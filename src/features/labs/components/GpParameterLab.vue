<script setup>
import { computed,ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { makeView,createDragger,fmt } from '../controllers/svg-drag.js'
import { geometricProgramOptimum } from '../services/foundation-geometry.mjs'
const svg=ref(null),dimension=ref(3),bound=ref(1)
const row=computed(()=>geometricProgramOptimum(dimension.value,bound.value))
const ymax=computed(()=>geometricProgramOptimum(dimension.value,8).value*1.15)
const view=computed(()=>makeView({x0:0,x1:8.8,y0:0,y1:ymax.value,width:440,height:320,pad:30})),P=p=>view.value.point(p)
const drag=createDragger(svg,view,(_,p)=>{bound.value=Math.max(.25,Math.min(8,p[0]))},{step:.05,snap:.01})
const curve=computed(()=>Array.from({length:156},(_,i)=>{const a=.25+i*.05;return P([a,geometricProgramOptimum(dimension.value,a).value]).join(',')}).join(' '))
</script>

<template>
 <figure class="study-lab" aria-label="GP có tham số, điểm đổi trạng thái và thay đổi số chiều">
  <figcaption class="lab-title">Cận dưới thay đổi nghiệm khi vượt một ngưỡng phụ thuộc số chiều</figcaption>
  <p class="lab-lead">Cực tiểu x₁ + 2x₂ + ⋯ + 2ⁿ⁻¹xₙ, giữ x₁⋯xₙ = 1 và x₁ ≥ a. Kéo chấm trên đồ thị để đổi a. Đổi n để thấy ngưỡng bắt đầu làm tăng chi phí chuyển vị trí.</p>
  <svg ref="svg" viewBox="0 0 440 320" role="group" aria-label="Giá trị tối ưu theo tham số a và mức a kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line x1="30" y1="290" x2="410" y2="290" class="lab-axis"/><line x1="30" y1="30" x2="30" y2="290" class="lab-axis"/>
   <line :x1="view.sx(row.threshold)" :x2="view.sx(row.threshold)" y1="40" y2="290" class="lab-guide"/>
   <polyline :points="curve" class="lab-accent"/>
   <circle :cx="view.sx(bound)" :cy="view.sy(row.value)" r="8" class="lab-dot-warn"/>
   <circle :cx="view.sx(bound)" :cy="view.sy(row.value)" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Tham số cận dưới a" :aria-valuetext="`a = ${fmt(bound,3)}, C* = ${fmt(row.value,3)}`" @pointerdown="drag.start('a',$event)" @keydown="drag.key('a',[bound,0],$event)"/>
   <text x="12" y="23">Giá trị tối ưu C*</text><text x="414" y="310">a</text>
   <text v-for="a in [0,2,4,6,8]" :key="a" :x="view.sx(a)-5" y="313">{{a}}</text>
   <text :x="view.sx(row.threshold)+8" y="47">Ngưỡng</text>
   <text x="36" :y="view.sy(dimension*row.threshold)-12">{{fmt(dimension*row.threshold,2)}}</text>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="x"/></details>
  <div class="lab-controls"><label>Số biến dương n<select v-model.number="dimension"><option v-for="n in [2,3,4,5,6]" :key="n" :value="n">{{n}}</option></select></label></div>
  <div class="lab-buttons"><button type="button" @click="dimension=3;bound=1">Ba biến, a = 1</button><button type="button" @click="dimension=3;bound=8">Ba biến, a = 8</button><button type="button" @click="bound=row.threshold">Đúng tại ngưỡng</button></div>
  <div class="lab-readout" role="status">
   <p>n = {{dimension}}, a = {{fmt(bound,4)}}. Ngưỡng qₙ = 2^((n − 1)/2) ≈ {{fmt(row.threshold,4)}}. {{row.active?'Cận x₁ ≥ a chặt tại nghiệm.':'Cận chưa chặt, nghiệm chưa đổi khi a tăng trong vùng này.'}}</p>
   <p>Giá trị tối ưu C* = {{fmt(row.value,5)}}. Tích các tọa độ x₁⋯xₙ = {{fmt(row.product,5)}}.</p>
   <ol><li v-for="(value,i) in row.point" :key="i">x{{i+1}}* = {{fmt(value,5)}}. Hệ số chi phí c{{i+1}} = {{row.weights[i]}}, phần chi phí c{{i+1}}x{{i+1}}* = {{fmt(row.weights[i]*value,5)}}.</li></ol>
   <p v-if="bound<=row.threshold">Ở nghiệm không bị cận làm thay đổi, mọi phần chi phí cᵢxᵢ* bằng nhau. Đồ thị phẳng vì cận vẫn thấp hơn hoặc vừa chạm tọa độ tối ưu tự do.</p>
   <p v-else>Khi a vượt ngưỡng, x₁* = a. Các phần chi phí còn lại vẫn bằng nhau theo AM–GM, nhưng phần chi phí đầu tiên lớn hơn. Tăng a làm các tọa độ khác giảm để giữ tích bằng 1.</p>
   <p>Đây là một họ GP có n biến với các hệ số 1, 2, 4, … cố định theo quy luật. Thay đổi n làm cả số biến và dãy hệ số đổi, nên không diễn giải đường này như mọi bài toán nhiều chiều đều khó hoặc tốn hơn theo cùng một tỉ lệ.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Với n = 3, kéo a qua 2. Vì sao nghiệm đứng yên trước ngưỡng rồi thay đổi sau ngưỡng?</li><li>Đặt a = 8. Vì sao x₂ và x₃ cùng giảm, nhưng không bằng nhau?</li><li>Giữ a rồi đổi n. Vì sao ngưỡng đổi theo 2^((n − 1)/2)?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
</style>
