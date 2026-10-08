<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { add, scale, sub, dot } from './convex-geometry.mjs'
const clipId = `${useId()}-clip`

// Thứ tự sinh bởi nón K = cone{k₁, k₂} trong R²: x ⪯ y khi y − x ∈ K.
// type="order": tập hữu hạn, phần tử tối thiểu, phần tử nhỏ nhất, vùng x + K và x − K.
// type="pareto": thêm vector trọng số λ để tìm phần tử cực tiểu λᵀz (vô hướng hóa).
const props = defineProps({ type: { type: String, default: 'order' } })
const svg = ref(null)
const view = ref(makeView({ x0: -0.5, x1: 7, y0: -0.5, y1: 7, width: 400, height: 400 }))
const P = p => view.value.point(p)
const pts = ref([[1, 6], [2, 4], [4, 2], [3, 6], [5, 4], [6, 1.5], [5.5, 5.5]])
const selected = ref(1)
const drag = createDragger(svg, view, (name, value) => { pts.value = pts.value.map((p, i) => (String(i) === name ? value : p)) }, { step: 0.1, snap: 0.1 })
const ang1 = ref(0), ang2 = ref(90), lamAngle = ref(40)
const dir = a => [Math.cos((a * Math.PI) / 180), Math.sin((a * Math.PI) / 180)]
const k1 = computed(() => dir(ang1.value)), k2 = computed(() => dir(ang2.value))
// y − x ∈ K khi y − x = αk₁ + βk₂ với α, β ≥ 0.
function inK(v) {
  const [a, b] = k1.value, [c, d] = k2.value, det = a * d - b * c
  if (Math.abs(det) < 1e-12) return false
  const alpha = (v[0] * d - v[1] * c) / det, beta = (a * v[1] - b * v[0]) / det
  return alpha >= -1e-9 && beta >= -1e-9
}
const precedes = (x, y) => inK(sub(y, x))
const minimal = computed(() => pts.value.map((x, i) => !pts.value.some((y, j) => j !== i && precedes(y, x) && !precedes(x, y))))
const minimum = computed(() => pts.value.findIndex(x => pts.value.every(y => precedes(x, y))))
const wedge = (x, sign) => [x, add(x, scale(sign * 12, k1.value)), add(x, scale(sign * 12, add(k1.value, k2.value))), add(x, scale(sign * 12, k2.value))]
const lambda = computed(() => dir(lamAngle.value))
const values = computed(() => pts.value.map(p => dot(lambda.value, p)))
const best = computed(() => values.value.indexOf(Math.min(...values.value)))
const levelLine = computed(() => {
  const c = values.value[best.value], l = lambda.value, x0 = scale(c, l), d = [-l[1], l[0]]
  return [add(x0, scale(-20, d)), add(x0, scale(20, d))]
})
const dualOk = computed(() => dot(lambda.value, k1.value) > 1e-9 && dot(lambda.value, k2.value) > 1e-9)
const label = i => String.fromCharCode(65 + i)
</script>

<template>
  <figure class="study-lab" :aria-label="type === 'order' ? 'Thứ tự sinh bởi một nón và các phần tử tối thiểu' : 'Tìm phần tử tối thiểu bằng tổng có trọng số'">
    <p class="lab-title">{{ type === 'order' ? 'So sánh các điểm theo một nón' : 'Vô hướng hóa: cực tiểu λᵀz trên tập điểm' }}</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Tập điểm, nón dời tới một điểm đang chọn và các phần tử tối thiểu" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs><clipPath :id="clipId"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath></defs>
      <line v-for="x in [1, 2, 3, 4, 5, 6]" :key="`gx${x}`" :x1="view.sx(x)" :x2="view.sx(x)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="y in [1, 2, 3, 4, 5, 6]" :key="`gy${y}`" :y1="view.sy(y)" :y2="view.sy(y)" x1="0" :x2="view.width" class="lab-grid" />
      <line :x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :y1="0" :y2="view.height" :x1="view.sx(0)" :x2="view.sx(0)" class="lab-axis" />
      <g :clip-path="`url(#${clipId})`">
        <template v-if="type === 'order'">
          <polygon :points="wedge(pts[selected], 1).map(p => P(p).join(',')).join(' ')" class="lab-region-soft" />
          <polygon :points="wedge(pts[selected], -1).map(p => P(p).join(',')).join(' ')" class="lab-bad-fill" style="opacity: 0.35" />
        </template>
        <template v-else>
          <line :x1="P(levelLine[0])[0]" :y1="P(levelLine[0])[1]" :x2="P(levelLine[1])[0]" :y2="P(levelLine[1])[1]" class="lab-accent" />
        </template>
      </g>
      <g v-for="(p, i) in pts" :key="i">
        <circle v-if="type === 'order' && minimum === i" :cx="P(p)[0]" :cy="P(p)[1]" r="15" class="lab-warn" />
        <circle :cx="P(p)[0]" :cy="P(p)[1]" :r="(type === 'pareto' && best === i) || selected === i ? 11 : 9" :class="minimal[i] ? 'lab-handle' : 'lab-handle lab-handle-alt'" tabindex="0" role="slider" :aria-label="`Điểm ${label(i)}`" @pointerdown="selected = i; drag.start(String(i), $event)" @keydown="drag.key(String(i), p, $event)" @focus="selected = i" />
        <text :x="P(p)[0] + 12" :y="P(p)[1] - 10">{{ label(i) }}</text>
      </g>
      <line v-if="type === 'pareto'" :x1="view.sx(0.3)" :y1="view.sy(0.3)" :x2="P(add([0.3, 0.3], scale(1.2, lambda)))[0]" :y2="P(add([0.3, 0.3], scale(1.2, lambda)))[1]" class="lab-accent" />
      <text v-if="type === 'pareto'" :x="P(add([0.3, 0.3], scale(1.35, lambda)))[0]" :y="P(add([0.3, 0.3], scale(1.35, lambda)))[1]" class="lab-small">λ</text>
    </svg>
    <div class="lab-controls">
      <template v-if="type === 'order'">
        <label>Góc của k₁: {{ ang1 }}°<input v-model.number="ang1" type="range" min="-60" max="80" step="5" @input="ang2 = Math.max(ang2, ang1 + 10)" /></label>
        <label>Góc của k₂: {{ ang2 }}°<input v-model.number="ang2" type="range" min="10" max="170" step="5" @input="ang1 = Math.min(ang1, ang2 - 10)" /></label>
      </template>
      <label v-else>Hướng của λ: {{ lamAngle }}°<input v-model.number="lamAngle" type="range" min="-30" max="120" step="1" /></label>
    </div>
    <div class="lab-readout" role="status">
      <template v-if="type === 'order'">
        <p>Nón K sinh bởi k₁ = {{ fmtPoint(k1) }} và k₂ = {{ fmtPoint(k2) }}{{ ang1 === 0 && ang2 === 90 ? ', tức là góc phần tư không âm: so sánh theo từng thành phần' : '' }}. Điểm đang chọn là {{ label(selected) }} = {{ fmtPoint(pts[selected], 1) }}.</p>
        <p>Vùng tím nhạt là {{ label(selected) }} + K, gồm những điểm "lớn hơn hoặc bằng" {{ label(selected) }}. Vùng đỏ nhạt là {{ label(selected) }} − K, gồm những điểm "nhỏ hơn hoặc bằng" nó.</p>
        <p>Phần tử tối thiểu (màu tím): {{ pts.map((p, i) => i).filter(i => minimal[i]).map(label).join(', ') }}. {{ minimum >= 0 ? `Phần tử nhỏ nhất là ${label(minimum)} (vòng vàng): mọi điểm khác đều nằm trong ${label(minimum)} + K.` : 'Không có phần tử nhỏ nhất: không điểm nào nhỏ hơn hoặc bằng tất cả các điểm khác.' }}</p>
      </template>
      <template v-else>
        <p>λ = {{ fmtPoint(lambda) }}. Giá trị λᵀz nhỏ nhất là {{ fmt(values[best]) }}, đạt tại {{ label(best) }}. Đường tím là đường mức λᵀz = {{ fmt(values[best]) }}: mọi điểm khác nằm về phía λ chỉ tới.</p>
        <p v-if="dualOk">Cả hai thành phần của λ dương, nên điểm tìm được chắc chắn là một phần tử tối thiểu.</p>
        <p v-else class="is-bad">λ có một thành phần không dương, nên điểm tìm được chưa chắc là phần tử tối thiểu.</p>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol v-if="type === 'order'">
        <li>Chọn lần lượt từng điểm. Điểm tối thiểu là điểm có vùng đỏ nhạt không chứa điểm nào khác.</li>
        <li>Kéo một điểm xuống góc dưới bên trái của mọi điểm khác. Phần tử nhỏ nhất xuất hiện không?</li>
        <li>Xoay hai vector sinh để nón hẹp lại. Số phần tử tối thiểu tăng hay giảm, và vì sao?</li>
      </ol>
      <ol v-else>
        <li>Xoay λ từ gần 0° tới gần 90°. Những điểm nào lần lượt được chọn?</li>
        <li>Có phần tử tối thiểu nào không bao giờ được chọn, dù λ dương ở mọi hướng không?</li>
      </ol>
    </details>
  </figure>
</template>
