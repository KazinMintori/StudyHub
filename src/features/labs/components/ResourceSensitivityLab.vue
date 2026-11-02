<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {polyhedronInBox} from '../services/convex-geometry.mjs'
import {resourceSensitivity} from '../services/foundation-geometry.mjs'
const svg=ref(null),valueSvg=ref(null),budget=ref(2),anchor=ref(2)
const view=ref(makeView({x0:-.4,x1:4.8,y0:-.4,y1:4.8,width:400,height:400,pad:30})),P=p=>view.value.point(p)
const dragView=computed(()=>({x0:.05,x1:4.5,y0:0,y1:0,toWorld:(x,y)=>[view.value.wx(x)+view.value.wy(y),0]}))
const drag=createDragger(svg,dragView,(_,p)=>{budget.value=p[0]},{step:.05,snap:.01})
const graph=ref(makeView({x0:-.2,x1:4.8,y0:-.35,y1:2.8,width:400,height:400,pad:30})),G=p=>graph.value.point(p)
const graphView=computed(()=>({...graph.value,x0:.05,x1:4.5}))
const graphDrag=createDragger(valueSvg,graphView,(_,p)=>{budget.value=p[0]},{step:.05,snap:.01})
const row=computed(()=>resourceSensitivity(budget.value)),base=computed(()=>resourceSensitivity(anchor.value))
const region=computed(()=>polyhedronInBox([{a:[1,1],b:budget.value}],[0,4.5,0,4.5]))
const endpoints=computed(()=>budget.value<=4.5?[[0,budget.value],[budget.value,0]]:[])
const curve=Array.from({length:180},(_,i)=>{const b=.025+i*.025;return G([b,resourceSensitivity(b).value]).join(',')}).join(' ')
const bound=b=>base.value.value-base.value.lambda*(b-anchor.value)
const support=computed(()=>{
 const lo=.05,hi=4.5,v=graph.value,points=[]
 for(const b of [lo,hi])if(bound(b)>=v.y0&&bound(b)<=v.y1)points.push([b,bound(b)])
 if(base.value.lambda>1e-12)for(const y of [v.y0,v.y1]){
  const b=anchor.value+(base.value.value-y)/base.value.lambda
  if(b>=lo&&b<=hi)points.push([b,y])
 }
 return points.length>=2?[points[0],points.at(-1)]:null
})
</script>

<template>
 <figure class="study-lab" aria-label="KKT có tham số, nghiệm theo ngân sách và cận độ nhạy">
  <figcaption class="lab-title">Nới ngân sách làm chi phí giảm bao nhiêu?</figcaption>
  <p class="lab-lead">Cực tiểu một nửa bình phương khoảng cách tới (2, 1), với x₁, x₂ ≥ 0 và x₁ + x₂ ≤ b. Kéo chấm trên đường ngân sách hoặc kéo điểm trên đồ thị V(b) để đổi cùng tham số b.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Miền khả thi theo ngân sách, điểm đích và nghiệm tối ưu" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <line :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P([4.5,0])[0]" :y2="P([4.5,0])[1]" class="lab-axis"/><line :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P([0,4.5])[0]" :y2="P([0,4.5])[1]" class="lab-axis"/>
    <polygon :points="region.map(p=>P(p).join(',')).join(' ')" class="lab-region"/>
    <line :x1="P(endpoints[0])[0]" :y1="P(endpoints[0])[1]" :x2="P(endpoints[1])[0]" :y2="P(endpoints[1])[1]" class="lab-accent"/>
    <circle :cx="P([2,1])[0]" :cy="P([2,1])[1]" r="7" class="lab-dot-hollow"/><text :x="P([2,1])[0]+12" :y="P([2,1])[1]+25">(2, 1)</text>
    <line :x1="P(row.point)[0]" :y1="P(row.point)[1]" :x2="P([2,1])[0]" :y2="P([2,1])[1]" class="lab-good"/>
    <circle :cx="P(row.point)[0]" :cy="P(row.point)[1]" r="7" class="lab-dot-warn"/><text :x="P(row.point)[0]-18" :y="P(row.point)[1]+28">x*</text>
    <circle :cx="P([budget/2,budget/2])[0]" :cy="P([budget/2,budget/2])[1]" r="7" class="lab-dot-accent"/>
    <circle :cx="P([budget/2,budget/2])[0]" :cy="P([budget/2,budget/2])[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Ngân sách b, di chuyển đường x₁ + x₂ = b" :aria-valuetext="'b = '+fmt(budget,3)" @pointerdown="drag.start('budget',$event)" @keydown="drag.key('budget',[budget,0],$event)"/>
    <text x="12" y="23">Không gian quyết định</text><text x="344" :y="P([0,0])[1]+24">x₁</text><text :x="P([0,0])[0]+12" y="48">x₂</text>
   </svg>
   <svg ref="valueSvg" viewBox="0 0 400 400" role="group" aria-label="Hàm giá trị tối ưu và đường tựa do nhân tử tại ngân sách neo cung cấp" @pointermove="graphDrag.move" @pointerup="graphDrag.end" @pointercancel="graphDrag.end" @lostpointercapture="graphDrag.end">
    <line x1="30" x2="370" :y1="graph.sy(0)" :y2="graph.sy(0)" class="lab-axis"/>
    <line v-if="support" :x1="G(support[0])[0]" :y1="G(support[0])[1]" :x2="G(support[1])[0]" :y2="G(support[1])[1]" class="lab-guide"/>
    <polyline :points="curve" class="lab-accent"/>
    <line v-for="b in [1,3]" :key="b" :x1="graph.sx(b)" :x2="graph.sx(b)" y1="48" :y2="graph.sy(0)" class="lab-guide"/>
    <circle :cx="G([anchor,base.value])[0]" :cy="G([anchor,base.value])[1]" r="7" class="lab-dot-hollow"/>
    <circle :cx="G([budget,row.value])[0]" :cy="G([budget,row.value])[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="G([budget,row.value])[0]" :cy="G([budget,row.value])[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Ngân sách b trên đồ thị giá trị tối ưu" :aria-valuetext="`b = ${fmt(budget,3)}, V = ${fmt(row.value,4)}`" @pointerdown="graphDrag.start('budget',$event)" @keydown="graphDrag.key('budget',[budget,0],$event)"/>
    <text x="12" y="23">Giá trị tối ưu V(b)</text><text v-for="b in [0,1,2,3,4]" :key="'label'+b" :x="graph.sx(b)-5" :y="graph.sy(0)+25">{{b}}</text><text x="355" :y="graph.sy(0)+25">b</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="x"/><LabPointControls :svg="valueSvg" axes="x"/></details>
  <div class="lab-buttons"><button type="button" @click="budget=1">b = 1</button><button type="button" @click="budget=2.2;anchor=2">b = 2.2, neo tại 2</button><button type="button" @click="budget=3">b = 3</button><button type="button" @click="anchor=budget">Đặt đường tựa tại b đang chọn</button></div>
  <div class="lab-readout" role="status">
   <p>b = {{fmt(budget,3)}}. x* = {{fmtPoint(row.point,4)}}, V(b) = {{fmt(row.value,5)}}. Nhân tử ngân sách λ* = {{fmt(row.lambda,4)}}, nhân tử không âm μ* = {{fmtPoint(row.mu,4)}}.</p>
   <p>Độ dư b − x₁* − x₂* = {{fmt(row.slack,4)}}. {{budget<1?'Biến x₂ đang chạm 0.':budget<3?'Cả hai biến dương, ngân sách đang chặt.':budget===3?'Ngân sách chặt, nhưng nhân tử đã bằng 0.':'Ngân sách dư, nghiệm tự do (2, 1) đã khả thi.'}}</p>
   <p>Đường tựa neo tại b₀ = {{fmt(anchor,3)}} cho cận V(b) ≥ {{fmt(base.value,5)}} − {{fmt(base.lambda,4)}}(b − {{fmt(anchor,3)}}). Tại b đang chọn, cận bằng {{fmt(bound(budget),5)}}, còn giá trị thật bằng {{fmt(row.value,5)}}.</p>
   <p>Trong ví dụ này V′(b) = −λ*(b), kể cả tại b = 1 và b = 3 vì hai đạo hàm một phía trùng nhau. Đường tựa là cận đúng trên toàn miền, còn dùng nó thay giá trị thật chỉ là xấp xỉ bậc nhất khi ngân sách thay đổi nhỏ.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Kéo b qua 1. Khi nào biến thứ hai bắt đầu nhận tài nguyên?</li><li>Đặt b = 3. Vì sao ràng buộc chặt mà λ* = 0?</li><li>Neo tại b₀ = 2 rồi thử b = 2.2. Vì sao giá trị thật 0.16 lớn hơn cận 0.15?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
