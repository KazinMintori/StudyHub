<script setup>
import {computed,ref,useId} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {polyhedronInBox,dot} from '../services/convex-geometry.mjs'
import {clipSegment} from '../services/svg-clipping.mjs'
import {lpShapes,lpHalfspaces,planarLp} from '../services/linear-program-geometry.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'

const svg=ref(null),key=ref('bounded'),c=ref([-.7,-.7]),arrowId=useId()
const shape=computed(()=>lpShapes[key.value]),result=computed(()=>planarLp(key.value,c.value))
const view=makeView({x0:-1.5,x1:5.8,y0:-1.2,y1:5.6,width:360,height:330,pad:27})
const controls=makeView({x0:-1.8,x1:1.8,y0:-1.8,y1:1.8,width:360,height:280,pad:38})
const controlView=computed(()=>controls)
const drag=createDragger(svg,controlView,(_,p)=>{c.value=p},{step:.05})
const length=computed(()=>Math.hypot(...c.value))
const zero=computed(()=>c.value.every(v=>Math.abs(v)<=(result.value.tolerance||1e-10)))
const frame={x0:27,x1:333,y0:27,y1:303}
const region=computed(()=>polyhedronInBox(lpHalfspaces(key.value),[-1.5,5.8,-1.2,5.6]))
const poly=points=>points.map(p=>view.point(p).join(',')).join(' ')
const segment=(p,q)=>clipSegment([view.point(p),view.point(q)],frame)
function levelLine(value){
 if(length.value<1e-10)return null
 const square=dot(c.value,c.value),base=c.value.map(v=>value*v/square),direction=[-c.value[1],c.value[0]],extent=30/length.value
 return segment(base.map((v,i)=>v-extent*direction[i]),base.map((v,i)=>v+extent*direction[i]))
}
const levels=computed(()=>{
 if(zero.value)return []
 const values=[[-1.5,-1.2],[5.8,-1.2],[5.8,5.6],[-1.5,5.6]].map(p=>dot(c.value,p)),lo=Math.min(...values),hi=Math.max(...values)
 return Array.from({length:7},(_,i)=>levelLine(lo+(hi-lo)*(i+1)/8)).filter(Boolean)
})
const optimumLine=computed(()=>result.value.status==='optimal'?levelLine(result.value.value):null)
const optimalSegments=computed(()=>{
 const r=result.value,out=[]
 if(r.status!=='optimal'||r.whole)return out
 if(r.lineDirection){const d=r.lineDirection;out.push(segment(r.point.map((v,i)=>v-20*d[i]),r.point.map((v,i)=>v+20*d[i])))}
 if(r.best?.length>1)out.push(segment(shape.value.vertices[r.best[0]],shape.value.vertices[r.best.at(-1)]))
 for(const d of r.flatRays||[])out.push(segment(r.point,r.point.map((v,i)=>v+30*d[i])))
 return out.filter(Boolean)
})
const badRay=computed(()=>result.value.status==='unbounded'?segment(result.value.point,result.value.point.map((v,i)=>v+30*result.value.ray[i])):null)
const center=computed(()=>key.value==='strip'||key.value==='infeasible'?[2,2]:[0,1].map(i=>shape.value.vertices.reduce((s,p)=>s+p[i],0)/shape.value.vertices.length))
const tip=computed(()=>zero.value?center.value:center.value.map((v,i)=>v-1.05*c.value[i]/length.value))
const directionLabel=computed(()=>placePointLabels([{key:'direction',text:'−c',point:view.point(tip.value),width:32}],{
 width:360,height:330,reserved:[
 ...[...shape.value.vertices,...(result.value.point?[result.value.point]:[])].map(p=>({x:view.sx(p[0])-11,y:view.sy(p[1])-11,width:22,height:22})),
 {x:334,y:view.sy(0)-5,width:26,height:32},{x:view.sx(0)+3,y:0,width:36,height:31}
 ]}).direction)
const boundaryLines=computed(()=>key.value==='infeasible'?[segment([0,-1.2],[0,5.6]),segment([1,-1.2],[1,5.6])]:[])
function preset(kind,vector){key.value=kind;c.value=vector}
</script>

<template>
 <figure class="study-lab" aria-label="Hình học LP với hướng mục tiêu kéo trực tiếp và các miền khả thi khác nhau">
  <figcaption class="lab-title">Kéo vector mục tiêu, quan sát giá trị có còn bị chặn dưới không</figcaption>
  <p class="lab-lead">Cực tiểu cᵀx là tịnh tiến đường mức theo hướng −c, vuông góc với đường đó. Kéo đầu vector c trong hình điều khiển. Miền không bị chặn không tự có nghĩa mục tiêu giảm về âm vô hạn.</p>
  <svg viewBox="0 0 360 330" role="img" aria-label="Miền khả thi, đường mức, nghiệm tối ưu hoặc tia làm giảm mục tiêu">
   <defs><marker :id="arrowId" viewBox="0 0 8 8" markerWidth="6" markerHeight="6" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8Z" class="arrow-head"/></marker></defs>
   <polygon v-if="region.length" :points="poly(region)" :class="result.whole?'whole-optimum':'region'"/>
   <line v-for="(line,i) in levels" :key="i" :x1="line[0][0]" :y1="line[0][1]" :x2="line[1][0]" :y2="line[1][1]" class="level"/>
   <line x1="23" :y1="view.sy(0)" x2="337" :y2="view.sy(0)" class="lab-axis"/>
   <line :x1="view.sx(0)" y1="22" :x2="view.sx(0)" y2="308" class="lab-axis"/>
   <line v-if="optimumLine" :x1="optimumLine[0][0]" :y1="optimumLine[0][1]" :x2="optimumLine[1][0]" :y2="optimumLine[1][1]" class="optimum-level"/>
   <line v-for="(line,i) in optimalSegments" :key="i" :x1="line[0][0]" :y1="line[0][1]" :x2="line[1][0]" :y2="line[1][1]" class="optimal-edge"/>
   <line v-if="badRay" :x1="badRay[0][0]" :y1="badRay[0][1]" :x2="badRay[1][0]" :y2="badRay[1][1]" class="bad-ray" :marker-end="'url(#'+arrowId+')'"/>
   <line v-for="(line,i) in boundaryLines" :key="i" :x1="line[0][0]" :y1="line[0][1]" :x2="line[1][0]" :y2="line[1][1]" :class="i?'bad-boundary':'first-boundary'"/>
   <circle v-for="(p,i) in shape.vertices" :key="i" :cx="view.sx(p[0])" :cy="view.sy(p[1])" r="4" class="lab-dot"/>
   <circle v-if="result.status==='optimal'&&!result.whole" :cx="view.sx(result.point[0])" :cy="view.sy(result.point[1])" r="7" class="lab-dot-warn"/>
   <line v-if="!zero" :x1="view.sx(center[0])" :y1="view.sy(center[1])" :x2="view.sx(tip[0])" :y2="view.sy(tip[1])" class="descent" :marker-end="'url(#'+arrowId+')'"/>
   <text v-if="!zero" :x="directionLabel.x" :y="directionLabel.y" :text-anchor="directionLabel.anchor">−c</text>
   <text x="338" :y="view.sy(0)+21">x₁</text><text :x="view.sx(0)+9" y="23">x₂</text>
  </svg>
  <p class="lab-legend"><span class="legend-accent">Miền khả thi và hướng giảm</span><span class="legend-guide">Đường mức</span><span class="legend-good">Cạnh, tia hoặc cả miền tối ưu</span><span class="legend-bad">Hướng làm mục tiêu giảm mãi</span></p>
  <svg ref="svg" viewBox="0 0 360 280" role="group" aria-label="Vector hệ số c kéo trực tiếp trên mặt phẳng c1 và c2" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line x1="30" :y1="controls.sy(0)" x2="330" :y2="controls.sy(0)" class="lab-axis"/>
   <line :x1="controls.sx(0)" y1="28" :x2="controls.sx(0)" y2="250" class="lab-axis"/>
   <line :x1="controls.sx(0)" :y1="controls.sy(0)" :x2="controls.sx(c[0])" :y2="controls.sy(c[1])" class="descent" :marker-end="'url(#'+arrowId+')'"/>
   <circle :cx="controls.sx(c[0])" :cy="controls.sy(c[1])" r="7" class="lab-dot-accent"/>
   <circle :cx="controls.sx(c[0])" :cy="controls.sy(c[1])" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Vector mục tiêu c1 và c2" :aria-valuetext="fmtPoint(c,4)" @pointerdown="drag.start('c',$event)" @keydown="drag.key('c',c,$event)"/>
   <text x="331" :y="controls.sy(0)+22">c₁</text><text :x="controls.sx(0)+10" y="23">c₂</text>
   <text x="18" y="268">Kéo đầu c, gốc là (0, 0)</text>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh vector bằng nút</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-controls"><label>Miền khả thi<select v-model="key"><option v-for="(item,id) in lpShapes" :key="id" :value="id">{{item.label}}</option></select></label></div>
  <div class="lab-buttons" role="group" aria-label="Các trạng thái LP để đối chiếu">
   <button type="button" @click="preset('bounded',[-.7,-.7])">Nghiệm tại một đỉnh</button>
   <button type="button" @click="preset('bounded',[-1.6,-1.7])">Cả cạnh tối ưu</button>
   <button type="button" @click="preset('unbounded',[1,1])">Miền vô hạn, tối ưu hữu hạn</button>
   <button type="button" @click="preset('unbounded',[-1,-1])">Mục tiêu giảm không bị chặn</button>
   <button type="button" @click="preset('unbounded',[1,.3])">Cả tia là nghiệm</button>
   <button type="button" @click="preset('strip',[1,-1])">Có nghiệm nhưng không có đỉnh</button>
   <button type="button" @click="preset('infeasible',[1,1])">Miền khả thi rỗng</button>
   <button type="button" @click="c=[0,0]">Mục tiêu bằng không</button>
  </div>
  <div class="lab-readout" role="status">
   <p>c = {{fmtPoint(c,4)}}. Bài toán cực tiểu cᵀx trên {{shape.label.toLowerCase()}}.</p>
   <template v-if="result.status==='optimal'">
    <p>Giá trị tối ưu = {{fmt(result.value,6)}}. Một nghiệm là {{fmtPoint(result.point,4)}}.</p>
    <p v-if="result.whole" class="is-good">Mục tiêu bằng 0: Mọi điểm khả thi đều tối ưu, không chỉ các đỉnh.</p>
    <p v-else-if="key==='strip'" class="is-good">Dải không có đỉnh, nhưng cả đường thẳng qua nghiệm theo hướng (1, 1) đều tối ưu.</p>
    <p v-else-if="result.flatRays.length" class="is-good">Có tia tối ưu vì cᵀr bằng 0 trên một hướng lùi xa. Giá trị tối ưu vẫn hữu hạn.</p>
    <p v-else-if="result.best.length>1" class="is-good">Có {{result.best.length}} đỉnh cùng tối ưu. Mọi điểm trên cạnh nối chúng cũng tối ưu.</p>
    <p v-else>Nghiệm duy nhất là một đỉnh. Đường mức tối ưu tựa vào miền tại đỉnh ấy.</p>
   </template>
   <p v-else-if="result.status==='unbounded'" class="is-bad">Không bị chặn dưới. Từ {{fmtPoint(result.point)}} đi theo r = {{fmtPoint(result.ray)}} vẫn khả thi, với cᵀr = {{fmt(result.slope,6)}} &lt; 0.</p>
   <p v-else class="is-bad">Bất khả thi: Điều kiện x₁ ≤ 0 và x₁ ≥ 1 mâu thuẫn, không có điểm nào thỏa đồng thời.</p>
   <p v-if="key==='infeasible'">Đường tím là x₁ = 0, phía hợp lệ về bên trái. Đường đỏ là x₁ = 1, phía hợp lệ về bên phải. Không có phần giao để tô.</p>
   <p>Hình chỉ vẽ phần miền nằm trong khung. Cắt hình không thêm ràng buộc cho bài toán. Các mũi tên hướng đã chuẩn hóa độ dài để dễ nhìn.</p>
   <p v-if="result.tolerance">So sánh bằng số dùng dung sai {{result.tolerance.toExponential(1)}}. Các giá trị gần bằng nhau có thể được phân loại cùng một mặt tối ưu trong phạm vi này.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Chọn cả cạnh tối ưu rồi kéo c một chút. Vì sao nghiệm có thể chuyển ngay về một đầu cạnh?</li><li>Đổi giữa hai cấu hình của miền vô hạn. Đại lượng cᵀr quyết định điều gì?</li><li>Chọn dải không có đỉnh, rồi đặt mục tiêu bằng 0. Tập nghiệm mở rộng thế nào?</li><li>Thử c = 0 trên miền rỗng. Mục tiêu đơn giản có làm bài toán khả thi không?</li></ol></details>
 </figure>
</template>

<style scoped>
svg text{font-size:18px}
.region{fill:var(--tim-soft);stroke:var(--tim);stroke-width:1.5}
.whole-optimum{fill:var(--xanh-soft);stroke:var(--xanh);stroke-width:1.5}
.level{stroke:var(--ink-3);stroke-width:.85;stroke-dasharray:4 5;opacity:.65}
.optimum-level{stroke:var(--vang);stroke-width:1.6}
.optimal-edge{stroke:var(--xanh);stroke-width:2.8}
.bad-ray{stroke:var(--do);stroke-width:2}
.descent{stroke:var(--tim);stroke-width:2}
.arrow-head{fill:var(--ink);stroke:none}
.first-boundary{stroke:var(--tim);stroke-width:2}.bad-boundary{stroke:var(--do);stroke-width:2}
svg :is(line,path,polygon,polyline,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
