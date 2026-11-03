<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,makeView} from '../controllers/svg-drag.js'
import {clipPolyline} from '../services/svg-clipping.mjs'

const svg=ref(null),gain=ref(1),rule=ref('glorot'),relu=ref(true),alternating=ref(false)
const view=ref(makeView({x0:0.1,x1:2.7,y0:-1,y1:1,width:400,height:110,pad:36}))
const bounds={x0:-0.5,x1:12.6,y0:-14,y1:14}
const plot=makeView({...bounds,width:400,height:330,pad:36})
const rows=computed(()=>{
  const values=[{layer:0,q:1}]
  for(let layer=1;layer<=12;layer++){
    const nin=alternating.value&&layer%2===0?4:8
    const nout=alternating.value&&layer%2===1?4:8
    const variance=rule.value==='glorot'?2/(nin+nout):rule.value==='he'?2/nin:gain.value/nin
    const activation=relu.value?0.5:1
    values.push({layer,nin,nout,variance,forward:activation*nin*variance,backward:activation*nout*variance,q:values.at(-1).q*activation*nin*variance})
  }
  return values
})
const coordinates=points=>points.map(p=>plot.point(p).join(',')).join(' ')
const curves=computed(()=>clipPolyline(rows.value.map(r=>[r.layer,Math.log2(r.q)]),bounds).map(coordinates))
const currentGain=computed(()=>rows.value[1].nin*rows.value[1].variance)
const handle=computed(()=>[currentGain.value,0])
const drag=createDragger(svg,view,(_,p)=>{gain.value=Math.max(0.25,Math.min(2.5,p[0]));rule.value='custom'},{step:0.05})
const valueText=value=>value<0.0001||value>10000?value.toExponential(3):fmt(value,4)
</script>

<template>
  <figure class="study-lab" aria-label="Mômen bậc hai của tín hiệu qua các tầng với Glorot và He">
    <figcaption class="lab-title">Theo dõi năng lượng tín hiệu thay vì đồng nhất nó với phương sai</figcaption>
    <p class="lab-lead">Mô hình khởi tạo giả định trọng số có trung bình 0, độc lập với đầu vào và các tích chéo có kỳ vọng 0. Với ReLU, tiền kích hoạt đối xứng. Kéo điểm vàng để đổi γ = nᵢₙ Var(W). Đường dưới biểu diễn log₂ của mômen bậc hai tương đối qua 12 tầng.</p>
    <svg ref="svg" viewBox="0 0 400 110" role="group" aria-label="Kéo hệ số phương sai khởi tạo gamma"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line :x1="view.sx(0.25)" :x2="view.sx(2.5)" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <text x="36" y="21">γ = 0,25</text><text x="294" y="21">γ = 2,5</text>
      <circle :cx="view.sx(currentGain)" :cy="view.sy(0)" r="7" class="lab-dot-warn" />
      <circle :cx="view.sx(currentGain)" :cy="view.sy(0)" r="32" class="lab-handle init-hit" tabindex="0" role="slider"
        aria-label="Hệ số gamma của khởi tạo" :aria-valuetext="fmt(currentGain,3)" aria-valuemin="0.25" aria-valuemax="2.5"
        @pointerdown="drag.start('gain',$event)" @keydown="drag.key('gain',handle,$event)" />
    </svg>
    <svg viewBox="0 0 400 330" role="img" aria-label="Logarit cơ số hai của mômen bậc hai tương đối qua các tầng">
      <line x1="36" x2="364" :y1="plot.sy(0)" :y2="plot.sy(0)" class="init-reference" />
      <line :x1="plot.sx(0)" :x2="plot.sx(0)" y1="36" y2="294" class="lab-axis" />
      <polyline v-for="(curve,i) in curves" :key="i" :points="curve" class="init-flow" />
      <text x="36" y="24">log₂(q / q₀)</text>
      <text x="14" :y="plot.sy(12)+6">12</text><text x="18" :y="plot.sy(0)+6">0</text><text x="7" :y="plot.sy(-12)+6">−12</text>
      <text :x="plot.sx(0)-5" y="317">0</text><text :x="plot.sx(12)-9" y="317">12</text><text x="164" y="317">Tầng</text>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh γ bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="rule==='glorot'" @click="rule='glorot'">Glorot</button>
      <button type="button" :aria-pressed="rule==='he'" @click="rule='he'">He</button>
      <button type="button" :aria-pressed="!relu" @click="relu=false">Tuyến tính</button>
      <button type="button" :aria-pressed="relu" @click="relu=true">ReLU</button>
      <button type="button" :aria-pressed="!alternating" @click="alternating=false">Các tầng rộng 8</button>
      <button type="button" :aria-pressed="alternating" @click="alternating=true">Xen kẽ 8 và 4</button>
    </div>
    <div class="lab-readout" role="status">
      <p>{{rule==='custom'?'Quy tắc tự chọn γ cố định':rule==='glorot'?'Glorot: Var(W) = 2 / (nᵢₙ + nₒᵤₜ)':'He: Var(W) = 2 / nᵢₙ'}}. Tầng đầu có {{rows[1].nin}} đầu vào, {{rows[1].nout}} đầu ra, γ = {{fmt(currentGain,4)}}.</p>
      <p>Hệ số truyền mômen bậc hai ở tầng đầu: Xuôi {{fmt(rows[1].forward,4)}}, ngược {{fmt(rows[1].backward,4)}}. Công thức ngược dùng thêm xấp xỉ độc lập của gradient và trọng số.</p>
      <p>Sau 12 tầng, q₁₂ / q₀ = {{valueText(rows[12].q)}}. {{Math.abs(Math.log2(rows[12].q))>14?'Giá trị cuối nằm ngoài miền dọc của đồ thị.':''}}</p>
      <p>q là kỳ vọng bình phương tín hiệu, không phải phương sai đầu ra ReLU. Đây là mô hình tại khởi tạo, không chứng nhận rằng mạng đã huấn luyện sẽ giữ nguyên các hệ số này.</p>
    </div>
  </figure>
</template>

<style scoped>
.init-reference { stroke: var(--ink-3); stroke-dasharray: 4 4; stroke-width: 1.3; }
.init-flow { stroke: var(--tim); fill: none; stroke-width: 1.7; }
.init-hit { fill: transparent !important; stroke: transparent; }
.init-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
