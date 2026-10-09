<script setup>
import { computed, ref, watch } from 'vue'
import FieldSimulation from './FieldSimulation.vue'
import MathMatrix from './MathMatrix.vue'
import SimulationControls from './SimulationControls.vue'
import { searchTrace, gradientTrace, bayesCounts, wordCountTrace } from './illustrations'
const props = defineProps({ type: { type: String, required: true } })
const step = ref(0), mode = ref('bfs'), rate = ref(.2), prior = ref(10), sensitivity = ref(80), falsePositive = ref(10), vectorX = ref(10), vectorY = ref(20), text = ref('uet học uet dữ liệu học')
const adjacency = { A: ['B','C'], B: ['D','E'], C: ['F'], D: [], E: [], F: [] }
const nodes = [{ id:'A', x:190,y:35 },{ id:'B',x:105,y:120 },{ id:'C',x:285,y:120 },{ id:'D',x:45,y:215 },{ id:'E',x:160,y:215 },{ id:'F',x:320,y:215 }]
const trace = computed(() => searchTrace(adjacency,mode.value)), state = computed(() => trace.value[step.value])
watch(mode, () => { step.value=0 })
const gradients = computed(() => gradientTrace(2,Number(rate.value),10))
const plot = x => ({ x: 190+x*65, y: 250-x*x*35 })
const curve = Array.from({length:81}, (_,i) => { const p=plot(-2.4+i*.06); return `${p.x},${p.y}` }).join(' ')
watch(rate, () => { step.value = 0 })
const visibleGradients = computed(() => gradients.value.slice(0,step.value+1).flatMap((x,i) => Math.abs(x)<=2.5 ? [{...plot(x),iteration:i}] : []))
// Keep gaps whenever an iterate leaves the viewport instead of joining unrelated points.
const gradientSegments = computed(() => gradients.value.slice(1,step.value+1).flatMap((x,i) => Math.abs(x)<=2.5 && Math.abs(gradients.value[i])<=2.5 ? [{from:plot(gradients.value[i]),to:plot(x),iteration:i+1}] : []))
const currentGradient = computed(() => plot(gradients.value[step.value]))
const counts = computed(() => bayesCounts(prior.value/100,sensitivity.value/100,falsePositive.value/100))
const matrix = [[1,2],[3,4],[5,6]], broadcast = computed(() => matrix.map(row => [row[0]+Number(vectorX.value),row[1]+Number(vectorY.value)]))
const repeatedRow = computed(() => matrix.map(() => [Number(vectorX.value), Number(vectorY.value)]))
const arrayLiteral = rows => `[${rows.map(row => `[${row.join(', ')}]`).join(',\n ')}]`
const broadcastCode = computed(() => `import numpy as np\n\nA = np.array([[1, 2], [3, 4], [5, 6]])\nb = np.array([${Number(vectorX.value)}, ${Number(vectorY.value)}])\nC = A + b\n\nprint(C)\nprint(A.shape, A.ndim)  # (3, 2), 2\nprint(b.shape, b.ndim)  # (2,), 1`)
const words = computed(() => wordCountTrace(text.value)); watch(text,()=>{step.value=0})
const codes = {
  search: `const frontier = ['A'];\nwhile (frontier.length) {\n  const node = mode === 'bfs' ? frontier.shift() : frontier.pop();\n  visit(node);\n  // DFS: thêm láng giềng theo thứ tự đảo để thăm nhánh trái trước.\n  frontier.push(...neighbors(node, mode));\n}`,
  gradient: `const points = [2];\nfor (let i = 0; i < 10; i++) {\n  const x = points.at(-1);\n  points.push(x - learningRate * 2 * x); // f(x) = x²\n}`,
  bayes: `const tp = population * prior * sensitivity;\nconst fp = population * (1 - prior) * falsePositive;\nconst posterior = tp / (tp + fp);`,
  mapreduce: `const pairs = words.map(word => [word, 1]);\nconst grouped = new Map();\nfor (const [key, value] of pairs) {\n  grouped.set(key, [...(grouped.get(key) || []), value]);\n}\nconst counts = [...grouped].map(([key, values]) =>\n  [key, values.reduce((sum, value) => sum + value, 0)]\n);`
}
</script>
<template>
  <figure class="code-illustration">
    <div v-if="type==='search'">
      <div class="illustration-toolbar"><label>Thuật toán<select v-model="mode"><option value="bfs">BFS · hàng đợi FIFO</option><option value="dfs">DFS · ngăn xếp LIFO</option></select></label></div>
      <svg viewBox="0 0 380 255" role="img" aria-label="Cây minh họa thứ tự duyệt BFS và DFS"><line v-for="node in nodes.filter(n=>n.id!=='A')" :key="`edge-${node.id}`" :x1="nodes.find(n=>adjacency[n.id].includes(node.id)).x" :y1="nodes.find(n=>adjacency[n.id].includes(node.id)).y" :x2="node.x" :y2="node.y" class="illustration-edge"/><g v-for="node in nodes" :key="node.id"><circle :cx="node.x" :cy="node.y" r="23" :class="{ visited: state.visited.includes(node.id), frontier: state.frontier.includes(node.id), current: state.current===node.id }"/><text :x="node.x" :y="node.y+6" text-anchor="middle">{{ node.id }}</text></g></svg>
      <p class="simulation-legend"><span>Viền nét đứt: đang chờ</span><span>Viền liền: đã thăm</span><span>Tô đậm: nút hiện tại</span></p>
      <SimulationControls v-model="step" :max="trace.length-1" :reset-key="trace" />
      <div class="trace-state" aria-live="polite"><p><strong>Bước {{ step }}:</strong> {{ state.current ? `Vừa thăm ${state.current}.` : 'Bắt đầu tại A.' }}</p><p>Đã thăm: {{ state.visited.join(' → ') || 'Chưa có' }}</p><p>{{ mode==='bfs' ? 'Hàng đợi (lấy bên trái)' : 'Ngăn xếp (lấy bên phải)' }}: {{ state.frontier.join(', ') || 'Rỗng' }}</p></div>
    </div>
    <div v-else-if="type==='gradient'">
      <label class="illustration-range">Tốc độ học η = {{ Number(rate).toFixed(2) }}<input v-model.number="rate" type="range" min=".05" max="1.2" step=".05"></label>
      <svg viewBox="0 0 380 290" role="img" aria-label="Đồ thị f(x)=x bình phương và các bước Gradient Descent"><line x1="20" y1="250" x2="360" y2="250" class="illustration-edge"/><line x1="190" y1="15" x2="190" y2="270" class="illustration-edge"/><polyline :points="curve" class="illustration-curve"/><line v-for="segment in gradientSegments" :key="segment.iteration" :x1="segment.from.x" :y1="segment.from.y" :x2="segment.to.x" :y2="segment.to.y" class="illustration-trace"/><circle v-for="p in visibleGradients" :key="p.iteration" :cx="p.x" :cy="p.y" r="4" class="visited"/><circle v-if="Math.abs(gradients[step])<=2.5" :cx="currentGradient.x" :cy="currentGradient.y" r="8" class="current gradient-marker"/><text x="210" y="35">f(x) = x²</text><text x="196" y="275">0</text></svg>
      <SimulationControls v-model="step" :max="gradients.length-1" :reset-key="gradients" />
      <div class="trace-state" aria-live="polite"><p>Khởi đầu x₀ = 2. Bước {{ step }}: x ≈ {{ gradients[step].toFixed(4) }}, f(x) ≈ {{ (gradients[step]**2).toFixed(4) }}.</p><p v-if="Math.abs(gradients[step])>2.5" class="gradient-notice">Điểm hiện tại đã ra khỏi vùng vẽ. Các giá trị ở trên vẫn được tính.</p><p>{{ rate<1 ? 'Với 0 < η < 1, |x| giảm trong ví dụ này.' : rate===1 ? 'η = 1 làm x đổi dấu và giữ nguyên độ lớn.' : 'η > 1 làm |x| tăng, vì vậy các điểm lớn ra khỏi vùng vẽ.' }}</p></div>
    </div>
    <div v-else-if="type==='bayes'">
      <div class="bayes-inputs"><label class="illustration-range">Tỷ lệ A: {{ prior }}%<input v-model.number="prior" type="range" min="1" max="99"></label><label class="illustration-range">P(B|A): {{ sensitivity }}%<input v-model.number="sensitivity" type="range" min="1" max="100"></label><label class="illustration-range">P(B|không A): {{ falsePositive }}%<input v-model.number="falsePositive" type="range" min="0" max="50"></label></div>
      <div class="bayes-result" aria-live="polite"><strong>P(A|B) ≈ {{ (counts.posterior*100).toFixed(1) }}%</strong><div class="bayes-bar"><span :style="{width:`${counts.posterior*100}%`}"></span></div><p>Trong 1000 trường hợp kỳ vọng: {{ counts.truePositive.toFixed(1) }} vừa thuộc A vừa có B; {{ counts.falseAlarm.toFixed(1) }} không thuộc A nhưng vẫn có B.</p></div><p class="small">Thay đổi tỷ lệ ban đầu để thấy cùng một quan sát có thể dẫn tới xác suất sau quan sát rất khác nhau.</p>
    </div>
    <div v-else-if="type==='broadcast'">
      <div class="bayes-inputs"><label class="illustration-range"><span><code>b[0]</code> = {{ vectorX }}</span><input v-model.number="vectorX" type="range" min="-20" max="20"></label><label class="illustration-range"><span><code>b[1]</code> = {{ vectorY }}</span><input v-model.number="vectorY" type="range" min="-20" max="20"></label></div>
      <section class="numpy-broadcast" aria-label="Broadcasting trong NumPy">
        <h3>Trong NumPy</h3>
        <p><code>C = A + b</code> cộng mảng một chiều <code>b</code> vào từng hàng của mảng hai chiều <code>A</code>.</p>
        <div class="numpy-array-cards">
          <div><strong>Mảng <code>A</code></strong><p><code>shape = (3, 2)</code><br><code>ndim = 2</code> · hai trục</p><pre><code>{{ arrayLiteral(matrix) }}</code></pre></div>
          <div><strong>Mảng <code>b</code></strong><p><code>shape = (2,)</code><br><code>ndim = 1</code> · một trục, hai phần tử</p><pre><code>[{{ vectorX }}, {{ vectorY }}]</code></pre></div>
          <div aria-live="polite"><strong>Kết quả <code>C</code></strong><p><code>shape = (3, 2)</code><br><code>ndim = 2</code> · hai trục</p><pre><code>{{ arrayLiteral(broadcast) }}</code></pre></div>
        </div>
        <p class="small"><code>ndim</code> đếm số trục của mảng, còn <code>shape</code> ghi số phần tử trên từng trục. Mảng <code>b</code> có hai phần tử nhưng chỉ có một trục.</p>
      </section>
      <details class="broadcast-math">
        <summary>Diễn giải bằng ma trận trong toán học</summary>
        <p>Phép cộng ma trận thông thường cần hai ma trận cùng kích thước. Quy tắc broadcasting ở trên tương ứng với việc lặp hai phần tử của <code>b</code> trên ba hàng để tạo ma trận B, rồi cộng A với B. Cả A, B và C đều là ma trận 3 × 2.</p>
        <div class="broadcast-display" aria-live="polite"><MathMatrix :matrices="[matrix, repeatedRow, broadcast]" :operators="['+', '=']" label="Ma trận A cộng ma trận B bằng ma trận C, và cả ba đều có ba hàng, hai cột" /></div>
      </details>
    </div>
    <div v-else-if="type==='mapreduce'">
      <label class="map-input">Văn bản để đếm từ<input v-model="text" maxlength="200" placeholder="Nhập một câu ngắn…"></label><div class="illustration-toolbar"><span>{{ ['Map: phát cặp (từ, 1)','Shuffle: nhóm theo từ','Reduce: cộng các giá trị'][step] }}</span></div>
      <SimulationControls v-model="step" :max="words.pairs.length ? 2 : 0" :reset-key="words" label="Pha" />
      <TransitionGroup name="map-phase" tag="div" class="map-output" aria-live="polite"><span v-for="(pair,i) in (step===0 ? words.pairs : step===1 ? words.groups : words.counts)" :key="`${step}-${i}-${pair[0]}`">{{ pair[0] }}: {{ Array.isArray(pair[1]) ? `[${pair[1].join(', ')}]` : pair[1] }}</span><p v-if="!words.pairs.length" key="empty">Nhập văn bản để bắt đầu.</p></TransitionGroup><p class="small">Mô hình tính toán trên tối đa 30 từ, minh họa ba pha và không mô phỏng thời gian truyền mạng.</p>
    </div>
    <FieldSimulation v-else-if="type==='field'" />
    <details v-if="type==='broadcast' || codes[type]" class="illustration-code"><summary>Xem code minh họa</summary><pre><code>{{ type==='broadcast' ? broadcastCode : codes[type] }}</code></pre></details>
    <figcaption>Thay đổi đầu vào hoặc chạy từng bước để kiểm tra điều vừa đọc.</figcaption>
  </figure>
</template>
