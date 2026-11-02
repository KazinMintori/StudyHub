<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {insideConvexPolygon,closestOnSegment} from '../services/convex-geometry.mjs'
import {momentTriangle,momentDistribution,probabilitySummary} from '../services/lp-models-geometry.mjs'

const svg=ref(null),second=ref(true),pair=ref([1/12,1/48]),theta=ref(.5)
const p=computed(()=>second.value?momentDistribution(...pair.value):[2*theta.value/3,1-theta.value,0,theta.value/3,0])
const summary=computed(()=>probabilitySummary(p.value))
const view=computed(()=>second.value?makeView({x0:-.02,x1:.19,y0:-.015,y1:.105,width:360,height:290,pad:36}):makeView({x0:-.05,x1:1.05,y0:0,y1:1,width:360,height:180,pad:36}))
const point=computed(()=>second.value?pair.value:[theta.value,.5])
const drag=createDragger(svg,view,(_,q)=>{
 if(second.value){
  if(!insideConvexPolygon(q,momentTriangle)){
   const options=momentTriangle.map((a,i)=>closestOnSegment(q,a,momentTriangle[(i+1)%3])).sort((a,b)=>a.distance-b.distance)
   q=options[0].point
  }
  pair.value=q
 }else theta.value=Math.max(0,Math.min(1,q[0]))
},{step:.005})
function minimum(){if(second.value)pair.value=[0,0];else theta.value=0}
function maximum(){if(second.value)pair.value=[1/6,0];else theta.value=1}
function middle(){if(second.value)pair.value=[1/12,1/48];else theta.value=.5}
</script>

<template>
 <figure class="study-lab" aria-label="Cận xác suất bằng LP trên các phân phối có cùng moment">
  <figcaption class="lab-title">Cùng trung bình, nhưng xác suất ở đuôi có thể khác nhau</figcaption>
  <p class="lab-lead">Các cột là xác suất tại 0, 1, 2, 3 và 4. Kéo điểm trong hình tham số để đổi phân phối mà vẫn giữ thông tin đang biết. Hai cột cuối tạo thành xác suất P(X ≥ 3).</p>
  <div class="lab-buttons" role="group" aria-label="Thông tin moment đã biết">
   <button type="button" :aria-pressed="!second" @click="second=false">Chỉ biết E[X] = 1</button>
   <button type="button" :aria-pressed="second" @click="second=true">Thêm E[X²] = 2</button>
   <button type="button" @click="minimum">Xác suất đuôi nhỏ nhất</button>
   <button type="button" @click="maximum">Xác suất đuôi lớn nhất</button>
   <button type="button" @click="middle">Phân phối ở giữa</button>
  </div>
  <svg viewBox="0 0 360 280" role="img" aria-label="Năm cột xác suất và biến cố từ giá trị ba trở lên">
   <line x1="28" y1="230" x2="333" y2="230" class="lab-axis"/>
   <rect x="217" y="34" width="115" height="196" class="tail-region"/>
   <rect v-for="(value,index) in p" :key="index" :x="43+index*58" :y="230-180*value" width="28" :height="Math.max(0,180*value)" :class="index>=3?'tail-bar':'mass-bar'"/>
   <text v-for="(value,index) in p" :key="'mass'+index" :x="57+index*58" y="28" text-anchor="middle">{{fmt(value,3)}}</text>
   <text v-for="index in [0,1,2,3,4]" :key="index" :x="57+index*58" y="253" text-anchor="middle">{{index}}</text>
   <text x="333" y="275">X</text><text x="18" y="275">Tổng xác suất = {{fmt(summary.sum,4)}}</text>
  </svg>
  <p v-if="second" class="lab-lead">Đặt s = p₃, t = p₄. Mọi phân phối thỏa cả hai moment được biểu diễn bởi tam giác s ≥ 0, t ≥ 0, s + 2t ≤ 1/6. Đây là miền tham số, không phải biểu đồ vị trí của X.</p>
  <p v-else class="lab-lead">Ở chế độ chỉ biết trung bình, hình dưới minh họa một họ phân phối nối hai phân phối cực trị. Nó không liệt kê mọi phân phối có cùng trung bình, nhưng đi qua đủ cận đuôi nhỏ nhất và lớn nhất.</p>
  <svg ref="svg" :viewBox="second?'0 0 360 290':'0 0 360 180'" role="group" aria-label="Điểm tham số kéo được để đổi phân phối với moment được giữ nguyên" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <polygon v-if="second" :points="momentTriangle.map(p=>view.point(p).join(',')).join(' ')" class="parameter-region"/>
   <line v-else :x1="view.sx(0)" :x2="view.sx(1)" :y1="view.sy(.5)" :y2="view.sy(.5)" class="lab-axis"/>
   <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="7" class="lab-dot-accent"/>
   <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Tham số của phân phối xác suất" :aria-valuetext="second?fmtPoint(pair,6):fmt(theta,6)" @pointerdown="drag.start('distribution',$event)" @keydown="drag.key('distribution',point,$event)"/>
   <template v-if="second"><text :x="view.sx(0)-19" :y="view.sy(0)+21">0</text><text :x="view.sx(1/6)" :y="view.sy(0)+24" text-anchor="middle">1/6</text><text :x="view.sx(0)-10" :y="view.sy(1/12)+5" text-anchor="end">1/12</text><text x="329" :y="view.sy(0)+22">s</text><text :x="view.sx(0)+12" y="27">t</text></template>
   <template v-else><text :x="view.sx(0)" y="157" text-anchor="middle">0</text><text :x="view.sx(1)" y="157" text-anchor="middle">1</text><text x="12" y="23">Tỉ lệ trộn hai phân phối</text></template>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh phân phối bằng nút</summary><LabPointControls :svg="svg" :axes="second?'xy':'x'"/></details>
  <div class="lab-readout" role="status">
   <p>p = {{fmtPoint(p,5)}}. E[X] = {{fmt(summary.mean,6)}}, E[X²] = {{fmt(summary.second,6)}}.</p>
   <p>Xác suất đuôi P(X ≥ 3) = {{fmt(summary.tail,6)}}. Cận tốt nhất với thông tin đang chọn là {{second?'1/6 ≈ 0.166667':'1/3 ≈ 0.333333'}}.</p>
   <p v-if="second">Các moment và tổng xác suất được giữ bởi công thức tham số. Chỉ đổi s và t trong tam giác mới bảo đảm mọi pᵢ không âm.</p>
   <p v-if="second">Trên tập {0, 1, 2, 3, 4}, đa thức X(X − 1)/6 chặn trên chỉ thị của biến cố X ≥ 3. Kỳ vọng của đa thức bằng (2 − 1)/6 = 1/6, nên không có phân phối khả thi nào vượt cận này.</p>
   <p v-else>Vì X không âm, chỉ thị của biến cố X ≥ 3 không vượt X/3. Lấy kỳ vọng cho cận 1/3. Nút cực đại cho thấy cận ấy đạt được.</p>
   <p>Các số hiển thị được làm tròn. Khi trộn hai phân phối thỏa cùng các đẳng thức moment, phân phối mới tiếp tục thỏa các đẳng thức ấy vì kỳ vọng tuyến tính theo p.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Giữ chỉ thông tin trung bình rồi đạt xác suất đuôi lớn nhất. Moment bậc hai bằng bao nhiêu?</li><li>Thêm moment bậc hai, đi tới hai nút cực trị rồi kéo giữa chúng. Vì sao mọi giá trị đuôi ở giữa đều đạt được?</li><li>Ở tam giác tham số, p₄ tăng có nhất thiết làm xác suất đuôi lớn nhất tăng không?</li></ol></details>
 </figure>
</template>

<style scoped>
svg text{font-size:17px}
.tail-region{fill:var(--vang-soft);stroke:none}
.tail-bar{fill:var(--vang)}.mass-bar{fill:var(--tim)}
.parameter-region{fill:var(--tim-soft);stroke:var(--tim);stroke-width:1.5}
svg :is(line,polyline,polygon,rect,path,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
