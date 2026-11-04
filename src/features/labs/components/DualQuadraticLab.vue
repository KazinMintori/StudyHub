<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,fmtPoint,makeView} from '../controllers/svg-drag.js'

const svg=ref(null),dimension=ref(1),multiplier=ref(2)
const view=ref(makeView({x0:-0.2,x1:4.2,y0:-4.5,y1:1.5,width:400,height:350,pad:36}))
const dual=value=>value-dimension.value*value*value/4
const primal=computed(()=>1/dimension.value)
const minimizer=computed(()=>Array(dimension.value).fill(multiplier.value/2))
const curve=computed(()=>Array.from({length:101},(_,i)=>view.value.point([i/25,dual(i/25)]).join(',')).join(' '))
const drag=createDragger(svg,view,(_,p)=>{multiplier.value=Math.max(0,Math.min(4,p[0]))},{step:0.05})
function chooseDimension(value){dimension.value=value;multiplier.value=0.5}
</script>

<template>
  <figure class="study-lab" aria-label="Infimum của Lagrangian và giá trị đối ngẫu của hàm bình phương">
    <figcaption class="lab-title">Nhân tử đổi cận dưới và đổi điểm cực tiểu của Lagrangian</figcaption>
    <p class="lab-lead">Cực tiểu hóa tổng bình phương tọa độ với tổng tọa độ ít nhất 1. Chọn một hoặc hai biến. Kéo chấm vàng trên đồ thị g(λ). Đường xanh nét đứt là giá trị tối ưu bài gốc.</p>
    <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Nhân tử lambda kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="36" x2="364" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="36" y2="314" class="lab-axis" />
      <line x1="36" x2="364" :y1="view.sy(primal)" :y2="view.sy(primal)" class="dual-primal" />
      <polyline :points="curve" class="dual-curve" />
      <circle :cx="view.sx(multiplier)" :cy="view.sy(dual(multiplier))" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(multiplier)" :cy="view.sy(dual(multiplier))" r="32" class="lab-handle dual-hit" tabindex="0" role="slider"
        aria-label="Nhân tử bất đẳng thức lambda" :aria-valuetext="fmt(multiplier,3)" aria-valuemin="0" aria-valuemax="4"
        @pointerdown="drag.start('lambda',$event)" @keydown="drag.key('lambda',[multiplier,dual(multiplier)],$event)" />
      <text x="15" y="25">g(λ)</text><text x="368" y="338">λ</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh λ bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="dimension===1" @click="chooseDimension(1)">Một biến</button>
      <button type="button" :aria-pressed="dimension===2" @click="chooseDimension(2)">Hai biến</button>
      <button type="button" @click="multiplier=2/dimension">Nhân tử tối ưu</button>
      <button type="button" @click="multiplier=0">Nhân tử bằng 0</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Có {{dimension}} biến. λ = {{fmt(multiplier,4)}}. Cực tiểu Lagrangian tại x(λ) = {{fmtPoint(minimizer,4)}}.</p>
      <p>g(λ) = {{fmt(dual(multiplier),4)}}, giá trị tối ưu bài gốc = {{fmt(primal,4)}}. Chênh lệch = {{fmt(primal-dual(multiplier),4)}}.</p>
      <p>Tổng tọa độ của x(λ) = {{fmt(dimension*multiplier/2,4)}}. {{dimension*multiplier/2<1-1e-10?'Điểm cực tiểu Lagrangian hiện tại chưa khả thi cho bài gốc.':'Điểm cực tiểu Lagrangian hiện tại thỏa tổng tọa độ ít nhất 1.'}}</p>
      <p>Phép lấy infimum theo x giữ cố định λ. Sau đó ta tối đa hóa g theo λ không âm để tìm cận dưới tốt nhất.</p>
    </div>
  </figure>
</template>

<style scoped>
.dual-curve { stroke: var(--tim); fill: none; stroke-width: 1.8; }
.dual-primal { stroke: var(--xanh); stroke-width: 1.5; stroke-dasharray: 5 4; }
.dual-hit { fill: transparent !important; stroke: transparent; }
.dual-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
