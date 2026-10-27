<script setup>
function jump(end) {
  const content = document.querySelector('.VPDoc .content-container')
  const top = end && content ? window.scrollY + content.getBoundingClientRect().bottom - window.innerHeight + 24 : 0
  window.scrollTo({ top: Math.max(0, top), behavior: 'instant' })
}
</script>

<template>
  <nav class="reading-page-controls" aria-label="Di chuyển nhanh trong bài">
    <button type="button" title="Về đầu bài" aria-label="Về đầu bài" @click="jump(false)"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M5 5h14M7 14l5-5 5 5M12 9v11" /></svg></button>
    <button type="button" title="Đến cuối bài" aria-label="Đến cuối bài" @click="jump(true)"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M5 19h14M7 10l5 5 5-5M12 15V4" /></svg></button>
  </nav>
</template>

<style scoped>
.reading-page-controls { position: fixed; right: max(var(--space-3), env(safe-area-inset-right)); bottom: calc(max(var(--space-4), env(safe-area-inset-bottom)) + 56px); z-index: 22; display: grid; border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper); box-shadow: var(--shadow-soft); }
button { display: grid; place-items: center; width: 44px; height: 44px; color: var(--ink-2); border-radius: var(--radius-sm); }
button + button { border-top: 1px solid var(--rule); }
button:hover { background: var(--tim-soft); color: var(--tim); }
svg { fill: none; stroke: currentColor; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
@media print { .reading-page-controls { display: none; } }
</style>
