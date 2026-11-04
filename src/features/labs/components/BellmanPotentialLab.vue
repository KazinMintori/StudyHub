<script setup>
import {computed,ref,useId} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,makeView} from '../controllers/svg-drag.js'
import {bellmanPotentials,potentialSlacks} from '../services/bellman-potentials.mjs'

const costSvg=ref(null),potentialSvg=ref(null),shortcut=ref(4),potentials=ref({S:4,A:3,B:1,T:0})
const completed=ref(0),markerId=useId()
const model=computed(()=>bellmanPotentials(shortcut.value))
const computedNode=computed(()=>model.value.stages[completed.value-1])
const candidates=computed(()=>{
  const node=computedNode.value
  return (model.value.graph[node]||[]).map(([name,cost])=>({
    name,cost,tail:model.value.values[name],total:cost+model.value.values[name],
  }))
})
const slacks=computed(()=>potentialSlacks(model.value.graph,potentials.value))
const feasible=computed(()=>slacks.value.every(edge=>edge.slack>=-1e-9))
const nodes={S:[42,104],A:[153,44],B:[253,173],T:[357,104]}
const labels={'S-A':[90,50],'S-B':[141,166],'A-B':[214,104],'A-T':[265,47],'B-T':[328,166]}
const edges=computed(()=>slacks.value.map(edge=>{
  const p=nodes[edge.from],q=nodes[edge.to],dx=q[0]-p[0],dy=q[1]-p[1],length=Math.hypot(dx,dy)
  return {...edge,x1:p[0]+18*dx/length,y1:p[1]+18*dy/length,x2:q[0]-18*dx/length,y2:q[1]-18*dy/length,label:labels[edge.from+'-'+edge.to]}
}))
const costView=ref(makeView({x0:0.5,x1:5.5,y0:-1,y1:1,width:400,height:360,pad:36}))
const costAxisY=-5/6
const costHandle=computed(()=>[shortcut.value,costAxisY])
const costDrag=createDragger(costSvg,costView,(_,p)=>{shortcut.value=Math.max(1,Math.min(5,Math.round(p[0]*10)/10));completed.value=0},{step:0.1})
const potentialView=ref(makeView({x0:-0.5,x1:2.5,y0:-1,y1:7,width:400,height:350,pad:36}))
const potentialDrag=createDragger(potentialSvg,potentialView,(name,p)=>{
  potentials.value={...potentials.value,[name]:Math.max(0,Math.min(6,Math.round(p[1]*10)/10))}
},{step:0.1})
const names=['S','A','B']
function setCost(value){shortcut.value=value;completed.value=0}
function copyValues(){potentials.value={...model.value.values}}
function nextStage(){completed.value=Math.min(4,completed.value+1)}
function alternate(){setCost(2);potentials.value={S:3,A:2,B:1,T:0}}
</script>

<template>
  <figure class="study-lab" aria-label="Tính Bellman và chứng chỉ thế năng đối ngẫu">
    <figcaption class="lab-title">Giá trị Bellman là một bộ thế năng tối ưu</figcaption>
    <p class="lab-lead">Kéo chấm vàng trên thanh chi phí để đổi cạnh S → B. Tính lùi từng nút theo thứ tự T, B, A, S. Đồ thị đọc các giá trị thế năng ở hình phía dưới để xác định cạnh còn dư hay vi phạm.</p>
    <svg ref="costSvg" viewBox="0 0 400 360" role="group" aria-label="Đồ thị DAG và chi phí cạnh S đến B kéo được"
      @pointermove="costDrag.move" @pointerup="costDrag.end" @pointercancel="costDrag.end" @lostpointercapture="costDrag.end">
      <defs><marker :id="markerId" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10Z" class="potential-arrow" /></marker></defs>
      <g v-for="edge in edges" :key="edge.from+edge.to">
        <line :x1="edge.x1" :y1="edge.y1" :x2="edge.x2" :y2="edge.y2" :marker-end="'url(#'+markerId+')'" class="potential-edge" :class="{'potential-tight':Math.abs(edge.slack)<1e-9,'potential-invalid':edge.slack< -1e-9}" />
        <text :x="edge.label[0]" :y="edge.label[1]" text-anchor="middle">{{fmt(edge.cost,1)}}</text>
      </g>
      <g v-for="(position,name) in nodes" :key="name">
        <circle :cx="position[0]" :cy="position[1]" r="17" class="potential-node" />
        <text :x="position[0]" :y="position[1]+6" text-anchor="middle">{{name}}</text>
        <text :x="position[0]" :y="position[1]+39" text-anchor="middle">{{model.stages.indexOf(name)<completed?'V='+fmt(model.values[name],1):'V=?'}}</text>
      </g>
      <text x="40" y="260">Chi phí S → B</text>
      <line :x1="costView.sx(1)" :x2="costView.sx(5)" :y1="costView.sy(costAxisY)" :y2="costView.sy(costAxisY)" class="lab-axis" />
      <circle :cx="costView.sx(shortcut)" :cy="costView.sy(costAxisY)" r="7" class="lab-dot-warn" />
      <circle :cx="costView.sx(shortcut)" :cy="costView.sy(costAxisY)" r="32" class="lab-handle potential-hit" tabindex="0" role="slider"
        aria-label="Chi phí cạnh S đến B" :aria-valuetext="fmt(shortcut,1)" aria-valuemin="1" aria-valuemax="5"
        @pointerdown="costDrag.start('cost',$event)" @keydown="costDrag.key('cost',costHandle,$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh chi phí bằng nút</summary><LabPointControls :svg="costSvg" axes="x" /></details>
    <p class="lab-lead">Kéo ba thế năng trên các cột S, A, B. Thế năng tại đích T giữ bằng 0. Cạnh xanh có bất đẳng thức chặt, cạnh tím nét đứt còn dư và cạnh đỏ vi phạm.</p>
    <svg ref="potentialSvg" viewBox="0 0 400 350" role="group" aria-label="Ba thế năng nút kéo được"
      @pointermove="potentialDrag.move" @pointerup="potentialDrag.end" @pointercancel="potentialDrag.end" @lostpointercapture="potentialDrag.end">
      <g v-for="(name,i) in names" :key="name">
        <line :x1="potentialView.sx(i)" :x2="potentialView.sx(i)" :y1="potentialView.sy(0)" :y2="potentialView.sy(6)" class="lab-axis" />
        <text :x="potentialView.sx(i)" y="333" text-anchor="middle">{{name}}</text>
        <text :x="potentialView.sx(i)" y="28" text-anchor="middle">{{fmt(potentials[name],1)}}</text>
        <circle :cx="potentialView.sx(i)" :cy="potentialView.sy(potentials[name])" r="7" class="lab-dot-warn" />
        <circle :cx="potentialView.sx(i)" :cy="potentialView.sy(potentials[name])" r="32" class="lab-handle potential-hit" tabindex="0" role="slider"
          :aria-label="'Thế năng tại '+name" :aria-valuetext="fmt(potentials[name],1)" aria-valuemin="0" aria-valuemax="6"
          @pointerdown="potentialDrag.start(name,$event)" @keydown="potentialDrag.key(name,[i,potentials[name]],$event)" />
      </g>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh thế năng bằng nút</summary><LabPointControls :svg="potentialSvg" axes="y" /></details>
    <div class="lab-buttons">
      <button type="button" @click="nextStage">Tính nút kế tiếp</button>
      <button type="button" @click="completed=4">Tính tất cả</button>
      <button type="button" @click="copyValues">Dùng giá trị Bellman làm thế năng</button>
      <button type="button" @click="setCost(3)">Hai đường cùng tối ưu</button>
      <button type="button" @click="alternate">Một bộ thế năng tối ưu khác</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Chi phí S → B = {{fmt(shortcut,1)}}. Thế năng hiện tại vS = {{fmt(potentials.S,1)}}.</p>
      <p v-if="computedNode==='T'">T là đích, nên V(T) = 0.</p>
      <template v-else-if="computedNode">
        <p v-for="option in candidates" :key="option.name">Qua {{option.name}} tốn {{fmt(option.cost,1)}} ngay và {{fmt(option.tail,1)}} cho phần còn lại, tổng {{fmt(option.total,1)}}.</p>
        <p>V({{computedNode}}) = {{fmt(model.values[computedNode],1)}}. Chọn nút {{model.decisions[computedNode].join(' hoặc ')}}.</p>
      </template>
      <p>{{feasible?'Mọi bất đẳng thức thế năng đều thỏa. vS là cận dưới của chi phí đường đi.':'Có bất đẳng thức thế năng bị vi phạm. Bộ số hiện tại chưa cho chứng chỉ cận dưới.'}}</p>
      <p v-if="feasible&&Math.abs(potentials.S-model.values.S)<1e-9">Cận dưới bằng chi phí đường ngắn nhất nên bộ thế năng hiện tại tối ưu.</p>
      <p v-if="shortcut===3&&completed===4">Hai đường S → A → B → T và S → B → T cùng có chi phí 4.</p>
      <p>Độ dư cạnh là cᵤᵥ − vᵤ + vᵥ. Chọn bộ thế năng tối ưu khác để thấy vA có thể nhỏ hơn V(A) mà mục tiêu vS vẫn tối ưu.</p>
    </div>
  </figure>
</template>

<style scoped>
.potential-edge { stroke: var(--tim); stroke-width: 1.5; stroke-dasharray: 4 4; }
.potential-tight { stroke: var(--xanh); stroke-dasharray: none; }
.potential-invalid { stroke: var(--do); stroke-dasharray: 2 3; }
.potential-arrow { fill: var(--ink-3); }
.potential-node { fill: var(--paper); stroke: var(--ink-3); stroke-width: 1.4; }
.potential-hit { fill: transparent !important; stroke: transparent; }
.potential-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
