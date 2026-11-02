<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {entropyMoment,project3,lineParameter} from '../services/foundation-geometry.mjs'
const svg=ref(null),dualSvg=ref(null),third=ref(.5),eta=ref(0)
const camera={yaw:35,pitch:28,scale:170,origin:[200,260]},P=p=>project3(p,camera)
const point=t=>[t-3/7,10/7-2*t,t],row=computed(()=>entropyMoment(third.value,eta.value))
const view=ref({x0:3/7+.001,x1:5/7-.001,y0:0,y1:0,toWorld:(x,y)=>[lineParameter([x,y],P(point(0)),P(point(1)))??third.value,0]})
const drag=createDragger(svg,view,(_,p)=>{third.value=p[0]},{step:.005,snap:.001})
const graph=ref(makeView({x0:-2.3,x1:1.3,y0:-2.1,y1:-.6,width:400,height:400,pad:30})),G=p=>graph.value.point(p)
const dragGraph=computed(()=>({...graph.value,x0:-2,x1:1}))
const dualDrag=createDragger(dualSvg,dragGraph,(_,p)=>{eta.value=p[0]},{step:.025,snap:.005})
const curve=Array.from({length:151},(_,i)=>{const h=-2+i*.02;return G([h,entropyMoment(4/7,h).dual]).join(',')}).join(' ')
const simplex=[[1,0,0],[0,1,0],[0,0,1]],optimal=[1/7,2/7,4/7]
</script>

<template>
 <figure class="study-lab" aria-label="Đối ngẫu entropy với ràng buộc kỳ vọng và phân phối dạng mũ">
  <figcaption class="lab-title">Một phân phối khả thi và một phân phối do nhân tử sinh ra</figcaption>
  <p class="lab-lead">Ba xác suất có tổng 1 và kỳ vọng của các mức (0, 1, 2) bằng 10/7. Kéo điểm trên đoạn để đổi phân phối khả thi. Kéo η ở hình sau để điều chỉnh cận đối ngẫu; phân phối dạng mũ tương ứng chưa chắc có đúng kỳ vọng.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Simplex xác suất trong R³, đoạn giữ nguyên kỳ vọng và điểm phân phối kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <polygon :points="simplex.map(p=>P(p).join(',')).join(' ')" class="lab-region-soft"/>
    <line :x1="P(point(3/7))[0]" :y1="P(point(3/7))[1]" :x2="P(point(5/7))[0]" :y2="P(point(5/7))[1]" class="lab-accent"/>
    <circle v-for="t in [3/7,5/7]" :key="t" :cx="P(point(t))[0]" :cy="P(point(t))[1]" r="6" class="lab-dot-hollow"/>
    <circle :cx="P(optimal)[0]" :cy="P(optimal)[1]" r="6" class="lab-dot-hollow"/><text :x="P(optimal)[0]+13" :y="P(optimal)[1]-15">x*</text>
    <circle :cx="P(row.point)[0]" :cy="P(row.point)[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="P(row.point)[0]" :cy="P(row.point)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Phân phối x trên đoạn tổng bằng 1 và kỳ vọng bằng 10/7" :aria-valuetext="fmtPoint(row.point,4)" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',[third,0],$event)"/>
    <text x="12" y="23">Không gian ba xác suất R³</text><text :x="P(simplex[0])[0]+5" :y="P(simplex[0])[1]+25">x₁</text><text :x="P(simplex[1])[0]-25" :y="P(simplex[1])[1]+25">x₂</text><text :x="P(simplex[2])[0]+12" :y="P(simplex[2])[1]-12">x₃</text>
   </svg>
   <svg ref="dualSvg" viewBox="0 0 400 400" role="group" aria-label="Hàm đối ngẫu sau khi chuẩn hóa phân phối, điểm η kéo được và cực đại tại âm log 2" @pointermove="dualDrag.move" @pointerup="dualDrag.end" @pointercancel="dualDrag.end" @lostpointercapture="dualDrag.end">
    <line v-for="value in [-2,-1]" :key="'grid'+value" x1="30" x2="370" :y1="graph.sy(value)" :y2="graph.sy(value)" class="lab-guide"/>
    <text v-for="value in [-2,-1]" :key="'value'+value" x="3" :y="graph.sy(value)+6">{{value}}</text>
    <polyline :points="curve" class="lab-good"/>
    <line :x1="graph.sx(0)" :x2="graph.sx(0)" y1="50" y2="370" class="lab-axis"/>
    <circle :cx="G([-Math.log(2),entropyMoment(4/7,-Math.log(2)).dual])[0]" :cy="G([-Math.log(2),entropyMoment(4/7,-Math.log(2)).dual])[1]" r="6" class="lab-dot-hollow"/>
    <text :x="graph.sx(-Math.log(2))-30" :y="graph.sy(entropyMoment(4/7,-Math.log(2)).dual)-15">η*</text>
    <circle :cx="G([eta,row.dual])[0]" :cy="G([eta,row.dual])[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="G([eta,row.dual])[0]" :cy="G([eta,row.dual])[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Nhân tử kỳ vọng η" :aria-valuetext="`η = ${fmt(eta,4)}, g = ${fmt(row.dual,5)}`" @pointerdown="dualDrag.start('eta',$event)" @keydown="dualDrag.key('eta',[eta,0],$event)"/>
    <text x="12" y="23">Cận đối ngẫu g̃(η)</text><text v-for="value in [-2,-1,0,1]" :key="value" :x="graph.sx(value)-7" y="393">{{value}}</text><text x="371" y="393">η</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="x"/><LabPointControls :svg="dualSvg" axes="x"/></details>
  <div class="lab-buttons"><button type="button" @click="third=4/7">Phân phối tối ưu</button><button type="button" @click="eta=-Math.log(2)">Nhân tử tối ưu</button><button type="button" @click="third=.5;eta=0">Bắt đầu lại</button></div>
  <div class="lab-readout" role="status">
   <p>Phân phối khả thi x = {{fmtPoint(row.point,4)}}. Tổng xác suất bằng 1 và kỳ vọng bằng 10/7. Mục tiêu f(x) = Σxᵢ log xᵢ = {{fmt(row.value,6)}}. Entropy bằng −f(x).</p>
   <p>η = {{fmt(eta,4)}}. Sau khi cực đại theo nhân tử chuẩn hóa τ, ta có τ = log Z − 1 = {{fmt(row.tau,4)}}. Phân phối dạng mũ là {{fmtPoint(row.induced,4)}} và có kỳ vọng {{fmt(row.mean,6)}}.</p>
   <p>Cận g̃(η) = {{fmt(row.dual,6)}}. Khoảng chứng nhận là [{{fmt(row.dual,6)}}, {{fmt(row.value,6)}}], độ rộng {{fmt(row.gap,6)}}. Mục tiêu được cực tiểu nên cận dưới là số âm nhỏ hơn hoặc bằng giá trị gốc.</p>
   <p>Tại η* = −log 2, phân phối dạng mũ có đúng kỳ vọng 10/7 và bằng (1, 2, 4)/7. Khi đó nó trùng phân phối entropy tối ưu. KKT và đẳng thức hai cận chứng nhận kết quả này.</p>
   <p>Miền yêu cầu mọi xác suất dương. Hai vòng rỗng ở đầu đoạn nằm trên biên có tọa độ bằng 0 và bị loại. Vùng kéo giữ cách đầu mút 0.001 để tránh log 0, không thay đổi miền toán học của bài giảng.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt η = 0. Vì sao phân phối dạng mũ đều nhưng không thỏa kỳ vọng 10/7?</li><li>Đưa η tới tối ưu, giữ phân phối gốc chưa tối ưu. Vì sao khoảng chứng nhận vẫn chưa bằng 0?</li><li>Đưa cả hai phía về tối ưu. Vì sao entropy là số dương, còn mục tiêu đang cực tiểu là số âm?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
