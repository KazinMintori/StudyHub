<script setup>
import { computed,ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { makeView,createDragger,fmt } from '../controllers/svg-drag.js'
import { minimaxRatio,minimaxRatioLevel } from '../services/foundation-geometry.mjs'
const svg=ref(null),s=ref(.75),tau=ref(1),lower=ref(.5),upper=ref(1.5),history=ref([])
const view=ref(makeView({x0:-.08,x1:1.2,y0:.3,y1:3.2,width:440,height:360,pad:30})),P=p=>view.value.point(p)
const row=computed(()=>minimaxRatio(s.value)),level=computed(()=>minimaxRatioLevel(tau.value))
const drag=createDragger(svg,view,(name,p)=>{
 if(name==='level')tau.value=Math.max(.5,Math.min(1.5,p[1]))
 else s.value=Math.max(0,Math.min(1,p[0]))
},{step:.01,snap:.001})
const curves=['first','second','value'].map(key=>({key,points:Array.from({length:201},(_,i)=>{const v=i/200;return P([v,minimaxRatio(v)[key]]).join(',')}).join(' ')}))
const exactS=(Math.sqrt(6)-1)/2,exactValue=2*Math.sqrt(6)-4
function next(){
 if(history.value.length>=12)return
 const trial=(lower.value+upper.value)/2,result=minimaxRatioLevel(trial)
 tau.value=trial
 if(result.feasible){upper.value=trial;s.value=(result.lower+result.upper)/2}
 else lower.value=trial
 history.value.push({...result,tau:trial,lo:lower.value,hi:upper.value})
}
function reset(){lower.value=.5;upper.value=1.5;tau.value=1;s.value=.75;history.value=[]}
</script>

<template>
 <figure class="study-lab" aria-label="Minimax hai tỉ số và thuật toán chia đôi qua kiểm tra khả thi">
  <figcaption class="lab-title">Hạ mức τ cho tới khi khoảng khả thi vừa biến mất</figcaption>
  <p class="lab-lead">Điểm quyết định là x = (s, 1 − s), 0 ≤ s ≤ 1. Hai đường mảnh là hai tỉ số, đường đậm là giá trị lớn hơn H(s). Kéo điểm s trên đường đậm và kéo τ ở mép phải để thử một mức.</p>
  <svg ref="svg" viewBox="0 0 440 360" role="group" aria-label="Hai hàm phân tuyến tính, hàm cực đại, điểm s và mức τ kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <rect v-if="level.feasible" :x="view.sx(level.lower)" y="30" :width="Math.max(0,view.sx(level.upper)-view.sx(level.lower))" height="300" class="lab-region-soft"/>
   <line :x1="view.sx(0)" :x2="view.sx(1)" :y1="view.sy(.4)" :y2="view.sy(.4)" class="lab-axis"/>
   <polyline v-for="curve in curves" :key="curve.key" :points="curve.points" :class="curve.key==='value'?'lab-accent':curve.key==='first'?'lab-line':'lab-warn'"/>
   <line :x1="view.sx(0)" :x2="view.sx(1.1)" :y1="view.sy(tau)" :y2="view.sy(tau)" class="lab-good"/>
   <circle :cx="view.sx(s)" :cy="view.sy(row.value)" r="7" class="lab-dot-accent"/>
   <circle :cx="view.sx(s)" :cy="view.sy(row.value)" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Tham số quyết định s" :aria-valuetext="`s = ${fmt(s,3)}, H = ${fmt(row.value,4)}`" @pointerdown="drag.start('s',$event)" @keydown="drag.key('s',[s,0],$event)"/>
   <circle :cx="view.sx(1.1)" :cy="view.sy(tau)" r="7" class="lab-dot-warn"/><text :x="view.sx(1.1)-7" :y="view.sy(tau)-18">τ</text>
   <circle :cx="view.sx(1.1)" :cy="view.sy(tau)" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Mức τ để kiểm tra khả thi" :aria-valuetext="'τ = '+fmt(tau,4)" @pointerdown="drag.start('level',$event)" @keydown="drag.key('level',[1.1,tau],$event)"/>
   <text x="12" y="23">Giá trị các tỉ số</text><text :x="view.sx(0)-5" y="352">0</text><text :x="view.sx(1)-5" y="352">1</text><text x="390" y="352">s</text>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <p class="lab-legend"><span class="legend-accent">H(s)</span><span>Đường mảnh: Tỉ số thứ nhất</span><span class="legend-warn">Tỉ số thứ hai</span><span class="legend-good">Mức τ, vùng tô là khoảng khả thi</span></p>
  <div class="lab-buttons"><button type="button" :disabled="history.length>=12" @click="next">Chia đôi bước tiếp</button><button type="button" @click="reset">Bắt đầu lại</button><button type="button" @click="s=exactS;tau=exactValue">Xem điểm tối ưu chính xác</button></div>
  <div class="lab-readout" role="status">
   <p>s = {{fmt(s,4)}}, hai tỉ số bằng {{fmt(row.first,4)}} và {{fmt(row.second,4)}}. H(s) = {{fmt(row.value,4)}}. {{row.value<=tau+1e-12?'Điểm đang chọn đạt mức τ.':'Điểm đang chọn chưa đạt mức τ.'}}</p>
   <p>Tại τ = {{fmt(tau,5)}}, đầu mút dưới L = {{fmt(level.lower,5)}}, đầu mút trên U = {{fmt(level.upper,5)}}. {{level.feasible?'L ≤ U nên có quyết định đạt mức này.':'L > U nên khoảng rỗng, mức này không khả thi.'}}</p>
   <p>Sau {{history.length}} bước chia đôi, giá trị tối ưu bị kẹp trong [{{fmt(lower,6)}}, {{fmt(upper,6)}}], độ dài {{fmt(upper-lower,6)}}. Kéo τ bằng tay chỉ thử một mức, không tự đổi khoảng kẹp.</p>
   <p>Tối ưu chính xác có s* = (√6 − 1)/2 ≈ {{fmt(exactS,6)}}, H* = 2√6 − 4 ≈ {{fmt(exactValue,6)}}. Chia đôi dùng phép thử khoảng khả thi, không dùng công thức tối ưu này để chọn nhánh.</p>
  </div>
  <ol v-if="history.length" class="lab-iterations"><li v-for="(step,i) in history" :key="i">Bước {{i+1}}: τ = {{fmt(step.tau,6)}}. L = {{fmt(step.lower,6)}}, U = {{fmt(step.upper,6)}}. {{step.feasible?'Khả thi, hạ cận trên.':'Vô nghiệm, nâng cận dưới.'}} Khoảng mới [{{fmt(step.lo,6)}}, {{fmt(step.hi,6)}}].</li></ol>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Giảm τ xuống 0.75. Vì sao khoảng rỗng dù từng tỉ số riêng đều có thể nhỏ hơn 0.75?</li><li>Thực hiện bốn bước chia đôi. Khoảng còn dài bao nhiêu?</li><li>Thực hiện sáu bước. Vì sao khoảng không quá 1/64 mà chưa cần biết nghiệm chính xác?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-iterations{font-size:var(--fs-ui)}
.lab-iterations li+li{margin-top:var(--space-2)}
</style>
