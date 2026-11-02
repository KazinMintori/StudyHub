<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,makeView,fmt,fmtPoint} from '../controllers/svg-drag.js'
import {cycleFiveModel} from '../services/foundation-geometry.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'
const svg=ref(null),signs=ref([1,-1,1,-1,1]),angles=ref(Array.from({length:5},(_,i)=>4*Math.PI*i/5))
const row=computed(()=>cycleFiveModel(signs.value,angles.value))
const view=ref(makeView({x0:-1.4,x1:1.4,y0:-1.4,y1:1.4,width:400,height:400,pad:45})),P=p=>view.value.point(p)
const drag=createDragger(svg,view,(name,p)=>{if(Math.hypot(...p)>1e-8)angles.value=angles.value.map((a,i)=>i===Number(name)?Math.atan2(p[1],p[0]):a)},{step:.05})
const vectorGroups=computed(()=>{
 const groups=[]
 row.value.vectors.forEach((vector,index)=>{
  const existing=groups.find(group=>Math.hypot(...vector.map((v,i)=>v-group.vector[i]))<1e-7)
  if(existing)existing.indices.push(index)
  else groups.push({vector,indices:[index]})
 })
 return groups.map((group,index)=>({...group,key:String(index),text:group.indices.map(i=>`u${i+1}`).join(', ')}))
})
const vectorLabels=computed(()=>placePointLabels(vectorGroups.value.map(group=>({key:group.key,point:P(group.vector),text:group.text})),{width:400,height:400,reserved:[{x:0,y:0,width:400,height:32}]}))
const vertices=Array.from({length:5},(_,i)=>[200+130*Math.cos(-Math.PI/2+2*Math.PI*i/5),210+130*Math.sin(-Math.PI/2+2*Math.PI*i/5)])
function toggle(i){signs.value=signs.value.map((s,j)=>j===i?-s:s)}
function resetVectors(){angles.value=Array.from({length:5},(_,i)=>4*Math.PI*i/5)}
</script>

<template>
 <figure class="study-lab" aria-label="Max-Cut chu trình năm đỉnh và thư giãn SDP bằng các vector đơn vị">
  <figcaption class="lab-title">Bỏ điều kiện hạng một cho phép một phương án không còn là phân hoạch hai nhóm</figcaption>
  <p class="lab-lead">Chạm hoặc bấm một đỉnh ở hình đầu để đổi dấu ±1 và đổi nhóm. Nhãn 1+ chỉ đỉnh 1 có dấu +1. Kéo từng đầu vector ở hình sau. Các vector đơn vị tạo Gram X khả thi cho SDP, nhưng thường không còn có dạng xxᵀ với xᵢ = ±1.</p>
  <div class="lab-pair">
   <svg viewBox="0 0 400 400" role="group" aria-label="Chu trình năm đỉnh, bấm mỗi đỉnh để đổi nhóm">
    <line v-for="(point,i) in vertices" :key="'edge'+i" :x1="point[0]" :y1="point[1]" :x2="vertices[(i+1)%5][0]" :y2="vertices[(i+1)%5][1]" :class="signs[i]!==signs[(i+1)%5]?'lab-good':'lab-guide'"/>
    <g v-for="(point,i) in vertices" :key="i"><circle :cx="point[0]" :cy="point[1]" r="30" :class="signs[i]===1?'lab-dot-accent':'lab-dot-warn'" class="sign-node" tabindex="0" role="button" :aria-label="`Đỉnh ${i+1}, dấu ${signs[i]}, bấm để đổi nhóm`" :aria-pressed="signs[i]===1" @click="toggle(i)" @keydown.enter.prevent="toggle(i)" @keydown.space.prevent="toggle(i)"/><text :x="point[0]" :y="point[1]+7" text-anchor="middle" class="sign-label">{{i+1}}{{signs[i]===1?'+':'−'}}</text></g>
    <text x="12" y="23">Phân hoạch nguyên, mỗi dấu là ±1</text><text x="32" y="387">Cạnh xanh: Hai đầu khác nhóm</text>
   </svg>
   <svg ref="svg" viewBox="0 0 400 400" role="group" aria-label="Năm vector đơn vị kéo được, tạo một nghiệm Gram hạng tối đa hai của SDP" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
    <circle :cx="P([0,0])[0]" :cy="P([0,0])[1]" :r="view.sx(1)-view.sx(0)" class="lab-guide"/>
    <line v-for="group in vectorGroups" :key="'v'+group.key" :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P(group.vector)[0]" :y2="P(group.vector)[1]" class="lab-accent"/>
    <circle v-for="group in vectorGroups" :key="'point'+group.key" :cx="P(group.vector)[0]" :cy="P(group.vector)[1]" r="7" class="lab-dot-warn"/>
    <text v-for="group in vectorGroups" :key="'label'+group.key" :x="vectorLabels[group.key].x" :y="vectorLabels[group.key].y" :text-anchor="vectorLabels[group.key].anchor">{{group.text}}</text>
    <circle v-for="(v,i) in row.vectors" :key="'handle'+i" :cx="P(v)[0]" :cy="P(v)[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" :aria-label="`Vector đơn vị u${i+1}`" :aria-valuetext="fmtPoint(v,4)" @pointerdown="drag.start(String(i),$event)" @keydown="drag.key(String(i),v,$event)"/>
    <text x="12" y="23">Vector uᵢ trong R², Xᵢⱼ = uᵢᵀuⱼ</text>
   </svg>
  </div>
  <details class="lab-tasks"><summary>Điều chỉnh vector bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-buttons"><button type="button" @click="signs=[1,1,1,1,1]">Tất cả cùng nhóm</button><button type="button" @click="signs=[1,-1,1,-1,1]">Một phân hoạch tối ưu</button><button type="button" @click="resetVectors">Vector SDP tối ưu</button><button type="button" @click="angles=signs.map(s=>s===1?0:Math.PI)">Đưa phân hoạch thành Gram hạng 1</button></div>
  <div class="lab-readout" role="status">
   <p>Dấu x = ({{signs.join(', ')}}), số cạnh cắt k = {{row.cuts}}. Mục tiêu QP xᵀWx = 10 − 4k = {{row.integerValue}}. Cắt nhiều nhất là 4 cạnh, tương ứng QP nhỏ nhất bằng −6.</p>
   <p>Gram đang chọn có hạng {{row.rank}}, tr(WX) = {{fmt(row.relaxed,6)}}. Giá trị cắt của nghiệm thư giãn này là {{fmt(row.relaxedCut,6)}}. Khi hạng bằng 2, nó không phải một phân hoạch hai nhóm, nên giá trị có thể không nguyên.</p>
   <p>Chứng chỉ ν = φ(1, 1, 1, 1, 1), φ = (1 + √5)/2, cho cận dưới QP/SDP d* = {{fmt(row.dual,6)}}. Độ rộng chứng nhận cho Gram đang chọn bằng {{fmt(row.relaxed-row.dual,6)}}.</p>
   <p>Cận trên được chứng nhận cho số cạnh cắt nguyên là {{fmt(row.cutUpper,6)}}. Đây là cận từ đối ngẫu, không phải mọi giá trị của một Gram đang thử đều là cận trên cho bài toán nguyên. Do số cạnh cắt nguyên, kết hợp cận này còn suy ra k ≤ 4.</p>
   <p>Từ chính dấu x đang chọn, bộ νᵢ = −xᵢ(Wx)ᵢ bằng ({{row.nu.join(', ')}}) làm điều kiện dừng KKT gốc đúng. Dù vậy, x có thể không tối ưu. KKT của bài toán phi lồi không tự là chứng nhận toàn cục.</p>
   <p>Hình vector chỉ khảo sát các Gram tạo bởi vector trong R², không vẽ toàn bộ miền SDP. Nó chứa nghiệm tối ưu của ví dụ này. Các vector trùng nhau được gộp thành một đường, một điểm và một nhãn chung, nhưng bộ điều khiển vẫn cho chọn riêng từng vector. Có thể chọn vector bằng danh sách trong bộ nút hoặc khôi phục cấu hình tối ưu để tách chúng.</p>
  </div>
  <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đổi dấu các đỉnh. Vì sao một chu trình có số đỉnh lẻ không thể cắt cả năm cạnh?</li><li>Đưa phân hoạch thành Gram hạng 1. Vì sao mục tiêu Gram trùng mục tiêu của vector dấu?</li><li>Khôi phục vector SDP tối ưu. Vì sao giá trị cắt khoảng 4.52254 không phải một cách cắt thật có hơn bốn cạnh?</li></ol></details>
 </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
.sign-node{cursor:pointer;touch-action:manipulation;stroke:transparent;stroke-width:8;paint-order:stroke}
.sign-node:focus-visible{stroke:var(--ink);stroke-width:4}
svg text{font-size:20px;pointer-events:none}
.sign-label{fill:var(--paper);font-weight:600}
.lab-pair svg{max-height:none}
</style>
