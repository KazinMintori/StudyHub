<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {createDragger,fmt,makeView} from '../controllers/svg-drag.js'
import {adaptiveSequence} from '../services/adaptive-sequence.mjs'

const svg=ref(null)
const gradients=ref([2,1,0,-2])
const selected=ref(0)
const view=ref(makeView({x0:-0.65,x1:3.65,y0:-3.1,y1:3.1,width:400,height:360,pad:32}))
const rows=computed(()=>adaptiveSequence(gradients.value))
const row=computed(()=>rows.value[selected.value])
const drag=createDragger(svg,view,(index,[,g])=>{
  selected.value=index
  const value=Math.max(-2.5,Math.min(2.5,g))
  gradients.value=gradients.value.map((previous,i)=>i===index?value:previous)
},{step:0.1})
function preset(values){
  gradients.value=values
  selected.value=1
}
</script>

<template>
  <figure class="study-lab" aria-label="Ký ức gradient của AdaGrad, RMSProp và Adam">
    <figcaption class="lab-title">Cùng gradient hiện tại, lịch sử khác nhau cho bước cập nhật khác nhau</figcaption>
    <p class="lab-lead">Kéo từng chấm theo chiều dọc để đổi gradient đầu vào. Chọn một bước để xem ba phương pháp đọc cùng chuỗi gradient. Mỗi tọa độ của một bài toán nhiều chiều có thể giữ trạng thái riêng như thế này.</p>
    <svg ref="svg" viewBox="0 0 400 360" role="group" aria-label="Bốn gradient đầu vào kéo được"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="32" x2="368" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <text x="16" y="24">gₜ</text>
      <g v-for="(g,i) in gradients" :key="i">
        <line :x1="view.sx(i)" :x2="view.sx(i)" :y1="view.sy(0)" :y2="view.sy(g)" class="adaptive-stem" />
        <text :x="view.sx(i)" y="345" text-anchor="middle">{{i+1}}</text>
        <circle :cx="view.sx(i)" :cy="view.sy(g)" r="6" :class="selected===i?'lab-dot-warn':'lab-dot-accent'" />
        <circle :cx="view.sx(i)" :cy="view.sy(g)" r="31" class="lab-handle adaptive-hit" tabindex="0" role="slider"
          :aria-label="'Gradient ở bước '+(i+1)" :aria-valuetext="fmt(g)" aria-valuemin="-2.5" aria-valuemax="2.5"
          @pointerdown="selected=i; drag.start(i,$event)" @keydown="drag.key(i,[i,g],$event)" />
      </g>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh gradient bằng nút</summary><LabPointControls :svg="svg" axes="y" /></details>
    <div class="lab-buttons">
      <button type="button" @click="preset([2,1,0,-2])">Ví dụ 2 rồi 1</button>
      <button type="button" @click="preset([2,0,0,0])">Một xung rồi im lặng</button>
      <button type="button" @click="preset([2,-2,2,-2])">Đổi dấu liên tục</button>
      <button v-for="(_,i) in gradients" :key="i" type="button" :aria-pressed="selected===i" @click="selected=i">Bước {{i+1}}</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Bước {{row.t}}, g = {{fmt(row.g,4)}}. Tốc độ học 0,1.</p>
      <p>AdaGrad dùng tổng bình phương {{fmt(row.sum,4)}}, cập nhật {{fmt(row.adagrad,5)}}.</p>
      <p>RMSProp dùng trung bình mũ {{fmt(row.rms,4)}}, cập nhật {{fmt(row.rmsprop,5)}}.</p>
      <p>Adam dùng m̂ = {{fmt(row.mean,4)}} và v̂ = {{fmt(row.square,4)}}, cập nhật {{fmt(row.adam,5)}}. Trước hiệu chỉnh, m = {{fmt(row.m,5)}} và v = {{fmt(row.v,5)}}.</p>
      <p>Ở bước có g = 0, quán tính còn lại có thể tiếp tục dời tham số trong Adam. AdaGrad và RMSProp dùng g hiện tại ở tử số.</p>
    </div>
  </figure>
</template>

<style scoped>
.adaptive-stem { stroke: var(--ink-3); stroke-width: 1.5; }
.adaptive-hit { fill: transparent !important; stroke: transparent; }
.adaptive-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
