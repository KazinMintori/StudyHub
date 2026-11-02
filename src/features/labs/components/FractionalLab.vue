<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {fractionalVertices as vertices,fractionalValue as value,fractionalSection,projectToPolygon} from '../services/fractional-geometry.mjs'
import {clipSegment} from '../services/svg-clipping.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'

const svg=ref(null),point=ref([2,2]),mode=ref('max'),level=ref(2)
const view=makeView({x0:-1.5,x1:7,y0:-1.5,y1:5.4,width:360,height:290,pad:25})
const P=view.point,pivot=[-2/3,-2/3],values=vertices.map(value)
const best=computed(()=>mode.value==='max'?2.75:8/7)
const section=computed(()=>fractionalSection(level.value,mode.value))
const ray=computed(()=>{
 let d=[-(2-level.value/2),1-level.value]
 if(d[0]+d[1]/2<0)d=d.map(v=>-v)
 return clipSegment([pivot,pivot.map((v,i)=>v+30*d[i])],{x0:-1.1,x1:6.7,y0:-1.1,y1:5.05})
})
const denominator=clipSegment([[-1.5,1],[0,-2]],{x0:-1.1,x1:6.7,y0:-1.1,y1:5.05})
const rail=makeView({x0:.6,x1:3.6,y0:0,y1:1,width:360,height:1,pad:30})
const selected=ref('point')
const dragView=computed(()=>selected.value==='point'?view:{x0:.6,x1:3.6,y0:0,y1:1,toWorld:x=>[rail.wx(x),.5]})
function move(name,p){if(name==='point'){point.value=projectToPolygon(p);level.value=value(point.value)}else level.value=p[0]}
const drag=createDragger(svg,dragView,move,{step:.05})
function start(name,event){selected.value=name;drag.start(name,event)}
function key(name,p,event){selected.value=name;drag.key(name,p,event)}
function choose(which){mode.value=which;point.value=which==='max'?[1,4]:[6,0];level.value=value(point.value)}
const labels=computed(()=>placePointLabels([
 {key:'p',text:'P',point:P(pivot)},{key:'q',text:'Q',point:P(point.value)},
 ...vertices.map((v,i)=>({key:String(i),text:String(i+1),point:P(v)}))
],{width:360,height:290,reserved:[...vertices.map(P),P(pivot),P(point.value)].map(([x,y])=>({x:x-8,y:y-8,width:16,height:16}))}))
</script>

<template>
 <figure class="study-lab" aria-label="Tập mức phân tuyến tính và miền đạt ngưỡng">
  <figcaption class="lab-title">Kéo điểm để xoay đường mức, kéo ngưỡng để thử tính khả thi</figcaption>
  <p class="lab-lead">Kéo Q trong tứ giác để đặt t = f(Q). Kéo chấm trên thước ngay dưới hình để chọn ngưỡng t độc lập, kể cả ngưỡng không đạt được. Tia màu vàng không chứa điểm P vì mẫu số tại P bằng 0.</p>
  <svg ref="svg" viewBox="0 0 360 360" role="group" aria-label="Tứ giác khả thi, tia mức và thước ngưỡng t" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line x1="25" :y1="view.sy(0)" x2="334" :y2="view.sy(0)" class="lab-axis"/>
   <line :x1="view.sx(0)" y1="20" :x2="view.sx(0)" y2="268" class="lab-axis"/>
   <text x="329" :y="view.sy(0)+24">x₁</text><text :x="view.sx(0)+9" y="22">x₂</text>
   <line v-if="denominator" :x1="P(denominator[0])[0]" :y1="P(denominator[0])[1]" :x2="P(denominator[1])[0]" :y2="P(denominator[1])[1]" class="denominator"/>
   <polygon :points="vertices.map(p=>P(p).join(',')).join(' ')" class="lab-region"/>
   <polygon v-if="section.length>=3" :points="section.map(p=>P(p).join(',')).join(' ')" class="accepted"/>
   <line v-if="section.length===2" :x1="P(section[0])[0]" :y1="P(section[0])[1]" :x2="P(section[1])[0]" :y2="P(section[1])[1]" class="boundary"/>
   <circle v-if="section.length===1" :cx="P(section[0])[0]" :cy="P(section[0])[1]" r="8" class="lab-dot-good"/>
   <line v-if="ray" :x1="P(ray[0])[0]" :y1="P(ray[0])[1]" :x2="P(ray[1])[0]" :y2="P(ray[1])[1]" class="level"/>
   <circle :cx="P(pivot)[0]" :cy="P(pivot)[1]" r="5" class="lab-dot-hollow"/>
   <circle v-for="(v,i) in vertices" :key="i" :cx="P(v)[0]" :cy="P(v)[1]" r="4" class="lab-dot"/>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="6" class="lab-dot-accent"/>
   <text v-for="(label,id) in labels" :key="id" :x="label.x" :y="label.y" :text-anchor="label.anchor">{{id==='p'?'P':id==='q'?'Q':Number(id)+1}}</text>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="27" class="lab-handle hit" role="slider" tabindex="0" aria-label="Điểm Q trong tứ giác" :aria-valuetext="fmtPoint(point,4)" @pointerdown="start('point',$event)" @keydown="key('point',point,$event)"/>
   <line x1="30" y1="323" x2="330" y2="323" class="lab-axis"/>
   <text x="30" y="353">0.6</text><text x="330" y="353" text-anchor="end">3.6</text><text x="180" y="300" text-anchor="middle">Ngưỡng t</text>
   <circle :cx="rail.sx(level)" cy="323" r="6" class="lab-dot-warn"/>
   <circle :cx="rail.sx(level)" cy="323" r="27" class="lab-handle hit" role="slider" tabindex="0" aria-label="Ngưỡng t trên thước" :aria-valuetext="fmt(level,5)" @pointerdown="start('level',$event)" @keydown="key('level',[level,.5],$event)"/>
  </svg>
  <p class="lab-legend"><span class="legend-accent">Miền khả thi</span><span class="legend-good">Phần đạt ngưỡng</span><span class="legend-warn">Tia f = t</span><span class="legend-bad">Mẫu số bằng 0</span></p>
  <div class="lab-controls"><label>Bài toán<select v-model="mode"><option value="max">Cực đại f, thử f ≥ t</option><option value="min">Cực tiểu f, thử f ≤ t</option></select></label><label>Ngưỡng t = {{fmt(level,4)}}<input v-model.number="level" type="range" min="0.6" max="3.6" step="0.005"/></label></div>
  <div class="lab-buttons"><button type="button" @click="choose('max')">Đỉnh cực đại</button><button type="button" @click="choose('min')">Đỉnh cực tiểu</button><button type="button" @click="mode='max';level=3.2">Ngưỡng không đạt</button><button type="button" @click="point=[2,2];level=value(point)">Điểm bên trong</button></div>
  <details class="lab-tasks"><summary>Di chuyển Q hoặc ngưỡng bằng nút</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-readout" role="status">
   <p>Q = {{fmtPoint(point,4)}}. f(Q) = {{fmt(value(point),5)}}. Ngưỡng t = {{fmt(level,5)}} {{Math.abs(level-value(point))<1e-8?'đi qua Q.':'được chọn độc lập với Q.'}}</p>
   <p>{{section.length?'Có':'Không có'}} điểm trong tứ giác thỏa f {{mode==='max'?'≥':'≤'}} t. Tại giá trị tối ưu, phần đạt ngưỡng có thể chỉ còn một đỉnh, không còn diện tích để tô.</p>
   <p>Giá trị {{mode==='max'?'lớn nhất':'nhỏ nhất'}} là {{fmt(best,6)}}. Theo thứ tự 1, 2, 3, 4, giá trị tại các đỉnh là {{values.map(v=>fmt(v,4)).join(', ')}}.</p>
   <p>Trong ví dụ này, hai đường tử số bằng 0 và mẫu số bằng 0 cắt nhau tại P = (−2/3, −2/3). Hình tia quay không áp dụng cho mọi cặp hàm affine, chẳng hạn 1/(x₁ + 1) có các đường mức song song.</p>
  </div>
 </figure>
</template>
<style scoped>
svg text{font-size:18px}
.accepted{fill:var(--xanh);fill-opacity:.22;stroke:none}
.lab-dot-good{fill:var(--xanh)}
.boundary{stroke:var(--xanh);stroke-width:2}
.denominator{stroke:var(--do);stroke-width:1.2;stroke-dasharray:5 5}
.level{stroke:var(--vang);stroke-width:1.8}
svg :is(line,polygon,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
