<script setup>
import { computed,ref,useId } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { makeView,createDragger,fmt,fmtPoint } from '../controllers/svg-drag.js'
import { polyhedronInBox } from '../services/convex-geometry.mjs'
import { trigonometricSlabWorst } from '../services/foundation-geometry.mjs'
const svg=ref(null),plotSvg=ref(null),point=ref([.5,.5]),count=ref(4),selectedT=ref(.3)
const tMax=Math.PI/3,clipId='slab-'+useId()
const view=ref(makeView({x0:-2.2,x1:2.2,y0:-2.2,y1:2.2,width:360,height:360,pad:24})),P=p=>view.value.point(p)
const drag=createDragger(svg,view,(_,p)=>{point.value=p},{step:.05,snap:.025})
const coefficient=t=>[Math.cos(t),Math.cos(2*t)]
const value=(t,x=point.value)=>x[0]*Math.cos(t)+x[1]*Math.cos(2*t)
const worst=computed(()=>trigonometricSlabWorst(point.value))
const inside=computed(()=>Math.abs(worst.value.value)<=1+1e-9)
const times=computed(()=>Array.from({length:count.value},(_,i)=>count.value===1?0:i*tMax/(count.value-1)))
const region=computed(()=>polyhedronInBox(times.value.flatMap(t=>{const a=coefficient(t);return [{a,b:1},{a:a.map(v=>-v),b:1}]}),[-2.2,2.2,-2.2,2.2]))
const exactBoundary=Array.from({length:181},(_,i)=>{const t=i*Math.PI/90,x=[Math.cos(t),Math.sin(t)],maximum=Math.abs(trigonometricSlabWorst(x).value);return x.map(v=>v/maximum)})
function boundaries(t){const [a,b]=coefficient(t),n=a*a+b*b;return [-1,1].map(sign=>[[-8,8].map(s=>[sign*a/n-s*b,sign*b/n+s*a])]).flat()}
const selectedSatisfied=computed(()=>Math.abs(value(selectedT.value))<=1+1e-9)
const plotView=computed(()=>{const max=Math.max(1.35,Math.abs(worst.value.value)*1.18);return makeView({x0:-tMax,x1:tMax,y0:-max,y1:max,width:360,height:300,pad:30})})
const plotDrag=createDragger(plotSvg,plotView,(_,p)=>{selectedT.value=p[0]},{step:.025,snap:.005})
const curve=computed(()=>Array.from({length:161},(_,i)=>{const t=-tMax+2*tMax*i/160;return plotView.value.point([t,value(t)]).join(',')}).join(' '))
</script>

<template>
 <figure class="study-lab" aria-label="Giao các dải ràng buộc của một đa thức lượng giác">
  <figcaption class="lab-title">Kéo hệ số x để đổi đa thức, kéo t để chọn một ràng buộc</figcaption>
  <p class="lab-lead">Ở ví dụ hai hệ số, pₓ(t) = x₁cos t + x₂cos 2t. Điểm x thuộc S khi |pₓ(t)| ≤ 1 với mọi |t| ≤ π/3. Hình hệ số và đồ thị đa thức được đặt riêng để đọc rõ trên điện thoại.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 360 360" role="group" aria-label="Không gian hai hệ số x, các dải song song và điểm x kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <defs><clipPath :id="clipId"><rect x="24" y="24" width="312" height="312"/></clipPath></defs>
    <line x1="24" y1="180" x2="336" y2="180" class="lab-axis"/><line x1="180" y1="24" x2="180" y2="336" class="lab-axis"/>
    <g :clip-path="'url(#'+clipId+')'">
     <polygon :points="region.map(p=>P(p).join(',')).join(' ')" class="lab-region-soft"/>
     <polygon :points="exactBoundary.map(p=>P(p).join(',')).join(' ')" class="lab-region"/>
     <g v-for="t in times" :key="t"><line v-for="(line,i) in boundaries(t)" :key="i" :x1="P(line[0])[0]" :y1="P(line[0])[1]" :x2="P(line[1])[0]" :y2="P(line[1])[1]" class="lab-guide"/></g>
     <line v-for="(line,i) in boundaries(selectedT)" :key="'s'+i" :x1="P(line[0])[0]" :y1="P(line[0])[1]" :x2="P(line[1])[0]" :y2="P(line[1])[1]" :class="selectedSatisfied?'lab-good':'lab-bad'"/>
    </g>
    <text x="304" y="203">x₁</text><text x="190" y="42">x₂</text>
    <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" :class="inside?'lab-dot-accent':'lab-dot-bad'" pointer-events="none"/>
    <circle :cx="P(point)[0]" :cy="P(point)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Hai hệ số x₁, x₂" :aria-valuetext="fmtPoint(point)" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',point,$event)"/>
   </svg>
   <svg ref="plotSvg" viewBox="0 0 360 300" role="group" aria-label="Đồ thị pₓ(t), hai mức cộng trừ 1 và giá trị t kéo được" @pointermove="plotDrag.move" @pointerup="plotDrag.end" @pointercancel="plotDrag.end" @lostpointercapture="plotDrag.end">
    <rect x="30" :y="plotView.sy(1)" width="300" :height="plotView.sy(-1)-plotView.sy(1)" class="lab-region-soft"/>
    <line x1="30" x2="330" :y1="plotView.sy(0)" :y2="plotView.sy(0)" class="lab-axis"/>
    <line v-for="level in [-1,1]" :key="level" x1="30" x2="330" :y1="plotView.sy(level)" :y2="plotView.sy(level)" class="lab-guide"/>
    <polyline :points="curve" class="lab-line"/>
    <text x="8" :y="plotView.sy(1)+5">1</text><text x="5" :y="plotView.sy(-1)+5">−1</text><text x="30" y="24">pₓ(t)</text><text x="24" y="292">−π/3</text><text x="306" y="292">π/3</text><text x="175" y="292">t</text>
    <circle :cx="plotView.sx(worst.t)" :cy="plotView.sy(worst.value)" r="5" class="lab-dot-warn"/>
    <circle :cx="plotView.sx(selectedT)" :cy="plotView.sy(value(selectedT))" r="7" :class="selectedSatisfied?'lab-dot-accent':'lab-dot-bad'" pointer-events="none"/>
    <circle :cx="plotView.sx(selectedT)" :cy="plotView.sy(value(selectedT))" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Giá trị t đang chọn trên đồ thị" :aria-valuetext="'t = '+fmt(selectedT,3)" @pointerdown="plotDrag.start('t',$event)" @keydown="plotDrag.key('t',[selectedT,0],$event)"/>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/><LabPointControls :svg="plotSvg" axes="x"/></details>
  <p class="lab-legend"><span class="legend-accent">Tập S</span><span class="legend-guide">Các dải xấp xỉ hữu hạn</span><span class="legend-good">Dải t đang thử nếu đạt</span><span class="legend-warn">Cực đại của |pₓ|</span></p>
  <div class="lab-controls"><label>Số dải dùng để xấp xỉ: {{count}}<input v-model.number="count" type="range" min="1" max="20" step="1"/></label></div>
  <div class="lab-readout" role="status">
   <p>x = {{fmtPoint(point)}}. Tại t = {{fmt(selectedT,3)}}, pₓ(t) = {{fmt(value(selectedT),4)}}. {{selectedSatisfied?'Ràng buộc tại riêng t này được thỏa.':'Ràng buộc tại t này bị vi phạm.'}}</p>
   <p>Giá trị lớn nhất của |pₓ(t)| trên cả đoạn bằng {{fmt(Math.abs(worst.value),4)}}, đạt tại t ≈ ±{{fmt(worst.t,4)}}. {{inside?'x thuộc S.':'x không thuộc S.'}}</p>
   <p>Phần giao của {{count}} dải là xấp xỉ S từ bên ngoài. Chỉ thỏa các dải hữu hạn chưa đủ để kết luận thuộc S. Kiểm tra ở trên dùng cực trị giải tích sau phép đổi u = cos t, không suy từ một lưới mẫu.</p>
   <p>Đa thức chẵn nên hai phía t và −t có cùng giá trị. Đường biên S được vẽ bằng các đoạn nhỏ nối những điểm biên tính được, còn quyết định thuộc tập dùng phép tính cực trị.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Kéo x ra ngoài S rồi tìm t làm |pₓ(t)| lớn hơn 1. Chỉ một t vi phạm đã đủ để bác bỏ.</li><li>Giữ x rồi kéo t. Vì sao dải ràng buộc trong hình hệ số thay đổi hướng?</li><li>Giảm số dải xuống 1. Vì sao phần giao có thể lớn hơn S rất nhiều?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
