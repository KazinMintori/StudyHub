<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'

const svgs=[ref(null),ref(null)],point=ref([1,1]),rate=ref(0.1),mu=ref(0.9)
const view=ref(makeView({x0:-3.4,x1:3.4,y0:-2.2,y1:2.2,width:400,height:330,pad:36}))
const methods=['Momentum','Nesterov']
const next=computed(()=>methods.map((_,i)=>{
  const [x,v]=point.value,at=i?x+mu.value*v:x
  const velocity=mu.value*v-rate.value*at
  return [x+velocity,velocity]
}))
const look=computed(()=>point.value[0]+mu.value*point.value[1])
const drags=svgs.map(svg=>createDragger(svg,view,(_,p)=>{point.value=[Math.max(-2,Math.min(2,p[0])),Math.max(-1,Math.min(1,p[1]))]},{step:0.05}))
function preset(p){point.value=p;rate.value=0.1;mu.value=0.9}
</script>

<template>
  <figure class="study-lab" aria-label="So sánh một bước Momentum và Nesterov với cùng vị trí và vận tốc">
    <figcaption class="lab-title">Nesterov có thể hãm đà mà vẫn làm mất mát tăng</figcaption>
    <p class="lab-lead">Hàm mất mát là θ²/2. Mỗi hình biểu diễn trạng thái gồm vị trí θ trên trục ngang và vận tốc v trên trục dọc. Kéo điểm vàng ở một trong hai hình. Điểm rỗng là trạng thái sau đúng một bước, không phải quỹ đạo liên tục.</p>
    <div class="lab-pair">
      <svg v-for="(name,i) in methods" :key="name" :ref="el=>svgs[i].value=el" viewBox="0 0 400 330" role="group" :aria-label="'Trạng thái '+name+' kéo được'"
        @pointermove="drags[i].move" @pointerup="drags[i].end" @pointercancel="drags[i].end" @lostpointercapture="drags[i].end">
        <line x1="36" x2="364" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
        <line :x1="view.sx(0)" :x2="view.sx(0)" y1="36" y2="294" class="lab-axis" />
        <line :x1="view.sx(point[0])" :y1="view.sy(point[1])" :x2="view.sx(next[i][0])" :y2="view.sy(next[i][1])" class="momentum-step" />
        <circle :cx="view.sx(next[i][0])" :cy="view.sy(next[i][1])" r="5" class="momentum-next" />
        <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="7" class="lab-dot-warn" />
        <circle :cx="view.sx(point[0])" :cy="view.sy(point[1])" r="32" class="lab-handle momentum-hit" tabindex="0" role="slider"
          :aria-label="'Vị trí và vận tốc '+name" :aria-valuetext="fmtPoint(point)" @pointerdown="drags[i].start('state',$event)" @keydown="drags[i].key('state',point,$event)" />
        <text x="12" y="27">v</text><text x="366" y="317">θ</text><text x="56" y="27">{{name}}</text>
      </svg>
    </div>
    <details class="lab-tasks"><summary>Điều chỉnh vị trí và vận tốc bằng nút</summary><LabPointControls :svg="svgs[0].value" /></details>
    <div class="lab-buttons">
      <button type="button" @click="preset([1,1])">Quán tính đi ra xa</button>
      <button type="button" @click="preset([1,-1])">Quán tính đi về nghiệm</button>
      <button type="button" @click="preset([1,0])">Vận tốc bằng 0</button>
      <button type="button" @click="rate=0.1">η = 0,1</button>
      <button type="button" @click="rate=0.5">η = 0,5</button>
      <button type="button" @click="mu=0">Bỏ quán tính</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Trạng thái (θ, v) = {{fmtPoint(point,3)}}. η = {{fmt(rate)}}, μ = {{fmt(mu)}}. Điểm lấy gradient của Nesterov có vị trí θ̃ = {{fmt(look,3)}}.</p>
      <p>Mất mát ban đầu = {{fmt(point[0]**2/2,4)}}.</p>
      <p v-for="(name,i) in methods" :key="name">{{name}}: Trạng thái mới {{fmtPoint(next[i],3)}}, mất mát {{fmt(next[i][0]**2/2,4)}}. {{next[i][0]**2>point[0]**2+1e-12?'Mất mát tăng trong bước này.':'Mất mát không tăng trong bước này.'}}</p>
      <p>Hai trục biểu diễn hai đại lượng khác nhau. Độ dài đoạn nối trên hình không phải thước đo tốc độ hội tụ.</p>
    </div>
  </figure>
</template>

<style scoped>
.momentum-step { stroke: var(--tim); stroke-width: 1.6; }
.momentum-next { fill: var(--paper); stroke: var(--tim); stroke-width: 1.8; }
.momentum-hit { fill: transparent !important; stroke: transparent; }
.momentum-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
