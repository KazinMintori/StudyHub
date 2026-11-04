<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'
import {clipSegment} from '../services/svg-clipping.mjs'

const pointSvg=ref(null),stepSvg=ref(null),point=ref([2,1]),step=ref(1),newton=ref(false)
const bounds={x0:-3.4,x1:3.4,y0:-3.4,y1:3.4}
const plane=ref(makeView({...bounds,width:400,height:340,pad:36}))
const value=p=>p[0]**2+2*p[1]**2
const gradient=computed(()=>[2*point.value[0],4*point.value[1]])
const direction=computed(()=>newton.value?point.value.map(v=>-v):gradient.value.map(v=>-v))
const derivative=computed(()=>gradient.value.reduce((sum,g,i)=>sum+g*direction.value[i],0))
const trial=t=>point.value.map((x,i)=>x+t*direction.value[i])
const armijo=t=>value(point.value)+0.1*t*derivative.value
const accepted=computed(()=>step.value>0&&value(trial(step.value))<=armijo(step.value)+1e-12)
const scale=computed(()=>Math.max(1,value(point.value),value(trial(1))))
const chart=computed(()=>makeView({x0:-0.1,x1:1.1,y0:-0.05*scale.value,y1:1.08*scale.value,width:400,height:340,pad:36}))
const pointDrag=createDragger(pointSvg,plane,(_,p)=>{
  point.value=p.map(v=>Math.max(-2.6,Math.min(2.6,v)))
  step.value=1
},{step:0.1})
const stepDrag=createDragger(stepSvg,chart,(_,p)=>{step.value=Math.max(0,Math.min(1,p[0]))},{step:0.025})
const contours=[1,4,9].map(c=>Array.from({length:81},(_,i)=>{
  const angle=2*Math.PI*i/80
  return plane.value.point([Math.sqrt(c)*Math.cos(angle),Math.sqrt(c/2)*Math.sin(angle)]).join(',')
}).join(' '))
const path=computed(()=>clipSegment([point.value,trial(step.value)],bounds)?.map(p=>plane.value.point(p).join(',')).join(' '))
const curve=computed(()=>Array.from({length:101},(_,i)=>chart.value.point([i/100,value(trial(i/100))]).join(',')).join(' '))
const cap=computed(()=>[0,1].map(t=>chart.value.point([t,armijo(t)]).join(',')).join(' '))
const inside=p=>p.every(v=>v>=bounds.x0&&v<=bounds.x1)
function reset(position){point.value=position;step.value=1;newton.value=false}
function apply(){
  if(!accepted.value)return
  point.value=trial(step.value)
  step.value=1
}
</script>

<template>
  <figure class="study-lab" aria-label="Hai vòng thử bước Armijo trên hàm toàn phương">
    <figcaption class="lab-title">Hướng giảm vẫn cần một hệ số bước phù hợp</figcaption>
    <p class="lab-lead">Hàm f(x, y) = x² + 2y². Kéo điểm xuất phát trong hình đường mức, hoặc kéo t trên đồ thị bên cạnh. Đường xanh nét đứt là cận Armijo với α = 0,1. Đường tím là mục tiêu thật tại điểm thử.</p>
    <div class="lab-pair">
      <svg ref="pointSvg" viewBox="0 0 400 340" role="group" aria-label="Điểm hiện tại kéo được trên đường mức"
        @pointermove="pointDrag.move" @pointerup="pointDrag.end" @pointercancel="pointDrag.end" @lostpointercapture="pointDrag.end">
        <polyline v-for="(curve,i) in contours" :key="i" :points="curve" class="armijo-contour" />
        <polyline v-if="path" :points="path" class="armijo-trial" />
        <circle v-if="inside(trial(step))" :cx="plane.sx(trial(step)[0])" :cy="plane.sy(trial(step)[1])" r="5" class="armijo-next" />
        <circle :cx="plane.sx(point[0])" :cy="plane.sy(point[1])" r="7" class="lab-dot-warn" />
        <circle :cx="plane.sx(point[0])" :cy="plane.sy(point[1])" r="32" class="lab-handle armijo-hit" tabindex="0" role="slider"
          aria-label="Điểm bắt đầu của bước Armijo" :aria-valuetext="fmtPoint(point,3)"
          @pointerdown="pointDrag.start('x',$event)" @keydown="pointDrag.key('x',point,$event)" />
        <text x="14" y="25">y</text><text x="368" y="326">x</text>
      </svg>
      <svg ref="stepSvg" viewBox="0 0 400 340" role="group" aria-label="Hệ số bước thử t kéo được"
        @pointermove="stepDrag.move" @pointerup="stepDrag.end" @pointercancel="stepDrag.end" @lostpointercapture="stepDrag.end">
        <polyline :points="curve" class="armijo-value" />
        <polyline :points="cap" class="armijo-cap" />
        <circle :cx="chart.sx(step)" :cy="chart.sy(value(trial(step)))" r="7" class="lab-dot-warn" />
        <circle :cx="chart.sx(step)" :cy="chart.sy(value(trial(step)))" r="32" class="lab-handle armijo-hit" tabindex="0" role="slider"
          aria-label="Hệ số bước t" :aria-valuetext="fmt(step,4)" aria-valuemin="0" aria-valuemax="1"
          @pointerdown="stepDrag.start('t',$event)" @keydown="stepDrag.key('t',[step,value(trial(step))],$event)" />
        <text x="16" y="26">Mục tiêu tại điểm thử</text><text x="369" y="326">t</text>
      </svg>
    </div>
    <details class="lab-tasks"><summary>Điều chỉnh điểm hiện tại bằng nút</summary><LabPointControls :svg="pointSvg" /></details>
    <details class="lab-tasks"><summary>Điều chỉnh hệ số bước bằng nút</summary><LabPointControls :svg="stepSvg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" @click="reset([2,1])">Vòng một tại (2, 1)</button>
      <button type="button" @click="reset([0,-1])">Vòng hai tại (0, −1)</button>
      <button type="button" @click="step/=2">Chia đôi bước thử</button>
      <button type="button" :disabled="!accepted" @click="apply">Nhận bước này</button>
      <button type="button" :aria-pressed="newton" @click="newton=!newton;step=1">Đổi gradient và Newton</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Điểm hiện tại {{fmtPoint(point,4)}}. Hướng {{newton?'Newton':'gradient âm'}} = {{fmtPoint(direction,4)}}. Đạo hàm theo hướng = {{fmt(derivative,4)}}.</p>
      <p>t = {{fmt(step,4)}}, điểm thử {{fmtPoint(trial(step),4)}}. Mục tiêu thật {{fmt(value(trial(step)),4)}}, cận Armijo {{fmt(armijo(step),4)}}.</p>
      <p>{{accepted?'Điểm thử đạt điều kiện giảm đủ.':'Bước chưa đạt điều kiện giảm đủ.'}} Đồ thị mục tiêu tự điều chỉnh thang đứng theo điểm hiện tại.</p>
    </div>
  </figure>
</template>

<style scoped>
.armijo-contour { fill: none; stroke: var(--ink-3); stroke-width: 1; stroke-dasharray: 4 4; }
.armijo-trial,.armijo-value { fill: none; stroke: var(--tim); stroke-width: 1.7; }
.armijo-cap { fill: none; stroke: var(--xanh); stroke-width: 1.7; stroke-dasharray: 5 4; }
.armijo-next { fill: var(--paper); stroke: var(--tim); stroke-width: 1.6; }
.armijo-hit { fill: transparent !important; stroke: transparent; }
.armijo-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
