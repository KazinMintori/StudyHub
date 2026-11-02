<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { project3, planeParameters, dot } from '../services/foundation-geometry.mjs'

const svg=ref(null), parameters=ref([0.2,-0.15]), yaw=ref(20), showKernel=ref(true)
const x0=[1,1,1], v1=[-2,1,0], v2=[-3,0,1], normal=[1,2,3]
const camera=computed(()=>({yaw:yaw.value,pitch:35,scale:38,origin:[200,210]}))
const P=p=>project3(p,camera.value)
const at=(s,t,base=x0)=>base.map((v,i)=>v+s*v1[i]+t*v2[i])
const point=computed(()=>at(...parameters.value))
const view=computed(()=>({x0:-0.5,x1:0.5,y0:-0.5,y1:0.5,toWorld:(x,y)=>planeParameters([x,y],P(x0),P(at(1,0)),P(at(0,1))) || parameters.value}))
const drag=createDragger(svg,view,(_,p)=>{parameters.value=p},{step:0.025,snap:0.005})
const polygon=base=>[[-.55,-.55],[.55,-.55],[.55,.55],[-.55,.55]].map(([s,t])=>P(at(s,t,base)).join(',')).join(' ')
const firstPart=computed(()=>at(parameters.value[0],0))
const axes=[{p:[3.8,0,0],label:'x₁'},{p:[0,3.8,0],label:'x₂'},{p:[0,0,3.8],label:'x₃'}]
</script>

<template>
  <figure class="study-lab" aria-label="Mặt phẳng nghiệm affine và không gian hạt nhân trong R³">
    <figcaption class="lab-title">Hai hướng tự do sinh ra một mặt phẳng</figcaption>
    <p class="lab-lead">Kéo x trên mặt phẳng tím. Mỗi vị trí tương ứng với một cặp (s, t), nhưng vẫn thỏa x₁ + 2x₂ + 3x₃ = 6. Mặt phẳng qua gốc giải hệ có vế phải bằng 0 và có cùng hai hướng tự do.</p>
    <svg ref="svg" viewBox="0 0 400 320" role="group" aria-label="Hai mặt phẳng song song, nghiệm riêng x₀ và điểm nghiệm x kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <g v-for="axis in axes" :key="axis.label"><line :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(axis.p)[0]" :y2="P(axis.p)[1]" class="lab-axis"/><text :x="P(axis.p)[0]+5" :y="P(axis.p)[1]-5">{{axis.label}}</text></g>
      <polygon v-if="showKernel" :points="polygon([0,0,0])" class="kernel-plane"/>
      <polygon :points="polygon(x0)" class="lab-region"/>
      <line :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(x0)[0]" :y2="P(x0)[1]" class="lab-line"/>
      <g v-for="(v,i) in [v1,v2]" :key="i"><line :x1="P(x0)[0]" :y1="P(x0)[1]" :x2="P(x0.map((z,j)=>z+0.45*v[j]))[0]" :y2="P(x0.map((z,j)=>z+0.45*v[j]))[1]" :class="i===0?'lab-good':'lab-warn'"/><text :x="P(x0.map((z,j)=>z+0.45*v[j]))[0]-20" :y="P(x0.map((z,j)=>z+0.45*v[j]))[1]-7">{{i===0?'v₁':'v₂'}}</text></g>
      <line :x1="P(x0)[0]" :y1="P(x0)[1]" :x2="P(firstPart)[0]" :y2="P(firstPart)[1]" class="lab-good"/>
      <line :x1="P(firstPart)[0]" :y1="P(firstPart)[1]" :x2="P(point)[0]" :y2="P(point)[1]" class="lab-warn"/>
      <circle :cx="P([0,0,0])[0]" :cy="P([0,0,0])[1]" r="4" class="lab-dot"/><text :x="P([0,0,0])[0]-24" :y="P([0,0,0])[1]+20">O</text>
      <circle :cx="P(x0)[0]" :cy="P(x0)[1]" r="5" class="lab-dot"/><text :x="P(x0)[0]-28" :y="P(x0)[1]+25">x₀</text>
      <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" class="lab-dot-accent" pointer-events="none"/><text :x="P(point)[0]+12" :y="P(point)[1]-10">x</text>
      <circle :cx="P(point)[0]" :cy="P(point)[1]" r="32" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Nghiệm x trên mặt phẳng" :aria-valuetext="`s = ${fmt(parameters[0])}, t = ${fmt(parameters[1])}, x = ${fmtPoint(point)}`" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',parameters,$event)"/>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/><p>Phím trái/phải đổi s. Phím lên/xuống đổi t. Hai tham số lần lượt dịch điểm theo v₁ và v₂, nên hướng trên màn hình có thể khác hướng của phím.</p></details>
    <p class="lab-legend"><span class="legend-accent">Ax = 6</span><span class="legend-guide">Ax = 0</span><span class="legend-good">Hướng v₁</span><span class="legend-warn">Hướng v₂</span></p>
    <div class="lab-controls"><label>Góc nhìn quanh x₃: {{yaw}}°<input v-model.number="yaw" type="range" min="-45" max="45" step="5"/></label><label class="lab-check"><input v-model="showKernel" type="checkbox"/>Hiện phần mặt phẳng Ax = 0</label></div>
    <div class="lab-buttons"><button type="button" @click="parameters=[0,0]">Về nghiệm riêng x₀</button></div>
    <div class="lab-readout" role="status"><p>x₀ = (1, 1, 1), v₁ = (−2, 1, 0), v₂ = (−3, 0, 1).</p><p>s = {{fmt(parameters[0])}}, t = {{fmt(parameters[1])}}. Nghiệm x = x₀ + sv₁ + tv₂ = {{fmtPoint(point)}}.</p><p>Ax = x₁ + 2x₂ + 3x₃ = {{fmt(dot(normal,point),4)}}. Av₁ = Av₂ = 0, nên thay s hoặc t không đổi vế phải.</p><p>Miền vẽ chỉ hiển thị một mảnh của mỗi mặt phẳng vô hạn. Ba tọa độ không phải ba hướng tự do độc lập: Ràng buộc để lại hai tham số s và t. Hình chiếu không bảo toàn góc và độ dài.</p></div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Giữ t cố định rồi thay s. Điểm chuyển động theo đường nào trên mặt phẳng?</li><li>Đưa điểm về x₀. Vì sao mặt phẳng Ax = 6 vẫn không đi qua O?</li><li>Ẩn mặt phẳng qua gốc, xoay hình rồi hiện lại. Hai mặt phẳng có còn song song không?</li></ol></details>
  </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
.kernel-plane{fill:var(--canvas);fill-opacity:.55;stroke:var(--ink-3);stroke-dasharray:5 4;stroke-width:1.5}
svg text{font-size:20px}
</style>
