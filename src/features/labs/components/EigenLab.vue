<script setup>
import { computed, ref } from 'vue'
import { makeView, fmt, createDragger } from '../controllers/svg-drag.js'
import LabPointControls from './LabPointControls.vue'

// Cực tiểu trị riêng lớn nhất (chủ đề 11, Lecture 02): A(x) = [[x, ε], [ε, 1 − x]].
// Hai trị riêng là 1/2 ± √((x − 1/2)² + ε²). Hàm λ_max lồi theo x vì là giá trị lớn nhất của họ hàm tuyến tính
// uᵀA(x)u với ‖u‖ = 1. Khi ε = 0 hai trị riêng cắt nhau và λ_max có một góc nhọn, khi ε > 0 chúng "tránh" nhau.
// Bài toán cực tiểu λ_max(A(x)) là SDP: cực tiểu t với tI − A(x) ⪰ 0.
const eps = ref(0.3), x = ref(0)
const lam = (xx, e) => { const r = Math.sqrt((xx - 0.5) ** 2 + e * e); return [0.5 - r, 0.5 + r] }
const cur = computed(() => lam(x.value, eps.value))
const view = computed(() => makeView({ x0: -1, x1: 2, y0: -1.6, y1: 2.3, width: 400, height: 340, pad:32 }))
const svg=ref(null), railSvg=ref(null)
const drag=createDragger(svg,view,(_,next)=>{x.value=next[0]},{step:.05,snap:.01})
const rail=ref(makeView({x0:0,x1:.8,y0:0,y1:1,width:400,height:100,pad:32}))
const dragEps=createDragger(railSvg,rail,(_,next)=>{eps.value=next[0]},{step:.02,snap:.01})
const P = (p) => [view.value.sx(p[0]), view.value.sy(p[1])]
const xs = Array.from({ length: 301 }, (_, i) => -1 + (3 * i) / 300)
const curve = (k) => xs.map(xx => P([xx, lam(xx, eps.value)[k]]).join(',')).join(' ')
// Đường tiếp tuyến dưới (dưới đạo hàm) của λ_max tại x hiện tại: λ_max(y) ≥ λ_max(x) + g(y − x) với g = u₁ᵀA₁u₁.
const slope = computed(() => {
  const r = Math.sqrt((x.value - 0.5) ** 2 + eps.value ** 2)
  return r < 1e-12 ? 0 : (x.value - 0.5) / r
})
const tangent = computed(() => {
  const y0 = cur.value[1], g = slope.value
  const left = g>0 ? Math.max(-1,x.value+(-1.6-y0)/g) : -1
  const right = g<0 ? Math.min(2,x.value+(-1.6-y0)/g) : 2
  return [P([left,y0+g*(left-x.value)]),P([right,y0+g*(right-x.value)])]
})
</script>

<template>
  <figure class="study-lab" aria-label="Trị riêng lớn nhất của một ma trận phụ thuộc affine vào một tham số">
    <p class="lab-title">Trị riêng lớn nhất là một hàm lồi</p>
    <p class="lab-lead">Kéo chấm tím trên đường trị riêng lớn nhất để đổi x. Kéo chấm trên thước ε để đổi phần tử ngoài đường chéo. Khi ε = 0, hai trị riêng gặp nhau tại x = 0.5.</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="group" aria-label="Hai trị riêng và điểm kéo trên đường trị riêng lớn nhất" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line v-for="t in [-1, 0, 1, 2]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="t in [-1, 0, 1, 2]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <text x="18" y="24">Trị riêng</text><text x="372" y="326">x</text>
      <polyline :points="curve(0)" class="lab-line" style="opacity: 0.6" />
      <line :x1="tangent[0][0]" :y1="tangent[0][1]" :x2="tangent[1][0]" :y2="tangent[1][1]" class="lab-guide" />
      <polyline :points="curve(1)" class="lab-accent" />
      <circle :cx="P([0.5, 0.5 + eps])[0]" :cy="P([0.5, 0.5 + eps])[1]" r="6" class="lab-dot-warn" />
      <circle :cx="P([x, cur[1]])[0]" :cy="P([x, cur[1]])[1]" r="7" class="lab-dot-accent" />
      <circle :cx="P([x, cur[0]])[0]" :cy="P([x, cur[0]])[1]" r="5" class="lab-dot" />
      <circle :cx="P([x, cur[1]])[0]" :cy="P([x, cur[1]])[1]" r="29" class="lab-handle hit" role="slider" tabindex="0" aria-label="Tham số x trên đường trị riêng lớn nhất" :aria-valuetext="fmt(x,4)" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',[x,0],$event)"/>
    </svg>
    <svg ref="railSvg" viewBox="0 0 400 100" role="group" aria-label="Thước kéo epsilon" @pointermove="dragEps.move" @pointerup="dragEps.end" @pointercancel="dragEps.end" @lostpointercapture="dragEps.end">
      <text x="200" y="23" text-anchor="middle">ε = {{fmt(eps,2)}}</text>
      <line x1="32" x2="368" y1="53" y2="53" class="lab-axis"/>
      <text x="32" y="90" text-anchor="middle">0</text><text x="368" y="90" text-anchor="middle">0.8</text>
      <circle :cx="rail.sx(eps)" cy="53" r="6" class="lab-dot-accent"/>
      <circle :cx="rail.sx(eps)" cy="53" r="29" class="lab-handle hit" role="slider" tabindex="0" aria-label="Tham số epsilon" :aria-valuetext="fmt(eps,4)" @pointerdown="dragEps.start('epsilon',$event)" @keydown="dragEps.key('epsilon',[eps,.5],$event)"/>
    </svg>
    <p class="lab-legend"><span class="legend-accent">λ_max(A(x))</span><span class="legend-guide">tiếp tuyến dưới tại x</span><span class="legend-warn">cực tiểu của λ_max</span></p>
    <div class="lab-buttons"><button type="button" @click="x=.5;eps=0">Trị riêng gặp nhau</button><button type="button" @click="x=.5;eps=.3">Trị riêng tách nhau</button><button type="button" @click="x=0;eps=.3">Điểm thử x = 0</button></div>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút</summary><LabPointControls :svg="svg" axes="x"/><LabPointControls :svg="railSvg" axes="x"/></details>
    <div class="lab-readout" role="status">
      <p>A(x) có hai trị riêng {{ fmt(cur[0], 3) }} và <span class="is-accent">{{ fmt(cur[1], 3) }}</span>.</p>
      <p>Giá trị nhỏ nhất của λ_max là 1/2 + ε = {{ fmt(0.5 + eps, 3) }}, đạt tại x = 1/2. SDP tương ứng: cực tiểu t với tI − A(x) ⪰ 0.</p>
      <p v-if="eps < 0.005 && Math.abs(x - 0.5) < 0.006" class="is-bad">Tại đây hai trị riêng bằng nhau và λ_max = max(x, 1 − x) có góc nhọn: không có đạo hàm, mọi độ dốc trong [−1, 1] đều cho một tiếp tuyến dưới.</p>
      <p v-else>Độ dốc của λ_max tại x là {{ fmt(slope, 3) }}, và tiếp tuyến nét đứt nằm dưới toàn bộ đường cong, đúng như với mọi hàm lồi.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo x qua lại với ε = 0.3. Hai trị riêng có bao giờ bằng nhau không? Khoảng cách nhỏ nhất giữa chúng là bao nhiêu?</li>
        <li>Đặt ε = 0. Hai đường bây giờ là hai đường thẳng nào, và λ_max có dạng gì tại x = 1/2?</li>
        <li>Đường λ_min ở dưới là hàm lõm. Vì sao, và cực đại λ_min có là bài toán lồi không?</li>
        <li>Tiếp tuyến nét đứt luôn nằm dưới λ_max. Điều đó nói gì về tính lồi?</li>
      </ol>
    </details>
  </figure>
</template>

<style scoped>
svg text{font-size:18px;pointer-events:none}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
