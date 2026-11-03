<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from '../controllers/svg-drag.js'
import LabPointControls from './LabPointControls.vue'

// LP bền vững (ví dụ tự đặt của chủ đề 8, Lecture 02): cực đại x₁ + 2x₂ với aᵢᵀx ≤ bᵢ, trong đó mỗi aᵢ chỉ biết
// thuộc hình tròn tâm āᵢ bán kính ρ. Ràng buộc bền vững āᵢᵀx + ρ‖x‖₂ ≤ bᵢ là ràng buộc nón bậc hai.
// Gốc tọa độ nằm trong miền (mọi bᵢ > 0), nên miền bền vững hình sao theo gốc: theo hướng đơn vị u, điểm biên
// cách gốc s(u) = min bᵢ/(āᵢᵀu + ρ) trên các i có āᵢᵀu + ρ > 0. Nghiệm tìm bằng cách quét u rồi tinh chỉnh.
const A = [[1, 0], [0, 1], [1, 1], [-1, 0], [0, -1]], B = [3, 2, 4, 1, 1], C = [1, 2]
const rho = ref(0.2)
const dot = (u, v) => u[0] * v[0] + u[1] * v[1]
const radius = (u, r) => {
  let s = Infinity
  for (let i = 0; i < A.length; i++) { const d = dot(A[i], u) + r; if (d > 1e-12) s = Math.min(s, B[i] / d) }
  return s
}
const dir = (t) => [Math.cos(t), Math.sin(t)]
const boundary = (r) => Array.from({ length: 721 }, (_, k) => { const u = dir((k / 720) * 2 * Math.PI), s = radius(u, r); return [s * u[0], s * u[1]] })
const optimum = (r) => {
  const val = (t) => { const u = dir(t); return radius(u, r) * dot(C, u) }
  let bt = 0, bv = -Infinity
  for (let k = 0; k < 3600; k++) { const t = (k / 3600) * 2 * Math.PI, v = val(t); if (v > bv) { bv = v; bt = t } }
  // Tinh chỉnh bằng tìm kiếm tỉ lệ vàng quanh góc tốt nhất (hàm theo góc có một đỉnh ở đây).
  let lo = bt - (2 * Math.PI) / 3600, hi = bt + (2 * Math.PI) / 3600
  for (let k = 0; k < 60; k++) { const m1 = lo + (hi - lo) * 0.382, m2 = lo + (hi - lo) * 0.618; if (val(m1) < val(m2)) lo = m1; else hi = m2 }
  const t = (lo + hi) / 2, u = dir(t), s = radius(u, r)
  return { x: [s * u[0], s * u[1]], value: val(t) }
}
const nominal = { x: [2, 2], value: 6 }
const robust = computed(() => optimum(rho.value))
const active = computed(() => {
  const x = robust.value.x, n = Math.hypot(...x)
  return A.map((a, i) => (Math.abs(dot(a, x) + rho.value * n - B[i]) < 2e-3 ? i : -1)).filter(i => i >= 0)
})
const worstViolation = computed(() => {
  const n = Math.hypot(...nominal.x)
  return Math.max(...A.map((a, i) => dot(a, nominal.x) + rho.value * n - B[i]))
})
const view = makeView({ x0: -1.6, x1: 3.6, y0: -1.6, y1: 2.6, width: 460, height: 372 })
const P = (p) => [view.sx(p[0]), view.sy(p[1])]
const svg=ref(null),trial=ref([1.2,1.1]),dragView=ref(view)
const drag=createDragger(svg,dragView,(_,p)=>{trial.value=p},{step:.05,snap:.01})
const radiusSvg = ref(null)
const radiusView = makeView({x0:0,x1:.6,y0:0,y1:1,width:360,height:105,pad:33})
const radiusDrag = createDragger(radiusSvg, ref(radiusView), (_, [next]) => { rho.value = next }, {step:.01,snap:.01})
const trialSlacks=computed(()=>A.map((a,i)=>B[i]-dot(a,trial.value)-rho.value*Math.hypot(...trial.value)))
const pts = (arr) => arr.map(p => P(p).join(',')).join(' ')
const nominalPoly = boundary(0)
const robustPoly = computed(() => boundary(rho.value))
const label = (i) => ['x₁ ≤ 3', 'x₂ ≤ 2', 'x₁ + x₂ ≤ 4', '−x₁ ≤ 1', '−x₂ ≤ 1'][i]
</script>

<template>
  <figure class="study-lab" aria-label="LP bền vững với hệ số bất định trong hình tròn">
    <p class="lab-title">Cái giá của việc an toàn với mọi hệ số</p>
    <p class="lab-lead">Kéo điểm thử x để kiểm tra từng ràng buộc. Miền nhạt là miền danh định. Khi mỗi hệ số aᵢ có thể lệch trong một hình tròn bán kính ρ, miền vững tô đậm giữ những điểm thỏa mọi hệ số có thể.</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="group" aria-label="Miền khả thi danh định, miền vững và điểm thử x kéo được" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <line v-for="t in [-1, 0, 1, 2, 3]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="t in [-1, 0, 1, 2]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
      <polygon :points="pts(nominalPoly)" class="lab-region-soft" style="opacity: 0.45" />
      <polygon :points="pts(robustPoly)" class="lab-region" />
      <circle :cx="P(nominal.x)[0]" :cy="P(nominal.x)[1]" r="6" class="lab-dot-hollow" />
      <circle :cx="P(robust.x)[0]" :cy="P(robust.x)[1]" r="7" class="lab-dot-warn" />
      <line :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P([0.45, 0.9])[0]" :y2="P([0.45, 0.9])[1]" class="lab-accent" />
      <text :x="P([0.45, 0.9])[0] + 6" :y="P([0.45, 0.9])[1]" class="lab-small">c</text>
      <circle :cx="P(trial)[0]" :cy="P(trial)[1]" r="7" :class="trialSlacks.every(v=>v>=-1e-9)?'lab-dot-accent':'lab-dot-bad'"/>
      <circle :cx="P(trial)[0]" :cy="P(trial)[1]" r="35" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Điểm thử x của LP bền vững" :aria-valuetext="fmtPoint(trial)" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',trial,$event)"/>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
    <p class="lab-legend"><span class="legend-accent">miền bền vững, hướng c</span><span class="legend-warn">nghiệm bền vững</span><span class="legend-guide">miền danh nghĩa (nhạt)</span></p>
    <svg ref="radiusSvg" viewBox="0 0 360 105" role="group" aria-label="Thước kéo bán kính bất định" @pointermove="radiusDrag.move" @pointerup="radiusDrag.end" @pointercancel="radiusDrag.end" @lostpointercapture="radiusDrag.end">
      <text x="180" y="22" text-anchor="middle" class="lab-small">Bán kính ρ</text>
      <line x1="33" x2="327" y1="55" y2="55" class="lab-axis"/>
      <text x="33" y="94" text-anchor="middle" class="lab-small">0</text>
      <text x="327" y="94" text-anchor="middle" class="lab-small">0.6</text>
      <circle :cx="radiusView.sx(rho)" cy="55" r="6" class="lab-dot-accent"/>
      <circle :cx="radiusView.sx(rho)" cy="55" r="28" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Bán kính bất định rho" :aria-valuetext="fmt(rho,2)" @pointerdown="radiusDrag.start('rho',$event)" @keydown="radiusDrag.key('rho',[rho,.5],$event)"/>
    </svg>
    <div class="lab-buttons">
      <button type="button" @click="rho=0">Không có bất định</button>
      <button type="button" @click="rho=.2;trial=[2,1.5]">Chứng nhận tại ρ = 0.2</button>
      <button type="button" @click="rho=.6">Bất định lớn</button>
    </div>
    <details class="lab-tasks"><summary>Đổi bán kính bằng nút</summary><LabPointControls :svg="radiusSvg" axes="x"/></details>
    <div class="lab-readout" role="status">
      <p>Điểm thử x = {{fmtPoint(trial)}}. {{trialSlacks.every(v=>v>=-1e-9)?'Điểm khả thi vững.':'Điểm chưa khả thi vững.'}} Độ dư nhỏ nhất bằng {{fmt(Math.min(...trialSlacks),3)}}. Độ dư âm nghĩa là có ràng buộc bị vượt trong trường hợp xấu nhất.</p>
      <p>Nghiệm danh nghĩa (ρ = 0): (2, 2), giá trị x₁ + 2x₂ = 6.</p>
      <p>Quét biên theo hướng cho nghiệm xấp xỉ {{ fmtPoint(robust.x, 3) }} với giá trị <span class="is-accent">{{ fmt(robust.value, 3) }}</span>. Các ràng buộc gần chặt gồm {{ active.map(label).join(', ') || 'không có' }}. Phần lời giảng chứng nhận chính xác giá trị 5 khi ρ = 0.2.</p>
      <p v-if="rho > 0" :class="worstViolation > 1e-9 ? 'is-bad' : ''">Nếu vẫn dùng nghiệm danh nghĩa (2, 2), trong trường hợp xấu nhất có ràng buộc bị vượt {{ fmt(worstViolation, 3) }}, vì số hạng ρ‖x‖₂ = {{ fmt(rho * Math.hypot(2, 2), 3) }}.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Tăng ρ từ 0. Miền bền vững co lại về phía nào nhiều nhất, và vì sao các điểm gần gốc tọa độ ít bị ảnh hưởng?</li>
        <li>Đặt ρ = 0.2 và kiểm tra nghiệm (2, 1.5) bằng tay: hai ràng buộc chặt cho phương trình nào?</li>
        <li>Biên của miền bền vững cong. Vì sao một ràng buộc vốn tuyến tính lại cho biên cong?</li>
        <li>Giá trị tối ưu giảm khi ρ tăng. Đó là cái giá của sự an toàn. Với ρ = 0.5, cái giá ấy là bao nhiêu phần trăm?</li>
      </ol>
    </details>
  </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent;touch-action:none}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{pointer-events:none}
svg .lab-small{font-size:19px}
</style>
