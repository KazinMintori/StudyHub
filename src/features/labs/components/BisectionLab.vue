<script setup>
import {computed,ref,watch} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3,unprojectPlane} from '../services/foundation-geometry.mjs'
import {clipPolygon} from '../services/convex-geometry.mjs'
import {clipPolyline,clipSegment} from '../services/svg-clipping.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'
import {apolloniusBoxLevel,distanceRatio} from '../services/apollonius-feasibility.mjs'

const props=defineProps({initialDimension:{type:Number,default:2,validator:value=>[2,3].includes(value)}})
const svg=ref(null),levelSvg=ref(null),dimension=ref(props.initialDimension),probe=ref([.5,1.8]),depth=ref(0)
const lower=ref(0),upper=ref(1),upperWitness=ref(props.initialDimension===3?[0,1,0]:[0,1]),history=ref([])
const manual=ref(false),manualLevel=ref(.4),paused=ref(false)
const epsilon=.01,exactLevel=Math.sqrt(5)-2
const shownLevel=computed(()=>manual.value?manualLevel.value:history.value.at(-1)?.level??.5)
const query=computed(()=>apolloniusBoxLevel(shownLevel.value,dimension.value))
const point=computed(()=>dimension.value===2?probe.value:[...probe.value,depth.value])
const ratio=computed(()=>distanceRatio(point.value))
const done=computed(()=>upper.value-lower.value<=epsilon)
const flat=makeView({x0:-2.5,x1:4.5,y0:-1,y1:4,width:360,height:272,pad:26})
const camera={yaw:32,pitch:28,scale:40,origin:[180,180]}
const P=p=>dimension.value===2?flat.point(p):project3(p.length===3?p:[...p,0],camera)
const bounds=computed(()=>({x0:20,x1:340,y0:20,y1:dimension.value===3?320:252}))
const view=computed(()=>({
 x0:-1,x1:1.5,y0:1,y1:3,
 toWorld:(x,y)=>dimension.value===2?flat.toWorld(x,y):unprojectPlane([x,y],depth.value,camera)
}))
const drag=createDragger(svg,view,(_,p)=>{probe.value=p},{step:.05})
const rail=makeView({x0:-.03,x1:1.03,y0:0,y1:1,width:360,height:110,pad:26})
const levelView=computed(()=>rail)
const levelDrag=createDragger(levelSvg,levelView,(_,p)=>{manual.value=true;manualLevel.value=Math.max(0,Math.min(1,p[0]))},{step:.01})
const box2=[[-1,1],[1.5,1],[1.5,3],[-1,3]]
const serialize=p=>p.map(v=>v.join(',')).join(' ')
function cutPolygon(poly,limits){
 for(const [normal,b]of limits){poly=clipPolygon(poly,normal,b);if(!poly.length)break}
 return poly
}
const viewportLimits=[[[1,0],4.5],[[-1,0],2.5],[[0,1],4],[[0,-1],1]]
const circlePoints=computed(()=>{
 if(query.value.kind!=='ball')return []
 const [x,y]=query.value.center,r=query.value.radius
 return Array.from({length:721},(_,i)=>{const a=i*Math.PI/360;return [x+r*Math.cos(a),y+r*Math.sin(a)]})
})
const circleRegion=computed(()=>query.value.kind==='halfspace'
 ?cutPolygon([[-2.5,-1],[4.5,-1],[4.5,4],[-2.5,4]],[[[1,0],2]])
 :cutPolygon(circlePoints.value,viewportLimits))
const intersection=computed(()=>query.value.kind==='halfspace'?box2:cutPolygon(circlePoints.value,[[[1,0],1.5],[[-1,0],1],[[0,1],3],[[0,-1],-1]]))
const circleLines=computed(()=>clipPolyline(circlePoints.value.map(flat.point),{x0:26,x1:334,y0:26,y1:246}).map(serialize))
const cubeCorners=Array.from({length:8},(_,i)=>[i&1?1.5:-1,i&2?3:1,i&4?1:-1])
const cubeEdges=Array.from({length:8},(_,i)=>[1,2,4].filter(bit=>(i&bit)===0).map(bit=>[cubeCorners[i],cubeCorners[i|bit]])).flat()
const mesh=computed(()=>{
 if(query.value.kind!=='ball')return []
 const c=query.value.center,r=query.value.radius,lines=[]
 for(const z of [-.7,0,.7]){
  const ring=Math.sqrt(1-z*z)
  lines.push(Array.from({length:181},(_,i)=>{const a=i*Math.PI/90;return P([c[0]+r*ring*Math.cos(a),r*ring*Math.sin(a),r*z])}))
 }
 for(const a of [0,Math.PI/2])lines.push(Array.from({length:181},(_,i)=>{
  const angle=i*Math.PI/90;return P([c[0]+r*Math.cos(angle)*Math.cos(a),r*Math.cos(angle)*Math.sin(a),r*Math.sin(angle)])
 }))
 return lines.flatMap(line=>clipPolyline(line,bounds.value).map(serialize))
})
const connector=computed(()=>query.value.center?clipSegment([P(query.value.center),P(query.value.candidate)],bounds.value):null)
const inset=p=>project3(p,{...camera,origin:[300,60],scale:17})
const limitPlane=()=>[[2,-.5,-1.2],[2,3.5,-1.2],[2,3.5,1.2],[2,-.5,1.2]].map(P)
const anchorA=computed(()=>dimension.value===2?[0,0]:[0,0,0])
const anchorB=computed(()=>dimension.value===2?[4,0]:[4,0,0])
const labels=computed(()=>placePointLabels([
 {key:'a',text:'A',point:P(anchorA.value)},
 {key:'b',text:'B',point:P(anchorB.value)}
],{width:360,height:dimension.value===3?340:272,reserved:[
 ...[anchorA.value,anchorB.value,point.value,query.value.candidate].map(p=>({x:P(p)[0]-10,y:P(p)[1]-10,width:20,height:20})),
 ...(dimension.value===3?[{x:258,y:14,width:90,height:80}]:[{x:flat.sx(2),y:0,width:70,height:30}])
]}))
const witnessInSlice=computed(()=>dimension.value===2||Math.abs(depth.value)<1e-12)
function reset(){lower.value=0;upper.value=1;upperWitness.value=dimension.value===2?[0,1]:[0,1,0];history.value=[];manual.value=false;paused.value=false}
function step(){
 if(done.value||paused.value)return
 manual.value=false
 const level=(lower.value+upper.value)/2,result=apolloniusBoxLevel(level,dimension.value)
 if(result.status==='feasible'){upper.value=level;upperWitness.value=[...result.candidate]}
 else if(result.status==='infeasible')lower.value=level
 else paused.value=true
 history.value.push({level,status:result.status,lower:lower.value,upper:upper.value})
}
function run(){let count=0;while(!done.value&&!paused.value&&count++<30)step()}
function tryLevel(value){manual.value=true;manualLevel.value=value}
function takeWitness(){probe.value=query.value.candidate.slice(0,2);if(dimension.value===3)depth.value=query.value.candidate[2]}
watch(dimension,()=>{probe.value=[.5,1.8];depth.value=0;reset()})
</script>

<template>
 <figure class="study-lab" aria-label="Chia đôi bằng chứng chỉ hình học của tập mức tỉ số khoảng cách">
  <figcaption class="lab-title">Mỗi mức được kiểm bằng một điểm, không cần biết trước nghiệm tối ưu</figcaption>
  <p class="lab-lead">Kéo điểm P trong miền X để thử một vị trí. Mức t được kéo trên hình nhỏ phía dưới. Điểm Q gần tâm tập mức nhất trong X là chứng chỉ dùng để kiểm khả thi. Thử mức bằng tay không tự thay đổi khoảng chia đôi.</p>
  <div class="lab-buttons" role="group" aria-label="Không gian của bài toán tỉ số khoảng cách">
   <button type="button" :aria-pressed="dimension===2" @click="dimension=2">Miền X trong R²</button>
   <button type="button" :aria-pressed="dimension===3" @click="dimension=3">Khối X trong R³</button>
  </div>
  <p v-if="dimension===3" class="lab-lead">Khối X thêm tọa độ x₃ thuộc [−1, 1]. Kéo P trên lát x₃ đang chọn. Chứng chỉ Q được tính trên toàn khối, và có x₃ = 0 trong ví dụ này. Lưới mảnh chỉ biểu diễn mặt cầu của tập mức, không phải đồ thị của hàm.</p>
  <svg ref="svg" :viewBox="dimension===3?'0 0 360 340':'0 0 360 272'" role="group" aria-label="Miền X, tập mức, điểm thử P kéo được và điểm chứng Q" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <template v-if="dimension===2">
    <polygon :points="serialize(box2.map(flat.point))" class="domain"/>
    <polygon :points="serialize(circleRegion.map(flat.point))" class="level-region"/>
    <polygon :points="serialize(intersection.map(flat.point))" class="intersection"/>
    <polyline v-for="(points,index) in circleLines" :key="index" :points="points" class="level-boundary"/>
    <line :x1="flat.sx(2)" :x2="flat.sx(2)" y1="20" y2="250" class="lab-guide"/>
    <text :x="flat.sx(2)+8" y="23">x₁ = 2</text>
   </template>
   <template v-else>
    <polygon v-if="query.kind==='halfspace'" :points="serialize(limitPlane())" class="halfspace-plane"/>
    <polyline v-for="(points,index) in mesh" :key="index" :points="points" class="sphere"/>
    <line v-for="(edge,index) in cubeEdges" :key="index" :x1="P(edge[0])[0]" :y1="P(edge[0])[1]" :x2="P(edge[1])[0]" :y2="P(edge[1])[1]" class="box-edge"/>
    <polygon :points="serialize(box2.map(p=>P([...p,depth])))" class="slice"/>
    <rect x="258" y="14" width="90" height="80" class="axis-paper"/>
    <line v-for="(end,index) in [[1,0,0],[0,1,0],[0,0,1]]" :key="index" x1="300" y1="60" :x2="inset(end)[0]" :y2="inset(end)[1]" class="lab-axis"/>
    <text x="320" y="81">x₁</text><text x="269" y="81">x₂</text><text x="307" y="35">x₃</text>
   </template>
   <line v-if="connector" :x1="connector[0][0]" :y1="connector[0][1]" :x2="connector[1][0]" :y2="connector[1][1]" class="lab-guide"/>
   <circle :cx="P(dimension===2?[0,0]:[0,0,0])[0]" :cy="P(dimension===2?[0,0]:[0,0,0])[1]" r="5" class="lab-dot"/>
   <circle :cx="P(dimension===2?[4,0]:[4,0,0])[0]" :cy="P(dimension===2?[4,0]:[4,0,0])[1]" r="5" class="lab-dot-bad"/>
   <text :x="labels.a.x" :y="labels.a.y" :text-anchor="labels.a.anchor">A</text>
   <text :x="labels.b.x" :y="labels.b.y" :text-anchor="labels.b.anchor">B</text>
   <rect :x="P(query.candidate)[0]-9" :y="P(query.candidate)[1]-9" width="18" height="18" class="certificate"/>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="7" class="lab-dot-accent"/>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="27" class="lab-handle hit" role="slider" tabindex="0" aria-label="Vị trí thử P trong miền X" :aria-valuetext="fmtPoint(point,4)" @pointerdown="drag.start('point',$event)" @keydown="drag.key('point',probe,$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Di chuyển P bằng nút</summary><LabPointControls :svg="svg"/></details>
  <div v-if="dimension===3" class="lab-buttons" role="group" aria-label="Lát tọa độ thứ ba để kéo P">
   <button type="button" :aria-pressed="depth===-1" @click="depth=-1">Lát x₃ = −1</button>
   <button type="button" :aria-pressed="depth===0" @click="depth=0">Lát x₃ = 0</button>
   <button type="button" :aria-pressed="depth===1" @click="depth=1">Lát x₃ = 1</button>
  </div>
  <p class="lab-legend"><span class="legend-accent">Miền X và điểm P</span><span class="legend-good">Tập mức và phần giao</span><span class="legend-warn">Q: Điểm chứng hình vuông</span></p>
  <svg ref="levelSvg" viewBox="0 0 360 110" role="group" aria-label="Mức t kéo trực tiếp trên đoạn từ không tới một" @pointermove="levelDrag.move" @pointerup="levelDrag.end" @pointercancel="levelDrag.end" @lostpointercapture="levelDrag.end">
   <line :x1="rail.sx(0)" :x2="rail.sx(1)" :y1="rail.sy(.5)" :y2="rail.sy(.5)" class="lab-axis"/>
   <line :x1="rail.sx(lower)" :x2="rail.sx(upper)" :y1="rail.sy(.5)" :y2="rail.sy(.5)" class="bracket"/>
   <circle :cx="rail.sx(shownLevel)" :cy="rail.sy(.5)" r="7" class="lab-dot-warn"/>
   <circle :cx="rail.sx(shownLevel)" :cy="rail.sy(.5)" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Mức t thử khả thi" :aria-valuemin="0" :aria-valuemax="1" :aria-valuenow="shownLevel" :aria-valuetext="fmt(shownLevel,5)" @pointerdown="levelDrag.start('level',$event)" @keydown="levelDrag.key('level',[shownLevel,.5],$event)"/>
   <text :x="rail.sx(0)" y="95" text-anchor="middle">0</text><text :x="rail.sx(1)" y="95" text-anchor="middle">1</text><text x="15" y="19">Mức t</text>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh t bằng nút</summary><LabPointControls :svg="levelSvg" axes="x"/></details>
  <div class="lab-buttons" role="group" aria-label="Thử mức và thực hiện chia đôi">
   <button type="button" :disabled="done||paused" @click="step">Chia đôi một bước</button>
   <button type="button" :disabled="done||paused" @click="run">Chia đôi tới độ rộng 0.01</button>
   <button type="button" @click="reset">Bắt đầu lại</button>
   <button type="button" @click="tryLevel(.125)">Thử t = 0.125</button>
   <button type="button" @click="tryLevel(.25)">Thử t = 0.25</button>
   <button type="button" @click="tryLevel(exactLevel)">Thử mức tiếp xúc</button>
   <button type="button" @click="tryLevel(1)">Thử t = 1</button>
   <button type="button" :disabled="query.status!=='feasible'" @click="takeWitness">Đưa P tới điểm chứng Q</button>
  </div>
  <div class="lab-readout" role="status">
   <p>P = {{fmtPoint(point,4)}}, tỉ số khoảng cách tại P là {{fmt(ratio,6)}}. {{ratio<=shownLevel?'P đạt mức đang chọn.':'P chưa đạt mức đang chọn.'}}</p>
   <p v-if="query.kind==='ball'">Tập mức t = {{fmt(shownLevel,6)}} là {{dimension===2?'đĩa tròn':'quả cầu'}}, tâm {{fmtPoint(query.center,4)}}, bán kính {{fmt(query.radius,4)}}.</p>
   <p v-else>Tại t = 1, tập mức là nửa không gian x₁ ≤ 2. Không dùng công thức tâm và bán kính có mẫu 1 − t² ở mức này.</p>
   <p>Q = {{fmtPoint(query.candidate,4)}}. Giá trị nhỏ nhất của φₜ trên X là {{fmt(query.residual,8)}}.</p>
   <p :class="query.status==='feasible'?'is-good':query.status==='infeasible'?'is-bad':''">{{query.status==='feasible'?'φₜ(Q) < 0: Có điểm chứng khả thi.':query.status==='infeasible'?'φₜ(Q) > 0: Ngay cả điểm tốt nhất trong X cũng không đạt mức.':'φₜ(Q) gần 0: Cần xét dung sai, không tự chọn nhánh chia đôi.'}}</p>
   <p>Phép thử phân loại theo dung sai {{query.tolerance.toExponential(1)}}. Các điểm ngoài khung của tập mức được cắt khỏi hình vẽ, nhưng phép tính dùng đủ tọa độ và bán kính.</p>
   <p>Khoảng kẹp [l, u] = [{{fmt(lower,6)}}, {{fmt(upper,6)}}], độ rộng {{fmt(upper-lower,6)}}, sau {{history.length}} bước.</p>
   <p>Cận trên đi kèm điểm {{fmtPoint(upperWitness,4)}} có tỉ số {{fmt(distanceRatio(upperWitness),6)}} ≤ u.</p>
   <p v-if="done" class="is-good">Đã đạt độ rộng không quá 0.01. Chia đôi dùng phép thử hình học, không dùng nghiệm √5 − 2 để chọn nhánh.</p>
   <p v-if="paused">Khoảng kẹp chưa được cập nhật vì phép thử ở gần biên dung sai.</p>
   <p v-if="dimension===3&&!witnessInSlice">P đang ở lát x₃ khác 0, còn Q xét trên toàn khối. Bấm đưa P tới Q để chuyển về lát chứa điểm chứng.</p>
  </div>
  <ol v-if="history.length" class="iterations"><li v-for="(row,index) in history" :key="index">Bước {{index+1}}: t = {{fmt(row.level,6)}}, {{row.status==='feasible'?'khả thi':row.status==='infeasible'?'không khả thi':'chưa phân loại chắc chắn'}}. Khoảng [{{fmt(row.lower,6)}}, {{fmt(row.upper,6)}}].</li></ol>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Thử mức 0.125, rồi mức 0.25. Dấu của giá trị nhỏ nhất φₜ khác nhau thế nào?</li><li>Thực hiện chia đôi tới độ rộng 0.01. Điểm giữ cho cận trên có thật sự đạt mức u không?</li><li>Chuyển sang R³ và đổi lát x₃. Vì sao điểm chứng của toàn khối có thể khác điểm đang chọn trong lát?</li><li>Thử t = 1. Vì sao tập mức trở thành nửa không gian?</li></ol></details>
 </figure>
</template>

<style scoped>
svg text{font-size:17px}
.domain{fill:var(--tim-soft);stroke:var(--tim);stroke-width:1.8}
.level-region{fill:var(--xanh-soft);stroke:none;opacity:.45}
.intersection{fill:var(--xanh-soft);stroke:var(--xanh);stroke-width:1.3}
.level-boundary{fill:none;stroke:var(--xanh);stroke-width:1.6}
.box-edge{stroke:var(--tim);stroke-width:1.4}
.slice{fill:var(--tim-soft);stroke:var(--tim);stroke-width:1;fill-opacity:.25}
.sphere{fill:none;stroke:var(--xanh);stroke-width:1;opacity:.7}
.certificate{fill:none;stroke:var(--vang);stroke-width:1.8}
.halfspace-plane{fill:var(--xanh-soft);fill-opacity:.4;stroke:var(--xanh);stroke-width:1.3}
.bracket{stroke:var(--tim);stroke-width:1.8}
.axis-paper{fill:var(--paper);stroke:none}
svg :is(line,polyline,polygon,rect,path,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
.iterations{font-size:var(--fs-ui)}
</style>
