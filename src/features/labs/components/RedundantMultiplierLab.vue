<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {polyhedronInBox} from '../services/convex-geometry.mjs'
import {project3,lineParameter} from '../services/foundation-geometry.mjs'
const svg=ref(null),t=ref(.5),showThird=ref(true)
const view=makeView({x0:-.3,x1:4.3,y0:-.3,y1:4.3,width:400,height:400,pad:30}),P=p=>view.point(p)
const normals=[[1,1],[2,1],[3,2]],rhs=[3,4,7]
const region=computed(()=>polyhedronInBox(normals.slice(0,showThird.value?3:2).map((a,i)=>({a:a.map(v=>-v),b:-rhs[i]})),[0,4,0,4]))
const lines=[[[0,3],[3,0]],[[0,4],[2,0]],[[0,3.5],[7/3,0]]]
const camera={yaw:35,pitch:28,scale:120,origin:[200,225]},Q=p=>project3(p,camera)
const start=[1,1,0],finish=[0,0,1]
const lambda=computed(()=>[1-t.value,1-t.value,t.value])
const gradientSegments=computed(()=>{
 let from=[310,55]
 return normals.map((a,i)=>{
  const to=[from[0]-70*lambda.value[i]*a[0],from[1]+70*lambda.value[i]*a[1]]
  const d=to.map((v,j)=>v-from[j]),length=Math.hypot(...d)
  const arrow=length>1?[[to[0],to[1]],[to[0]-8*d[0]/length+4*d[1]/length,to[1]-8*d[1]/length-4*d[0]/length],[to[0]-8*d[0]/length-4*d[1]/length,to[1]-8*d[1]/length+4*d[0]/length]]:[]
  const segment={from,to,arrow,length};from=to;return segment
 })
})
const dragView=ref({x0:0,x1:1,y0:0,y1:0,toWorld:(x,y)=>[lineParameter([x,y],Q(start),Q(finish))??t.value,0]})
const drag=createDragger(svg,dragView,(_,p)=>{t.value=p[0]},{step:.025,snap:.005})
</script>

<template>
 <figure class="study-lab" aria-label="Một nghiệm gốc duy nhất và đoạn các bộ nhân tử tối ưu">
  <figcaption class="lab-title">Thêm ràng buộc thừa có thể thêm cách phân chia chứng nhận</figcaption>
  <p class="lab-lead">Hình đầu là miền x ≥ 0 với x₁ + x₂ ≥ 3 và 2x₁ + x₂ ≥ 4. Ràng buộc thứ ba là tổng hai ràng buộc đó. Kéo điểm ở hình nhân tử để thay đổi t trong bộ λ = (1 − t, 1 − t, t).</p>
  <div class="lab-pair">
   <svg viewBox="0 0 400 400" role="img" aria-label="Miền khả thi không đổi khi bật tắt ràng buộc thứ ba và nghiệm gốc (1,2)">
    <polygon :points="region.map(p=>P(p).join(',')).join(' ')" class="lab-region"/>
    <line :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P([4,0])[0]" :y2="P([4,0])[1]" class="lab-axis"/><line :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P([0,4])[0]" :y2="P([0,4])[1]" class="lab-axis"/>
    <template v-for="(line,i) in lines" :key="i"><line v-if="i<2||showThird" :x1="P(line[0])[0]" :y1="P(line[0])[1]" :x2="P(line[1])[0]" :y2="P(line[1])[1]" :class="i===2?'lab-good':'lab-guide'"/></template>
    <circle :cx="P([1,2])[0]" :cy="P([1,2])[1]" r="8" class="lab-dot-warn"/><text :x="P([1,2])[0]+14" :y="P([1,2])[1]-13">x* = (1, 2)</text>
    <text x="12" y="23">Miền gốc và đường mức chi phí 7</text><text x="344" :y="P([0,0])[1]+23">x₁</text><text :x="P([0,0])[0]+12" y="48">x₂</text>
   </svg>
   <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Đoạn các nhân tử không âm trong không gian ba chiều" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <g v-for="(axis,i) in [[1.25,0,0],[0,1.25,0],[0,0,1.25]]" :key="i"><line :x1="Q([0,0,0])[0]" :y1="Q([0,0,0])[1]" :x2="Q(axis)[0]" :y2="Q(axis)[1]" class="lab-axis"/><text :x="Q(axis)[0]+7" :y="Q(axis)[1]+7">λ{{i+1}}</text></g>
    <line :x1="Q(start)[0]" :y1="Q(start)[1]" :x2="Q(finish)[0]" :y2="Q(finish)[1]" class="lab-accent"/>
    <circle :cx="Q(start)[0]" :cy="Q(start)[1]" r="6" class="lab-dot-hollow"/><circle :cx="Q(finish)[0]" :cy="Q(finish)[1]" r="6" class="lab-dot-hollow"/>
    <text :x="Q(start)[0]+12" :y="Q(start)[1]+24">t = 0</text><text :x="Q(finish)[0]+18" :y="Q(finish)[1]+28">t = 1</text>
    <circle :cx="Q(lambda)[0]" :cy="Q(lambda)[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="Q(lambda)[0]" :cy="Q(lambda)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Bộ nhân tử λ tối ưu, điều chỉnh t" :aria-valuetext="`t = ${fmt(t,3)}, λ = ${fmtPoint(lambda,3)}`" @pointerdown="drag.start('lambda',$event)" @keydown="drag.key('lambda',[t,0],$event)"/>
    <text x="12" y="23">Nhân tử của cách viết ba ràng buộc</text>
   </svg>
  </div>
  <svg viewBox="0 0 400 250" role="img" aria-label="Phân rã âm gradient mục tiêu thành ba pháp tuyến có trọng số, ghép nối đuôi">
   <text x="12" y="23">Các pháp tuyến ghép nối đuôi</text>
   <line x1="310" y1="55" x2="100" y2="195" class="lab-guide"/>
   <g v-for="(segment,i) in gradientSegments" :key="i">
    <line v-if="segment.length>1" :x1="segment.from[0]" :y1="segment.from[1]" :x2="segment.to[0]" :y2="segment.to[1]" :class="['lab-accent','lab-warn','lab-good'][i]"/>
    <polygon v-if="segment.length>1" :points="segment.arrow.map(p=>p.join(',')).join(' ')" :class="'normal-arrow normal-'+i"/>
   </g>
   <circle cx="310" cy="55" r="4" class="lab-dot"/><text x="322" y="61">O</text>
   <circle cx="100" cy="195" r="5" class="lab-dot-hollow"/><text x="48" y="226">−∇f = (−3, −2)</text>
  </svg>
  <p class="lab-legend"><span class="legend-accent">λ₁∇g₁</span><span class="legend-warn">λ₂∇g₂</span><span class="legend-good">λ₃∇g₃</span></p>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="x"/></details>
  <div class="lab-controls"><label class="lab-check"><input v-model="showThird" type="checkbox"/>Vẽ ràng buộc thừa 3x₁ + 2x₂ ≥ 7</label></div>
  <div class="lab-buttons"><button type="button" @click="t=0">Chỉ dùng hai ràng buộc đầu</button><button type="button" @click="t=1">Chỉ dùng ràng buộc thứ ba</button></div>
  <div class="lab-readout" role="status">
   <p>t = {{fmt(t,3)}}, λ = {{fmtPoint(lambda,3)}}. Các nhân tử của −x₁ ≤ 0 và −x₂ ≤ 0 đều bằng 0.</p>
   <p>Hệ số của x₁ trong chứng nhận bằng λ₁ + 2λ₂ + 3λ₃ = 3. Hệ số của x₂ bằng λ₁ + λ₂ + 2λ₃ = 2. Cận dưới bằng 3λ₁ + 4λ₂ + 7λ₃ = 7 ở mọi t trong đoạn.</p>
   <p>Hình ghép vector dùng pháp tuyến của gᵢ ≤ 0, tức ∇g₁ = (−1, −1), ∇g₂ = (−2, −1), ∇g₃ = (−3, −2). Khi đổi t, ba phần đóng góp đổi nhưng tổng vẫn bằng −∇f. Đây là hình học của nhiều bộ nhân tử cùng chứng nhận một nghiệm.</p>
   <p>Nghiệm gốc vẫn duy nhất là (1, 2), cho chi phí 7. Ở t = 1, hai ràng buộc đầu đạt đẳng thức nhưng nhân tử của chúng bằng 0. Ràng buộc chặt không bắt buộc có nhân tử dương.</p>
   <p>Bật/tắt ở hình đầu chỉ so sánh miền khả thi. Hình nhân tử luôn biểu diễn cách viết có đủ ba ràng buộc. Nếu thực sự bỏ ràng buộc thứ ba khỏi mô hình, chỉ còn cặp nhân tử tối ưu (1, 1).</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Tắt ràng buộc thứ ba. Vì sao miền tô không đổi?</li><li>Kéo t từ 0 tới 1. Vì sao cận dưới luôn bằng 7?</li><li>Nhân tử nào bằng 0 tại t = 1 dù ràng buộc tương ứng vẫn chặt?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
.normal-arrow{stroke:none}
.normal-0{fill:var(--tim)}
.normal-1{fill:var(--vang)}
.normal-2{fill:var(--xanh)}
</style>
