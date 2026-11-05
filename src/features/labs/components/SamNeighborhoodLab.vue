<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,makeView} from '../controllers/svg-drag.js'
import {clipPolyline} from '../services/svg-clipping.mjs'

const svg=ref(null),theta=ref(.7),rho=ref(.5),curvature=ref(1)
const bounds={x0:-2.2,x1:2.2,y0:-.7,y1:20}
const view=ref(makeView({...bounds,width:400,height:350,pad:36}))
const loss=x=>curvature.value*x*x/2
const gradient=computed(()=>curvature.value*theta.value)
const approximation=computed(()=>Math.abs(gradient.value)>1e-12?rho.value*Math.sign(gradient.value):0)
const worst=computed(()=>theta.value+(theta.value<0?-rho.value:rho.value))
const P=p=>view.value.point(p)
const thetaPoint=computed(()=>[theta.value,loss(theta.value)])
const curve=computed(()=>clipPolyline(Array.from({length:141},(_,i)=>{const x=-2.2+i*4.4/140;return[x,loss(x)]}),bounds).map(segment=>segment.map(p=>P(p).join(',')).join(' ')))
const drag=createDragger(svg,view,(_,p)=>{theta.value=Math.max(-1.5,Math.min(1.5,p[0]))},{step:.1})
</script>

<template>
 <figure class="study-lab" aria-label="Lân cận SAM và cực đại chính xác của một hàm bậc hai">
  <figcaption class="lab-title">Gradient bằng 0 vẫn có thể có mất mát lớn ở lân cận</figcaption>
  <p class="lab-lead">Với L(θ) = aθ²/2, kéo tâm θ để đổi đoạn [θ − ρ, θ + ρ]. Vòng đỏ là một điểm có mất mát lớn nhất trên đoạn. Điểm xanh là bước leo theo gradient đã chuẩn hóa, chọn bước 0 khi gradient bằng 0.</p>
  <svg ref="svg" viewBox="0 0 400 350" role="group" aria-label="Đồ thị mất mát và tâm lân cận kéo được"
   @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <rect :x="view.sx(theta-rho)" y="36" :width="view.sx(theta+rho)-view.sx(theta-rho)" height="278" class="sam-interval"/>
   <line x1="36" x2="364" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis"/>
   <polyline v-for="(line,i) in curve" :key="i" :points="line" class="sam-curve"/>
   <line v-for="end in [theta-rho,theta+rho]" :key="end" :x1="view.sx(end)" :x2="view.sx(end)" :y1="view.sy(0)" :y2="view.sy(loss(end))" class="lab-guide"/>
   <circle :cx="view.sx(worst)" :cy="view.sy(loss(worst))" r="10" class="sam-worst"/>
   <circle :cx="view.sx(theta+approximation)" :cy="view.sy(loss(theta+approximation))" r="4" class="sam-ascent"/>
   <circle :cx="view.sx(theta)" :cy="view.sy(loss(theta))" r="6" class="lab-dot-accent"/>
   <circle :cx="view.sx(theta)" :cy="view.sy(loss(theta))" r="32" class="lab-handle sam-hit" tabindex="0" role="slider" aria-label="Tâm θ của lân cận" :aria-valuetext="fmt(theta,3)"
    @pointerdown="drag.start('theta',$event)" @keydown="drag.key('theta',thetaPoint,$event)"/>
   <text x="13" y="25">L</text><text x="365" y="337">θ</text>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh θ bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
  <div class="lab-buttons">
   <button type="button" @click="curvature=1">Độ cong 1</button><button type="button" @click="curvature=9">Độ cong 9</button>
   <button type="button" @click="theta=0">Tâm tại cực tiểu</button><button type="button" @click="theta=.7">Tâm lệch khỏi cực tiểu</button>
   <button type="button" @click="rho=.25">ρ = 0,25</button><button type="button" @click="rho=.5">ρ = 0,5</button>
  </div>
  <div class="lab-readout" role="status">
   <p>θ = {{fmt(theta,3)}}, a = {{fmt(curvature)}}, ρ = {{fmt(rho,2)}}. Mất mát tại tâm = {{fmt(loss(theta),5)}}.</p>
   <p>Gradient = {{fmt(gradient,4)}}, bước leo xấp xỉ = {{fmt(approximation,3)}}. Mất mát sau bước leo = {{fmt(loss(theta+approximation),5)}}.</p>
   <p>Cực đại chính xác trên đoạn = {{fmt(loss(worst),5)}}. {{theta===0?'Hai đầu mút cùng đạt cực đại, nhưng bước 0 của tuyến tính hóa ở lại đáy.':'Riêng hàm bậc hai này, bước leo chuẩn hóa tới đúng đầu mút xa 0 nhất.'}}</p>
   <p>Hình đo độ nhạy khi thay tham số trong một mô hình đơn giản. Nó không đo sự thay đổi phân phối dữ liệu hay bảo đảm khả năng tổng quát hóa của một mạng.</p>
  </div>
 </figure>
</template>

<style scoped>
.sam-interval{fill:var(--tim-soft);fill-opacity:.5}
.sam-curve{fill:none;stroke:var(--ink-3);stroke-width:1.5}
.sam-worst{fill:var(--paper);stroke:var(--do);stroke-width:1.7}
.sam-ascent{fill:var(--xanh)}
.sam-hit{fill:transparent!important;stroke:transparent}
.sam-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
</style>
