<script setup>
import { computed, ref, onMounted, onUnmounted, watch } from 'vue'
import { withBase } from 'vitepress'
import { probabilitySourceLibrary as entries } from '../probability-source-library.mjs'
import { studyLink } from './links'

const selectedId = ref('1-questions-and-data--01-understanding-the-world')
const kind = ref('notes')
const loading = ref(true)
const loadFailed = ref(false)
const frame = ref(null)
const viewer = ref(null)
const selected = computed(() => entries.find(entry => entry.id === selectedId.value) || entries[0])
const groups = [...new Set(entries.map(entry => entry.group))]
const frameUrl = computed(() => withBase(`/materials/xac-suat-thong-ke/embedded/${selected.value.id}.${kind.value}.html`))
const index = computed(() => entries.indexOf(selected.value))
let timeout
function syncHash() {
  const params = new URLSearchParams(location.hash.slice(1))
  const entry = entries.find(entry => entry.id === params.get('bai'))
  if (entry) selectedId.value = entry.id
  const requested = params.get('tab') === 'slides' ? 'slides' : 'notes'
  kind.value = selected.value[requested] ? requested : selected.value.notes ? 'notes' : 'slides'
}
function writeHash() {
  if (typeof window === 'undefined') return
  history.replaceState(null, '', `${location.pathname}${location.search}#bai=${selectedId.value}&tab=${kind.value}`)
}
function select(id) {
  const entry = entries.find(entry => entry.id === id)
  if (!entry) return
  selectedId.value = id
  if (!entry[kind.value]) kind.value = entry.notes ? 'notes' : 'slides'
  writeHash()
}
function changeKind(value) {
  if (!selected.value[value]) return
  kind.value = value
  writeHash()
}
function loadDone() { loading.value = false; clearTimeout(timeout) }
function receive(event) {
  if (event.source !== frame.value?.contentWindow || event.data?.type !== 'studyhub-source-navigation') return
  const entry = entries.find(entry => entry.id === event.data.id)
  if (!entry || !['notes', 'slides'].includes(event.data.kind) || !entry[event.data.kind]) return
  select(entry.id)
  changeKind(event.data.kind)
}
function reload() {
  loadFailed.value = false
  loading.value = true
  if (frame.value) frame.value.src = frameUrl.value
}
async function fullscreen() {
  if (!viewer.value?.requestFullscreen) return
  try { await viewer.value.requestFullscreen() } catch {}
}
watch(frameUrl, () => {
  loading.value = true
  loadFailed.value = false
  clearTimeout(timeout)
  timeout = setTimeout(() => { if (loading.value) loadFailed.value = true }, 20000)
})
onMounted(() => {
  syncHash()
  window.addEventListener('hashchange', syncHash)
  window.addEventListener('message', receive)
})
onUnmounted(() => {
  clearTimeout(timeout)
  window.removeEventListener('hashchange', syncHash)
  window.removeEventListener('message', receive)
})
</script>

<template>
  <main class="course-shell source-reader">
    <nav class="book-breadcrumbs" aria-label="Đường dẫn">
      <a :href="studyLink('/xac-suat-thong-ke/')">Xác suất thống kê</a><span>/</span><span>Toàn bộ tài liệu</span>
    </nav>
    <h1>Toàn bộ Notes và Slides</h1>
    <p class="source-description">31 trang Notes và 28 bộ Slides. Nội dung gốc bằng tiếng Anh, giữ nguyên công thức, ví dụ và hình.</p>

    <div class="source-toolbar">
      <div class="source-picker">
        <label for="source-lesson">Chọn bài</label>
        <select id="source-lesson" :value="selectedId" @change="select($event.target.value)">
          <optgroup v-for="group in groups" :key="group" :label="group">
            <option v-for="entry in entries.filter(entry => entry.group === group)" :key="entry.id" :value="entry.id">{{ entry.title }}</option>
          </optgroup>
        </select>
      </div>
      <nav class="source-tabs" aria-label="Loại tài liệu">
        <button :disabled="!selected.notes" :aria-pressed="kind === 'notes'" @click="changeKind('notes')">Notes</button>
        <button :disabled="!selected.slides" :aria-pressed="kind === 'slides'" @click="changeKind('slides')">Slides</button>
      </nav>
      <button class="source-fullscreen" @click="fullscreen">Toàn màn hình</button>
    </div>

    <div class="source-position">
      <h2>{{ selected.title }}</h2>
      <span role="status" aria-live="polite">{{ loading ? 'Đang tải…' : `${kind === 'notes' ? 'Notes' : 'Slides'} · ${index + 1} / ${entries.length}` }}</span>
    </div>
    <div v-if="loadFailed" class="source-error" role="status">Tài liệu chưa tải được. <button @click="reload">Thử lại</button></div>
    <div ref="viewer" class="source-viewer">
      <iframe :key="frameUrl" ref="frame" :src="frameUrl" :title="`${kind === 'notes' ? 'Notes' : 'Slides'}: ${selected.title}`" sandbox="allow-scripts allow-popups allow-popups-to-escape-sandbox allow-presentation" allow="fullscreen" referrerpolicy="no-referrer" @load="loadDone" @error="loadFailed = true" />
    </div>
    <nav class="source-pagination" aria-label="Chuyển bài">
      <button class="study-button" :disabled="index === 0" @click="select(entries[index - 1].id)">← Bài trước</button>
      <button class="study-button" :disabled="index === entries.length - 1" @click="select(entries[index + 1].id)">Bài tiếp →</button>
    </nav>
    <details class="source-references"><summary>Tài liệu tham khảo</summary>
      <p>Stat 20, UC Berkeley, học kỳ xuân 2026. <a :href="selected[kind]" target="_blank" rel="noopener noreferrer">Mở tài liệu gốc</a> · <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer">CC BY 4.0</a>.</p>
    </details>
  </main>
</template>

<style scoped>
.source-reader { max-width: 1280px; padding-top: var(--space-5); }
.source-reader h1 { font-size: var(--fs-h1); font-weight: 600; margin: var(--space-3) 0; }
.source-description { color: var(--ink-2); margin-bottom: var(--space-5); }
.source-toolbar { display: flex; align-items: end; gap: var(--space-4); border-bottom: 1px solid var(--rule); padding-bottom: var(--space-3); }
.source-picker { flex: 1; min-width: 0; }
.source-picker label { display: block; margin-bottom: var(--space-1); font-size: var(--fs-small); color: var(--ink-2); }
.source-picker select { width: 100%; }
.source-tabs { display: flex; gap: var(--space-3); }
.source-tabs button, .source-fullscreen { min-height: 44px; padding: var(--space-2); color: var(--ink-2); }
.source-tabs button[aria-pressed=true] { color: var(--ink); border-bottom: 2px solid var(--tim); font-weight: 600; }
.source-tabs button:disabled { opacity: .45; cursor: default; }
.source-fullscreen:hover { color: var(--tim); }
.source-position { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--space-2); margin: var(--space-4) 0; }
.source-position h2 { font-size: var(--fs-lead); font-weight: 500; }
.source-position > span { color: var(--ink-3); font-size: var(--fs-small); }
.source-viewer { background: var(--printed-paper); border: 1px solid var(--rule); }
.source-viewer iframe { display: block; width: 100%; height: max(600px, calc(100svh - 250px)); border: 0; }
.source-viewer:fullscreen { width: 100vw; height: 100svh; }
.source-viewer:fullscreen iframe { height: 100%; }
.source-pagination { display: flex; justify-content: space-between; margin-top: var(--space-3); }
.source-references { color: var(--ink-2); margin-top: var(--space-5); font-size: var(--fs-small); }
.source-references summary { min-height: 44px; }
.source-references a { color: var(--tim); text-decoration: underline; }
.source-error { color: var(--do); padding: var(--space-3) 0; }
.source-error button { min-height: 44px; text-decoration: underline; }
@media(max-width:767px) {
  .source-reader { padding: var(--space-4); }
  .source-toolbar { flex-wrap: wrap; gap: var(--space-2) var(--space-4); }
  .source-picker { flex-basis: 100%; }
  .source-tabs { flex: 1; }
  .source-reader h1 { font-size: var(--fs-h2); }
  .source-viewer iframe { height: 75svh; min-height: 500px; }
}
</style>
