<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {project3,unprojectPlane} from '../services/foundation-geometry.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'

const props=defineProps({initialMode:{type:String,default:'2d',validator:value=>['2d','3d'].includes(value)}})
const svg=ref(null),mode=ref(props.initialMode),selected=ref('a')
const pairs=ref({
  '2d':{a:[-.8,0],b:[.8,0]},
  '3d':{a:[-.6,-.4],b:[.6,.4]}
})
const camera={yaw:32,pitch:28,scale:108,origin:[180,238]}
const flat=makeView({x0:-1.1,x1:1.1,y0:0,y1:1.15,width:360,height:320,pad:36})
const height=p=>Math.max(0,1-p[0]**2-p[1]**2)
const a=computed(()=>pairs.value[mode.value].a),b=computed(()=>pairs.value[mode.value].b)
const lifted=p=>[p[0],p[1],height(p)]
const middle=computed(()=>a.value.map((value,i)=>(value+b.value[i])/2))
const midpointHeight=computed(()=>(height(a.value)+height(b.value))/2)
const gap=computed(()=>((a.value[0]-b.value[0])**2+(a.value[1]-b.value[1])**2)/4)
const separated=computed(()=>a.value.some((value,index)=>value!==b.value[index]))
const P=(p,z=0)=>mode.value==='2d'?flat.point([p[0],z]):project3([p[0],p[1],z],camera)
const active=computed(()=>pairs.value[mode.value][selected.value])
const view=computed(()=>({x0:-1,x1:1,y0:-1,y1:1,toWorld:(x,y)=>mode.value==='2d'?[flat.toWorld(x,y)[0],0]:unprojectPlane([x,y],0,camera)}))
function movePoint(_,p){
  if(mode.value==='2d')p=[p[0],0]
  const radius=Math.hypot(...p)
  pairs.value[mode.value][selected.value]=radius>1?p.map(value=>value/radius):p
}
const drag=createDragger(svg,view,movePoint,{step:.05})
const arc=computed(()=>Array.from({length:101},(_,i)=>{const x=-1+i/50;return P([x,0],1-x*x).join(',')}).join(' '))
const disk=computed(()=>Array.from({length:97},(_,i)=>P([Math.cos(i*Math.PI/48),Math.sin(i*Math.PI/48)]).join(',')).join(' '))
const mesh=computed(()=>{
  const lines=[]
  for(const r of [.3,.6,.85,1])lines.push(Array.from({length:81},(_,i)=>{
    const angle=i*Math.PI/40;return P([r*Math.cos(angle),r*Math.sin(angle)],1-r*r).join(',')
  }).join(' '))
  for(const direction of [[1,0],[0,1]])lines.push(Array.from({length:81},(_,i)=>{
    const t=-1+i/40;return P(direction.map(value=>value*t),1-t*t).join(',')
  }).join(' '))
  return lines
})
const plotted=computed(()=>({
  a:P(a.value,height(a.value)),b:P(b.value,height(b.value)),
  m:P(middle.value,midpointHeight.value),g:P(middle.value,height(middle.value))
}))
const labels=computed(()=>{
  const points=Object.values(plotted.value).concat([P(a.value),P(b.value)])
  const axes=mode.value==='3d'?[
    {x:project3([0,0,1.18],camera)[0]+4,y:project3([0,0,1.18],camera)[1]-26,width:34,height:36},
    {x:P([1.18,0])[0]+3,y:P([1.18,0])[1]-6,width:38,height:34},
    {x:P([0,1.18])[0]-32,y:P([0,1.18])[1]-6,width:38,height:34}
  ]:[
    {x:flat.sx(0)+5,y:2,width:32,height:34},
    {x:331,y:flat.sy(0)-5,width:28,height:34}
  ]
  const specs=[{key:'a',text:separated.value?'A':'A = B',point:plotted.value.a}]
  if(separated.value)specs.push({key:'b',text:'B',point:plotted.value.b},{key:'m',text:'M',point:plotted.value.m},{key:'g',text:'G',point:plotted.value.g})
  return placePointLabels(specs,{width:360,height:320,reserved:[
    ...points.map(([x,y])=>({x:x-9,y:y-9,width:18,height:18})),
    ...axes
  ]})
})
function reset(){pairs.value[mode.value]=mode.value==='2d'?{a:[-.8,0],b:[.8,0]}:{a:[-.6,-.4],b:[.6,.4]}}
function coincide(){pairs.value[mode.value].b=[...a.value]}
</script>

<template>
  <figure class="study-lab" aria-label="Biến bù, tập nâng chiều và hình chiếu xuống miền đầu vào">
    <figcaption class="lab-title">Biến bù giữ hình chiếu, nhưng không giữ tính lồi của tập nâng chiều</figcaption>
    <p class="lab-lead">Chọn A hoặc B, rồi kéo chấm trên trục hoặc mặt phẳng đáy. Điểm phía trên luôn có s = 1 − bình phương độ dài đầu vào. Miền màu xanh là hình chiếu của tập nâng chiều xuống miền đầu vào.</p>
    <div class="lab-buttons" role="group" aria-label="Không gian của biến bù">
      <button type="button" :aria-pressed="mode==='2d'" @click="mode='2d'">Đầu vào R, cung trong R²</button>
      <button type="button" :aria-pressed="mode==='3d'" @click="mode='3d'">Đầu vào R², mặt trong R³</button>
    </div>
    <div class="lab-buttons" role="group" aria-label="Chọn điểm đầu vào cần kéo">
      <button type="button" :aria-pressed="selected==='a'" @click="selected='a'">Kéo A</button>
      <button type="button" :aria-pressed="selected==='b'" @click="selected='b'">Kéo B</button>
      <button type="button" @click="coincide">Cho B trùng A</button>
      <button type="button" @click="reset">Hai điểm đối xứng</button>
    </div>
    <svg ref="svg" viewBox="0 0 360 320" role="group" aria-label="Hai điểm thuộc cung hoặc mặt, trung điểm dây và điểm trên mặt cùng đầu vào" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <template v-if="mode==='2d'">
        <line x1="28" :y1="flat.sy(0)" x2="334" :y2="flat.sy(0)" class="lab-axis"/>
        <line :x1="flat.sx(0)" y1="22" :x2="flat.sx(0)" :y2="flat.sy(0)+12" class="lab-axis"/>
        <line :x1="flat.sx(-1)" :y1="flat.sy(0)" :x2="flat.sx(1)" :y2="flat.sy(0)" class="projection"/>
        <polyline :points="arc" class="surface-boundary"/>
        <text x="337" :y="flat.sy(0)+19">x</text><text :x="flat.sx(0)+11" y="28">s</text>
        <text :x="flat.sx(-1)" :y="flat.sy(0)+27" text-anchor="middle">−1</text>
        <text :x="flat.sx(1)" :y="flat.sy(0)+27" text-anchor="middle">1</text>
      </template>
      <template v-else>
        <polygon :points="disk" class="projection-floor"/>
        <line v-for="(end,index) in [[1.18,0,0],[0,1.18,0],[0,0,1.18]]" :key="index" :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="project3(end,camera)[0]" :y2="project3(end,camera)[1]" class="lab-axis"/>
        <polyline v-for="(line,index) in mesh" :key="index" :points="line" class="surface-mesh"/>
        <text :x="P([1.18,0])[0]+8" :y="P([1.18,0])[1]+18">x₁</text>
        <text :x="P([0,1.18])[0]-27" :y="P([0,1.18])[1]+18">x₂</text>
        <text :x="project3([0,0,1.18],camera)[0]+10" :y="project3([0,0,1.18],camera)[1]">s</text>
      </template>
      <line v-for="(point,index) in [a,b]" :key="index" :x1="P(point)[0]" :y1="P(point)[1]" :x2="P(point,height(point))[0]" :y2="P(point,height(point))[1]" class="lab-guide"/>
      <line :x1="plotted.a[0]" :y1="plotted.a[1]" :x2="plotted.b[0]" :y2="plotted.b[1]" class="chord"/>
      <line v-if="separated" :x1="plotted.m[0]" :y1="plotted.m[1]" :x2="plotted.g[0]" :y2="plotted.g[1]" class="gap"/>
      <circle :cx="plotted.a[0]" :cy="plotted.a[1]" r="6" class="lab-dot-accent"/>
      <rect v-if="separated" :x="plotted.b[0]-5" :y="plotted.b[1]-5" width="10" height="10" class="b-point"/>
      <path v-if="separated" :d="`M${plotted.m[0]},${plotted.m[1]-7}l7,7 -7,7 -7,-7Z`" class="midpoint"/>
      <circle v-if="separated" :cx="plotted.g[0]" :cy="plotted.g[1]" r="6" class="lab-dot-hollow"/>
      <template v-for="(label,key) in labels" :key="key">
        <text :x="label.x" :y="label.y" :text-anchor="label.anchor">{{key==='a'&&!separated?'A = B':key.toUpperCase()}}</text>
      </template>
      <circle :cx="P(a)[0]" :cy="P(a)[1]" r="5" class="lab-dot-accent"/>
      <rect :x="P(b)[0]-4" :y="P(b)[1]-4" width="8" height="8" class="b-point"/>
      <circle :cx="P(active)[0]" :cy="P(active)[1]" r="27" class="lab-handle hit" role="slider" tabindex="0" :aria-label="`Đầu vào của điểm ${selected.toUpperCase()}`" :aria-valuetext="fmtPoint(mode==='2d'?[active[0]]:active,4)" @pointerdown="drag.start(selected,$event)" @keydown="drag.key(selected,active,$event)"/>
    </svg>
    <p class="lab-legend"><span class="legend-accent">A: Chấm tròn tím</span><span class="legend-good">B: Hình vuông xanh</span><span class="legend-warn">Dây nối A và B</span><span class="legend-bad">M: Hình thoi trên dây</span></p>
    <details class="lab-tasks"><summary>Di chuyển đầu vào bằng nút</summary><LabPointControls :svg="svg" :axes="mode==='2d'?'x':'xy'"/></details>
    <div class="lab-readout" role="status">
      <p>A = {{fmtPoint(mode==='2d'?[a[0],height(a)]:lifted(a),3)}}, B = {{fmtPoint(mode==='2d'?[b[0],height(b)]:lifted(b),3)}}.</p>
      <p>Độ cao của trung điểm M là {{fmt(midpointHeight,4)}}. Tại cùng đầu vào, mặt có độ cao {{fmt(height(middle),4)}} ở điểm G.</p>
      <p :class="separated?'is-bad':'is-good'">{{separated?'M nằm ngoài tập nâng chiều.':'A và B trùng nhau nên trung điểm vẫn thuộc tập.'}} Chênh lệch độ cao G − M = {{fmt(gap,4)}}.</p>
      <p v-if="separated&&gap<.00005">Khoảng cách vẫn dương nhưng nhỏ hơn độ chính xác của số đang hiển thị. Giá trị làm tròn 0.0000 không có nghĩa hai điểm đã trùng nhau.</p>
      <p v-if="mode==='2d'">Đẳng thức nâng chiều là x² + s = 1, s ≥ 0. Miền đầu vào vẫn là đoạn [−1, 1]. Chỉ cung parabol là khả thi trong không gian (x, s).</p>
      <p v-else>Đẳng thức nâng chiều là x₁² + x₂² + s = 1, s ≥ 0. Miền đầu vào là đĩa đơn vị. Chỉ mặt cong là khả thi trong R³, còn các điểm nằm dưới mặt nói chung không thỏa đẳng thức.</p>
      <p>Hình chiếu giữ được miền đầu vào lồi. Dây nối hai điểm khác nhau trên mặt nằm dưới mặt, nên tập nâng chiều này không lồi. Hình R³ là phép chiếu trực giao, không dùng để đo góc hoặc khoảng cách.</p>
    </div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Giữ A cố định, kéo B về A. Vì sao khoảng G − M giảm về 0?</li><li>Chuyển sang R³. Kéo điểm trên đĩa đáy, rồi so sánh độ cao mặt và trung điểm dây.</li><li>M có đầu vào hợp lệ. Vì sao điều đó chưa đủ để M thỏa đẳng thức có biến bù?</li></ol></details>
  </figure>
</template>

<style scoped>
svg text{font-size:18px}
.surface-boundary{fill:none;stroke:var(--ink);stroke-width:2}
.surface-mesh{fill:none;stroke:var(--ink-2);stroke-width:1;opacity:.6}
.projection{stroke:var(--xanh);stroke-width:3}
.projection-floor{fill:var(--xanh-soft);stroke:var(--xanh);stroke-width:1.3}
.chord{stroke:var(--vang);stroke-width:2.4}
.gap{stroke:var(--do);stroke-width:1.4;stroke-dasharray:4 4}
.b-point{fill:var(--xanh)}
.midpoint{fill:var(--paper);stroke:var(--do);stroke-width:2}
svg :is(line,polyline,polygon,rect,path,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
