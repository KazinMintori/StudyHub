<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'
import {basisPairs,basisSolution,columnNames,resourceVertices} from '../services/lp-bases.mjs'

const svg=ref(null),capacity=ref(4),basis=ref(0)
const view=ref(makeView({x0:-1.1,x1:4.5,y0:-1.8,y1:5.8,width:400,height:410,pad:34}))
const selected=computed(()=>basisSolution(basisPairs[basis.value],capacity.value))
const polygon=computed(()=>resourceVertices(capacity.value).map(p=>view.value.point(p).join(',')).join(' '))
const handle=computed(()=>[0,capacity.value])
const drag=createDragger(svg,view,(_,p)=>{
  capacity.value=Math.max(1,Math.min(5,Math.round(p[1]*10)/10))
},{step:0.1})
const name=pair=>pair.map(i=>columnNames[i]).join(', ')
</script>

<template>
  <figure class="study-lab" aria-label="Cơ sở và điểm cực của miền quy hoạch tuyến tính">
    <figcaption class="lab-title">Hai cơ sở có thể biểu diễn cùng một đỉnh</figcaption>
    <p class="lab-lead">Miền xanh thỏa x + y ≤ b, x ≤ 2 và x, y ≥ 0. Kéo điểm vàng trên trục dọc để thay đổi tài nguyên b. Chọn hai cột để giải hệ cơ sở. Vòng tím chỉ hình chiếu của nghiệm cơ sở xuống mặt phẳng x, y.</p>
    <svg ref="svg" viewBox="0 0 400 410" role="group" aria-label="Giới hạn tài nguyên b kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="34" x2="366" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="34" y2="376" class="lab-axis" />
      <polygon :points="polygon" class="basis-feasible" />
      <line :x1="view.sx(2)" :x2="view.sx(2)" :y1="view.sy(0)" :y2="view.sy(5.2)" class="basis-limit" />
      <circle v-if="selected.x&&selected.x[0]<=4.1&&selected.x[1]>=-1.5" :cx="view.sx(selected.x[0])" :cy="view.sy(selected.x[1])" r="8" class="basis-selected" />
      <circle :cx="view.sx(0)" :cy="view.sy(capacity)" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(0)" :cy="view.sy(capacity)" r="32" class="lab-handle basis-hit" tabindex="0" role="slider"
        aria-label="Giới hạn tài nguyên b" :aria-valuetext="fmt(capacity,1)" aria-valuemin="1" aria-valuemax="5"
        @pointerdown="drag.start('b',$event)" @keydown="drag.key('b',handle,$event)" />
      <text x="15" y="25">y</text><text x="366" y="398">x</text><text :x="view.sx(2)+7" y="38">x = 2</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh b bằng nút</summary><LabPointControls :svg="svg" axes="y" /></details>
    <div class="lab-buttons">
      <button v-for="(pair,i) in basisPairs" :key="i" type="button" :aria-pressed="basis===i" @click="basis=i">{{name(pair)}}</button>
      <button type="button" @click="capacity=2">b = 2</button>
      <button type="button" @click="capacity=4">b = 4</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Cơ sở thử: {{name(basisPairs[basis])}}. Giới hạn b = {{fmt(capacity,1)}}.</p>
      <p v-if="selected.kind==='singular'">Hai cột phụ thuộc tuyến tính nên cặp này không tạo cơ sở.</p>
      <p v-else>(x, y, s₁, s₂) = {{fmtPoint(selected.x)}}. {{selected.kind==='infeasible'?'Có biến âm nên nghiệm cơ sở này không khả thi.':selected.kind==='degenerate'?'Nghiệm cơ sở khả thi suy biến vì một biến cơ sở bằng 0.':'Nghiệm cơ sở khả thi với hai biến cơ sở dương.'}}</p>
      <p>Khi b = 2, thử lần lượt các cặp (x, y), (x, s₁), (x, s₂). Cả ba đều cho cùng đỉnh (2, 0).</p>
    </div>
  </figure>
</template>

<style scoped>
.basis-feasible { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.4; }
.basis-limit { stroke: var(--ink-3); stroke-width: 1.2; stroke-dasharray: 4 4; }
.basis-selected { fill: var(--paper); stroke: var(--tim); stroke-width: 1.8; }
.basis-hit { fill: transparent !important; stroke: transparent; }
.basis-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
