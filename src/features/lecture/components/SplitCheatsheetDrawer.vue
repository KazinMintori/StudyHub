<script setup>
import { ref, computed, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { useLecture } from '../../navigation/index.mjs'
import { useTopic } from '../controllers/topic-state.js'
import { loadLecturePayload } from '../services/lecture-payload.mjs'
import { loadConceptData } from '../../wiki/services/concept-loader.mjs'
import { filterParallelCheatsheet } from '../services/parallel-cheatsheet.mjs'
import { lectureConceptIds, lecturePath } from '../services/lecture-model.mjs'
import { lookupConcepts, lookupConnections, prioritizeLookupSections } from '../services/lesson-lookup.mjs'
import { studyLink } from '../../../core/routing/links.js'
import MathText from '../../../core/math/components/MathText.vue'

const { course, lesson } = useLecture()
const { topic } = useTopic()
const isOpen = ref(false), payload = ref(null), related = ref(null), loading = ref(false), error = ref(false)
const query = ref(''), search = ref(null), closeButton = ref(null)
const scope = ref('lesson'), view = ref('all'), inspectedId = ref(''), limit = ref(20)
let version = 0, previousFocus
const available = computed(() => Boolean(course.value && lesson.value))
const ids = computed(() => lectureConceptIds(lesson.value))
const filters = [{ id:'all', label:'Tổng hợp' }, { id:'formula', label:'Công thức' }, { id:'relations', label:'Liên hệ' }]
const sections = computed(() => {
 const result = prioritizeLookupSections(filterParallelCheatsheet(payload.value?.cheatsheet,query.value),topic.value?.source)
 return view.value === 'formula' ? result.map(section => ({ ...section, table:null, items:(section.items || []).filter(item => item.formula || item.formulaRows?.length) })).filter(section => section.items.length) : result
})
const concepts = computed(() => lookupConcepts(payload.value?.concepts,ids.value,query.value,{ global:scope.value === 'wiki' }))
const connections = computed(() => lookupConnections(payload.value?.concepts,ids.value,related.value || (() => []),query.value))
const inspected = computed(() => payload.value?.concepts?.[inspectedId.value])
const hasResults = computed(() => scope.value === 'wiki' ? concepts.value.length : view.value === 'relations' ? connections.value.length : sections.value.length || (view.value === 'all' && concepts.value.length))
const fullCheatsheetLink = computed(() => available.value ? studyLink(lecturePath(course.value.id,lesson.value.slug,'cheatsheet')) : '')
async function fetchContent() {
 if (!available.value) return
 const current = ++version
 loading.value = true; error.value = false
 try {
  const [result,dictionary] = await Promise.all([loadLecturePayload(course.value,lesson.value),loadConceptData()])
  if (current === version) { payload.value = result; related.value = dictionary.relatedConcepts }
 } catch {
  if (current === version) { payload.value = null; error.value = true }
 } finally { if (current === version) loading.value = false }
}
function closeDrawer(restoreFocus = true) {
 isOpen.value = false
 if (restoreFocus && previousFocus?.isConnected) previousFocus.focus()
}
async function openDrawer(returnFocus) {
 if (!available.value) return
 previousFocus = returnFocus || document.activeElement
 scope.value = 'lesson'; view.value = 'all'; query.value = ''; inspectedId.value = ''; limit.value = 20
 isOpen.value = true
 if (!payload.value) fetchContent()
 await nextTick()
 // Let mobile readers inspect the reference without opening the keyboard.
 closeButton.value?.focus()
}
function changeScope(value) { scope.value = value; inspectedId.value = ''; limit.value = 20 }
function handleKeydown(event) {
 if (event.key === 'Escape' && isOpen.value) { event.preventDefault(); closeDrawer(); return }
 if (['INPUT','TEXTAREA','SELECT'].includes(event.target?.tagName) || event.target?.isContentEditable) return
 if (event.altKey && !event.ctrlKey && !event.metaKey && event.key.toLowerCase() === 'c' && available.value) {
  event.preventDefault()
  if (isOpen.value) closeDrawer()
  else openDrawer(document.querySelector('.study-tools-trigger'))
 }
}
watch(isOpen,value => {
 if (typeof document !== 'undefined') document.documentElement.classList.toggle('study-lookup-open',value)
})
watch(query,() => { limit.value = 20; inspectedId.value = '' })
watch(() => [course.value?.id,lesson.value?.slug],() => {
 version++; payload.value = null; related.value = null; query.value = ''; scope.value = 'lesson'; view.value = 'all'; inspectedId.value = ''; loading.value = false; error.value = false
 if (!available.value) closeDrawer()
 else if (isOpen.value) fetchContent()
})
onMounted(() => window.addEventListener('keydown',handleKeydown))
onUnmounted(() => {
 version++; window.removeEventListener('keydown',handleKeydown)
 document.documentElement.classList.remove('study-lookup-open')
})
defineExpose({ openDrawer, closeDrawer })
</script>

<template>
 <Teleport to="body">
  <aside v-if="available && isOpen" id="parallel-cheatsheet" class="split-cheatsheet-drawer" role="dialog"
   aria-modal="false" aria-labelledby="knowledge-handbook-title">
   <header class="drawer-header">
    <div class="drawer-title-group">
     <h2 id="knowledge-handbook-title" class="drawer-title">Notebook</h2>
     <p class="drawer-context">{{ scope === 'wiki' ? 'Toàn bộ Wiki' : lesson.title }}</p>
    </div>
    <button ref="closeButton" type="button" class="drawer-close-btn" aria-label="Đóng Notebook" @click="closeDrawer">
     <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18" /></svg>
    </button>
   </header>
   <div class="drawer-search">
    <label for="knowledge-handbook-search">{{ scope === 'wiki' ? 'Tìm trong toàn bộ Wiki' : 'Tìm kiến thức trong bài đang học' }}</label>
    <input id="knowledge-handbook-search" ref="search" v-model="query" type="search" autocomplete="off" placeholder="Nhập khái niệm hoặc công thức…">
   </div>
   <div v-if="scope === 'lesson'" class="drawer-filters" role="group" aria-label="Loại kiến thức">
    <button v-for="filter in filters" :key="filter.id" type="button" :aria-pressed="view === filter.id" @click="view=filter.id; inspectedId=''">{{ filter.label }}</button>
   </div>
   <div class="drawer-body" tabindex="0" aria-label="Nội dung Notebook">
    <p v-if="loading" role="status">Đang tải kiến thức…</p>
    <div v-else-if="error" role="alert"><p>Chưa tải được nội dung.</p><button type="button" class="drawer-text-action" @click="fetchContent">Thử lại</button></div>
    <template v-else>
     <article v-if="inspected" class="drawer-inspected">
      <button type="button" class="drawer-text-action" @click="inspectedId=''">Trở về danh sách</button>
      <h3>{{ inspected.name }}</h3>
      <MathText as="p" :text="inspected.definition" />
      <template v-if="inspected.use"><h4>Liên hệ và cách dùng</h4><MathText as="p" :text="inspected.use" /></template>
      <template v-if="inspected.example"><h4>Ví dụ</h4><MathText as="p" :text="inspected.example" /></template>
      <a :href="studyLink(`/wiki/${inspectedId}`)" target="_blank" rel="noopener" class="drawer-wiki-link">Đọc mục Wiki đầy đủ<span class="visually-hidden"> trong thẻ mới</span> ↗</a>
     </article>
     <template v-else-if="scope === 'wiki'">
      <p v-if="!query.trim()" class="drawer-empty">Nhập từ khóa để tìm khái niệm từ tất cả các môn học.</p>
      <template v-else-if="concepts.length">
       <p class="drawer-result-count" role="status">{{ concepts.length }} kết quả trong Wiki</p>
       <article v-for="term in concepts.slice(0,limit)" :key="term.id" class="drawer-concept">
        <button type="button" class="drawer-concept-title" @click="inspectedId=term.id">{{ term.name }}</button>
        <MathText as="p" :text="term.definition" />
       </article>
       <button v-if="limit < concepts.length" type="button" class="drawer-text-action" @click="limit+=20">Hiện thêm kết quả</button>
      </template>
     </template>
     <template v-else-if="view === 'relations'">
      <article v-for="connection in connections" :key="connection.id" class="drawer-connection">
       <h3>{{ connection.name }}</h3>
       <p>Khái niệm liên quan</p>
       <div class="drawer-relation-links"><button v-for="term in connection.targets" :key="term.id" type="button" @click="inspectedId=term.id">{{ term.name }}</button></div>
      </article>
     </template>
     <template v-else>
      <p v-if="topic?.source" class="drawer-current-topic">Đang đọc {{ topic.source }}: {{ topic.title }}</p>
      <article v-for="section in sections" :key="section.id" class="drawer-section">
       <h3>{{ section.title }}</h3>
       <section v-for="(item,index) in section.items" :key="index" class="drawer-item">
        <h4 v-if="item.name">{{ item.name }}</h4>
        <MathText v-if="view === 'all' && item.description" as="p" :text="item.description" />
        <div v-if="item.formulaRows?.length" class="formula-group">
         <div v-for="(row,rowIndex) in item.formulaRows" :key="rowIndex" class="formula-line">
          <p v-if="row.label" class="formula-label"><MathText :text="row.label" /></p>
          <MathText as="div" class="formula-value" :text="row.formula" />
         </div>
        </div>
        <MathText v-else-if="item.formula" as="div" class="formula-value" :text="item.formula" />
        <ul v-if="item.variables?.length"><li v-for="(variable,i) in item.variables" :key="i"><MathText :text="variable" /></li></ul>
        <template v-if="view === 'all'">
         <ul v-if="item.bullets?.length"><li v-for="(bullet,i) in item.bullets" :key="i"><MathText :text="bullet" /></li></ul>
         <MathText v-if="item.note" as="p" :text="item.note" />
         <pre v-if="item.code"><code>{{ item.code }}</code></pre>
        </template>
       </section>
       <dl v-for="(row,i) in section.table?.rows" :key="i" class="drawer-table-row"><div v-for="(cell,j) in row" :key="j"><dt><MathText :text="section.table.headers[j]" /></dt><dd><MathText :text="cell" /></dd></div></dl>
      </article>
      <section v-if="view === 'all' && concepts.length" class="drawer-section">
       <h3>Khái niệm của bài</h3>
       <article v-for="term in concepts" :key="term.id" class="drawer-concept">
        <button type="button" class="drawer-concept-title" @click="inspectedId=term.id">{{ term.name }}</button>
        <MathText as="p" :text="term.definition" />
       </article>
      </section>
     </template>
     <p v-if="!inspected && !hasResults && (scope === 'lesson' || query.trim())" role="status" class="drawer-empty">{{ query.trim() ? 'Chưa có kết quả phù hợp trong phạm vi đang chọn.' : 'Mục này chưa có nội dung riêng cho bài học.' }}</p>
    </template>
   </div>
   <footer class="drawer-footer">
    <button type="button" class="drawer-scope-action" @click="changeScope(scope === 'lesson' ? 'wiki' : 'lesson')">{{ scope === 'lesson' ? 'Tìm trong toàn bộ Wiki' : 'Quay lại kiến thức của bài' }}<span aria-hidden="true">{{ scope === 'lesson' ? '→' : '←' }}</span></button>
    <a v-if="scope === 'lesson' && payload?.cheatsheet" :href="fullCheatsheetLink" class="drawer-full-link" @click="closeDrawer">Mở Cheatsheet</a>
    <a v-else :href="studyLink('/wiki/')" target="_blank" rel="noopener" class="drawer-full-link">Mở Wiki<span class="visually-hidden"> trong thẻ mới</span> ↗</a>
   </footer>
  </aside>
 </Teleport>
</template>

<style scoped>
.split-cheatsheet-drawer{position:fixed;z-index:80;top:calc(var(--vp-nav-height) + var(--space-4));right:var(--space-4);bottom:var(--space-4);width:440px;max-width:calc(100vw - 32px);display:flex;flex-direction:column;min-width:0;border:1px solid var(--rule);border-radius:var(--radius-lg);background:var(--paper);color:var(--ink);box-shadow:var(--shadow);font-family:var(--font-ui)}
.drawer-header{display:flex;align-items:flex-start;gap:var(--space-3);padding:var(--space-4);border-bottom:1px solid var(--rule)}
.drawer-title-group{flex:1;min-width:0}.drawer-title{margin:0;font:600 17px/1.4 var(--font-ui);overflow-wrap:anywhere}
.drawer-context{margin:var(--space-1) 0 0;color:var(--ink-3);font:400 var(--fs-meta)/1.5 var(--font-ui)}
.drawer-close-btn{display:grid;place-items:center;flex:none;min-width:44px;min-height:44px;border:1px solid var(--rule);border-radius:var(--radius);color:var(--ink-2);background:var(--paper);cursor:pointer}
.drawer-search{display:grid;gap:var(--space-2);padding:var(--space-3) var(--space-4)}
.drawer-search label{font:500 var(--fs-small)/1.5 var(--font-ui)}.drawer-search input{width:100%;min-width:0;box-sizing:border-box;font-size:16px;min-height:44px;padding:var(--space-2) var(--space-3);border:1px solid var(--rule);border-radius:var(--radius);background:var(--canvas);color:var(--ink)}
.drawer-filters{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--space-1);padding:0 var(--space-4) var(--space-3);border-bottom:1px solid var(--rule)}
.drawer-filters button{min-height:44px;padding:var(--space-2) var(--space-1);border:1px solid transparent;border-radius:var(--radius);color:var(--ink-2);background:var(--canvas);font:500 var(--fs-small)/1.4 var(--font-ui);cursor:pointer}
.drawer-filters button[aria-pressed=true]{color:var(--tim);background:var(--tim-soft);border-color:var(--tim)}
.drawer-body{flex:1;min-height:0;min-width:0;overflow:auto;scrollbar-width:none;padding:var(--space-4);overscroll-behavior:contain;font:var(--fs-small)/1.65 var(--font-ui)}
.drawer-body::-webkit-scrollbar{display:none;width:0;height:0}.drawer-current-topic,.drawer-result-count{margin:0 0 var(--space-4);color:var(--ink-3);font-size:var(--fs-meta)}
.drawer-section + .drawer-section{margin-top:var(--space-6)}.drawer-section h3,.drawer-connection h3,.drawer-inspected h3{font-size:var(--fs-ui);line-height:1.5;margin:0 0 var(--space-3)}
.drawer-item + .drawer-item{border-top:1px solid var(--rule);margin-top:var(--space-4);padding-top:var(--space-4)}.drawer-item h4,.drawer-inspected h4{font-size:var(--fs-small);line-height:1.5;margin:0 0 var(--space-2);font-weight:600}
.drawer-item :is(p,ul),.drawer-concept p{margin:var(--space-2) 0}.drawer-item ul{padding-left:20px}.formula-value{min-width:0}.formula-label{color:var(--ink-3)}
.drawer-item pre{white-space:pre-wrap;overflow-wrap:anywhere;font:var(--fs-small)/1.6 var(--font-code)}.drawer-table-row{margin:var(--space-3) 0;padding:var(--space-3) 0;border-top:1px solid var(--rule)}
.drawer-table-row>div{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:var(--space-2)}.drawer-table-row dd{margin:0;min-width:0}.drawer-table-row dt{color:var(--ink-3)}
.drawer-concept,.drawer-connection{padding-block:var(--space-3);border-bottom:1px solid var(--rule)}.drawer-concept-title{min-height:44px;color:var(--tim);font-weight:600;text-align:left;cursor:pointer}
.drawer-relation-links{display:flex;flex-wrap:wrap;gap:var(--space-2)}.drawer-relation-links button{min-height:44px;padding:var(--space-2) var(--space-3);border:1px solid var(--rule);border-radius:var(--radius);background:var(--canvas);color:var(--tim);text-align:left;cursor:pointer}
.drawer-connection>p,.drawer-empty{color:var(--ink-3)}.drawer-text-action,.drawer-wiki-link{display:inline-flex;align-items:center;min-height:44px;color:var(--tim);font-size:var(--fs-small);cursor:pointer}
.drawer-footer{display:flex;flex-wrap:wrap;align-items:center;gap:var(--space-1) var(--space-3);border-top:1px solid var(--rule);padding:var(--space-2) var(--space-4);padding-bottom:max(var(--space-2),env(safe-area-inset-bottom))}
.drawer-scope-action{display:flex;align-items:center;justify-content:space-between;gap:var(--space-2);flex:1 1 auto;min-height:44px;color:var(--tim);font:600 var(--fs-small)/1.4 var(--font-ui);text-align:left;cursor:pointer}.drawer-full-link{display:flex;align-items:center;min-height:44px;color:var(--ink-3);font-size:var(--fs-meta)}
:is(button,input,a):focus-visible{outline:2px solid var(--tim);outline-offset:3px}
@media(max-width:1279px){.split-cheatsheet-drawer{top:auto;left:0;right:0;bottom:0;width:auto;max-width:none;height:62dvh;max-height:calc(100dvh - var(--vp-nav-height) - 60px);border-radius:var(--radius-lg) var(--radius-lg) 0 0}.drawer-header{padding:var(--space-3) var(--space-4)}.drawer-search{padding-block:var(--space-2)}}
</style>
