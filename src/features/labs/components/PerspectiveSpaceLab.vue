<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3,unprojectPlane} from '../services/foundation-geometry.mjs'
const svg=ref(null),center=ref([.5,.2]),depth=ref(2.5)
const camera={yaw:25,pitch:27,scale:54,origin:[195,260]}
const P=p=>project3(p,camera)
const image=p=>[p[0]/p[2],p[1]/p[2],1]
const object=computed(()=>[[-.65,-.5],[.65,-.5],[.65,.5],[-.65,.5]].map(p=>[p[0]+center.value[0],p[1]+center.value[1],depth.value]))
const point=computed(()=>[...center.value,depth.value])
const projected=computed(()=>image(point.value))
const view=computed(()=>({x0:-1.2,x1:1.2,y0:-1.2,y1:1.2,toWorld:(x,y)=>unprojectPlane([x,y],depth.value,camera)}))
const drag=createDragger(svg,view,(_,p)=>{center.value=p},{step:.1,snap:.01})
const path=points=>points.map(p=>P(p).join(',')).join(' ')
</script>
<template>
 <figure class="study-lab" aria-label="Vật thể trong R³ chiếu xuyên tâm lên mặt phẳng t bằng 1">
  <figcaption class="lab-title">Phối cảnh trong R³: Cùng kích thước, xa hơn thì ảnh nhỏ hơn</figcaption>
  <p class="lab-lead">Kéo tâm hình chữ nhật trong mặt phẳng có độ sâu t cố định. Đổi t để đưa vật ra xa. Mỗi tia từ O qua một đỉnh gặp mặt phẳng t = 1 tại đỉnh ảnh tương ứng.</p>
  <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Hình chữ nhật, ảnh của nó và bốn tia qua gốc trong không gian ba chiều" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <polygon :points="path([[-2,-1.5,1],[2,-1.5,1],[2,1.5,1],[-2,1.5,1]])" class="screen"/>
   <line :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P([0,0,4])[0]" :y2="P([0,0,4])[1]" class="lab-axis"/>
   <line v-for="(p,i) in object" :key="i" :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(p)[0]" :y2="P(p)[1]" class="lab-guide"/>
   <polygon :points="path(object.map(image))" class="lab-good-fill"/><polygon :points="path(object)" class="lab-region"/>
   <circle :cx="P(projected)[0]" :cy="P(projected)[1]" r="5" class="lab-dot"/><circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" class="lab-dot-accent"/>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="30" class="lab-handle hit" tabindex="0" role="slider" aria-label="Tâm vật trong lát có độ sâu t cố định" :aria-valuetext="fmtPoint(point,3)" @pointerdown="drag.start('center',$event)" @keydown="drag.key('center',center,$event)"/>
   <text :x="P([0,0,0])[0]-10" :y="P([0,0,0])[1]+25">O</text><text x="32" y="34">Vật</text><text x="370" y="256" text-anchor="end">t = 1</text><text :x="P([0,0,4])[0]+12" :y="P([0,0,4])[1]+7">t</text>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-controls"><label>Độ sâu t = {{fmt(depth)}}<input v-model.number="depth" type="range" min="1.4" max="3.6" step=".1"/></label></div>
  <div class="lab-readout" role="status"><p>Tâm vật x = {{fmtPoint(point)}}. Ảnh P(x) = {{fmtPoint(projected.slice(0,2))}}.</p><p>Kích thước ngang và dọc của ảnh bằng 1/t = {{fmt(1/depth,3)}} lần kích thước vật. Diện tích ảnh bằng 1/t² = {{fmt(1/depth**2,3)}} lần diện tích vật.</p><p>Đây là mặt phẳng ảnh ảo ở phía trước O, thuận tiện để dùng P(z,t) = z/t. Máy ảnh lỗ kim có màn thật phía sau O cho ảnh đảo dấu. Các mảnh mặt phẳng chỉ giới hạn vùng vẽ.</p></div>
 </figure>
</template>
<style scoped>
svg text{font-size:20px;pointer-events:none}.screen{fill:var(--canvas);fill-opacity:.7;stroke:var(--ink-3);stroke-width:1;stroke-dasharray:5 5}.hit{fill:transparent!important;stroke:transparent}.hit:focus-visible{stroke:var(--vang)}svg :is(line,polygon,circle:not(.hit)){pointer-events:none}
</style>
