<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import MathMatrix from '../../../core/math/components/MathMatrix.vue'
import { makeView, createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { project3, unprojectPlane } from '../services/foundation-geometry.mjs'

// PSD uses the Frobenius-orthonormal coordinates
// u=(a-c)/sqrt(2), v=sqrt(2)b, t=(a+c)/sqrt(2).
// Then a*c-b²=(t²-u²-v²)/2 and trace=sqrt(2)t.
const props=defineProps({type:{type:String,default:'soc'}})
const svg=ref(null), sliceSvg=ref(null), xy=ref([.4,.3]), height=ref(.8), yaw=ref(35), pitch=ref(28)
const camera=computed(()=>({yaw:yaw.value,pitch:pitch.value,scale:78,origin:[210,212]}))
const P=p=>project3(p,camera.value)
const flat=ref(makeView({x0:-1.6,x1:1.6,y0:-1.6,y1:1.6,width:360,height:360,pad:25}))
const point=computed(()=>[...xy.value,height.value])
const view=computed(()=>({x0:-1.3,x1:1.3,y0:-1.3,y1:1.3,toWorld:(x,y)=>unprojectPlane([x,y],height.value,camera.value)}))
const move=(_,p)=>{xy.value=p}
const drag=createDragger(svg,view,move,{step:.05,snap:.01})
const sliceView=computed(()=>({...flat.value,x0:-1.3,x1:1.3,y0:-1.3,y1:1.3}))
const sliceDrag=createDragger(sliceSvg,sliceView,move,{step:.05,snap:.01})
const rings=Array.from({length:6},(_,j)=>{const h=(j+1)*.25;return Array.from({length:97},(_,i)=>[h*Math.cos(i*Math.PI/48),h*Math.sin(i*Math.PI/48),h])})
const rays=Array.from({length:12},(_,i)=>[[0,0,0],[1.5*Math.cos(i*Math.PI/6),1.5*Math.sin(i*Math.PI/6),1.5]])
const path=points=>points.map(p=>P(p).join(',')).join(' ')
const sliceRing=computed(()=>height.value<0?[]:Array.from({length:97},(_,i)=>[height.value*Math.cos(i*Math.PI/48),height.value*Math.sin(i*Math.PI/48),height.value]))
const radius=computed(()=>Math.hypot(...xy.value))
const inside=computed(()=>radius.value<=height.value+1e-9)
const matrix=computed(()=>{const [u,v]=xy.value,t=height.value;return [[(t+u)/Math.SQRT2,v/Math.SQRT2],[v/Math.SQRT2,(t-u)/Math.SQRT2]]})
const displayMatrix=computed(()=>matrix.value.map(row=>row.map(value=>Number(value.toFixed(3)))))
const eig=computed(()=>[(height.value+radius.value)/Math.SQRT2,(height.value-radius.value)/Math.SQRT2])
const axes=computed(()=>[{p:[1.7,0,0],label:props.type==='psd'?'u':'x₁'},{p:[0,1.7,0],label:props.type==='psd'?'v':'x₂'},{p:[0,0,1.7],label:'t'}])
function preset(boundary=false){height.value=.8;xy.value=boundary?[.8,0]:[0,0]}
</script>

<template>
  <figure class="study-lab" :aria-label="type==='soc'?'Nón bậc hai và lát cắt tròn trong R³':'Nón PSD hai hàng trong ba tọa độ trực chuẩn'">
    <figcaption class="lab-title">{{type==='soc'?'Kéo điểm trên lát cắt của nón bậc hai':'Ma trận đối xứng hai hàng cũng có hình học ba chiều'}}</figcaption>
    <p class="lab-lead">Kéo điểm trong một trong hai hình. Độ cao t được giữ cố định khi kéo. Thay t để xem lát cắt co lại, phình ra hoặc biến mất. {{type==='psd'?'Ba tọa độ u, v, t mô tả ba thành phần độc lập của một ma trận đối xứng, không phải tọa độ của vector mà ma trận tác động lên.':''}}</p>
    <svg ref="svg" viewBox="0 0 420 330" role="group" aria-label="Khung nón vô hạn, lát cắt ngang t cố định và điểm thử kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <polygon :points="[[-1.3,-1.3,height],[1.3,-1.3,height],[1.3,1.3,height],[-1.3,1.3,height]].map(p=>P(p).join(',')).join(' ')" class="slice-plane"/>
      <g v-for="axis in axes" :key="axis.label"><line :x1="P([0,0,0])[0]" :y1="P([0,0,0])[1]" :x2="P(axis.p)[0]" :y2="P(axis.p)[1]" class="lab-axis"/><text :x="P(axis.p)[0]+5" :y="P(axis.p)[1]+5">{{axis.label}}</text></g>
      <polyline v-for="(ray,i) in rays" :key="'r'+i" :points="path(ray)" class="lab-guide"/>
      <polyline v-for="(ring,i) in rings" :key="'c'+i" :points="path(ring)" class="lab-line"/>
      <polygon v-if="height>=0" :points="path(sliceRing)" class="lab-good-fill cut-disk"/>
      <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" :class="inside?'lab-dot-accent':'lab-dot-bad'" pointer-events="none"/>
      <text :x="P(point)[0]+12" :y="P(point)[1]-12">q</text>
      <circle :cx="P(point)[0]" :cy="P(point)[1]" r="32" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Điểm q trong lát cắt nón" :aria-valuetext="fmtPoint(point)" @pointerdown="drag.start('q',$event)" @keydown="drag.key('q',xy,$event)"/>
    </svg>
    <p class="lab-lead">Nhìn thẳng vào lát cắt t = {{fmt(height)}}. {{height<0?'Lát cắt rỗng.':height===0?'Lát cắt chỉ còn đỉnh nón.':'Miền thuộc nón là đĩa tròn có bán kính t.'}}</p>
    <svg ref="sliceSvg" viewBox="0 0 360 360" role="group" aria-label="Mặt cắt ngang của nón nhìn chính diện, cùng điểm q kéo được" @pointermove="sliceDrag.move" @pointerup="sliceDrag.end" @pointercancel="sliceDrag.end" @lostpointercapture="sliceDrag.end">
      <line x1="20" y1="180" x2="340" y2="180" class="lab-axis"/><line x1="180" y1="20" x2="180" y2="340" class="lab-axis"/>
      <circle v-if="height>=0" cx="180" cy="180" :r="height*310/3.2" class="lab-good-fill"/>
      <circle :cx="flat.sx(xy[0])" :cy="flat.sy(xy[1])" r="8" :class="inside?'lab-dot-accent':'lab-dot-bad'" pointer-events="none"/>
      <text x="318" y="202">{{type==='psd'?'u':'x₁'}}</text><text x="190" y="31">{{type==='psd'?'v':'x₂'}}</text>
      <circle :cx="flat.sx(xy[0])" :cy="flat.sy(xy[1])" r="32" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Cùng điểm q trong hình lát cắt" :aria-valuetext="fmtPoint(point)" @pointerdown="sliceDrag.start('q',$event)" @keydown="sliceDrag.key('q',xy,$event)"/>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="sliceSvg"/></details>
    <div class="lab-controls"><label>Độ cao t = {{fmt(height)}}<input v-model.number="height" type="range" min="-.2" max="1.4" step=".05"/></label><label>Góc nhìn quanh trục đứng: {{yaw}}°<input v-model.number="yaw" type="range" min="-180" max="180" step="5"/></label><label>Góc nhìn từ trên: {{pitch}}°<input v-model.number="pitch" type="range" min="20" max="40" step="2"/></label></div>
    <div class="lab-buttons"><button type="button" @click="preset(false)">Điểm trong</button><button type="button" @click="preset(true)">Điểm trên biên</button><button type="button" @click="height=0;xy=[0,0]">Đỉnh nón</button></div>
    <div class="lab-readout" role="status">
      <p>q = {{fmtPoint(point)}}. Độ dài ngang = {{fmt(radius)}}, độ cao t = {{fmt(height)}}. {{inside?'q thuộc nón.':'q không thuộc nón.'}}</p>
      <template v-if="type==='psd'"><p>Ma trận tương ứng <MathMatrix :rows="displayMatrix" label="Ma trận đối xứng tương ứng với điểm q, làm tròn ba chữ số thập phân"/>.</p><p>Hai trị riêng là {{fmt(eig[0],3)}} và {{fmt(eig[1],3)}}. {{inside?'Cả hai không âm, nên ma trận nửa xác định dương.':'Có trị riêng âm, nên ma trận không nửa xác định dương.'}}</p><p>Tọa độ trực chuẩn u = (a − c)/√2, v = √2b, t = (a + c)/√2, với ma trận có các hàng (a, b) và (b, c). Đổi t trong khi giữ u, v cố định làm hai phần tử đường chéo cùng thay đổi.</p></template>
      <p v-else>Nón gồm những điểm thỏa √(x₁² + x₂²) ≤ t. Vì độ dài không âm, không có điểm nào của nón ở t &lt; 0. Các vòng phía trên chỉ thể hiện biên, còn đĩa lát cắt cho thấy cả phần bên trong.</p>
      <p>Hình chiếu vuông góc làm đường tròn ngang thành ellipse. Nón còn kéo dài lên vô hạn, không có nắp ở vòng trên cùng.</p>
    </div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đặt điểm trên biên rồi tăng riêng t. Điểm mới nằm ở đâu so với nón?</li><li>Đặt t = 0 rồi kéo điểm ra khỏi gốc. Vì sao mọi điểm khác gốc đều ở ngoài?</li><li>{{type==='psd'?'Vì sao ma trận ở biên có ít nhất một trị riêng bằng 0?':'So sánh hình tròn trong lát cắt chính diện với ellipse trên hình 3D. Điều kiện thuộc nón có đổi theo góc nhìn không?'}}</li></ol></details>
  </figure>
</template>

<style scoped>
.slice-plane{fill:var(--canvas);fill-opacity:.65;stroke:var(--ink-3);stroke-width:1;stroke-dasharray:4 4}
.cut-disk{fill-opacity:.55}
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
</style>
