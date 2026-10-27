<script setup>
import { computed, nextTick, onMounted, onUnmounted, ref, shallowRef } from 'vue'
import { courseCatalog } from '../../../content/catalog.mjs'
import { studyLink } from '../../../core/routing/links.js'
import { buildSearchEntries, searchEntries } from '../services/site-search.mjs'

const dialog = ref(null), input = ref(null), trigger = ref(null), query = ref('')
const entries = shallowRef(buildSearchEntries(courseCatalog))
const results = computed(() => searchEntries(entries.value, query.value))
let wikiLoaded = false, disposed = false
async function open() {
  if (dialog.value.open) return
  dialog.value.showModal()
  await nextTick()
  input.value.focus()
  if (!wikiLoaded) {
    try {
      const { concepts } = await import('../../../../docs/.vitepress/concepts.mjs')
      if (disposed) return
      entries.value = buildSearchEntries(courseCatalog, concepts)
      wikiLoaded = true
    } catch { /* Course and topic results remain available offline. */ }
  }
}
function close() { dialog.value.close(); trigger.value.focus() }
function hotkey(event) {
  const editing = event.target?.closest?.('input, textarea, select, [contenteditable="true"]')
  if (((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') || (!editing && event.key === '/')) {
    event.preventDefault()
    open()
  }
}
function move(event) {
  const links = [...dialog.value.querySelectorAll('.site-search-results a')]
  if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
    event.preventDefault()
    const index = links.indexOf(document.activeElement)
    const next = event.key === 'ArrowDown' ? index + 1 : index - 1
    if (next < 0) input.value.focus()
    else links[Math.min(next, links.length - 1)]?.focus()
  } else if (event.key === 'Enter' && event.target === input.value) {
    event.preventDefault()
    links[0]?.click()
  }
}
onMounted(() => window.addEventListener('keydown', hotkey))
onUnmounted(() => { disposed = true; window.removeEventListener('keydown', hotkey) })
</script>

<template>
  <button ref="trigger" type="button" class="site-search-button" aria-label="Tìm kiếm" aria-haspopup="dialog" title="Tìm kiếm (Ctrl + K)" @click="open">
    <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" /><path d="m16 16 5 5" /></svg>
    <span>Tìm kiếm</span><kbd>Ctrl K</kbd>
  </button>
  <Teleport to="body">
    <dialog ref="dialog" class="site-search-dialog" aria-labelledby="site-search-title" @keydown="move" @click="event => { if (event.target === dialog) close() }">
      <div class="site-search-heading"><label id="site-search-title" for="site-search-input">Tìm kiếm</label><button type="button" aria-label="Đóng tìm kiếm" @click="close">Đóng</button></div>
      <input id="site-search-input" ref="input" v-model="query" type="search" autocomplete="off" placeholder="Tìm bài giảng, chủ đề hoặc thuật ngữ…">
      <p class="site-search-status" role="status">{{ query.trim() ? (results.length ? `${results.length} kết quả${results.length === 30 ? ' đầu tiên' : ''}` : 'Chưa có kết quả. Thử từ khóa khác hoặc bỏ dấu.') : 'Nhập tên môn, bài giảng, chủ đề hoặc thuật ngữ. Có thể gõ không dấu.' }}</p>
      <ul class="site-search-results">
        <li v-for="result in results" :key="result.path"><a :href="studyLink(result.path)"><strong>{{ result.title }}</strong><span>{{ result.context }}</span></a></li>
      </ul>
    </dialog>
  </Teleport>
</template>

<style scoped>
.site-search-button { display: inline-flex; flex: 0 0 auto; align-items: center; justify-content: center; gap: var(--space-2); min-width: 44px; height: 44px; margin-right: var(--space-3); padding: 0 var(--space-2); border-radius: var(--radius); color: var(--ink-2); font: var(--fs-small)/1.5 var(--font-ui); }
.site-search-button:hover { color: var(--tim); background: var(--tim-soft); }
svg { fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; }
kbd { padding: 1px 5px; border: 1px solid var(--rule); border-radius: var(--radius-sm); font-size: var(--fs-meta); }
.site-search-dialog { position: fixed; inset: 12dvh 0 auto; width: min(640px, calc(100vw - 32px)); max-height: 76dvh; margin-inline: auto; padding: var(--space-5); overflow-y: auto; border: 1px solid var(--rule); border-radius: var(--radius-lg); background: var(--paper); color: var(--ink); box-shadow: var(--shadow); font: var(--fs-ui)/1.5 var(--font-ui); }
.site-search-dialog::backdrop { background: rgb(0 0 0 / .5); }
.site-search-heading { display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3); font-weight: 600; }
.site-search-heading button { min-height: 44px; padding-inline: var(--space-3); color: var(--tim); }
input { width: 100%; min-height: 48px; padding: var(--space-3); border: 1px solid var(--rule); border-radius: var(--radius); background: var(--canvas); color: var(--ink); font-size: 16px; }
.site-search-status { margin-block: var(--space-3); color: var(--ink-3); font-size: var(--fs-small); white-space: normal; }
ul { margin: 0; padding: 0; list-style: none; }
li + li { border-top: 1px solid var(--rule); }
li a { display: grid; gap: var(--space-1); padding: var(--space-3); border-radius: var(--radius-sm); white-space: normal; }
li a:hover, li a:focus-visible { background: var(--tim-soft); }
li span { color: var(--ink-3); font-size: var(--fs-small); }
@media (max-width: 1439px) { .site-search-button { margin-right: 0; } .site-search-button span, .site-search-button kbd { display: none; } }
@media print { .site-search-dialog { display: none; } }
</style>
