<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'
import {resourceVertices} from '../services/lp-bases.mjs'
import {clipSegment} from '../services/svg-clipping.mjs'

const svg=ref(null),objective=ref([3,2])
const vertices=resourceVertices(4)
const diagram=makeView({x0:-0.6,x1:4.6,y0:-0.6,y1:4.6,width:400,height:350,pad:36})
const controls=ref(makeView({x0:-6,x1:6,y0:-6,y1:6,width:400,height:400,pad:36}))
const values=computed(()=>vertices.map(p=>p[0]*objective.value[0]+p[1]*objective.value[1]))
const maximum=computed(()=>Math.max(...values.value))
const optimal=computed(()=>vertices.filter((_,i)=>Math.abs(values.value[i]-maximum.value)<1e-9))
const zero=computed(()=>Math.hypot(...objective.value)<1e-9)
const support=computed(()=>{
  if(zero.value)return null
  const [a,b]=objective.value
  const p=Math.abs(a)>Math.abs(b)?[maximum.value/a,0]:[0,maximum.value/b]
  const direction=[-b,a]
  const segment=clipSegment([p.map((x,i)=>x-20*direction[i]),p.map((x,i)=>x+20*direction[i])],diagram)
  return segment?.map(p=>diagram.point(p).join(',')).join(' ')
})
const drag=createDragger(svg,controls,(_,p)=>{objective.value=p.map(x=>Math.max(-5,Math.min(5,x)))},{step:0.1})
const polygon=vertices.map(p=>diagram.point(p).join(',')).join(' ')
</script>

<template>
  <figure class="study-lab" aria-label="Quy hoạch tuyến tính trên miền tài nguyên hai chiều">
    <figcaption class="lab-title">Cùng miền tài nguyên, đổi hướng mục tiêu để đổi tập nghiệm</figcaption>
    <p class="lab-lead">Miền thỏa x + y ≤ 4, x ≤ 2 và x, y ≥ 0. Kéo đầu vector c ở hình điều khiển để cực đại hóa c₁x + c₂y. Vòng xanh đánh dấu các đỉnh tối ưu và đường tím là mức mục tiêu cao nhất.</p>
    <svg viewBox="0 0 400 350" role="img" aria-label="Miền đa giác và đường mục tiêu tại mức tối ưu">
      <line x1="36" x2="364" :y1="diagram.sy(0)" :y2="diagram.sy(0)" class="lab-axis" />
      <line :x1="diagram.sx(0)" :x2="diagram.sx(0)" y1="36" y2="314" class="lab-axis" />
      <polygon :points="polygon" class="resource-region" />
      <polyline v-if="support" :points="support" class="resource-level" />
      <circle v-for="(p,i) in vertices" :key="i" :cx="diagram.sx(p[0])" :cy="diagram.sy(p[1])" r="4" class="lab-dot" />
      <circle v-for="(p,i) in optimal" :key="'best'+i" :cx="diagram.sx(p[0])" :cy="diagram.sy(p[1])" r="8" class="resource-best" />
      <text x="13" y="26">y</text><text x="368" y="337">x</text>
    </svg>
    <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Vector mục tiêu c kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="36" x2="364" :y1="controls.sy(0)" :y2="controls.sy(0)" class="lab-axis" />
      <line :x1="controls.sx(0)" :x2="controls.sx(0)" y1="36" y2="364" class="lab-axis" />
      <line :x1="controls.sx(0)" :y1="controls.sy(0)" :x2="controls.sx(objective[0])" :y2="controls.sy(objective[1])" class="resource-level" />
      <circle :cx="controls.sx(objective[0])" :cy="controls.sy(objective[1])" r="7" class="lab-dot-warn" />
      <circle :cx="controls.sx(objective[0])" :cy="controls.sy(objective[1])" r="32" class="lab-handle resource-hit" tabindex="0" role="slider"
        aria-label="Hai hệ số mục tiêu c" :aria-valuetext="fmtPoint(objective,3)"
        @pointerdown="drag.start('c',$event)" @keydown="drag.key('c',objective,$event)" />
      <text x="14" y="25">c₂</text><text x="368" y="387">c₁</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh hệ số bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" @click="objective=[3,2]">c = (3, 2)</button>
      <button type="button" @click="objective=[1,1]">Cả cạnh x + y = 4</button>
      <button type="button" @click="objective=[0,0]">Mục tiêu bằng 0</button>
    </div>
    <div class="lab-readout" role="status">
      <p>c = {{fmtPoint(objective,3)}}. Giá trị cực đại = {{fmt(maximum,4)}}.</p>
      <p v-if="zero">Mọi điểm của miền đều tối ưu.</p>
      <p v-else>Đỉnh tối ưu {{optimal.map(p=>fmtPoint(p,3)).join(' và ')}}. {{optimal.length>1?'Toàn bộ cạnh nối hai đỉnh này cũng tối ưu.':''}}</p>
    </div>
  </figure>
</template>

<style scoped>
.resource-region { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.5; }
.resource-level { fill: none; stroke: var(--tim); stroke-width: 1.7; }
.resource-best { fill: var(--paper); stroke: var(--xanh); stroke-width: 1.8; }
.resource-hit { fill: transparent !important; stroke: transparent; }
.resource-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
