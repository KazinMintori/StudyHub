<script setup>
import { computed,ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger,makeView,fmt } from '../controllers/svg-drag.js'
import { standardNormalCdf } from '../services/foundation-geometry.mjs'
const svg=ref(null),amount=ref(5),threshold=ref(10),eta=ref(.95)
const quantiles={'.5':0,'.9':1.2815515655446004,'.95':1.6448536269514722,'.99':2.3263478740408408}
const q=computed(()=>quantiles[String(eta.value).replace(/^0/,'')])
const mean=computed(()=>2*amount.value),sigma=computed(()=>.3*amount.value)
const probability=computed(()=>amount.value===0?(threshold.value>=0?1:0):standardNormalCdf((threshold.value-mean.value)/sigma.value))
const required=computed(()=>mean.value+q.value*sigma.value)
const maximum=computed(()=>threshold.value/(2+.3*q.value))
const view=ref(makeView({x0:-2,x1:22,y0:-.3,y1:1.25,width:440,height:330,pad:30})),P=p=>view.value.point(p)
const drag=createDragger(svg,view,(name,p)=>{
 if(name==='mean')amount.value=Math.max(0,Math.min(7,p[0]/2))
 else threshold.value=Math.max(0,Math.min(14,p[0]))
},{step:.1,snap:.01})
const density=y=>sigma.value>0?Math.exp(-.5*((y-mean.value)/sigma.value)**2):0
const grid=Array.from({length:481},(_,i)=>-2+i/20)
const curve=computed(()=>grid.map(y=>P([y,density(y)]).join(',')).join(' '))
const tail=computed(()=>{
 const ys=[threshold.value,...grid.filter(y=>y>threshold.value)]
 return [P([threshold.value,0]),...ys.map(y=>P([y,density(y)])),P([22,0])].map(p=>p.join(',')).join(' ')
})
</script>

<template>
 <figure class="study-lab" aria-label="Ràng buộc xác suất Gaussian và xác suất vượt ngưỡng">
  <figcaption class="lab-title">Đạt yêu cầu ở trung bình chưa đủ để xác suất vi phạm nhỏ</figcaption>
  <p class="lab-lead">Hệ số a có trung bình 2 và độ lệch chuẩn 0.3. Tổng Y = ax có trung bình 2x và độ lệch chuẩn 0.3x. Kéo chấm ở đỉnh đường cong để đổi x, kéo chấm dưới trục để đổi ngưỡng b.</p>
  <svg ref="svg" viewBox="0 0 440 330" role="group" aria-label="Phân phối của Y, trung bình kéo được và ngưỡng b kéo được, vùng vi phạm nằm bên phải b" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line x1="30" x2="410" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis"/>
   <template v-if="amount>0">
    <polygon :points="tail" class="lab-bad-fill" opacity=".45"/>
    <polyline :points="curve" class="lab-line"/>
    <line :x1="view.sx(mean)" :x2="view.sx(mean)" :y1="view.sy(0)" :y2="view.sy(1)" class="lab-guide"/>
   </template>
   <line v-else :x1="view.sx(0)" :x2="view.sx(0)" :y1="view.sy(0)" :y2="view.sy(1)" class="lab-accent"/>
   <line :x1="view.sx(threshold)" :x2="view.sx(threshold)" :y1="view.sy(0)" :y2="view.sy(1.1)" class="lab-bad"/>
   <line :x1="view.sx(required)" :x2="view.sx(required)" :y1="view.sy(0)" :y2="view.sy(.45)" class="lab-good"/>
   <text x="12" y="23">Phân phối của Y = ax</text><text x="390" :y="view.sy(0)+22">Y</text>
   <text v-for="value in [0,5,10,15,20]" :key="value" :x="view.sx(value)-5" :y="view.sy(0)+21">{{value}}</text>
   <circle :cx="view.sx(mean)" :cy="view.sy(1)" r="7" class="lab-dot-accent"/>
   <text :x="view.sx(mean)+12" :y="view.sy(1)-12">μ = 2x</text>
   <circle :cx="view.sx(mean)" :cy="view.sy(1)" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Lượng nguyên liệu x, kéo trung bình μ" :aria-valuetext="'x = '+fmt(amount,3)" @pointerdown="drag.start('mean',$event)" @keydown="drag.key('mean',[mean,0],$event)"/>
   <circle :cx="view.sx(threshold)" :cy="view.sy(0)+43" r="7" class="lab-dot-bad"/><text :x="view.sx(threshold)+12" :y="view.sy(0)+50">b</text>
   <circle :cx="view.sx(threshold)" :cy="view.sy(0)+43" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Ngưỡng tài nguyên b" :aria-valuetext="'b = '+fmt(threshold,3)" @pointerdown="drag.start('threshold',$event)" @keydown="drag.key('threshold',[threshold,0],$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="x"/></details>
  <p class="lab-legend"><span class="legend-bad">Vùng Y &gt; b</span><span class="legend-good">Phân vị μ + qησ</span><span class="legend-accent">Trung bình μ</span></p>
  <div class="lab-controls"><label>Xác suất đạt yêu cầu η<select v-model.number="eta"><option :value=".5">50%</option><option :value=".9">90%</option><option :value=".95">95%</option><option :value=".99">99%</option></select></label></div>
  <div class="lab-buttons"><button type="button" @click="amount=5;threshold=10">x = 5, b = 10</button><button type="button" @click="amount=maximum">Đưa về cận xác suất</button><button type="button" @click="amount=0">x = 0</button></div>
  <div class="lab-readout" role="status">
   <p>x = {{fmt(amount,3)}}, b = {{fmt(threshold,3)}}. μ = {{fmt(mean,3)}}, σ = {{fmt(sigma,3)}}. Xác suất thỏa xấp xỉ {{fmt(100*probability,2)}}%, xác suất vi phạm xấp xỉ {{fmt(100*(1-probability),2)}}%.</p>
   <p>qη = {{fmt(q,6)}}. Phân vị yêu cầu bằng μ + qησ = {{fmt(required,4)}}. {{required<=threshold+1e-9?'Ràng buộc xác suất được thỏa.':'Ràng buộc xác suất bị vi phạm.'}} Lượng lớn nhất cho mức η đang chọn là x ≈ {{fmt(maximum,5)}}.</p>
   <p v-if="amount===0">Khi x = 0, Y luôn bằng 0. Đây là một khối xác suất tại 0, không phải đường mật độ Gaussian có độ rộng dương. Với b ≥ 0, xác suất thỏa bằng 1.</p>
   <p v-else>Đường cong được đổi thang dọc để vừa khung, còn chiều ngang giữ nguyên đơn vị của Y. Xác suất được tính từ hàm phân phối Gaussian, không đếm điểm ảnh hoặc lấy mẫu Monte Carlo. Phần đuôi ngoài khung vẫn được tính trong số đọc.</p>
   <p>Đây là một ràng buộc riêng lẻ dưới giả thiết a thực sự có phân phối Gaussian. Nó không bảo đảm mọi kịch bản, vì phân phối Gaussian có đuôi không bị chặn.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt x = 5 và b = 10. Vì sao một nửa phân phối nằm ở phía vi phạm?</li><li>Chọn 95% rồi đưa về cận. Nới yêu cầu lên 99% làm lượng cho phép tăng hay giảm?</li><li>Kéo b mà giữ x. Vì sao đường cong không đổi, nhưng phần vi phạm thay đổi?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
</style>
