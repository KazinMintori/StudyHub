<script setup>
import { computed, ref } from 'vue'
import { createDragger, fmt, fmtPoint, makeView } from '../controllers/svg-drag.js'
import { project3 } from '../services/foundation-geometry.mjs'
import LabPointControls from './LabPointControls.vue'

const svg = ref(null)
const point = ref([.6, 1.2])
const height = ref(0)
const view = makeView({x0:-2.4,x1:2.4,y0:-2.4,y1:2.4,width:360,height:360,pad:30})
const P = view.point
const drag = createDragger(svg, ref(view), (_, next) => { point.value = next }, {step:.05})
const norm = computed(() => Math.hypot(point.value[0], height.value))
const state = computed(() => point.value[1] >= norm.value - 1e-9
 ? 'Thuộc nón trên'
 : point.value[1] <= -norm.value + 1e-9 ? 'Chỉ thỏa bất đẳng thức đã bình phương' : 'Nằm ngoài cả hai miền')

const boundary = computed(() => {
 const extent = Math.sqrt(2.4 ** 2 - height.value ** 2)
 return Array.from({length:65}, (_, i) => {
  const x = extent * (i / 32 - 1)
  return [x, Math.hypot(x, height.value)]
 })
})
function region(sign) {
 const edge = boundary.value
 return [...edge.map(([x,t])=>[x,sign*t])].map(P).join(' ')
}
const camera = {yaw:25,pitch:23,scale:49,origin:[180,165]}
const S = p => project3(p,camera)
const ring = sign => Array.from({length:65},(_,i)=>{
 const angle = i * Math.PI / 32
 return [2.4*Math.cos(angle),2.4*Math.sin(angle),sign*2.4]
})
const mesh = sign => ring(sign).filter((_,i)=>i<64&&i%8===0)
const rings = [ring(1),ring(-1)]
const scenePoint = computed(()=>S([point.value[0],height.value,point.value[1]]))
const slice = computed(()=>[[-2.4,height.value,-2.4],[2.4,height.value,-2.4],[2.4,height.value,2.4],[-2.4,height.value,2.4]].map(S).join(' '))
</script>

<template>
 <figure class="study-lab" aria-label="Lát cắt của nón bậc hai và miền thừa sau khi bình phương">
  <figcaption class="lab-title">Điều kiện t ≥ 0 chọn nửa nón trên</figcaption>
  <p class="lab-lead">Kéo điểm trong lát cắt để thay y₁ và t. Hai hình dùng chung điểm (y₁, y₂, t). Đổi y₂ để xem lát qua trục hoặc lát lệch khỏi trục.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 360 360" role="group" aria-label="Lát cắt hai chiều có điểm kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <polygon :points="region(1)" class="upper"/>
    <polygon :points="region(-1)" class="lower"/>
    <line x1="22" x2="334" y1="180" y2="180" class="lab-axis"/>
    <line x1="180" x2="180" y1="22" y2="335" class="lab-axis"/>
    <text x="334" y="205">y₁</text><text x="193" y="28">t</text>
    <circle :cx="P(point)[0]" :cy="P(point)[1]" r="6" class="lab-dot-accent"/>
    <circle :cx="P(point)[0]" :cy="P(point)[1]" r="28" class="lab-handle hit" role="slider" tabindex="0" aria-label="Điểm (y1, t) trong lát cắt" :aria-valuetext="fmtPoint(point,4)" @pointerdown="drag.start('point',$event)" @keydown="drag.key('point',point,$event)"/>
   </svg>
   <svg viewBox="0 0 360 330" role="img" aria-label="Hai nửa nón trong không gian ba chiều cùng mặt phẳng lát cắt">
    <polygon :points="slice" class="slice"/>
    <template v-for="(sign,i) in [1,-1]" :key="sign">
     <polyline :points="rings[i].map(S).join(' ')" fill="none" :class="sign===1?'upper-line':'lower-line'"/>
     <line v-for="(edge,j) in mesh(sign)" :key="j" x1="180" y1="165" :x2="S(edge)[0]" :y2="S(edge)[1]" :class="sign===1?'upper-line':'lower-line'"/>
    </template>
    <polyline v-for="sign in [1,-1]" :key="`section-${sign}`" :points="boundary.map(([x,t])=>S([x,height,sign*t]).join(',')).join(' ')" fill="none" :class="sign===1?'upper-section':'lower-section'"/>
    <line v-for="(end,i) in [[2.8,0,0],[0,2.8,0]]" :key="i" x1="180" y1="165" :x2="S(end)[0]" :y2="S(end)[1]" class="lab-axis"/>
    <text :x="S([2.8,0,0])[0]+6" :y="S([2.8,0,0])[1]+18">y₁</text>
    <text :x="S([0,2.8,0])[0]-10" :y="S([0,2.8,0])[1]+20" text-anchor="end">y₂</text>
    <line x1="180" x2="180" y1="35" y2="295" class="lab-axis"/>
    <text x="193" y="31">t</text>
    <circle :cx="scenePoint[0]" :cy="scenePoint[1]" r="6" class="lab-dot-accent"/>
   </svg>
  </div>
  <div class="lab-buttons">
   <button type="button" :aria-pressed="height===0" @click="height=0">Lát y₂ = 0</button>
   <button type="button" :aria-pressed="height===1" @click="height=1">Lát y₂ = 1</button>
   <button type="button" @click="point=[.6,-1.2]">Điểm trong nón dưới</button>
   <button type="button" @click="point=[.6,1.2]">Điểm trong nón trên</button>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh điểm bằng nút</summary><LabPointControls :svg="svg"/></details>
  <p class="lab-legend"><span class="legend-good">Miền thỏa chuẩn ≤ t</span><span class="legend-bad">Miền thừa sau khi bình phương</span></p>
  <div class="lab-readout" role="status">
   <p>(y₁, y₂, t) = {{fmtPoint([point[0],height,point[1]],3)}}. Chuẩn của (y₁, y₂) bằng {{fmt(norm,3)}}. {{state}}.</p>
   <p>Bình phương cho điều kiện chuẩn ≤ |t|. Hai nửa nón cùng thỏa điều kiện đó. Mặt phẳng tím giữ y₂ cố định, còn đường ngang trong lát cắt biểu diễn t = 0.</p>
   <p>Trong hình R³, hai đường đậm là giao tuyến của mặt phẳng tím với mặt nón. Chúng tương ứng với hai đường biên trên lát cắt bên trái. Tọa độ được chiếu lên màn hình, nên dùng số đọc để kiểm tra độ dài.</p>
  </div>
 </figure>
</template>

<style scoped>
svg text{font-size:18px;pointer-events:none}
.upper{fill:var(--xanh-soft);stroke:var(--xanh);stroke-width:1.4}
.lower{fill:var(--do-soft);stroke:var(--do);stroke-width:1.4}
.slice{fill:var(--tim-soft);fill-opacity:.35;stroke:var(--tim);stroke-width:1}
.upper-line{stroke:var(--xanh);stroke-width:.8}
.lower-line{stroke:var(--do);stroke-width:.8}
.upper-section{stroke:var(--xanh);stroke-width:1.8}
.lower-section{stroke:var(--do);stroke-width:1.8}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
