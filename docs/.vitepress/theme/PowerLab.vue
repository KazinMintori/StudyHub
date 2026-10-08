<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, fmt } from './svg-drag'

// Họ hàm lũy thừa x^a trên x > 0. Đạo hàm bậc hai a(a − 1)x^(a − 2) có dấu của a(a − 1),
// nên hàm lồi khi a ≤ 0 hoặc a ≥ 1 và lõm khi 0 ≤ a ≤ 1. Hình nhỏ bên phải vẽ chính parabol a(a − 1).
const a = ref(0.5)
const clip = `${useId()}-power-clip`
const view = makeView({ x0: 0, x1: 3, y0: -0.4, y1: 4, width: 300, height: 260 })
const inset = makeView({ x0: -2, x1: 3, y0: -0.6, y1: 6.5, width: 140, height: 260 })
const f = x => x ** a.value
const curve = computed(() => {
  const pts = []
  for (let i = 1; i <= 300; i++) {
    const x = (3 * i) / 300, y = f(x)
    pts.push([view.sx(x), view.sy(Math.min(Math.max(y, -1), 5))])
  }
  return pts.map(p => p.join(',')).join(' ')
})
const u = 0.4, v = 2.6
const chord = computed(() => [[view.sx(u), view.sy(Math.min(f(u), 5))], [view.sx(v), view.sy(Math.min(f(v), 5))]])
const mid = (u + v) / 2
const gapAtMid = computed(() => (f(u) + f(v)) / 2 - f(mid))
const curvature = computed(() => a.value * (a.value - 1))
const kind = computed(() => {
  const k = curvature.value
  if (Math.abs(k) < 1e-9) return Math.abs(a.value) < 1e-9 ? 'là hằng số, vừa lồi vừa lõm' : 'tuyến tính, vừa lồi vừa lõm'
  return k > 0 ? 'lồi' : 'lõm'
})
const parabola = Array.from({ length: 101 }, (_, i) => { const s = -2 + (5 * i) / 100; return [inset.sx(s), inset.sy(s * (s - 1))].join(',') }).join(' ')
</script>

<template>
  <figure class="study-lab" aria-label="Họ hàm lũy thừa x mũ a trên nửa trục dương">
    <p class="lab-title">Lũy thừa xᵃ: lồi hay lõm tùy số mũ</p>
    <svg viewBox="0 0 460 260" role="img" :aria-label="`Đồ thị x mũ ${fmt(a, 1)} và parabol a(a − 1)`">
      <defs><clipPath :id="clip"><rect x="0" y="0" width="300" height="260" /></clipPath></defs>
      <g :clip-path="`url(#${clip})`">
        <line v-for="x in [1, 2]" :key="`g${x}`" :x1="view.sx(x)" :x2="view.sx(x)" y1="0" y2="260" class="lab-grid" />
        <line x1="0" x2="300" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" y2="260" class="lab-axis" />
        <line x1="0" x2="300" :y1="view.sy(1)" :y2="view.sy(1)" class="lab-grid" />
        <polyline :points="curve" class="lab-line" style="stroke-width: 2.5" />
        <line :x1="chord[0][0]" :y1="chord[0][1]" :x2="chord[1][0]" :y2="chord[1][1]" class="lab-accent" style="stroke-width: 2" />
        <line :x1="view.sx(mid)" :x2="view.sx(mid)" :y1="view.sy(Math.min(f(mid), 5))" :y2="view.sy(Math.min((f(u) + f(v)) / 2, 5))" :class="gapAtMid >= -1e-9 ? 'lab-good' : 'lab-bad'" />
        <text :x="view.sx(1) - 4" :y="view.sy(0) + 16" class="lab-small">1</text>
        <text :x="view.sx(2) - 4" :y="view.sy(0) + 16" class="lab-small">2</text>
      </g>
      <g transform="translate(316, 0)">
        <rect x="0" y="0" width="140" height="260" class="lab-region-soft" style="opacity: 0.3" />
        <rect :x="inset.sx(0)" y="0" :width="inset.sx(1) - inset.sx(0)" height="260" class="lab-bad-fill" style="stroke: none; opacity: 0.5" />
        <line x1="0" x2="140" :y1="inset.sy(0)" :y2="inset.sy(0)" class="lab-axis" />
        <polyline :points="parabola" class="lab-line" />
        <circle :cx="inset.sx(a)" :cy="inset.sy(curvature)" r="5" class="lab-dot-warn" />
        <text x="6" y="16" class="lab-small">a(a − 1)</text>
        <text :x="inset.sx(0) - 4" :y="inset.sy(0) + 16" class="lab-small">0</text>
        <text :x="inset.sx(1) - 4" :y="inset.sy(0) + 16" class="lab-small">1</text>
      </g>
    </svg>
    <div class="lab-controls">
      <label>Số mũ a = {{ fmt(a, 1) }}<input v-model.number="a" type="range" min="-2" max="3" step="0.1" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p>f(x) = x^{{ fmt(a, 1) }}, f''(x) = a(a − 1)x^(a − 2) với a(a − 1) = {{ fmt(curvature, 2) }}. Trên x &gt; 0, hàm <span :class="kind === 'lõm' ? 'is-bad' : 'is-good'">{{ kind }}</span>.</p>
      <p v-if="gapAtMid >= -1e-9">Dây cung nối x = {{ u }} và x = {{ v }}: tại trung điểm, dây cung nằm trên đồ thị một khoảng {{ fmt(gapAtMid, 3) }}.</p>
      <p v-else>Dây cung nối x = {{ u }} và x = {{ v }}: tại trung điểm, đồ thị vượt lên trên dây cung một khoảng {{ fmt(-gapAtMid, 3) }}.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo a từ 3 xuống −2. Hai giá trị nào của a làm hàm đổi từ lồi sang lõm rồi lại sang lồi? Hàm trông thế nào đúng tại hai giá trị đó?</li>
        <li>Vì sao a = −1 (hàm 1/x) và a = 2 (hàm x²) cùng lồi, dù một hàm giảm và một hàm tăng?</li>
        <li>Đặt a = 0.5. Dây cung nằm dưới đồ thị bao nhiêu tại trung điểm?</li>
      </ol>
    </details>
  </figure>
</template>
