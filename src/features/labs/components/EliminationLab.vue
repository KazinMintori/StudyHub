<script setup>
import { computed, ref, useId } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { makeView, createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import {clipPolyline,clipSegment} from '../services/svg-clipping.mjs'
import {placePointLabels} from '../services/diagram-labels.mjs'

// Khử một ràng buộc đẳng thức tuyến tính (ví dụ tự đặt của chủ đề 2, Lecture 02).
// f(x) = (x₁ − 2)² + 2(x₂ − 1)², ràng buộc aᵀx = b với a = (cos θ, sin θ).
// Mọi điểm trên đường viết được thành x = x₀ + z·d, x₀ = b·a, d = (−sin θ, cos θ), nên bài toán
// hai biến có ràng buộc trở thành bài toán một biến z không ràng buộc: g(z) = f(x₀ + z d).
const C = [2, 1], Dg = [1, 2]
const f = (p) => Dg[0] * (p[0] - C[0]) ** 2 + Dg[1] * (p[1] - C[1]) ** 2
const deg = ref(45), b = ref(0.71), z = ref(-1.2)
const showGrad = ref(true)
const svg=ref(null),curveSvg=ref(null),arrowId=useId()
const th = computed(() => (deg.value * Math.PI) / 180)
const a = computed(() => [Math.cos(th.value), Math.sin(th.value)])
const d = computed(() => [-Math.sin(th.value), Math.cos(th.value)])
const x0 = computed(() => [b.value * a.value[0], b.value * a.value[1]])
const at = (t) => [x0.value[0] + t * d.value[0], x0.value[1] + t * d.value[1]]
const g = (t) => f(at(t))
// g là parabol theo z: z* = dᵀD(c − x₀) / dᵀDd.
const zStar = computed(() => {
  const dd = d.value, xx = x0.value
  return (Dg[0] * dd[0] * (C[0] - xx[0]) + Dg[1] * dd[1] * (C[1] - xx[1])) / (Dg[0] * dd[0] ** 2 + Dg[1] * dd[1] ** 2)
})
const xStar = computed(() => at(zStar.value))
const fStar = computed(() => f(xStar.value))
const grad = computed(() => [2 * Dg[0] * (xStar.value[0] - C[0]), 2 * Dg[1] * (xStar.value[1] - C[1])])
const nu = computed(() => -(grad.value[0] * a.value[0] + grad.value[1] * a.value[1]))
const cur = computed(() => at(z.value))

const view = makeView({ x0: -5, x1: 5, y0: -5, y1: 5, width: 360, height: 350, pad:28 })
const P = (p) => [view.sx(p[0]), view.sy(p[1])]
const box={x0:28,x1:332,y0:28,y1:322}
const serialize=points=>points.map(point=>point.join(',')).join(' ')
const ellipse = (L) => Array.from({ length: 121 }, (_, i) => {
  const t = (i / 120) * 2 * Math.PI
  return P([C[0] + Math.sqrt(L / Dg[0]) * Math.cos(t), C[1] + Math.sqrt(L / Dg[1]) * Math.sin(t)])
})
const ellipseSegments=L=>clipPolyline(ellipse(L),box).map(serialize)
const levels = [0.5, 1.5, 3, 5, 8, 12]
const lineEnds = computed(() => clipSegment([P(at(-12)),P(at(12))],box))
// Đồ thị nhỏ của g(z) trên đoạn z ∈ [−4, 4].
const Z = [-4, 4]
const gView = computed(() => {
  const ys = Array.from({ length: 161 }, (_, i) => g(Z[0] + (i / 160) * (Z[1] - Z[0])))
  const lo=fStar.value,hi=Math.max(...ys),span=hi-lo
  return makeView({ x0: Z[0], x1: Z[1], y0:lo-.08*span,y1:hi+.08*span,width:360,height:260,pad:30 })
})
const gCurve = computed(() => Array.from({ length: 161 }, (_, i) => {
  const t = Z[0] + (i / 160) * (Z[1] - Z[0])
  return `${gView.value.sx(t)},${gView.value.sy(g(t))}`
}).join(' '))
const arrowEnd = computed(() => {
  const gr=grad.value,length=Math.hypot(...gr)
  return length<1e-10?xStar.value:gr.map((value,i)=>xStar.value[i]+.85*value/length)
})
const mainView=computed(()=>view)
const drag=createDragger(svg,mainView,(_,p)=>{
  z.value=Math.max(-4,Math.min(4,(p[0]-x0.value[0])*d.value[0]+(p[1]-x0.value[1])*d.value[1]))
},{step:.1})
const curveDrag=createDragger(curveSvg,gView,(_,p)=>{z.value=p[0]},{step:.1})
const labels=computed(()=>placePointLabels([
  {key:'base',text:'x₀',point:P(x0.value)},
  {key:'point',text:'x(z)',point:P(cur.value),width:42}
],{width:360,height:350,reserved:[
  ...[C,x0.value,xStar.value,cur.value].map(p=>({x:P(p)[0]-9,y:P(p)[1]-9,width:18,height:18})),
  {x:180,y:0,width:44,height:36},{x:328,y:170,width:32,height:32}
]}))
function example(){deg.value=45;b.value=Math.SQRT1_2;z.value=-1.2}
</script>

<template>
  <figure class="study-lab" aria-label="Khử một ràng buộc đẳng thức tuyến tính bằng cách tham số hóa đường thẳng">
    <p class="lab-title">Đi dọc ràng buộc thay vì giữ ràng buộc</p>
    <p class="lab-lead">Kéo chấm tím trên hình đường mức hoặc trên parabol. Hai điểm cùng biểu diễn một giá trị z, với x = x₀ + z·d. Trên hình đường mức, chuyển động được chiếu lên đường ràng buộc nên điểm luôn khả thi.</p>
    <div class="lab-buttons" role="group" aria-label="Các cấu hình khử ràng buộc">
      <button type="button" @click="example">Ví dụ x₁ + x₂ = 1</button>
      <button type="button" @click="z=zStar">Đưa z tới nghiệm</button>
      <button type="button" @click="b=a[0]*C[0]+a[1]*C[1]">Đi qua nghiệm tự do</button>
      <button type="button" @click="deg=0">Pháp tuyến ngang</button>
      <button type="button" @click="deg=90">Pháp tuyến dọc</button>
    </div>
    <div class="lab-pair">
    <svg ref="svg" viewBox="0 0 360 350" role="group" aria-label="Đường mức ellipse, đường ràng buộc và điểm khả thi kéo trực tiếp" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <defs><marker :id="arrowId" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" class="gradient-head"/></marker></defs>
      <line v-for="t in [-4,-2,2,4]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="28" y2="322" class="lab-grid" />
      <line v-for="t in [-4,-2,2,4]" :key="`gy${t}`" x1="28" x2="332" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line x1="23" x2="337" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="22" y2="326" class="lab-axis" />
      <g v-for="L in levels" :key="L"><polyline v-for="(points,index) in ellipseSegments(L)" :key="index" :points="points" class="contour"/></g>
      <polyline v-for="(points,index) in ellipseSegments(fStar)" :key="index" :points="points" class="lab-warn"/>
      <line v-if="lineEnds" :x1="lineEnds[0][0]" :y1="lineEnds[0][1]" :x2="lineEnds[1][0]" :y2="lineEnds[1][1]" class="constraint" />
      <circle :cx="P(C)[0]" :cy="P(C)[1]" r="4" class="lab-dot" />
      <circle :cx="P(x0)[0]" :cy="P(x0)[1]" r="5" class="lab-dot-hollow" />
      <line v-if="showGrad&&Math.hypot(...grad)>1e-10" :x1="P(xStar)[0]" :y1="P(xStar)[1]" :x2="P(arrowEnd)[0]" :y2="P(arrowEnd)[1]" class="gradient" :marker-end="`url(#${arrowId})`"/>
      <circle :cx="P(xStar)[0]" :cy="P(xStar)[1]" r="6" class="lab-dot-warn" />
      <circle :cx="P(cur)[0]" :cy="P(cur)[1]" r="7" class="lab-dot-accent" />
      <text :x="labels.base.x" :y="labels.base.y" :text-anchor="labels.base.anchor">x₀</text>
      <text :x="labels.point.x" :y="labels.point.y" :text-anchor="labels.point.anchor">x(z)</text>
      <text x="338" :y="view.sy(0)+20">x₁</text><text :x="view.sx(0)+11" y="25">x₂</text>
      <circle :cx="P(cur)[0]" :cy="P(cur)[1]" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Điểm x trên đường ràng buộc" :aria-valuetext="fmt(z,4)" @pointerdown="drag.start('z',$event)" @keydown="drag.key('z',cur,$event)"/>
    </svg>
    <svg ref="curveSvg" viewBox="0 0 360 260" role="group" aria-label="Parabol g theo z với điểm điều chỉnh trực tiếp" @pointermove="curveDrag.move" @pointerup="curveDrag.end" @pointercancel="curveDrag.end" @lostpointercapture="curveDrag.end">
      <line :x1="gView.sx(0)" :x2="gView.sx(0)" y1="26" y2="230" class="lab-axis" />
      <text x="12" y="20">g(z)</text>
      <text v-for="t in [-4, -2, 2, 4]" :key="`zt${t}`" :x="gView.sx(t)" y="251" text-anchor="middle">{{ t }}</text>
      <polyline :points="gCurve" class="lab-line" />
      <circle :cx="gView.sx(zStar)" :cy="gView.sy(fStar)" r="5" class="lab-dot-warn" />
      <circle :cx="gView.sx(z)" :cy="gView.sy(g(z))" r="7" class="lab-dot-accent" />
      <circle :cx="gView.sx(z)" :cy="gView.sy(g(z))" r="27" class="lab-handle hit" tabindex="0" role="slider" aria-label="Tham số z trên parabol" :aria-valuetext="fmt(z,4)" @pointerdown="curveDrag.start('z',$event)" @keydown="curveDrag.key('z',[z,g(z)],$event)"/>
    </svg>
    </div>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/><LabPointControls :svg="curveSvg" axes="x"/></details>
    <p class="lab-legend"><span class="legend-accent">đường ràng buộc và điểm x(z)</span><span class="legend-warn">đường mức qua nghiệm</span><span v-if="showGrad" class="legend-bad">gradient tại nghiệm</span></p>
    <div class="lab-controls">
      <label>Góc của pháp tuyến a: {{ deg }}°<input v-model.number="deg" type="range" min="0" max="179" step="1" /></label>
      <label>Vế phải b = {{ fmt(b, 2) }}<input v-model.number="b" type="range" min="-1.5" max="2.5" step="0.01" /></label>
      <label>Tham số z = {{ fmt(z, 2) }}<input v-model.number="z" type="range" min="-4" max="4" step="0.01" /></label>
      <label class="lab-check"><input v-model="showGrad" type="checkbox" /> Hiện gradient tại nghiệm</label>
    </div>
    <div class="lab-readout" role="status">
      <p>a = {{ fmtPoint(a) }}, x₀ = {{ fmtPoint(x0) }}, d = {{ fmtPoint(d) }}. Điểm x(z) = {{ fmtPoint(cur) }} cho g(z) = {{ fmt(g(z), 3) }}.</p>
      <p>Cực tiểu của parabol: z* = {{ fmt(zStar, 3) }}, nên x* = {{ fmtPoint(xStar, 3) }} và f(x*) = <span class="is-accent">{{ fmt(fStar, 3) }}</span>.</p>
      <p>Với L = f + ν(aᵀx − b), tại x* ta có ∇f = {{ fmtPoint(grad, 3) }} = −ν·a, trong đó ν = {{ fmt(nu, 3) }}. Gradient vuông góc với đường ràng buộc.</p>
      <p>Kiểm tra aᵀx(z) − b = {{fmt(a[0]*cur[0]+a[1]*cur[1]-b,6)}}. Mũi tên đỏ chỉ hướng gradient và đã chuẩn hóa độ dài cho dễ nhìn. Hai hình dùng thang tọa độ riêng, không so độ dốc bằng mắt giữa chúng.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo điểm trực tiếp trên một trong hai hình cho tới khi chấm tím trùng chấm vàng. Lúc đó parabol có gì đặc biệt?</li>
        <li>Bấm “Ví dụ x₁ + x₂ = 1” để đặt b = 1/√2 chính xác. So x* với kết quả tính tay (2/3, 1/3).</li>
        <li>Đổi b để đường thẳng đi qua tâm (2, 1) của các ellipse. Khi đó ν bằng bao nhiêu, và vì sao?</li>
        <li>Xoay góc mà giữ b. Gradient tại nghiệm có bao giờ không vuông góc với đường ràng buộc không?</li>
      </ol>
    </details>
  </figure>
</template>

<style scoped>
svg text{font-size:18px}
.contour{fill:none;stroke:var(--ink-3);stroke-width:1;opacity:.5}
.constraint{stroke:var(--tim);stroke-width:2.4}
.gradient{stroke:var(--do);stroke-width:2}
.gradient-head{fill:var(--do);stroke:none}
svg :is(line,polyline,path,text),svg circle:not(.hit){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
