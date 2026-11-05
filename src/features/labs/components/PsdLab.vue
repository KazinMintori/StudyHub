<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import LabPointControls from './LabPointControls.vue'
import MathMatrix from '../../../core/math/components/MathMatrix.vue'
import { eigSym2, isPsd2, isPd2, scale } from '../services/convex-geometry.mjs'

// Ma trận đối xứng X = [[x, y], [y, z]]. Hình vẽ giá trị vᵀXv trên mọi hướng đơn vị v:
// vạch xanh hướng ra ngoài khi giá trị dương, vạch đỏ hướng vào trong khi giá trị âm.
const view = makeView({ x0: -2.6, x1: 2.6, y0: -2, y1: 2, width: 420, height: 324 })
const P = p => view.point(p)
const x = ref(2), y = ref(1), z = ref(1)
const q = v => x.value * v[0] * v[0] + 2 * y.value * v[0] * v[1] + z.value * v[1] * v[1]
const eig = computed(() => eigSym2(x.value, y.value, z.value))
const bars = computed(() => Array.from({ length: 36 }, (_, i) => {
  const t = (2 * Math.PI * i) / 36, v = [Math.cos(t), Math.sin(t)], value = q(v)
  return { from: v, to: scale(1 + 0.22 * value, v), positive: value >= -1e-12 }
}))
const circle = Array.from({ length: 120 }, (_, i) => [Math.cos((2 * Math.PI * i) / 120), Math.sin((2 * Math.PI * i) / 120)])
const psd = computed(() => isPsd2(x.value, y.value, z.value)), pd = computed(() => isPd2(x.value, y.value, z.value))
const det = computed(() => x.value * z.value - y.value * y.value)
const worst = computed(() => eig.value.vectors[1])
const svg=ref(null),direction=ref([Math.sqrt(.75),.5])
const dragView=ref(view)
const drag=createDragger(svg,dragView,(_,p)=>{const length=Math.hypot(...p);if(length>1e-8)direction.value=p.map(v=>v/length)},{step:.05})
</script>

<template>
  <figure class="study-lab" aria-label="Ma trận đối xứng 2x2 và dạng toàn phương của nó">
    <p class="lab-title">Dạng toàn phương vᵀXv trên mọi hướng</p>
    <p class="lab-lead">Kéo v quanh đường tròn đơn vị để chọn một hướng thử. Hình vẽ thêm 36 hướng cách đều để gợi hình dạng. Vạch xanh hướng ra ngoài khi vᵀXv dương, vạch đỏ hướng vào trong khi giá trị âm. Một hướng âm đã đủ để bác bỏ tính PSD.</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="group" aria-label="Đường tròn đơn vị với các vạch thể hiện giá trị dạng toàn phương theo từng hướng và hai hướng riêng" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line :x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :y1="0" :y2="view.height" :x1="view.sx(0)" :x2="view.sx(0)" class="lab-axis" />
      <polygon :points="circle.map(p => P(p).join(',')).join(' ')" class="lab-guide" />
      <line v-for="(b, i) in bars" :key="i" :x1="P(b.from)[0]" :y1="P(b.from)[1]" :x2="P(b.to)[0]" :y2="P(b.to)[1]" :class="b.positive ? 'lab-good' : 'lab-bad'" style="stroke-width: 1.4" />
      <line :x1="P(scale(-1.9, eig.vectors[0]))[0]" :y1="P(scale(-1.9, eig.vectors[0]))[1]" :x2="P(scale(1.9, eig.vectors[0]))[0]" :y2="P(scale(1.9, eig.vectors[0]))[1]" class="lab-accent" style="stroke-width: 1.5" />
      <line :x1="P(scale(-1.9, eig.vectors[1]))[0]" :y1="P(scale(-1.9, eig.vectors[1]))[1]" :x2="P(scale(1.9, eig.vectors[1]))[0]" :y2="P(scale(1.9, eig.vectors[1]))[1]" class="lab-warn" style="stroke-width: 1.5" />
      <text :x="P(scale(1.95, eig.vectors[0]))[0] + 4" :y="Math.max(28,P(scale(1.95, eig.vectors[0]))[1])" class="lab-small">λ₁</text>
      <text :x="P(scale(1.95, eig.vectors[1]))[0] + 4" :y="Math.max(28,P(scale(1.95, eig.vectors[1]))[1])" class="lab-small">λ₂</text>
      <line :x1="P([0,0])[0]" :y1="P([0,0])[1]" :x2="P(direction)[0]" :y2="P(direction)[1]" class="lab-accent"/>
      <circle :cx="P(direction)[0]" :cy="P(direction)[1]" r="8" class="lab-dot-accent" pointer-events="none"/>
      <text :x="P(direction)[0]+12" :y="P(direction)[1]-12">v</text>
      <circle :cx="P(direction)[0]" :cy="P(direction)[1]" r="32" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Hướng thử v trên đường tròn đơn vị" :aria-valuetext="fmtPoint(direction)" @pointerdown="drag.start('v',$event)" @keydown="drag.key('v',direction,$event)"/>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
    <div class="lab-controls">
      <label>x = {{ fmt(x, 1) }}<input v-model.number="x" type="range" min="-2" max="3" step="0.1" /></label>
      <label>y = {{ fmt(y, 1) }}<input v-model.number="y" type="range" min="-2.5" max="2.5" step="0.1" /></label>
      <label>z = {{ fmt(z, 1) }}<input v-model.number="z" type="range" min="-2" max="3" step="0.1" /></label>
    </div>
    <div class="lab-buttons">
      <button type="button" @click="x=1;y=0;z=1">Ma trận đơn vị</button>
      <button type="button" @click="x=1;y=-1;z=1">PSD có phần tử âm</button>
      <button type="button" @click="x=1;y=1.5;z=1">Có một hướng âm</button>
      <button type="button" @click="x=-1;y=0;z=-1">Mọi hướng đều âm</button>
    </div>
    <div class="lab-readout" role="status">
      <p>X = <MathMatrix :rows="[[x,y],[y,z]]" label="Ma trận đối xứng X"/> có trị riêng λ₁ = {{ fmt(eig.values[0]) }} và λ₂ = {{ fmt(eig.values[1]) }}, định thức xz − y² = {{ fmt(det) }}.</p>
      <p>Hướng đang thử v = {{fmtPoint(direction)}}, có vᵀXv = {{fmt(q(direction),4)}}. Một hướng không âm chưa chứng minh ma trận PSD. Hai trị riêng bên trên kiểm tra các giá trị nhỏ nhất và lớn nhất trên mọi hướng đơn vị.</p>
      <p>Ba điều kiện của Ví dụ 2.6: x ≥ 0 <span :class="x >= 0 ? 'is-good' : 'is-bad'">{{ x >= 0 ? 'đúng' : 'sai' }}</span>, z ≥ 0 <span :class="z >= 0 ? 'is-good' : 'is-bad'">{{ z >= 0 ? 'đúng' : 'sai' }}</span>, xz ≥ y² <span :class="det >= -1e-12 ? 'is-good' : 'is-bad'">{{ det >= -1e-12 ? 'đúng' : 'sai' }}</span>.</p>
      <p v-if="pd"><span class="is-good">X xác định dương:</span> mọi vạch đều hướng ra ngoài, vᵀXv &gt; 0 với mọi v ≠ 0.</p>
      <p v-else-if="psd"><span class="is-good">X nửa xác định dương nhưng suy biến:</span> theo hướng {{ fmtPoint(worst) }}, vᵀXv = 0 và vạch biến mất.</p>
      <p v-else><span class="is-bad">X không nửa xác định dương:</span> theo hướng {{ fmtPoint(worst) }}, vᵀXv = {{ fmt(eig.values[1]) }} &lt; 0. Một hướng như vậy là đủ để bác bỏ.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Đặt x = z = 1 rồi kéo y từ 0 lên 1.5. Ở giá trị nào của y thì vạch đỏ đầu tiên xuất hiện, và theo hướng nào?</li>
        <li>Đặt x = z = 1, y = −1. Ma trận có phần tử âm nhưng các vạch ra sao?</li>
        <li>Hướng dài nhất và ngắn nhất của các vạch trùng với đường nào?</li>
      </ol>
    </details>
  </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{pointer-events:none}
svg text, svg .lab-small { font-size: 20px; pointer-events: none; }
</style>
