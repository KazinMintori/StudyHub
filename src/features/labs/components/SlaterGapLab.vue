<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt} from '../controllers/svg-drag.js'
const svg=ref(null),sequenceSvg=ref(null),u=ref(0),lambda=ref(1)
const view=ref(makeView({x0:-1,x1:1,y0:-.65,y1:1.4,width:400,height:340,pad:30})),P=p=>view.value.point(p)
const dragView=computed(()=>({...view.value,x0:-.8,x1:.8}))
const drag=createDragger(svg,dragView,(_,p)=>{u.value=p[0]},{step:.05,snap:.01})
const seqView=ref(makeView({x0:.5,x1:8.5,y0:-2,y1:4.5,width:400,height:340,pad:30})),Q=p=>seqView.value.point(p)
const L=r=>Math.exp(-r)+lambda.value/(r*r)-lambda.value*u.value
const limit=computed(()=>-lambda.value*u.value)
const seqDrag=createDragger(sequenceSvg,seqView,(_,p)=>{lambda.value=Math.max(0,Math.min(2,(p[1]-Math.exp(-1))/(1-u.value)))},{step:.05,snap:.01})
const curve=computed(()=>Array.from({length:141},(_,i)=>{const r=1+i*.05;return Q([r,L(r)]).join(',')}).join(' '))
</script>

<template>
 <figure class="study-lab" aria-label="Slater không thỏa, khoảng cách đối ngẫu và hàm giá trị không liên tục">
  <figcaption class="lab-title">Ngay tại u = 0, bài toán lồi có khe hở đối ngẫu bằng 1</figcaption>
  <p class="lab-lead">Cực tiểu e⁻ˢ trên miền t &gt; 0, với s²/t ≤ u. Kéo u ở hàng dưới hình đầu. Ở hình sau, kéo chấm tại r = 1 theo chiều dọc để đổi λ và xem Lagrangian tiến về cận nào.</p>
  <div class="lab-pair">
   <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Giá trị gốc p(u) bằng 0 với u dương, bằng 1 tại 0 và vô nghiệm với u âm" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <line :x1="view.sx(0)" :x2="view.sx(0)" y1="30" y2="310" class="lab-axis"/>
    <line :x1="view.sx(0)" :x2="view.sx(.9)" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-good"/>
    <circle :cx="P([0,1])[0]" :cy="P([0,1])[1]" r="7" class="lab-dot-accent"/><text :x="P([0,1])[0]+13" :y="P([0,1])[1]+6">p(0) = 1</text>
    <circle :cx="P([0,0])[0]" :cy="P([0,0])[1]" r="7" class="lab-dot-hollow"/><text x="235" :y="view.sy(0)-17">p(u) = 0</text>
    <text x="35" y="100">u &lt; 0</text><text x="35" y="126">Vô nghiệm</text>
    <line v-if="u>=0" :x1="P([u,-.4])[0]" :x2="P([u,-.4])[0]" :y1="view.sy(-.4)" :y2="view.sy(u===0?1:0)" class="lab-guide"/>
    <circle :cx="P([u,-.4])[0]" :cy="P([u,-.4])[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="P([u,-.4])[0]" :cy="P([u,-.4])[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Tham số ràng buộc u" :aria-valuetext="'u = '+fmt(u,3)" @pointerdown="drag.start('u',$event)" @keydown="drag.key('u',[u,0],$event)"/>
    <text x="12" y="23">Hàm giá trị gốc</text><text :x="view.sx(-.8)" y="334">−0.8</text><text :x="view.sx(0)-5" y="334">0</text><text :x="view.sx(.8)-8" y="334">0.8</text><text x="376" y="334">u</text>
   </svg>
   <svg ref="sequenceSvg" viewBox="0 0 400 340" role="group" aria-label="Giá trị Lagrangian dọc dãy s bằng r và t bằng r mũ bốn, nhân tử λ kéo được" @pointermove="seqDrag.move" @pointerup="seqDrag.end" @pointercancel="seqDrag.end" @lostpointercapture="seqDrag.end">
    <line x1="30" x2="370" :y1="seqView.sy(limit)" :y2="seqView.sy(limit)" class="lab-guide"/>
    <polyline :points="curve" class="lab-accent"/>
    <circle :cx="Q([1,L(1)])[0]" :cy="Q([1,L(1)])[1]" r="7" class="lab-dot-warn"/>
    <circle :cx="Q([1,L(1)])[0]" :cy="Q([1,L(1)])[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Nhân tử không âm λ của ràng buộc phân thức" :aria-valuetext="'λ = '+fmt(lambda,3)" @pointerdown="seqDrag.start('lambda',$event)" @keydown="seqDrag.key('lambda',[1,L(1)],$event)"/>
    <text x="12" y="23">L(r, r⁴, λ)</text><text x="200" :y="seqView.sy(limit)-13">gᵤ(λ) = −λu</text><text v-for="r in [1,4,8]" :key="r" :x="seqView.sx(r)-5" y="334">{{r}}</text><text x="380" y="334">r</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="x"/><LabPointControls :svg="sequenceSvg" axes="y"/></details>
  <div class="lab-buttons"><button type="button" @click="u=-.5">u = −0.5</button><button type="button" @click="u=0">u = 0</button><button type="button" @click="u=.5">u = 0.5</button></div>
  <div class="lab-readout" role="status">
   <p>u = {{fmt(u,3)}}. <template v-if="u<0">Miền khả thi rỗng, p(u) = +∞. Vì gᵤ(λ) = −λu tăng không giới hạn khi λ tăng, d(u) = +∞. Không gọi hiệu +∞ − +∞ là khoảng cách đối ngẫu.</template><template v-else-if="u===0">Tất cả điểm khả thi có s = 0 và t &gt; 0, nên p(0) = 1 được đạt. Nhưng g₀(λ) = 0 với mọi λ ≥ 0, nên d(0) = 0 và khe hở bằng 1. Không có nhân tử KKT hữu hạn.</template><template v-else>Slater thỏa. Giá trị p(u) = 0 nhưng không đạt, vì e⁻ˢ luôn dương. Đối ngẫu có d(u) = 0 đạt tại λ = 0.</template></p>
   <p>Với λ = {{fmt(lambda,3)}}, cận đối ngẫu gᵤ(λ) = {{fmt(limit,4)}}. Dãy r = 1, 2, 4, 8 cho L lần lượt {{[1,2,4,8].map(r=>fmt(L(r),5)).join(', ')}}. Cho r tăng vô hạn mới đạt giới hạn, không phải giá trị ở điểm cuối đồ thị.</p>
   <p>Dãy s = r, t = r⁴ thuộc miền t &gt; 0 và dùng để lấy infimum của Lagrangian. Nó không cần thỏa ràng buộc gốc. Đặc biệt tại u = 0, mọi điểm của dãy đều không khả thi cho bài toán gốc, nhưng hoàn toàn hợp lệ khi tính hàm đối ngẫu.</p>
   <p>Hình đầu đánh dấu giá trị tối ưu, không đánh dấu sự tồn tại nghiệm đạt giá trị đó. Chấm tại u = 0 không được nối xuống đoạn u &gt; 0 vì p có bước nhảy ở đây.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt u = 0 rồi đổi λ. Vì sao cận dưới vẫn bằng 0?</li><li>Chọn u dương rất nhỏ. Vì sao infimum đổi từ 1 xuống 0 mà nghiệm không được đạt?</li><li>Với u âm, vì sao phải xét λ lớn tùy ý thay vì kết luận từ khoảng kéo hữu hạn 0 ≤ λ ≤ 2?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
