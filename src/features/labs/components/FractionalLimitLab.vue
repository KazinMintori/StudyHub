<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt} from '../controllers/svg-drag.js'
const svg=ref(null),z=ref(.25),kind=ref('unattained')
const view=makeView({x0:0,x1:1,y0:.8,y1:2.2,width:360,height:300,pad:35})
const dragView=computed(()=>({...view,toWorld:(x)=>[view.wx(x),1]}))
const drag=createDragger(svg,dragView,(_,p)=>{z.value=p[0]},{step:.025})
const f=t=>kind.value==='unattained'?1+t:1
const point=computed(()=>[z.value,f(z.value)])
const x=computed(()=>z.value>0?1/z.value-1:null)
</script>
<template>
 <figure class="study-lab" aria-label="Nghiệm tại z bằng không và vấn đề đạt giá trị tối ưu">
  <figcaption class="lab-title">z = 0: Điểm giới hạn có đủ để kết luận không đạt nghiệm?</figcaption>
  <p class="lab-lead">Xét x ≥ 0 và z = 1/(x + 1). Kéo chấm theo phương ngang về z = 0 để thấy x tiến ra vô cực. Đổi hàm mục tiêu để so sánh hai kết luận về khả năng đạt giá trị tối ưu.</p>
  <div class="lab-buttons"><button type="button" :aria-pressed="kind==='unattained'" @click="kind='unattained'">Tỉ số (x + 2)/(x + 1)</button><button type="button" :aria-pressed="kind==='constant'" @click="kind='constant'">Tỉ số (x + 1)/(x + 1)</button></div>
  <svg ref="svg" viewBox="0 0 360 300" role="group" aria-label="Mục tiêu sau đổi biến theo z, với đầu mút không ứng với x hữu hạn" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line x1="28" :y1="view.sy(1)" x2="328" :y2="view.sy(1)" class="lab-axis"/>
   <line :x1="view.sx(0)" y1="22" :x2="view.sx(0)" y2="274" class="lab-axis"/>
   <text x="337" :y="view.sy(1)-9">z</text><text x="47" y="24">Mục tiêu</text>
   <line :x1="view.sx(0)" :y1="view.sy(f(0))" :x2="view.sx(1)" :y2="view.sy(f(1))" class="objective"/>
   <circle :cx="view.sx(0)" :cy="view.sy(1)" r="6" class="limit"/>
   <circle :cx="view.sx(1)" :cy="view.sy(f(1))" r="5" class="lab-dot-good"/>
   <circle v-if="z>0" :cx="view.sx(z)" :cy="view.sy(f(z))" r="6" class="lab-dot-accent"/>
   <text :x="view.sx(0)" y="282" text-anchor="middle">0</text><text :x="view.sx(1)" y="282" text-anchor="middle">1</text>
   <circle :cx="view.sx(z)" :cy="view.sy(f(z))" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Biến z chỉ di chuyển ngang" :aria-valuetext="fmt(z,6)" @pointerdown="drag.start('z',$event)" @keydown="drag.key('z',point,$event)"/>
  </svg>
  <div class="lab-buttons"><button type="button" @click="z=0">Điểm giới hạn z = 0</button><button type="button" @click="z=.01">Một điểm rất xa</button><button type="button" @click="z=.5">Điểm hữu hạn x = 1</button></div>
  <details class="lab-tasks"><summary>Di chuyển z bằng nút</summary><LabPointControls :svg="svg" axes="x"/></details>
  <div class="lab-readout" role="status">
   <p>z = {{fmt(z,6)}}. {{x===null?'Không có x hữu hạn ứng với điểm đang chọn.':`x = ${fmt(x,4)}.`}} Mục tiêu LP = {{fmt(f(z),6)}}.</p>
   <p v-if="kind==='unattained'">LP cực tiểu 1 + z trên 0 ≤ z ≤ 1, đạt 1 chỉ tại z = 0. Bài toán gốc luôn có f(x) &gt; 1, nên cận dưới đúng là 1 nhưng không có điểm x hữu hạn đạt cận ấy.</p>
   <p v-else>LP có mục tiêu hằng bằng 1. Điểm z = 0 tối ưu, đồng thời mọi điểm 0 &lt; z ≤ 1 cũng tối ưu. Bài toán gốc đạt giá trị 1 ở mọi x ≥ 0. Vì vậy chỉ nhìn thấy một nghiệm tối ưu z = 0 chưa đủ để kết luận không đạt nghiệm trong bài toán gốc.</p>
   <p>Chấm rỗng đánh dấu z = 0, thuộc LP đã đóng miền nhưng không thuộc ảnh của bất kỳ x hữu hạn nào. Đoạn vẽ thể hiện chính xác mục tiêu tuyến tính theo z, không phải đồ thị theo x.</p>
  </div>
 </figure>
</template>
<style scoped>
svg text{font-size:18px}
.objective{stroke:var(--tim);stroke-width:1.8}
.lab-dot-good{fill:var(--xanh)}
.limit{fill:var(--paper);stroke:var(--do);stroke-width:1.8}
svg :is(line,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
