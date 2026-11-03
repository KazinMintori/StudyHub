<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt} from '../controllers/svg-drag.js'
import {fitData,fittedIntercept,fittedError} from '../services/qp-geometry.mjs'
import {clipSegment} from '../services/svg-clipping.mjs'
const dataSvg=ref(null),curveSvg=ref(null),slope=ref(1),bounded=ref(true)
const data=makeView({x0:0,x1:5,y0:0,y1:9,width:360,height:300,pad:35})
const curve=makeView({x0:-.1,x1:2.4,y0:0,y1:15,width:360,height:300,pad:35})
const dataView=computed(()=>({x0:0,x1:0,y0:0,y1:bounded.value?1:2.2,toWorld:(_,y)=>[0,(data.wy(y)-4.5)/1.5]}))
const curveView=computed(()=>({x0:0,x1:bounded.value?1:2.2,y0:0,y1:1,toWorld:x=>[curve.wx(x),0]}))
const dataDrag=createDragger(dataSvg,dataView,(_,p)=>{slope.value=p[1]},{step:.05})
const curveDrag=createDragger(curveSvg,curveView,(_,p)=>{slope.value=p[0]},{step:.05})
const intercept=computed(()=>fittedIntercept(slope.value))
const plottedLine=computed(()=>clipSegment([[0,intercept.value],[5,5*slope.value+intercept.value]],data))
const parabola=Array.from({length:111},(_,i)=>{const a=i/50;return curve.point([a,fittedError(a)]).join(',')}).join(' ')
function setBound(value){bounded.value=value;if(value)slope.value=Math.min(1,slope.value)}
</script>
<template>
 <figure class="study-lab" aria-label="Bình phương tối thiểu có ràng buộc hệ số và tối ưu từng phần">
  <figcaption class="lab-title">Giữ hệ số góc, tối ưu hệ số chặn, rồi đọc parabol sai số</figcaption>
  <p class="lab-lead">Kéo chấm tím trên đường khớp theo phương đứng, hoặc kéo điểm trên parabol theo phương ngang. Với mỗi hệ số góc a, hệ số chặn luôn được tối ưu thành b = 4.5 − 2.5a. Hai hình biểu diễn cùng một lựa chọn a.</p>
  <div class="lab-pair">
   <svg ref="dataSvg" viewBox="0 0 360 300" role="group" aria-label="Bốn điểm dữ liệu, đường hồi quy và các sai số thẳng đứng" @pointermove="dataDrag.move" @pointerup="dataDrag.end" @pointercancel="dataDrag.end" @lostpointercapture="dataDrag.end">
    <line x1="30" :y1="data.sy(0)" x2="330" :y2="data.sy(0)" class="lab-axis"/><line :x1="data.sx(0)" y1="23" :x2="data.sx(0)" y2="267" class="lab-axis"/>
    <text x="332" y="286">u</text><text x="45" y="23">y</text>
    <line v-for="(p,i) in fitData" :key="i" :x1="data.sx(p[0])" :x2="data.sx(p[0])" :y1="data.sy(p[1])" :y2="data.sy(slope*p[0]+intercept)" class="residual"/>
    <line v-if="plottedLine" :x1="data.sx(plottedLine[0][0])" :y1="data.sy(plottedLine[0][1])" :x2="data.sx(plottedLine[1][0])" :y2="data.sy(plottedLine[1][1])" class="fit"/>
    <circle v-for="(p,i) in fitData" :key="i" :cx="data.sx(p[0])" :cy="data.sy(p[1])" r="5" class="lab-dot"/>
    <circle :cx="data.sx(4)" :cy="data.sy(4.5+1.5*slope)" r="6" class="lab-dot-accent"/>
    <circle :cx="data.sx(4)" :cy="data.sy(4.5+1.5*slope)" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Hệ số góc, kéo điểm theo phương đứng" :aria-valuetext="fmt(slope,5)" @pointerdown="dataDrag.start('slope',$event)" @keydown="dataDrag.key('slope',[0,slope],$event)"/>
   </svg>
   <svg ref="curveSvg" viewBox="0 0 360 300" role="group" aria-label="Parabol tổng bình phương sai số sau khi khử hệ số chặn" @pointermove="curveDrag.move" @pointerup="curveDrag.end" @pointercancel="curveDrag.end" @lostpointercapture="curveDrag.end">
    <rect v-if="bounded" :x="curve.sx(0)" y="35" :width="curve.sx(1)-curve.sx(0)" height="230" class="allowed"/>
    <line x1="30" :y1="curve.sy(0)" x2="330" :y2="curve.sy(0)" class="lab-axis"/><line :x1="curve.sx(0)" y1="23" :x2="curve.sx(0)" y2="267" class="lab-axis"/>
    <text x="332" y="286">a</text><text x="53" y="23">J(a)</text><text :x="curve.sx(1)" y="289" text-anchor="middle">1</text><text :x="curve.sx(1.7)" y="289" text-anchor="middle">1.7</text>
    <polyline :points="parabola" class="fit"/>
    <circle :cx="curve.sx(1.7)" :cy="curve.sy(.05)" r="5" class="unconstrained"/>
    <circle :cx="curve.sx(slope)" :cy="curve.sy(fittedError(slope))" r="6" class="lab-dot-accent"/>
    <circle :cx="curve.sx(slope)" :cy="curve.sy(fittedError(slope))" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Hệ số góc trên parabol, kéo ngang" :aria-valuetext="fmt(slope,5)" @pointerdown="curveDrag.start('slope',$event)" @keydown="curveDrag.key('slope',[slope,0],$event)"/>
   </svg>
  </div>
  <div class="lab-buttons"><button type="button" @click="setBound(false);slope=1.7">Nghiệm tự do</button><button type="button" @click="setBound(true);slope=1">Nghiệm với 0 ≤ a ≤ 1</button><button type="button" @click="slope=.5">Thử a = 0.5</button></div>
  <details class="lab-tasks"><summary>Đổi a bằng nút trên hình dữ liệu</summary><LabPointControls :svg="dataSvg" axes="y"/></details>
  <details class="lab-tasks"><summary>Đổi a bằng nút trên parabol</summary><LabPointControls :svg="curveSvg" axes="x"/></details>
  <div class="lab-readout" role="status">
   <p>a = {{fmt(slope,5)}}, b = {{fmt(intercept,5)}}. Tổng bình phương sai số J = {{fmt(fittedError(slope),6)}}. {{bounded?'Đang giữ 0 ≤ a ≤ 1.':'Đã bỏ giới hạn a ≤ 1; hình cho thử a trong [0, 2.2].'}}</p>
   <p>J(a) = 5(a − 1.7)² + 0.05. Nghiệm tự do có a = 1.7, b = 0.25 và J = 0.05. Thêm giới hạn cho a làm nghiệm chuyển tới a = 1, b = 2 và J = 2.5.</p>
   <p>Các đoạn vàng đo sai số theo y. Sai số được bình phương rồi cộng, không phải khoảng cách vuông góc từ điểm tới đường. Chỉ a bị chặn, còn b vẫn được tính lại sau mỗi thay đổi.</p>
  </div>
 </figure>
</template>
<style scoped>
svg text{font-size:18px}
.fit{fill:none;stroke:var(--tim);stroke-width:1.8}
.residual{stroke:var(--vang);stroke-width:1.4}
.allowed{fill:var(--xanh-soft)}
.unconstrained{fill:var(--xanh)}
svg :is(line,polyline,rect,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
