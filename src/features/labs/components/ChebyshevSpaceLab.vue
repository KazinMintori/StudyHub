<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3,unprojectPlane} from '../services/foundation-geometry.mjs'
import {polyhedronInBox,dot} from '../services/convex-geometry.mjs'
import {chebyshevShapes,chebyshevModel} from '../services/lp-models-geometry.mjs'

const svg=ref(null),radiusSvg=ref(null),center=ref([1.5,1.5]),radius=ref(1),yaw=ref(32)
const constraints=chebyshevShapes.pentagon,model=chebyshevModel(constraints)
const camera=computed(()=>({yaw:yaw.value,pitch:28,scale:44,origin:[180,205]}))
const P=(p,r=0)=>project3([p[0]-1.7,p[1]-1.7,r],camera.value)
const world=computed(()=>({x0:-.3,x1:4.3,y0:-.3,y1:4.3,toWorld:(x,y)=>{
 const p=unprojectPlane([x,y],radius.value,camera.value);return [p[0]+1.7,p[1]+1.7]
}}))
const drag=createDragger(svg,world,(_,p)=>{center.value=p},{step:.05})
const rail=makeView({x0:-.05,x1:2.05,y0:0,y1:1,width:360,height:110,pad:28})
const radiusView=computed(()=>rail)
const radiusDrag=createDragger(radiusSvg,radiusView,(_,p)=>{radius.value=Math.max(0,Math.min(2,p[0]))},{step:.025})
const slice=r=>polyhedronInBox(constraints.map(({a,b})=>({a,b:b-r*Math.hypot(...a)})),[-.3,4.3,-.3,4.3])
const serialize=(points,r)=>points.map(p=>P(p,r).join(',')).join(' ')
const levels=[0,model.radius/3,2*model.radius/3]
const chosenSlice=computed(()=>radius.value>model.radius+1e-9?[]:slice(radius.value))
const residuals=computed(()=>constraints.map(({a,b})=>a[0]*center.value[0]+a[1]*center.value[1]+radius.value*Math.hypot(...a)-b))
const feasible=computed(()=>residuals.value.every(value=>value<=1e-9))
function optimal(){center.value=[...model.center];radius.value=model.radius}
</script>
<template>
 <figure class="study-lab" aria-label="Miền khả thi của LP tâm Chebyshev trong không gian hai tọa độ tâm và bán kính">
  <figcaption class="lab-title">Quả cầu ở mặt phẳng, nhưng bài toán LP có ba biến</figcaption>
  <p class="lab-lead">Với ngũ giác ban đầu, mỗi điểm trong hình này là bộ (x_c₁, x_c₂, r). Đa giác ở một độ cao r cho biết các tâm có thể chứa đường tròn bán kính ấy. Kéo điểm tím trong mặt phẳng ngang đang chọn, rồi kéo bán kính trên đoạn bên dưới.</p>
  <svg ref="svg" viewBox="0 0 360 330" role="group" aria-label="Các lát tâm khả thi theo bán kính và điểm thử ba biến kéo được ở độ cao cố định" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <polygon v-for="(r,index) in levels" :key="index" :points="serialize(slice(r),r)" class="slice-outline"/>
   <polygon v-if="chosenSlice.length>=3" :points="serialize(chosenSlice,radius)" class="chosen-slice"/>
   <line :x1="P(center,0)[0]" :y1="P(center,0)[1]" :x2="P(center,radius)[0]" :y2="P(center,radius)[1]" class="lab-guide"/>
   <line :x1="P(model.center,0)[0]" :y1="P(model.center,0)[1]" :x2="P(model.center,model.radius)[0]" :y2="P(model.center,model.radius)[1]" class="lab-guide"/>
   <circle :cx="P(model.center,model.radius)[0]" :cy="P(model.center,model.radius)[1]" r="5" class="lab-dot-warn"/>
   <circle :cx="P(center,radius)[0]" :cy="P(center,radius)[1]" r="7" :class="feasible?'lab-dot-accent':'lab-dot-bad'"/>
   <circle :cx="P(center,radius)[0]" :cy="P(center,radius)[1]" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Hai tọa độ tâm trong lát bán kính cố định" :aria-valuetext="fmtPoint(center,5)" @pointerdown="drag.start('center',$event)" @keydown="drag.key('center',center,$event)"/>
   <line v-for="(end,index) in [[[4.35,0],0],[[0,4.35],0],[[0,0],2.2]]" :key="index" :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P(end[0],end[1])[0]" :y2="P(end[0],end[1])[1]" class="lab-axis"/>
   <text :x="P([4.35,0])[0]-4" :y="P([4.35,0])[1]+18" text-anchor="end">x_c₁</text>
   <text :x="P([0,4.35])[0]-36" :y="P([0,4.35])[1]+18">x_c₂</text>
   <text :x="P([0,0],2.2)[0]+8" :y="P([0,0],2.2)[1]">r</text>
  </svg>
  <details class="lab-tasks"><summary>Di chuyển tâm bằng nút</summary><LabPointControls :svg="svg"/></details>
  <svg ref="radiusSvg" viewBox="0 0 360 110" role="group" aria-label="Bán kính r kéo trực tiếp từ không tới hai" @pointermove="radiusDrag.move" @pointerup="radiusDrag.end" @pointercancel="radiusDrag.end" @lostpointercapture="radiusDrag.end">
   <line :x1="rail.sx(0)" :y1="rail.sy(.5)" :x2="rail.sx(2)" :y2="rail.sy(.5)" class="lab-axis"/>
   <circle :cx="rail.sx(radius)" :cy="rail.sy(.5)" r="7" class="lab-dot-accent"/>
   <circle :cx="rail.sx(radius)" :cy="rail.sy(.5)" r="27" class="lab-handle hit" role="slider" tabindex="0" aria-label="Bán kính r của lát khả thi" :aria-valuetext="fmt(radius,5)" @pointerdown="radiusDrag.start('radius',$event)" @keydown="radiusDrag.key('radius',[radius,.5],$event)"/>
   <text x="14" y="20">Bán kính r</text><text :x="rail.sx(0)" y="96" text-anchor="middle">0</text><text :x="rail.sx(2)" y="96" text-anchor="middle">2</text>
  </svg>
  <details class="lab-tasks"><summary>Đổi bán kính bằng nút</summary><LabPointControls :svg="radiusSvg" axes="x"/></details>
  <div class="lab-buttons" role="group" aria-label="Các mức bán kính để đối chiếu">
   <button type="button" @click="radius=0">Bán kính bằng 0</button>
   <button type="button" @click="center=[1.5,1.5];radius=1">Một điểm khả thi</button>
   <button type="button" @click="optimal">Đỉnh tối ưu của LP</button>
   <button type="button" @click="radius=2">Bán kính quá lớn</button>
   <button type="button" @click="yaw=yaw===32?-32:32">Đổi góc nhìn</button>
  </div>
  <div class="lab-readout" role="status">
   <p>Điểm thử = {{fmtPoint([...center,radius],5)}}. {{feasible?'Năm bất đẳng thức đều thỏa.':'Có ít nhất một bất đẳng thức bị vi phạm.'}}</p>
   <p>Các vế trái trừ vế phải của LP là {{residuals.map(value=>fmt(value,5)).join(', ')}}. Giá trị dương cho biết đường tròn tương ứng không nằm trọn trong ngũ giác.</p>
   <p v-if="radius>model.radius+1e-9">Lát khả thi ở độ cao này rỗng. Đổi tâm không thể cứu một bán kính đã vượt giá trị tối ưu.</p>
   <p>Bán kính tối ưu {{fmt(model.radius,6)}}. Mỗi lớp mảnh là một lát bán kính khác nhau, không phải một mặt biên riêng của đa diện LP. Mục tiêu cực đại r là đi lên cao nhất trong miền khả thi.</p>
   <p>Phép chiếu R³ không bảo toàn khoảng cách hoặc góc. Kiểm khả thi dùng các bất đẳng thức số với dung sai 10⁻⁹, không suy từ việc điểm có vẻ nằm trên một miền tô hay không.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt r = 0. Miền tâm khả thi trở về tập nào?</li><li>Tăng r rồi kéo tâm. Vì sao đa giác tâm nhỏ dần?</li><li>Đặt r = 2. Vì sao không có thao tác kéo tâm nào làm đủ năm bất đẳng thức thỏa?</li></ol></details>
 </figure>
</template>
<style scoped>
svg text{font-size:17px}
.slice-outline{fill:none;stroke:var(--ink-3);stroke-width:1.1}
.chosen-slice{fill:var(--xanh-soft);stroke:var(--xanh);stroke-width:1.4}
svg :is(line,polyline,polygon,path,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
