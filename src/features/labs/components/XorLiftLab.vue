<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt} from '../controllers/svg-drag.js'
import {project3} from '../services/foundation-geometry.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'
const svg=ref(null),lift=ref(0),yaw=ref(30)
const camera=computed(()=>({yaw:yaw.value,pitch:30,scale:146,origin:[173,174]}))
const P=p=>project3(p,camera.value)
const points=computed(()=>[[0,0,0],[1,1,lift.value],[1,0,0],[0,1,0]])
const plane=[[0,0,-.25],[1,0,.25],[1,1,.75],[0,1,.25]]
const names=['A','B','C','D']
const labels=computed(()=>placePointLabels(points.value.map((p,i)=>({key:names[i],text:names[i],point:P(p)})),{width:400,height:340}))
const value=p=>p[0]+p[1]-2*p[2]-.5
const separated=computed(()=>lift.value>.75)
// This control changes the camera only; data coordinates stay fixed.
const cameraView=ref({x0:0,x1:1,y0:0,y1:1,toWorld:(x,y)=>[(x-80)/240,y/340]})
const cameraHandle=computed(()=>[80+240*(yaw.value+20)/90,306])
const drag=createDragger(svg,cameraView,(_,p)=>{yaw.value=-20+90*p[0]},{step:.05})
const poly=points=>points.map(p=>P(p).join(',')).join(' ')
</script>
<template>
 <figure class="study-lab" aria-label="XOR được nâng từ R² sang R³ nhờ đặc trưng tích">
  <figcaption class="lab-title">XOR: Nâng một điểm để hai bao lồi không còn cắt nhau</figcaption>
  <p class="lab-lead">Ở R², đoạn AB cắt đoạn CD. Thêm đặc trưng x₃ = x₁x₂ đưa riêng B lên cao. Kéo nút góc nhìn để xoay hình. Thanh nâng chỉ nội suy quá trình, tại mức 1 mới là đặc trưng tích đầy đủ.</p>
  <div class="lab-buttons" role="group" aria-label="Không gian đặc trưng XOR"><button type="button" :aria-pressed="lift===0" @click="lift=0">R²: XOR chưa tách được</button><button type="button" :aria-pressed="lift===1" @click="lift=1">R³: Thêm đặc trưng tích</button></div>
  <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Hai đoạn bao lồi của bốn điểm XOR và mảnh mặt phẳng phân lớp" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <polygon :points="poly([[0,0,0],[1,0,0],[1,1,0],[0,1,0]])" class="floor"/>
   <polygon :points="poly(plane)" class="boundary"/>
   <line :x1="P(points[0])[0]" :y1="P(points[0])[1]" :x2="P(points[1])[0]" :y2="P(points[1])[1]" class="lab-accent"/>
   <line :x1="P(points[2])[0]" :y1="P(points[2])[1]" :x2="P(points[3])[0]" :y2="P(points[3])[1]" class="lab-good"/>
   <g v-for="(p,i) in points" :key="i"><circle v-if="i<2" :cx="P(p)[0]" :cy="P(p)[1]" r="7" class="lab-dot-accent"/><rect v-else :x="P(p)[0]-6" :y="P(p)[1]-6" width="12" height="12" class="square"/><text :x="labels[names[i]].x" :y="labels[names[i]].y" :text-anchor="labels[names[i]].anchor">{{names[i]}}</text></g>
   <text x="20" y="275">Góc nhìn {{fmt(yaw,0)}}°</text><line x1="80" x2="320" y1="306" y2="306" class="lab-line"/><circle :cx="cameraHandle[0]" cy="306" r="7" class="lab-dot-warn"/><circle :cx="cameraHandle[0]" cy="306" r="28" class="lab-handle hit" tabindex="0" role="slider" aria-label="Góc nhìn ba chiều của hình XOR" :aria-valuetext="fmt(yaw,3)" @pointerdown="drag.start('yaw',$event)" @keydown="drag.key('yaw',[(yaw+20)/90,.5],$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-controls"><label>Mức nâng x₃ = {{fmt(lift)}}·x₁x₂<input v-model.number="lift" type="range" min="0" max="1" step=".05"/></label></div>
  <div class="lab-readout" role="status"><p>Mặt phẳng vẽ có phương trình x₁ + x₂ − 2x₃ = 1/2. Giá trị f = x₁ + x₂ − 2x₃ − 1/2 tại A, B, C, D lần lượt là {{points.map(p=>fmt(value(p))).join(', ')}}.</p><p :class="separated?'is-good':'is-bad'">{{separated?'Mặt phẳng đang vẽ tách A, B ở phía f < 0 khỏi C, D ở phía f > 0.':'Mặt phẳng đang vẽ chưa tách nghiêm ngặt hai nhóm.'}}</p><p v-if="lift>0&&!separated">Với mức nâng dương, hai bao lồi đã rời nhau và có thể tìm mặt phẳng khác để tách. Mặt phẳng cố định đang minh họa chỉ tách được khi mức nâng lớn hơn 3/4.</p><p>Đây là thay đổi đặc trưng dữ liệu. Đổi góc nhìn trên màn hình không tự biến dữ liệu không phân tách được thành dữ liệu phân tách được.</p></div>
 </figure>
</template>
<style scoped>
svg text{font-size:20px;pointer-events:none}.floor{fill:var(--canvas);stroke:var(--ink-3);stroke-width:1;stroke-dasharray:4 4}.boundary{fill:var(--vang-soft);fill-opacity:.65;stroke:var(--vang);stroke-width:1.4}.square{fill:var(--xanh)}.hit{fill:transparent!important;stroke:transparent}.hit:focus-visible{stroke:var(--vang)}svg :is(line,polygon,rect,circle:not(.hit)){pointer-events:none}
</style>
