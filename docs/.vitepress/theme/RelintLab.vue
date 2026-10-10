<script setup>
import { computed, ref } from 'vue'
import { makeView, fmt } from './svg-drag'

// type="segment": đoạn thẳng trong R², quả cầu (hình tròn) quanh một điểm và phần giao với đường thẳng chứa đoạn.
// type="square": hình vuông nằm trong mặt phẳng x₃ = 0 của R³, vẽ bằng phép chiếu xiên.
const props = defineProps({ type: { type: String, default: 'segment' } })
const r = ref(0.5)

// --- segment ---
const view = makeView({ x0: -3, x1: 3, y0: -2, y1: 2, width: 420, height: 280 })
const A = [-2, -1], B = [2, 1]
const s = ref(0.4)
const len = Math.hypot(B[0] - A[0], B[1] - A[1])
const u = [(B[0] - A[0]) / len, (B[1] - A[1]) / len]
const x = computed(() => [A[0] + s.value * (B[0] - A[0]), A[1] + s.value * (B[1] - A[1])])
const roomLeft = computed(() => s.value * len), roomRight = computed(() => (1 - s.value) * len)
const segInside = computed(() => roomLeft.value >= r.value - 1e-9 && roomRight.value >= r.value - 1e-9)
const chordEnds = computed(() => [[x.value[0] - r.value * u[0], x.value[1] - r.value * u[1]], [x.value[0] + r.value * u[0], x.value[1] + r.value * u[1]]])
const P = p => view.point(p)
const scaleR = rr => (rr / (view.x1 - view.x0)) * view.width

// --- square in R³, phép chiếu xiên: (x1, x2, x3) ↦ (x1 + 0.55 x2, x3 + 0.4 x2) ---
const v3 = makeView({ x0: -2.6, x1: 2.6, y0: -1.7, y1: 1.9, width: 420, height: 290 })
const proj = ([a, b, c]) => v3.point([a + 0.55 * b, c + 0.4 * b])
const pa = ref(0.3), pb = ref(-0.2)
const square = [[-1, -1, 0], [1, -1, 0], [1, 1, 0], [-1, 1, 0]].map(proj)
const plane = [[-1.8, -1.6, 0], [1.8, -1.6, 0], [1.8, 1.6, 0], [-1.8, 1.6, 0]].map(proj)
const center = computed(() => proj([pa.value, pb.value, 0]))
const disk = computed(() => Array.from({ length: 64 }, (_, i) => { const t = (2 * Math.PI * i) / 64; return proj([pa.value + r.value * Math.cos(t), pb.value + r.value * Math.sin(t), 0]) }))
const sphereRadius = computed(() => (r.value / (v3.x1 - v3.x0)) * v3.width)
const squareInside = computed(() => Math.abs(pa.value) + r.value <= 1 + 1e-9 && Math.abs(pb.value) + r.value <= 1 + 1e-9)
const onBoundary = computed(() => Math.abs(Math.abs(pa.value) - 1) < 1e-9 || Math.abs(Math.abs(pb.value) - 1) < 1e-9)
const axes = [[[0, 0, 0], [2.2, 0, 0], 'x₁'], [[0, 0, 0], [0, 2.2, 0], 'x₂'], [[0, 0, 0], [0, 0, 1.6], 'x₃']]
</script>

<template>
  <figure class="study-lab" :aria-label="type === 'segment' ? 'Nội tương đối của một đoạn thẳng' : 'Nội tương đối của hình vuông trong không gian ba chiều'">
    <template v-if="type === 'segment'">
      <p class="lab-title">Một đoạn thẳng không có điểm trong, nhưng có nội tương đối</p>
      <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Đoạn thẳng, đường thẳng chứa nó, hình tròn bán kính r quanh điểm x">
        <line :x1="view.sx(-3)" :y1="view.sy(-1.5)" :x2="view.sx(3)" :y2="view.sy(1.5)" class="lab-guide" />
        <line :x1="P(A)[0]" :y1="P(A)[1]" :x2="P(B)[0]" :y2="P(B)[1]" class="lab-line" />
        <circle :cx="P(x)[0]" :cy="P(x)[1]" :r="scaleR(r)" class="lab-region-soft" />
        <circle :cx="P(x)[0]" :cy="P(x)[1]" :r="scaleR(r)" class="lab-guide" />
        <line :x1="P(chordEnds[0])[0]" :y1="P(chordEnds[0])[1]" :x2="P(chordEnds[1])[0]" :y2="P(chordEnds[1])[1]" :class="segInside ? 'lab-good' : 'lab-bad'" />
        <circle :cx="P(A)[0]" :cy="P(A)[1]" r="5" class="lab-dot" /><circle :cx="P(B)[0]" :cy="P(B)[1]" r="5" class="lab-dot" />
        <circle :cx="P(x)[0]" :cy="P(x)[1]" r="7" class="lab-dot-warn" />
        <text :x="P(x)[0] - 4" :y="P(x)[1] - 14">x</text>
        <text :x="view.sx(2.15)" :y="view.sy(1.55)" class="lab-small">aff C</text>
      </svg>
      <div class="lab-controls">
        <label>Vị trí của x trên đoạn: {{ fmt(s) }}<input v-model.number="s" type="range" min="0" max="1" step="0.01" /></label>
        <label>Bán kính r = {{ fmt(r) }}<input v-model.number="r" type="range" min="0.05" max="1.5" step="0.05" /></label>
      </div>
      <div class="lab-readout" role="status">
        <p>Hình tròn bán kính r quanh x luôn có điểm nằm ngoài đường thẳng chứa đoạn, nên <span class="is-bad">x không phải điểm trong</span> của C khi xét trong R².</p>
        <p v-if="segInside">Phần giao của hình tròn với đường thẳng aff C là đoạn màu xanh, và nó <span class="is-good">nằm trọn trong C</span>. Với bán kính này, x thỏa điều kiện của nội tương đối.</p>
        <p v-else>Phần giao của hình tròn với aff C <span class="is-bad">lòi ra ngoài C</span> ở phía đầu mút gần hơn. Hãy thử giảm r. {{ s === 0 || s === 1 ? 'Ở đầu mút, giảm r bao nhiêu cũng không đủ: Đầu mút thuộc biên tương đối.' : 'Vì x không phải đầu mút, luôn có một r đủ nhỏ thỏa điều kiện.' }}</p>
      </div>
    </template>

    <template v-else>
      <p class="lab-title">Hình vuông nằm phẳng trong R³</p>
      <svg :viewBox="`0 0 ${v3.width} ${v3.height}`" role="img" aria-label="Mặt phẳng x3 bằng 0, hình vuông trên đó, quả cầu bán kính r quanh một điểm và đường tròn giao với mặt phẳng">
        <polygon :points="plane.map(p => p.join(',')).join(' ')" class="lab-region-soft" />
        <g v-for="[from, to, name] in axes" :key="name">
          <line :x1="proj(from)[0]" :y1="proj(from)[1]" :x2="proj(to)[0]" :y2="proj(to)[1]" class="lab-axis" />
          <text :x="proj(to)[0] + 6" :y="proj(to)[1] + 4" class="lab-small">{{ name }}</text>
        </g>
        <polygon :points="square.map(p => p.join(',')).join(' ')" class="lab-region" />
        <circle :cx="center[0]" :cy="center[1]" :r="sphereRadius" class="lab-guide" />
        <polygon :points="disk.map(p => p.join(',')).join(' ')" :class="squareInside ? 'lab-good-fill' : 'lab-bad-fill'" />
        <circle :cx="center[0]" :cy="center[1]" r="6" class="lab-dot-warn" />
      </svg>
      <div class="lab-controls">
        <label>x₁ = {{ fmt(pa) }}<input v-model.number="pa" type="range" min="-1" max="1" step="0.05" /></label>
        <label>x₂ = {{ fmt(pb) }}<input v-model.number="pb" type="range" min="-1" max="1" step="0.05" /></label>
        <label>Bán kính r = {{ fmt(r) }}<input v-model.number="r" type="range" min="0.05" max="1" step="0.05" /></label>
      </div>
      <div class="lab-readout" role="status">
        <p>Điểm đang xét là ({{ fmt(pa) }}, {{ fmt(pb) }}, 0). Quả cầu bán kính r (đường tròn nét đứt) luôn có điểm với x₃ ≠ 0, nên nó không nằm trong hình vuông: <span class="is-bad">hình vuông không có điểm trong nào trong R³</span>.</p>
        <p v-if="squareInside">Phần giao của quả cầu với mặt phẳng x₃ = 0 là hình tròn màu xanh, và nó <span class="is-good">nằm trọn trong hình vuông</span>. Điểm này thuộc nội tương đối.</p>
        <p v-else-if="onBoundary">Điểm nằm trên cạnh của hình vuông. Hình tròn giao luôn lòi ra ngoài, dù r nhỏ đến đâu: điểm thuộc <span class="is-bad">biên tương đối</span>.</p>
        <p v-else>Hình tròn giao <span class="is-bad">lòi ra ngoài hình vuông</span>. Giảm r cho tới khi r ≤ {{ fmt(Math.min(1 - Math.abs(pa), 1 - Math.abs(pb))) }} thì điều kiện được thỏa.</p>
      </div>
    </template>
  </figure>
</template>
