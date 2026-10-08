<script setup>
import { computed, ref, watch, useId } from 'vue'
import { mix, quadratic, dualCertificate, optimizerTrace, solveSmallLP, bellmanTrace, dag } from './math-ai.mjs'
import MathText from './MathText.vue'
import { mathLabels } from '../math-labels.mjs'
const props=defineProps({ type:{type:String,required:true}, initialMethod:{type:String,default:'gd'} })
const theta=ref(.5), concave=ref(false), lambda=ref(2), method=ref(props.initialMethod), rate=ref(.15), kappa=ref(10), momentum=ref(.8), step=ref(0), c1=ref(3), c2=ref(2), longest=ref(false)
const names={gd:'Gradient',newton:'Newton',momentum:'Momentum',nesterov:'Nesterov',adagrad:'AdaGrad',rmsprop:'RMSProp',adam:'Adam'}
const trace=computed(()=>optimizerTrace({method:method.value,rate:rate.value,kappa:kappa.value,momentum:momentum.value})), row=computed(()=>trace.value[step.value])
watch([method,rate,kappa,momentum],()=>{step.value=0})
const a=[-1,1],b=[2,-1], point=computed(()=>mix(a,b,theta.value))
const sign=computed(()=>concave.value?-1:1), f=x=>sign.value*x*x
const z=computed(()=>theta.value*(-1)+(1-theta.value)*2), chord=computed(()=>theta.value*f(-1)+(1-theta.value)*f(2))
const cx=x=>60+(x+2)*65, cy=y=>175-y*27
const curve=computed(()=>Array.from({length:81},(_,i)=>{const x=-1.7+i*.05;return `${cx(x)},${cy(f(x))}`}).join(' '))
const certificate=computed(()=>dualCertificate(lambda.value)), lp=computed(()=>solveSmallLP([c1.value,c2.value]))
const bellman=computed(()=>bellmanTrace(dag,['T','B','A','S'],'T',longest.value)), bellmanStep=ref(0)
watch(longest,()=>{bellmanStep.value=0})
const nodes=[{id:'S',x:45,y:110},{id:'A',x:145,y:40},{id:'B',x:245,y:150},{id:'T',x:345,y:80}]
const arrowId=`math-dag-${useId()}`
const edgeLabels={'S-A':[90,59],'S-B':[135,154],'A-B':[184,89],'A-T':[245,34],'B-T':[308,140]}
const dagEdges=nodes.flatMap(from=>dag[from.id].map(([to,cost])=>{
  const target=nodes.find(n=>n.id===to),dx=target.x-from.x,dy=target.y-from.y,length=Math.hypot(dx,dy)
  return {from:from.id,to,cost,x1:from.x+18*dx/length,y1:from.y+18*dy/length,x2:target.x-18*dx/length,y2:target.y-18*dy/length,label:edgeLabels[`${from.id}-${to}`]}
}))
const visible=computed(()=>trace.value.slice(0,step.value+1).filter(r=>r.x.every(Number.isFinite)&&r.x.every(x=>Math.abs(x)<=3)))
const visibleSegments=computed(()=>{
  const rows=trace.value.slice(0,step.value+1)
  return rows.slice(1).flatMap((to,i)=>{
    const from=rows[i],inside=row=>row.x.every(x=>Number.isFinite(x)&&Math.abs(x)<=3)
    return inside(from)&&inside(to)?[{from:from.x,to:to.x,iteration:to.iteration}]:[]
  })
})
const px=x=>190+x*50, py=y=>120-y*35
const contours=[.5,2,5,10,20]
const fmt=x=>Number.isFinite(x)?(Math.abs(x)>10000?x.toExponential(2):x.toFixed(4)):'Vượt giới hạn số'
const labTitles={segment:'Từ tổ hợp affine đến đoạn nối',chord:'So hàm với dây cung',optimizer:'Theo dõi từng bước cập nhật',dual:'Một cận dưới đang tốt đến đâu?',lp:'Đổi mục tiêu trên cùng miền khả thi',bellman:'Tính giá trị từ đích về nguồn'}
</script>
<template>
  <figure class="math-lab" :aria-label="labTitles[type]">
    <figcaption>{{ labTitles[type] }}</figcaption>
    <template v-if="type==='segment'">
      <label>θ = {{ theta.toFixed(2) }}<input v-model.number="theta" type="range" min="-.2" max="1.2" step=".05"></label>
      <svg viewBox="0 0 380 210" role="img" aria-label="Đường qua A và B, đoạn nối tô đậm và điểm tổ hợp z">
        <line x1="55" y1="5" x2="325" y2="185" class="axis"/>
        <line x1="100" y1="35" x2="280" y2="155" class="main-line"/>
        <circle cx="100" cy="35" r="5"/><circle cx="280" cy="155" r="5"/>
        <text x="55" y="26">A = (−1,1)</text><text x="225" y="178">B = (2,−1)</text>
        <circle :cx="100+(1-theta)*180" :cy="35+(1-theta)*120" r="7" class="marker"/>
      </svg>
      <p role="status">z = θA + (1−θ)B = ({{ fmt(point[0]) }}, {{ fmt(point[1]) }}). {{ theta>=0&&theta<=1?'z nằm trên đoạn AB.':'z nằm trên đường AB nhưng ngoài đoạn nối.' }}</p>
    </template>
    <template v-else-if="type==='chord'">
      <label>Hàm<select v-model="concave"><option :value="false">f(x) = x²</option><option :value="true">f(x) = −x²</option></select></label>
      <label>θ = {{ theta.toFixed(2) }}<input v-model.number="theta" type="range" min="0" max="1" step=".05"></label>
      <svg viewBox="0 0 380 320" role="img" aria-label="Đồ thị hàm, dây cung nối hai điểm và so sánh chiều cao tại cùng z">
        <line x1="35" y1="175" x2="355" y2="175" class="axis"/><text x="353" y="194">x</text>
        <polyline :points="curve" class="main-line"/>
        <line :x1="cx(-1)" :y1="cy(f(-1))" :x2="cx(2)" :y2="cy(f(2))" class="secondary-line"/>
        <line :x1="cx(z)" :y1="cy(f(z))" :x2="cx(z)" :y2="cy(chord)" class="dashed"/>
        <circle :cx="cx(z)" :cy="cy(f(z))" r="6" class="marker"/>
        <circle :cx="cx(z)" :cy="cy(chord)" r="5" class="hollow"/>
        <text x="35" y="20">Nét liền: f · đoạn thẳng: dây cung</text>
        <text :x="cx(-1)-8" y="194">−1</text><text :x="cx(2)-4" y="194">2</text>
      </svg>
      <p role="status">z = {{ fmt(z) }}, f(z) = {{ fmt(f(z)) }}, còn giá trị dây cung = {{ fmt(chord) }}. {{ concave?'Đồ thị nằm trên dây cung: ví dụ hàm lõm.':'Đồ thị nằm dưới dây cung: ví dụ hàm lồi.' }}</p>
    </template>
    <template v-else-if="type==='optimizer'">
      <div class="lab-inputs"><label>Phương pháp<select v-model="method"><option v-for="(name,id) in names" :key="id" :value="id">{{ name }}</option></select></label>
        <label>η = {{ rate.toFixed(2) }}<input v-model.number="rate" type="range" min=".01" max=".4" step=".01" :disabled="method==='newton'"></label>
        <label>κ = {{ kappa }}<input v-model.number="kappa" type="range" min="1" max="20" step="1"></label>
        <label v-if="method==='momentum'||method==='nesterov'">μ = {{ momentum.toFixed(2) }}<input v-model.number="momentum" type="range" min="0" max=".95" step=".05"></label></div>
      <MathText v-if="mathLabels[method]" as="p" :text="mathLabels[method]" />
      <MathText as="p" :text="mathLabels.quadratic" />
      <svg viewBox="0 0 380 240" role="img" aria-label="Đường đồng mức của hàm toàn phương và các điểm cập nhật">
        <line x1="20" y1="120" x2="365" y2="120" class="axis"/><line x1="190" y1="15" x2="190" y2="225" class="axis"/>
        <ellipse v-for="c in contours" :key="c" cx="190" cy="120" :rx="Math.sqrt(2*c)*50" :ry="Math.sqrt(2*c/kappa)*35" class="contour"/>
        <line v-for="segment in visibleSegments" :key="segment.iteration" :x1="px(segment.from[0])" :y1="py(segment.from[1])" :x2="px(segment.to[0])" :y2="py(segment.to[1])" class="main-line"/>
        <circle v-for="r in visible" :key="r.iteration" :cx="px(r.x[0])" :cy="py(r.x[1])" r="4"/>
        <text x="197" y="139">0</text><text x="355" y="139">x</text><text x="198" y="20">y</text>
      </svg>
      <div class="lab-buttons"><button @click="step=0">Đặt lại</button><button :disabled="step===20" @click="step++">Bước tiếp →</button><label>Bước {{ step }} / 20<input v-model.number="step" type="range" min="0" max="20" step="1"></label></div>
      <p role="status">Bước {{ step }}: ({{ fmt(row.x[0]) }}, {{ fmt(row.x[1]) }}) và f = {{ fmt(row.value) }}.</p>
      <p v-if="trace.slice(0,step+1).some(r=>r.x.some(x=>Math.abs(x)>3))" class="lab-notice">Có điểm vượt vùng vẽ |x|, |y| ≤ 3. Số ở trên vẫn được tính. Chỉ nối hai bước liên tiếp cùng ở trong vùng, còn các bước ra ngoài làm đường đi ngắt đoạn.</p>
      <details v-if="method==='adam'||method==='rmsprop'||method==='adagrad'"><summary>Trạng thái thuật toán ở bước này</summary><p>m = {{ row.m.map(fmt).join(', ') }}, v = {{ row.v.map(fmt).join(', ') }}, còn tổng bình phương = {{ row.sum.map(fmt).join(', ') }}.</p></details>
    </template>
    <template v-else-if="type==='dual'">
      <label>λ = {{ lambda.toFixed(2) }}<input v-model.number="lambda" type="range" min="0" max="4" step=".1"></label>
      <svg viewBox="0 0 380 200" role="img" aria-label="Cận dưới g(lambda) và giá trị khả thi bằng 1">
        <line x1="35" y1="165" x2="350" y2="165" class="axis"/><line x1="35" y1="55" x2="350" y2="55" class="secondary-line"/>
        <polyline :points="Array.from({length:81},(_,i)=>`${35+i*315/80},${165-(i/20-(i/20)**2/4)*110}`).join(' ')" class="main-line"/>
        <circle :cx="35+lambda*315/4" :cy="165-certificate.dual*110" r="6" class="marker"/>
        <text x="38" y="45">f(1) = p* = 1</text><text x="335" y="186">λ</text><text x="31" y="185">0</text><text x="188" y="185">2</text><text x="342" y="185">4</text>
      </svg>
      <p role="status">g(λ) = {{ fmt(certificate.dual) }}, còn f(1)−g(λ) = {{ fmt(certificate.gap) }}. Điểm cực tiểu của L theo x là {{ fmt(certificate.minimizer) }}.</p>
    </template>
    <template v-else-if="type==='lp'">
      <div class="lab-inputs"><label>c₁ = {{ c1 }}<input v-model.number="c1" type="range" min="0" max="5" step="1"></label><label>c₂ = {{ c2 }}<input v-model.number="c2" type="range" min="0" max="5" step="1"></label></div>
      <svg viewBox="0 0 380 250" role="img" aria-label="Miền x+y không vượt 4, x không vượt 2, x và y không âm, cùng các đỉnh tối ưu">
        <line x1="40" y1="220" x2="350" y2="220" class="axis"/><line x1="40" y1="220" x2="40" y2="15" class="axis"/>
        <polygon points="40,220 170,220 170,130 40,40" class="region"/>
        <g v-for="p in lp.vertices" :key="p.point.join(',')"><circle :cx="40+p.point[0]*65" :cy="220-p.point[1]*45" r="5"/><text :x="47+p.point[0]*65" :y="212-p.point[1]*45">({{ p.point.join(',') }})</text></g>
        <circle v-for="p in lp.optimal" :key="p.join(',')" :cx="40+p[0]*65" :cy="220-p[1]*45" r="9" class="hollow"/>
        <text x="341" y="238">x</text><text x="22" y="19">y</text>
      </svg>
      <p role="status">max {{ c1 }}x + {{ c2 }}y = {{ lp.value }}. Đỉnh đạt tối ưu: {{ lp.optimal.map(p=>`(${p.join(',')})`).join(', ') }}. {{ lp.optimal.length>1?'Toàn bộ đoạn nối giữa các đỉnh tối ưu cũng tối ưu.':'' }}</p>
    </template>
    <template v-else-if="type==='bellman'">
      <label>Mục tiêu<select v-model="longest"><option :value="false">Đường ngắn nhất (min)</option><option :value="true">Đường dài nhất (max)</option></select></label>
      <svg viewBox="0 0 390 215" role="img" aria-label="Đồ thị DAG với các cạnh có hướng S đến A, S đến B, A đến B, A đến T, B đến T">
        <defs><marker :id="arrowId" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="arrow-head"/></marker></defs>
        <g v-for="edge in dagEdges" :key="`${edge.from}-${edge.to}`">
          <line :x1="edge.x1" :y1="edge.y1" :x2="edge.x2" :y2="edge.y2" :marker-end="`url(#${arrowId})`" :class="bellman[bellmanStep].actions[edge.from]===edge.to?'main-line':'axis'"/>
          <text :x="edge.label[0]" :y="edge.label[1]" text-anchor="middle">{{ edge.cost }}</text>
        </g>
        <g v-for="n in nodes" :key="n.id"><circle :cx="n.x" :cy="n.y" r="16" class="node"/><text :x="n.x" :y="n.y+5" text-anchor="middle">{{ n.id }}</text><text :x="n.x" :y="n.y+36" text-anchor="middle">V={{ bellman[bellmanStep].values[n.id]??'?' }}</text></g>
      </svg>
      <div class="lab-buttons"><button @click="bellmanStep=0">Đặt lại</button><button :disabled="bellmanStep===3" @click="bellmanStep++">Tính nút tiếp →</button></div>
      <p role="status">Vừa tính nút {{ bellman[bellmanStep].node }}. {{ Object.entries(bellman[bellmanStep].values).map(([n,v])=>`V(${n})=${v}`).join(', ') }}.</p>
    </template>
    <details class="lab-code"><summary>Xem code và điều kiện mô phỏng</summary><p>Chương trình dùng dữ liệu nhỏ tự đặt. Các quan hệ toán được ghi ngay trong Notes. Mô phỏng hữu hạn không thay chứng minh cho mọi điểm. Code tính toán được chia sẻ giữa component và kiểm tra tại <code>docs/.vitepress/theme/math-ai.mjs</code>.</p><slot /></details>
  </figure>
</template>
<style scoped>
.math-lab { margin: 28px 0; padding: 20px; border: 1px solid var(--vp-c-border); border-radius: 10px; background: var(--vp-c-bg-soft); color: var(--vp-c-text-1); overflow: hidden; }
.math-lab figcaption { font-size: var(--fs-read); font-weight: 600; margin-bottom: 18px; }
.math-lab label { display: grid; gap: 8px; font-size: var(--fs-ui); margin-bottom: 12px; }
.math-lab input[type=range] { width: 100%; min-height: 44px; accent-color: var(--vp-c-brand-1); }
.math-lab select { min-height: 44px; padding: 8px; border: 1px solid var(--vp-c-border); border-radius: var(--radius); background: var(--vp-c-bg); color: var(--vp-c-text-1); max-width: 100%; }
.math-lab svg { display: block; width: 100%; max-height: 360px; overflow: hidden; }
.math-lab svg text { font: 17px var(--font-ui); fill: var(--vp-c-text-1); }
.math-lab svg circle { fill: var(--vp-c-text-1); }
.axis { stroke: var(--vp-c-text-3); stroke-width: 1.2; }
.arrow-head { fill: var(--vp-c-text-3); }
.main-line { fill: none; stroke: var(--vp-c-brand-1); stroke-width: 3; }
.secondary-line { stroke: var(--vp-c-text-1); stroke-width: 2; }
.dashed,.contour { stroke: var(--vp-c-text-3); stroke-dasharray: 4 5; fill: none; }
.math-lab svg .marker { fill: var(--vp-c-brand-1); }
.math-lab svg .hollow { fill: var(--vp-c-bg-soft); stroke: var(--vp-c-text-1); stroke-width: 2; }
.math-lab svg .node { fill: var(--vp-c-bg-soft); stroke: var(--vp-c-text-1); stroke-width: 1.5; }
.region { fill: var(--vp-c-brand-soft); stroke: var(--vp-c-brand-1); stroke-width: 2; }
.lab-inputs { display: grid; grid-template-columns: repeat(auto-fit,minmax(140px,1fr)); gap: 16px; }
.lab-buttons { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; }
.lab-buttons button { min-height: 44px; padding: 8px 16px; border: 1px solid var(--vp-c-border); border-radius: var(--radius); background: var(--vp-c-bg); color: var(--vp-c-text-1); }
.lab-buttons button:disabled { cursor: default; }
.lab-buttons label { flex: 1 1 140px; margin: 0; }
.lab-code { border-top: 1px solid var(--vp-c-divider); padding-top: 12px; }
.math-lab summary { min-height: 44px; cursor: pointer; padding: 8px 0; }
.math-lab p { font-size: var(--fs-ui); overflow-wrap: anywhere; }
.lab-notice { border-left: 3px solid var(--vp-c-brand-1); padding-left: 12px; }
@media(max-width:480px) { .math-lab { padding: 12px; } .lab-inputs { grid-template-columns: 1fr; gap: 4px; } }
</style>
