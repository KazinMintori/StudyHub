<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, makeView } from '../controllers/svg-drag.js'
import { project3 } from '../services/foundation-geometry.mjs'

const svg = ref(null)
const point = ref([.7,1])
const c = ref(1)
const view = makeView({x0:-1.5,x1:1.5,y0:-1.5,y1:1.5,width:360,height:330,pad:37})
const drag = createDragger(svg,ref(view),(_,next)=>{point.value=next},{step:.05,snap:.01})
const marker = computed(()=>view.point(point.value))
const schur = computed(()=>c.value-.5)
const value = (u,v) => 2*(u+v/2)**2+schur.value*v*v
const minimum = computed(()=>schur.value*point.value[1]**2)
const optimumU = computed(()=>-point.value[1]/2)
const camera = {yaw:35,pitch:27,scale:66,origin:[180,219]}
const S = (u,v,z) => project3([u,v,z*.17],camera)
const coords = Array.from({length:49},(_,i)=>-1.5+i/16)
const mesh = computed(()=>[-1.5,-1,-.5,0,.5,1,1.5].flatMap(fixed=>[
 coords.map(u=>S(u,fixed,value(u,fixed)).join(',')).join(' '),
 coords.map(v=>S(fixed,v,value(fixed,v)).join(',')).join(' '),
]))
const slice = computed(()=>coords.map(u=>S(u,point.value[1],value(u,point.value[1])).join(',')).join(' '))
const floor = [[-1.5,-1.5],[1.5,-1.5],[1.5,1.5],[-1.5,1.5]].map(([u,v])=>S(u,v,0).join(',')).join(' ')
const current3 = computed(()=>S(...point.value,value(...point.value)))
const optimum3 = computed(()=>S(optimumU.value,point.value[1],minimum.value))
const zero3 = computed(()=>S(optimumU.value,point.value[1],0))
const optimum2 = computed(()=>view.point([optimumU.value,point.value[1]]))
function choose(next) { c.value=next; point.value=[.7,1] }
</script>

<template>
 <figure class="study-lab" aria-label="Cực tiểu theo một khối biến và hình dạng của phần bù Schur">
  <figcaption class="lab-title">Điểm thấp nhất của từng lát cho phần bù Schur</figcaption>
  <p class="lab-lead">Kéo điểm (u, v) trên hình R². Giá trị v chọn một lát trên mặt R³. Đường xanh giữ v cố định, và chấm vàng nằm ở u* = −v/2.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 360 330" role="group" aria-label="Mặt phẳng u v và điểm kéo" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <text x="37" y="23">Mặt phẳng (u, v)</text>
    <rect x="37" y="37" width="286" height="256" class="frame"/>
    <line x1="37" x2="323" y1="165" y2="165" class="lab-axis"/>
    <line x1="180" x2="180" y1="37" y2="293" class="lab-axis"/>
    <line x1="37" x2="323" :y1="marker[1]" :y2="marker[1]" class="slice"/>
    <line :x1="view.sx(.75)" :y1="view.sy(-1.5)" :x2="view.sx(-.75)" :y2="view.sy(1.5)" class="lab-guide"/>
    <text x="326" y="315">u</text><text x="18" y="53">v</text>
    <circle :cx="optimum2[0]" :cy="optimum2[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="marker[0]" :cy="marker[1]" r="6" class="lab-dot-accent"/>
    <circle :cx="marker[0]" :cy="marker[1]" r="28" class="lab-handle hit" role="slider" tabindex="0" aria-label="Điểm u và v" :aria-valuetext="fmt(point[0],3)+', '+fmt(point[1],3)" @pointerdown="drag.start('p',$event)" @keydown="drag.key('p',point,$event)"/>
   </svg>
   <svg viewBox="0 0 360 330" role="img" aria-label="Mặt dạng toàn phương, lát tại v cố định và điểm cực tiểu của lát">
    <text x="22" y="23">Mặt z = q(u, v)</text>
    <polygon :points="floor" class="frame"/>
    <polyline v-for="(line,index) in mesh" :key="index" :points="line" class="mesh"/>
    <polyline :points="slice" class="slice"/>
    <line v-if="Math.abs(minimum)>1e-9" :x1="zero3[0]" :y1="zero3[1]" :x2="optimum3[0]" :y2="optimum3[1]" class="lab-guide"/>
    <circle :cx="optimum3[0]" :cy="optimum3[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="current3[0]" :cy="current3[1]" r="6" class="lab-dot-accent"/>
   </svg>
  </div>
  <div class="lab-buttons">
   <button type="button" @click="choose(1)">Phần bù dương</button>
   <button type="button" @click="choose(.5)">Phần bù bằng 0</button>
   <button type="button" @click="choose(.25)">Phần bù âm</button>
   <button type="button" @click="point=[optimumU,point[1]]">Đưa u tới cực tiểu</button>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút</summary><LabPointControls :svg="svg"/></details>
  <p class="lab-legend"><span class="legend-accent">Điểm đang thử</span><span class="legend-warn">Cực tiểu khi giữ v</span><span class="legend-good">Lát tại v đang chọn</span></p>
  <div class="lab-readout" role="status">
   <p>q(u, v) = 2u² + 2uv + Cv² = 2(u + v/2)² + Sv².</p>
   <p>A = 2, B = 1, C = {{fmt(c,2)}}. Phần bù S = C − 1/2 = {{fmt(schur,2)}}. {{schur<0?'Ma trận có hướng âm.':schur===0?'Ma trận PSD và suy biến.':'Ma trận xác định dương.'}}</p>
   <p>u = {{fmt(point[0],3)}}, v = {{fmt(point[1],3)}}. Giá trị đang thử q = {{fmt(value(...point),4)}}. Khi giữ v, u* = {{fmt(optimumU,3)}} và q nhỏ nhất bằng Sv² = {{fmt(minimum,4)}}.</p>
   <p>Đường nét đứt trong R² là quỹ tích các điểm cực tiểu theo u. Khung mảnh trong R³ nằm ở z = 0. Khi S âm và v khác 0, chấm vàng nằm dưới khung đó.</p>
   <p>Độ cao trong hình R³ được nhân với 0.17 để giữ mặt trong khung. Dùng số đọc q và Sv² để so sánh giá trị dạng toàn phương.</p>
  </div>
 </figure>
</template>

<style scoped>
svg text{font-size:18px;pointer-events:none}
.frame,.mesh,.slice{fill:none;stroke-width:1}
.frame{stroke:var(--ink-3)}
.mesh{stroke:var(--tim);opacity:.55}
.slice{stroke:var(--xanh);stroke-width:2}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
