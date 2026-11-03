<script setup>
import { computed,ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import MathMatrix from '../../../core/math/components/MathMatrix.vue'
import { createDragger,makeView,fmt,fmtPoint } from '../controllers/svg-drag.js'
import { ellipsoidResource,dot } from '../services/foundation-geometry.mjs'
const svg=ref(null),coefficientSvg=ref(null),point=ref([3,3]),u=ref([.2,.1])
const view=ref(makeView({x0:-.5,x1:5.5,y0:-.5,y1:5.5,width:400,height:400,pad:30})),P=p=>view.value.point(p)
const coefficientView=ref(makeView({x0:0,x1:10,y0:0,y1:10,width:400,height:400,pad:30})),A=p=>coefficientView.value.point(p)
const drag=createDragger(svg,view,(_,p)=>{point.value=p.map(v=>Math.max(0,v))},{step:.05,snap:.01})
const coefficientDrag=createDragger(coefficientSvg,coefficientView,(_,p)=>{
 const raw=[(p[0]-5)/3,(p[1]-5)/4],length=Math.hypot(...raw)
 u.value=length>1?raw.map(v=>v/length):raw
},{step:.1,snap:.01})
const row=computed(()=>ellipsoidResource(point.value))
const coefficient=computed(()=>[5+3*u.value[0],5+4*u.value[1]])
const selectedCost=computed(()=>dot(coefficient.value,point.value))
const ellipse=Array.from({length:121},(_,i)=>[5+3*Math.cos(i*Math.PI/60),5+4*Math.sin(i*Math.PI/60)])
const boundary=[[0,0],...Array.from({length:91},(_,i)=>{
 const direction=[Math.cos(i*Math.PI/180),Math.sin(i*Math.PI/180)],cost=ellipsoidResource(direction).worst
 return direction.map(v=>37*v/cost)
})]
const optimum=[16/5,9/5]
const matrix=computed(()=>[[row.value.t,...row.value.z],[row.value.z[0],row.value.t,0],[row.value.z[1],0,row.value.t]].map(r=>r.map(v=>Number(v.toFixed(3)))))
</script>

<template>
 <figure class="study-lab" aria-label="Bất định ellipsoid, miền khả thi vững và ma trận SDP tương đương">
  <figcaption class="lab-title">Cùng một điểm x, ba cách kiểm tra giới hạn tài nguyên</figcaption>
  <p class="lab-lead">Kéo quyết định x trong hình đầu. Kéo hệ số a trong ellipsoid ở hình sau để thử một kịch bản. Chi phí danh định chỉ dùng tâm (5, 5), còn kiểm tra vững phải xét toàn bộ ellipsoid.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Miền quyết định không âm, tập khả thi vững và điểm x kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <line :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P([5.5,0])[0]" :y2="P([5.5,0])[1]" class="lab-axis"/><line :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P([0,5.5])[0]" :y2="P([0,5.5])[1]" class="lab-axis"/>
    <polygon :points="boundary.map(p=>P(p).join(',')).join(' ')" class="lab-region"/>
    <line :x1="P([0,5])[0]" :y1="P([0,5])[1]" :x2="P([5,0])[0]" :y2="P([5,0])[1]" class="lab-guide"/>
    <circle :cx="P(optimum)[0]" :cy="P(optimum)[1]" r="7" class="lab-dot-hollow"/><text :x="P(optimum)[0]+13" :y="P(optimum)[1]+26">x*</text>
    <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" :class="row.worst<=37+1e-9?'lab-dot-accent':'lab-dot-bad'"/>
    <circle :cx="P(point)[0]" :cy="P(point)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Quyết định x gồm hai khối lượng xử lý" :aria-valuetext="fmtPoint(point)" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',point,$event)"/>
    <text x="12" y="23">Không gian quyết định</text><text x="342" :y="P([0,0])[1]+23">x₁</text><text :x="P([0,0])[0]+12" y="48">x₂</text>
   </svg>
   <svg ref="coefficientSvg" viewBox="0 0 400 400" role="group" aria-label="Ellipsoid hệ số có tâm (5,5), hai bán trục 3 và 4, hệ số a kéo được" @pointermove="coefficientDrag.move" @pointerup="coefficientDrag.end" @pointercancel="coefficientDrag.end" @lostpointercapture="coefficientDrag.end">
    <line x1="30" y1="370" x2="370" y2="370" class="lab-axis"/><line x1="30" y1="30" x2="30" y2="370" class="lab-axis"/>
    <polygon :points="ellipse.map(p=>A(p).join(',')).join(' ')" class="lab-region"/>
    <line :x1="A([2,5])[0]" :y1="A([2,5])[1]" :x2="A([8,5])[0]" :y2="A([8,5])[1]" class="lab-guide"/><line :x1="A([5,1])[0]" :y1="A([5,1])[1]" :x2="A([5,9])[0]" :y2="A([5,9])[1]" class="lab-guide"/>
    <circle :cx="A([5,5])[0]" :cy="A([5,5])[1]" r="5" class="lab-dot"/><text x="140" y="245">(5, 5)</text>
    <circle :cx="A(row.coefficient)[0]" :cy="A(row.coefficient)[1]" r="10" class="lab-dot-hollow"/><text :x="Math.min(300,A(row.coefficient)[0]+13)" :y="A(row.coefficient)[1]-16">Xấu nhất</text>
    <circle :cx="A(coefficient)[0]" :cy="A(coefficient)[1]" r="7" :class="selectedCost<=37?'lab-dot-accent':'lab-dot-bad'"/>
    <circle :cx="A(coefficient)[0]" :cy="A(coefficient)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Hệ số a bên trong ellipsoid bất định" :aria-valuetext="fmtPoint(coefficient)" @pointerdown="coefficientDrag.start('a',$event)" @keydown="coefficientDrag.key('a',coefficient,$event)"/>
    <text x="12" y="23">Không gian hệ số a</text><text x="342" y="394">a₁</text><text x="43" y="48">a₂</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/><LabPointControls :svg="coefficientSvg"/></details>
  <p class="lab-legend"><span class="legend-accent">Miền vững ở hình đầu, ellipsoid ở hình sau</span><span>Vòng rỗng: Nghiệm x* hoặc kịch bản xấu nhất</span><span class="legend-guide">Đường mức x₁ + x₂ = 5 ở hình đầu</span></p>
  <div class="lab-buttons"><button type="button" @click="point=[3,3]">Thử x = (3, 3)</button><button type="button" @click="point=[...optimum]">Đưa về nghiệm x*</button><button type="button" @click="u=[...row.u]">Thử kịch bản xấu nhất</button><button type="button" @click="point=[0,0]">Thử x = 0</button></div>
  <div class="lab-readout" role="status">
   <p>x = {{fmtPoint(point)}}. Tổng xử lý bằng {{fmt(point[0]+point[1],3)}}. Chi phí danh định bằng {{fmt(row.nominal,3)}}, chi phí ở hệ số a đang thử bằng {{fmt(selectedCost,3)}}.</p>
   <p>Chi phí lớn nhất bằng {{fmt(row.nominal,3)}} + {{fmt(row.radius,3)}} = {{fmt(row.worst,3)}}. {{row.worst<=37+1e-9?'Điểm x thỏa mọi kịch bản.':'Có kịch bản vượt ngân sách 37.'}} Hướng gây chi phí lớn nhất là u* = {{fmtPoint(row.u,3)}}.</p>
   <p>Dạng SOCP dùng z = (3x₁, 4x₂) và t = 37 − 5x₁ − 5x₂. Ta kiểm ‖z‖₂ ≤ t. Hiện tại ‖z‖₂ = {{fmt(row.radius,3)}} và t = {{fmt(row.t,3)}}.</p>
   <p>Cùng điều kiện đó viết thành LMI M(x) ⪰ 0, với ma trận sau (chỉ số hiển thị được làm tròn):</p>
   <MathMatrix :rows="matrix" label="Ma trận M có hàng đầu t, z một, z hai; khối dưới t nhân ma trận đơn vị"/>
   <p>Ba trị riêng là t − ‖z‖₂, t và t + ‖z‖₂, hiện bằng {{fmtPoint(row.eigenvalues,3)}}. {{row.eigenvalues[0]>=-1e-9?'M nửa xác định dương.':'M không nửa xác định dương.'}}</p>
   <p>Nghiệm chính xác là x* = (16/5, 9/5), cho tổng xử lý 5. Đường mức qua x* đỡ miền vững. Các đường cong chỉ được vẽ bằng đoạn nhỏ, còn chi phí và kết luận khả thi được tính trực tiếp từ chuẩn.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Thử x = (3, 3), rồi bấm kịch bản xấu nhất. Vì sao chi phí tăng từ 30 lên 45?</li><li>Đưa về x*. Chi phí xấu nhất có đúng bằng 37 không?</li><li>Kéo hệ số a về tâm ellipsoid. Vì sao kiểm tra riêng điểm tâm chưa chứng minh tính vững?</li><li>Khi t = 0, điều kiện nón yêu cầu z bằng bao nhiêu? Trong ví dụ này có x nào thỏa đồng thời t = 0 và z = 0 không?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
