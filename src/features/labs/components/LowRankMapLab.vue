<script setup>
import {computed,ref} from 'vue'
import MathMatrix from '../../../core/math/components/MathMatrix.vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'
import {planeParameters,project3} from '../services/foundation-geometry.mjs'

const inputSvg=ref(null),outputSvg=ref(null),h=ref([0.6,0.3]),tied=ref(false),rank=ref(1),second=ref(false),yaw=ref(25)
const singular=computed(()=>tied.value?[1,1]:[3,1])
const inputView=ref(makeView({x0:-1.35,x1:1.35,y0:-1.35,y1:1.35,width:400,height:400,pad:38}))
const camera=computed(()=>({yaw:yaw.value,pitch:35,scale:44,origin:[200,205]}))
const P=p=>project3(p,camera.value)
const target=computed(()=>[singular.value[0]*h.value[0],0,singular.value[1]*h.value[1]])
const keepSecond=computed(()=>tied.value&&second.value&&rank.value===1)
const approximation=computed(()=>rank.value===2?target.value:keepSecond.value?[0,0,target.value[2]]:[target.value[0],0,0])
const outputView=computed(()=>({x0:-1,x1:1,y0:-1,y1:1,toWorld:(x,y)=>planeParameters([x,y],P([0,0,0]),P([singular.value[0],0,0]),P([0,0,singular.value[1]]))||h.value}))
function move(_,point){const norm=Math.hypot(...point);h.value=norm>1?point.map(v=>v/norm):point}
const inputDrag=createDragger(inputSvg,inputView,move,{step:0.05})
const outputDrag=createDragger(outputSvg,outputView,move,{step:0.05})
const circle=Array.from({length:120},(_,i)=>[Math.cos(i*Math.PI/60),Math.sin(i*Math.PI/60)])
const image=computed(()=>circle.map(p=>P([singular.value[0]*p[0],0,singular.value[1]*p[1]]).join(',')).join(' '))
const bestLine=computed(()=>[-1,1].map(sign=>P(keepSecond.value?[0,0,sign]:[sign*singular.value[0],0,0]).join(',')).join(' '))
const residual=computed(()=>rank.value===2?0:keepSecond.value?singular.value[0]**2:singular.value[1]**2)
const total=computed(()=>singular.value.reduce((sum,v)=>sum+v*v,0))
const original=computed(()=>[[singular.value[0],0],[0,0],[0,singular.value[1]]])
function spectrum(value){tied.value=value;second.value=false}
</script>

<template>
 <figure class="study-lab" aria-label="Xấp xỉ ma trận hạng thấp từ R² tới R³">
  <figcaption class="lab-title">Hạng một chỉ giữ một hướng của ảnh</figcaption>
  <p class="lab-lead">Kéo h trong đĩa đơn vị hoặc kéo điểm Mh ở hình không gian. Ma trận M đã biết đưa R² vào mặt phẳng x₂ = 0 của R³. Vòng xanh là Mᵣh sau khi cắt SVD. Các hình chỉ biểu diễn ảnh của đĩa đơn vị.</p>
  <svg ref="inputSvg" viewBox="0 0 400 400" role="group" aria-label="Vector đầu vào h trong R² kéo được"
   @pointermove="inputDrag.move" @pointerup="inputDrag.end" @pointercancel="inputDrag.end" @lostpointercapture="inputDrag.end">
   <line x1="38" x2="362" :y1="inputView.sy(0)" :y2="inputView.sy(0)" class="lab-axis"/>
   <line :x1="inputView.sx(0)" :x2="inputView.sx(0)" y1="38" y2="362" class="lab-axis"/>
   <polygon :points="circle.map(p=>inputView.point(p).join(',')).join(' ')" class="rank-domain"/>
   <line :x1="inputView.sx(0)" :y1="inputView.sy(0)" :x2="inputView.sx(h[0])" :y2="inputView.sy(h[1])" class="rank-vector"/>
   <circle :cx="inputView.sx(h[0])" :cy="inputView.sy(h[1])" r="7" class="lab-dot-accent"/>
   <circle :cx="inputView.sx(h[0])" :cy="inputView.sy(h[1])" r="32" class="lab-handle rank-hit" role="slider" tabindex="0" aria-label="Vector h" :aria-valuetext="fmtPoint(h,3)"
    @pointerdown="inputDrag.start('h',$event)" @keydown="inputDrag.key('h',h,$event)"/>
   <text x="365" y="387">h₁</text><text x="15" y="24">h₂</text>
  </svg>
  <svg ref="outputSvg" viewBox="0 0 400 350" role="group" aria-label="Ảnh Mh kéo được trên mặt phẳng hai chiều trong R³"
   @pointermove="outputDrag.move" @pointerup="outputDrag.end" @pointercancel="outputDrag.end" @lostpointercapture="outputDrag.end">
   <polygon :points="image" class="rank-domain"/>
   <g v-for="(axis,i) in [[3.7,0,0],[0,2,0],[0,0,2]]" :key="i">
    <line :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(axis)[0]" :y2="P(axis)[1]" class="lab-axis"/>
    <text :x="P(axis)[0]+8" :y="P(axis)[1]-8">x{{['₁','₂','₃'][i]}}</text>
   </g>
   <polyline v-if="rank===1" :points="bestLine" class="rank-kept"/>
   <line :x1="P(target)[0]" :y1="P(target)[1]" :x2="P(approximation)[0]" :y2="P(approximation)[1]" class="lab-guide"/>
   <circle :cx="P(target)[0]" :cy="P(target)[1]" r="6" class="lab-dot-accent"/>
   <circle :cx="P(approximation)[0]" :cy="P(approximation)[1]" r="9" class="rank-result"/>
   <circle :cx="P(target)[0]" :cy="P(target)[1]" r="32" class="lab-handle rank-hit" role="slider" tabindex="0" aria-label="Ảnh Mh của h" :aria-valuetext="fmtPoint(target,3)"
    @pointerdown="outputDrag.start('h',$event)" @keydown="outputDrag.key('h',h,$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh h bằng nút</summary><LabPointControls :svg="inputSvg"/></details>
  <div class="lab-buttons">
   <button type="button" @click="spectrum(false)">Phổ 3 và 1</button><button type="button" @click="spectrum(true)">Hai trị kỳ dị bằng 1</button>
   <button type="button" @click="rank=1;second=false">Giữ một hướng</button><button type="button" @click="rank=2">Giữ hai hướng</button>
   <button type="button" :disabled="!tied" @click="rank=1;second=!second">Đổi nghiệm khi phổ bằng nhau</button>
   <button type="button" @click="yaw=yaw===25?-25:25">Xoay mặt phẳng</button>
  </div>
  <div class="lab-readout" role="status">
   <p>M = <MathMatrix :rows="original" label="Ma trận M cỡ ba nhân hai"/>. h = {{fmtPoint(h,3)}}.</p>
   <p>Mh = {{fmtPoint(target,3)}}. Mᵣh = {{fmtPoint(approximation,3)}}.</p>
   <p>Hạng giữ lại r = {{rank}}. Bình phương sai số Frobenius = {{fmt(residual,3)}}. Tỷ lệ tổng bình phương trị kỳ dị được giữ = {{fmt(100*(1-residual/total),1)}}%.</p>
   <p v-if="tied&&rank===1">Hai trị kỳ dị trùng nhau: Hai lựa chọn đang minh họa là hai nghiệm tối ưu khác nhau. Còn nhiều nghiệm tối ưu khác.</p>
   <p>Mô hình này xấp xỉ một ma trận đã biết. Trong LoRA, A và B được học theo hàm mất mát của tác vụ, nên nghiệm huấn luyện không mặc nhiên là phép cắt SVD của một cập nhật đầy đủ.</p>
  </div>
 </figure>
</template>

<style scoped>
.rank-domain{fill:var(--tim-soft);stroke:var(--tim);stroke-width:1.4;fill-opacity:.3}
.rank-vector{stroke:var(--tim);stroke-width:1.6}
.rank-kept{fill:none;stroke:var(--xanh);stroke-width:1.8}
.rank-result{fill:var(--paper);stroke:var(--xanh);stroke-width:1.8;fill-opacity:.3}
.rank-hit{fill:transparent!important;stroke:transparent}
.rank-hit:focus-visible{stroke:transparent}
svg:has(.rank-hit:focus-visible) .lab-dot-accent{stroke:var(--vang);stroke-width:2}
svg text{font-size:20px;pointer-events:none}
</style>
