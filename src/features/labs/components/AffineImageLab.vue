<script setup>
import LabPointControls from './LabPointControls.vue'
import { computed, ref, watch } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import { add, matVec2, lerp, insideConvexPolygon, closestOnSegment } from '../services/convex-geometry.mjs'

// Ảnh của một tập lồi qua f(x) = Ax + b. Bên trái là tập gốc với hai điểm kéo được,
// bên phải là ảnh của tập và ảnh của đoạn nối hai điểm.
const svg = ref(null)
const left = makeView({ x0: -2, x1: 2, y0: -2, y1: 2, width: 360, height: 360, pad: 28 })
const right = computed(() => {
  const extent = Math.max(2, ...image.value.flat().map(Math.abs)) * 1.25
  return makeView({ x0: -extent, x1: extent, y0: -extent, y1: extent, width: 360, height: 360, pad: 28 })
})
const L = p => left.point(p)
const R = p => right.value.point(p)
const viewForDrag = ref(left)
const pts = ref({ p: [-0.8, -0.5], q: [0.9, 0.7] })
const drag = createDragger(svg, viewForDrag, (name, value) => { pts.value = { ...pts.value, [name]: inSet(value) } }, { step: 0.05, snap: 0.01 })
const a11 = ref(1.5), a12 = ref(0.5), a21 = ref(0), a22 = ref(1), b1 = ref(0.5), b2 = ref(0)
const A = computed(() => [[a11.value, a12.value], [a21.value, a22.value]])
const f = x => add(matVec2(A.value, x), [b1.value, b2.value])
const shapes = {
  square: { label: 'Hình vuông [−1, 1]²', pts: [[-1, -1], [1, -1], [1, 1], [-1, 1]] },
  disk: { label: 'Hình tròn đơn vị', pts: Array.from({ length: 72 }, (_, i) => [Math.cos((2 * Math.PI * i) / 72), Math.sin((2 * Math.PI * i) / 72)]) },
  triangle: { label: 'Tam giác', pts: [[-1.2, -1], [1.4, -0.6], [-0.2, 1.3]] }
}
const shape = ref('square')
function inSet(p) {
  if (shape.value === 'disk') { const length = Math.hypot(...p); return length > 1 ? p.map(v => v / length) : p }
  const polygon = shapes[shape.value].pts
  if (insideConvexPolygon(p, polygon)) return p
  return polygon.map((a, i) => closestOnSegment(p, a, polygon[(i+1)%polygon.length])).reduce((a,b) => a.distance < b.distance ? a : b).point
}
watch(shape, () => { pts.value = Object.fromEntries(Object.entries(pts.value).map(([name,p]) => [name,inSet(p)])) })
const image = computed(() => shapes[shape.value].pts.map(f))
const det = computed(() => a11.value * a22.value - a12.value * a21.value)
const midTheta = ref(0.3)
const mid = computed(() => lerp(pts.value.p, pts.value.q, midTheta.value))
const fMid = computed(() => f(mid.value))
const midOfImages = computed(() => lerp(f(pts.value.p), f(pts.value.q), midTheta.value))
</script>

<template>
  <figure class="study-lab" aria-label="Ảnh của một tập lồi qua ánh xạ affine">
    <p class="lab-title">Ánh xạ affine biến đoạn thẳng thành đoạn thẳng</p>
    <p class="lab-lead">Kéo p và q trong tập gốc. Hai hình cập nhật cùng một tổ hợp θp + (1 − θ)q. Trên điện thoại, chúng xếp dọc để giữ nhãn và điểm đủ lớn.</p>
    <div class="lab-pair">
    <svg ref="svg" viewBox="0 0 360 360" role="group" aria-label="Tập gốc với hai điểm p, q kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line x1="28" x2="332" :y1="left.sy(0)" :y2="left.sy(0)" class="lab-axis" /><line :x1="left.sx(0)" :x2="left.sx(0)" y1="28" y2="332" class="lab-axis" />
      <polygon :points="shapes[shape].pts.map(p => L(p).join(',')).join(' ')" class="lab-region" />
      <line :x1="L(pts.p)[0]" :y1="L(pts.p)[1]" :x2="L(pts.q)[0]" :y2="L(pts.q)[1]" class="lab-accent" />
      <circle :cx="L(mid)[0]" :cy="L(mid)[1]" r="6" class="lab-dot-warn" />
      <circle v-for="name in ['p', 'q']" :key="name" :cx="L(pts[name])[0]" :cy="L(pts[name])[1]" r="7" class="lab-dot" />
      <circle v-for="name in ['p', 'q']" :key="'hit'+name" :cx="L(pts[name])[0]" :cy="L(pts[name])[1]" r="34" class="lab-handle point-hit" tabindex="0" role="slider" :aria-label="`Điểm ${name} trong S`" :aria-valuetext="fmtPoint(pts[name])" @pointerdown="drag.start(name, $event)" @keydown="drag.key(name, pts[name], $event)" />
      <text :x="L(pts.p)[0] + 10" :y="L(pts.p)[1] + 18">p</text><text :x="L(pts.q)[0] + 10" :y="L(pts.q)[1] - 8">q</text>
      <text x="12" y="23">Tập gốc S</text>
    </svg>
    <svg viewBox="0 0 360 360" role="img" aria-label="Ảnh f(S) và ảnh của đoạn nối p, q">
      <line x1="28" x2="332" :y1="right.sy(0)" :y2="right.sy(0)" class="lab-axis" /><line :x1="right.sx(0)" :x2="right.sx(0)" y1="28" y2="332" class="lab-axis" />
      <polygon :points="image.map(p => R(p).join(',')).join(' ')" class="lab-region" />
      <line :x1="R(f(pts.p))[0]" :y1="R(f(pts.p))[1]" :x2="R(f(pts.q))[0]" :y2="R(f(pts.q))[1]" class="lab-accent" />
      <circle :cx="R(fMid)[0]" :cy="R(fMid)[1]" r="7" class="lab-dot-warn" />
      <circle :cx="R(f(pts.p))[0]" :cy="R(f(pts.p))[1]" r="5" class="lab-dot" /><circle :cx="R(f(pts.q))[0]" :cy="R(f(pts.q))[1]" r="5" class="lab-dot" />
      <text :x="R(f(pts.p))[0] - 20" :y="R(f(pts.p))[1] + 42" text-anchor="end">f(p)</text><text :x="R(f(pts.q))[0] + 8" :y="R(f(pts.q))[1] - 12">f(q)</text>
      <text x="12" y="23">Ảnh f(S)</text>
    </svg>
    </div>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-controls">
      <label>Tập gốc<select v-model="shape"><option v-for="(item, key) in shapes" :key="key" :value="key">{{ item.label }}</option></select></label>
      <label>θ của điểm vàng: {{ fmt(midTheta) }}<input v-model.number="midTheta" type="range" min="0" max="1" step="0.05" /></label>
      <label>a₁₁ = {{ fmt(a11, 1) }}<input v-model.number="a11" type="range" min="-2" max="2" step="0.1" /></label>
      <label>a₁₂ = {{ fmt(a12, 1) }}<input v-model.number="a12" type="range" min="-2" max="2" step="0.1" /></label>
      <label>a₂₁ = {{ fmt(a21, 1) }}<input v-model.number="a21" type="range" min="-2" max="2" step="0.1" /></label>
      <label>a₂₂ = {{ fmt(a22, 1) }}<input v-model.number="a22" type="range" min="-2" max="2" step="0.1" /></label>
      <label>b₁ = {{ fmt(b1, 1) }}<input v-model.number="b1" type="range" min="-2" max="2" step="0.1" /></label>
      <label>b₂ = {{ fmt(b2, 1) }}<input v-model.number="b2" type="range" min="-2" max="2" step="0.1" /></label>
    </div>
    <div class="lab-buttons"><button type="button" @click="a11=1;a12=0;a21=0;a22=0">Ép thành đoạn thẳng</button><button type="button" @click="a11=0;a12=0;a21=0;a22=0">Ép thành một điểm</button><button type="button" @click="a11=1.5;a12=.5;a21=0;a22=1">Khôi phục A</button></div>
    <div class="lab-readout" role="status">
      <p>A = [[{{ fmt(a11, 1) }}, {{ fmt(a12, 1) }}], [{{ fmt(a21, 1) }}, {{ fmt(a22, 1) }}]], det A = {{ fmt(det) }}{{ Math.abs(det) < 1e-9 ? ': A suy biến, ảnh bị ép thành một đoạn thẳng hoặc một điểm, nhưng vẫn là tập lồi.' : '.' }}</p>
      <p>Điểm vàng trong tập gốc là θp + (1 − θ)q. Ảnh của nó, f(θp + (1 − θ)q) = {{ fmtPoint(fMid) }}, trùng với θf(p) + (1 − θ)f(q) = {{ fmtPoint(midOfImages) }}. Ánh xạ affine giữ nguyên trọng số trên đoạn thẳng.</p>
      <p>Hai đầu mút được giữ trong S khi kéo. Hai hình dùng thang tọa độ riêng, nên kích thước trên màn hình không cho biết trực tiếp tỉ lệ co giãn. Khi A suy biến, đoạn thẳng có thể co thành một điểm.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Chọn hình tròn và thay đổi A. Ảnh luôn có hình gì?</li>
        <li>Đặt a₂₁ = a₂₂ = 0. Ảnh của hình vuông còn là hình hai chiều không?</li>
        <li>Đổi b mà giữ A. Ảnh thay đổi theo cách nào?</li>
      </ol>
    </details>
  </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{font-size:20px;pointer-events:none}
.lab-pair svg{max-height:none}
</style>
