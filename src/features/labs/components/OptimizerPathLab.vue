<script setup>
import {computed,ref,watch} from 'vue'
import LabPointControls from './LabPointControls.vue'
import SimulationControls from './SimulationControls.vue'
import {optimizerTrace} from '../services/math-ai.mjs'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'
import {clipPolyline,clipSegment} from '../services/svg-clipping.mjs'
import {project3,unprojectPlane} from '../services/foundation-geometry.mjs'

const props=defineProps({adaptive:Boolean})
const defaultMethod=props.adaptive?'adam':'momentum'
const extraMethods={newton:'Newton',adagrad:'AdaGrad',rmsprop:'RMSProp',adam:'Adam'}
const svg=ref(null),start=ref([2,2]),method=ref(defaultMethod),rate=ref(0.1),kappa=ref(10),momentum=ref(0.9),step=ref(0)
const bounds={x0:-3.2,x1:3.2,y0:-3.2,y1:3.2}
const flat=makeView({...bounds,width:400,height:340,pad:36})
const space=ref(false)
const camera={yaw:35,pitch:32,scale:30,origin:[200,218]}
const view=computed(()=>space.value?{...bounds,toWorld:(x,y)=>unprojectPlane([x,y],0,camera)}:flat)
const ground=p=>space.value?project3([...p,0],camera):flat.point(p)
const surface=p=>project3([...p,(p[0]**2+kappa.value*p[1]**2)*4/(18*(1+kappa.value))],camera)
const trace=computed(()=>optimizerTrace({method:method.value,rate:rate.value,kappa:kappa.value,momentum:momentum.value,start:start.value,steps:30}))
const row=computed(()=>trace.value[step.value])
const inside=p=>p.every(Number.isFinite)&&p[0]>=bounds.x0&&p[0]<=bounds.x1&&p[1]>=bounds.y0&&p[1]<=bounds.y1
const shown=computed(()=>trace.value.slice(0,step.value+1))
const coordinates=(points,project=ground)=>points.map(p=>project(p).join(',')).join(' ')
const path=computed(()=>shown.value.slice(1).flatMap((row,i)=>{
  const from=shown.value[i].x,to=row.x
  if(!inside(from)&&!inside(to))return []
  const segment=clipSegment([from,to],bounds)
  return segment?[coordinates(segment)]:[]
}))
const contour=computed(()=>[0.5,2,5,10].map(c=>{
  const points=Array.from({length:129},(_,i)=>{const a=2*Math.PI*i/128;return [Math.sqrt(2*c)*Math.cos(a),Math.sqrt(2*c/kappa.value)*Math.sin(a)]})
  return clipPolyline(points,bounds).map(points=>coordinates(points))
}))
const mesh=computed(()=>[-3,-2,-1,0,1,2,3].flatMap(fixed=>[0,1].map(axis=>{
  const points=Array.from({length:25},(_,i)=>{const moving=-3+i/4;return axis===0?[fixed,moving]:[moving,fixed]})
  return coordinates(points,surface)
})))
watch([start,method,rate,kappa,momentum],()=>{step.value=0})
const drag=createDragger(svg,view,(_,p)=>{start.value=p.map(x=>Math.max(-2.7,Math.min(2.7,x)));step.value=0},{step:0.1})
function stable(){start.value=[2,2];method.value=defaultMethod;rate.value=0.1;kappa.value=10;momentum.value=0.9;step.value=0}
</script>

<template>
  <figure class="study-lab" aria-label="Đường cập nhật trên hàm toàn phương">
    <figcaption class="lab-title">Đổi điểm xuất phát trực tiếp trên đường đồng mức</figcaption>
    <p class="lab-lead">Hàm f(x, y) = (x² + κy²)/2 dùng gradient toàn phần. Kéo điểm xuất phát màu vàng rồi xem từng bước. Ở chế độ R³, lưới biểu diễn độ cao của hàm và các bước nằm trên mặt phẳng tham số bên dưới.</p>
    <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Điểm xuất phát kéo được trên mặt phẳng tham số"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polyline :points="coordinates([[-3.2,0],[3.2,0]])" class="lab-axis" />
      <polyline :points="coordinates([[0,-3.2],[0,3.2]])" class="lab-axis" />
      <template v-if="space"><polyline v-for="(line,i) in mesh" :key="i" :points="line" class="optimizer-mesh" /></template>
      <template v-else><g v-for="(curves,i) in contour" :key="i"><polyline v-for="(curve,j) in curves" :key="j" :points="curve" class="optimizer-contour" /></g></template>
      <polyline v-for="(segment,i) in path" :key="i" :points="segment" class="optimizer-path" />
      <template v-for="r in shown" :key="r.iteration"><circle v-if="inside(r.x)" :cx="ground(r.x)[0]" :cy="ground(r.x)[1]" r="2.2" class="optimizer-history" /></template>
      <circle v-if="step>0&&inside(row.x)" :cx="ground(row.x)[0]" :cy="ground(row.x)[1]" r="5" class="lab-dot-accent" />
      <circle :cx="ground(start)[0]" :cy="ground(start)[1]" r="7" class="lab-dot-warn" />
      <circle :cx="ground(start)[0]" :cy="ground(start)[1]" r="32" class="lab-handle optimizer-hit" tabindex="0" role="slider"
        aria-label="Điểm xuất phát của thuật toán" :aria-valuetext="fmtPoint(start)" @pointerdown="drag.start('start',$event)" @keydown="drag.key('start',start,$event)" />
      <template v-if="space"><text x="20" y="29">Mặt f(x, y)</text><text x="20" y="325">Mặt phẳng tham số</text></template>
      <template v-else><text x="12" y="26">y</text><text x="366" y="328">x</text></template>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh điểm xuất phát bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-controls">
      <label>η = {{fmt(rate)}}<input v-model.number="rate" type="range" min="0.01" max="0.4" step="0.01" :disabled="method==='newton'" /></label>
      <label>κ = {{kappa}}<input v-model.number="kappa" type="range" min="1" max="20" step="1" /></label>
      <label>μ = {{fmt(momentum)}}<input v-model.number="momentum" type="range" min="0" max="0.95" step="0.05" :disabled="method!=='momentum'&&method!=='nesterov'" /></label>
    </div>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="space" @click="space=!space">{{space?'Về đường đồng mức R²':'Xem mặt trong R³'}}</button>
      <button type="button" :aria-pressed="method==='gd'" @click="method='gd'">Gradient toàn phần</button>
      <button type="button" :aria-pressed="method==='momentum'" @click="method='momentum'">Momentum</button>
      <button type="button" :aria-pressed="method==='nesterov'" @click="method='nesterov'">Nesterov</button>
      <template v-if="adaptive">
        <button v-for="(label,key) in extraMethods" :key="key" type="button" :aria-pressed="method===key" @click="method=key">{{label}}</button>
      </template>
      <button type="button" @click="stable">Khôi phục ví dụ</button>
      <button type="button" @click="step=10">Xem bước 10</button>
      <button type="button" @click="method='gd';rate=0.3;kappa=10;step=0">Thử bước gradient quá lớn</button>
    </div>
    <SimulationControls v-model="step" :max="trace.length-1" :reset-key="trace" />
    <div class="lab-readout" role="status">
      <p>Bước {{step}}, vị trí {{fmtPoint(row.x,4)}}, f = {{fmt(row.value,4)}}. Khởi đầu {{fmtPoint(start)}}.</p>
      <p v-if="method==='adagrad'">Tổng bình phương gradient {{fmtPoint(row.sum,4)}}.</p>
      <p v-if="method==='rmsprop'">Trung bình mũ của bình phương gradient {{fmtPoint(row.v,4)}}.</p>
      <p v-if="method==='adam'">Mômen trước hiệu chỉnh m = {{fmtPoint(row.m,4)}}, v = {{fmtPoint(row.v,4)}}.</p>
      <p v-if="!inside(row.x)">Điểm hiện tại vượt miền vẽ. Bảng vẫn tính giá trị. Hình giữ các bước có đầu hoặc cuối trong khung và cắt chúng tại biên.</p>
      <p v-else>Kéo vòng tại điểm xuất phát để tạo một lần chạy mới. Vận tốc đầu được đặt lại bằng 0.</p>
      <p>Thay đổi η, μ hoặc κ có thể làm thuật toán dao động hay phân kỳ. Mô phỏng hữu hạn không chứng minh tốc độ hội tụ cho mọi hàm.</p>
    </div>
  </figure>
</template>

<style scoped>
.optimizer-contour { fill: none; stroke: var(--ink-3); stroke-width: 1; stroke-dasharray: 4 5; }
.optimizer-mesh { fill: none; stroke: var(--ink-3); stroke-width: 1; opacity: 0.65; }
.optimizer-path { fill: none; stroke: var(--tim); stroke-width: 1.7; }
.optimizer-history { fill: var(--ink-3); }
.optimizer-hit { fill: transparent !important; stroke: transparent; }
.optimizer-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
