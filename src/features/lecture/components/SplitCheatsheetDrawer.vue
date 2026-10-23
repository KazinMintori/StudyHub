<script setup>
import { ref, computed, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { useLecture } from '../../navigation/index.mjs'
import { loadLecturePayload } from '../services/lecture-payload.mjs'
import { filterParallelCheatsheet } from '../services/parallel-cheatsheet.mjs'
import { lecturePath } from '../services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'
import MathText from '../../../core/math/components/MathText.vue'

const { course, lesson } = useLecture()
const isOpen = ref(false), payload = ref(null), loading = ref(false), error = ref(false)
const query = ref(''), search = ref(null)
let version = 0, previousFocus
const available = computed(() => course.value && lesson.value && course.value.id !== 'triet-hoc-mac-lenin')
const sections = computed(() => filterParallelCheatsheet(payload.value?.cheatsheet, query.value))
const fullCheatsheetLink = computed(() => available.value
 ? studyLink(lecturePath(course.value.id,lesson.value.slug,'cheatsheet')) : '')
async function fetchCheatsheet() {
 if (!available.value) return
 const current = ++version
 loading.value = true; error.value = false
 try {
  const result = await loadLecturePayload(course.value,lesson.value)
  if (current === version) payload.value = result
 } catch {
  if (current === version) { payload.value = null; error.value = true }
 } finally {
  if (current === version) loading.value = false
 }
}
function closeDrawer() {
 isOpen.value = false
 if (previousFocus?.isConnected) previousFocus.focus()
}
async function toggleDrawer() {
 if (isOpen.value) { closeDrawer(); return }
 previousFocus = document.activeElement; isOpen.value = true
 if (!payload.value) fetchCheatsheet()
 await nextTick(); search.value?.focus()
}
function handleKeydown(e) {
 if (e.key === 'Escape' && isOpen.value) { e.preventDefault(); closeDrawer(); return }
 const target = e.target
 if (['INPUT','TEXTAREA','SELECT'].includes(target?.tagName) || target?.isContentEditable) return
 if (e.altKey && !e.ctrlKey && !e.metaKey && e.key.toLowerCase() === 'c' && available.value) {
  e.preventDefault(); toggleDrawer()
 }
}
watch(isOpen,value => {
 if (typeof document !== 'undefined') document.documentElement.classList.toggle('study-lookup-open',value)
})
watch(() => [course.value?.id,lesson.value?.slug],() => {
 version++; payload.value = null; query.value = ''; loading.value = false; error.value = false
 if (!available.value) closeDrawer()
 else if (isOpen.value) fetchCheatsheet()
})
onMounted(() => window.addEventListener('keydown',handleKeydown))
onUnmounted(() => {
 version++; window.removeEventListener('keydown',handleKeydown)
 document.documentElement.classList.remove('study-lookup-open')
})
</script>

<template>
 <div v-if="available" class="split-cheatsheet-container">
  <button type="button" class="split-cheatsheet-trigger" :aria-expanded="isOpen" aria-controls="parallel-cheatsheet"
   title="Tra cứu công thức khi đọc bài (Alt+C)" @click="toggleDrawer">
   {{ isOpen ? 'Đóng tra cứu' : 'Tra cứu song song' }}
  </button>
  <Teleport to="body">
   <aside v-if="isOpen" id="parallel-cheatsheet" class="split-cheatsheet-drawer"
    aria-labelledby="parallel-cheatsheet-title" aria-label="Cheatsheet song song">
    <header class="drawer-header">
     <div class="drawer-title-group">
      <p class="drawer-kicker">Tra cứu khi đọc</p>
      <h2 id="parallel-cheatsheet-title" class="drawer-title">{{ lesson.title }}</h2>
     </div>
     <button type="button" class="drawer-close-btn" @click="closeDrawer">Đóng</button>
    </header>
    <div class="drawer-search">
     <label for="parallel-cheatsheet-search">Tìm định nghĩa hoặc công thức</label>
     <input id="parallel-cheatsheet-search" ref="search" v-model="query" type="search" autocomplete="off"
      placeholder="Ví dụ: Bảo toàn, mômen">
     <a :href="fullCheatsheetLink" class="drawer-full-link">Mở trang Cheatsheet</a>
    </div>
    <div class="drawer-body" tabindex="0" aria-label="Nội dung tra cứu">
     <p v-if="loading" role="status">Đang tải nội dung…</p>
     <div v-else-if="error" role="alert">
      <p>Chưa tải được nội dung tra cứu.</p>
      <button type="button" class="study-button" @click="fetchCheatsheet">Thử lại</button>
     </div>
     <template v-else-if="sections.length">
      <article v-for="section in sections" :key="section.id" class="drawer-section">
       <h3>{{ section.title }}</h3>
       <section v-for="(item,index) in section.items" :key="index" class="drawer-item">
        <h4 v-if="item.name">{{ item.name }}</h4>
        <div v-if="item.formulaRows?.length" class="formula-group">
         <div v-for="(row,rowIndex) in item.formulaRows" :key="rowIndex" class="formula-line">
          <p v-if="row.label" class="formula-label"><MathText :text="row.label" /></p>
          <MathText as="div" class="formula-value" :text="row.formula" />
         </div>
        </div>
        <MathText v-else-if="item.formula" as="div" class="formula-value" :text="item.formula" />
        <MathText v-if="item.description" as="p" :text="item.description" />
        <ul v-if="item.variables?.length">
         <li v-for="(variable,i) in item.variables" :key="i"><MathText :text="variable" /></li>
        </ul>
        <ul v-if="item.bullets?.length">
         <li v-for="(bullet,i) in item.bullets" :key="i"><MathText :text="bullet" /></li>
        </ul>
        <MathText v-if="item.note" as="p" :text="item.note" />
        <pre v-if="item.code"><code>{{ item.code }}</code></pre>
       </section>
       <dl v-for="(row,i) in section.table?.rows" :key="i" class="drawer-table-row">
        <div v-for="(cell,j) in row" :key="j">
         <dt><MathText :text="section.table.headers[j]" /></dt>
         <dd><MathText :text="cell" /></dd>
        </div>
       </dl>
      </article>
     </template>
     <p v-else role="status">{{ query.trim() ? 'Không tìm thấy nội dung phù hợp. Thử từ khóa khác.' : 'Bài này chưa có Cheatsheet riêng.' }}</p>
    </div>
   </aside>
  </Teleport>
 </div>
</template>

<style scoped>
.split-cheatsheet-container{min-width:0;display:flex}
.split-cheatsheet-trigger,.drawer-close-btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:var(--space-2) var(--space-3);border:1px solid var(--rule);border-radius:var(--radius);color:var(--ink-2);background:var(--paper);font:500 var(--fs-small)/1.4 var(--font-ui);white-space:nowrap;overflow:visible}
.split-cheatsheet-trigger:hover,.split-cheatsheet-trigger[aria-expanded=true]{color:var(--tim);border-color:var(--tim);background:var(--tim-soft)}
.split-cheatsheet-drawer{position:fixed;z-index:45;top:calc(var(--vp-nav-height) + var(--space-4));right:var(--space-4);bottom:var(--space-4);width:440px;max-width:calc(100vw - 32px);display:flex;flex-direction:column;min-width:0;border:1px solid var(--rule);border-radius:var(--radius-lg);background:var(--paper);color:var(--ink);box-shadow:var(--shadow)}
.drawer-header{display:flex;align-items:flex-start;gap:var(--space-3);padding:var(--space-4);border-bottom:1px solid var(--rule)}
.drawer-title-group{flex:1;min-width:0}
.drawer-kicker{margin:0 0 var(--space-1);color:var(--ink-3);font:500 var(--fs-meta)/1.5 var(--font-ui)}
.drawer-title{margin:0;font:600 var(--fs-ui)/1.5 var(--font-ui);overflow-wrap:anywhere}
.drawer-close-btn{flex:none}
.drawer-search{display:grid;gap:var(--space-2);padding:var(--space-3) var(--space-4);border-bottom:1px solid var(--rule)}
.drawer-search label{font:500 var(--fs-small)/1.5 var(--font-ui)}
.drawer-search input{width:100%;box-sizing:border-box;font-size:16px;min-height:44px}
.drawer-full-link{font-size:var(--fs-small);color:var(--tim);min-height:32px;display:flex;align-items:center}
.drawer-body{flex:1;min-height:0;min-width:0;overflow:auto;scrollbar-width:none;padding:var(--space-4);overscroll-behavior:contain;font:var(--fs-small)/1.65 var(--font-ui)}
.drawer-body::-webkit-scrollbar{display:none;width:0;height:0}
.drawer-section + .drawer-section{margin-top:var(--space-6)}
.drawer-section h3{font-size:var(--fs-ui);line-height:1.5;margin:0 0 var(--space-3)}
.drawer-item + .drawer-item{border-top:1px solid var(--rule);margin-top:var(--space-4);padding-top:var(--space-4)}
.drawer-item h4{font-size:var(--fs-small);line-height:1.5;margin:0 0 var(--space-2);font-weight:600}
.drawer-item :is(p,ul){margin:var(--space-2) 0}
.drawer-item ul{padding-left:20px}
.formula-value{min-width:0}
.formula-label{color:var(--ink-3)}
.drawer-item pre{white-space:pre-wrap;overflow-wrap:anywhere;font:var(--fs-small)/1.6 var(--font-code)}
.drawer-table-row{margin:var(--space-3) 0;padding:var(--space-3) 0;border-top:1px solid var(--rule)}
.drawer-table-row > div{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:var(--space-2)}
.drawer-table-row dd{margin:0;min-width:0}
.drawer-table-row dt{color:var(--ink-3)}
@media(max-width:1279px){
 .split-cheatsheet-drawer{top:auto;left:0;right:0;bottom:0;width:auto;max-width:none;height:48dvh;max-height:calc(100dvh - var(--vp-nav-height) - 52px);border-radius:var(--radius-lg) var(--radius-lg) 0 0}
 .drawer-header{padding:var(--space-3) var(--space-4)}
 .drawer-search{padding-block:var(--space-2)}
}
</style>
