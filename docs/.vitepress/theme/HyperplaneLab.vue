<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { add, sub, scale, dot, norm2 } from './convex-geometry.mjs'

// type="halfspace": siêu phẳng aᵀx = b, nửa không gian aᵀx ≤ b, khoảng cách có dấu của một điểm thử.
// type="voronoi": tập các điểm gần a hơn gần b là một nửa không gian.
const props = defineProps({ type: { type: String, default: 'halfspace' } })
const uid = useId()
const svg = ref(null)
const view = ref(makeView({ x0: -5, x1: 5, y0: -3.75, y1: 3.75, width: 440, height: 330 }))
const P = p => view.value.point(p)
const pts = ref({ a: [1.2, 0.9], x: [2.5, 2], p: [-1.5, -0.5], q: [1.5, 1.5], z: [0.5, -2] })
const b = ref(2), b2 = ref(-1), showParallel = ref(false)
const drag = createDragger(svg, view, (name, value) => {
  if (name === 'a' && norm2(value) < 0.3) return
  pts.value = { ...pts.value, [name]: value }
}, { step: 0.1, snap: 0.1 })

function clipLine(p, d) {
  const v = view.value
  let t0 = -1e9, t1 = 1e9
  for (const [dv, lo, hi, pv] of [[d[0], v.x0, v.x1, p[0]], [d[1], v.y0, v.y1, p[1]]]) {
    if (Math.abs(dv) < 1e-12) { if (pv < lo || pv > hi) return null; continue }
    const s = (lo - pv) / dv, e = (hi - pv) / dv
    t0 = Math.max(t0, Math.min(s, e)); t1 = Math.min(t1, Math.max(s, e))
  }
  return t0 <= t1 ? [add(p, scale(t0, d)), add(p, scale(t1, d))] : null
}
// Đa giác của nửa mặt phẳng nᵀx ≤ c trong khung nhìn.
function halfPolygon(n, c) {
  const v = view.value
  let poly = [[v.x0, v.y0], [v.x1, v.y0], [v.x1, v.y1], [v.x0, v.y1]]
  const out = []
  for (let i = 0; i < poly.length; i++) {
    const p = poly[i], q = poly[(i + 1) % poly.length], vp = dot(n, p) - c, vq = dot(n, q) - c
    if (vp <= 0) out.push(p)
    if ((vp < 0 && vq > 0) || (vp > 0 && vq < 0)) out.push(add(p, scale(vp / (vp - vq), sub(q, p))))
  }
  return out
}

// --- halfspace ---
const a = computed(() => pts.value.a)
const na = computed(() => norm2(a.value))
const x0 = computed(() => scale(b.value / (na.value * na.value), a.value))
const dir = computed(() => [-a.value[1] / na.value, a.value[0] / na.value])
const hyper = computed(() => clipLine(x0.value, dir.value))
const hyper2 = computed(() => clipLine(scale(b2.value / (na.value * na.value), a.value), dir.value))
const value = computed(() => dot(a.value, pts.value.x))
const signed = computed(() => (value.value - b.value) / na.value)
const foot = computed(() => sub(pts.value.x, scale(signed.value / na.value, a.value)))
const normalTip = computed(() => add(x0.value, scale(1.4 / na.value, a.value)))

// --- voronoi ---
const vor = computed(() => {
  const p = pts.value.p, q = pts.value.q, n = sub(q, p)
  return { n, c: (dot(q, q) - dot(p, p)) / 2, mid: scale(0.5, add(p, q)) }
})
const vorLine = computed(() => norm2(vor.value.n) < 1e-9 ? null : clipLine(vor.value.mid, [-vor.value.n[1] / norm2(vor.value.n), vor.value.n[0] / norm2(vor.value.n)]))
const zCloser = computed(() => norm2(sub(pts.value.z, pts.value.p)) <= norm2(sub(pts.value.z, pts.value.q)))
const arrow = `${uid}-arrow`
</script>

<template>
  <figure class="study-lab" :aria-label="type === 'halfspace' ? 'Siêu phẳng và nửa không gian' : 'Nửa không gian các điểm gần một điểm hơn'">
    <p class="lab-title">{{ type === 'halfspace' ? 'Siêu phẳng aᵀx = b và nửa không gian aᵀx ≤ b' : 'Những điểm gần p hơn gần q' }}</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" :aria-label="type === 'halfspace' ? 'Đường thẳng aᵀx = b, phần tô là nửa mặt phẳng aᵀx ≤ b, vector pháp tuyến a và điểm thử x' : 'Hai điểm p, q, đường trung trực và nửa mặt phẳng gần p hơn'" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs><marker :id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="lab-arrow-accent" /></marker></defs>
      <line v-for="x in [-4, -3, -2, -1, 1, 2, 3, 4]" :key="`gx${x}`" :x1="view.sx(x)" :x2="view.sx(x)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="y in [-3, -2, -1, 1, 2, 3]" :key="`gy${y}`" :y1="view.sy(y)" :y2="view.sy(y)" x1="0" :x2="view.width" class="lab-grid" />
      <line :x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :y1="0" :y2="view.height" :x1="view.sx(0)" :x2="view.sx(0)" class="lab-axis" />

      <template v-if="type === 'halfspace'">
        <polygon :points="halfPolygon(a, b).map(p => P(p).join(',')).join(' ')" class="lab-region-soft" />
        <line v-if="hyper" :x1="P(hyper[0])[0]" :y1="P(hyper[0])[1]" :x2="P(hyper[1])[0]" :y2="P(hyper[1])[1]" class="lab-accent" />
        <line v-if="showParallel && hyper2" :x1="P(hyper2[0])[0]" :y1="P(hyper2[0])[1]" :x2="P(hyper2[1])[0]" :y2="P(hyper2[1])[1]" class="lab-warn" />
        <line :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P(x0)[0]" :y2="P(x0)[1]" class="lab-guide" />
        <line :x1="P(x0)[0]" :y1="P(x0)[1]" :x2="P(normalTip)[0]" :y2="P(normalTip)[1]" class="lab-accent" :marker-end="`url(#${arrow})`" />
        <line :x1="P(pts.x)[0]" :y1="P(pts.x)[1]" :x2="P(foot)[0]" :y2="P(foot)[1]" class="lab-guide" />
        <circle :cx="P(x0)[0]" :cy="P(x0)[1]" r="5" class="lab-dot" />
        <text :x="P(x0)[0] - 30" :y="P(x0)[1] + 18">x₀</text>
        <circle :cx="P(a)[0]" :cy="P(a)[1]" r="9" class="lab-handle" tabindex="0" role="slider" aria-label="Đầu mút vector pháp tuyến a tính từ gốc" @pointerdown="drag.start('a', $event)" @keydown="drag.key('a', a, $event)" />
        <line :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P(a)[0]" :y2="P(a)[1]" class="lab-line" />
        <text :x="P(a)[0] + 12" :y="P(a)[1] - 8">a</text>
        <circle :cx="P(pts.x)[0]" :cy="P(pts.x)[1]" r="9" class="lab-handle lab-handle-alt" tabindex="0" role="slider" aria-label="Điểm thử x" @pointerdown="drag.start('x', $event)" @keydown="drag.key('x', pts.x, $event)" />
        <text :x="P(pts.x)[0] + 12" :y="P(pts.x)[1] - 8">x</text>
      </template>

      <template v-else>
        <polygon :points="halfPolygon(vor.n, vor.c).map(p => P(p).join(',')).join(' ')" class="lab-region-soft" />
        <line v-if="vorLine" :x1="P(vorLine[0])[0]" :y1="P(vorLine[0])[1]" :x2="P(vorLine[1])[0]" :y2="P(vorLine[1])[1]" class="lab-accent" />
        <line :x1="P(pts.p)[0]" :y1="P(pts.p)[1]" :x2="P(pts.q)[0]" :y2="P(pts.q)[1]" class="lab-guide" />
        <line :x1="P(pts.z)[0]" :y1="P(pts.z)[1]" :x2="P(pts.p)[0]" :y2="P(pts.p)[1]" :class="zCloser ? 'lab-good' : 'lab-line'" />
        <line :x1="P(pts.z)[0]" :y1="P(pts.z)[1]" :x2="P(pts.q)[0]" :y2="P(pts.q)[1]" :class="zCloser ? 'lab-line' : 'lab-bad'" />
        <circle v-for="name in ['p', 'q']" :key="name" :cx="P(pts[name])[0]" :cy="P(pts[name])[1]" r="9" class="lab-handle" tabindex="0" role="slider" :aria-label="`Điểm ${name}`" @pointerdown="drag.start(name, $event)" @keydown="drag.key(name, pts[name], $event)" />
        <text v-for="name in ['p', 'q']" :key="`t${name}`" :x="P(pts[name])[0] + 12" :y="P(pts[name])[1] - 8">{{ name }}</text>
        <circle :cx="P(pts.z)[0]" :cy="P(pts.z)[1]" r="9" class="lab-handle lab-handle-alt" tabindex="0" role="slider" aria-label="Điểm thử z" @pointerdown="drag.start('z', $event)" @keydown="drag.key('z', pts.z, $event)" />
        <text :x="P(pts.z)[0] + 12" :y="P(pts.z)[1] + 18">z</text>
      </template>
    </svg>

    <div v-if="type === 'halfspace'" class="lab-controls">
      <label>b = {{ fmt(b, 1) }}<input v-model.number="b" type="range" min="-4" max="4" step="0.1" /></label>
      <label class="lab-check"><input v-model="showParallel" type="checkbox" /> Thêm siêu phẳng song song aᵀx = b₂</label>
      <label v-if="showParallel">b₂ = {{ fmt(b2, 1) }}<input v-model.number="b2" type="range" min="-4" max="4" step="0.1" /></label>
    </div>
    <div class="lab-readout" role="status">
      <template v-if="type === 'halfspace'">
        <p>a = {{ fmtPoint(a, 1) }}, ‖a‖₂ = {{ fmt(na) }}. Điểm của siêu phẳng gần gốc nhất là x₀ = ba/‖a‖² = {{ fmtPoint(x0) }}, cách gốc |b|/‖a‖₂ = {{ fmt(Math.abs(b) / na) }}.</p>
        <p>Với điểm thử x = {{ fmtPoint(pts.x, 1) }}: aᵀx = {{ fmt(value) }}, nên khoảng cách có dấu (aᵀx − b)/‖a‖₂ = <span :class="signed <= 0 ? 'is-good' : 'is-bad'">{{ fmt(signed) }}</span>. {{ signed <= 1e-9 ? 'x thuộc nửa không gian aᵀx ≤ b (vùng tô).' : 'x nằm ở phía a chỉ tới, ngoài nửa không gian.' }}</p>
        <p v-if="showParallel">Hai siêu phẳng song song cách nhau |b − b₂|/‖a‖₂ = {{ fmt(Math.abs(b - b2) / na) }}.</p>
      </template>
      <template v-else>
        <p>Vùng tô là {z : ‖z − p‖₂ ≤ ‖z − q‖₂}. Nó là nửa mặt phẳng (q − p)ᵀz ≤ (‖q‖² − ‖p‖²)/2, với (q − p) = {{ fmtPoint(vor.n, 1) }} và vế phải {{ fmt(vor.c) }}.</p>
        <p>Điểm thử z cách p một khoảng {{ fmt(norm2(sub(pts.z, pts.p))) }} và cách q một khoảng {{ fmt(norm2(sub(pts.z, pts.q))) }}, nên z <span :class="zCloser ? 'is-good' : 'is-bad'">{{ zCloser ? 'gần p hơn' : 'gần q hơn' }}</span>.</p>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol v-if="type === 'halfspace'">
        <li>Giữ a, tăng b. Siêu phẳng dịch theo hướng nào so với vector a?</li>
        <li>Kéo đầu mút của a cho a dài gấp đôi mà giữ nguyên hướng. Siêu phẳng thay đổi thế nào, và vì sao?</li>
        <li>Đặt x ngay trên đường thẳng. Khoảng cách có dấu khi đó bằng bao nhiêu?</li>
      </ol>
      <ol v-else>
        <li>Kéo p và q lại gần nhau. Đường biên luôn có quan hệ hình học gì với đoạn pq?</li>
        <li>Đặt z trên đường biên và đo hai khoảng cách.</li>
        <li>Với thêm một điểm thứ ba, vùng gần p nhất sẽ là giao của mấy nửa mặt phẳng?</li>
      </ol>
    </details>
  </figure>
</template>
