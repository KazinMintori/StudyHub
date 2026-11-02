<script setup>
import { computed,ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger,fmt,fmtPoint } from '../controllers/svg-drag.js'
import { project3,planeParameters,lineFitSpace } from '../services/foundation-geometry.mjs'
const svg=ref(null),parameters=ref([1,1]),yaw=ref(-20)
const row=computed(()=>lineFitSpace(...parameters.value)),optimum=lineFitSpace(1.5,5/6)
const camera=computed(()=>({yaw:yaw.value,pitch:30,scale:42,origin:[200,240]})),P=p=>project3(p,camera.value)
const point=(a,c)=>lineFitSpace(a,c).prediction
const view=computed(()=>({x0:0,x1:2,y0:-.5,y1:1.5,toWorld:(x,y)=>planeParameters([x,y],P([0,0,0]),P([0,1,2]),P([1,1,1]))||parameters.value}))
const drag=createDragger(svg,view,(_,p)=>{parameters.value=p},{step:.025,snap:.005})
const plane=[point(0,-.5),point(2,-.5),point(2,1.5),point(0,1.5)]
const mesh=Array.from({length:7},(_,i)=>[[point(i/3,-.5),point(i/3,1.5)],[point(0,-.5+i/3),point(2,-.5+i/3)]]).flat()
const axes=[{p:[3,0,0],label:'b₁'},{p:[0,4,0],label:'b₂'},{p:[0,0,5.5],label:'b₃'}]
const isBest=computed(()=>Math.abs(parameters.value[0]-1.5)+Math.abs(parameters.value[1]-5/6)<1e-8)
</script>

<template>
 <figure class="study-lab" aria-label="Phép chiếu bình phương tối thiểu từ dữ liệu R³ lên mặt phẳng dự đoán">
  <figcaption class="lab-title">Hai tham số tạo một mặt phẳng trong không gian ba quan sát</figcaption>
  <p class="lab-lead">Với t = 0, 1, 2, mô hình y = at + c cho vector dự đoán Ax = (c, a + c, 2a + c). Kéo điểm dự đoán trên mặt phẳng để đổi a và c. Dữ liệu b = (1, 2, 4) đứng yên.</p>
  <svg ref="svg" viewBox="0 0 400 360" role="group" aria-label="Mặt phẳng các dự đoán, dữ liệu b, điểm dự đoán Ax kéo được và hình chiếu tối ưu" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <g v-for="axis in axes" :key="axis.label"><line :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(axis.p)[0]" :y2="P(axis.p)[1]" class="lab-axis"/><text :x="P(axis.p)[0]+5" :y="P(axis.p)[1]+5">{{axis.label}}</text></g>
   <polygon :points="plane.map(p=>P(p).join(',')).join(' ')" class="lab-region plane"/>
   <line v-for="(line,i) in mesh" :key="i" :x1="P(line[0])[0]" :y1="P(line[0])[1]" :x2="P(line[1])[0]" :y2="P(line[1])[1]" class="lab-guide mesh"/>
   <line :x1="P(row.target)[0]" :y1="P(row.target)[1]" :x2="P(row.prediction)[0]" :y2="P(row.prediction)[1]" class="lab-bad"/>
   <line :x1="P(row.target)[0]" :y1="P(row.target)[1]" :x2="P(optimum.prediction)[0]" :y2="P(optimum.prediction)[1]" class="lab-good"/>
   <circle :cx="P(row.target)[0]" :cy="P(row.target)[1]" r="6" class="lab-dot"/><text :x="P(row.target)[0]+10" :y="P(row.target)[1]-12">b</text>
   <circle :cx="P(optimum.prediction)[0]" :cy="P(optimum.prediction)[1]" r="6" class="lab-dot-hollow"/><text :x="P(optimum.prediction)[0]-45" :y="P(optimum.prediction)[1]-12">Ax*</text>
   <circle :cx="P(row.prediction)[0]" :cy="P(row.prediction)[1]" r="8" class="lab-dot-accent" pointer-events="none"/><text :x="P(row.prediction)[0]+12" :y="P(row.prediction)[1]+23">{{isBest?'Ax = Ax*':'Ax'}}</text>
   <text :x="P([0,0,0])[0]-20" :y="P([0,0,0])[1]+20">O</text>
   <circle :cx="P(row.prediction)[0]" :cy="P(row.prediction)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Vector dự đoán Ax trên mặt phẳng" :aria-valuetext="`a = ${fmt(parameters[0])}, c = ${fmt(parameters[1])}, Ax = ${fmtPoint(row.prediction)}`" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',parameters,$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/><p>Trái/phải đổi a, lên/xuống đổi c. Trên hình chiếu, các hướng này không nhất thiết cùng hướng với nút.</p></details>
  <p class="lab-legend"><span class="legend-accent">Mặt phẳng các dự đoán</span><span class="legend-bad">Phần dư đang chọn</span><span class="legend-good">Phần dư ngắn nhất</span></p>
  <div class="lab-controls"><label>Góc nhìn quanh b₃: {{yaw}}°<input v-model.number="yaw" type="range" min="-45" max="10" step="5"/></label></div>
  <div class="lab-buttons"><button type="button" @click="parameters=[1.5,5/6]">Đưa về nghiệm tối ưu</button><button type="button" @click="parameters=[1,1]">Đường y = t + 1</button></div>
  <div class="lab-readout" role="status"><p>a = {{fmt(parameters[0],3)}}, c = {{fmt(parameters[1],3)}}. Ax = {{fmtPoint(row.prediction)}}.</p><p>r = Ax − b = {{fmtPoint(row.residual)}}. Tổng bình phương sai số bằng {{fmt(row.value,4)}}.</p><p>Aᵀr = {{fmtPoint(row.normalResidual,4)}}. {{isBest?'Tại nghiệm tối ưu, cả hai thành phần bằng 0: Phần dư vuông góc với cả hai cột của A.':'Một vector phần dư chưa vuông góc với mặt phẳng cho biết dự đoán còn có thể được cải thiện.'}}</p><p>Nghiệm tối ưu có a = 3/2 và c = 5/6. Dự đoán tối ưu là hình chiếu trực giao duy nhất của b lên mặt phẳng các dự đoán. Hai tham số ở không gian R², còn dự đoán và phần dư ở R³.</p><p>Hình chỉ vẽ một mảnh của mặt phẳng vô hạn. Góc vuông của phép chiếu trong không gian có thể không hiện thành góc vuông trên màn hình.</p></div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Kéo dự đoán lại gần b. Vì sao không thể đưa nó trùng b?</li><li>Bấm về nghiệm tối ưu. Vì sao sai số vẫn khác 0 dù Aᵀr bằng 0?</li><li>Giữ a rồi thay c bằng các nút. Vector dự đoán dịch theo hướng cột nào của A?</li></ol></details>
 </figure>
</template>

<style scoped>
.plane{fill-opacity:.35}
.mesh{opacity:.4;stroke-width:1}
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
</style>
