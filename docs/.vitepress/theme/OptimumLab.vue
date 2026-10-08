<script setup>
import { computed, ref } from 'vue'
import { makeView, fmt } from './svg-drag'

// Bài toán một biến: minimize f(x) trên miền khả thi {x trong dom f : l <= x <= u}.
// Kết luận về p*, việc đạt nghiệm và ràng buộc chặt được suy luận theo tính chất giải tích của từng hàm,
// còn đồ thị chỉ để nhìn. Không kết luận từ một lưới điểm hữu hạn khi có thể lập luận chính xác.
const fns = {
  quad: { label: 'f(x) = (x − 3)²', f: x => (x - 3) ** 2, positive: false },
  inv: { label: 'f(x) = 1/x, miền x > 0', f: x => 1 / x, positive: true },
  neglog: { label: 'f(x) = −log x, miền x > 0', f: x => -Math.log(x), positive: true },
  xlogx: { label: 'f(x) = x log x, miền x > 0', f: x => x * Math.log(x), positive: true },
  well: { label: 'f(x) = x⁴ − 4x² + x', f: x => x ** 4 - 4 * x * x + x, positive: false }
}
const choice = ref('quad')
const hasLower = ref(false), hasUpper = ref(true)
const lower = ref(-1), upper = ref(1)
const view = makeView({ x0: -3, x1: 5, y0: -6, y1: 6, width: 440, height: 300 })
const fn = computed(() => fns[choice.value])

const lo = computed(() => Math.max(hasLower.value ? lower.value : -Infinity, fn.value.positive ? 0 : -Infinity))
const loOpen = computed(() => fn.value.positive && (!hasLower.value || lower.value <= 0))
const hi = computed(() => hasUpper.value ? upper.value : Infinity)
const infeasible = computed(() => lo.value > hi.value || (loOpen.value && hi.value <= lo.value))
const clamp = (x, a, b) => Math.min(b, Math.max(a, x))
const rootsWell = [-1.47299760111403, 1.3469974085277738] // hai điểm cực tiểu cục bộ của x⁴ − 4x² + x

// Kết luận chính xác cho từng hàm.
const analysis = computed(() => {
  if (infeasible.value) return { status: 'infeasible' }
  const f = fn.value.f, a = lo.value, b = hi.value
  if (choice.value === 'quad') { const x = clamp(3, a, b); return { status: 'attained', x, value: f(x) } }
  if (choice.value === 'xlogx') { const x = clamp(1 / Math.E, a, b); return { status: 'attained', x, value: f(x) } }
  if (choice.value === 'inv') return Number.isFinite(b) ? { status: 'attained', x: b, value: f(b) } : { status: 'not-attained', value: 0 }
  if (choice.value === 'neglog') return Number.isFinite(b) ? { status: 'attained', x: b, value: f(b) } : { status: 'unbounded' }
  // Hàm bậc bốn: cực tiểu trên đoạn đạt tại một điểm dừng bên trong hoặc tại đầu mút.
  const candidates = [...rootsWell.filter(x => x >= a && x <= b), ...[a, b].filter(Number.isFinite)]
  const best = candidates.reduce((p, x) => (f(x) < f(p) ? x : p), candidates[0])
  return { status: 'attained', x: best, value: f(best) }
})
const activeBound = computed(() => {
  const r = analysis.value
  if (r.status !== 'attained') return ''
  if (hasLower.value && Math.abs(r.x - lower.value) < 1e-9 && lower.value > (fn.value.positive ? 0 : -Infinity)) return 'dưới'
  if (hasUpper.value && Math.abs(r.x - upper.value) < 1e-9) return 'trên'
  return ''
})
const localMins = computed(() => {
  if (choice.value !== 'well' || infeasible.value) return []
  return rootsWell.filter(x => x > lo.value && x < hi.value)
})

// Đồ thị được cắt thành nhiều đoạn khi hàm ra khỏi khung nhìn hoặc ra khỏi miền xác định.
const curve = computed(() => {
  const f = fn.value.f, segs = [[]]
  for (let i = 0; i <= 400; i++) {
    const x = view.x0 + (i / 400) * (view.x1 - view.x0)
    const y = fn.value.positive && x <= 0.005 ? NaN : f(x)
    if (Number.isFinite(y) && y >= view.y0 - 1 && y <= view.y1 + 1) segs.at(-1).push(`${view.sx(x)},${view.sy(y)}`)
    else if (segs.at(-1).length) segs.push([])
  }
  return segs.filter(s => s.length > 1).map(s => s.join(' '))
})
const feasibleSeg = computed(() => infeasible.value ? null : [Math.max(lo.value, view.x0), Math.min(hi.value, view.x1)])
</script>

<template>
  <figure class="study-lab" aria-label="Giá trị tối ưu của một bài toán một biến">
    <p class="lab-title">Miền khả thi quyết định nghiệm</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Đồ thị hàm mục tiêu, miền khả thi tô trên trục hoành và điểm tối ưu nếu có">
      <line v-for="x in [-2, -1, 1, 2, 3, 4]" :key="`gx${x}`" :x1="view.sx(x)" :x2="view.sx(x)" y1="0" :y2="view.height" class="lab-grid" />
      <line :x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
      <text v-for="x in [-2, -1, 1, 2, 3, 4]" :key="`tx${x}`" :x="view.sx(x) - 5" :y="view.sy(0) + 18" class="lab-small">{{ x }}</text>
      <rect v-if="feasibleSeg" :x="view.sx(feasibleSeg[0])" :y="view.sy(0) - 6" :width="Math.max(0, view.sx(feasibleSeg[1]) - view.sx(feasibleSeg[0]))" height="12" class="lab-region" />
      <circle v-if="feasibleSeg && loOpen && lo >= view.x0" :cx="view.sx(lo)" :cy="view.sy(0)" r="6" class="lab-dot-hollow" />
      <polyline v-for="(pts, i) in curve" :key="i" :points="pts" class="lab-line" />
      <template v-if="analysis.status === 'attained'">
        <line :x1="view.sx(analysis.x)" :x2="view.sx(analysis.x)" :y1="view.sy(0)" :y2="view.sy(Math.max(view.y0, Math.min(view.y1, analysis.value)))" class="lab-guide" />
        <circle :cx="view.sx(analysis.x)" :cy="view.sy(Math.max(view.y0, Math.min(view.y1, analysis.value)))" r="8" class="lab-dot-accent" />
      </template>
      <circle v-for="x in localMins" :key="x" :cx="view.sx(x)" :cy="view.sy(Math.max(view.y0, fn.f(x)))" r="6" class="lab-dot-hollow" />
    </svg>
    <div class="lab-controls">
      <label>Hàm mục tiêu
        <select v-model="choice"><option v-for="(item, key) in fns" :key="key" :value="key">{{ item.label }}</option></select>
      </label>
      <label class="lab-check"><input v-model="hasLower" type="checkbox" /> Có ràng buộc x ≥ l</label>
      <label v-if="hasLower">l = {{ fmt(lower, 1) }}<input v-model.number="lower" type="range" min="-3" max="5" step="0.1" /></label>
      <label class="lab-check"><input v-model="hasUpper" type="checkbox" /> Có ràng buộc x ≤ u</label>
      <label v-if="hasUpper">u = {{ fmt(upper, 1) }}<input v-model.number="upper" type="range" min="-3" max="5" step="0.1" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p v-if="analysis.status === 'infeasible'" class="is-bad">Miền khả thi rỗng: không có x nào thỏa đồng thời mọi điều kiện. Theo quy ước, p* = +∞.</p>
      <template v-else-if="analysis.status === 'attained'">
        <p>Giá trị tối ưu p* = <span class="is-accent">{{ fmt(analysis.value, 4) }}</span>, đạt tại x* = {{ fmt(analysis.x, 4) }}.</p>
        <p v-if="activeBound">Nghiệm nằm đúng trên cận {{ activeBound }}, nên ràng buộc đó chặt (active) tại x*. Bỏ ràng buộc này đi thì nghiệm sẽ thay đổi.</p>
        <p v-else>Không ràng buộc nào chặt tại x*: nghiệm nằm bên trong miền khả thi.</p>
        <p v-if="localMins.length > 1">Trên miền này có hai điểm cực tiểu cục bộ (vòng tròn rỗng). Chỉ một điểm là tối ưu toàn cục.</p>
      </template>
      <p v-else-if="analysis.status === 'not-attained'" class="is-bad">Cận dưới lớn nhất là p* = 0, nhưng không có x khả thi nào đạt giá trị 0: với mọi x &gt; 0, điểm 2x cho giá trị nhỏ hơn.</p>
      <p v-else class="is-bad">Hàm mục tiêu giảm không giới hạn trên miền khả thi: p* = −∞, bài toán không bị chặn dưới.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Với (x − 3)², đặt u = 1 rồi kéo u lên quá 3. Khi nào ràng buộc x ≤ u thôi chặt?</li>
        <li>Chọn 1/x và bỏ ràng buộc x ≤ u. Vì sao không có nghiệm dù p* hữu hạn?</li>
        <li>Chọn −log x và bỏ ràng buộc x ≤ u. Điều gì khác với trường hợp 1/x?</li>
        <li>Chọn hàm bậc bốn, đặt l = 0. Nghiệm nhảy sang điểm nào, và vì sao điểm −1.47 không còn được xét?</li>
        <li>Đặt l lớn hơn u. Máy báo gì?</li>
      </ol>
    </details>
  </figure>
</template>
