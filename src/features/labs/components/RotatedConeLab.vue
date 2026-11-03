<script setup>
import { computed, ref } from 'vue'
import { createDragger, fmt, makeView } from '../controllers/svg-drag.js'
import LabPointControls from './LabPointControls.vue'

const svg = ref(null)
const point = ref([2,2])
const magnitude = ref(1.5)
const view = makeView({x0:0,x1:4,y0:0,y1:4,width:360,height:300,pad:35})
const P = view.point
const drag = createDragger(svg, ref(view), (_, next)=>{ point.value=next }, {step:.05})
const bound = computed(()=>magnitude.value**2)
const edge = computed(()=>{
 if (bound.value===0) return [[0,4],[0,0],[4,0]]
 const start = bound.value / 4
 return Array.from({length:81},(_,i)=>{
  const y = start+(4-start)*i/80
  return [y,bound.value/y]
 })
})
const region = computed(()=>[...edge.value,[4,4]].map(P).join(' '))
const product = computed(()=>point.value[0]*point.value[1])
const feasible = computed(()=>product.value >= bound.value-1e-9)
</script>

<template>
 <figure class="study-lab" aria-label="Lát cắt của nón xoay trong mặt phẳng y và z">
  <figcaption class="lab-title">Giữ độ dài của x và kéo cặp (y, z)</figcaption>
  <p class="lab-lead">Miền xanh gồm những cặp không âm có tích yz ít nhất bằng bình phương độ dài của x. Đưa y về 0 và quan sát điều kiện ở biên.</p>
  <svg ref="svg" viewBox="0 0 360 300" role="group" aria-label="Miền tích yz và điểm kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <polygon :points="region" class="region"/>
   <line x1="26" x2="333" y1="265" y2="265" class="lab-axis"/>
   <line x1="35" x2="35" y1="25" y2="272" class="lab-axis"/>
   <text x="335" y="281">y</text><text x="49" y="27">z</text>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="6" :class="feasible?'lab-dot-accent':'lab-dot-bad'"/>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="28" class="lab-handle hit" tabindex="0" role="slider" aria-label="Cặp y và z" :aria-valuetext="fmt(point[0],4)+', '+fmt(point[1],4)" @pointerdown="drag.start('point',$event)" @keydown="drag.key('point',point,$event)"/>
  </svg>
  <div class="lab-buttons">
   <button type="button" @click="magnitude=1.5;point=[2,2]">Độ dài x bằng 1.5</button>
   <button type="button" @click="magnitude=0;point=[0,2]">Biên x = 0, y = 0</button>
   <button type="button" @click="magnitude=1.5;point=[0,2]">Biên x khác 0, y = 0</button>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-readout" role="status">
   <p>y = {{fmt(point[0],3)}}, z = {{fmt(point[1],3)}}. Tích yz = {{fmt(product,3)}} và bình phương độ dài của x = {{fmt(bound,3)}}. {{feasible?'Thỏa điều kiện nón xoay.':'Vi phạm điều kiện nón xoay.'}}</p>
   <p v-if="point[0]===0">Tại y = 0, điều kiện tích chỉ cho phép x = 0. Biểu thức chia cho y không xác định ở đây.</p>
  </div>
 </figure>
</template>

<style scoped>
svg text{font-size:18px;pointer-events:none}
.region{fill:var(--xanh-soft);stroke:var(--xanh);stroke-width:1.4}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
