<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {makeView,createDragger,fmt} from '../controllers/svg-drag.js'
const svg=ref(null),theta=ref(.5),massA=ref(.4),massB=ref(.5)
const view=ref(makeView({x0:0,x1:1,y0:0,y1:1,width:400,height:280,pad:40}))
const denominator=computed(()=>theta.value*massA.value+(1-theta.value)*massB.value)
const mu=computed(()=>denominator.value>0?theta.value*massA.value/denominator.value:null)
const conditional=computed(()=>mu.value===null?null:mu.value*.25+(1-mu.value)*.8)
const naive=computed(()=>theta.value*.25+(1-theta.value)*.8)
const handle=computed(()=>[40+320*theta.value,240])
const drag=createDragger(svg,view,(_,p)=>{theta.value=p[0]},{step:.025})
const rows=computed(()=>[{name:'A',q:.25,y:54},{name:'B',q:.8,y:110},{name:'Trộn',q:conditional.value,y:166}])
function preset(kind){theta.value=.5;massA.value=kind==='empty'?0:.4;massB.value=kind==='empty'?0:kind==='equal'?.4:.5}
</script>
<template>
 <figure class="study-lab" aria-label="Trộn phân phối rồi điều kiện hóa theo cùng một biến cố">
  <figcaption class="lab-title">Cùng một biến cố, trọng số thay đổi sau điều kiện hóa</figcaption>
  <p class="lab-lead">Giữ cố định v = 1. Trong mỗi thanh, tím là xác suất u = 1 và xanh là u = 2 sau khi điều kiện hóa. Kéo nút θ để đổi tỷ lệ trộn hai phân phối đồng thời.</p>
  <div class="lab-buttons" role="group" aria-label="Ví dụ chuẩn hóa"><button type="button" @click="preset('original')">Ví dụ 5/9</button><button type="button" @click="preset('equal')">Hai khối lượng bằng nhau</button><button type="button" @click="preset('empty')">Biến cố có xác suất 0</button></div>
  <svg ref="svg" viewBox="0 0 400 280" role="group" aria-label="Ba thanh xác suất điều kiện và nút kéo tỷ lệ trộn" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <g v-for="row in rows" :key="row.name"><text x="14" :y="row.y+8">{{row.name}}</text><rect x="80" :y="row.y-14" width="300" height="28" class="empty"/><template v-if="row.q!==null"><rect x="80" :y="row.y-14" :width="300*row.q" height="28" class="first"/><rect :x="80+300*row.q" :y="row.y-14" :width="300*(1-row.q)" height="28" class="second"/></template><text v-else x="90" :y="row.y+7">Không xác định</text></g>
   <text x="20" y="211">θ = {{fmt(theta)}}</text><text x="380" y="211" text-anchor="end">Tỷ lệ của A</text>
   <line x1="40" x2="360" y1="240" y2="240" class="lab-line"/>
   <circle :cx="handle[0]" :cy="handle[1]" r="8" class="lab-dot-accent"/>
   <circle :cx="handle[0]" :cy="handle[1]" r="30" class="lab-handle hit" tabindex="0" role="slider" aria-label="Tỷ lệ θ của phân phối A" aria-valuemin="0" aria-valuemax="1" :aria-valuenow="theta" :aria-valuetext="fmt(theta,4)" @pointerdown="drag.start('theta',$event)" @keydown="drag.key('theta',[theta,.5],$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-controls"><label>Xác suất v = 1 trong A: {{fmt(massA)}}<input v-model.number="massA" type="range" min="0" max="1" step=".05"/></label><label>Xác suất v = 1 trong B: {{fmt(massB)}}<input v-model.number="massB" type="range" min="0" max="1" step=".05"/></label></div>
  <div class="lab-readout" role="status"><p>Xác suất của biến cố sau khi trộn là θ·{{fmt(massA)}} + (1 − θ)·{{fmt(massB)}} = {{fmt(denominator,4)}}.</p><template v-if="mu!==null"><p>Trọng số mới μ = {{fmt(mu,4)}}. Xác suất u = 1 sau điều kiện hóa bằng {{fmt(conditional,4)}}, còn trộn trực tiếp hai xác suất điều kiện với θ cho {{fmt(naive,4)}}.</p><p>Với θ ở giữa 0 và 1, μ = θ khi hai xác suất của biến cố bằng nhau. Nếu một bên có khối lượng bằng 0, bên đó không đóng góp sau điều kiện hóa.</p></template><p v-else class="is-bad">Biến cố v = 1 có xác suất 0 trong phân phối trộn. Không được chia cho 0 để tạo một phân phối có điều kiện.</p><p>Hai thanh A và B mô tả các tỷ lệ cố định bên trong biến cố khi nó có xác suất dương. Khi khối lượng bằng 0, các tỷ lệ đó chỉ là quy ước để dựng ví dụ, không phải xác suất có điều kiện xác định.</p></div>
 </figure>
</template>
<style scoped>
svg text{font-size:20px;pointer-events:none}.first{fill:var(--tim)}.second{fill:var(--xanh)}.empty{fill:var(--canvas);stroke:var(--ink-3);stroke-width:1}.hit{fill:transparent!important;stroke:transparent}.hit:focus-visible{stroke:var(--vang)}svg :is(line,rect,circle:not(.hit)){pointer-events:none}
</style>
