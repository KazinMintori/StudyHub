<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,makeView} from '../controllers/svg-drag.js'
import {clipPolyline} from '../services/svg-clipping.mjs'

const referenceSvg=ref(null),trialSvg=ref(null)
const reference=ref(2),penalty=ref(1),limit=ref(0.5),trial=ref(0)
const free=computed(()=>reference.value/(1+penalty.value))
const optimum=computed(()=>Math.max(-limit.value,Math.min(limit.value,free.value)))
const value=x=>(x-reference.value)**2+penalty.value*x*x
const control=ref(makeView({x0:-3.5,x1:3.5,y0:-1,y1:1,width:400,height:110,pad:36}))
const referencePoint=computed(()=>[reference.value,0])
const referenceDrag=createDragger(referenceSvg,control,(_,p)=>{reference.value=Math.max(-3,Math.min(3,p[0]))},{step:0.1})
const bounds={x0:-2.1,x1:2.1,y0:-1,y1:29}
const chart=ref(makeView({...bounds,width:400,height:350,pad:36}))
const trialDrag=createDragger(trialSvg,chart,(_,p)=>{trial.value=Math.max(-limit.value,Math.min(limit.value,p[0]))},{step:0.05})
const curves=computed(()=>{
  const points=Array.from({length:121},(_,i)=>{
    const x=-2+i/30
    return [x,value(x)]
  })
  return clipPolyline(points,bounds).map(points=>points.map(p=>chart.value.point(p).join(',')).join(' '))
})
function chooseLimit(value){limit.value=value;trial.value=Math.max(-value,Math.min(value,trial.value))}
</script>

<template>
  <figure class="study-lab" aria-label="Hình chiếu nghiệm tự do lên đoạn vận tốc an toàn">
    <figcaption class="lab-title">Giới hạn an toàn có thể giữ nghiệm ở đầu mút</figcaption>
    <p class="lab-lead">Mục tiêu là (v − vref)² + λv² với |v| ≤ vmax. Kéo vận tốc tham chiếu trên thanh phía trên và điểm thử trong đoạn tô xanh bên dưới. Vòng tím đánh dấu nghiệm tự do, vòng xanh là nghiệm có ràng buộc.</p>
    <svg ref="referenceSvg" viewBox="0 0 400 110" role="group" aria-label="Vận tốc tham chiếu kéo được"
      @pointermove="referenceDrag.move" @pointerup="referenceDrag.end" @pointercancel="referenceDrag.end" @lostpointercapture="referenceDrag.end">
      <line :x1="control.sx(-3)" :x2="control.sx(3)" :y1="control.sy(0)" :y2="control.sy(0)" class="lab-axis" />
      <text x="34" y="23">vref = −3</text><text x="283" y="23">vref = 3</text>
      <circle :cx="control.sx(reference)" :cy="control.sy(0)" r="7" class="lab-dot-warn" />
      <circle :cx="control.sx(reference)" :cy="control.sy(0)" r="32" class="lab-handle control-hit" tabindex="0" role="slider"
        aria-label="Vận tốc tham chiếu" :aria-valuetext="fmt(reference,3)" aria-valuemin="-3" aria-valuemax="3"
        @pointerdown="referenceDrag.start('reference',$event)" @keydown="referenceDrag.key('reference',referencePoint,$event)" />
    </svg>
    <svg ref="trialSvg" viewBox="0 0 400 350" role="group" aria-label="Vận tốc thử trong đoạn an toàn kéo được"
      @pointermove="trialDrag.move" @pointerup="trialDrag.end" @pointercancel="trialDrag.end" @lostpointercapture="trialDrag.end">
      <rect :x="chart.sx(-limit)" y="36" :width="chart.sx(limit)-chart.sx(-limit)" height="278" class="control-feasible" />
      <line x1="36" x2="364" :y1="chart.sy(0)" :y2="chart.sy(0)" class="lab-axis" />
      <polyline v-for="(curve,i) in curves" :key="i" :points="curve" class="control-curve" />
      <circle :cx="chart.sx(free)" :cy="chart.sy(value(free))" r="7" class="control-free" />
      <circle :cx="chart.sx(optimum)" :cy="chart.sy(value(optimum))" r="9" class="control-optimum" />
      <circle :cx="chart.sx(trial)" :cy="chart.sy(value(trial))" r="6" class="lab-dot-warn" />
      <circle :cx="chart.sx(trial)" :cy="chart.sy(value(trial))" r="32" class="lab-handle control-hit" tabindex="0" role="slider"
        aria-label="Vận tốc thử v" :aria-valuetext="fmt(trial,3)" :aria-valuemin="-limit" :aria-valuemax="limit"
        @pointerdown="trialDrag.start('v',$event)" @keydown="trialDrag.key('v',[trial,value(trial)],$event)" />
      <text x="16" y="24">f(v)</text><text x="368" y="336">v</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh tham chiếu bằng nút</summary><LabPointControls :svg="referenceSvg" axes="x" /></details>
    <details class="lab-tasks"><summary>Điều chỉnh vận tốc thử bằng nút</summary><LabPointControls :svg="trialSvg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" @click="reference=2;penalty=1;chooseLimit(0.5);trial=0">Ví dụ bị chặn</button>
      <button type="button" @click="penalty=1">λ = 1</button>
      <button type="button" @click="penalty=2">λ = 2</button>
      <button type="button" @click="chooseLimit(0.5)">vmax = 0,5</button>
      <button type="button" @click="chooseLimit(1.5)">vmax = 1,5</button>
      <button type="button" @click="trial=optimum">Đưa điểm thử về nghiệm</button>
    </div>
    <div class="lab-readout" role="status">
      <p>vref = {{fmt(reference,3)}}, λ = {{fmt(penalty)}}, vmax = {{fmt(limit)}}. Nghiệm tự do {{fmt(free,4)}}, nghiệm có ràng buộc {{fmt(optimum,4)}}.</p>
      <p>Vận tốc thử {{fmt(trial,4)}}, mục tiêu {{fmt(value(trial),4)}}. Giá trị tối ưu {{fmt(value(optimum),4)}}.</p>
      <p>Đạo hàm tại nghiệm = {{fmt(2*(1+penalty)*optimum-2*reference,4)}}. {{Math.abs(free)>limit?'Giới hạn vận tốc chặt tại nghiệm.':'Nghiệm tự do thuộc đoạn an toàn.'}}</p>
    </div>
  </figure>
</template>

<style scoped>
.control-feasible { fill: var(--xanh-soft); }
.control-curve { fill: none; stroke: var(--ink-3); stroke-width: 1.5; }
.control-free { fill: var(--paper); stroke: var(--tim); stroke-width: 1.7; }
.control-optimum { fill: var(--paper); stroke: var(--xanh); stroke-width: 1.8; }
.control-hit { fill: transparent !important; stroke: transparent; }
.control-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
