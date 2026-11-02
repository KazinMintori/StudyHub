<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { makeView, createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { lineParameter, project3, unprojectPlane } from '../services/foundation-geometry.mjs'

const props = defineProps({ type: { type: String, default: 'segment' } })
const svg = ref(null), radius = ref(0.5), s = ref(0.4), pa = ref(0.3), pb = ref(-0.2), yaw = ref(35)
const segmentView = makeView({ x0: -3.6, x1: 3.6, y0: -18/7, y1: 18/7, width: 420, height: 300 })
const a = [-2, -1], b = [2, 1], length = Math.sqrt(20), unit = [4/length, 2/length]
const camera = computed(() => ({ yaw: yaw.value, pitch: 35, scale: 65, origin: [210, 170] }))
const center = computed(() => props.type === 'segment' ? a.map((v, i) => v + s.value * (b[i]-v)) : [pa.value, pb.value])
const P = (p, z = 0) => props.type === 'segment' ? segmentView.point(p) : project3([...p, z], camera.value)
const view = computed(() => props.type === 'segment' ? segmentView : {
  x0: -1, x1: 1, y0: -1, y1: 1, toWorld: (x, y) => unprojectPlane([x, y], 0, camera.value)
})
const drag = createDragger(svg, view, (_, p) => {
  if (props.type === 'segment') s.value = Math.max(0, Math.min(1, lineParameter(p, a, b)))
  else { pa.value = p[0]; pb.value = p[1] }
}, { step: 0.05, snap: 0.01 })
const margin = computed(() => props.type === 'segment' ? Math.min(s.value, 1-s.value)*length : Math.min(1-Math.abs(pa.value), 1-Math.abs(pb.value)))
const relativeInterior = computed(() => margin.value > 1e-9)
const fits = computed(() => radius.value <= margin.value + 1e-9)
const disk = computed(() => Array.from({ length: 97 }, (_, i) => {
  const angle = 2*Math.PI*i/96
  return P([pa.value+radius.value*Math.cos(angle), pb.value+radius.value*Math.sin(angle)]).join(',')
}).join(' '))
const sphere = computed(() => [0, 1, 2].map(axis => Array.from({ length: 97 }, (_, i) => {
  const t=2*Math.PI*i/96, u=radius.value*Math.cos(t), v=radius.value*Math.sin(t)
  const p=axis===0 ? [pa.value+u,pb.value+v,0] : axis===1 ? [pa.value+u,pb.value,v] : [pa.value,pb.value+u,v]
  return project3(p, camera.value).join(',')
}).join(' ')))
const chord = computed(() => [-1, 1].map(sign => center.value.map((v, i) => v + sign*radius.value*unit[i])))
const poly = points => points.map(p => P(p).join(',')).join(' ')
const axes = [{ to:[2.2,0,0], label:'x₁' }, { to:[0,2.2,0], label:'x₂' }, { to:[0,0,1.6], label:'x₃' }]
function boundary() { if (props.type === 'segment') s.value=0; else pa.value=1 }
function middle() { s.value=0.5; pa.value=0; pb.value=0 }
</script>

<template>
  <figure class="study-lab" :aria-label="type === 'segment' ? 'Nội tương đối của đoạn thẳng trong R²' : 'Nội tương đối của hình vuông phẳng trong R³'">
    <figcaption class="lab-title">{{ type === 'segment' ? 'Ở trong đoạn, nhưng không có phần trong trong R²' : 'Một điểm trong mặt phẳng có thể không là điểm trong trong R³' }}</figcaption>
    <p class="lab-lead">{{ type === 'segment' ? 'Kéo điểm x dọc đoạn. Đĩa quanh x có điểm ra ngoài đường thẳng. Chỉ xét phần giao với đường chứa đoạn thì ta mới kiểm tra được nội tương đối.' : 'Kéo điểm x trên hình vuông. Khối cầu quanh x luôn có điểm ở phía trên và phía dưới mặt phẳng. Phần giao với mặt phẳng mới là lân cận dùng để xét nội tương đối.' }}</p>
    <svg ref="svg" viewBox="0 0 420 300" role="group" aria-label="Tập C, lân cận quanh điểm x kéo được và phần giao với bao affine" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <template v-if="type === 'segment'">
        <line :x1="P([-3.4,-1.7])[0]" :y1="P([-3.4,-1.7])[1]" :x2="P([3.4,1.7])[0]" :y2="P([3.4,1.7])[1]" class="lab-guide" />
        <circle :cx="P(center)[0]" :cy="P(center)[1]" :r="radius*420/7.2" class="lab-region-soft" />
        <circle :cx="P(center)[0]" :cy="P(center)[1]" :r="radius*420/7.2" class="lab-guide" />
        <line :x1="P(a)[0]" :y1="P(a)[1]" :x2="P(b)[0]" :y2="P(b)[1]" class="lab-accent" />
        <line :x1="P(chord[0])[0]" :y1="P(chord[0])[1]" :x2="P(chord[1])[0]" :y2="P(chord[1])[1]" :class="fits ? 'lab-good' : 'lab-bad'" />
        <circle v-for="(p, i) in [a,b]" :key="i" :cx="P(p)[0]" :cy="P(p)[1]" r="5" class="lab-dot" />
        <text :x="P(a)[0]-22" :y="P(a)[1]+23">a</text><text :x="P(b)[0]+8" :y="P(b)[1]-12">b</text><text x="30" y="30">C = [a, b]</text>
      </template>
      <template v-else>
        <polygon :points="poly([[-1.8,-1.6],[1.8,-1.6],[1.8,1.6],[-1.8,1.6]])" class="lab-region-soft" />
        <polygon :points="poly([[-1,-1],[1,-1],[1,1],[-1,1]])" class="lab-region" />
        <g v-for="axis in axes" :key="axis.label"><line :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="project3(axis.to,camera)[0]" :y2="project3(axis.to,camera)[1]" class="lab-axis" /><text :x="project3(axis.to,camera)[0]+5" :y="project3(axis.to,camera)[1]-5">{{ axis.label }}</text></g>
        <circle :cx="P(center)[0]" :cy="P(center)[1]" :r="radius*65" class="lab-guide" />
        <polyline v-for="(ring,i) in sphere" :key="i" :points="ring" class="lab-guide sphere-ring" />
        <polygon :points="disk" :class="fits ? 'lab-good-fill' : 'lab-bad-fill'" />
      </template>
      <circle :cx="P(center)[0]" :cy="P(center)[1]" r="8" class="lab-dot-warn" pointer-events="none" />
      <text :x="P(center)[0]+12" :y="P(center)[1]-12">x</text>
      <circle :cx="P(center)[0]" :cy="P(center)[1]" r="32" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Điểm x trong tập C" :aria-valuetext="fmtPoint(type === 'segment' ? center : [...center,0])" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',center,$event)" />
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" /></details>
    <p class="lab-legend"><span class="legend-accent">Tập C</span><span class="legend-guide">Lân cận trong không gian bao quanh</span><span :class="fits ? 'legend-good' : 'legend-bad'">Phần giao với bao affine</span></p>
    <div class="lab-controls"><label>Bán kính r = {{ fmt(radius) }}<input v-model.number="radius" type="range" min="0.05" :max="type === 'segment' ? 1.2 : 1" step="0.05" /></label><label v-if="type === 'square'">Góc nhìn quanh x₃: {{ yaw }}°<input v-model.number="yaw" type="range" min="-70" max="70" step="5" /></label></div>
    <div class="lab-buttons"><button type="button" @click="boundary">Đưa x ra biên tương đối</button><button type="button" @click="middle">Đưa x về giữa</button><button v-if="relativeInterior" type="button" @click="radius=Math.min(type === 'segment' ? 1.2 : 1, margin/2)">Chọn r nhỏ vừa đủ</button></div>
    <div class="lab-readout" role="status">
      <p>x = {{ fmtPoint(type === 'segment' ? center : [...center,0]) }}. Khoảng cách đến biên tương đối gần nhất bằng {{ fmt(margin) }}.</p>
      <p>{{ relativeInterior ? 'x thuộc nội tương đối: Có một bán kính dương đủ nhỏ.' : 'x thuộc biên tương đối: Mọi bán kính dương đều làm phần giao vượt ra ngoài C.' }}</p>
      <p>{{ fits ? 'Bán kính đang chọn cho phần giao nằm trong C.' : 'Bán kính đang chọn chưa cho phần giao nằm trong C.' }} Một bán kính không đạt chưa đủ để bác bỏ việc x thuộc nội tương đối.</p>
      <p>{{ type === 'segment' ? 'Không có đĩa mở bán kính dương nào nằm trong một đoạn thẳng của R². Do đó, phần trong của C trong R² rỗng.' : 'Không có khối cầu mở bán kính dương nào nằm trong mặt phẳng x₃ = 0. Phần trong của C trong R³ rỗng. Hình là phép chiếu vuông góc. Đường bao nhìn thấy của khối cầu là đường tròn, còn đĩa giao được vẽ thành ellipse.' }}</p>
    </div>
    <details class="lab-tasks"><summary>Thử và giải thích</summary><ol><li>Đưa điểm ra biên rồi giảm r. Vì sao không thể làm phần giao nằm trong C?</li><li>Đưa điểm vào giữa, chọn r lớn rồi giảm r. Điểm có thay đổi việc thuộc nội tương đối không?</li><li>{{ type === 'segment' ? 'Nếu xét cùng đoạn trong chính đường thẳng chứa nó, phần trong thay đổi thế nào?' : 'Xoay hình. Nội tương đối có phụ thuộc góc nhìn trên màn hình không?' }}</li></ol></details>
  </figure>
</template>

<style scoped>
.point-hit { fill: transparent !important; stroke: transparent; }
.point-hit:focus-visible { stroke: var(--vang); }
.sphere-ring { stroke-width: 1; opacity: .45; }
svg text { font-size: 20px; }
</style>
