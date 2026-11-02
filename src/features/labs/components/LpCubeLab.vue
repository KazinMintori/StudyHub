<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3,planeBoxSection} from '../services/foundation-geometry.mjs'
import {cubeLp} from '../services/linear-program-geometry.mjs'

const svg=ref(null),c=ref([1,1,1]),yaw=ref(32)
const model=computed(()=>cubeLp(c.value))
const camera=computed(()=>({yaw:yaw.value,pitch:28,scale:116,origin:[180,177]}))
const P=p=>project3(p.map(value=>value-.5),camera.value)
const poly=points=>points.map(p=>P(p).join(',')).join(' ')
const edges=Array.from({length:8},(_,i)=>[1,2,4].filter(bit=>(i&bit)===0).map(bit=>[i,i|bit])).flat()
const faces=[[0,1,3,2],[4,5,7,6],[0,1,5,4],[2,3,7,6],[0,2,6,4],[1,3,7,5]]
const optimalFaces=computed(()=>faces.filter(face=>face.every(index=>model.value.best.includes(index))))
const section=computed(()=>{
 if(model.value.dimension===3)return []
 const offset=model.value.value-c.value.reduce((a,b)=>a+b,0)/2
 return planeBoxSection(c.value,offset,.72).map(p=>p.map(value=>value+.5))
})
const control=makeView({x0:-1.5,x1:1.5,y0:-1.5,y1:1.5,width:360,height:270,pad:36})
const controlView=computed(()=>control)
const drag=createDragger(svg,controlView,(_,p)=>{c.value=[...p,c.value[2]]},{step:.05})
const name=computed(()=>['Một đỉnh','Một cạnh','Một mặt','Toàn khối'][model.value.dimension])
function choose(p){c.value=p}
</script>

<template>
 <figure class="study-lab" aria-label="LP trên khối lập phương trong R³ và số chiều của tập nghiệm tối ưu">
  <figcaption class="lab-title">Trong R³, nghiệm tối ưu có thể là một đỉnh, cạnh, mặt hoặc toàn khối</figcaption>
  <p class="lab-lead">Miền khả thi là khối [0, 1]³. Kéo c₁ và c₂ trên hình điều khiển, rồi chọn c₃ bằng nút. Mặt phẳng màu vàng có phương trình cᵀx = p*, tựa vào khối tại toàn bộ tập nghiệm.</p>
  <svg viewBox="0 0 360 330" role="img" aria-label="Khối lập phương, mặt phẳng mức tối ưu và đỉnh cạnh hoặc mặt được chọn">
   <polygon v-if="section.length>=3" :points="poly(section)" class="support"/>
   <polygon v-for="(face,index) in optimalFaces" :key="index" :points="poly(face.map(i=>model.vertices[i]))" class="optimal-face"/>
   <line v-for="([a,b],index) in edges" :key="index" :x1="P(model.vertices[a])[0]" :y1="P(model.vertices[a])[1]" :x2="P(model.vertices[b])[0]" :y2="P(model.vertices[b])[1]" :class="model.best.includes(a)&&model.best.includes(b)?'optimal-edge':'cube-edge'"/>
   <circle v-for="index in model.best" :key="index" :cx="P(model.vertices[index])[0]" :cy="P(model.vertices[index])[1]" r="5" class="lab-dot-warn"/>
   <line v-for="(end,index) in [[1.35,0,0],[0,1.35,0],[0,0,1.35]]" :key="index" :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(end)[0]" :y2="P(end)[1]" class="lab-axis"/>
   <text :x="P([1.35,0,0])[0]+9" :y="P([1.35,0,0])[1]+18">x₁</text>
   <text :x="P([0,1.35,0])[0]-26" :y="P([0,1.35,0])[1]+18">x₂</text>
   <text :x="P([0,0,1.35])[0]+8" :y="P([0,0,1.35])[1]">x₃</text>
  </svg>
  <div class="lab-buttons" role="group" aria-label="Đổi góc nhìn hình học khối">
   <button type="button" :aria-pressed="yaw===32" @click="yaw=32">Góc nhìn thứ nhất</button>
   <button type="button" :aria-pressed="yaw===-32" @click="yaw=-32">Góc nhìn thứ hai</button>
  </div>
  <svg ref="svg" viewBox="0 0 360 270" role="group" aria-label="Kéo hai hệ số c1 và c2 của mục tiêu tuyến tính" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line x1="28" :y1="control.sy(0)" x2="330" :y2="control.sy(0)" class="lab-axis"/>
   <line :x1="control.sx(0)" y1="26" :x2="control.sx(0)" y2="240" class="lab-axis"/>
   <line :x1="control.sx(0)" :y1="control.sy(0)" :x2="control.sx(c[0])" :y2="control.sy(c[1])" class="coefficient"/>
   <circle :cx="control.sx(c[0])" :cy="control.sy(c[1])" r="7" class="lab-dot-accent"/>
   <circle :cx="control.sx(c[0])" :cy="control.sy(c[1])" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Hai hệ số c1 và c2" :aria-valuetext="fmtPoint(c,4)" @pointerdown="drag.start('c',$event)" @keydown="drag.key('c',c,$event)"/>
   <text x="331" :y="control.sy(0)+22">c₁</text><text :x="control.sx(0)+10" y="23">c₂</text>
   <text x="17" y="258">c₃ hiện tại = {{fmt(c[2],2)}}</text>
  </svg>
  <details class="lab-tasks"><summary>Đổi c₁ và c₂ bằng nút</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-buttons" role="group" aria-label="Hệ số thứ ba của mục tiêu">
   <button v-for="value in [-1,0,1]" :key="value" type="button" :aria-pressed="c[2]===value" @click="c=[c[0],c[1],value]">c₃ = {{value}}</button>
  </div>
  <div class="lab-buttons" role="group" aria-label="Số chiều của tập nghiệm LP">
   <button type="button" @click="choose([1,1,1])">Một đỉnh tối ưu</button>
   <button type="button" @click="choose([1,1,0])">Một cạnh tối ưu</button>
   <button type="button" @click="choose([1,0,0])">Một mặt tối ưu</button>
   <button type="button" @click="choose([0,0,0])">Toàn khối tối ưu</button>
   <button type="button" @click="choose([-1,1,-1])">Đổi dấu hai hệ số</button>
  </div>
  <div class="lab-readout" role="status">
   <p>c = {{fmtPoint(c,4)}}. Giá trị tối ưu p* = {{fmt(model.value,6)}}. {{name}} là tập nghiệm, có số chiều {{model.dimension}}.</p>
   <p>Một nghiệm là {{fmtPoint(model.point,2)}}. Có {{model.best.length}} đỉnh của khối đạt cùng giá trị tối ưu.</p>
   <p>Mỗi số hạng cᵢxᵢ được tối ưu riêng trên 0 ≤ xᵢ ≤ 1. Nếu cᵢ &gt; 0 thì xᵢ = 0, nếu cᵢ &lt; 0 thì xᵢ = 1. Nếu cᵢ = 0, tọa độ ấy được tự do trên cả đoạn [0, 1].</p>
   <p v-if="model.dimension===3">Khi c = 0, mọi điểm trong khối đều tối ưu. Không có một mặt phẳng mức riêng để vẽ, vì phương trình 0 = 0 đúng trên toàn không gian.</p>
   <p>So sánh bằng số dùng dung sai {{model.tolerance.toExponential(1)}}. Hình 3D là phép chiếu trực giao, không dùng để đo góc hay khoảng cách.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Từ một đỉnh tối ưu, cho c₃ bằng 0. Vì sao tập nghiệm trở thành một cạnh?</li><li>Cho thêm c₂ bằng 0. Hai tọa độ tự do tạo thành mặt nào?</li><li>Đổi góc nhìn rồi đọc lại tọa độ nghiệm. Đại lượng nào giữ nguyên?</li></ol></details>
 </figure>
</template>

<style scoped>
svg text{font-size:18px}
.support{fill:var(--vang-soft);stroke:var(--vang);stroke-width:1.1;fill-opacity:.4}
.optimal-face{fill:var(--xanh-soft);stroke:var(--xanh);stroke-width:1}
.cube-edge{stroke:var(--ink-2);stroke-width:1.3}
.optimal-edge{stroke:var(--xanh);stroke-width:2.4}
.coefficient{stroke:var(--tim);stroke-width:2}
svg :is(line,polyline,polygon,path,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
