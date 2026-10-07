<script setup>
import { computed, ref, watch } from 'vue'
import FieldSimulation from './FieldSimulation.vue'
import { searchTrace, gradientTrace, bayesCounts, wordCountTrace } from './illustrations'
const props = defineProps({ type: { type: String, required: true } })
const step = ref(0), mode = ref('bfs'), rate = ref(.2), prior = ref(10), sensitivity = ref(80), falsePositive = ref(10), vectorX = ref(10), vectorY = ref(20), text = ref('uet học uet dữ liệu học')
const adjacency = { A: ['B','C'], B: ['D','E'], C: ['F'], D: [], E: [], F: [] }
const nodes = [{ id:'A', x:370,y:40 },{ id:'B',x:230,y:125 },{ id:'C',x:510,y:125 },{ id:'D',x:135,y:220 },{ id:'E',x:320,y:220 },{ id:'F',x:550,y:220 }]
const trace = computed(() => searchTrace(adjacency,mode.value)), state = computed(() => trace.value[step.value])
watch(mode, () => { step.value=0 })
const gradients = computed(() => gradientTrace(2,Number(rate.value),10))
const plot = x => ({ x: 370+x*125, y: 310-x*x*43 })
const curve = Array.from({length:81}, (_,i) => { const p=plot(-2.4+i*.06); return `${p.x},${p.y}` }).join(' ')
const visibleGradients = computed(() => gradients.value.filter(x => Math.abs(x)<=2.5).map(plot))
const counts = computed(() => bayesCounts(prior.value/100,sensitivity.value/100,falsePositive.value/100))
const matrix = [[1,2],[3,4],[5,6]], broadcast = computed(() => matrix.map(row => [row[0]+Number(vectorX.value),row[1]+Number(vectorY.value)]))
const words = computed(() => wordCountTrace(text.value)); watch(text,()=>{step.value=0})
const codes = {
  search: `const frontier = ['A'];\nwhile (frontier.length) {\n  const node = mode === 'bfs' ? frontier.shift() : frontier.pop();\n  visit(node);\n  // DFS: thêm láng giềng theo thứ tự đảo để thăm nhánh trái trước.\n  frontier.push(...neighbors(node, mode));\n}`,
  gradient: `const points = [2];\nfor (let i = 0; i < 10; i++) {\n  const x = points.at(-1);\n  points.push(x - learningRate * 2 * x); // f(x) = x²\n}`,
  bayes: `const tp = population * prior * sensitivity;\nconst fp = population * (1 - prior) * falsePositive;\nconst posterior = tp / (tp + fp);`,
  broadcast: `const result = matrix.map(row =>\n  row.map((value, column) => value + vector[column])\n); // minh họa broadcasting (3,2) + (2,)`,
  mapreduce: `const pairs = words.map(word => [word, 1]);\nconst grouped = new Map();\nfor (const [key, value] of pairs) {\n  grouped.set(key, [...(grouped.get(key) || []), value]);\n}\nconst counts = [...grouped].map(([key, values]) =>\n  [key, values.reduce((sum, value) => sum + value, 0)]\n);`
}
</script>
<template>
  <figure class="code-illustration">
    <div v-if="type==='search'">
      <div class="illustration-toolbar"><label>Thuật toán<select v-model="mode"><option value="bfs">BFS · hàng đợi FIFO</option><option value="dfs">DFS · ngăn xếp LIFO</option></select></label><div class="button-row"><button class="study-button" @click="step=0">Đặt lại</button><button class="study-button primary" :disabled="step===trace.length-1" @click="step++">Bước tiếp →</button></div></div>
      <svg viewBox="0 0 740 270" role="img" aria-label="Cây minh họa thứ tự duyệt BFS và DFS"><line v-for="node in nodes.filter(n=>n.id!=='A')" :key="`edge-${node.id}`" :x1="nodes.find(n=>adjacency[n.id].includes(node.id)).x" :y1="nodes.find(n=>adjacency[n.id].includes(node.id)).y" :x2="node.x" :y2="node.y" class="illustration-edge"/><g v-for="node in nodes" :key="node.id"><circle :cx="node.x" :cy="node.y" r="23" :class="{ visited: state.visited.includes(node.id), current: state.current===node.id }"/><text :x="node.x" :y="node.y+6" text-anchor="middle">{{ node.id }}</text></g></svg>
      <div class="trace-state" aria-live="polite"><p><strong>Bước {{ step }}:</strong> {{ state.current ? `Vừa thăm ${state.current}.` : 'Bắt đầu tại A.' }}</p><p>Đã thăm: {{ state.visited.join(' → ') || 'Chưa có' }}</p><p>{{ mode==='bfs' ? 'Hàng đợi (lấy bên trái)' : 'Ngăn xếp (lấy bên phải)' }}: {{ state.frontier.join(', ') || 'Rỗng' }}</p></div>
    </div>
    <div v-else-if="type==='gradient'">
      <label class="illustration-range">Tốc độ học η = {{ Number(rate).toFixed(2) }}<input v-model.number="rate" type="range" min=".05" max="1.2" step=".05"></label>
      <svg viewBox="0 0 740 350" role="img" aria-label="Đồ thị f(x)=x bình phương và các bước Gradient Descent"><line x1="45" y1="310" x2="695" y2="310" class="illustration-edge"/><line x1="370" y1="20" x2="370" y2="330" class="illustration-edge"/><polyline :points="curve" class="illustration-curve"/><polyline :points="visibleGradients.map(p=>`${p.x},${p.y}`).join(' ')" class="illustration-trace"/><circle v-for="(p,i) in visibleGradients" :key="i" :cx="p.x" :cy="p.y" r="5" class="current"/><text x="390" y="40">f(x) = x²</text><text x="375" y="335">0</text></svg>
      <div class="trace-state" aria-live="polite"><p>Khởi đầu x₀ = 2. Sau 10 bước: x ≈ {{ gradients.at(-1).toFixed(4) }}, f(x) ≈ {{ (gradients.at(-1)**2).toFixed(4) }}.</p><p>{{ rate<1 ? 'Với 0 < η < 1, |x| giảm trong ví dụ này.' : rate===1 ? 'η = 1 làm x đổi dấu và giữ nguyên độ lớn.' : 'η > 1 làm |x| tăng; các điểm lớn ra khỏi vùng vẽ.' }}</p></div>
    </div>
    <div v-else-if="type==='bayes'">
      <div class="bayes-inputs"><label class="illustration-range">Tỷ lệ A: {{ prior }}%<input v-model.number="prior" type="range" min="1" max="99"></label><label class="illustration-range">P(B|A): {{ sensitivity }}%<input v-model.number="sensitivity" type="range" min="1" max="100"></label><label class="illustration-range">P(B|không A): {{ falsePositive }}%<input v-model.number="falsePositive" type="range" min="0" max="50"></label></div>
      <div class="bayes-result" aria-live="polite"><strong>P(A|B) ≈ {{ (counts.posterior*100).toFixed(1) }}%</strong><div class="bayes-bar"><span :style="{width:`${counts.posterior*100}%`}"></span></div><p>Trong 1000 trường hợp kỳ vọng: {{ counts.truePositive.toFixed(1) }} vừa thuộc A vừa có B; {{ counts.falseAlarm.toFixed(1) }} không thuộc A nhưng vẫn có B.</p></div><p class="small">Thay đổi tỷ lệ ban đầu để thấy cùng một quan sát có thể dẫn tới xác suất sau quan sát rất khác nhau.</p>
    </div>
    <div v-else-if="type==='broadcast'">
      <div class="bayes-inputs"><label class="illustration-range">Vector[0] = {{ vectorX }}<input v-model.number="vectorX" type="range" min="-20" max="20"></label><label class="illustration-range">Vector[1] = {{ vectorY }}<input v-model.number="vectorY" type="range" min="-20" max="20"></label></div>
      <div class="broadcast-display"><div><strong>Ma trận (3,2)</strong><div v-for="(row,i) in matrix" :key="i">{{ row.join(' · ') }}</div></div><span aria-hidden="true">+</span><div><strong>Vector (2,)</strong><div>{{ vectorX }} · {{ vectorY }}</div></div><span aria-hidden="true">=</span><div aria-live="polite"><strong>Kết quả (3,2)</strong><div v-for="(row,i) in broadcast" :key="i">{{ row.join(' · ') }}</div></div></div><p class="small">Cùng một vector được cộng vào từng hàng; chỉ số cột quyết định thành phần cộng vào.</p>
    </div>
    <div v-else-if="type==='mapreduce'">
      <label class="map-input">Văn bản để đếm từ<input v-model="text" maxlength="200" placeholder="Nhập một câu ngắn…"></label><div class="illustration-toolbar"><span>{{ ['Map: phát cặp (từ, 1)','Shuffle: nhóm theo từ','Reduce: cộng các giá trị'][step] }}</span><div class="button-row"><button class="study-button" @click="step=0">Đặt lại</button><button class="study-button primary" :disabled="step===2" @click="step++">Bước tiếp →</button></div></div>
      <div class="map-output" aria-live="polite"><span v-for="(pair,i) in (step===0 ? words.pairs : step===1 ? words.groups : words.counts)" :key="i">{{ pair[0] }}: {{ Array.isArray(pair[1]) ? `[${pair[1].join(', ')}]` : pair[1] }}</span><p v-if="!words.pairs.length">Nhập văn bản để bắt đầu.</p></div><p class="small">Mô hình tính toán trên tối đa 30 từ, minh họa ba pha; không mô phỏng thời gian truyền mạng.</p>
    </div>
    <FieldSimulation v-else-if="type==='field'" />
    <details v-if="codes[type]" class="illustration-code"><summary>Xem code minh họa</summary><pre><code>{{ codes[type] }}</code></pre></details>
    <figcaption>Thay đổi đầu vào hoặc chạy từng bước để kiểm tra điều vừa đọc.</figcaption>
  </figure>
</template>
