<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmtPoint, makeView } from '../controllers/svg-drag.js'
import { minimalIndices } from '../services/convex-geometry.mjs'
import { project3 } from '../services/foundation-geometry.mjs'
import { placePointLabels } from '../services/diagram-labels.mjs'

const plans = [[1,7,5],[3,4,4],[5,3,6],[7,1,3],[4,6,8],[2,8,7],[6,5,1],[1,9,9]]
const dimension = ref(2)
const selected = ref(6)
const weights = ref([1,1])
const thirdWeight = ref(1)
const svg = ref(null)
const flat = makeView({x0:0,x1:10,y0:0,y1:10,width:360,height:330,pad:30})
const control = makeView({x0:0,x1:3,y0:0,y1:3,width:360,height:260,pad:40})
const drag = createDragger(svg,ref(control),(_,point)=>{weights.value=point},{step:.1,snap:.05})
const objectives = computed(()=>plans.map(point=>point.slice(0,dimension.value)))
const pareto = computed(()=>minimalIndices(objectives.value))
const lambda = computed(()=>dimension.value===2?weights.value:[...weights.value,thirdWeight.value])
const weightedValues = computed(()=>objectives.value.map(point=>point.reduce((sum,value,index)=>sum+lambda.value[index]*value,0)))
const hasWeight = computed(()=>lambda.value.some(value=>value>0))
const winners = computed(()=>hasWeight.value?weightedValues.value.map((value,index)=>Math.abs(value-Math.min(...weightedValues.value))<1e-9?index:-1).filter(index=>index>=0):[])
const scene = point=>project3(point.map(value=>value-4),{yaw:32,pitch:28,scale:23,origin:[180,174]})
const plotted = computed(()=>plans.map(point=>dimension.value===2?flat.point(point):scene(point)))
const labels = computed(()=>placePointLabels(plotted.value.map((point,index)=>({key:String(index),text:String.fromCharCode(65+index),point})),{
 width:360,height:330,reserved:[...plotted.value.map(([x,y])=>({x:x-8,y:y-8,width:16,height:16})),{x:0,y:0,width:70,height:28},{x:280,y:300,width:80,height:30}]
}))
const name = index=>String.fromCharCode(65+index)
</script>

<template>
 <figure class="study-lab" aria-label="Các phương án hữu hạn, trội Pareto và vô hướng hóa trong R2 hoặc R3">
  <figcaption class="lab-title">Thêm mục tiêu thứ ba có thể đổi phương án nào là Pareto?</figcaption>
  <p class="lab-lead">Tám phương án A đến H có ba mục tiêu đều cần giảm. Chọn hai hoặc ba mục tiêu, rồi chọn một phương án để đọc tọa độ. Kéo vector trọng số ở hình dưới để xem tổng có trọng số chọn phương án nào.</p>
  <div class="lab-buttons"><button type="button" :aria-pressed="dimension===2" @click="dimension=2">Hai mục tiêu</button><button type="button" :aria-pressed="dimension===3" @click="dimension=3">Ba mục tiêu</button></div>
  <svg viewBox="0 0 360 330" role="img" aria-label="Các giá trị mục tiêu của tám phương án">
   <template v-if="dimension===2">
    <line x1="30" x2="330" y1="300" y2="300" class="lab-axis"/><line x1="30" x2="30" y1="30" y2="300" class="lab-axis"/>
    <text x="331" y="324">F₁</text><text x="5" y="22">F₂</text>
   </template>
   <template v-else>
    <line v-for="(end,index) in [[9.2,0,0],[0,9.2,0],[0,0,8]]" :key="index" :x1="scene([0,0,0])[0]" :y1="scene([0,0,0])[1]" :x2="scene(end)[0]" :y2="scene(end)[1]" class="lab-axis"/>
    <text :x="scene([9.2,0,0])[0]" :y="scene([9.2,0,0])[1]+20" text-anchor="end">F₁</text><text :x="scene([0,9.2,0])[0]-10" :y="scene([0,9.2,0])[1]+20" text-anchor="end">F₂</text><text :x="scene([0,0,8])[0]+10" :y="scene([0,0,8])[1]">F₃</text>
   </template>
   <circle v-for="(point,index) in plotted" :key="index" :cx="point[0]" :cy="point[1]" :r="index===selected?8:5" :class="pareto.includes(index)?'lab-dot-accent':'lab-dot'"/>
   <circle v-for="index in winners" :key="'winner'+index" :cx="plotted[index][0]" :cy="plotted[index][1]" r="10" class="chosen"/>
   <text v-for="(label,index) in labels" :key="index" :x="label.x" :y="label.y" :text-anchor="label.anchor">{{name(Number(index))}}</text>
  </svg>
  <div class="lab-buttons" role="group" aria-label="Chọn phương án"><button v-for="(_,index) in plans" :key="index" type="button" :aria-pressed="selected===index" @click="selected=index">{{name(index)}}</button></div>
  <svg ref="svg" viewBox="0 0 360 260" role="group" aria-label="Hai trọng số đầu kéo được trong mặt phẳng" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <line x1="40" x2="320" y1="220" y2="220" class="lab-axis"/><line x1="40" x2="40" y1="40" y2="220" class="lab-axis"/>
   <line x1="40" y1="220" :x2="control.sx(weights[0])" :y2="control.sy(weights[1])" class="weight-vector"/>
   <text x="323" y="246">λ₁</text><text x="14" y="27">λ₂</text>
   <circle :cx="control.sx(weights[0])" :cy="control.sy(weights[1])" r="6" class="lab-dot-warn"/>
   <circle :cx="control.sx(weights[0])" :cy="control.sy(weights[1])" r="28" class="lab-handle hit" tabindex="0" role="slider" aria-label="Hai trọng số lambda 1 và lambda 2" :aria-valuetext="fmtPoint(weights,3)" @pointerdown="drag.start('weights',$event)" @keydown="drag.key('weights',weights,$event)"/>
  </svg>
  <div v-if="dimension===3" class="lab-buttons"><button v-for="value in [0,1,4]" :key="value" type="button" :aria-pressed="thirdWeight===value" @click="thirdWeight=value">λ₃ = {{value}}</button></div>
  <div class="lab-buttons"><button type="button" @click="weights=[1,0];thirdWeight=0">Chỉ trọng số F₁</button><button type="button" @click="weights=[1,1];thirdWeight=1">Mọi trọng số dương</button></div>
  <details class="lab-tasks"><summary>Điều chỉnh trọng số bằng nút</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-readout" role="status">
   <p>Phương án {{name(selected)}} có mục tiêu {{fmtPoint(objectives[selected],0)}}. {{pareto.includes(selected)?'Đây là một điểm Pareto.':'Có phương án khác trội hơn điểm này.'}}</p>
   <p>Các phương án Pareto là {{pareto.map(name).join(', ')}}. Với trọng số {{fmtPoint(lambda,2)}}, {{hasWeight?'tổng chọn '+winners.map(name).join(', ')+'.':'cần chọn ít nhất một trọng số dương.'}}</p>
   <p>Với hai mục tiêu, B trội hơn G. Khi xét thêm F₃, G đạt giá trị nhỏ nhất ở mục tiêu thứ ba nên trở thành Pareto. Khi chỉ đặt trọng số F₁, A và H cùng tối ưu tổng, dù A trội hơn H.</p>
   <p>Trong hai mục tiêu đầu, C cũng Pareto nhưng mọi tổng với hai trọng số dương đều cho ít nhất một trong hai phương án B, D giá trị nhỏ hơn C. Một điểm Pareto của tập phương án rời rạc có thể bị tổng trọng số bỏ sót.</p>
   <p>Chấm tím đánh dấu Pareto, vòng vàng đánh dấu nghiệm của tổng. Phép so sánh luôn dùng đủ tọa độ, kể cả khi hình R³ bị chiếu lên màn hình.</p>
  </div>
 </figure>
</template>

<style scoped>
svg text{font-size:18px;pointer-events:none}
.chosen{fill:none;stroke:var(--vang);stroke-width:1.7}
.weight-vector{stroke:var(--vang);stroke-width:1.8}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
