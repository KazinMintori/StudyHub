<script setup>
import { computed,ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { makeView,createDragger,fmt } from '../controllers/svg-drag.js'
import { ridgeScalar } from '../services/foundation-geometry.mjs'
const svg=ref(null),parameterSvg=ref(null),w=ref(1)
const row=computed(()=>ridgeScalar(w.value)),current=computed(()=>[row.value.f1,row.value.f2])
const view=ref(makeView({x0:-2,x1:22,y0:-.4,y1:4.4,width:400,height:400,pad:30})),P=p=>view.value.point(p)
const drag=createDragger(svg,view,(_,p)=>{w.value=Math.max(0,Math.min(2,1+p[1]/4-p[0]/20))},{step:.1})
const parameterView=ref(makeView({x0:-.2,x1:2.2,y0:-1,y1:1,width:400,height:140,pad:30}))
const parameterDrag=createDragger(parameterSvg,parameterView,(_,p)=>{w.value=Math.max(0,Math.min(2,p[0]))},{step:.025,snap:.005})
const curve=Array.from({length:201},(_,i)=>{const r=ridgeScalar(i/100);return[r.f1,r.f2]})
const support=computed(()=>{
 if(w.value===0)return[[0,0],[20,0]]
 if(w.value===2)return[[0,0],[0,4]]
 const gamma=row.value.gamma,c=row.value.f1+gamma*row.value.f2
 const points=[[0,c/gamma],[20,(c-20)/gamma],[c,0],[c-4*gamma,4]].filter(p=>p[0]>=0&&p[0]<=20&&p[1]>=0&&p[1]<=4)
 return points.length>=2?[points[0],points.at(-1)]:null
})
</script>

<template>
 <figure class="study-lab" aria-label="Đường biên Pareto của hồi quy ridge một tham số">
  <figcaption class="lab-title">Một nghiệm w, hai mục tiêu và một trọng số tương ứng</figcaption>
  <p class="lab-lead">F₁(w) = 5(w − 2)² đo sai số, F₂(w) = w² đo độ lớn tham số. Kéo điểm trên đường Pareto hoặc kéo w trên đoạn bên dưới. Hai cách điều chỉnh cùng một nghiệm.</p>
  <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Không gian hai mục tiêu, đường Pareto và điểm mục tiêu kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P([21,0])[0]" :y2="P([21,0])[1]" class="lab-axis"/><line :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P([0,4.2])[0]" :y2="P([0,4.2])[1]" class="lab-axis"/>
   <polyline :points="curve.map(p=>P(p).join(',')).join(' ')" class="lab-accent"/>
   <line v-if="support" :x1="P(support[0])[0]" :y1="P(support[0])[1]" :x2="P(support[1])[0]" :y2="P(support[1])[1]" class="lab-guide"/>
   <circle :cx="P(current)[0]" :cy="P(current)[1]" r="8" class="lab-dot-warn"/>
   <circle :cx="P(current)[0]" :cy="P(current)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Điểm mục tiêu trên biên Pareto" :aria-valuetext="`w = ${fmt(w,3)}, F₁ = ${fmt(row.f1,3)}, F₂ = ${fmt(row.f2,3)}`" @pointerdown="drag.start('front',$event)" @keydown="drag.key('front',current,$event)"/>
   <text x="12" y="23">Không gian mục tiêu R²</text><text x="346" :y="P([0,0])[1]-12">F₁</text><text :x="P([0,0])[0]+12" y="48">F₂</text>
   <text :x="P([20,0])[0]-9" :y="P([20,0])[1]+24">20</text><text :x="P([0,4])[0]-24" :y="P([0,4])[1]+6">4</text><text :x="P([0,0])[0]-15" :y="P([0,0])[1]+24">0</text>
  </svg>
  <svg ref="parameterSvg" viewBox="0 0 400 140" role="group" aria-label="Tham số w kéo được trên đoạn từ 0 đến 2" @pointermove="parameterDrag.move" @pointerup="parameterDrag.end" @pointercancel="parameterDrag.end" @lostpointercapture="parameterDrag.end">
   <text x="12" y="23">Không gian tham số R</text>
   <line :x1="parameterView.sx(0)" y1="70" :x2="parameterView.sx(2)" y2="70" class="lab-good"/>
   <text v-for="value in [0,1,2]" :key="value" :x="parameterView.sx(value)-5" y="112">{{value}}</text>
   <circle :cx="parameterView.sx(w)" cy="70" r="7" class="lab-dot-warn"/>
   <circle :cx="parameterView.sx(w)" cy="70" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Tham số hồi quy w" :aria-valuetext="'w = '+fmt(w,3)" @pointerdown="parameterDrag.start('w',$event)" @keydown="parameterDrag.key('w',[w,0],$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/><LabPointControls :svg="parameterSvg" axes="x"/></details>
  <div class="lab-buttons"><button type="button" @click="w=2">γ = 0</button><button type="button" @click="w=1">γ = 5</button><button type="button" @click="w=0">Đầu mút w = 0</button></div>
  <div class="lab-readout" role="status">
   <p>w = {{fmt(w,4)}}, F₁ = {{fmt(row.f1,4)}}, F₂ = {{fmt(row.f2,4)}}.</p>
   <p v-if="w>0">Tổng F₁ + γF₂ chọn đúng điểm này khi γ = 5(2 − w)/w = {{fmt(row.gamma,4)}}. {{w===2?'Đây là đầu mút γ = 0, chỉ cực tiểu sai số.':'Đường tựa qua điểm đang chọn có hệ số góc −1/γ.'}}</p>
   <p v-else>w = 0 đạt riêng F₂ nhỏ nhất. Không có γ hữu hạn nào trong tổng F₁ + γF₂ cho đúng w = 0. Nó chỉ là giới hạn khi γ tiến tới +∞, hoặc nghiệm của trọng số (0, 1).</p>
   <p>Toàn bộ đoạn 0 ≤ w ≤ 2 là Pareto. Đi sang phải làm sai số giảm nhưng chuẩn tăng. Không một w nào làm đồng thời F₁ = 0 và F₂ = 0. Đường đánh đổi này nằm trong không gian mục tiêu, còn w nằm trên trục tham số.</p>
   <p>Trong hình đầu, điểm bị giữ trên biên Pareto khi kéo. Mô phỏng không coi mọi vị trí con trỏ trong mặt phẳng là một cặp mục tiêu đạt được.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Kéo w từ 2 xuống 0. Từng mục tiêu đổi theo chiều nào?</li><li>Ở w = 1, vì sao hai trọng số là (1, 5) thay vì (1, 1)?</li><li>Với 0 &lt; γ &lt; +∞, hai đầu mút có đạt được hay chỉ được tiến tới?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
figure>svg+svg{margin-top:var(--space-3)}
</style>
