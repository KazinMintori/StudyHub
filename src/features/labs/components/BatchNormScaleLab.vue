<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,makeView} from '../controllers/svg-drag.js'

const svg=ref(null),scale=ref(1),epsilon=ref(1)
const view=ref(makeView({x0:0,x1:3.5,y0:-1,y1:1,width:400,height:120,pad:36}))
const handle=computed(()=>[scale.value,0])
const original=computed(()=>1/Math.sqrt(1+epsilon.value))
const normalized=computed(()=>scale.value/Math.sqrt(scale.value**2+epsilon.value))
const drag=createDragger(svg,view,(_,p)=>{scale.value=Math.max(0.2,Math.min(3,p[0]))},{step:0.05})
const plot=makeView({x0:-1.2,x1:1.2,y0:0,y1:2,width:400,height:210,pad:34})
const rows=computed(()=>[{y:1.4,value:original.value},{y:0.6,value:normalized.value}])
</script>

<template>
  <figure class="study-lab" aria-label="Ảnh hưởng của epsilon lên chuẩn hóa lô khi đổi thang">
    <figcaption class="lab-title">Đổi thang lô và quan sát đầu ra chuẩn hóa</figcaption>
    <p class="lab-lead">Lô ban đầu gồm −1 và 1. Kéo điểm vàng để nhân cả hai giá trị với α. Dấu tròn biểu diễn lô ban đầu, ô vuông biểu diễn lô sau khi nhân. Mỗi hàng đặt hai đầu ra trên cùng trục giá trị.</p>
    <svg ref="svg" viewBox="0 0 400 120" role="group" aria-label="Kéo hệ số dương alpha"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line :x1="view.sx(0.2)" :x2="view.sx(3)" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <text x="34" y="23">α = 0,2</text><text x="311" y="23">α = 3</text>
      <circle :cx="view.sx(scale)" :cy="view.sy(0)" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(scale)" :cy="view.sy(0)" r="32" tabindex="0" role="slider" class="lab-handle bn-hit"
        aria-label="Hệ số alpha" :aria-valuetext="fmt(scale,3)" aria-valuemin="0.2" aria-valuemax="3"
        @pointerdown="drag.start('alpha',$event)" @keydown="drag.key('alpha',handle,$event)" />
    </svg>
    <svg viewBox="0 0 400 210" role="img" aria-label="Hai hàng giá trị sau chuẩn hóa">
      <line :x1="plot.sx(0)" :x2="plot.sx(0)" y1="30" y2="176" class="lab-axis" />
      <g v-for="(row,i) in rows" :key="i">
        <line x1="34" x2="366" :y1="plot.sy(row.y)" :y2="plot.sy(row.y)" class="lab-axis" />
        <g v-for="sign in [-1,1]" :key="sign">
          <circle v-if="i===0" :cx="plot.sx(sign*row.value)" :cy="plot.sy(row.y)" r="6" class="lab-dot-accent" />
          <rect v-else :x="plot.sx(sign*row.value)-5" :y="plot.sy(row.y)-5" width="10" height="10" class="bn-scaled" />
        </g>
      </g>
      <text :x="plot.sx(-1)" y="199" text-anchor="middle">−1</text>
      <text :x="plot.sx(0)" y="199" text-anchor="middle">0</text>
      <text :x="plot.sx(1)" y="199" text-anchor="middle">1</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh α bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="epsilon===0" @click="epsilon=0">ε = 0</button>
      <button type="button" :aria-pressed="epsilon===1" @click="epsilon=1">ε = 1</button>
      <button type="button" @click="scale=1">α = 1</button>
      <button type="button" @click="scale=2">α = 2</button>
    </div>
    <div class="lab-readout" role="status">
      <p>α = {{fmt(scale,3)}}, ε = {{epsilon}}. Cặp chuẩn hóa trước khi đổi thang là ({{fmt(-original,4)}}, {{fmt(original,4)}}).</p>
      <p>Cặp sau khi đổi thang là ({{fmt(-normalized,4)}}, {{fmt(normalized,4)}}).</p>
      <p>{{epsilon===0?'Với ε = 0 và phương sai lô dương, α triệt tiêu ở tử và mẫu.':'Với ε dương, sau khi rút gọn α, mẫu số còn chứa ε/α². Mức ε = 1 giúp thấy rõ sự khác biệt.'}}</p>
    </div>
  </figure>
</template>

<style scoped>
.bn-hit { fill: transparent !important; stroke: transparent; }
.bn-hit:focus-visible { stroke: var(--vang); }
.bn-scaled { fill: var(--xanh); }
svg text { font-size: 19px; pointer-events: none; }
</style>
