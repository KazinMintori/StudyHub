<script setup>
import { computed, ref, watch, useId } from 'vue'
import LabPointControls from './LabPointControls.vue'
import {convexHull,clipPolygon} from '../services/convex-geometry.mjs'
import { makeView, createDragger, fmt } from '../controllers/svg-drag.js'
const svg=ref(null)
const clipId = `${useId()}-clip`

// Mô phỏng cho hàm một biến.
// type="chord": bất đẳng thức dây cung. type="tangent": tiếp tuyến và cận dưới toàn cục.
// type="epigraph": epigraph và tập mức dưới. type="jensen": f(E x) so với E f(x).
const props = defineProps({ type: { type: String, default: 'chord' }, initial: { type: String, default: '' } })
const catalog = {
  sq: { label: 'x²', f: x => x * x, df: x => 2 * x, dom: () => true, y: [-1.5, 6], convex: true },
  abs: { label: '|x|', f: x => Math.abs(x), df: x => Math.sign(x), dom: () => true, y: [-1.5, 3.5], convex: true, kink: 0 },
  exp: { label: 'eˣ', f: x => Math.exp(x), df: x => Math.exp(x), dom: () => true, y: [-1, 7], convex: true },
  negLog: { label: '−log x (x > 0)', f: x => -Math.log(x), df: x => -1 / x, dom: x => x > 0, y: [-2, 4], convex: true },
  xlogx: { label: 'x log x (x > 0)', f: x => x * Math.log(x), df: x => Math.log(x) + 1, dom: x => x > 0, y: [-1, 4], convex: true },
  quartic: { label: 'x⁴', f: x => x ** 4, df: x => 4 * x ** 3, dom: () => true, y: [-1, 6], convex: true },
  cube: { label: 'x³', f: x => x ** 3, df: x => 3 * x * x, dom: () => true, y: [-5, 5], convex: false },
  negSq: { label: '−x²', f: x => -x * x, df: x => -2 * x, dom: () => true, y: [-5, 1.5], convex: false },
  wavy: { label: '0.3x² + sin(1.5x)', f: x => 0.3 * x * x + Math.sin(1.5 * x), df: x => 0.6 * x + 1.5 * Math.cos(1.5 * x), dom: () => true, y: [-2, 4], convex: false },
  invSq: { label: '1/x² (x ≠ 0)', f: x => 1 / (x * x), df: x => -2 / x ** 3, dom: x => Math.abs(x) > 1e-9, y: [-1, 6], convex: false },
  negExp: { label: '−eˣ', f: x => -Math.exp(x), df: x => -Math.exp(x), dom: () => true, y: [-7, 1], convex: false }
}
const lists = {
  chord: ['sq', 'abs', 'exp', 'negLog', 'cube', 'wavy', 'invSq'],
  tangent: ['sq', 'abs', 'exp', 'negLog', 'xlogx', 'quartic', 'cube', 'wavy', 'invSq'],
  epigraph: ['sq', 'abs', 'exp', 'wavy', 'negExp', 'cube'],
  jensen: ['sq', 'exp', 'abs', 'negLog', 'negSq']
}
const choice = ref(props.initial && lists[props.type].includes(props.initial) ? props.initial : lists[props.type][0])
const fn = computed(() => catalog[choice.value])
const view = computed(() => makeView({ x0: -3, x1: 3, y0: fn.value.y[0], y1: fn.value.y[1], width: 400, height: 300, pad:24 }))
const P = (x, y) => [view.value.sx(x), view.value.sy(y)]
const inView = y => y >= view.value.y0 - 0.5 && y <= view.value.y1 + 0.5
const curveSegments = computed(() => {
  const segs = [[]]
  for (let i = 0; i <= 480; i++) {
    const x = -3 + (6 * i) / 480
    if (!fn.value.dom(x) || !inView(fn.value.f(x))) { if (segs.at(-1).length) segs.push([]); continue }
    segs.at(-1).push(P(x, fn.value.f(x)).join(','))
  }
  return segs.filter(s => s.length > 1).map(s => s.join(' '))
})

// --- chord ---
const a = ref(-1.5), b = ref(2), theta = ref(0.4)
const z = computed(() => theta.value * a.value + (1 - theta.value) * b.value)
const endpointsOk = computed(() => fn.value.dom(a.value) && fn.value.dom(b.value))
const segmentInDomain=computed(()=>endpointsOk.value&&(choice.value!=='invSq'||a.value*b.value>0))
const chordValue = computed(() => theta.value * fn.value.f(a.value) + (1 - theta.value) * fn.value.f(b.value))
const graphValue = computed(() => (fn.value.dom(z.value) ? fn.value.f(z.value) : NaN))
const worstGap = computed(() => {
  if (!endpointsOk.value || !segmentInDomain.value) return null
  let best = { gap: -Infinity, t: 0 }
  for (let i = 1; i < 200; i++) { const t = i / 200, zz = t * a.value + (1 - t) * b.value, gap = fn.value.f(zz) - (t * fn.value.f(a.value) + (1 - t) * fn.value.f(b.value)); if (gap > best.gap) best = { gap, t } }
  return best
})

// --- tangent ---
const x0 = ref(0.8), sub = ref(0.3)
watch(choice, key => { if (catalog[key].dom(x0.value) === false) x0.value = 1 })
const slope = computed(() => (fn.value.kink !== undefined && Math.abs(x0.value - fn.value.kink) < 1e-9 ? sub.value : fn.value.df(x0.value)))
const tangentAt = x => fn.value.f(x0.value) + slope.value * (x - x0.value)
const violations = computed(() => {
  if (!fn.value.dom(x0.value)) return []
  const out = []
  for (let i = 0; i <= 300; i++) { const x = -3 + (6 * i) / 300; if (fn.value.dom(x) && tangentAt(x) > fn.value.f(x) + 1e-9) out.push(x) }
  return out
})

// --- epigraph ---
const alpha = ref(2)
// Epigraph trong khung nhìn: kẹp đồ thị vào khung để phần nằm dưới đáy khung vẫn được tô kín cột.
const epiPolygons = computed(() => {
  const v = view.value, polys = [[]]
  for (let i = 0; i <= 480; i++) {
    const x = -3 + (6 * i) / 480
    if (!fn.value.dom(x)) { if (polys.at(-1).length) polys.push([]); continue }
    const y = Math.min(Math.max(fn.value.f(x), v.y0), v.y1)
    polys.at(-1).push([v.sx(x), v.sy(y)])
  }
  return polys.filter(p=>p.length>1).map(p=>clipFrame([[p[0][0],24],...p,[p.at(-1)[0],24]]).map(q=>q.join(',')).join(' '))
})
const sublevel = computed(() => {
  const intervals = []
  let start = null
  for (let i = 0; i <= 600; i++) {
    const x = -3 + (6 * i) / 600, ok = fn.value.dom(x) && fn.value.f(x) <= alpha.value
    if (ok && start === null) start = x
    if (!ok && start !== null) { intervals.push([start, -3 + (6 * (i - 1)) / 600]); start = null }
  }
  if (start !== null) intervals.push([start, 3])
  return intervals
})

// --- jensen ---
const pts = ref([-2, 0.5, 2]), probs = ref([0.3, 0.5])
const p3 = computed(() => Math.max(0, 1 - probs.value[0] - probs.value[1]))
watch(()=>probs.value[0],p=>{probs.value[1]=Math.min(probs.value[1],1-p)})
watch(()=>probs.value[1],p=>{probs.value[0]=Math.min(probs.value[0],1-p)})
const weights = computed(() => { const raw = [probs.value[0], probs.value[1], p3.value], s = raw.reduce((u, v) => u + v, 0); return raw.map(v => v / s) })
const jensenOk = computed(() => pts.value.every(x => fn.value.dom(x)))
const mean = computed(() => weights.value.reduce((s, w, i) => s + w * pts.value[i], 0))
const meanF = computed(() => weights.value.reduce((s, w, i) => s + w * fn.value.f(pts.value[i]), 0))
const fMean = computed(() => fn.value.f(mean.value))

const handleY=x=>fn.value.dom(x)&&fn.value.f(x)>=view.value.y0&&fn.value.f(x)<=view.value.y1?fn.value.f(x):0
const handles=computed(()=>props.type==='chord'?[{key:'a',point:[a.value,handleY(a.value)],label:'Đầu mút a'},{key:'b',point:[b.value,handleY(b.value)],label:'Đầu mút b'}]:props.type==='tangent'?[{key:'x0',point:[x0.value,handleY(x0.value)],label:'Điểm tiếp xúc x₀'}]:props.type==='epigraph'?[{key:'alpha',point:[2.45,alpha.value],label:'Mức α của lát cắt'}]:pts.value.map((x,i)=>({key:String(i),point:[x,handleY(x)],label:`Giá trị x${i+1}`})))
const handleText=h=>h.key==='alpha'?`α = ${fmt(alpha.value,4)}`:`x = ${fmt(h.point[0],4)}`
const drag=createDragger(svg,view,(name,p)=>{
 const x=Math.max(-2.8,Math.min(2.8,p[0]))
 if(name==='a')a.value=x
 else if(name==='b')b.value=x
 else if(name==='x0')x0.value=x
 else if(name==='alpha')alpha.value=p[1]
 else pts.value=pts.value.map((v,i)=>String(i)===name?x:v)
},{step:.1})
const clipFrame=poly=>{for(const [a,b]of [[[1,0],400],[[-1,0],0],[[0,1],300],[[0,-1],0]])poly=clipPolygon(poly,a,b);return poly}
const jensenHull=computed(()=>jensenOk.value?clipFrame(convexHull(pts.value.map(x=>P(x,fn.value.f(x))))):[])
const clippedCurves=computed(()=>curveSegments.value.map(segment=>segment.split(' ').map(p=>p.split(',').map(Number)).filter(p=>p[1]>=0&&p[1]<=300).map(p=>p.join(',')).join(' ')))

const titles = { chord: 'Đồ thị và dây cung', tangent: 'Tiếp tuyến tại một điểm', epigraph: 'Epigraph và tập mức dưới', jensen: 'Bất đẳng thức Jensen' }
</script>

<template>
  <figure class="study-lab" :aria-label="titles[type]">
    <p class="lab-title">{{ titles[type] }}</p>
    <p class="lab-lead">Kéo trực tiếp chấm tím để đổi vị trí hoặc mức cắt. Nếu giá trị hàm ra ngoài khung hoặc không xác định, nút kéo nằm trên trục hoành để bạn vẫn đổi được đầu vào. Nút này không đại diện cho giá trị hàm khi ở trên trục.</p>
    <svg ref="svg" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end" :viewBox="`0 0 ${view.width} ${view.height + 30}`" role="group" :aria-label="`Đồ thị hàm ${fn.label}`">
      <defs><clipPath :id="clipId"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath></defs>
      <line v-for="x in [-2, -1, 1, 2]" :key="`gx${x}`" :x1="view.sx(x)" :x2="view.sx(x)" y1="0" :y2="view.height" class="lab-grid" />
      <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
      <text v-for="x in [-2, -1, 1, 2]" :key="`tx${x}`" :x="view.sx(x)" :y="view.height + 20" text-anchor="middle" class="lab-small">{{ x }}</text>
      <g :clip-path="`url(#${clipId})`">
        <template v-if="type === 'epigraph'">
          <polygon v-for="(poly, i) in epiPolygons" :key="`e${i}`" :points="poly" class="lab-region-soft" />
          <line x1="0" :x2="view.width" :y1="view.sy(alpha)" :y2="view.sy(alpha)" class="lab-warn" />
          <line v-for="(iv, i) in sublevel" :key="`s${i}`" :x1="view.sx(iv[0])" :x2="view.sx(iv[1])" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-good" style="stroke-width: 3" />
        </template>
        <polyline v-for="(seg, i) in clippedCurves" :key="i" :points="seg" class="lab-line" style="stroke-width: 2.5" />
        <template v-if="type === 'chord' && endpointsOk">
          <line :x1="P(a, fn.f(a))[0]" :y1="P(a, fn.f(a))[1]" :x2="P(b, fn.f(b))[0]" :y2="P(b, fn.f(b))[1]" class="lab-accent" />
          <line v-if="Number.isFinite(graphValue)" :x1="P(z, graphValue)[0]" :y1="P(z, graphValue)[1]" :x2="P(z, chordValue)[0]" :y2="P(z, chordValue)[1]" :class="graphValue <= chordValue + 1e-9 ? 'lab-good' : 'lab-bad'" />
          <circle :cx="P(a, fn.f(a))[0]" :cy="P(a, fn.f(a))[1]" r="5" class="lab-dot" /><circle :cx="P(b, fn.f(b))[0]" :cy="P(b, fn.f(b))[1]" r="5" class="lab-dot" />
          <circle v-if="Number.isFinite(graphValue)" :cx="P(z, graphValue)[0]" :cy="P(z, graphValue)[1]" r="6" class="lab-dot-warn" />
          <circle :cx="P(z, chordValue)[0]" :cy="P(z, chordValue)[1]" r="6" class="lab-dot-hollow" />
        </template>
        <template v-if="type === 'tangent' && fn.dom(x0)">
          <line :x1="P(-3, tangentAt(-3))[0]" :y1="P(-3, tangentAt(-3))[1]" :x2="P(3, tangentAt(3))[0]" :y2="P(3, tangentAt(3))[1]" class="lab-accent" />
          <circle v-for="x in violations" :key="`v${x}`" :cx="P(x, tangentAt(x))[0]" :cy="P(x, tangentAt(x))[1]" r="2.5" class="lab-dot-bad" />
          <circle :cx="P(x0, fn.f(x0))[0]" :cy="P(x0, fn.f(x0))[1]" r="7" class="lab-dot-warn" />
        </template>
        <template v-if="type === 'jensen' && jensenOk">
          <polygon :points="jensenHull.map(p=>p.join(',')).join(' ')" class="lab-region-soft" />
          <circle v-for="(x, i) in pts" :key="`j${i}`" :cx="P(x, fn.f(x))[0]" :cy="P(x, fn.f(x))[1]" :r="4 + 10 * weights[i]" class="lab-dot" />
          <line :x1="P(mean, fMean)[0]" :y1="P(mean, fMean)[1]" :x2="P(mean, meanF)[0]" :y2="P(mean, meanF)[1]" :class="meanF >= fMean - 1e-9 ? 'lab-good' : 'lab-bad'" />
          <circle :cx="P(mean, fMean)[0]" :cy="P(mean, fMean)[1]" r="6" class="lab-dot-warn" />
          <circle :cx="P(mean, meanF)[0]" :cy="P(mean, meanF)[1]" r="6" class="lab-dot-hollow" />
        </template>
      </g>
      <g v-for="h in handles" :key="h.key">
        <circle :cx="P(...h.point)[0]" :cy="P(...h.point)[1]" r="7" class="lab-dot-accent"/>
        <circle :cx="P(...h.point)[0]" :cy="P(...h.point)[1]" r="27" class="lab-handle hit" tabindex="0" role="slider" :aria-label="h.label" :aria-valuetext="handleText(h)" @pointerdown="drag.start(h.key,$event)" @keydown="drag.key(h.key,h.point,$event)"/>
      </g>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
    <div class="lab-controls">
      <label>Hàm f(x) = <select v-model="choice"><option v-for="key in lists[type]" :key="key" :value="key">{{ catalog[key].label }}</option></select></label>
      <template v-if="type === 'chord'">
        <label>a = {{ fmt(a) }}<input v-model.number="a" type="range" min="-2.8" max="2.8" step="0.05" /></label>
        <label>b = {{ fmt(b) }}<input v-model.number="b" type="range" min="-2.8" max="2.8" step="0.05" /></label>
        <label>θ = {{ fmt(theta) }}<input v-model.number="theta" type="range" min="0" max="1" step="0.01" /></label>
      </template>
      <template v-if="type === 'tangent'">
        <label>x₀ = {{ fmt(x0) }}<input v-model.number="x0" type="range" min="-2.8" max="2.8" step="0.05" /></label>
        <label v-if="fn.kink !== undefined && Math.abs(x0 - fn.kink) < 1e-9">Độ dốc chọn tại điểm gãy: {{ fmt(sub) }}<input v-model.number="sub" type="range" min="-1.5" max="1.5" step="0.05" /></label>
      </template>
      <label v-if="type === 'epigraph'">α = {{ fmt(alpha) }}<input v-model.number="alpha" type="range" :min="fn.y[0]" :max="fn.y[1]" step="0.05" /></label>
      <template v-if="type === 'jensen'">
        <label v-for="(x, i) in pts" :key="`px${i}`">x{{ ['₁', '₂', '₃'][i] }} = {{ fmt(x) }}<input v-model.number="pts[i]" type="range" min="-2.8" max="2.8" step="0.05" /></label>
        <label>P(x₁) = {{ fmt(weights[0]) }}<input v-model.number="probs[0]" type="range" min="0" max="1" step="0.01" /></label>
        <label>P(x₂) = {{ fmt(weights[1]) }}<input v-model.number="probs[1]" type="range" min="0" max="1" step="0.01" /></label>
      </template>
    </div>
    <div class="lab-readout" role="status">
      <template v-if="type === 'chord'">
        <p v-if="!endpointsOk" class="is-bad">Một đầu mút nằm ngoài miền xác định của hàm.</p>
        <p v-else-if="!segmentInDomain" class="is-bad">Đoạn [a, b] đi qua điểm không thuộc miền xác định: miền không lồi, nên hàm không thể lồi dù đạo hàm bậc hai dương ở mọi nơi nó xác định.</p>
        <template v-else>
          <p>Tại z = θa + (1 − θ)b = {{ fmt(z) }}: f(z) = {{ fmt(graphValue) }}, còn dây cung cho θf(a) + (1 − θ)f(b) = {{ fmt(chordValue) }}. <span :class="graphValue <= chordValue + 1e-9 ? 'is-good' : 'is-bad'">{{ graphValue <= chordValue + 1e-9 ? 'Đồ thị nằm dưới dây cung.' : 'Đồ thị vượt lên trên dây cung.' }}</span></p>
          <p v-if="worstGap && worstGap.gap > 1e-6" class="is-bad">Với cặp a, b này, mức vi phạm lớn nhất trên lưới lấy mẫu là {{ fmt(worstGap.gap, 3) }} tại θ ≈ {{ fmt(worstGap.t) }}. Chỉ một vi phạm là đủ để kết luận hàm không lồi.</p>
          <p v-else>Các điểm lấy mẫu trên đoạn này chưa vi phạm dây cung. Đây là phép thử hữu hạn, không phải chứng minh cho cả đoạn. Định nghĩa còn đòi điều đó với mọi cặp a, b.</p>
        </template>
      </template>
      <template v-if="type === 'tangent'">
        <p v-if="!fn.dom(x0)" class="is-bad">x₀ nằm ngoài miền xác định.</p>
        <template v-else>
          <p>Tiếp tuyến tại x₀ = {{ fmt(x0) }}: y = {{ fmt(fn.f(x0)) }} + ({{ fmt(slope) }})(x − x₀).</p>
          <p v-if="violations.length" class="is-bad">Tiếp tuyến vượt lên trên đồ thị ở những điểm đỏ, nên nó không phải cận dưới toàn cục.</p>
          <p v-else class="is-good">Trên cả khung nhìn, tiếp tuyến nằm dưới (hoặc chạm) đồ thị.</p>
          <p v-if="fn.kink !== undefined && Math.abs(x0 - fn.kink) < 1e-9">Tại điểm gãy, hàm không có đạo hàm. Mọi độ dốc trong đoạn [−1, 1] vẫn cho một đường thẳng nằm dưới đồ thị, gọi là một dưới đạo hàm.</p>
        </template>
      </template>
      <template v-if="type === 'epigraph'">
        <p>Phần tập mức dưới trong khung {x : f(x) ≤ {{ fmt(alpha) }}} (vạch xanh trên trục) gồm {{ sublevel.length }} khoảng{{ sublevel.length ? ': ' + sublevel.map(iv => `[${fmt(iv[0])}, ${fmt(iv[1])}]`).join(', ') : '' }}{{ sublevel.some(iv => iv[1] >= 2.99 || iv[0] <= -2.99) ? ' (kéo dài ra ngoài khung nhìn)' : '' }}.</p>
        <p>{{ sublevel.length <= 1 ? 'Phần tập mức dưới trong khung là một khoảng hoặc rỗng, nên lồi.' : 'Tập mức dưới gồm nhiều khoảng rời nhau, không lồi.' }} {{ choice === 'negExp' ? 'Hàm −eˣ lõm, vậy mà mọi tập mức dưới của nó đều lồi: chiều ngược của mệnh đề không đúng.' : '' }}</p>
      </template>
      <template v-if="type === 'jensen'">
        <p v-if="!jensenOk" class="is-bad">Có điểm nằm ngoài miền xác định.</p>
        <template v-else>
          <p>E x = {{ fmt(mean) }}, f(E x) = <span class="is-accent">{{ fmt(fMean) }}</span> (điểm vàng), còn E f(x) = {{ fmt(meanF) }} (vòng tròn rỗng).</p>
          <p><span :class="meanF >= fMean - 1e-9 ? 'is-good' : 'is-bad'">E f(x) − f(E x) = {{ fmt(meanF - fMean, 3) }}</span>. {{ catalog[choice].convex ? 'Với hàm lồi, hiệu này luôn không âm.' : 'Hàm này lõm, nên chiều bất đẳng thức đảo lại.' }}</p>
        </template>
      </template>
    </div>
  </figure>
</template>

<style scoped>
svg text{font-size:20px;pointer-events:none}svg .lab-small{font-size:18px}
svg :is(line,path,polyline,polygon),svg circle:not(.lab-handle){pointer-events:none}
.hit{fill:transparent!important;stroke:transparent}.hit:focus-visible{stroke:var(--vang)}
</style>
