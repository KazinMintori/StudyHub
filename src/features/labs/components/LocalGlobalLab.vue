<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt } from '../controllers/svg-drag.js'
import LabPointControls from './LabPointControls.vue'

// Minh họa lời chứng minh "cục bộ suy ra toàn cục" của §4.2.2. Nếu x tối ưu trong bán kính R
// nhưng có điểm khả thi y tốt hơn, điểm z = x + θ(y − x) với |z − x| = R/2 phải khả thi
// (miền lồi) và có f(z) ≤ dây cung < f(x) (hàm lồi), mâu thuẫn. Lab chỉ ra giả thiết nào hỏng.
const fns = {
  rawwell: { label:'x⁴ − 4x² + x',f:x=>x**4-4*x*x+x,convex:false,y:[-6,7] },
  quad: { label: '½(x − 1)²', f: x => 0.5 * (x - 1) ** 2, convex: true, y: [-0.5, 5] },
  absq: { label: '|x − 0.5| + 0.2x²', f: x => Math.abs(x - 0.5) + 0.2 * x * x, convex: true, y: [-0.3, 5] },
  well: { label: '0.25x⁴ − x² + 0.3x', f: x => 0.25 * x ** 4 - x * x + 0.3 * x, convex: false, y: [-2, 4] },
  wavy: { label: '0.3x² + sin(1.5x)', f: x => 0.3 * x * x + Math.sin(1.5 * x), convex: false, y: [-1.5, 4] }
}
const sets = {
  all: { label: 'toàn đoạn [−3, 3]', pieces: [[-3, 3]], convex: true },
  box: { label: 'đoạn [−0.5, 2.5]', pieces: [[-0.5, 2.5]], convex: true },
  two: { label: 'hai đoạn [−3, −1.2] ∪ [1.6, 3]', pieces: [[-3, -1.2], [1.6, 3]], convex: false }
}
const props=defineProps({initialFunction:{type:String,default:'well'}})
const fKey = ref(props.initialFunction in fns?props.initialFunction:'well'), sKey = ref('all')
const x0 = ref(fKey.value==='rawwell'?1.3469974085277738:1.33), R = ref(0.6)
const fn = computed(() => fns[fKey.value]), S = computed(() => sets[sKey.value])
const feasible = x => S.value.pieces.some(([a, b]) => x >= a - 1e-12 && x <= b + 1e-12)
const clip = `${useId()}-lg-clip`
const view = computed(() => makeView({ x0: -3, x1: 3, y0: fn.value.y[0], y1: fn.value.y[1], width: 460, height: 280 }))
const P = (x, y) => [view.value.sx(x), view.value.sy(y)]
const grid = Array.from({ length: 1201 }, (_, i) => -3 + (6 * i) / 1200)
const curve = computed(() => {
  const segments=[[]]
  for(const x of grid){
    const y=fn.value.f(x)
    if(y>=view.value.y0&&y<=view.value.y1)segments.at(-1).push(P(x,y).join(','))
    else if(segments.at(-1).length)segments.push([])
  }
  return segments.filter(segment=>segment.length>1).map(segment=>segment.join(' '))
})
const fx = computed(() => fn.value.f(x0.value))
const x0Feasible = computed(() => feasible(x0.value))
// Sai số 2e-4 bù cho bước 0.01 của thanh trượt: x lệch đáy giếng một chút vẫn được xem là cực tiểu.
const isLocal = computed(() => x0Feasible.value && grid.every(z => !feasible(z) || Math.abs(z - x0.value) > R.value || fn.value.f(z) >= fx.value - 2e-4))
const best = computed(() => { let b = null; for (const z of grid) if (feasible(z) && (b === null || fn.value.f(z) < fn.value.f(b))) b = z; return b })
const isGlobal = computed(() => x0Feasible.value && fx.value <= fn.value.f(best.value) + 2e-4)
// Khi x cục bộ mà không toàn cục: dựng z trên đoạn từ x tới y = điểm tốt nhất.
const proof = computed(() => {
  if (!isLocal.value || isGlobal.value) return null
  const y = best.value, d = Math.abs(y - x0.value), theta = R.value / (2 * d)
  const z = x0.value + theta * (y - x0.value)
  const chord = (1 - theta) * fx.value + theta * fn.value.f(y)
  return { y, z, chord, fz: fn.value.f(z), zFeasible: feasible(z) }
})
const svg=ref(null)
const drag=createDragger(svg,view,(name,p)=>{if(name==='radius')R.value=Math.max(.1,Math.min(1.5,Math.abs(p[0]-x0.value)));else x0.value=p[0]},{step:.05,snap:.01})
const handleY=computed(()=>Math.max(26,Math.min(view.value.height-28,view.value.sy(fx.value))))
</script>

<template>
  <figure class="study-lab" aria-label="Cực tiểu cục bộ và cực tiểu toàn cục">
    <p class="lab-title">Vì sao cục bộ kéo theo toàn cục, và khi nào không</p>
    <p class="lab-lead">Kéo điểm x dọc đồ thị để đổi vị trí đang xét. Đổi bán kính R để so sánh một lân cận nhỏ với toàn miền. Các đánh giá số dùng một lưới hữu hạn và được phân biệt với định lý tổng quát.</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="group" aria-label="Đồ thị hàm, miền khả thi, điểm x kéo được và lân cận bán kính R" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
      <defs><clipPath :id="clip"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath></defs>
      <g :clip-path="`url(#${clip})`">
        <rect :x="view.sx(x0 - R)" y="0" :width="view.sx(x0 + R) - view.sx(x0 - R)" :height="view.height" class="lab-region-soft" style="opacity: 0.45" />
        <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
        <line v-for="(p, i) in S.pieces" :key="`s${i}`" :x1="view.sx(p[0])" :x2="view.sx(p[1])" :y1="view.height - 6" :y2="view.height - 6" class="lab-good" style="stroke-width: 6" />
        <polyline v-for="(segment,index) in curve" :key="'curve'+index" :points="segment" class="lab-line" style="stroke-width: 2.5" />
        <template v-if="proof">
          <line :x1="P(x0, fx)[0]" :y1="P(x0, fx)[1]" :x2="P(proof.y, fn.f(proof.y))[0]" :y2="P(proof.y, fn.f(proof.y))[1]" class="lab-accent" style="stroke-width: 2" />
          <line :x1="P(proof.z, proof.chord)[0]" :y1="P(proof.z, proof.chord)[1]" :x2="P(proof.z, proof.fz)[0]" :y2="P(proof.z, proof.fz)[1]" class="lab-bad" />
          <circle :cx="P(proof.z, proof.fz)[0]" :cy="P(proof.z, proof.fz)[1]" r="5.5" :class="proof.zFeasible ? 'lab-dot-bad' : 'lab-dot-hollow'" />
          <circle :cx="P(proof.y, fn.f(proof.y))[0]" :cy="P(proof.y, fn.f(proof.y))[1]" r="6" class="lab-dot" />
        </template>
        <circle :cx="P(x0, fx)[0]" :cy="P(x0, fx)[1]" r="7" class="lab-dot-warn" />
      </g>
      <circle :cx="view.sx(x0)" :cy="handleY" r="34" class="lab-handle point-hit" tabindex="0" role="slider" aria-label="Điểm x đang khảo sát" aria-valuemin="-3" aria-valuemax="3" :aria-valuenow="x0" :aria-valuetext="`x = ${fmt(x0)}, f(x) = ${fmt(fx,3)}`" @pointerdown="drag.start('x',$event)" @keydown="drag.key('x',[x0,0],$event)"/>
    </svg>
    <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg" axes="x"/></details>
    <p class="lab-legend"><span class="legend-good">miền khả thi</span><span class="legend-accent">dây cung từ x tới điểm tốt nhất y</span><span class="legend-bad">khoảng cách giữa đồ thị và dây cung tại z</span></p>
    <div class="lab-controls">
      <label>Hàm f(x) = <select v-model="fKey"><option v-for="(item, key) in fns" :key="key" :value="key">{{ item.label }}</option></select></label>
      <label>Miền khả thi <select v-model="sKey"><option v-for="(item, key) in sets" :key="key" :value="key">{{ item.label }}</option></select></label>
      <label>x = {{ fmt(x0) }}<input v-model.number="x0" type="range" min="-3" max="3" step="0.01" /></label>
      <label>Bán kính lân cận R = {{ fmt(R) }}<input v-model.number="R" type="range" min="0.1" max="1.5" step="0.05" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p v-if="!x0Feasible" class="is-bad">x nằm ngoài miền khả thi.</p>
      <template v-else>
        <p>f(x) = {{fmt(fx,3)}}. Trên lưới kiểm tra trong bán kính R, {{isLocal?'chưa tìm thấy điểm tốt hơn x ngoài sai số so sánh.':'có điểm cho giá trị nhỏ hơn x.'}} Trên lưới của toàn miền, {{isGlobal?'x có giá trị gần mức nhỏ nhất tìm được.':`có điểm tốt hơn tại y ≈ ${fmt(best)}, f(y) = ${fmt(fn.f(best),3)}.`}}</p>
        <p v-if="view.sy(fx)<0||view.sy(fx)>view.height">Giá trị f(x) nằm ngoài thang dọc. Vùng nhận kéo được đặt gần mép khung, còn giá trị thật được ghi ở trên.</p>
        <template v-if="proof">
          <p>Lời chứng minh lấy z = {{ fmt(proof.z) }} trên đoạn từ x tới y, cách x đúng R/2.</p>
          <p v-if="!proof.zFeasible" class="is-bad">z không khả thi: miền khả thi không lồi, nên đoạn nối hai điểm khả thi đi ra ngoài miền. Lời chứng minh hỏng ở bước này.</p>
          <p v-else-if="proof.fz > proof.chord + 1e-9" class="is-bad">z khả thi, nhưng f(z) = {{ fmt(proof.fz, 3) }} lớn hơn giá trị {{ fmt(proof.chord, 3) }} của dây cung: đồ thị vượt lên trên dây cung, tức f không lồi. Lời chứng minh hỏng ở bước này.</p>
        </template>
        <p v-else-if="isLocal && isGlobal && fn.convex && S.convex" class="is-good">Hàm lồi trên miền lồi: điểm tốt nhất trong một lân cận cũng là điểm tốt nhất trên toàn miền.</p>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Với hàm 0.25x⁴ − x² + 0.3x, đặt x gần 1.33. Vì sao nó là cực tiểu cục bộ mà không toàn cục? Quan sát điểm z và dây cung.</li>
        <li>Chọn ½(x − 1)² với miền gồm hai đoạn, rồi đặt x = −1.2. Hàm lồi, vậy chỗ nào trong lời chứng minh bị hỏng?</li>
        <li>Với ½(x − 1)² trên miền lồi, thử tìm một điểm cực tiểu cục bộ không toàn cục. Vì sao không tìm được?</li>
      </ol>
    </details>
  </figure>
</template>

<style scoped>
.point-hit{fill:transparent!important;stroke:transparent}
.point-hit:focus-visible{stroke:var(--vang)}
svg text{pointer-events:none}
</style>
