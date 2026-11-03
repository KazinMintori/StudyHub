<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, makeView } from '../controllers/svg-drag.js'

const svg = ref(null)
const point = ref([1,2])
const view = makeView({x0:-2.3,x1:2.3,y0:-1,y1:5,width:360,height:330,pad:30})
const drag = createDragger(svg,ref(view),(_,next)=>{point.value=next},{step:.05,snap:.01})
const boundary = Array.from({length:101},(_,i)=>{
  const x = Math.sqrt(5)*(i/50-1)
  return view.point([x,x*x]).join(',')
}).join(' ')
const marker = computed(()=>view.point(point.value))
const margin = computed(()=>point.value[1]-point.value[0]**2)
</script>

<template>
 <figure class="study-lab" aria-label="Miền phía trên parabol của một bất đẳng thức ma trận">
  <figcaption class="lab-title">Kéo điểm để thử một bất đẳng thức ma trận</figcaption>
  <p class="lab-lead">Ma trận có hàng đầu (1, x) và hàng sau (x, y). Miền tô tím gồm các điểm làm ma trận nửa xác định dương. Kéo chấm qua đường biên để quan sát định thức đổi dấu.</p>
  <svg ref="svg" viewBox="0 0 360 330" role="group" aria-label="Epigraph của x bình phương, có điểm thử kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <polygon :points="boundary" class="lab-region"/>
   <line x1="30" x2="330" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis"/>
   <line x1="180" x2="180" y1="30" y2="300" class="lab-axis"/>
   <text x="325" :y="view.sy(0)+22">x</text><text x="191" y="23">y</text>
   <circle :cx="marker[0]" :cy="marker[1]" r="6" :class="margin>=-1e-10?'lab-dot-accent':'lab-dot-bad'"/>
   <circle :cx="marker[0]" :cy="marker[1]" r="28" class="lab-handle hit" role="slider" tabindex="0" aria-label="Điểm thử x và y" :aria-valuetext="fmt(point[0],3)+', '+fmt(point[1],3)" @pointerdown="drag.start('p',$event)" @keydown="drag.key('p',point,$event)"/>
  </svg>
  <div class="lab-buttons">
   <button type="button" @click="point=[1,2]">Điểm (1, 2)</button>
   <button type="button" @click="point=[2,3]">Điểm (2, 3)</button>
   <button type="button" @click="point=[1,1]">Điểm trên biên</button>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-readout" role="status">
   <p>x = {{fmt(point[0],3)}}, y = {{fmt(point[1],3)}}. Định thức y − x² = {{fmt(margin,4)}}. {{margin>=-1e-10?'Ma trận nửa xác định dương.':'Ma trận có trị riêng âm.'}}</p>
   <p>Với vector v = (−x, 1), dạng toàn phương bằng đúng y − x². Khi điểm nằm dưới parabol, vector này chứng minh ma trận vi phạm điều kiện PSD.</p>
  </div>
 </figure>
</template>

<style scoped>
svg text{font-size:18px;pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
