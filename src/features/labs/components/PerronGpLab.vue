<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import MathMatrix from '../../../core/math/components/MathMatrix.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {perronCertificate} from '../services/foundation-geometry.mjs'
const svg=ref(null),certificateSvg=ref(null),t=ref(2),r=ref(1)
const row=computed(()=>perronCertificate(t.value,r.value))
const view=ref(makeView({x0:0,x1:4.5,y0:.2,y1:1.5,width:400,height:340,pad:30})),P=p=>view.value.point(p)
const designView=computed(()=>({...view.value,x0:.25,x1:4}))
const drag=createDragger(svg,designView,(_,p)=>{t.value=p[0]},{step:.05,snap:.01})
const certificateView=ref(makeView({x0:0,x1:4.5,y0:.2,y1:2.2,width:400,height:340,pad:30})),Q=p=>certificateView.value.point(p)
const ratioView=computed(()=>({...certificateView.value,x0:.25,x1:4}))
const ratioDrag=createDragger(certificateSvg,ratioView,(_,p)=>{r.value=p[0]},{step:.05,snap:.01})
const grid=Array.from({length:151},(_,i)=>.25+i*.025)
const designCurve=grid.map(t=>P([t,perronCertificate(t,t).radius]).join(',')).join(' ')
const ratioCurves=computed(()=>[0,1,2].map(index=>grid.map(r=>{
 const model=perronCertificate(t.value,r)
 return Q([r,index===2?model.upper:model.ratios[index]]).join(',')
}).join(' ')))
</script>

<template>
 <figure class="study-lab" aria-label="Bán kính phổ của ma trận dương và chứng nhận GP bằng vector dương">
  <figcaption class="lab-title">Thiết kế ma trận và tìm vector chứng nhận là hai việc khác nhau</figcaption>
  <p class="lab-lead">A(t) = ¼[[t, 1], [1, 1/t]], với t &gt; 0. Kéo t ở hình đầu để đổi thiết kế. Kéo r ở hình sau để đổi vector chứng nhận v = (r, 1). Cận tốt nhất đạt khi r = t.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Bán kính phổ theo thiết kế t, điểm t kéo được và cực tiểu tại 1" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <line v-for="value in [.5,1]" :key="value" x1="30" x2="370" :y1="view.sy(value)" :y2="view.sy(value)" class="lab-guide"/>
    <polyline :points="designCurve" class="lab-accent"/>
    <circle :cx="view.sx(1)" :cy="view.sy(.5)" r="6" class="lab-dot-hollow"/>
    <circle :cx="view.sx(t)" :cy="view.sy(row.radius)" r="7" class="lab-dot-warn"/>
    <circle :cx="view.sx(t)" :cy="view.sy(row.radius)" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Thiết kế ma trận t" :aria-valuetext="`t = ${fmt(t,3)}, ρ = ${fmt(row.radius,4)}`" @pointerdown="drag.start('t',$event)" @keydown="drag.key('t',[t,0],$event)"/>
    <text x="12" y="23">Bán kính phổ ρ(A(t))</text><text x="2" :y="view.sy(.5)+6">0.5</text><text x="12" :y="view.sy(1)+6">1</text><text v-for="x in [1,2,3,4]" :key="x" :x="view.sx(x)-5" y="333">{{x}}</text><text x="375" y="333">t</text>
   </svg>
   <svg ref="certificateSvg" viewBox="0 0 400 340" role="group" aria-label="Hai tỉ số thành phần Av chia v, giá trị lớn nhất và r kéo được" @pointermove="ratioDrag.move" @pointerup="ratioDrag.end" @pointercancel="ratioDrag.end" @lostpointercapture="ratioDrag.end">
    <polyline v-for="(curve,i) in ratioCurves" :key="i" :points="curve" :class="i===2?'lab-accent':i===0?'lab-line':'lab-warn'"/>
    <line x1="30" x2="370" :y1="certificateView.sy(row.radius)" :y2="certificateView.sy(row.radius)" class="lab-good"/>
    <circle :cx="certificateView.sx(t)" :cy="certificateView.sy(row.radius)" r="6" class="lab-dot-hollow"/>
    <circle :cx="certificateView.sx(r)" :cy="certificateView.sy(row.upper)" r="7" class="lab-dot-warn"/>
    <circle :cx="certificateView.sx(r)" :cy="certificateView.sy(row.upper)" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Tỉ số r của vector chứng nhận v" :aria-valuetext="`r = ${fmt(r,3)}, λ = ${fmt(row.upper,4)}`" @pointerdown="ratioDrag.start('r',$event)" @keydown="ratioDrag.key('r',[r,0],$event)"/>
    <text x="12" y="23">λ(v) = maxᵢ (Av)ᵢ/vᵢ</text><text v-for="x in [1,2,3,4]" :key="x" :x="certificateView.sx(x)-5" y="333">{{x}}</text><text x="375" y="333">r</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="x"/><LabPointControls :svg="certificateSvg" axes="x"/></details>
  <p class="lab-legend"><span class="legend-accent">Giá trị cần cực tiểu</span><span class="legend-good">Bán kính phổ thật trong hình chứng nhận</span><span>Đường mảnh và đường vàng: Hai tỉ số thành phần</span></p>
  <div class="lab-buttons"><button type="button" @click="t=2;r=1">t = 2, v = (1, 1)</button><button type="button" @click="r=t">Chọn vector Perron</button><button type="button" @click="t=1;r=1">Thiết kế tối ưu</button><button type="button" @click="t=4;r=4">Một thiết kế có ρ &gt; 1</button></div>
  <div class="lab-readout" role="status">
   <MathMatrix :rows="row.matrix.map(row=>row.map(value=>Number(value.toFixed(4))))" label="Ma trận A của thiết kế đang chọn"/>
   <p>v = {{fmtPoint(row.vector,3)}}, Av = {{fmtPoint(row.image,4)}}. Hai tỉ số (Av)ᵢ/vᵢ bằng {{fmtPoint(row.ratios,4)}}. Chọn λ bằng giá trị lớn hơn, ta có Av ≤ λv.</p>
   <p>λ = {{fmt(row.upper,5)}} là cận trên của ρ(A) = {{fmt(row.radius,5)}}. Độ lệch chứng nhận bằng {{fmt(row.gap,5)}}. Thay r chỉ cải thiện chứng nhận của cùng A, không làm đổi bán kính phổ thật.</p>
   <p>{{row.radius<1?'Vì ρ < 1, các trạng thái của hệ zₖ₊₁ = Azₖ tiến về 0.':Math.abs(row.radius-1)<1e-9?'Vì ρ = 1, hệ ở ngưỡng giữa suy giảm và tăng trưởng; không suy ra mọi trạng thái đều về 0.':'Vì ρ > 1, trạng thái dương tăng theo hướng Perron về lâu dài.'}} Đây là kết luận tiệm cận, không có nghĩa từng tọa độ giảm ở mọi bước.</p>
   <p>Họ ma trận này có hạng một, nên ρ tính được bằng (t + 1/t)/4. Không dùng quy tắc trace đó cho ma trận tổng quát. Hình chỉ vẽ t và r từ 0.25 tới 4, còn bài toán xét mọi giá trị dương.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Giữ t = 2 rồi kéo r tới 2. Vì sao cận từ 0.75 hạ xuống đúng 0.625?</li><li>Đặt t = 1. Vì sao đây là thiết kế tốt nhất ngay cả khi cho phép t ngoài khung vẽ?</li><li>Đặt t = 4. Chứng nhận đã khít có đồng nghĩa ma trận ổn định không?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
