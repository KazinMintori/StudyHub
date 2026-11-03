<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, makeView, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { project3, unprojectPlane } from '../services/foundation-geometry.mjs'
import { placePointLabels } from '../services/diagram-labels.mjs'

const flatSvg = ref(null), spaceSvg = ref(null)
const space = ref(false)
const point = ref([1.5, 1.5, 0])
const altitude = computed(() => space.value ? 3 : 0)
const anchors = computed(() => [[0,0,0], [4,0,0], [0,4,altitude.value]])
const weights = [1,1,2]
const flat = ref(makeView({ x0: -1, x1: 5, y0: -1, y1: 5, width: 400, height: 350, pad: 38 }))
const camera = { yaw: 30, pitch: 30, scale: 40, origin: [200, 180] }
const project = p => project3([p[0]-2, p[1]-2, p[2]-altitude.value/2], camera)
const spatialView = computed(() => ({
  x0: -0.5, x1: 4.5, y0: -0.5, y1: 4.5,
  toWorld: (x,y) => unprojectPlane([x,y], point.value[2]-altitude.value/2, camera).map(value => value+2)
}))
function move(_, [x,y]) {
  point.value = [Math.max(-0.5,Math.min(4.5,x)), Math.max(-0.5,Math.min(4.5,y)), point.value[2]]
}
const flatDrag = createDragger(flatSvg, flat, move, { step: 0.1, snap: 0.05 })
const spaceDrag = createDragger(spaceSvg, spatialView, move, { step: 0.1, snap: 0.05 })
const squared = computed(() => anchors.value.reduce((sum, p, i) =>
  sum + weights[i] * p.reduce((value, coordinate, j) => value+(point.value[j]-coordinate)**2,0), 0))
const euclidean = computed(() => anchors.value.reduce((sum,p,i) =>
  sum+weights[i]*Math.hypot(...p.map((coordinate,j)=>point.value[j]-coordinate)), 0))
const manhattan = computed(() => anchors.value.reduce((sum,p,i) =>
  sum+weights[i]*p.reduce((value,coordinate,j)=>value+Math.abs(point.value[j]-coordinate),0), 0))
const activeProjection = p => space.value ? project(p) : flat.value.point(p)
const labels = computed(() => placePointLabels(
  anchors.value.map((p,i)=>({key:i,text:'p'+(i+1),point:activeProjection(p),width:28})),
  {width:400,height:350,reserved:[{x:activeProjection(point.value)[0]-10,y:activeProjection(point.value)[1]-10,width:20,height:20}]}
))
function toggleSpace() {
  space.value = !space.value
  point.value = [point.value[0],point.value[1],space.value ? 1.5 : 0]
}
</script>

<template>
  <figure class="study-lab" aria-label="So sánh ba chi phí định vị trong hai và ba chiều">
    <figcaption class="lab-title">Cùng ba điểm neo, ba dạng nghiệm tối ưu</figcaption>
    <p class="lab-lead">Ba neo có trọng số 1, 1 và 2. Kéo điểm vàng để đọc chi phí. Với Manhattan, mọi điểm trên đoạn xanh đều tối ưu trong R², và mọi điểm trên hình chữ nhật xanh đều tối ưu trong R³.</p>
    <svg v-if="!space" ref="flatSvg" viewBox="0 0 400 350" role="group" aria-label="Ba điểm neo và vị trí thử kéo được trong mặt phẳng"
      @pointermove="flatDrag.move" @pointerup="flatDrag.end" @pointercancel="flatDrag.end" @lostpointercapture="flatDrag.end">
      <line :x1="flat.sx(0)" :x2="flat.sx(4.5)" :y1="flat.sy(0)" :y2="flat.sy(0)" class="lab-axis" />
      <line :x1="flat.sx(0)" :x2="flat.sx(0)" :y1="flat.sy(0)" :y2="flat.sy(4.5)" class="lab-axis" />
      <line :x1="flat.sx(0)" :x2="flat.sx(0)" :y1="flat.sy(0)" :y2="flat.sy(4)" class="median-set" />
      <g v-for="(p,i) in anchors" :key="i">
        <line :x1="flat.sx(p[0])" :y1="flat.sy(p[1])" :x2="flat.sx(point[0])" :y2="flat.sy(point[1])" class="lab-guide" />
        <circle :cx="flat.sx(p[0])" :cy="flat.sy(p[1])" r="5" class="lab-dot-accent" />
        <text :x="labels[i].x" :y="labels[i].y" :text-anchor="labels[i].anchor">p{{i+1}}</text>
      </g>
      <circle :cx="flat.sx(point[0])" :cy="flat.sy(point[1])" r="7" class="lab-dot-warn" />
      <circle :cx="flat.sx(point[0])" :cy="flat.sy(point[1])" r="31" class="lab-handle location-hit"
        tabindex="0" role="slider" aria-label="Vị trí thử hai chiều" :aria-valuetext="fmtPoint(point.slice(0,2))"
        @pointerdown="flatDrag.start('point',$event)" @keydown="flatDrag.key('point',point,$event)" />
    </svg>
    <svg v-else ref="spaceSvg" viewBox="0 0 400 350" role="group" aria-label="Ba điểm neo và vị trí thử kéo được trong lát ngang của không gian"
      @pointermove="spaceDrag.move" @pointerup="spaceDrag.end" @pointercancel="spaceDrag.end" @lostpointercapture="spaceDrag.end">
      <polygon :points="[[0,0,0],[0,4,0],[0,4,3],[0,0,3]].map(p=>project(p).join(',')).join(' ')" class="median-face" />
      <g v-for="(p,i) in anchors" :key="i">
        <line :x1="project(p)[0]" :y1="project(p)[1]" :x2="project(point)[0]" :y2="project(point)[1]" class="lab-guide" />
        <circle :cx="project(p)[0]" :cy="project(p)[1]" r="5" class="lab-dot-accent" />
        <text :x="labels[i].x" :y="labels[i].y" :text-anchor="labels[i].anchor">p{{i+1}}</text>
      </g>
      <circle :cx="project(point)[0]" :cy="project(point)[1]" r="7" class="lab-dot-warn" />
      <circle :cx="project(point)[0]" :cy="project(point)[1]" r="31" class="lab-handle location-hit"
        tabindex="0" role="slider" aria-label="Vị trí thử trong lát ngang ba chiều" :aria-valuetext="fmtPoint(point)"
        @pointerdown="spaceDrag.start('point',$event)" @keydown="spaceDrag.key('point',point,$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh vị trí bằng nút</summary><LabPointControls :svg="space ? spaceSvg : flatSvg" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="space" @click="toggleSpace">Đổi R² và R³</button>
      <button type="button" @click="point=[1,2,altitude/2]">Nghiệm toàn phương</button>
      <button type="button" @click="point=[0,4,altitude]">Nghiệm Euclid</button>
      <button type="button" @click="point=[0,2,altitude/2]">Một nghiệm Manhattan</button>
    </div>
    <div v-if="space" class="lab-buttons">
      <button v-for="z in [0,1.5,3]" :key="z" type="button" @click="point=[point[0],point[1],z]">Lát z = {{z}}</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Vị trí {{fmtPoint(space ? point : point.slice(0,2))}}. Tổng bình phương {{fmt(squared,3)}}, tổng Euclid {{fmt(euclidean,3)}}, tổng Manhattan {{fmt(manhattan,3)}}.</p>
      <p v-if="space">Kéo trong hình giữ nguyên z. Ba nút lát đổi tọa độ cao. Tập nghiệm Manhattan có x = 0, y từ 0 đến 4 và z từ 0 đến 3.</p>
      <p v-else>Trong R², nghiệm toàn phương là (1, 2). Nghiệm Euclid là p₃. Tập nghiệm Manhattan có x = 0 và y từ 0 đến 4.</p>
    </div>
  </figure>
</template>

<style scoped>
.median-set { stroke: var(--xanh); stroke-width: 2.2; }
.median-face { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.4; }
.location-hit { fill: transparent !important; stroke: transparent; }
.location-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
