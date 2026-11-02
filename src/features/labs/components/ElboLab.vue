<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {makeView,createDragger,fmt} from '../controllers/svg-drag.js'
const svg=ref(null),q=ref(.5)
const view=ref(makeView({x0:0,x1:1,y0:-2.4,y1:-.6,width:400,height:300,pad:32}))
const evidence=Math.log(.4),term=(a,p)=>a===0?0:a*Math.log(p/a)
const elbo=a=>term(a,.1)+term(1-a,.3)
const kl=computed(()=>evidence-elbo(q.value))
const P=p=>view.value.point(p)
const curve=Array.from({length:201},(_,i)=>{const a=i/200;return P([a,elbo(a)]).join(',')}).join(' ')
const drag=createDragger(svg,view,(_,p)=>{q.value=p[0]},{step:.025})
</script>
<template>
 <figure class="study-lab" aria-label="Cận ELBO và độ phân kỳ tới hậu nghiệm trong mô hình hai trạng thái">
  <figcaption class="lab-title">Cận ELBO chạm log p(x) khi q bằng hậu nghiệm</figcaption>
  <p class="lab-lead">Mô hình có p(x, z = 0) = 0.1 và p(x, z = 1) = 0.3. Kéo điểm tím để đổi q(z = 0). Đoạn vàng đo đúng độ phân kỳ KL từ q tới hậu nghiệm.</p>
  <div class="lab-buttons" role="group" aria-label="Phân phối thử q"><button type="button" @click="q=.5">q = (0.5, 0.5)</button><button type="button" @click="q=.1">q = (0.1, 0.9)</button><button type="button" @click="q=.25">Hậu nghiệm (0.25, 0.75)</button><button type="button" @click="q=0">Một xác suất bằng 0</button></div>
  <svg ref="svg" viewBox="0 0 400 300" role="group" aria-label="Đồ thị ELBO theo q, cận trên log bằng chứng và khoảng cách KL" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line x1="32" x2="368" y1="268" y2="268" class="lab-axis"/><line x1="32" x2="32" y1="32" y2="268" class="lab-axis"/>
   <line x1="32" x2="368" :y1="P([0,evidence])[1]" :y2="P([0,evidence])[1]" class="lab-guide"/><text x="368" :y="P([0,evidence])[1]-12" text-anchor="end">log p(x)</text>
   <polyline :points="curve" class="lab-accent"/>
   <line :x1="P([q,0])[0]" :x2="P([q,0])[0]" :y1="P([q,elbo(q)])[1]" :y2="P([q,evidence])[1]" class="lab-warn"/>
   <circle :cx="P([q,elbo(q)])[0]" :cy="P([q,elbo(q)])[1]" r="8" class="lab-dot-accent"/><circle :cx="P([q,elbo(q)])[0]" :cy="P([q,elbo(q)])[1]" r="28" class="lab-handle hit" tabindex="0" role="slider" aria-label="Xác suất q của trạng thái 0" :aria-valuetext="fmt(q,4)" @pointerdown="drag.start('q',$event)" @keydown="drag.key('q',[q,elbo(q)],$event)"/>
   <text x="32" y="292">0</text><text x="368" y="292" text-anchor="end">q₀ = 1</text>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-readout" role="status"><p>q = ({{fmt(q,3)}}, {{fmt(1-q,3)}}), ELBO = {{fmt(elbo(q),6)}}. log p(x) = {{fmt(evidence,6)}}.</p><p>log p(x) − ELBO = KL(q ∥ p(z | x)) = {{fmt(kl,6)}} ≥ 0. {{kl<1e-10?'Cận đang chạm giá trị thật.':'Cực đại cận dưới tương đương giảm độ phân kỳ tới hậu nghiệm trong ví dụ này.'}}</p><p>Ở đầu mút q₀ = 0 hoặc 1, dùng giới hạn 0 log 0 = 0. Cận ELBO vẫn có nghĩa, nhưng cách viết p(x) thành kỳ vọng của p(x,z)/q(z) cần q dương trên toàn miền hỗ trợ của p(x,z).</p></div>
 </figure>
</template>
<style scoped>
svg text{font-size:20px;pointer-events:none}svg :is(line,polyline),svg circle:not(.hit){pointer-events:none}.hit{fill:transparent!important;stroke:transparent}.hit:focus-visible{stroke:var(--vang)}
</style>
