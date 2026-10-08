<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt } from './svg-drag'

// Bài toán người cứu hộ, ví dụ tự đặt của chủ đề 1: người cứu hộ ở A = (0, 40) trên cát, người bị nạn ở
// B = (60, −30) dưới nước, mép nước là trục hoành. Chọn điểm xuống nước P = (x, 0) với 0 ≤ x ≤ 60 để
// T(x) = |AP|/v₁ + |PB|/v₂ nhỏ nhất. T lồi nên T′ tăng, và nghiệm được tìm bằng chia đôi trên T′.
const A = [0, 40], B = [60, -30]
const v1 = ref(5), v2 = ref(1.5)
const x = ref(20)
const showBest = ref(false)
const run = t => Math.hypot(A[1], t - A[0])
const swim = t => Math.hypot(B[1], B[0] - t)
const T = t => run(t) / v1.value + swim(t) / v2.value
const dT = t => (t - A[0]) / (v1.value * run(t)) - (B[0] - t) / (v2.value * swim(t))
const xLine = A[0] + ((B[0] - A[0]) * A[1]) / (A[1] - B[1])

const best = computed(() => {
  let lo = 0, hi = 60
  if (dT(lo) >= 0) return lo
  if (dT(hi) <= 0) return hi
  for (let i = 0; i < 80; i++) { const m = (lo + hi) / 2; if (dT(m) > 0) hi = m; else lo = m }
  return (lo + hi) / 2
})
const state = computed(() => {
  const r = run(x.value), s = swim(x.value)
  const s1 = (x.value - A[0]) / r, s2 = (B[0] - x.value) / s
  return { r, s, tr: r / v1.value, ts: s / v2.value, total: r / v1.value + s / v2.value, s1, s2, th1: (Math.asin(s1) * 180) / Math.PI, th2: (Math.asin(s2) * 180) / Math.PI }
})
const atBest = computed(() => Math.abs(x.value - best.value) < 0.25)
const slope = computed(() => dT(x.value))

// Cảnh bãi biển: cùng tỉ lệ cho hai trục để góc trên hình đúng là góc thật.
const svg = ref(null)
const view = computed(() => makeView({ x0: -14, x1: 74, y0: -36, y1: 44, width: 460, height: 418 }))
const S = p => view.value.point(p)
const drag = createDragger(svg, view, (_, p) => { x.value = Math.min(60, Math.max(0, p[0])) }, { step: 0.5, snap: 0.1 })
const path = (t) => [A, [t, 0], B].map(p => S(p).join(',')).join(' ')
// Cung đánh dấu góc giữa pháp tuyến của mép nước (hướng lên hoặc xuống) và tia từ P tới một điểm.
function arc(c, to, r, up) {
  const dx = to[0] - c[0], dy = to[1] - c[1], len = Math.hypot(dx, dy)
  const u1 = [0, up ? -1 : 1], u2 = [dx / len, dy / len]
  const cross = u1[0] * u2[1] - u1[1] * u2[0]
  if (!len || Math.abs(cross) < 1e-6) return ''
  const a = [c[0] + r * u1[0], c[1] + r * u1[1]], b = [c[0] + r * u2[0], c[1] + r * u2[1]]
  return `M${a[0]},${a[1]} A${r},${r} 0 0 ${cross > 0 ? 1 : 0} ${b[0]},${b[1]}`
}
const arcs = computed(() => {
  const c = S([x.value, 0])
  return { run: arc(c, S(A), 30, true), swim: arc(c, S(B), 30, false), c }
})

// Đồ thị T(x) trên đoạn [0, 60], thang dọc tự co giãn theo hai vận tốc.
// Bố cục dọc: nhãn T ở trên, đường cong trong [26, 132], trục ở 140, số chia ở 158, chú thích trục ở 182.
const PW = 460, PH = 190, AXIS = 140
const grid = Array.from({ length: 241 }, (_, i) => i * 0.25)
const plot = computed(() => {
  const vals = grid.map(T)
  const lo = Math.min(...vals), hi = Math.max(...vals)
  const px = g => 34 + (g / 60) * (PW - 56)
  const py = t => 26 + (1 - (t - lo) / (hi - lo || 1)) * 106
  return { px, py, lo, hi, pts: grid.map((g, i) => `${px(g)},${py(vals[i])}`).join(' ') }
})
</script>

<template>
  <figure class="study-lab" aria-label="Người cứu hộ chọn điểm xuống nước">
    <p class="lab-title">Chạy bao xa rồi mới bơi?</p>
    <p class="lab-lead">Kéo điểm P dọc mép nước. Đồ thị bên dưới cho biết tổng thời gian T(x) ứng với mỗi điểm xuống nước.</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Bãi cát phía trên, mặt nước phía dưới, người cứu hộ A, người bị nạn B, điểm xuống nước P và hai góc so với pháp tuyến" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <!-- Khung rộng hơn tỉ lệ viewBox thì hình được canh giữa: cát và nước kéo dài ra hai bên để không lộ dải trống. -->
      <rect x="-400" y="0" :width="view.width + 800" :height="view.sy(0)" class="lab-sand" />
      <rect x="-400" :y="view.sy(0)" :width="view.width + 800" :height="view.height - view.sy(0)" class="lab-water" />
      <line v-for="g in [0, 10, 20, 30, 40, 50, 60]" :key="`g${g}`" :x1="view.sx(g)" :x2="view.sx(g)" y1="0" :y2="view.height" class="lab-grid" style="opacity: 0.6" />
      <line x1="-400" :x2="view.width + 400" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" style="stroke-width: 2" />
      <text v-for="g in [0, 20, 40, 60]" :key="`t${g}`" :x="view.sx(g) + 4" :y="view.sy(0) - 6" class="lab-small">{{ g }}</text>
      <text :x="view.sx(48)" :y="view.sy(38)" class="lab-small">cát, v₁ = {{ fmt(v1, 1) }} m/s</text>
      <text :x="view.sx(-12)" :y="view.sy(-32)" class="lab-small">nước, v₂ = {{ fmt(v2, 1) }} m/s</text>
      <line :x1="S(A)[0]" :y1="S(A)[1]" :x2="S(B)[0]" :y2="S(B)[1]" class="lab-guide" />
      <polyline v-if="showBest" :points="path(best)" class="lab-good" style="stroke-width: 2.5; opacity: 0.8" />
      <line :x1="arcs.c[0]" :x2="arcs.c[0]" :y1="view.sy(13)" :y2="view.sy(-13)" class="lab-guide" style="stroke-dasharray: 2 4" />
      <path v-if="arcs.run" :d="arcs.run" class="lab-warn" />
      <path v-if="arcs.swim" :d="arcs.swim" class="lab-warn" />
      <text v-if="arcs.run" :x="arcs.c[0] - 26" :y="arcs.c[1] - 36" class="lab-small">θ₁</text>
      <text v-if="arcs.swim" :x="arcs.c[0] + 8" :y="arcs.c[1] + 48" class="lab-small">θ₂</text>
      <polyline :points="path(x)" class="lab-accent" />
      <circle :cx="S(A)[0]" :cy="S(A)[1]" r="7" class="lab-dot" />
      <text :x="S(A)[0] - 22" :y="S(A)[1] + 5">A</text>
      <circle :cx="S(B)[0]" :cy="S(B)[1]" r="7" class="lab-dot-bad" />
      <text :x="S(B)[0] + 12" :y="S(B)[1] + 5">B</text>
      <circle :cx="arcs.c[0]" :cy="arcs.c[1]" r="10" class="lab-handle" tabindex="0" role="slider" aria-label="Điểm xuống nước P" :aria-valuetext="`x = ${fmt(x, 1)} mét`" @pointerdown="drag.start('p', $event)" @keydown="drag.key('p', [x, 0], $event)" />
      <text :x="arcs.c[0] - 26" :y="arcs.c[1] + 24">P</text>
    </svg>
    <p class="lab-legend"><span class="legend-accent">đường đang chọn</span><span class="legend-guide">đoạn thẳng AB</span><span v-if="showBest" class="legend-good">đường nhanh nhất</span><span class="legend-warn">góc với pháp tuyến</span></p>
    <svg :viewBox="`0 0 ${PW} ${PH}`" role="img" aria-label="Đồ thị tổng thời gian T theo vị trí điểm xuống nước x" style="margin-top: var(--space-3)">
      <line x1="34" :x2="PW - 22" :y1="AXIS" :y2="AXIS" class="lab-axis" />
      <text v-for="g in [0, 20, 40, 60]" :key="`p${g}`" :x="plot.px(g) - 6" :y="AXIS + 18" class="lab-small">{{ g }}</text>
      <text x="8" y="16" class="lab-small">T(x), giây</text>
      <text :x="PW / 2" :y="PH - 8" class="lab-small" text-anchor="middle">x, vị trí xuống nước (m)</text>
      <polyline :points="plot.pts" class="lab-line" />
      <line v-if="showBest" x1="34" :x2="PW - 22" :y1="plot.py(T(best))" :y2="plot.py(T(best))" class="lab-guide" />
      <circle v-if="showBest" :cx="plot.px(best)" :cy="plot.py(T(best))" r="6" class="lab-dot-hollow" />
      <line :x1="plot.px(x)" :x2="plot.px(x)" :y1="plot.py(state.total)" :y2="AXIS" class="lab-guide" />
      <circle :cx="plot.px(x)" :cy="plot.py(state.total)" r="7" class="lab-dot-accent" />
    </svg>
    <div class="lab-controls">
      <label>Vận tốc chạy trên cát v₁ = {{ fmt(v1, 1) }} m/s<input v-model.number="v1" type="range" min="1" max="8" step="0.1" /></label>
      <label>Vận tốc bơi v₂ = {{ fmt(v2, 1) }} m/s<input v-model.number="v2" type="range" min="0.5" max="8" step="0.1" /></label>
      <label class="lab-check"><input v-model="showBest" type="checkbox" /> Hiện đường nhanh nhất</label>
    </div>
    <div class="lab-buttons">
      <button type="button" @click="x = xLine">Đi theo đoạn thẳng AB</button>
      <button type="button" @click="x = 60">Bơi ít nhất</button>
      <button type="button" @click="x = best; showBest = true">Tới điểm nhanh nhất</button>
    </div>
    <div class="lab-readout" role="status">
      <p>Xuống nước tại x = {{ fmt(x, 1) }} m. Chạy {{ fmt(state.r, 1) }} m mất {{ fmt(state.tr, 2) }} s, bơi {{ fmt(state.s, 1) }} m mất {{ fmt(state.ts, 2) }} s, tổng cộng <span class="is-accent">T = {{ fmt(state.total, 2) }} s</span>.</p>
      <p>Góc θ₁ ≈ {{ fmt(state.th1, 1) }}°, θ₂ ≈ {{ fmt(state.th2, 1) }}°. Hai tỉ số sin θ₁ / v₁ = {{ fmt(state.s1 / v1, 4) }} và sin θ₂ / v₂ = {{ fmt(state.s2 / v2, 4) }}.</p>
      <p v-if="atBest" class="is-good">Hai tỉ số bằng nhau, tức T′(x) = 0. Đó là định luật khúc xạ Snell, và vì T là hàm lồi nên điểm này nhanh nhất.</p>
      <p v-else-if="slope < 0">Tỉ số thứ nhất nhỏ hơn, nên T′(x) &lt; 0. Dời P sang phải thì quãng chạy dài thêm, nhưng thời gian bơi giảm nhiều hơn thời gian chạy tăng.</p>
      <p v-else>Tỉ số thứ nhất lớn hơn, nên T′(x) &gt; 0. Dời P sang trái sẽ tới nơi sớm hơn.</p>
      <p v-if="showBest">Nhanh nhất: x* = {{ fmt(best, 2) }} m, T* = {{ fmt(T(best), 2) }} s. Đi theo đoạn thẳng AB mất {{ fmt(T(xLine), 2) }} s, chạy tới x = 60 rồi bơi thẳng mất {{ fmt(T(60), 2) }} s.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo P từ trái sang phải và nhìn chấm tím trên đồ thị. T giảm rồi tăng: chỗ đổi chiều nằm ở đâu, và lúc đó hai tỉ số trong khung kết quả ra sao?</li>
        <li>Bấm "Đi theo đoạn thẳng AB" rồi "Bơi ít nhất". Phương án nào nhanh hơn, và cả hai còn chậm hơn điểm nhanh nhất bao nhiêu giây?</li>
        <li>Đặt hai vận tốc bằng nhau. Điểm nhanh nhất rơi vào đâu? Giải thích mà không cần tính.</li>
        <li>Cho bơi nhanh hơn chạy, chẳng hạn v₁ = 1.5 và v₂ = 5. Đường nhanh nhất bây giờ bẻ góc theo chiều nào?</li>
        <li>Đổi vận tốc vài lần, mỗi lần bấm "Tới điểm nhanh nhất". Hai tỉ số sin θ / v có còn bằng nhau không?</li>
      </ol>
    </details>
  </figure>
</template>
