<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, fmt, fmtPoint } from './svg-drag'

// Quy hoạch phân tuyến tính (ví dụ tự đặt của chủ đề 6, Lecture 02):
// f(x) = (x₁ + 2x₂ + 2)/(x₁ + 0.5x₂ + 1) trên X = {x₁ ≥ 1, x₂ ≥ 0, x₁ + x₂ ≤ 6, x₂ ≤ 4}.
// Tập {f = t} trong miền xác định là một tia xuất phát từ điểm xoay P = (−2/3, −2/3), nơi tử và mẫu cùng bằng 0.
// Đỉnh tối ưu: max 11/4 tại (1, 4), min 8/7 tại (6, 0) (kiểm bằng Python). Phép đổi biến y = x/mẫu, z = 1/mẫu.
const C = [1, 2], C0 = 2, E = [1, 0.5], E0 = 1
const num = (x) => C[0] * x[0] + C[1] * x[1] + C0
const den = (x) => E[0] * x[0] + E[1] * x[1] + E0
const f = (x) => num(x) / den(x)
const X = [[1, 0], [6, 0], [2, 4], [1, 4]]
const PIV = [-2 / 3, -2 / 3]
const mode = ref('max'), t = ref(2)
const vals = X.map(f)
const best = computed(() => {
  const target = mode.value === 'max' ? Math.max(...vals) : Math.min(...vals)
  return { value: target, i: vals.findIndex(v => Math.abs(v - target) < 1e-12) }
})
// Phần của X có f ≥ t (cực đại) hoặc f ≤ t (cực tiểu): cắt X bởi nửa mặt phẳng tuyến tính tương ứng.
const g = (x) => (mode.value === 'max' ? 1 : -1) * (num(x) - t.value * den(x))
const clipped = computed(() => {
  const out = []
  for (let i = 0; i < X.length; i++) {
    const p = X[i], q = X[(i + 1) % X.length], gp = g(p), gq = g(q)
    if (gp >= 0) out.push(p)
    if ((gp > 0 && gq < 0) || (gp < 0 && gq > 0)) { const s = gp / (gp - gq); out.push([p[0] + s * (q[0] - p[0]), p[1] + s * (q[1] - p[1])]) }
  }
  return out
})
const view = makeView({ x0: -1.2, x1: 6.8, y0: -1.2, y1: 5.2, width: 460, height: 368 })
const P = (p) => [view.sx(p[0]), view.sy(p[1])]
const clip = `${useId()}-frac-clip`
// Tia {f = t}: hướng d vuông góc với pháp tuyến (c − t e), chọn chiều làm mẫu số dương.
const ray = computed(() => {
  const n = [C[0] - t.value * E[0], C[1] - t.value * E[1]]
  let d = [-n[1], n[0]]
  if (E[0] * d[0] + E[1] * d[1] < 0) d = [-d[0], -d[1]]
  const len = Math.hypot(d[0], d[1]) || 1
  return [PIV, [PIV[0] + (20 * d[0]) / len, PIV[1] + (20 * d[1]) / len]]
})
// Đường mẫu số bằng 0: x₁ = −1 − 0.5x₂.
const denLine = [[0.5, -3], [-5, 8]]
const feasibleNow = computed(() => clipped.value.length > 0)
const yz = (x) => { const d = den(x); return { y: [x[0] / d, x[1] / d], z: 1 / d } }
</script>

<template>
  <figure class="study-lab" aria-label="Quy hoạch phân tuyến tính: các tập mức là tia xuất phát từ một điểm chung">
    <p class="lab-title">Các đường mức quay quanh một điểm</p>
    <p class="lab-lead">Tập các điểm có f(x) = t là một tia xuất phát từ điểm xoay P, nơi tử số và mẫu số cùng bằng 0. Kéo t để xoay tia, và quan sát phần của miền khả thi còn đạt mức t.</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Miền khả thi, điểm xoay, tia mức f bằng t và phần miền đạt mức t">
      <defs><clipPath :id="clip"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath></defs>
      <g :clip-path="`url(#${clip})`">
        <line v-for="k in [0, 1, 2, 3, 4, 5, 6]" :key="`gx${k}`" :x1="view.sx(k)" :x2="view.sx(k)" y1="0" :y2="view.height" class="lab-grid" />
        <line v-for="k in [0, 1, 2, 3, 4, 5]" :key="`gy${k}`" x1="0" :x2="view.width" :y1="view.sy(k)" :y2="view.sy(k)" class="lab-grid" />
        <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
        <line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
        <line :x1="P(denLine[0])[0]" :y1="P(denLine[0])[1]" :x2="P(denLine[1])[0]" :y2="P(denLine[1])[1]" class="lab-bad" style="stroke-width: 1.5; stroke-dasharray: 6 5" />
        <polygon :points="X.map(p => P(p).join(',')).join(' ')" class="lab-region" />
        <polygon v-if="clipped.length >= 3" :points="clipped.map(p => P(p).join(',')).join(' ')" class="lab-good-fill" style="opacity: 0.85" />
        <line :x1="P(ray[0])[0]" :y1="P(ray[0])[1]" :x2="P(ray[1])[0]" :y2="P(ray[1])[1]" class="lab-warn" />
        <circle :cx="P(PIV)[0]" :cy="P(PIV)[1]" r="6" class="lab-dot" />
        <text :x="P(PIV)[0] + 8" :y="P(PIV)[1] + 16" class="lab-small">P</text>
        <circle v-for="(v, i) in X" :key="`v${i}`" :cx="P(v)[0]" :cy="P(v)[1]" :r="i === best.i ? 7 : 4" :class="i === best.i ? 'lab-dot-accent' : 'lab-dot'" />
        <text v-for="(v, i) in X" :key="`t${i}`" :x="P(v)[0] + 8" :y="P(v)[1] - 8" class="lab-small">{{ fmt(vals[i], 3) }}</text>
      </g>
    </svg>
    <p class="lab-legend"><span class="legend-accent">miền khả thi</span><span class="legend-warn">tia f(x) = t</span><span class="legend-good">phần của miền {{ mode === 'max' ? 'có f ≥ t' : 'có f ≤ t' }}</span><span class="legend-bad">mẫu số bằng 0</span></p>
    <div class="lab-controls">
      <label>Mức t = {{ fmt(t, 3) }}<input v-model.number="t" type="range" min="0.6" max="3.6" step="0.005" /></label>
      <label>Bài toán<select v-model="mode"><option value="max">cực đại f</option><option value="min">cực tiểu f</option></select></label>
    </div>
    <div class="lab-buttons"><button type="button" @click="t = best.value">Đặt t bằng giá trị tối ưu</button></div>
    <div class="lab-readout" role="status">
      <p>Giá trị tại bốn đỉnh: {{ X.map((v, i) => `${fmtPoint(v, 0)} → ${fmt(vals[i], 3)}`).join(', ') }}.</p>
      <p v-if="feasibleNow" class="is-good">Có điểm khả thi với f {{ mode === 'max' ? '≥' : '≤' }} {{ fmt(t, 3) }}: phần tô xanh khác rỗng.</p>
      <p v-else class="is-bad">Không điểm khả thi nào có f {{ mode === 'max' ? '≥' : '≤' }} {{ fmt(t, 3) }}.</p>
      <p>Nghiệm {{ mode === 'max' ? 'cực đại' : 'cực tiểu' }}: đỉnh {{ fmtPoint(X[best.i], 0) }} với f = <span class="is-accent">{{ fmt(best.value, 4) }}</span>. Sau phép đổi biến, y = x/(x₁ + 0.5x₂ + 1) = {{ fmtPoint(yz(X[best.i]).y, 3) }} và z = {{ fmt(yz(X[best.i]).z, 3) }}, cho cùng giá trị y₁ + 2y₂ + 2z = {{ fmt(C[0] * yz(X[best.i]).y[0] + C[1] * yz(X[best.i]).y[1] + C0 * yz(X[best.i]).z, 4) }}.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo t từ nhỏ đến lớn. Vì sao tia f = t luôn đi qua cùng một điểm P?</li>
        <li>Tăng t cho tới khi phần tô xanh vừa biến mất. Nó biến mất tại đỉnh nào, và giá trị t lúc đó bằng bao nhiêu?</li>
        <li>Đổi sang cực tiểu và làm lại. Nghiệm có còn ở một đỉnh không?</li>
        <li>Đường nét đứt đỏ là nơi mẫu số bằng 0. Nếu miền khả thi chạm đường ấy, chuyện gì sẽ xảy ra với f?</li>
      </ol>
    </details>
  </figure>
</template>
