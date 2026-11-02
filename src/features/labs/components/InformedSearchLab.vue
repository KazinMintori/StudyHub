<script setup>
import {computed,ref,useId,watch} from 'vue'
import SimulationControls from './SimulationControls.vue'
import {informedExamples,traceInformed,inspectHeuristic,validateInformed,informedCode,informedLine} from '../services/informed-search.mjs'
const props=defineProps({initialMode:{type:String,default:'astar'},initialExample:{type:String,default:'weighted'}})
const mode=ref(props.initialMode),exampleId=ref(props.initialExample),reopen=ref(true),zero=ref(false),step=ref(0),custom=ref(null),input=ref(''),error=ref(''),copied=ref(false)
const marker='informed-'+useId().replace(/[^a-zA-Z0-9_-]/g,'')
const base=computed(()=>custom.value||informedExamples.find(e=>e.id===exampleId.value)||informedExamples[0])
const example=computed(()=>({...base.value,h:zero.value?Object.fromEntries(Object.keys(base.value.graph).map(v=>[v,0])):base.value.h}))
const frames=computed(()=>traceInformed(example.value,mode.value,reopen.value))
const state=computed(()=>frames.value[Math.min(step.value,frames.value.length-1)])
const current=computed(()=>state.value.nodes.find(n=>n.id===state.value.current))
const resetKey=computed(()=>JSON.stringify([example.value,mode.value,reopen.value]))
watch(resetKey,()=>{step.value=0;copied.value=false})
watch(exampleId,()=>{custom.value=null;error.value='';input.value=JSON.stringify(informedExamples.find(e=>e.id===exampleId.value),null,2)},{immediate:true})
const diagnostic=computed(()=>inspectHeuristic(example.value))
const frontier=computed(()=>[...state.value.frontier].sort((a,b)=>a.f-b.f||a.id-b.id))
const vertices=computed(()=>{
 const ids=Object.keys(example.value.graph)
 const layout=ids.length===5?{S:[185,40],A:[60,150],B:[310,150],C:[185,270],G:[185,390]}
   :ids.length===4?{S:[185,40],A:[60,170],B:[310,170],G:[185,310]}
   :ids.length===3?{S:[55,190],A:[185,40],G:[315,190]}
   :ids.length===2?{S:[90,60],A:[280,60]}
   :ids.includes('a')?{S:[55,40],a:[185,40],b:[55,180],c:[55,320],d:[185,225],e:[315,125],G:[315,350]}:null
 return ids.map((id,i)=>{const a=-Math.PI/2+2*Math.PI*i/ids.length;const [x,y]=layout?.[id]||[185+132*Math.cos(a),190+140*Math.sin(a)];return {id,x,y}})
})
const height=computed(()=>Math.max(...vertices.value.map(v=>v.y))+80)
const edges=computed(()=>Object.entries(example.value.graph).flatMap(([a,list])=>list.map(([b,w])=>({a,b,w,from:vertices.value.find(v=>v.id===a),to:vertices.value.find(v=>v.id===b)}))))
function curve(e){const a=e.from,b=e.to,dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy),bend=30;return `M${a.x+dx*23/d} ${a.y+dy*23/d} Q${(a.x+b.x)/2-dy*bend/d} ${(a.y+b.y)/2+dx*bend/d} ${b.x-dx*26/d} ${b.y-dy*26/d}`}
function edgeLabel(e){const dx=e.to.x-e.from.x,dy=e.to.y-e.from.y,d=Math.hypot(dx,dy);return {x:(e.from.x+e.to.x)/2-dy*27/d,y:(e.from.y+e.to.y)/2+dx*27/d+5}}
function heuristicLabel(v){const vertical=edges.value.some(e=>e.a===v.id&&Math.abs(e.to.x-v.x)<1&&e.to.y>v.y);return vertical?{x:v.x+38,y:v.y+5,anchor:'start'}:{x:v.x,y:v.y+48,anchor:'middle'}}
const line=computed(()=>informedLine(state.value.phase))
const description={start:'Đưa nút đầu vào biên.',take:'Lấy nút có độ ưu tiên nhỏ nhất. Chưa mở rộng nút này.',stale:'Bỏ bản ghi cũ vì đã có chi phí tốt hơn hoặc trạng thái đang đóng.',expand:'Đóng trạng thái và xét các cạnh đi ra.',consider:'Xét cạnh đang tô đậm và tính chi phí của đường đi mới.',skip:'Đường đi mới không cải thiện chi phí tốt nhất đã biết.',blocked:'Đã tìm được đường tốt hơn tới trạng thái đóng nhưng chế độ này bỏ qua việc mở lại.',insert:'Thêm bản ghi đường đi tốt hơn vào biên.',reopen:'Mở lại trạng thái đã đóng vì tìm được đường có chi phí nhỏ hơn.',success:'Lấy một bản ghi đích hợp lệ ra khỏi biên. Khôi phục đường đi qua các nút cha.',failure:'Biên rỗng. Không có đường tới đích trong đồ thị đã nhập.',budget:'Chạm giới hạn 1.200 thao tác của bộ xem. Chưa kết luận có hay không có lời giải.'}
const summary=computed(()=>['ucs','greedy','astar'].map(m=>{const f=traceInformed(example.value,m,true);return {mode:m,end:f.at(-1),expanded:f.filter(x=>x.phase==='expand').length}}))
const names={ucs:'UCS',greedy:'Greedy',astar:'A*'}
function apply(){try{const e=JSON.parse(input.value);validateInformed(e);custom.value=e;error.value='';zero.value=false;step.value=0}catch(e){error.value=e.message}}
async function copy(){try{await navigator.clipboard.writeText(informedCode.join('\n'));copied.value=true}catch{copied.value=false;error.value='Chưa chép được. Bạn có thể chọn mã trong khung bên dưới.'}}
function tokens(row){return row.split(/('(?:[^'\\]|\\.)*'|\b(?:export|function|const|let|for|of|if|return|while|yield|continue|new|true|false|null)\b|\b\d+\b)/g).filter(Boolean).map(text=>({text,kind:text.startsWith("'")?'string':/^(export|function|const|let|for|of|if|return|while|yield|continue|new|true|false|null)$/.test(text)?'keyword':/^\d/.test(text)?'number':''}))}
</script>

<template>
<figure class="lab informed-lab" aria-label="Mô phỏng tìm kiếm UCS, Greedy và A sao">
  <div class="informed-settings">
    <label>Chiến lược<select v-model="mode"><option value="ucs">UCS · Ưu tiên g</option><option value="greedy">Greedy · Ưu tiên h</option><option value="astar">A* · Ưu tiên g + h</option></select></label>
    <label>Trường hợp<select v-model="exampleId"><option v-for="e in informedExamples" :key="e.id" :value="e.id">{{ e.title }}</option></select></label>
    <label class="check"><input v-model="zero" type="checkbox">Đặt mọi h bằng 0</label>
    <label v-if="mode!=='greedy'" class="check"><input v-model="reopen" type="checkbox">Mở lại trạng thái khi có đường tốt hơn</label>
  </div>
  <p class="convention">Cạnh có hướng, chi phí không âm. Phá hòa theo thứ tự thêm vào biên. Kiểm tra đích sau khi bỏ bản ghi cũ. Chỉ thêm lại khi g giảm nghiêm ngặt. Greedy không mở lại trạng thái đã đóng. Lịch sử phục vụ thao tác quay lại, không đại diện cho bộ nhớ vốn có của thuật toán.</p>
  <p v-if="!reopen && mode==='astar' && !diagnostic.consistent" class="notice">Đang tắt mở lại với heuristic chưa nhất quán. Kết quả có thể mất tính tối ưu dù heuristic chấp nhận được.</p>
  <SimulationControls v-model="step" :max="frames.length-1" :reset-key="resetKey" />
  <p role="status" aria-live="polite" class="informed-status">{{ description[state.phase] }}<span v-if="current"> Nút #{{ current.id }}: {{ current.state }}. g = {{ current.g }}, h = {{ current.h }}, g + h = {{ current.g+current.h }}. Độ ưu tiên = {{ current.f }}.</span></p>
  <div class="informed-panels">
    <section class="informed-graph" aria-label="Đồ thị và heuristic"><h4>Trạng thái và chi phí</h4>
      <svg :viewBox="`0 0 370 ${height}`" role="img" aria-label="Đồ thị có hướng, chi phí trên cạnh và heuristic dưới đỉnh">
        <defs><marker :id="marker" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M1 1 9 5 1 9" /></marker></defs>
        <g v-for="(e,i) in edges" :key="i" :class="{highlight:state.edge?.[0]===e.a&&state.edge?.[1]===e.b}"><path :d="curve(e)" :marker-end="`url(#${marker})`" /><text class="edge-label" :x="edgeLabel(e).x" :y="edgeLabel(e).y" text-anchor="middle">{{ e.w }}</text></g>
        <g v-for="v in vertices" :key="v.id" :class="{current:current?.state===v.id,closed:state.closed.includes(v.id),queued:state.frontier.some(n=>n.state===v.id)}"><circle :cx="v.x" :cy="v.y" r="21"/><circle v-if="v.id===example.goal" :cx="v.x" :cy="v.y" r="26" class="goal"/><text :x="v.x" :y="v.y+5" text-anchor="middle">{{ v.id }}</text><text :x="heuristicLabel(v).x" :y="heuristicLabel(v).y" :text-anchor="heuristicLabel(v).anchor">h = {{ example.h[v.id] }}</text></g>
      </svg>
      <p>Viền đôi: Đích. Viền đậm: Đang xét. Nền nhạt: Có bản ghi ở biên.</p>
      <p>Đường hiện tại: {{ state.path.join(' → ')||'Chưa lấy nút' }}</p><p>Đang đóng: {{ state.closed.join(', ')||'Chưa có' }}</p>
    </section>
    <section class="informed-frontier" aria-label="Biên tìm kiếm"><h4>Biên theo thứ tự lấy ra</h4>
      <ol v-if="frontier.length"><li v-for="n in frontier" :key="n.id"><strong>#{{ n.id }} · {{ n.state }} · Ưu tiên {{ n.f }}</strong><span>g = {{ n.g }} · h = {{ n.h }} · g + h = {{ n.g+n.h }}</span><span>Cha {{ n.parent===null?'∅':'#'+n.parent }} · Sâu {{ n.depth }}<template v-if="n.g!==state.best[n.state]"> · Bản ghi cũ</template></span></li></ol><p v-else>Biên rỗng.</p>
      <div v-if="state.result" class="informed-result"><h4>Đường đi trả về</h4><p>{{ state.result.path.join(' → ') }}</p><p>Tổng chi phí {{ state.result.cost }} · {{ state.result.depth }} hành động</p></div>
    </section>
  </div>
  <section class="heuristic-audit"><h4>Kiểm tra bảng heuristic</h4><p>Chấp nhận được: {{ diagnostic.admissible?'Có':'Không' }}. Nhất quán: {{ diagnostic.consistent?'Có':'Không' }}.</p>
    <p v-if="diagnostic.over.length">Ước lượng quá cao tại: {{ diagnostic.over.join(', ') }}.</p>
    <ul v-if="diagnostic.violations.length"><li v-for="v in diagnostic.violations" :key="v.from+'-'+v.to">Cạnh {{ v.from }} → {{ v.to }} vi phạm: {{ v.left }} &gt; {{ v.cost }} + {{ example.h[v.to] }} = {{ v.right }}.</li></ul>
    <details><summary>Chi phí thật để đối chiếu và kết quả ba chiến lược</summary><p>Chi phí thật được tính riêng bằng phép nới lỏng Bellman, chỉ dùng kiểm chứng và không điều khiển thuật toán phía trên.</p><p v-for="v in vertices" :key="v.id">{{ v.id }}: h = {{ example.h[v.id] }}, h* = {{ Number.isFinite(diagnostic.exact[v.id])?diagnostic.exact[v.id]:'∞ (Không tới được đích)' }}.</p><p v-for="r in summary" :key="r.mode">{{ names[r.mode] }}: {{ r.end.phase==='budget'?'Chạm giới hạn xem':r.end.result?'Chi phí '+r.end.result.cost:'Không có đường' }}. {{ r.expanded }} lần mở rộng. So sánh này bật mở lại cho UCS và A*.</p></details>
  </section>
  <section class="informed-code"><div class="code-bar"><h4>JavaScript · Dòng {{ line+1 }} đang thực thi</h4><button type="button" @click="copy">{{ copied?'Đã chép mã':'Chép mã' }}</button></div><pre><code><span v-for="(t,j) in tokens(informedCode[line]||'')" :key="j" :class="t.kind">{{ t.text }}</span></code></pre>
    <details><summary>Xem đầy đủ chương trình đang chạy</summary><p>Hàm sinh trả từng bước bằng yield. snap chỉ sao chép dữ liệu quan sát. Dãy frontier được sắp trực tiếp để dễ theo dõi, khi giải bài lớn có thể thay bằng heap.</p><pre><code><span v-for="(row,i) in informedCode" :key="i" class="code-row" :class="{active:i===line}"><span class="line-number" aria-hidden="true">{{ i+1 }}</span><span><span v-for="(t,j) in tokens(row)" :key="j" :class="t.kind">{{ t.text }}</span></span></span></code></pre></details>
  </section>
  <details class="informed-edit"><summary>Thay đồ thị và bảng heuristic</summary><p>JSON gồm graph (Danh sách kề), h (Bảng heuristic), start và goal. Tối đa 8 trạng thái. Heuristic tại đích bằng 0. Có thể nhập heuristic ước lượng quá để quan sát phản ví dụ.</p><label>Dữ liệu<textarea v-model="input" rows="10" spellcheck="false"/></label><button type="button" @click="apply">Áp dụng và đặt lại</button><p v-if="error" role="alert">{{ error }}</p></details>
  <details class="lab-tasks"><summary>Thử dự đoán trước khi chạy</summary><ol><li>Chuyển giữa Greedy và A*. Nút nào được lấy ra tiếp theo và dựa trên giá trị nào?</li><li>Chọn đích xuất hiện sớm. Quan sát lúc G được thêm vào biên và lúc G thực sự được lấy ra.</li><li>Chọn heuristic chưa nhất quán, rồi tắt và bật mở lại. Giải thích vì sao kết quả thay đổi từ 6 thành 5.</li><li>Đặt mọi h bằng 0. Đối chiếu từng bước của A* và UCS.</li></ol></details>
</figure>
</template>

<style scoped>
.informed-lab{min-width:0}.informed-settings{display:grid;grid-template-columns:1fr 1fr;gap:12px}.informed-settings label,.informed-edit label{display:grid;gap:6px;font:var(--fs-small)/1.6 var(--font-ui)}.informed-lab :is(select,button,textarea){min-height:44px;border:1px solid var(--control);border-radius:var(--radius);padding:8px;background:var(--paper);color:var(--ink);font:inherit;max-width:100%}.informed-lab select{width:100%}.informed-lab :is(button,select,input,textarea):focus-visible{outline:3px solid var(--tim);outline-offset:3px}.informed-settings .check{display:flex;align-items:center;gap:8px}.check input{width:22px;height:22px;flex-shrink:0}.convention{font-size:var(--fs-small);line-height:1.7;color:var(--ink-2)}.informed-status,.notice{padding:12px;border-left:3px solid var(--tim);background:var(--tim-soft);line-height:1.7}.informed-panels{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}.informed-panels section{min-width:0;padding:12px;border:1px solid var(--rule);border-radius:var(--radius);background:var(--paper)}.informed-lab h4{font:600 var(--fs-ui)/1.5 var(--font-ui);margin:0 0 10px}.informed-graph svg{width:100%;margin:0;border:0;max-height:none}.informed-graph svg path{stroke:var(--ink-2);stroke-width:1.3;fill:none}.informed-graph circle{stroke:var(--ink-2);stroke-width:1.4;fill:var(--paper)}.informed-graph text{font:16px var(--font-ui);fill:var(--ink)}.informed-graph .edge-label{paint-order:stroke;stroke:var(--paper);stroke-width:6px;stroke-linejoin:round}.informed-graph .highlight path{stroke:var(--tim);stroke-width:2.2}.informed-graph .closed circle{fill:var(--rule)}.informed-graph .queued circle{fill:var(--tim-soft)}.informed-graph .current circle{stroke:var(--tim);stroke-width:2.5}.informed-graph .goal{fill:none!important;stroke-dasharray:3 3}.informed-panels p{font-size:var(--fs-small);line-height:1.7;overflow-wrap:anywhere}.informed-frontier ol{margin:0;padding:0;list-style:none;display:grid;gap:8px;max-height:430px;overflow:auto}.informed-frontier li{display:grid;gap:3px;padding:8px;border:1px solid var(--rule);border-radius:var(--radius);font-size:var(--fs-small)}.informed-result{margin-top:16px;padding:12px;background:var(--tim-soft);border-radius:var(--radius);overflow-wrap:anywhere}.heuristic-audit{margin-top:20px;font-size:var(--fs-small);line-height:1.7}.code-bar{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;margin-top:20px}.informed-code{min-width:0}.informed-code pre{white-space:pre-wrap;overflow-wrap:anywhere;overflow:visible;background:var(--paper);padding:12px;color:var(--ink);font:13px/1.8 var(--font-code);border:1px solid var(--rule);border-radius:var(--radius)}.informed-code code{font:inherit}.code-row{display:grid;grid-template-columns:3ch minmax(0,1fr);gap:8px}.code-row.active{background:var(--tim-soft);border-left:3px solid var(--tim)}.line-number{user-select:none;color:var(--ink-2)}.keyword{color:var(--tim);font-weight:600}.string{color:var(--xanh)}.number{color:var(--do)}.informed-edit textarea{display:block;width:100%;box-sizing:border-box;font:12px/1.6 var(--font-code);margin:8px 0}.informed-lab details{margin-top:16px;font-size:var(--fs-small);line-height:1.7}.informed-lab summary{cursor:pointer;min-height:44px}.informed-lab button{cursor:pointer;font-size:var(--fs-small)}@media(max-width:700px){.informed-panels,.informed-settings{grid-template-columns:minmax(0,1fr)}.informed-lab{padding:12px}.informed-panels section{padding:8px}}
</style>
