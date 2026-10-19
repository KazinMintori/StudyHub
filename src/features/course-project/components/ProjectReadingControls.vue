<script setup>
import { onMounted, onBeforeUnmount } from 'vue'
function toggle(open) {
  for (const detail of document.querySelectorAll('.project-brief-detail')) detail.open = open
}
function revealHash() {
  if (!location.hash) return
  let target
  try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))) } catch { return }
  if (!target) return
  let parent = target.closest('details')
  while (parent) { parent.open = true; parent = parent.parentElement?.closest('details') }
  requestAnimationFrame(() => target.scrollIntoView({ block: 'start' }))
}
onMounted(() => { revealHash(); window.addEventListener('hashchange', revealHash) })
onBeforeUnmount(() => window.removeEventListener('hashchange', revealHash))
</script>
<template>
  <div class="project-reading-controls" aria-label="Hiển thị phần giải thích chi tiết">
    <span>Chọn mục cần đọc</span>
    <div><button type="button" @click="toggle(true)">Mở tất cả</button><button type="button" @click="toggle(false)">Thu gọn tất cả</button></div>
  </div>
</template>
<style scoped>
.project-reading-controls { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--space-3); margin: var(--space-5) 0; font: 400 var(--fs-small)/1.6 var(--font-ui); }
.project-reading-controls > div { display: flex; flex-wrap: wrap; gap: var(--space-2); }
button { padding: var(--space-2) var(--space-3); min-height: 44px; border: 1px solid var(--rule); border-radius: var(--radius); cursor: pointer; color: var(--tim); background: var(--paper); }
button:hover { background: var(--tim-soft); border-color: var(--tim); }
button:focus-visible { outline: 2px solid var(--tim); outline-offset: 3px; }
:global(.data-project-brief .project-brief-detail) { margin: var(--space-3) 0; border: 1px solid var(--rule); border-radius: var(--radius-lg); background: var(--paper); }
:global(.data-project-brief .project-brief-detail > summary) { cursor: pointer; padding: var(--space-4); min-height: 56px; font: 600 var(--fs-ui)/1.7 var(--font-ui); color: var(--ink); }
:global(.data-project-brief .project-brief-detail > summary:hover) { color: var(--tim); background: var(--tim-soft); border-radius: var(--radius-lg); }
:global(.data-project-brief .project-brief-detail > summary:focus-visible) { outline: 2px solid var(--tim); outline-offset: 3px; }
:global(.data-project-brief .project-brief-detail[open]) { padding: 0 var(--space-4) var(--space-4); }
:global(.data-project-brief .project-brief-detail[open] > summary) { margin: 0 calc(-1 * var(--space-4)); border-bottom: 1px solid var(--rule); border-radius: var(--radius-lg) var(--radius-lg) 0 0; }
:global(.data-project-brief .project-brief-detail h3) { margin-top: var(--space-5); }
</style>
