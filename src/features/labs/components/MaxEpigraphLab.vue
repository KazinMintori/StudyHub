<script setup>
import {computed,ref,watch} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3,unprojectPlane} from '../services/foundation-geometry.mjs'
import {clipPolyline} from '../services/svg-clipping.mjs'

const props=defineProps({initialMode:{type:String,default:'2d',validator:value=>['2d','3d'].includes(value)}})
const plotSvg=ref(null),spaceSvg=ref(null),mode=ref(props.initialMode),input=ref([1,props.initialMode==='3d'?.4:0]),level=ref(4.5),reverse=ref(false)
const functions=[x=>x*x,x=>(x-3)**2,x=>2-x]
const surface=p=>Math.max(...functions.map(f=>f(p[0])))+p[1]**2
const values=computed(()=>functions.map(f=>f(input.value[0])+input.value[1]**2))
const residuals=computed(()=>values.value.map(value=>level.value-value))
const feasible=computed(()=>residuals.value.every(value=>value>=-1e-10))
const sectionMinimum=computed(()=>2.25+input.value[1]**2)
const flat=makeView({x0:-.5,x1:3.5,y0:0,y1:14,width:360,height:330,pad:32})
const view=computed(()=>flat)
const flatDrag=createDragger(plotSvg,view,(_,p)=>{input.value=[p[0],input.value[1]];level.value=p[1]},{step:.1})
const camera=computed(()=>({yaw:reverse.value?-32:32,pitch:28,scale:60,origin:[180,243]}))
const P=(p,t=0)=>project3([p[0]-1.5,p[1],t*.18],camera.value)
const spaceView=computed(()=>({x0:-.5,x1:3.5,y0:-1,y1:1,toWorld:(x,y)=>{
  const p=unprojectPlane([x,y],0,camera.value);return [p[0]+1.5,p[1]]
}}))
const spaceDrag=createDragger(spaceSvg,spaceView,(_,p)=>{input.value=p},{step:.1})
const serialize=points=>points.map(point=>point.join(',')).join(' ')
const clippedCurve=f=>clipPolyline(Array.from({length:241},(_,i)=>{
  const x=-.5+i/60;return flat.point([x,f(x)+input.value[1]**2])
}),{x0:32,x1:328,y0:32,y1:298}).map(serialize)
const curves=computed(()=>functions.map(clippedCurve))
const boundary=computed(()=>clippedCurve(x=>Math.max(...functions.map(f=>f(x)))))
const region=computed(()=>serialize([
  [32,32],[328,32],
  ...Array.from({length:241},(_,i)=>{
    const x=3.5-i/60;return flat.point([x,Math.min(14,surface([x,input.value[1]]))])
  })
]))
const slice=computed(()=>{
  const t=level.value-input.value[1]**2
  if(t<0)return null
  const radius=Math.sqrt(t),lower=Math.max(-radius,3-radius,2-t),upper=Math.min(radius,3+radius)
  return lower>upper+1e-10?null:[Math.max(-.5,lower),Math.min(3.5,upper)]
})
const mesh=computed(()=>{
  const lines=[]
  for(const y of [-1,-.5,0,.5,1])lines.push(serialize(Array.from({length:81},(_,i)=>{
    const p=[-.5+i/20,y];return P(p,surface(p))
  })))
  for(const x of [0,.75,1.5,2.25,3])lines.push(serialize(Array.from({length:41},(_,i)=>{
    const p=[x,-1+i/20];return P(p,surface(p))
  })))
  return lines
})
const section=computed(()=>serialize(Array.from({length:81},(_,i)=>{
  const p=[-.5+i/20,input.value[1]];return P(p,surface(p))
})))
const levelRegion=computed(()=>{
  if(level.value<2.25)return null
  const root=Math.sqrt(level.value),lo=Math.max(-.5,3-root,2-level.value),hi=Math.min(3.5,root)
  if(lo>hi)return null
  const upper=Array.from({length:101},(_,i)=>{
    const x=lo+(hi-lo)*i/100
    const y=Math.min(1,Math.sqrt(Math.max(0,level.value-Math.max(...functions.map(f=>f(x))))))
    return [x,y]
  })
  return serialize([...upper,...upper.slice().reverse().map(([x,y])=>[x,-y])].map(p=>P(p,level.value)))
})
const baseCorners=[[-.5,-1],[3.5,-1],[3.5,1],[-.5,1]]
function optimum(){input.value=[1.5,0];level.value=2.25}
function below(){input.value=[1.5,0];level.value=2}
watch(mode,()=>{input.value=[1,mode.value==='3d'?.4:0];level.value=4.5})
</script>

<template>
  <figure class="study-lab" aria-label="Epigraph của giá trị lớn nhất và phép nâng từ đầu vào một chiều lên hai chiều">
    <figcaption class="lab-title">Hạ mức t tới nơi ba ràng buộc còn có thể cùng thỏa mãn</figcaption>
    <p class="lab-lead">Kéo điểm P trên đồ thị để đổi x và t. Miền tô xanh nằm phía trên cả ba đường. Đoạn xanh nằm ngang cho biết những x khả thi tại mức t đang chọn.</p>
    <div class="lab-buttons" role="group" aria-label="Chiều của đầu vào và epigraph">
      <button type="button" :aria-pressed="mode==='2d'" @click="mode='2d'">Đầu vào R, epigraph trong R²</button>
      <button type="button" :aria-pressed="mode==='3d'" @click="mode='3d'">Đầu vào R², epigraph trong R³</button>
    </div>
    <p v-if="mode==='3d'" class="lab-lead">Bản mở rộng thêm cùng số hạng y² vào mỗi hàm. Kéo chấm trên mặt phẳng đáy để đổi (x, y). Hình phẳng còn lại là lát cắt tại y đang chọn. Lưới trong R³ là biên dưới, epigraph gồm các điểm ở trên biên này. Trong khung nét đứt ở độ cao t, chỉ phần xanh là khả thi.</p>
    <div class="lab-buttons" role="group" aria-label="Các mức thử của epigraph">
      <button type="button" @click="level=surface(input)">Đặt t sát đồ thị</button>
      <button type="button" @click="optimum">Nghiệm tối ưu</button>
      <button type="button" @click="below">Dưới giá trị tối ưu</button>
      <button type="button" @click="level=5">Nâng t lên 5</button>
      <button v-if="mode==='3d'" type="button" :aria-pressed="reverse" @click="reverse=!reverse">Đổi góc nhìn</button>
    </div>
    <div class="lab-pair" :class="{'single-panel':mode==='2d'}">
      <svg v-if="mode==='3d'" ref="spaceSvg" viewBox="0 0 360 330" role="group" aria-label="Biên epigraph trong R³ và đầu vào kéo trên mặt phẳng đáy" @pointermove="spaceDrag.move" @pointerup="spaceDrag.end" @pointercancel="spaceDrag.end" @lostpointercapture="spaceDrag.end">
        <polygon :points="serialize(baseCorners.map(p=>P(p)))" class="base-plane"/>
        <line v-for="(end,index) in [[[3.6,0],0],[[1.5,1.15],0],[[1.5,0],14.5]]" :key="index" :x1="P([1.5,0])[0]" :y1="P([1.5,0])[1]" :x2="P(end[0],end[1])[0]" :y2="P(end[0],end[1])[1]" class="lab-axis"/>
        <polyline v-for="(line,index) in mesh" :key="index" :points="line" class="surface-mesh"/>
        <polygon :points="serialize(baseCorners.map(p=>P(p,level)))" class="level-plane"/>
        <polygon v-if="levelRegion" :points="levelRegion" class="level-region"/>
        <polyline :points="section" class="section"/>
        <line :x1="P(input)[0]" :y1="P(input)[1]" :x2="P(input,level)[0]" :y2="P(input,level)[1]" class="lab-guide"/>
        <circle :cx="P(input,level)[0]" :cy="P(input,level)[1]" r="6" :class="feasible?'lab-dot-accent':'lab-dot-bad'"/>
        <circle :cx="P(input)[0]" :cy="P(input)[1]" r="7" class="lab-dot-accent"/>
        <circle :cx="P(input)[0]" :cy="P(input)[1]" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Đầu vào x và y trên mặt phẳng đáy" :aria-valuetext="fmtPoint(input,4)" @pointerdown="spaceDrag.start('input',$event)" @keydown="spaceDrag.key('input',input,$event)"/>
        <text :x="P([3.6,0])[0]+4" :y="P([3.6,0])[1]+20">x</text>
        <text :x="P([1.5,1.15])[0]-20" :y="P([1.5,1.15])[1]+20">y</text>
        <text :x="P([1.5,0],14.5)[0]+10" :y="P([1.5,0],14.5)[1]">t</text>
      </svg>
      <svg ref="plotSvg" viewBox="0 0 360 330" role="group" aria-label="Ba đường cong lồi, epigraph chung và điểm P có tọa độ x và t" @pointermove="flatDrag.move" @pointerup="flatDrag.end" @pointercancel="flatDrag.end" @lostpointercapture="flatDrag.end">
        <polygon :points="region" class="epigraph-region"/>
        <line x1="32" y1="298" x2="328" y2="298" class="lab-axis"/>
        <line :x1="flat.sx(0)" y1="26" :x2="flat.sx(0)" y2="304" class="lab-axis"/>
        <g v-for="(segments,index) in curves" :key="index">
          <polyline v-for="(points,i) in segments" :key="i" :points="points" :class="['curve',`curve-${index}`]"/>
        </g>
        <polyline v-for="(points,index) in boundary" :key="index" :points="points" class="envelope"/>
        <line x1="32" :y1="flat.sy(level)" x2="328" :y2="flat.sy(level)" class="level-line"/>
        <line v-if="slice" :x1="flat.sx(slice[0])" :y1="flat.sy(level)" :x2="flat.sx(slice[1])" :y2="flat.sy(level)" class="feasible-slice"/>
        <circle v-if="slice&&Math.abs(slice[1]-slice[0])<1e-8" :cx="flat.sx(slice[0])" :cy="flat.sy(level)" r="4" class="slice-singleton"/>
        <circle :cx="flat.sx(input[0])" :cy="flat.sy(level)" r="7" :class="feasible?'lab-dot-accent':'lab-dot-bad'"/>
        <circle :cx="flat.sx(input[0])" :cy="flat.sy(level)" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Điểm P điều chỉnh x và t" :aria-valuetext="fmtPoint([input[0],level],4)" @pointerdown="flatDrag.start('trial',$event)" @keydown="flatDrag.key('trial',[input[0],level],$event)"/>
        <text :x="flat.sx(0)+9" y="24">t</text><text x="331" y="319">x</text>
        <text v-for="x in [1,2,3]" :key="x" :x="flat.sx(x)" y="321" text-anchor="middle">{{x}}</text>
        <text :x="flat.sx(0)-9" :y="flat.sy(5)+6" text-anchor="end">5</text>
        <text :x="flat.sx(0)-9" :y="flat.sy(10)+6" text-anchor="end">10</text>
      </svg>
    </div>
    <p class="lab-legend"><span class="legend-accent">q₁ = x²{{mode==='3d'?' + y²':''}}</span><span class="legend-warn">q₂ = (x − 3)²{{mode==='3d'?' + y²':''}}</span><span class="legend-guide">q₃ = 2 − x{{mode==='3d'?' + y²':''}}</span><span class="legend-good">Miền thỏa cả ba qᵢ ≤ t</span></p>
    <details class="lab-tasks"><summary>Di chuyển các điểm bằng nút</summary><LabPointControls v-if="mode==='3d'" :svg="spaceSvg"/><LabPointControls :svg="plotSvg"/></details>
    <div class="lab-readout" role="status">
      <p v-if="mode==='2d'">P = (x, t) = {{fmtPoint([input[0],level],3)}}.</p>
      <p v-else>P = (x, y, t) = {{fmtPoint([...input,level],3)}}. Trong bản mở rộng, mỗi qᵢ(x, y) bằng qᵢ(x) + y².</p>
      <p :class="feasible?'is-good':'is-bad'">{{feasible?'P thỏa cả ba ràng buộc.':'P chưa thuộc epigraph.'}} Mức t = {{fmt(level,3)}}, giá trị lớn nhất của ba hàm là {{fmt(surface(input),3)}}.</p>
      <p>Ba độ dư t − qᵢ lần lượt là {{residuals.map(value=>fmt(value,3)).join(', ')}}. Độ dư âm chỉ đúng ràng buộc đang bị vi phạm.</p>
      <p>Nhận xét khả thi dùng dung sai số 10⁻¹⁰. Các độ dư hiển thị được làm tròn tới ba chữ số thập phân.</p>
      <p v-if="slice">Tại mức đang chọn, đầu vào x khả thi trên đoạn [{{slice.map(value=>fmt(value,3)).join(', ')}}]{{mode==='3d'?' trong lát cắt y hiện tại':''}}.</p>
      <p v-else>Không có x khả thi tại mức t này{{mode==='3d'?' trong lát cắt y hiện tại':''}}.</p>
      <p v-if="mode==='3d'">Đáy lát cắt hiện tại là 2.25 + y² = {{fmt(sectionMinimum,3)}}. Đáy toàn bộ epigraph vẫn là t = 2.25, tại (x, y) = (1.5, 0).</p>
      <p v-else>Đáy epigraph ở (1.5, 2.25). Hai parabol chạm mức t tại đó, còn đường thẳng có độ dư 1.75.</p>
      <p>Hình phẳng chỉ hiển thị −0.5 ≤ x ≤ 3.5 và 0 ≤ t ≤ 14. Hình R³ có thang đứng bằng 0.18 lần thang đầu vào, nên không dùng hình chiếu để đo độ dài hay góc.</p>
    </div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt t dưới 2.25. Vì sao kéo x không thể tìm được một điểm khả thi?</li><li>Đưa P tới nghiệm tối ưu. Vì sao chỉ hai trong ba ràng buộc đạt dấu bằng?</li><li>Chuyển sang R³ rồi kéo y ra xa 0. Đáy lát cắt thay đổi thế nào?</li></ol></details>
  </figure>
</template>

<style scoped>
.single-panel{grid-template-columns:minmax(0,1fr)!important}
svg text{font-size:18px}
.epigraph-region{fill:var(--xanh-soft);stroke:none}
.curve{fill:none;stroke-width:1.5}
.curve-0{stroke:var(--tim)}.curve-1{stroke:var(--vang)}.curve-2{stroke:var(--ink-3);stroke-dasharray:5 4}
.envelope{fill:none;stroke:var(--ink);stroke-width:2}
.level-line{stroke:var(--ink-3);stroke-width:1;stroke-dasharray:5 5}
.feasible-slice{stroke:var(--xanh);stroke-width:3.4}
.slice-singleton{fill:var(--xanh)}
.base-plane{fill:var(--tim-soft);stroke:var(--rule);stroke-width:1}
.level-plane{fill:none;stroke:var(--ink-3);stroke-width:1;stroke-dasharray:5 4}
.level-region{fill:var(--xanh-soft);stroke:var(--xanh);stroke-width:1.3}
.surface-mesh{fill:none;stroke:var(--ink-2);stroke-width:1;opacity:.5}
.section{fill:none;stroke:var(--vang);stroke-width:2.4}
svg :is(line,polyline,polygon,path,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
