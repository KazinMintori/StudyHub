<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { add, sub, scale, dot, norm2, barycentric, combination } from './convex-geometry.mjs'

// type: line (đường thẳng qua hai điểm), combination (tổ hợp affine của ba điểm),
// origin (vì sao tổng hệ số bằng 1), solutions (tập nghiệm của một phương trình tuyến tính).
const props = defineProps({ type: { type: String, default: 'line' } })
const uid = useId()
const svg = ref(null)

const views = {
  line: makeView({ x0: -3, x1: 8, y0: -2, y1: 6, width: 440, height: 320 }),
  combination: makeView({ x0: -4, x1: 7, y0: -3, y1: 6, width: 440, height: 360 }),
  origin: makeView({ x0: -4, x1: 7, y0: -3, y1: 6, width: 440, height: 360 }),
  solutions: makeView({ x0: -5, x1: 5, y0: -4, y1: 4, width: 400, height: 320 })
}
const view = computed(() => views[props.type] || views.line)
const P = p => view.value.point(p)
const gridX = computed(() => { const v = view.value; return Array.from({ length: Math.floor(v.x1) - Math.ceil(v.x0) + 1 }, (_, i) => Math.ceil(v.x0) + i) })
const gridY = computed(() => { const v = view.value; return Array.from({ length: Math.floor(v.y1) - Math.ceil(v.y0) + 1 }, (_, i) => Math.ceil(v.y0) + i) })

// Cắt đường thẳng p + t d theo khung nhìn (Liang–Barsky), trả về hai đầu mút.
function clipLine(p, d) {
  const v = view.value
  let t0 = -1e9, t1 = 1e9
  for (const [dv, lo, hi, pv] of [[d[0], v.x0, v.x1, p[0]], [d[1], v.y0, v.y1, p[1]]]) {
    if (Math.abs(dv) < 1e-12) { if (pv < lo || pv > hi) return null; continue }
    const a = (lo - pv) / dv, b = (hi - pv) / dv
    t0 = Math.max(t0, Math.min(a, b)); t1 = Math.min(t1, Math.max(a, b))
  }
  return t0 <= t1 ? [add(p, scale(t0, d)), add(p, scale(t1, d))] : null
}

const points = ref({
  x1: [4, 3], x2: [1, 1],
  p1: [-1, -1], p2: [4, 0], p3: [1, 4], y: [5, 3],
  o: [0, 0]
})
const drag = createDragger(svg, view, (name, value) => { points.value = { ...points.value, [name]: value } }, { step: 0.25, snap: 0.25 })

// --- line ---
const theta = ref(0.5)
const lineDir = computed(() => sub(points.value.x1, points.value.x2))
const yLine = computed(() => add(points.value.x2, scale(theta.value, lineDir.value)))
const fullLine = computed(() => norm2(lineDir.value) < 1e-9 ? null : clipLine(points.value.x2, lineDir.value))
const ticks = [-0.5, 0, 0.5, 1, 1.5].map(t => ({ t, label: t === 0.5 ? '½' : t === 1.5 ? '1.5' : t === -0.5 ? '−½' : String(t) }))
const lineStatus = computed(() => {
  if (norm2(lineDir.value) < 1e-9) return 'Hai điểm trùng nhau nên “đường thẳng” suy biến thành một điểm.'
  if (theta.value >= 0 && theta.value <= 1) return 'Với 0 ≤ θ ≤ 1, y nằm trên đoạn thẳng nối x₂ và x₁.'
  return theta.value > 1 ? 'Với θ > 1, y đã đi quá x₁ và nằm trên phần kéo dài về phía x₁.' : 'Với θ < 0, y lùi về phía sau x₂, trên phần kéo dài về phía x₂.'
})

// --- combination ---
const weights = computed(() => barycentric(points.value.y, points.value.p1, points.value.p2, points.value.p3))
const triangle = computed(() => [points.value.p1, points.value.p2, points.value.p3])
const edgeLines = computed(() => [[0, 1], [1, 2], [2, 0]].map(([i, j]) => clipLine(triangle.value[i], sub(triangle.value[j], triangle.value[i]))).filter(Boolean))
const negatives = computed(() => (weights.value || []).filter(w => w < -1e-9).length)

// --- origin ---
const presets = {
  sum2: { w: [1, 1, 0], label: 'p₁ + p₂ (tổng hệ số bằng 2)' },
  half: { w: [0.5, 0.5, 0.5], label: '½p₁ + ½p₂ + ½p₃ (tổng bằng 1.5)' },
  centroid: { w: [1 / 3, 1 / 3, 1 / 3], label: 'Trọng tâm ⅓p₁ + ⅓p₂ + ⅓p₃ (tổng bằng 1)' }
}
const affineWeights = [0.2, 0.5, 0.3]
const second = ref('sum2')
const relative = (w, o) => add(o, combination([sub(points.value.p1, o), sub(points.value.p2, o), sub(points.value.p3, o)], w))
const affinePoint = computed(() => relative(affineWeights, points.value.o))
const otherPoint = computed(() => relative(presets[second.value].w, points.value.o))
const otherSum = computed(() => presets[second.value].w.reduce((s, x) => s + x, 0))

// --- solutions: a1 x1 + a2 x2 = b ---
const a1 = ref(1), a2 = ref(2), rhs = ref(4), tParam = ref(1)
const normal = computed(() => [a1.value, a2.value])
const degenerate = computed(() => norm2(normal.value) < 1e-9)
const x0 = computed(() => degenerate.value ? [0, 0] : scale(rhs.value / dot(normal.value, normal.value), normal.value))
const dirUnit = computed(() => degenerate.value ? [1, 0] : scale(1 / norm2(normal.value), [-a2.value, a1.value]))
const xt = computed(() => add(x0.value, scale(tParam.value, dirUnit.value)))
const solutionLine = computed(() => degenerate.value ? null : clipLine(x0.value, dirUnit.value))
const nullLine = computed(() => degenerate.value ? null : clipLine([0, 0], dirUnit.value))

const titles = {
  line: 'Một điểm chạy trên đường thẳng qua hai điểm',
  combination: 'Tổ hợp affine của ba điểm trong mặt phẳng',
  origin: 'Tổng hệ số bằng 1 và vị trí của gốc tọa độ',
  solutions: 'Tập nghiệm của một phương trình tuyến tính'
}
const arrow = `${uid}-arrow`, arrowAccent = `${uid}-arrow-accent`
</script>

<template>
  <figure class="study-lab" :aria-label="titles[type]">
    <p class="lab-title">{{ titles[type] }}</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" :aria-label="titles[type]" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs>
        <marker :id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="lab-arrow-head" /></marker>
        <marker :id="arrowAccent" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="lab-arrow-accent" /></marker>
      </defs>
      <g>
        <line v-for="x in gridX" :key="`gx${x}`" :x1="view.sx(x)" :x2="view.sx(x)" :y1="0" :y2="view.height" :class="x === 0 ? 'lab-axis' : 'lab-grid'" />
        <line v-for="y in gridY" :key="`gy${y}`" :y1="view.sy(y)" :y2="view.sy(y)" :x1="0" :x2="view.width" :class="y === 0 ? 'lab-axis' : 'lab-grid'" />
      </g>

      <template v-if="type === 'line'">
        <line v-if="fullLine" :x1="P(fullLine[0])[0]" :y1="P(fullLine[0])[1]" :x2="P(fullLine[1])[0]" :y2="P(fullLine[1])[1]" class="lab-guide" />
        <line :x1="P(points.x2)[0]" :y1="P(points.x2)[1]" :x2="P(points.x1)[0]" :y2="P(points.x1)[1]" class="lab-accent" />
        <g v-for="tick in ticks" :key="tick.t">
          <circle :cx="P(add(points.x2, scale(tick.t, lineDir)))[0]" :cy="P(add(points.x2, scale(tick.t, lineDir)))[1]" r="3" class="lab-dot" />
          <text :x="P(add(points.x2, scale(tick.t, lineDir)))[0] + 8" :y="P(add(points.x2, scale(tick.t, lineDir)))[1] + 18" class="lab-small">θ={{ tick.label }}</text>
        </g>
        <circle :cx="P(yLine)[0]" :cy="P(yLine)[1]" r="8" class="lab-dot-warn" />
        <text :x="P(yLine)[0] - 6" :y="P(yLine)[1] - 14">y</text>
        <circle :cx="P(points.x1)[0]" :cy="P(points.x1)[1]" r="9" class="lab-handle" tabindex="0" role="slider" aria-label="Điểm x₁, kéo hoặc dùng phím mũi tên" @pointerdown="drag.start('x1', $event)" @keydown="drag.key('x1', points.x1, $event)" />
        <circle :cx="P(points.x2)[0]" :cy="P(points.x2)[1]" r="9" class="lab-handle" tabindex="0" role="slider" aria-label="Điểm x₂, kéo hoặc dùng phím mũi tên" @pointerdown="drag.start('x2', $event)" @keydown="drag.key('x2', points.x2, $event)" />
        <text :x="P(points.x1)[0] + 12" :y="P(points.x1)[1] - 10">x₁</text>
        <text :x="P(points.x2)[0] + 12" :y="P(points.x2)[1] - 10">x₂</text>
      </template>

      <template v-else-if="type === 'combination'">
        <line v-for="(seg, i) in edgeLines" :key="`e${i}`" :x1="P(seg[0])[0]" :y1="P(seg[0])[1]" :x2="P(seg[1])[0]" :y2="P(seg[1])[1]" class="lab-guide" />
        <polygon :points="triangle.map(p => P(p).join(',')).join(' ')" class="lab-region" />
        <line v-for="(p, i) in triangle" :key="`s${i}`" :x1="P(points.y)[0]" :y1="P(points.y)[1]" :x2="P(p)[0]" :y2="P(p)[1]" class="lab-line" stroke-dasharray="2 4" />
        <circle v-for="(name, i) in ['p1', 'p2', 'p3']" :key="name" :cx="P(points[name])[0]" :cy="P(points[name])[1]" r="9" class="lab-handle" tabindex="0" role="slider" :aria-label="`Điểm p${i + 1}`" @pointerdown="drag.start(name, $event)" @keydown="drag.key(name, points[name], $event)" />
        <text v-for="(name, i) in ['p1', 'p2', 'p3']" :key="`t${name}`" :x="P(points[name])[0] + 12" :y="P(points[name])[1] - 10">p{{ ['₁', '₂', '₃'][i] }}</text>
        <circle :cx="P(points.y)[0]" :cy="P(points.y)[1]" r="9" class="lab-handle lab-handle-alt" tabindex="0" role="slider" aria-label="Điểm y cần biểu diễn" @pointerdown="drag.start('y', $event)" @keydown="drag.key('y', points.y, $event)" />
        <text :x="P(points.y)[0] + 12" :y="P(points.y)[1] + 20">y</text>
      </template>

      <template v-else-if="type === 'origin'">
        <polygon :points="triangle.map(p => P(p).join(',')).join(' ')" class="lab-region-soft" />
        <line v-for="(p, i) in triangle" :key="`v${i}`" :x1="P(points.o)[0]" :y1="P(points.o)[1]" :x2="P(p)[0]" :y2="P(p)[1]" class="lab-line" :marker-end="`url(#${arrow})`" />
        <circle v-for="(name, i) in ['p1', 'p2', 'p3']" :key="name" :cx="P(points[name])[0]" :cy="P(points[name])[1]" r="8" class="lab-handle" tabindex="0" role="slider" :aria-label="`Điểm p${i + 1}`" @pointerdown="drag.start(name, $event)" @keydown="drag.key(name, points[name], $event)" />
        <text v-for="(name, i) in ['p1', 'p2', 'p3']" :key="`t${name}`" :x="P(points[name])[0] + 12" :y="P(points[name])[1] - 10">p{{ ['₁', '₂', '₃'][i] }}</text>
        <circle :cx="P(affinePoint)[0]" :cy="P(affinePoint)[1]" r="7" class="lab-dot-accent" />
        <text :x="P(affinePoint)[0] + 10" :y="P(affinePoint)[1] + 20" class="lab-small">tổ hợp affine</text>
        <circle :cx="P(otherPoint)[0]" :cy="P(otherPoint)[1]" r="7" :class="Math.abs(otherSum - 1) < 1e-9 ? 'lab-dot-accent' : 'lab-dot-bad'" />
        <text :x="P(otherPoint)[0] + 10" :y="P(otherPoint)[1] - 10" class="lab-small">{{ Math.abs(otherSum - 1) < 1e-9 ? 'trọng tâm' : 'tổ hợp thứ hai' }}</text>
        <circle :cx="P(points.o)[0]" :cy="P(points.o)[1]" r="9" class="lab-handle lab-handle-alt" tabindex="0" role="slider" aria-label="Gốc tọa độ O, kéo để dời gốc" @pointerdown="drag.start('o', $event)" @keydown="drag.key('o', points.o, $event)" />
        <text :x="P(points.o)[0] - 26" :y="P(points.o)[1] + 22">O</text>
      </template>

      <template v-else-if="type === 'solutions'">
        <line v-if="nullLine" :x1="P(nullLine[0])[0]" :y1="P(nullLine[0])[1]" :x2="P(nullLine[1])[0]" :y2="P(nullLine[1])[1]" class="lab-guide" />
        <line v-if="solutionLine" :x1="P(solutionLine[0])[0]" :y1="P(solutionLine[0])[1]" :x2="P(solutionLine[1])[0]" :y2="P(solutionLine[1])[1]" class="lab-accent" />
        <line v-if="!degenerate" :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P(x0)[0]" :y2="P(x0)[1]" class="lab-line" :marker-end="`url(#${arrow})`" />
        <line v-if="!degenerate && Math.abs(tParam) > 0.05" :x1="P(x0)[0]" :y1="P(x0)[1]" :x2="P(xt)[0]" :y2="P(xt)[1]" class="lab-warn" :marker-end="`url(#${arrow})`" />
        <circle :cx="P(x0)[0]" :cy="P(x0)[1]" r="6" class="lab-dot" />
        <text :x="P(x0)[0] + 10" :y="P(x0)[1] + 20">x₀</text>
        <circle :cx="P(xt)[0]" :cy="P(xt)[1]" r="8" class="lab-dot-warn" />
        <text :x="P(xt)[0] + 10" :y="P(xt)[1] - 10">x₀ + t·d</text>
      </template>
    </svg>

    <div v-if="type === 'line'" class="lab-controls">
      <label>θ = {{ fmt(theta) }}<input v-model.number="theta" type="range" min="-1" max="2" step="0.05" /></label>
    </div>
    <div v-if="type === 'origin'" class="lab-controls">
      <label>Tổ hợp thứ hai
        <select v-model="second"><option v-for="(item, key) in presets" :key="key" :value="key">{{ item.label }}</option></select>
      </label>
    </div>
    <div v-if="type === 'solutions'" class="lab-controls">
      <label>a₁ = {{ fmt(a1, 1) }}<input v-model.number="a1" type="range" min="-3" max="3" step="0.5" /></label>
      <label>a₂ = {{ fmt(a2, 1) }}<input v-model.number="a2" type="range" min="-3" max="3" step="0.5" /></label>
      <label>b = {{ fmt(rhs, 1) }}<input v-model.number="rhs" type="range" min="-6" max="6" step="0.5" /></label>
      <label>t = {{ fmt(tParam, 1) }}<input v-model.number="tParam" type="range" min="-4" max="4" step="0.1" /></label>
    </div>

    <div class="lab-readout" role="status">
      <template v-if="type === 'line'">
        <p>y = θx₁ + (1 − θ)x₂ = <span class="is-accent">{{ fmtPoint(yLine) }}</span></p>
        <p>Viết theo cách thứ hai: y = x₂ + θ(x₁ − x₂), tức là xuất phát từ x₂ = {{ fmtPoint(points.x2) }} rồi đi θ = {{ fmt(theta) }} lần vector x₁ − x₂ = {{ fmtPoint(lineDir) }}.</p>
        <p>{{ lineStatus }}</p>
      </template>
      <template v-else-if="type === 'combination'">
        <template v-if="weights">
          <p>y = θ₁p₁ + θ₂p₂ + θ₃p₃ với θ = (<span v-for="(w, i) in weights" :key="i"><span :class="w < -1e-9 ? 'is-bad' : 'is-good'">{{ fmt(w) }}</span>{{ i < 2 ? ', ' : '' }}</span>), tổng ba hệ số bằng {{ fmt(weights[0] + weights[1] + weights[2]) }}.</p>
          <p v-if="negatives === 0">Mọi hệ số đều không âm, nên y nằm trong tam giác (kể cả cạnh). Đây là một tổ hợp lồi.</p>
          <p v-else>Có {{ negatives }} hệ số âm, nên y nằm ngoài tam giác. Nó vẫn là một tổ hợp affine của ba đỉnh.</p>
        </template>
        <p v-else class="is-bad">Ba điểm đang thẳng hàng. Khi đó các tổ hợp affine của chúng chỉ phủ một đường thẳng, nên không phải điểm y nào cũng biểu diễn được.</p>
      </template>
      <template v-else-if="type === 'origin'">
        <p>Tổ hợp affine 0.2p₁ + 0.5p₂ + 0.3p₃ = <span class="is-accent">{{ fmtPoint(affinePoint) }}</span>. Dời O đi đâu, điểm này cũng đứng yên.</p>
        <p v-if="Math.abs(otherSum - 1) > 1e-9">Tổ hợp thứ hai có tổng hệ số {{ fmt(otherSum, 1) }} cho điểm <span class="is-bad">{{ fmtPoint(otherPoint) }}</span>. Khi O dịch một vector v, điểm này dịch (1 − {{ fmt(otherSum, 1) }})v, nghĩa là kết quả phụ thuộc vào chỗ ta đặt gốc.</p>
        <p v-else>Tổ hợp thứ hai cũng có tổng hệ số bằng 1, nên trọng tâm {{ fmtPoint(otherPoint) }} cũng không đổi khi dời gốc.</p>
      </template>
      <template v-else-if="type === 'solutions'">
        <p v-if="degenerate" class="is-bad">Với a₁ = a₂ = 0, phương trình thành 0 = b: vô nghiệm nếu b ≠ 0, và mọi điểm đều là nghiệm nếu b = 0.</p>
        <template v-else>
          <p>Phương trình {{ fmt(a1, 1) }}x₁ + {{ fmt(a2, 1) }}x₂ = {{ fmt(rhs, 1) }}. Nghiệm riêng gần gốc nhất x₀ = {{ fmtPoint(x0) }}.</p>
          <p>Hướng d = {{ fmtPoint(dirUnit) }} thỏa a₁d₁ + a₂d₂ = 0, nên mọi điểm x₀ + t·d vẫn là nghiệm: với t = {{ fmt(tParam, 1) }}, vế trái bằng <span class="is-good">{{ fmt(dot(normal, xt)) }}</span>.</p>
          <p>Đường nét đứt đi qua gốc là tập nghiệm của phương trình thuần nhất (b = 0). Tập nghiệm của phương trình ban đầu chính là đường đó tịnh tiến thêm x₀.</p>
        </template>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol v-if="type === 'line'">
        <li>Kéo θ từ 0 đến 1 và quan sát y đi từ x₂ tới x₁. Tỉ lệ quãng đường đã đi trên đoạn có bằng θ không?</li>
        <li>Đưa θ lên 1.5 rồi xuống −0.5. Điểm y còn trên đường thẳng không, còn trên đoạn không?</li>
        <li>Kéo x₁ trùng với x₂. Lúc đó công thức cho ra tập điểm nào?</li>
      </ol>
      <ol v-else-if="type === 'combination'">
        <li>Kéo y vào trong tam giác rồi ra ngoài qua từng cạnh. Hệ số nào đổi dấu khi y vượt qua cạnh đối diện với p₁?</li>
        <li>Đặt y trùng một đỉnh. Bộ hệ số lúc đó là gì?</li>
        <li>Kéo ba điểm cho gần thẳng hàng và quan sát các hệ số lớn lên thế nào.</li>
      </ol>
      <ol v-else-if="type === 'origin'">
        <li>Kéo O đi khắp khung hình và theo dõi điểm tím. Nó có dịch chuyển không?</li>
        <li>Chọn “p₁ + p₂” rồi kéo O. Điểm đỏ di chuyển cùng chiều hay ngược chiều với O?</li>
        <li>Chọn trọng tâm. Vì sao điểm này cũng đứng yên?</li>
      </ol>
      <ol v-else>
        <li>Đổi b mà giữ a₁, a₂. Đường nghiệm thay đổi thế nào, còn đường nét đứt thì sao?</li>
        <li>Kéo t để x₀ + t·d chạy trên đường nghiệm. Vế trái có lúc nào khác b không?</li>
        <li>Đặt b = 0. Tập nghiệm lúc này có chứa gốc tọa độ không?</li>
      </ol>
    </details>
  </figure>
</template>
