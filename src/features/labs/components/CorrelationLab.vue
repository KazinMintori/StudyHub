<script setup>
import LabPointControls from './LabPointControls.vue'
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt } from '../controllers/svg-drag.js'
import { project3 } from '../services/foundation-geometry.mjs'

// Lát cắt của tập ma trận tương quan 3×3 (chủ đề 10, Lecture 02). Với ρ₂₃ = c cố định, ma trận
// R = [[1, ρ₁₂, ρ₁₃], [ρ₁₂, 1, c], [ρ₁₃, c, 1]] nửa xác định dương khi và chỉ khi (ρ₁₂, ρ₁₃) nằm trong ellipse
// ρ₁₂² + ρ₁₃² − 2cρ₁₂ρ₁₃ ≤ 1 − c² (đã kiểm bằng Python). Đây là miền khả thi của một LMI theo hai biến.
const c = ref(0.8), pt = ref([0.8, 0.5]), fixRow = ref(true)
// Trị riêng của ma trận đối xứng 3×3 theo công thức lượng giác.
function eig3(A) {
  const p1 = A[0][1] ** 2 + A[0][2] ** 2 + A[1][2] ** 2
  if (p1 < 1e-15) return [A[0][0], A[1][1], A[2][2]].sort((a, b) => a - b)
  const q = (A[0][0] + A[1][1] + A[2][2]) / 3
  const p2 = (A[0][0] - q) ** 2 + (A[1][1] - q) ** 2 + (A[2][2] - q) ** 2 + 2 * p1, p = Math.sqrt(p2 / 6)
  const B = A.map((row, i) => row.map((v, j) => (v - (i === j ? q : 0)) / p))
  const det = B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1]) - B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0]) + B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0])
  const phi = Math.acos(Math.min(1, Math.max(-1, det / 2))) / 3
  const e1 = q + 2 * p * Math.cos(phi), e3 = q + 2 * p * Math.cos(phi + (2 * Math.PI) / 3)
  return [e3, 3 * q - e1 - e3, e1]
}
const R = computed(() => [[1, pt.value[0], pt.value[1]], [pt.value[0], 1, c.value], [pt.value[1], c.value, 1]])
const eigs = computed(() => eig3(R.value))
const determinant = computed(() => {
  const [a,b] = pt.value
  return 1 + 2*a*b*c.value - a*a - b*b - c.value*c.value
})
// The handles keep all three 2×2 principal minors nonnegative.
const psd = computed(() => determinant.value >= -1e-10)
// Khoảng của ρ₁₃ khi ρ₁₂ và ρ₂₃ cố định: ρ₁₂c ± √((1 − ρ₁₂²)(1 − c²)).
const interval = computed(() => {
  const r = pt.value[0], h = Math.sqrt(Math.max(0, (1 - r * r) * (1 - c.value * c.value)))
  return [r * c.value - h, r * c.value + h]
})
const view = ref(makeView({ x0: -1.15, x1: 1.15, y0: -1.15, y1: 1.15, width: 400, height: 400 }))
const svg = ref(null)
const P = (p) => [view.value.sx(p[0]), view.value.sy(p[1])]
const drag = createDragger(svg, view, (_, p) => { pt.value = [Math.max(-1, Math.min(1, p[0])), Math.max(-1, Math.min(1, p[1]))] }, { step: 0.02, snap: 0.01 })
function section(value) {
  if (Math.abs(value) === 1) return [[-1,-value],[1,value]]
  return Array.from({length:97}, (_, i) => {
    const angle = i*Math.PI/48
    const major = Math.sqrt(1+value)*Math.cos(angle)
    const minor = Math.sqrt(1-value)*Math.sin(angle)
    return [(major+minor)/Math.SQRT2,(major-minor)/Math.SQRT2]
  })
}
const ellipse = computed(() => section(c.value).map(P).join(' '))
const space = ref(null)
const rail = ref(makeView({x0:-1,x1:1,y0:0,y1:1,width:400,height:410,pad:40}))
const moveSlice = createDragger(space,rail,(_,p)=>{c.value=p[0]}, {step:.02,snap:.01})
const scene = p => project3(p,{yaw:32,pitch:25,scale:96,origin:[200,166]})
const ring = (value) => section(value).map(p=>scene([...p,value]).join(',')).join(' ')
const rings = [-1,-.75,-.5,-.25,0,.25,.5,.75,1].map(ring)
const plane = computed(()=>[[-1,-1],[1,-1],[1,1],[-1,1]].map(p=>scene([...p,c.value]).join(',')).join(' '))
const selected = computed(()=>scene([...pt.value,c.value]))
function preset(slice, point) { c.value=slice; pt.value=point }
const area = computed(() => Math.PI * Math.sqrt(1 - c.value * c.value))
</script>

<template>
  <figure class="study-lab" aria-label="Lát cắt của tập ma trận tương quan, miền khả thi của một bất đẳng thức ma trận tuyến tính">
    <p class="lab-title">Những bộ hệ số tương quan có thể xảy ra</p>
    <p class="lab-lead">Kéo điểm ở lát R² để đổi ρ₁₂ và ρ₁₃. Kéo chấm trên thước trong hình R³ để đổi ρ₂₃. Hai hình dùng chung bộ hệ số. Các vòng mảnh cho thấy lát cắt đổi hình dạng dọc theo ρ₂₃.</p>
    <div class="lab-pair">
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Hình vuông các hệ số trong khoảng trừ một tới một và ellipse các cặp hợp lệ" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <rect :x="view.sx(-1)" :y="view.sy(1)" :width="view.sx(1) - view.sx(-1)" :height="view.sy(-1) - view.sy(1)" class="lab-region-soft" style="opacity: 0.3" />
      <line v-for="t in [-1, -0.5, 0, 0.5, 1]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="t in [-1, -0.5, 0, 0.5, 1]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
      <text x="380" y="394" text-anchor="end">ρ₁₂</text>
      <text x="9" y="20">ρ₁₃</text>
      <polygon v-if="Math.abs(c)<1" :points="ellipse" class="lab-region" />
      <polyline v-else :points="ellipse" class="slice-line" />
      <template v-if="fixRow">
        <line :x1="view.sx(pt[0])" :x2="view.sx(pt[0])" y1="0" :y2="view.height" class="lab-guide" />
        <line :x1="view.sx(pt[0])" :x2="view.sx(pt[0])" :y1="view.sy(interval[0])" :y2="view.sy(interval[1])" class="lab-warn" style="stroke-width: 5" />
      </template>
      <circle :cx="P(pt)[0]" :cy="P(pt)[1]" r="7" :class="psd?'lab-dot-accent':'lab-dot-bad'"/>
      <circle :cx="P(pt)[0]" :cy="P(pt)[1]" r="30" class="lab-handle hit" tabindex="0" role="slider" aria-label="Cặp hệ số tương quan" :aria-valuetext="`ρ₁₂ = ${fmt(pt[0], 2)}, ρ₁₃ = ${fmt(pt[1], 2)}`" @pointerdown="drag.start('p', $event)" @keydown="drag.key('p', pt, $event)" />
    </svg>
    <svg ref="space" viewBox="0 0 400 410" role="group" aria-label="Miền tương quan R³ và thước kéo lát cắt" @pointermove="moveSlice.move" @pointerup="moveSlice.end" @pointercancel="moveSlice.end" @lostpointercapture="moveSlice.end">
      <text x="22" y="25">Các lát trong R³</text>
      <polygon :points="plane" class="slice-plane"/>
      <polyline v-for="(line,i) in rings" :key="i" :points="line" class="wire"/>
      <polyline :points="ring(c)" class="slice-line"/>
      <circle :cx="selected[0]" :cy="selected[1]" r="7" :class="psd?'lab-dot-accent':'lab-dot-bad'"/>
      <text x="200" y="329" text-anchor="middle">Vị trí lát ρ₂₃</text>
      <line x1="40" x2="360" y1="360" y2="360" class="lab-axis"/>
      <text x="40" y="399" text-anchor="middle">−1</text>
      <text x="360" y="399" text-anchor="middle">1</text>
      <circle :cx="rail.sx(c)" cy="360" r="6" class="lab-dot-accent"/>
      <circle :cx="rail.sx(c)" cy="360" r="29" class="lab-handle hit" role="slider" tabindex="0" aria-label="Vị trí lát rho 23" :aria-valuetext="fmt(c,2)" @pointerdown="moveSlice.start('slice',$event)" @keydown="moveSlice.key('slice',[c,.5],$event)"/>
    </svg>
    </div>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút</summary><LabPointControls :svg="svg"/><LabPointControls :svg="space" axes="x"/></details>
    <p class="lab-legend"><span class="legend-accent">cặp hệ số làm R ⪰ 0</span><span class="legend-guide">hình vuông [−1, 1]² (nhạt)</span><span v-if="fixRow" class="legend-warn">các giá trị ρ₁₃ được phép khi ρ₁₂ cố định</span></p>
    <div class="lab-controls">
      <label class="lab-check"><input v-model="fixRow" type="checkbox" /> Cố định ρ₁₂ và tìm khoảng của ρ₁₃</label>
    </div>
    <div class="lab-buttons">
      <button type="button" @click="preset(0,[.5,.5])">Lát tròn</button>
      <button type="button" @click="preset(.8,[.8,.28])">Biên dưới 0.28</button>
      <button type="button" @click="preset(.5,[.9,-.9])">Ngoài miền PSD</button>
      <button type="button" @click="preset(1,[.6,.6])">Lát ρ₂₃ = 1</button>
      <button type="button" @click="preset(-1,[.6,-.6])">Lát ρ₂₃ = −1</button>
    </div>
    <div class="lab-readout" role="status">
      <p>R có hàng (1, {{ fmt(pt[0], 2) }}, {{ fmt(pt[1], 2) }}), ({{ fmt(pt[0], 2) }}, 1, {{ fmt(c, 2) }}), ({{ fmt(pt[1], 2) }}, {{ fmt(c, 2) }}, 1). Trị riêng: {{ eigs.map(e => fmt(e, 3)).join(', ') }}.</p>
      <p v-if="psd" class="is-good">Mọi trị riêng không âm: đây là một ma trận tương quan hợp lệ.</p>
      <p v-else class="is-bad">Có trị riêng âm: không tồn tại ba biến ngẫu nhiên nào có các hệ số tương quan này, dù từng hệ số đều nằm trong [−1, 1].</p>
      <p v-if="fixRow">Với ρ₁₂ = {{ fmt(pt[0], 2) }} và ρ₂₃ = {{ fmt(c, 2) }}, hai bài toán SDP cực tiểu và cực đại ρ₁₃ cho khoảng <span class="is-accent">[{{ fmt(interval[0], 3) }}, {{ fmt(interval[1], 3) }}]</span>.</p>
      <p>Định thức bằng {{fmt(determinant,4)}}. <template v-if="Math.abs(c)===1">Lát co thành đoạn thẳng ρ₁₃ = {{c===1?'ρ₁₂':'−ρ₁₂'}} và có diện tích 0.</template><template v-else>Diện tích lát là π√(1 − c²) ≈ {{ fmt(area, 3) }}, khoảng {{ fmt((area / 4) * 100, 1) }}% hình vuông.</template></p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Đặt ρ₂₃ = 0.8 và kéo điểm tới ρ₁₂ = 0.8. ρ₁₃ nhỏ nhất có thể là bao nhiêu? Kết quả này nói gì về "tính bắc cầu" của tương quan?</li>
        <li>Đưa ρ₂₃ về 0. Ellipse thành hình gì, và điều kiện R ⪰ 0 khi đó đơn giản thành gì?</li>
        <li>Kéo ρ₂₃ gần 1. Ellipse dẹt lại về đường nào, và vì sao?</li>
        <li>Đặt điểm ở góc (0.9, −0.9) với ρ₂₃ = 0.5. Trị riêng nhỏ nhất bằng bao nhiêu?</li>
      </ol>
    </details>
  </figure>
</template>

<style scoped>
svg text{font-size:18px;pointer-events:none}
.wire,.slice-line{fill:none;stroke:var(--tim);stroke-width:1}
.wire{opacity:.55}
.slice-line{stroke-width:2}
.slice-plane{fill:var(--tim-soft);fill-opacity:.32;stroke:var(--tim);stroke-width:1}
.hit{fill:transparent!important;stroke:transparent;touch-action:none}
.hit:focus-visible{stroke:var(--vang)}
</style>
