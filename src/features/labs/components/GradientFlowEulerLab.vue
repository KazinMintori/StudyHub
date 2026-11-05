<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,makeView} from '../controllers/svg-drag.js'
import {clipPolyline} from '../services/svg-clipping.mjs'

const svg=ref(null),initial=ref(1.5),curvature=ref(1),step=ref(0.5)
const bounds={x0:-0.2,x1:3.2,y0:-2.5,y1:2.5}
const view=ref(makeView({...bounds,width:400,height:350,pad:36}))
const exact=t=>initial.value*Math.exp(-curvature.value*t)
const factor=computed(()=>1-curvature.value*step.value)
const samples=computed(()=>Array.from({length:Math.floor(3/step.value)+1},(_,k)=>[k*step.value,initial.value*factor.value**k]))
const last=computed(()=>samples.value.at(-1))
const P=p=>view.value.point(p)
const clipped=points=>clipPolyline(points,bounds).map(segment=>segment.map(p=>P(p).join(',')).join(' '))
const exactCurve=computed(()=>clipped(Array.from({length:121},(_,i)=>[i/40,exact(i/40)])))
const eulerCurve=computed(()=>clipped(samples.value))
const visibleSamples=computed(()=>samples.value.filter(([,x])=>Math.abs(x)<=2.5))
const initialPoint=computed(()=>[0,initial.value])
const drag=createDragger(svg,view,(_,p)=>{initial.value=Math.max(-2,Math.min(2,p[1]))},{step:0.1})
</script>

<template>
 <figure class="study-lab" aria-label="So sánh dòng gradient chính xác và bước Euler">
  <figcaption class="lab-title">Dòng liên tục giảm đều, bước rời rạc có thể vượt quá xa</figcaption>
  <p class="lab-lead">Xét f(x) = ax²/2 với a dương. Kéo điểm xuất phát ở t = 0. Đường tím là x(t) = x₀ exp(−at). Các chấm xanh là bước Euler xₖ₊₁ = (1 − aη)xₖ. Trục ngang là thời gian, trục đứng là trạng thái x.</p>
  <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Trạng thái theo thời gian và điểm xuất phát kéo được"
   @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line x1="36" x2="364" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis"/>
   <line :x1="view.sx(0)" :x2="view.sx(0)" y1="36" y2="314" class="lab-axis"/>
   <polyline v-for="(line,i) in exactCurve" :key="'c'+i" :points="line" class="flow-exact"/>
   <polyline v-for="(line,i) in eulerCurve" :key="'e'+i" :points="line" class="flow-euler"/>
   <circle v-for="(p,i) in visibleSamples" :key="i" :cx="P(p)[0]" :cy="P(p)[1]" r="3" class="flow-sample"/>
   <circle :cx="view.sx(0)" :cy="view.sy(initial)" r="7" class="lab-dot-warn"/>
   <circle :cx="view.sx(0)" :cy="view.sy(initial)" r="32" class="lab-handle flow-hit" tabindex="0" role="slider" aria-label="Trạng thái ban đầu x₀" :aria-valuetext="fmt(initial,3)"
    @pointerdown="drag.start('x0',$event)" @keydown="drag.key('x0',initialPoint,$event)"/>
   <text x="14" y="25">x</text><text x="367" y="337">t</text>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh x₀ bằng nút</summary><LabPointControls :svg="svg" axes="y" /></details>
  <div class="lab-buttons">
   <button type="button" @click="curvature=1;step=.5;initial=1.5">Ví dụ ổn định</button>
   <button type="button" @click="curvature=4;step=.5;initial=1.5">Đúng ngưỡng dao động</button>
   <button type="button" @click="curvature=4;step=.75;initial=1.5">Bước quá lớn</button>
   <button type="button" @click="step=.2">Giảm bước còn 0,2</button>
   <button type="button" @click="initial=0">Xuất phát tại nghiệm</button>
  </div>
  <div class="lab-readout" role="status">
   <p>a = {{fmt(curvature)}}, η = {{fmt(step)}}, x₀ = {{fmt(initial,3)}}. Hệ số mỗi bước 1 − aη = {{fmt(factor,3)}}.</p>
   <p>Tại t = {{fmt(last[0],2)}}: Dòng chính xác x(t) = {{fmt(exact(last[0]),5)}}, Euler xₖ = {{fmt(last[1],5)}}.</p>
   <p>Năng lượng ban đầu {{fmt(curvature*initial*initial/2,5)}}, năng lượng Euler tại mốc cuối {{fmt(curvature*last[1]**2/2,5)}}.</p>
   <p>{{Math.abs(factor)<1?'Euler hội tụ về 0 khi lặp tiếp.':Math.abs(factor)===1?'Ở cấu hình này, Euler giữ nguyên độ lớn khi x₀ khác 0.':'Khi x₀ khác 0, Euler khuếch đại độ lớn qua mỗi bước.'}} Các phần quỹ đạo vượt |x| = 2,5 được cắt khỏi hình, nhưng giá trị cuối vẫn được tính đầy đủ.</p>
  </div>
 </figure>
</template>

<style scoped>
.flow-exact{fill:none;stroke:var(--tim);stroke-width:1.7}
.flow-euler{fill:none;stroke:var(--xanh);stroke-width:1.4;stroke-dasharray:5 4}
.flow-sample{fill:var(--xanh)}
.flow-hit{fill:transparent!important;stroke:transparent}
.flow-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
</style>
