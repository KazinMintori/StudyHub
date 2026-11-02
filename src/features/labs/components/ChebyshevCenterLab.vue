<script setup>
import {computed,ref,watch} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {dot,polyhedronInBox,closestOnSegment,convexHull,insideConvexPolygon,clipPolygon} from '../services/convex-geometry.mjs'
import {clipSegment,clipPolyline} from '../services/svg-clipping.mjs'
import {chebyshevShapes,chebyshevModel,polygonCentroid} from '../services/lp-models-geometry.mjs'

const svg=ref(null),constraints=ref(chebyshevShapes.pentagon.map(row=>({a:[...row.a],b:row.b})))
const selected=ref(0),centerMode=ref(false),showCentroid=ref(false),chosen=ref([2,2])
const model=computed(()=>chebyshevModel(constraints.value))
const centroid=computed(()=>polygonCentroid(constraints.value))
watch(model,next=>{chosen.value=next?.center||[2,2];if(!next||next.centers.length<2)centerMode.value=false},{immediate:true})
const view=makeView({x0:-1,x1:5,y0:-1,y1:5,width:360,height:360,pad:34})
const world=computed(()=>view),frame={x0:34,x1:326,y0:34,y1:326}
const P=p=>view.point(p),poly=points=>points.map(p=>P(p).join(',')).join(' ')
const polygon=computed(()=>polyhedronInBox(constraints.value,[-1,5,-1,5]))
const normalLength=row=>Math.hypot(...row.a)
const row=computed(()=>constraints.value[selected.value])
const edgePoint=computed(()=>{
 const reference=[2,2],denom=dot(row.value.a,row.value.a),distance=(row.value.b-dot(row.value.a,reference))/denom
 return reference.map((v,i)=>v+distance*row.value.a[i])
})
const handle=computed(()=>centerMode.value?chosen.value:edgePoint.value)
function move(_,point){
 if(centerMode.value){
  const hull=convexHull(model.value.centers)
  if(hull.length>2&&insideConvexPolygon(point,hull)){chosen.value=point;return}
  const candidates=hull.map((a,i)=>closestOnSegment(point,a,hull[(i+1)%hull.length]))
  candidates.sort((a,b)=>a.distance-b.distance);chosen.value=candidates[0].point
 }else{
  const unit=row.value.a.map(value=>value/normalLength(row.value)),reference=[2,2]
  let lower=-Infinity,upper=Infinity
  for(let i=0;i<2;i++)if(Math.abs(unit[i])>1e-12){
   const ends=[(-.8-reference[i])/unit[i],(4.8-reference[i])/unit[i]].sort((a,b)=>a-b)
   lower=Math.max(lower,ends[0]);upper=Math.min(upper,ends[1])
  }
  const distance=Math.max(lower,Math.min(upper,(dot(row.value.a,point)-dot(row.value.a,reference))/normalLength(row.value)))
  constraints.value=constraints.value.map((item,index)=>index===selected.value?{a:item.a,b:dot(row.value.a,reference)+distance*normalLength(row.value)}:item)
 }
}
const drag=createDragger(svg,world,move,{step:.05})
const lines=computed(()=>constraints.value.map(item=>{
 const square=dot(item.a,item.a),base=item.a.map(value=>value*item.b/square),direction=[-item.a[1],item.a[0]],extent=30/normalLength(item)
 return clipSegment([P(base.map((v,i)=>v-extent*direction[i])),P(base.map((v,i)=>v+extent*direction[i]))],frame)
}))
const circlePoints=computed(()=>model.value?Array.from({length:161},(_,i)=>{
 const angle=i*Math.PI/80;return [chosen.value[0]+model.value.radius*Math.cos(angle),chosen.value[1]+model.value.radius*Math.sin(angle)]
}):[])
const circleLines=computed(()=>clipPolyline(circlePoints.value.map(P),frame).map(points=>points.map(p=>p.join(',')).join(' ')))
const circleRegion=computed(()=>{
 let polygon=circlePoints.value
 for(const item of [{a:[1,0],b:5},{a:[-1,0],b:1},{a:[0,1],b:5},{a:[0,-1],b:1}])polygon=clipPolygon(polygon,item.a,item.b)
 return polygon
})
const slacks=computed(()=>model.value?constraints.value.map(item=>item.b-dot(item.a,chosen.value)-model.value.radius*normalLength(item)):[])
const active=computed(()=>slacks.value.map((v,i)=>Math.abs(v)<1e-7?i:-1).filter(i=>i>=0))
function load(kind){constraints.value=chebyshevShapes[kind].map(item=>({a:[...item.a],b:item.b}));selected.value=0;centerMode.value=false}
const label=item=>fmtPoint(item.a,0)+' · x ≤ '+fmt(item.b,3)
</script>

<template>
 <figure class="study-lab" aria-label="Tâm Chebyshev, hình tròn nội tiếp lớn nhất và trường hợp tâm không duy nhất">
  <figcaption class="lab-title">Dịch từng cạnh và quan sát bán kính lớn nhất</figcaption>
  <p class="lab-lead">Chọn một ràng buộc rồi kéo điểm tím để dịch cạnh song song với chính nó. Miền hình tròn lớn nhất được tính bằng LP theo hai tọa độ tâm và r ≥ 0. Hình dùng cùng thang đo trên hai trục, nên đường tròn không bị kéo thành ellipse.</p>
  <svg ref="svg" viewBox="0 0 360 360" role="group" aria-label="Đa giác, đường tròn lớn nhất và một tay nắm dịch cạnh hoặc chọn tâm" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <polygon v-if="polygon.length>=3" :points="poly(polygon)" class="domain"/>
   <template v-for="(line,index) in lines" :key="index"><line v-if="line" :x1="line[0][0]" :y1="line[0][1]" :x2="line[1][0]" :y2="line[1][1]" :class="active.includes(index)?'active-edge':'other-edge'"/></template>
   <polygon v-if="model" :points="poly(circleRegion)" class="ball-fill"/>
   <polyline v-for="(points,index) in circleLines" :key="index" :points="points" class="ball-edge"/>
   <line v-if="model&&model.centers.length===2" :x1="P(model.centers[0])[0]" :y1="P(model.centers[0])[1]" :x2="P(model.centers[1])[0]" :y2="P(model.centers[1])[1]" class="center-set"/>
   <circle v-if="model" :cx="P(chosen)[0]" :cy="P(chosen)[1]" r="5" class="lab-dot"/>
   <circle v-if="showCentroid&&centroid" :cx="P(centroid)[0]" :cy="P(centroid)[1]" r="6" class="lab-dot-hollow"/>
   <circle :cx="P(handle)[0]" :cy="P(handle)[1]" r="6" class="lab-dot-accent"/>
   <circle :cx="P(handle)[0]" :cy="P(handle)[1]" r="27" class="lab-handle hit" tabindex="0" role="slider" :aria-label="centerMode?'Tâm tối ưu trên tập các tâm':'Vế phải của ràng buộc đã chọn'" :aria-valuetext="centerMode?fmtPoint(chosen,4):fmt(row.b,5)" @pointerdown="drag.start('handle',$event)" @keydown="drag.key('handle',handle,$event)"/>
   <text x="333" :y="view.sy(0)+22">x₁</text><text :x="view.sx(0)+9" y="24">x₂</text>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-controls">
   <label>Ràng buộc cần dịch<select v-model.number="selected" @change="centerMode=false"><option v-for="(item,index) in constraints" :key="index" :value="index">Cạnh {{index+1}}: {{label(item)}}</option></select></label>
   <label class="lab-check"><input v-model="showCentroid" type="checkbox"/> Hiện trọng tâm diện tích</label>
  </div>
  <div class="lab-buttons" role="group" aria-label="Đa giác và cách chọn tâm">
   <button type="button" @click="load('pentagon')">Ngũ giác ban đầu</button>
   <button type="button" @click="load('rectangle')">Hình chữ nhật, nhiều tâm</button>
   <button type="button" @click="load('empty')">Miền rỗng</button>
   <button type="button" :disabled="!model||model.centers.length<2" :aria-pressed="centerMode" @click="centerMode=!centerMode">Kéo để chọn một tâm tối ưu</button>
  </div>
  <p class="lab-legend"><span class="legend-accent">Miền khả thi</span><span class="legend-good">Đường tròn lớn nhất</span><span class="legend-warn">Ràng buộc chặt</span></p>
  <div class="lab-readout" role="status">
   <template v-if="model">
    <p>Tâm đang vẽ = {{fmtPoint(chosen,5)}}. Bán kính tối ưu r = {{fmt(model.radius,6)}}.</p>
    <p>Có {{active.length}} ràng buộc chặt tại tâm này: {{active.map(i=>i+1).join(', ')}}. Các độ dư của LP là {{slacks.map(v=>fmt(v,5)).join(', ')}}.</p>
    <p v-if="model.centers.length>1">Bán kính là duy nhất về giá trị, còn tâm không duy nhất. Đoạn xanh biểu diễn các tâm tối ưu trong ví dụ này. Chọn chế độ kéo tâm để đổi tâm mà giữ nguyên bán kính.</p>
    <p v-if="showCentroid&&centroid">Trọng tâm diện tích = {{fmtPoint(centroid,5)}}. Nó cân bằng diện tích, không tự cực đại khoảng cách nhỏ nhất tới các cạnh.</p>
   </template>
   <p v-else class="is-bad">Miền rỗng trong họ ràng buộc đang xét: Không có hình tròn nào với r ≥ 0 thỏa toàn bộ điều kiện.</p>
   <p v-if="centerMode">Kéo tâm trên tập các tâm tối ưu. Thao tác này không dịch cạnh và không đổi r.</p>
   <p v-else>Tay nắm tím chỉ dịch ràng buộc {{selected+1}} theo pháp tuyến, với vế phải b = {{fmt(row.b,5)}}. Các cạnh khác được giữ nguyên.</p>
   <p>Các họ pháp tuyến trong mô phỏng này luôn bao kín nếu miền khác rỗng. Việc xét các bộ ba ràng buộc độc lập phù hợp với ví dụ nhỏ này, không phải cách giải LP quy mô lớn. Hình được cắt theo khung, không thêm cận cho bài toán.</p>
   <p>Các độ dư hiển thị được làm tròn. Phép kiểm các bất đẳng thức của LP dùng dung sai 10⁻⁸, còn việc đánh dấu tiếp xúc dùng dung sai 10⁻⁷.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Chọn hình chữ nhật rồi kéo tâm. Vì sao hình tròn chỉ chạm hai cạnh ở các tâm bên trong đoạn tối ưu?</li><li>Ở ngũ giác, dịch một cạnh còn dư vào trong. Khi nào bán kính bắt đầu giảm?</li><li>Chọn miền rỗng rồi dịch ràng buộc trái. Tại sao phải giữ r ≥ 0 khi xét khả thi?</li></ol></details>
 </figure>
</template>

<style scoped>
svg text{font-size:18px}
.domain{fill:var(--tim-soft);stroke:var(--tim);stroke-width:1.3}
.active-edge{stroke:var(--vang);stroke-width:1.6}
.other-edge{stroke:var(--ink-3);stroke-width:1;stroke-dasharray:4 5}
.ball-fill{fill:var(--xanh-soft);stroke:none}
.ball-edge{fill:none;stroke:var(--xanh);stroke-width:1.8}
.center-set{stroke:var(--xanh);stroke-width:2.7}
svg :is(line,polyline,polygon,path,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
