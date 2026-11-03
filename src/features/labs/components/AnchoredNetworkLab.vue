<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt } from '../controllers/svg-drag.js'

const svg = ref(null), points = ref([0.8, 3.2]), anchored = ref(true)
const view = ref(makeView({ x0: -0.75, x1: 4.75, y0: -1, y1: 1, width: 400, height: 220, pad: 36 }))
const drag = createDragger(svg,view,(name,[x])=>{
  points.value=points.value.map((value,i)=>i===Number(name)?Math.min(4,Math.max(0,x)):value)
},{step:0.1,snap:0.05})
const energy = computed(()=> (points.value[0]-points.value[1])**2 +
  (anchored.value ? points.value[0]**2+(points.value[1]-4)**2 : 0))
const gradient = computed(()=>[
  2*(points.value[0]-points.value[1])+(anchored.value?2*points.value[0]:0),
  2*(points.value[1]-points.value[0])+(anchored.value?2*(points.value[1]-4):0)
])
</script>

<template>
  <figure class="study-lab" aria-label="Mạng hai nút tự do có hoặc không có neo">
    <figcaption class="lab-title">Bỏ neo làm mất nghiệm duy nhất</figcaption>
    <p class="lab-lead">Kéo x₁ và x₂ trên hai hàng để thử vị trí dọc theo cùng một trục. Các đường nối biểu diễn ba số hạng bình phương, mỗi liên kết có trọng số 1.</p>
    <svg ref="svg" viewBox="0 0 400 220" role="group" aria-label="Hai nút có thể kéo dọc theo một trục"
      @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line v-if="anchored" :x1="view.sx(0)" y1="110" :x2="view.sx(points[0])" y2="72" class="network-edge" />
      <line :x1="view.sx(points[0])" y1="72" :x2="view.sx(points[1])" y2="148" class="network-edge" />
      <line v-if="anchored" :x1="view.sx(points[1])" y1="148" :x2="view.sx(4)" y2="110" class="network-edge" />
      <circle v-if="anchored" :cx="view.sx(0)" cy="110" r="5" class="lab-dot-accent" />
      <circle v-if="anchored" :cx="view.sx(4)" cy="110" r="5" class="lab-dot-accent" />
      <text :x="view.sx(0)" y="195" text-anchor="middle">0</text>
      <text :x="view.sx(4)" y="195" text-anchor="middle">4</text>
      <g v-for="(x,i) in points" :key="i">
        <text x="13" :y="i===0 ? 78 : 154">x{{i+1}}</text>
        <circle :cx="view.sx(x)" :cy="i===0 ? 72 : 148" r="7" class="lab-dot-warn" />
        <circle :cx="view.sx(x)" :cy="i===0 ? 72 : 148" r="31" class="lab-handle network-hit"
          tabindex="0" role="slider" :aria-label="'Vị trí nút x' + (i+1)" aria-valuemin="0" aria-valuemax="4"
          :aria-valuenow="x" :aria-valuetext="'x' + (i+1) + ' = ' + fmt(x,3)"
          @pointerdown="drag.start(String(i),$event)" @keydown="drag.key(String(i),[x,0],$event)" />
      </g>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh vị trí bằng nút</summary><LabPointControls :svg="svg" axes="x" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="anchored" @click="anchored=!anchored">Đổi có neo và bỏ neo</button>
      <button type="button" @click="points=anchored ? [4/3,8/3] : [2,2]">Đưa về cân bằng</button>
      <button v-if="!anchored" type="button" @click="points=[3,3]">Tịnh tiến cả hai tới 3</button>
    </div>
    <div class="lab-readout" role="status">
      <p>x₁ = {{fmt(points[0],3)}}, x₂ = {{fmt(points[1],3)}}. Năng lượng {{fmt(energy,4)}}. Gradient ({{gradient.map(x=>fmt(x,3)).join(', ')}}).</p>
      <p v-if="anchored">Ma trận hệ số là [[2, −1], [−1, 2]], xác định dương. Nghiệm cân bằng duy nhất là (4/3, 8/3).</p>
      <p v-else>Ma trận hệ số là [[1, −1], [−1, 1]], suy biến. Mọi x₁ = x₂ đều có năng lượng bằng 0. Hai nút có thể cùng tịnh tiến mà không đổi khoảng cách giữa chúng.</p>
    </div>
  </figure>
</template>

<style scoped>
.network-edge { stroke: var(--ink-3); stroke-width: 1.6; }
.network-hit { fill: transparent !important; stroke: transparent; }
.network-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
