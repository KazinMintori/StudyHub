<script setup>
import {computed,ref,useId} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {chebyshevCertificate,project3,lineParameter} from '../services/foundation-geometry.mjs'
import {polyhedronInBox} from '../services/convex-geometry.mjs'
const svg=ref(null),dualSvg=ref(null),parameters=ref([0,1]),t=ref(0),clip='cheb-'+useId()
const view=ref(makeView({x0:-.4,x1:2.6,y0:-2.5,y1:6,width:400,height:400,pad:30})),P=p=>view.value.point(p)
const drag=createDragger(svg,view,(name,p)=>{
 if(name==='intercept')parameters.value=[Math.max(-1.5,Math.min(1,p[1])),parameters.value[1]]
 else parameters.value=[parameters.value[0],Math.max(-.5,Math.min(2,(p[1]-parameters.value[0])/2))]
},{step:.05,snap:.01})
const row=computed(()=>chebyshevCertificate(parameters.value,t.value))
const band=computed(()=>polyhedronInBox([
 {a:[parameters.value[1],-1],b:row.value.value-parameters.value[0]},
 {a:[-parameters.value[1],1],b:row.value.value+parameters.value[0]}
],[view.value.x0,view.value.x1,view.value.y0,view.value.y1]))
const camera={yaw:35,pitch:28,scale:200,origin:[200,235]},Q=p=>project3(p,camera)
const dualView=ref({x0:-.25,x1:.25,y0:0,y1:0,toWorld:(x,y)=>[lineParameter([x,y],Q([0,0,0]),Q([1,-2,1]))??t.value,0]})
const dualDrag=createDragger(dualSvg,dualView,(_,p)=>{t.value=p[0]},{step:.01,snap:.005})
const data=[[0,0],[1,0],[2,2]]
</script>

<template>
 <figure class="study-lab" aria-label="Chứng chỉ đối ngẫu của xấp xỉ Chebyshev ba quan sát">
  <figcaption class="lab-title">Ba sai số dao động và một chứng chỉ chuẩn L1</figcaption>
  <p class="lab-lead">Khớp đường y = w₀ + w₁t cho dữ liệu (0, 0), (1, 0), (2, 2). Kéo hai chấm dự đoán đầu và cuối theo chiều dọc. Kéo bộ ν ở hình sau để cải thiện cận dưới độc lập với đường khớp.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Ba quan sát, đường dự đoán, phần dư và hai điểm dự đoán kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <defs><clipPath :id="clip"><rect x="30" y="30" width="340" height="340"/></clipPath></defs>
    <polygon :points="band.map(p=>P(p).join(',')).join(' ')" class="lab-region-soft"/>
    <line x1="30" x2="370" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis"/>
    <g :clip-path="`url(#${clip})`"><line :x1="P([-.4,parameters[0]-.4*parameters[1]])[0]" :y1="P([-.4,parameters[0]-.4*parameters[1]])[1]" :x2="P([2.6,parameters[0]+2.6*parameters[1]])[0]" :y2="P([2.6,parameters[0]+2.6*parameters[1]])[1]" class="lab-accent"/></g>
    <g v-for="(point,i) in data" :key="i"><line :x1="P(point)[0]" :y1="P(point)[1]" :x2="P([point[0],row.prediction[i]])[0]" :y2="P([point[0],row.prediction[i]])[1]" class="lab-bad"/><circle :cx="P(point)[0]" :cy="P(point)[1]" r="6" class="lab-dot"/></g>
    <circle v-for="i in [0,2]" :key="i" :cx="P([i,row.prediction[i]])[0]" :cy="P([i,row.prediction[i]])[1]" r="7" class="lab-dot-warn"/>
    <circle v-for="i in [0,2]" :key="'handle'+i" :cx="P([i,row.prediction[i]])[0]" :cy="P([i,row.prediction[i]])[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" :aria-label="i===0?'Dự đoán tại t = 0, đổi w₀':'Dự đoán tại t = 2, đổi w₁'" :aria-valuetext="`w = ${fmtPoint(parameters,3)}, dự đoán ${fmt(row.prediction[i],3)}`" @pointerdown="drag.start(i===0?'intercept':'slope',$event)" @keydown="drag.key(i===0?'intercept':'slope',[i,row.prediction[i]],$event)"/>
    <text x="12" y="23">Không gian quan sát (t, y)</text><text v-for="i in [0,1,2]" :key="'label'+i" :x="view.sx(i)-5" :y="view.sy(0)+25">{{i}}</text><text x="352" :y="view.sy(0)+25">t</text>
   </svg>
   <svg ref="dualSvg" viewBox="0 0 400 400" role="group" aria-label="Đoạn khả thi của ν trong hạt nhân A chuyển vị, giới hạn bởi chuẩn L1 không quá 1" @pointermove="dualDrag.move" @pointerup="dualDrag.end" @pointercancel="dualDrag.end" @lostpointercapture="dualDrag.end">
    <line :x1="Q([-.25,.5,-.25])[0]" :y1="Q([-.25,.5,-.25])[1]" :x2="Q([.25,-.5,.25])[0]" :y2="Q([.25,-.5,.25])[1]" class="lab-accent"/>
    <circle v-for="z in [-.25,0,.25]" :key="z" :cx="Q([z,-2*z,z])[0]" :cy="Q([z,-2*z,z])[1]" r="6" class="lab-dot-hollow"/>
    <text :x="Q([-.25,.5,-.25])[0]-15" :y="Q([-.25,.5,-.25])[1]+27">z = −1/4</text><text :x="Q([.25,-.5,.25])[0]-58" :y="Q([.25,-.5,.25])[1]-15">z = 1/4</text>
    <circle :cx="Q(row.nu)[0]" :cy="Q(row.nu)[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="Q(row.nu)[0]" :cy="Q(row.nu)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Nhân tử ν = z(1, −2, 1)" :aria-valuetext="`z = ${fmt(t,3)}, ν = ${fmtPoint(row.nu,3)}`" @pointerdown="dualDrag.start('nu',$event)" @keydown="dualDrag.key('nu',[t,0],$event)"/>
    <text x="12" y="23">Đoạn nhân tử trong R³</text><text x="36" y="370">Aᵀν = 0, ‖ν‖₁ ≤ 1</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="y"/><LabPointControls :svg="dualSvg" axes="x"/></details>
  <p class="lab-legend"><span class="legend-accent">Đường khớp</span><span class="legend-guide">Vùng nhạt: Dải sai số hai phía ±‖r‖∞</span><span class="legend-bad">Phần dư theo chiều dọc</span></p>
  <div class="lab-buttons"><button type="button" @click="parameters=[-.5,1]">Đường tối ưu</button><button type="button" @click="t=.25">Chứng chỉ tối ưu</button><button type="button" @click="parameters=[0,1];t=0">Bắt đầu lại</button></div>
  <div class="lab-readout" role="status">
   <p>w = {{fmtPoint(parameters,3)}}, phần dư r = Aw − b = {{fmtPoint(row.residual,3)}}. Sai số lớn nhất ‖r‖∞ = {{fmt(row.value,4)}}.</p>
   <p>ν = {{fmtPoint(row.nu,3)}}. ‖ν‖₁ = {{fmt(row.norm,4)}}. Mọi điểm trên đoạn đều thỏa Aᵀν = 0. Cận dưới bᵀν = {{fmt(row.dual,4)}}, nên giá trị tối ưu nằm trong [{{fmt(row.dual,4)}}, {{fmt(row.value,4)}}].</p>
   <p>Độ rộng chứng nhận là {{fmt(row.gap,4)}}. Chọn đường tối ưu và chứng chỉ tối ưu để hai cận cùng bằng 1/2. Ba phần dư khi đó có dấu −, +, − và độ lớn cùng bằng 1/2. Cả ba quan sát chạm biên dải sai số, luân phiên ở phía trên và dưới đường khớp.</p>
   <p>Đoạn nhân tử là một đoạn trong không gian R³, không phải toàn bộ không gian đó. Tọa độ z chỉ tham số hóa đoạn ν = z(1, −2, 1), với −1/4 ≤ z ≤ 1/4. Hai điểm dự đoán ở hình đầu là đại lượng kéo được, còn ba chấm dữ liệu đen đứng yên.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Giữ đường khớp rồi kéo z tới 1/4. Vì sao cận dưới tăng mà sai số đường không đổi?</li><li>Với ν tối ưu, thử tìm đường có sai số nhỏ hơn 1/2. Điều gì ngăn việc đó?</li><li>Vì sao các dấu −, +, − của phần dư phù hợp các dấu +, −, + của chứng chỉ?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
