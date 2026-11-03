<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {variancePolygon,distributionVariance,projectVariancePoint} from '../services/qp-geometry.mjs'
const svg=ref(null),point=ref([.4,.2])
const flat=makeView({x0:0,x1:.85,y0:0,y1:.6,width:360,height:280,pad:36}),view=computed(()=>flat)
const drag=createDragger(svg,view,(_,p)=>{point.value=projectVariancePoint(p)},{step:.02})
const model=computed(()=>distributionVariance(point.value))
</script>
<template>
 <figure class="study-lab" aria-label="Phương sai lõm theo phân phối xác suất">
  <figcaption class="lab-title">Đổi xác suất, giữ các giá trị có thể nhận</figcaption>
  <p class="lab-lead">Kéo chấm trong miền xác suất. Thí nghiệm dùng các giá trị 0, 2, 4 với p₂ = 1 − p₀ − p₄ và giữ 1 ≤ E[X] ≤ 2. Đây là một phần của họ phân phối trên {0, 1, 2, 3, 4}, đủ để đạt cả cận phương sai lớn nhất và nhỏ nhất trong bài.</p>
  <svg ref="svg" viewBox="0 0 360 280" role="group" aria-label="Miền của p0 và p4 với tổng xác suất và trung bình được giữ đúng" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line x1="28" :y1="flat.sy(0)" x2="331" :y2="flat.sy(0)" class="lab-axis"/><line :x1="flat.sx(0)" y1="24" :x2="flat.sx(0)" y2="252" class="lab-axis"/>
   <polygon :points="variancePolygon.map(p=>flat.point(p).join(',')).join(' ')" class="lab-region"/>
   <text x="331" y="269">p₀</text><text x="46" y="24">p₄</text><text x="15" y="273">0</text>
   <circle :cx="flat.sx(point[0])" :cy="flat.sy(point[1])" r="6" class="lab-dot-accent"/>
   <circle :cx="flat.sx(point[0])" :cy="flat.sy(point[1])" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Hai xác suất p0 và p4" :aria-valuetext="fmtPoint(model.p,5)" @pointerdown="drag.start('p',$event)" @keydown="drag.key('p',point,$event)"/>
  </svg>
  <svg viewBox="0 0 360 190" role="img" aria-label="Ba cột xác suất tại 0, 2 và 4">
   <line x1="30" y1="143" x2="330" y2="143" class="lab-axis"/>
   <rect v-for="(p,i) in model.p" :key="i" :x="53+110*i" :y="143-100*p" width="34" :height="100*p" class="probability"/>
   <text v-for="(p,i) in model.p" :key="i" :x="70+110*i" y="28" text-anchor="middle">{{fmt(p,3)}}</text>
   <text v-for="(x,i) in [0,2,4]" :key="i" :x="70+110*i" y="175" text-anchor="middle">X = {{x}}</text>
  </svg>
  <div class="lab-buttons"><button type="button" @click="point=[.5,.5]">Phương sai lớn nhất</button><button type="button" @click="point=[0,0]">Dồn toàn bộ vào 2</button><button type="button" @click="point=[.5,0]">Trung bình bằng 1</button><button type="button" @click="point=[.4,.2]">Phân phối bên trong</button></div>
  <details class="lab-tasks"><summary>Điều chỉnh xác suất bằng nút</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-readout" role="status">
   <p>(p₀, p₂, p₄) = {{fmtPoint(model.p,5)}}. Tổng = {{fmt(model.p.reduce((a,b)=>a+b,0),6)}}, E[X] = {{fmt(model.mean,6)}} và E[X²] = {{fmt(model.second,6)}}.</p>
   <p>Var(X) = E[X²] − E[X]² = {{fmt(model.variance,6)}}. Các giá trị 0, 2, 4 giữ nguyên, chỉ xác suất thay đổi. Hessian của phương sai theo các xác suất là nửa xác định âm, nên phương sai là hàm lõm theo phân phối.</p>
   <p>Trên toàn họ phân phối có 0 ≤ X ≤ 4, ta có X² ≤ 4X. Gọi μ = E[X], suy ra Var(X) ≤ 4μ − μ² ≤ 4. Phân phối (1/2, 0, 1/2) đạt 4 tại μ = 2, còn dồn vào X = 2 đạt phương sai 0.</p>
  </div>
 </figure>
</template>
<style scoped>
svg text{font-size:18px}
.probability{fill:var(--tim);fill-opacity:.65}
svg :is(line,polygon,rect,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
