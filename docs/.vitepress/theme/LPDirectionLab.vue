<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, fmt, fmtPoint } from './svg-drag'

// Hình học của LP (chủ đề 4, Lecture 02): cực tiểu cᵀx trên một đa diện cho bằng đỉnh và tia.
// Đa diện bị chặn: ngũ giác tự đặt. Đa diện không bị chặn: conv{v₁, v₂, v₃} + cone{r_a, r_b}.
// Bài toán không bị chặn dưới khi cᵀr < 0 với một tia r. Nếu không, nghiệm là đỉnh có cᵀv nhỏ nhất,
// và cả một cạnh tối ưu khi c vuông góc với cạnh đó.
const shapes = {
  bounded: { label: 'ngũ giác bị chặn', vertices: [[0.5, 0.5], [3.5, 0.5], [4.5, 2.2], [2.8, 3.8], [0.8, 3.0]], rays: [] },
  unbounded: { label: 'đa diện không bị chặn', vertices: [[0.5, 2.5], [1.5, 0.8], [3.5, 0.5]], rays: [{ from: 0, d: [-0.3, 1] }, { from: 2, d: [1, 0.1] }] }
}
const key = ref('bounded'), angle = ref(225)
const shape = computed(() => shapes[key.value])
const c = computed(() => [Math.cos((angle.value * Math.PI) / 180), Math.sin((angle.value * Math.PI) / 180)])
const dot = (u, v) => u[0] * v[0] + u[1] * v[1]
const TOL = 1e-9
const result = computed(() => {
  const V = shape.value.vertices, cc = c.value
  const badRay = shape.value.rays.find(r => dot(cc, r.d) < -TOL)
  if (badRay) return { status: 'unbounded', ray: badRay }
  const vals = V.map(v => dot(cc, v)), m = Math.min(...vals)
  const best = vals.map((v, i) => [v, i]).filter(([v]) => v <= m + 1e-6).map(([, i]) => i)
  const flatRay = shape.value.rays.find(r => Math.abs(dot(cc, r.d)) <= TOL && best.includes(r.from))
  return { status: 'optimal', value: m, best, flatRay }
})
// Cạnh kề đỉnh tối ưu có hướng gần vuông góc với c nhất, để nút "xoay vuông góc" chọn đúng cạnh.
const nearestEdgeNormal = computed(() => {
  const V = shape.value.vertices
  if (result.value.status !== 'optimal') return null
  const i = result.value.best[0], cand = [], rays = shape.value.rays
  if (key.value === 'bounded') cand.push([V[(i + V.length - 1) % V.length], V[i]], [V[i], V[(i + 1) % V.length]])
  else { if (i > 0) cand.push([V[i - 1], V[i]]); if (i < V.length - 1) cand.push([V[i], V[i + 1]]) }
  for (const r of rays) if (r.from === i) cand.push([V[i], [V[i][0] + r.d[0], V[i][1] + r.d[1]]])
  let bestAngle = null, bestErr = Infinity
  for (const [p, q] of cand) {
    const e = [q[0] - p[0], q[1] - p[1]], len = Math.hypot(...e)
    for (const s of [1, -1]) {
      const n = [s * e[1] / len, -s * e[0] / len]
      // Pháp tuyến n phải làm đỉnh i (và cả cạnh) tối ưu: n·(v − V[i]) ≥ 0 với mọi đỉnh v, và n·r ≥ 0 với mọi tia r.
      if (V.every(v => dot(n, [v[0] - V[i][0], v[1] - V[i][1]]) >= -1e-9) && rays.every(r => dot(n, r.d) >= -1e-9)) {
        const a = (Math.atan2(n[1], n[0]) * 180) / Math.PI, a360 = (a + 360) % 360
        const err = Math.abs(((a360 - angle.value + 540) % 360) - 180)
        if (err < bestErr) { bestErr = err; bestAngle = a360 }
      }
    }
  }
  return bestAngle
})
// Giữ nguyên độ chính xác của góc, để hai đỉnh của cạnh cho đúng cùng một giá trị.
function snapToEdge() { if (nearestEdgeNormal.value !== null) angle.value = nearestEdgeNormal.value }

const view = makeView({ x0: -0.8, x1: 5.6, y0: -0.6, y1: 4.6, width: 460, height: 372 })
const P = (p) => [view.sx(p[0]), view.sy(p[1])]
const clip = `${useId()}-lp-clip`
const regionPts = computed(() => {
  const s = shape.value, V = s.vertices
  if (!s.rays.length) return V.map(v => P(v).join(',')).join(' ')
  const far = 30, [ra, rb] = s.rays
  const pa = [V[ra.from][0] + far * ra.d[0], V[ra.from][1] + far * ra.d[1]]
  const pb = [V[rb.from][0] + far * rb.d[0], V[rb.from][1] + far * rb.d[1]]
  const mid = V[1], q = [mid[0] + far * (ra.d[0] + rb.d[0]), mid[1] + far * (ra.d[1] + rb.d[1])]
  return [pa, ...V, pb, q].map(p => P(p).join(',')).join(' ')
})
// Các đường mức cᵀx = k, cắt theo khung nhìn.
const levelLine = (k) => {
  const cc = c.value, base = [k * cc[0], k * cc[1]], t = [-cc[1], cc[0]]
  return [P([base[0] - 20 * t[0], base[1] - 20 * t[1]]), P([base[0] + 20 * t[0], base[1] + 20 * t[1]])]
}
const levels = computed(() => {
  const vals = shape.value.vertices.map(v => dot(c.value, v))
  const lo = Math.min(...vals) - 1.5, hi = Math.max(...vals) + 1.5, out = []
  for (let k = Math.ceil(lo * 2) / 2; k <= hi; k += 0.5) out.push(k)
  return out
})
const centroid = computed(() => {
  const V = shape.value.vertices
  return [V.reduce((s, v) => s + v[0], 0) / V.length, V.reduce((s, v) => s + v[1], 0) / V.length]
})
const arrowTip = computed(() => [centroid.value[0] - 1.1 * c.value[0], centroid.value[1] - 1.1 * c.value[1]])
const optEdge = computed(() => {
  const r = result.value
  if (r.status !== 'optimal') return null
  const V = shape.value.vertices
  if (r.flatRay) { const v = V[r.flatRay.from]; return [v, [v[0] + 30 * r.flatRay.d[0], v[1] + 30 * r.flatRay.d[1]]] }
  if (r.best.length >= 2) return [V[r.best[0]], V[r.best[1]]]
  return null
})
</script>

<template>
  <figure class="study-lab" aria-label="Hình học của quy hoạch tuyến tính: Đẩy đường mức theo hướng giảm">
    <p class="lab-title">Đẩy đường mức theo hướng −c</p>
    <p class="lab-lead">Mỗi đường nét đứt là một đường mức cᵀx = hằng số, vuông góc với c. Cực tiểu cᵀx nghĩa là đẩy đường mức theo hướng mũi tên −c cho tới khi nó sắp rời khỏi miền khả thi.</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Miền khả thi, các đường mức của hàm mục tiêu, hướng giảm và điểm hoặc cạnh tối ưu">
      <defs><clipPath :id="clip"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath></defs>
      <g :clip-path="`url(#${clip})`">
        <line v-for="t in [0, 1, 2, 3, 4, 5]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
        <line v-for="t in [0, 1, 2, 3, 4]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
        <polygon :points="regionPts" class="lab-region" />
        <line v-for="k in levels" :key="`k${k}`" :x1="levelLine(k)[0][0]" :y1="levelLine(k)[0][1]" :x2="levelLine(k)[1][0]" :y2="levelLine(k)[1][1]" class="lab-guide" style="opacity: 0.55" />
        <template v-if="result.status === 'optimal'">
          <line :x1="levelLine(result.value)[0][0]" :y1="levelLine(result.value)[0][1]" :x2="levelLine(result.value)[1][0]" :y2="levelLine(result.value)[1][1]" class="lab-warn" />
          <line v-if="optEdge" :x1="P(optEdge[0])[0]" :y1="P(optEdge[0])[1]" :x2="P(optEdge[1])[0]" :y2="P(optEdge[1])[1]" class="lab-good" style="stroke-width: 6" />
          <circle v-for="i in result.best" :key="`b${i}`" :cx="P(shape.vertices[i])[0]" :cy="P(shape.vertices[i])[1]" r="7" class="lab-dot-warn" />
        </template>
        <template v-else>
          <line :x1="P(shape.vertices[result.ray.from])[0]" :y1="P(shape.vertices[result.ray.from])[1]" :x2="P([shape.vertices[result.ray.from][0] + 30 * result.ray.d[0], shape.vertices[result.ray.from][1] + 30 * result.ray.d[1]])[0]" :y2="P([shape.vertices[result.ray.from][0] + 30 * result.ray.d[0], shape.vertices[result.ray.from][1] + 30 * result.ray.d[1]])[1]" class="lab-bad" />
        </template>
        <circle v-for="(v, i) in shape.vertices" :key="`v${i}`" :cx="P(v)[0]" :cy="P(v)[1]" r="4" class="lab-dot" />
        <line :x1="P(centroid)[0]" :y1="P(centroid)[1]" :x2="P(arrowTip)[0]" :y2="P(arrowTip)[1]" class="lab-accent" />
        <circle :cx="P(arrowTip)[0]" :cy="P(arrowTip)[1]" r="5" class="lab-dot-accent" />
        <text :x="P(arrowTip)[0] + 8" :y="P(arrowTip)[1] - 6" class="lab-small">−c</text>
      </g>
    </svg>
    <p class="lab-legend"><span class="legend-accent">hướng giảm −c</span><span class="legend-guide">đường mức</span><span class="legend-warn">đường mức tối ưu</span><span class="legend-good">tập nghiệm khi có nhiều nghiệm</span><span class="legend-bad">tia làm hàm giảm mãi</span></p>
    <div class="lab-controls">
      <label>Hướng của c: {{ fmt(angle, 1) }}°<input v-model.number="angle" type="range" min="0" max="359.9" step="0.1" /></label>
      <label>Miền khả thi<select v-model="key"><option v-for="(s, k) in shapes" :key="k" :value="k">{{ s.label }}</option></select></label>
    </div>
    <div class="lab-buttons">
      <button type="button" :disabled="nearestEdgeNormal === null" @click="snapToEdge">Xoay c vuông góc với cạnh kề nghiệm</button>
    </div>
    <div class="lab-readout" role="status">
      <p>c = {{ fmtPoint(c) }}. Bài toán: cực tiểu cᵀx trên {{ shape.label }}.</p>
      <template v-if="result.status === 'optimal'">
        <p v-if="result.flatRay" class="is-good">Giá trị tối ưu {{ fmt(result.value, 3) }}, đạt trên cả một tia xuất phát từ đỉnh {{ fmtPoint(shape.vertices[result.flatRay.from]) }}: c vuông góc với hướng của tia.</p>
        <p v-else-if="result.best.length >= 2" class="is-good">Giá trị tối ưu {{ fmt(result.value, 3) }}, đạt trên cả cạnh nối {{ fmtPoint(shape.vertices[result.best[0]]) }} và {{ fmtPoint(shape.vertices[result.best[1]]) }}: mọi điểm của cạnh đều là nghiệm.</p>
        <p v-else>Nghiệm duy nhất tại đỉnh {{ fmtPoint(shape.vertices[result.best[0]]) }}, giá trị tối ưu <span class="is-accent">{{ fmt(result.value, 3) }}</span>. Hai ràng buộc gặp nhau ở đỉnh này là hai ràng buộc chặt.</p>
      </template>
      <p v-else class="is-bad">Theo tia xuất phát từ {{ fmtPoint(shape.vertices[result.ray.from]) }} với hướng {{ fmtPoint(result.ray.d) }}, ta có cᵀr = {{ fmt(dot(c, result.ray.d), 3) }} &lt; 0: giá trị giảm mãi, bài toán không bị chặn dưới.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Xoay c một vòng. Đỉnh tối ưu nhảy từ đỉnh này sang đỉnh kề, và giữa hai lần nhảy luôn có một hướng làm cả cạnh tối ưu. Bấm nút để tìm hướng ấy.</li>
        <li>Đổi sang đa diện không bị chặn. Với những hướng nào bài toán vẫn có nghiệm? Hãy so các hướng đó với hai tia của đa diện.</li>
        <li>Với đa diện không bị chặn, tìm hướng c làm cả một tia trở thành tập nghiệm. Giá trị tối ưu khi đó có hữu hạn không?</li>
        <li>Vì sao nghiệm không bao giờ nằm hẳn bên trong miền khả thi, trừ khi c = 0?</li>
      </ol>
    </details>
  </figure>
</template>
