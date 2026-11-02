<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { dot, norm2, project3, unprojectPlane, projectToHyperplane, planeBoxSection } from '../services/foundation-geometry.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'

const svg=ref(null), xy=ref([1,1]), z=ref(1), offset=ref(6), yaw=ref(25), normalChoice=ref('tilted')
const normals={tilted:[1,-2,2],vertical:[1,0,0],horizontal:[0,0,1]}
const normal=computed(()=>normals[normalChoice.value])
const point=computed(()=>[...xy.value,z.value])
const camera=computed(()=>({yaw:yaw.value,pitch:28,scale:38,origin:[200,170]}))
const P=p=>project3(p,camera.value)
const projection=computed(()=>projectToHyperplane(point.value,normal.value,offset.value))
const onPlane=computed(()=>Math.abs(projection.value.signed)<1e-8)
const closest=computed(()=>normal.value.map(v=>offset.value*v/dot(normal.value,normal.value)))
const tip=computed(()=>closest.value.map((v,i)=>v+normal.value[i]/norm2(normal.value)))
const section=computed(()=>planeBoxSection(normal.value,offset.value,2.5))
const view=computed(()=>({x0:-2,x1:2,y0:-2,y1:2,toWorld:(x,y)=>unprojectPlane([x,y],z.value,camera.value)}))
const drag=createDragger(svg,view,(_,p)=>{xy.value=p},{step:.1,snap:.01})
const inBox=p=>p.every(v=>Math.abs(v)<=3)
const axes=[{p:[3.1,0,0],label:'x₁'},{p:[0,3.1,0],label:'x₂'},{p:[0,0,3.1],label:'x₃'}]
const labels=computed(()=>{
 const specifications=[{key:'point',text:onPlane.value?'x = h':'x',point:P(point.value)}]
 if(inBox(tip.value))specifications.push({key:'normal',text:'a',point:P(tip.value)})
 if(inBox(projection.value.foot)&&!onPlane.value)specifications.push({key:'foot',text:'h',point:P(projection.value.foot)})
 const reserved=axes.map(axis=>{const p=P(axis.p);return{x:p[0]+1,y:p[1]-21,width:34,height:30}})
 return placePointLabels(specifications,{width:400,height:340,reserved})
})
function preset(choice){normalChoice.value=choice;offset.value=choice==='tilted'?6:0}
</script>

<template>
  <figure class="study-lab" aria-label="Siêu phẳng, pháp tuyến và khoảng cách có dấu trong R³">
    <figcaption class="lab-title">Từ đường thẳng trong R² sang mặt phẳng trong R³</figcaption>
    <p class="lab-lead">Kéo x trong lát cắt ngang có x₃ cố định. Đổi x₃ để đi ra khỏi lát cắt. Mặt tím thỏa aᵀx = b. Đoạn từ x đến chân chiếu h vuông góc với mặt phẳng, còn pháp tuyến chỉ phía có aᵀx lớn hơn b.</p>
    <div class="lab-buttons" role="group" aria-label="Phương của mặt phẳng"><button type="button" :aria-pressed="normalChoice==='tilted'" @click="preset('tilted')">Mặt nghiêng</button><button type="button" :aria-pressed="normalChoice==='vertical'" @click="preset('vertical')">Mặt đứng</button><button type="button" :aria-pressed="normalChoice==='horizontal'" @click="preset('horizontal')">Mặt ngang</button></div>
    <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Mảnh mặt phẳng vô hạn, lát cắt ngang và điểm x kéo được cùng chân chiếu" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polygon :points="[[-2,-2,z],[2,-2,z],[2,2,z],[-2,2,z]].map(p=>P(p).join(',')).join(' ')" class="slice"/>
      <g v-for="axis in axes" :key="axis.label"><line :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(axis.p)[0]" :y2="P(axis.p)[1]" class="lab-axis"/><text :x="P(axis.p)[0]+5" :y="P(axis.p)[1]+5">{{axis.label}}</text></g>
      <polygon v-if="section.length>=3" :points="section.map(p=>P(p).join(',')).join(' ')" class="lab-region plane"/>
      <line v-if="inBox(closest)&&inBox(tip)" :x1="P(closest)[0]" :y1="P(closest)[1]" :x2="P(tip)[0]" :y2="P(tip)[1]" class="lab-good"/>
      <text v-if="labels.normal" :x="labels.normal.x" :y="labels.normal.y" :text-anchor="labels.normal.anchor">a</text>
      <line v-if="inBox(projection.foot)" :x1="P(point)[0]" :y1="P(point)[1]" :x2="P(projection.foot)[0]" :y2="P(projection.foot)[1]" :class="projection.signed<=0?'lab-good':'lab-bad'"/>
      <circle v-if="inBox(projection.foot)&&!onPlane" :cx="P(projection.foot)[0]" :cy="P(projection.foot)[1]" r="5" class="lab-dot-hollow"/><text v-if="labels.foot" :x="labels.foot.x" :y="labels.foot.y" :text-anchor="labels.foot.anchor">h</text>
      <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" class="lab-dot-accent" pointer-events="none"/><text :x="labels.point.x" :y="labels.point.y" :text-anchor="labels.point.anchor">{{onPlane?'x = h':'x'}}</text>
      <circle :cx="P(point)[0]" :cy="P(point)[1]" r="32" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Điểm x trong lát cắt ngang" :aria-valuetext="fmtPoint(point)" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',xy,$event)"/>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
    <p class="lab-legend"><span class="legend-accent">aᵀx = b</span><span class="legend-guide">Lát x₃ cố định</span><span class="legend-good">Phía aᵀx ≤ b</span><span class="legend-bad">Phía aᵀx > b</span></p>
    <div class="lab-controls"><label>x₃ = {{fmt(z)}}<input v-model.number="z" type="range" min="-2" max="2" step=".1"/></label><label>b = {{fmt(offset)}}<input v-model.number="offset" type="range" min="-6" max="6" step=".2"/></label><label>Góc nhìn: {{yaw}}°<input v-model.number="yaw" type="range" min="-50" max="50" step="5"/></label></div>
    <div class="lab-buttons"><button type="button" @click="xy=[1,1];z=1;offset=6;normalChoice='tilted'">Ví dụ x = (1, 1, 1), b = 6</button></div>
    <div class="lab-readout" role="status"><p>a = {{fmtPoint(normal,0)}}, x = {{fmtPoint(point)}}, aᵀx − b = {{fmt(dot(normal,point)-offset)}}.</p><p>Khoảng cách có dấu δ = {{fmt(projection.signed,4)}}. {{Math.abs(projection.signed)<1e-8?'x nằm trên mặt phẳng.':projection.signed<0?'x thuộc nửa không gian aᵀx ≤ b.':'x nằm ngoài nửa không gian aᵀx ≤ b.'}}</p><p>Chân chiếu h = {{fmtPoint(projection.foot)}}. aᵀh = {{fmt(dot(normal,projection.foot),4)}} = b.</p><p v-if="!section.length">Mặt phẳng đang nằm ngoài khối xem hình. Nó vẫn tồn tại, không phải là tập rỗng.</p><p>Mảnh đa giác chỉ giới hạn vùng vẽ, không phải biên của mặt phẳng. Màu đoạn khoảng cách cho biết phía của x theo phép tính. Hình chiếu trên màn hình có thể làm góc vuông trông nghiêng.</p></div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Với mặt nghiêng và b = 6, điểm (1, 1, 1) có khoảng cách có dấu bằng bao nhiêu?</li><li>Chọn mặt đứng rồi đổi riêng x₃. Khoảng cách có thay đổi không?</li><li>Chọn mặt ngang. Vì sao kéo điểm trong lát cắt ngang không đổi khoảng cách, còn thay x₃ thì có?</li></ol></details>
  </figure>
</template>

<style scoped>
.slice{fill:var(--canvas);stroke:var(--ink-3);stroke-dasharray:4 4;stroke-width:1;fill-opacity:.7}
.plane{fill-opacity:.45}
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
</style>
