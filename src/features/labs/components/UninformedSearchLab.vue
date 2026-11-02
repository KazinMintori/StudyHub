<script setup>
import { computed, ref, useId, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'
import { searchExamples, traceUninformed, searchCode, idsCode, activeSearchLine } from '../services/uninformed-search.mjs'
import { codeTokens } from '../services/agent-decision.mjs'
const props=defineProps({mode:{type:String,default:'bfs'}})
const mode=ref(props.mode), exampleId=ref('weighted'), step=ref(0), goalAtStart=ref(false), copied=ref(false)
const graphText=ref(''), error=ref(''), custom=ref(null)
const marker='search-'+useId().replace(/[^a-zA-Z0-9_-]/g,'')
const example=computed(()=>custom.value||searchExamples.find(e=>e.id===exampleId.value))
const frames=computed(()=>traceUninformed(example.value.graph,example.value.start,goalAtStart.value?example.value.start:example.value.goal,mode.value))
const state=computed(()=>frames.value[Math.min(step.value,frames.value.length-1)])
const current=computed(()=>state.value.nodes.find(n=>n.id===state.value.current))
const resetKey=computed(()=>JSON.stringify([mode.value,example.value,goalAtStart.value]))
watch(resetKey,()=>{step.value=0;copied.value=false})
watch(exampleId,()=>{custom.value=null;error.value='';graphText.value=JSON.stringify(searchExamples.find(e=>e.id===exampleId.value).graph,null,2)},{immediate:true})
const vertices=computed(()=>Object.keys(example.value.graph).map((id,i,all)=>({id,x:40+(i%3)*120,y:70+Math.floor(i/3)*115})))
const edges=computed(()=>Object.entries(example.value.graph).flatMap(([a,list])=>list.map(([b,w])=>({a,b,w,from:vertices.value.find(v=>v.id===a),to:vertices.value.find(v=>v.id===b)}))))
const height=computed(()=>120+Math.floor((vertices.value.length-1)/3)*115)
const code=computed(()=>mode.value==='ids'?idsCode:searchCode)
const line=computed(()=>activeSearchLine(state.value.phase,mode.value))
const weightedMode=computed(()=>['ucs','dijkstra'].includes(mode.value))
const comparison=computed(()=>{
  if(!weightedMode.value)return null
  return ['ucs','dijkstra'].map(strategy=>{
    const trace=traceUninformed(example.value.graph,example.value.start,goalAtStart.value?example.value.start:example.value.goal,strategy)
    const end=trace.at(-1)
    return {strategy,phase:end.phase,cost:end.result?.cost,taken:trace.filter(f=>f.phase==='take').length,expanded:end.settled.length}
  })
})
const descriptions={budget:'Tạm dừng ở giới hạn 1.000 thao tác của bộ xem để bảo vệ bộ nhớ trình duyệt. Chưa kết luận bài toán vô nghiệm. Hãy thử đồ thị nhỏ hơn.',start:'Đưa nút đầu vào biên tìm kiếm.',iteration:'Bắt đầu lượt DFS mới. Xóa biên và thông tin của lượt trước, giữ giới hạn độ sâu hiện tại.',take:'Lấy một nút khỏi biên theo chiến lược đã chọn. Chưa mở rộng nút này.',stale:'Bỏ bản ghi cũ: Đã có đường tốt hơn hoặc trạng thái này đã được chốt.',success:'Kiểm tra đích thành công khi lấy nút khỏi biên. Lần theo cha để khôi phục đường đi.',expand:'Mở rộng nút hiện tại: Xét các hành động đi ra từ trạng thái này.',consider:'Xét cạnh đang được đánh dấu và chi phí của đường đi mới.',skip:'Không thêm bản ghi này vì trạng thái đã phát hiện hoặc chi phí không cải thiện.',insert:'Thêm một nút tìm kiếm mới vào biên. Nút lưu đường đi riêng dù trạng thái có thể trùng.',cutoff:'Chạm giới hạn độ sâu và còn nhánh chưa xét. Đây là tạm ngừng do giới hạn, chưa phải không có lời giải.',failure:'Biên đã hết và không còn nhánh bị cắt cần xét sâu hơn. Không tìm thấy đường tới đích.'}
const frontier=computed(()=>mode.value==='dfs'||mode.value==='ids'?[...state.value.frontier].reverse():weightedMode.value?[...state.value.frontier].sort((a,b)=>a.g-b.g||a.id-b.id):state.value.frontier)
function edgePath(e){const dx=e.to.x-e.from.x,dy=e.to.y-e.from.y,len=Math.hypot(dx,dy),ux=dx/len,uy=dy/len,bend=dy===0&&Math.abs(dx)>150?-80:18;return `M${e.from.x+ux*19} ${e.from.y+uy*19} Q${(e.from.x+e.to.x)/2-uy*bend} ${(e.from.y+e.to.y)/2+ux*bend} ${e.to.x-ux*23} ${e.to.y-uy*23}`}
function applyGraph(){try{const g=JSON.parse(graphText.value);if(Object.keys(g).length>8)throw Error('Chỉ nhập tối đa 8 trạng thái để hình dễ đọc.');if(Object.keys(g).some(v=>v.length>5))throw Error('Tên trạng thái dài tối đa 5 ký tự.');for(const [u,edges] of Object.entries(g))for(const [v]of edges)if(u===v)throw Error('Hình không hỗ trợ cạnh tự nối.');traceUninformed(g,example.value.start,example.value.goal,mode.value);custom.value={...example.value,graph:g,title:'Đồ thị tự nhập'};step.value=0;error.value=''}catch(e){error.value=e.message}}
async function copy(){try{await navigator.clipboard.writeText(code.value.join('\n'));copied.value=true}catch{copied.value=false}}
</script>

<template>
  <figure class="study-lab search-lab" aria-label="Mô phỏng truy vết tìm kiếm không có thông tin">
    <figcaption class="lab-title">Cùng một bài toán, khác cách chọn biên</figcaption>
    <p class="lab-lead">Mỗi nút trong biên lưu trạng thái, cha, độ sâu và chi phí đường đi. Xem từng thao tác trước khi chạy tự động.</p>
    <div class="search-settings">
      <label>Chiến lược<select v-model="mode"><option value="bfs">BFS · Hàng đợi</option><option value="dfs">DFS · Ngăn xếp</option><option value="ucs">UCS · Dừng ở đích</option><option value="dijkstra">Dijkstra · Tính mọi khoảng cách</option><option value="ids">IDS · Tăng giới hạn độ sâu</option></select></label>
      <label>Trường hợp<select v-model="exampleId"><option v-for="e in searchExamples" :key="e.id" :value="e.id">{{ e.title }}</option></select></label>
      <label class="goal-toggle"><input v-model="goalAtStart" type="checkbox">Bắt đầu đã là đích</label>
    </div>
    <p class="search-convention">Cạnh có hướng, chi phí không âm. Thứ tự láng giềng theo dữ liệu nhập. BFS/DFS đánh dấu ngay khi thêm vào biên. DFS thêm láng giềng theo thứ tự ngược để ưu tiên nhánh đầu. UCS phá hòa theo thứ tự thêm, cho cập nhật đường tốt hơn. IDS chỉ loại chu trình trên đường hiện tại. Tất cả kiểm tra đích khi lấy nút ra. Bộ xem lưu lịch sử để quay lại, nên bộ nhớ giao diện không đại diện cho độ phức tạp bộ nhớ của thuật toán.</p>
    <SimulationControls v-model="step" :max="frames.length-1" :reset-key="resetKey" />
    <p role="status" aria-live="polite" class="search-status">{{ state.phase==='complete'?'Đã tính xong khoảng cách từ nguồn tới mọi đỉnh có thể đến được. Đỉnh không thể tới có khoảng cách vô hạn.':descriptions[state.phase] }} <span v-if="current">Nút #{{ current.id }}: {{ current.state }}, độ sâu {{ current.depth }}, chi phí {{ current.g }}.</span><span v-if="state.limit!==null"> Giới hạn hiện tại: {{ state.limit }}.</span></p>
    <div class="search-panels">
      <section class="search-graph" aria-label="Đồ thị trạng thái">
        <h4>Đồ thị trạng thái</h4>
        <svg :viewBox="`0 0 330 ${height}`" role="img" aria-label="Đồ thị có hướng với nhãn chi phí trên cạnh">
          <defs><marker :id="marker" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M1 1 9 5 1 9" /></marker></defs>
          <g v-for="e in edges" :key="e.a+'-'+e.b" :class="{highlight:state.edge?.[0]===e.a&&state.edge?.[1]===e.b}">
            <path :d="edgePath(e)" :marker-end="`url(#${marker})`" />
            <text :x="(e.from.x+e.to.x)/2+7" :y="e.from.y===e.to.y&&Math.abs(e.from.x-e.to.x)>150?20:(e.from.y+e.to.y)/2-8" class="edge-label">{{ e.w }}</text>
          </g>
          <g v-for="v in vertices" :key="v.id" :class="{current:current?.state===v.id,queued:state.frontier.some(n=>n.state===v.id),expanded:state.settled.includes(v.id)}">
            <circle :cx="v.x" :cy="v.y" r="19" /><circle v-if="v.id===(goalAtStart?example.start:example.goal)" :cx="v.x" :cy="v.y" r="24" class="goal-ring" />
            <text :x="v.x" :y="v.y+5" text-anchor="middle">{{ v.id }}</text>
          </g>
        </svg>
        <p class="search-legend">Viền đôi: Đích. Viền tím đậm: Nút đang xét. Nền nhạt: Đang ở biên. Danh sách dưới đây phân biệt rõ các trạng thái ngoài màu sắc.</p>
        <p><strong>Đường tới nút đang xét:</strong> {{ state.path.join(' → ')||'Chưa lấy nút' }}</p>
        <p><strong>Đã mở rộng:</strong> {{ state.settled.join(', ')||'Chưa có' }}</p>
      </section>
      <section class="search-frontier" aria-label="Nội dung biên tìm kiếm">
        <h4>Biên · Nút sắp lấy đứng đầu</h4>
        <ol v-if="frontier.length"><li v-for="n in frontier" :key="n.id"><span>#{{ n.id }} · {{ n.state }}</span><span>Chi phí {{ n.g }} · Sâu {{ n.depth }} · Cha {{ n.parent===null?'∅':'#'+n.parent }}</span></li></ol>
        <p v-else>Biên rỗng.</p>
        <div v-if="state.result" class="search-result"><h4>{{ state.phase==='complete'?'Đường tới đích đã chọn':'Lời giải' }}</h4><template v-if="Number.isFinite(state.result.cost)"><p>{{ state.result.path.join(' → ') }}</p><p>{{ state.result.depth }} hành động · Tổng chi phí {{ state.result.cost }}</p></template><p v-else>Không có đường tới đích đã chọn.</p></div>
        <p v-if="state.phase==='failure'" class="search-result">Không có đường tới đích trong đồ thị đã nhập.</p>
      </section>
    </div>
    <section v-if="weightedMode" class="search-distances" aria-label="Khoảng cách tạm thời và đã chốt">
      <h4>Khoảng cách tốt nhất đã biết ở bước hiện tại</h4>
      <ul><li v-for="v in vertices" :key="v.id"><strong>{{ v.id }}: {{ state.best[v.id]??'∞' }}</strong> · {{ state.settled.includes(v.id)||(state.phase==='success'&& current?.state===v.id)?'Đã chốt':state.best[v.id]===undefined?'Chưa tìm thấy đường':'Tạm thời' }}</li></ul>
      <details><summary>So sánh kết quả cuối của UCS và Dijkstra</summary><p>Hai chế độ dùng chung phép chọn chi phí nhỏ nhất và nới lỏng cạnh. Khác biệt trong bộ xem là điều kiện dừng. Dijkstra cũng có thể được cài để dừng tại đích như UCS.</p><ul><li v-for="r in comparison" :key="r.strategy"><strong>{{ r.strategy==='ucs'?'UCS dừng tại đích':'Dijkstra tính mọi khoảng cách' }}</strong>: {{ r.taken }} lần lấy nút, {{ r.expanded }} lần mở rộng. {{ r.phase==='budget'?'Đã chạm giới hạn của bộ xem.':Number.isFinite(r.cost)?'Chi phí tới đích: '+r.cost:'Không có đường tới đích.' }}</li></ul><p>Hãy chọn “Còn nhánh sau khi tới đích” để thấy Dijkstra tiếp tục xét các nhánh mà UCS có thể bỏ lại.</p></details>
    </section>
    <details class="search-tree"><summary>Các nút tìm kiếm đã sinh: Phân biệt nút với trạng thái</summary><p>Cùng một nhãn trạng thái có thể xuất hiện ở nhiều nút. Mỗi ID có một cha riêng nên đại diện cho một đường đi riêng. Với IDS, danh sách lưu cả các lượt trước để xem lại.</p><ol><li v-for="n in state.nodes" :key="n.id"><strong>#{{ n.id }} · {{ n.state }}</strong> ← {{ n.parent===null?'Gốc':'Cha #'+n.parent }} · Sâu {{ n.depth }} · Chi phí {{ n.g }}</li></ol></details>
    <section class="search-running" aria-label="Dòng mã đang chạy">
      <div class="search-code-bar"><h4>Dòng mã tương ứng · {{ line+1 }}</h4><button type="button" @click="copy">{{ copied?'Đã chép':'Chép toàn bộ mã' }}</button></div>
      <pre><code><span v-for="(t,i) in codeTokens(code[line])" :key="i" :class="t.kind">{{ t.text }}</span></code></pre>
      <details><summary>Xem chương trình JavaScript đang thực thi</summary><p>Hàm sinh trả từng trạng thái bằng yield. Hàm snap chỉ sao chép dữ liệu để quan sát, không lựa chọn bước thay cho thuật toán.</p><pre><code><span v-for="(row,i) in code" :key="i" class="search-code-row" :class="{active:i===line}"><span aria-hidden="true" class="line-number">{{ i+1 }}</span><span><span v-for="(t,j) in codeTokens(row)" :key="j" :class="t.kind">{{ t.text }}</span></span></span></code></pre></details>
    </section>
    <details class="search-edit"><summary>Thay cạnh và chi phí</summary><p>Dữ liệu là danh sách kề JSON. Mỗi cạnh có dạng ["đỉnh tới", chi phí]. Giữ trạng thái đầu {{ example.start }} và đích {{ example.goal }} trong danh sách. Tối đa 8 trạng thái, không hỗ trợ cạnh tự nối trong hình.</p><label>Dữ liệu đồ thị<textarea v-model="graphText" rows="8" spellcheck="false" /></label><button type="button" @click="applyGraph">Áp dụng và đặt lại</button><p v-if="error" role="alert">{{ error }}</p></details>
    <details class="lab-tasks"><summary>Thử dự đoán trước khi chạy</summary><ol><li>Ở đồ thị có trọng số, vì sao BFS trả ít hành động hơn UCS nhưng chi phí lớn hơn?</li><li>Chọn trường hợp đích xuất hiện sớm. Dừng lúc đích vừa được thêm vào biên và dự đoán lựa chọn UCS.</li><li>Chọn đồ thị không có đường tới đích. Với IDS, phân biệt bước bị cắt do giới hạn với kết luận thất bại.</li></ol></details>
  </figure>
</template>

<style scoped>
.search-lab{min-width:0}.search-settings{display:grid;grid-template-columns:1fr 1fr;gap:12px}.search-settings label,.search-edit label{display:grid;gap:6px;font:var(--fs-small)/1.6 var(--font-ui)}.search-lab select,.search-lab button,.search-lab textarea{min-height:44px;border:1px solid var(--control);border-radius:var(--radius);padding:8px;background:var(--paper);color:var(--ink);font:inherit;max-width:100%}.search-lab select{width:100%}.search-lab :is(button,select,input,textarea):focus-visible{outline:3px solid var(--tim);outline-offset:3px}.search-settings .goal-toggle{display:flex;align-items:center;gap:8px;grid-column:1/-1}.goal-toggle input{width:22px;height:22px}.search-convention,.search-legend{font-size:var(--fs-small);line-height:1.7;color:var(--ink-2)}.search-status{padding:12px;border-left:3px solid var(--tim);background:var(--tim-soft);line-height:1.7}.search-panels{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}.search-panels section{min-width:0;padding:12px;border:1px solid var(--rule);border-radius:var(--radius);background:var(--paper)}.search-lab h4{font:600 var(--fs-ui)/1.5 var(--font-ui);margin:0 0 10px}.search-graph svg{max-height:none;margin:0;border:0}.search-graph svg path{stroke:var(--ink-2);stroke-width:1.4;fill:none}.search-graph circle{stroke:var(--ink-2);stroke-width:1.5;fill:var(--paper)}.search-graph text{font:15px var(--font-ui);fill:var(--ink)}.search-graph .edge-label{paint-order:stroke;stroke:var(--paper);stroke-width:6px;stroke-linejoin:round}.search-graph .highlight path{stroke:var(--tim);stroke-width:2.5}.search-graph .queued circle{fill:var(--tim-soft)}.search-graph .current circle{stroke:var(--tim);stroke-width:3}.search-graph .goal-ring{fill:none!important;stroke-dasharray:3 3}.search-graph p{font-size:var(--fs-small);line-height:1.7;overflow-wrap:anywhere}.search-frontier ol{margin:0;padding:0;list-style:none;display:grid;gap:8px;max-height:400px;overflow:auto}.search-frontier li{display:grid;gap:3px;padding:8px;border:1px solid var(--rule);border-radius:var(--radius);font-size:var(--fs-small)}.search-frontier li span:first-child{font-weight:600}.search-result{margin-top:16px;padding:12px;background:var(--tim-soft);border-radius:var(--radius);overflow-wrap:anywhere}.search-code-bar{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-top:20px}.search-running{min-width:0}.search-running pre{white-space:pre-wrap;overflow-wrap:anywhere;overflow:visible;background:var(--paper);padding:12px;color:var(--ink);font:13px/1.8 var(--font-code);border:1px solid var(--rule);border-radius:var(--radius)}.search-running code{font:inherit}.search-code-row{display:grid;grid-template-columns:3ch minmax(0,1fr);gap:8px}.search-code-row.active{background:var(--tim-soft);border-left:3px solid var(--tim)}.line-number{user-select:none;color:var(--ink-2)}.keyword{color:var(--tim);font-weight:600}.string{color:var(--xanh)}.number{color:var(--do)}.search-edit textarea{display:block;width:100%;box-sizing:border-box;font:12px/1.6 var(--font-code);margin:8px 0}.search-lab details{margin-top:16px;font-size:var(--fs-small);line-height:1.7}.search-lab summary{cursor:pointer;min-height:44px}.search-lab button{cursor:pointer;font-size:var(--fs-small)}@media(max-width:700px){.search-panels,.search-settings{grid-template-columns:minmax(0,1fr)}.search-lab{padding:12px}.search-panels section{padding:8px}}
</style>
