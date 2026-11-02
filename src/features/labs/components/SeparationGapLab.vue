<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {makeView,createDragger,fmt} from '../controllers/svg-drag.js'
const svg=ref(null),kind=ref('strict'),probe=ref(1.5)
const view=ref(makeView({x0:-.5,x1:7.5,y0:-2,y1:2,width:400,height:300,pad:20}))
const P=p=>view.value.point(p)
const lower=x=>kind.value==='weak'?0:kind.value==='strict'?-Math.exp(-x):-.5
const upper=x=>kind.value==='weak'?1/x:kind.value==='strict'?Math.exp(-x):.5
const xs=computed(()=>Array.from({length:121},(_,i)=>(kind.value==='weak'?.55:-.5)+(7.5-(kind.value==='weak'?.55:-.5))*i/120))
const curve=fn=>xs.value.map(x=>P([x,fn(x)]).join(',')).join(' ')
const shape=(fn,edge)=>[P([xs.value[0],edge]),...xs.value.map(x=>P([x,fn(x)])),P([7.5,edge])].map(p=>p.join(',')).join(' ')
const distance=computed(()=>upper(probe.value)-lower(probe.value))
const drag=createDragger(svg,view,(_,p)=>{probe.value=Math.min(7,Math.max(.6,p[0]))},{step:.2})
const names={weak:'Chỉ phân tách không ngặt',strict:'Ngặt, khoảng cách bằng 0',strong:'Mạnh, có dải đệm'}
function preset(value){kind.value=value;probe.value=1.5}
</script>
<template>
 <figure class="study-lab" aria-label="Phân biệt phân tách không ngặt, nghiêm ngặt và mạnh">
  <figcaption class="lab-title">Không chạm đường tách vẫn có thể tiến sát nó tùy ý</figcaption>
  <p class="lab-lead">Chọn từng cặp tập. Kéo điểm trên biên D sang phải để xem đoạn nối thẳng đứng co lại hay giữ nguyên. Hai miền tiếp tục vô hạn ngoài khung vẽ.</p>
  <div class="lab-buttons" role="group" aria-label="Ba mức phân tách"><button v-for="(name,value) in names" :key="value" type="button" :aria-pressed="kind===value" @click="preset(value)">{{name}}</button></div>
  <svg ref="svg" viewBox="0 0 400 300" role="group" aria-label="Hai tập lồi và đường tách v bằng 0" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <polygon :points="shape(lower,-2)" class="shade-c"/><polygon :points="shape(upper,2)" class="shade-d"/>
   <polyline :points="curve(lower)" class="lab-accent"/><polyline :points="curve(upper)" class="lab-good"/>
   <line x1="20" x2="380" :y1="P([0,0])[1]" :y2="P([0,0])[1]" class="separator"/>
   <text x="25" y="273">C</text><text x="25" y="45">D</text><text x="370" y="139" text-anchor="end">v = 0</text>
   <line :x1="P([probe,0])[0]" :x2="P([probe,0])[0]" :y1="P([probe,lower(probe)])[1]" :y2="P([probe,upper(probe)])[1]" class="lab-warn"/>
   <circle :cx="P([probe,upper(probe)])[0]" :cy="P([probe,upper(probe)])[1]" r="8" class="lab-dot-warn"/>
   <circle :cx="P([probe,upper(probe)])[0]" :cy="P([probe,upper(probe)])[1]" r="30" class="lab-handle hit" tabindex="0" role="slider" aria-label="Hoành độ u của cặp điểm trên hai biên" :aria-valuetext="`u = ${fmt(probe,4)}`" @pointerdown="drag.start('probe',$event)" @keydown="drag.key('probe',[probe,upper(probe)],$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-readout" role="status"><p v-if="kind==='weak'">C có v ≤ 0, còn D có u &gt; 0 và v ≥ 1/u. Trục v = 0 chạm C nên không phân tách nghiêm ngặt. Khoảng cách giữa hai tập bằng 0.</p><p v-else-if="kind==='strict'">C có v ≤ −e⁻ᵘ và D có v ≥ e⁻ᵘ. Mỗi điểm của C nằm dưới v = 0 và mỗi điểm của D nằm trên nó. Phân tách nghiêm ngặt, nhưng khoảng cách giữa hai tập vẫn bằng 0.</p><p v-else>C có v ≤ −1/2, D có v ≥ 1/2. Khoảng cách giữa hai tập bằng 1. Đường v = 0 có dải đệm rộng 1, tức cách mỗi tập 1/2.</p><p>Tại u = {{fmt(probe)}}, hai điểm cùng hoành độ cách nhau {{fmt(distance,5)}}. Đây là độ dài đoạn đang vẽ, không tự động là khoảng cách nhỏ nhất giữa hai tập.</p><p v-if="kind!=='strong'">Khi u tăng không giới hạn, đoạn nối tiến về 0. Một ảnh trong khung hữu hạn không thể tự chứng minh khoảng cách của cả hai tập vô hạn là dương.</p></div>
 </figure>
</template>
<style scoped>
svg text{font-size:20px;pointer-events:none}.shade-c{fill:var(--tim-soft)}.shade-d{fill:var(--xanh-soft)}.separator{stroke:var(--ink);stroke-width:1.3;stroke-dasharray:5 5}.hit{fill:transparent!important;stroke:transparent}.hit:focus-visible{stroke:var(--vang)}svg :is(line,polygon,polyline,circle:not(.hit)){pointer-events:none}
</style>
