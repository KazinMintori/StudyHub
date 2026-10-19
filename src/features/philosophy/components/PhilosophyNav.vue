<script setup>
import { studyLink } from '../../../core/routing/links.js'
defineProps({ exam: Boolean })
</script>

<template>
  <nav class="philosophy-nav" aria-label="Nội dung môn Triết học">
    <a :href="studyLink('/triet-hoc-mac-lenin/')" :aria-current="!exam ? 'page' : undefined">Học tập</a>
    <a :href="studyLink('/triet-hoc-mac-lenin/on-thi/')" :aria-current="exam ? 'page' : undefined">Ôn thi</a>
  </nav>
</template>

<style scoped>
.philosophy-nav { display: flex; gap: var(--space-6); border-bottom: 1px solid var(--rule); margin: var(--space-5) 0 var(--space-6); }
.philosophy-nav a { display: inline-flex; align-items: center; min-height: 48px; padding: var(--space-2) 0; color: var(--ink-2); font-size: var(--fs-ui); border-bottom: 2px solid transparent; }
.philosophy-nav a[aria-current] { color: var(--tim); border-color: var(--tim); font-weight: 600; }
.philosophy-nav a:hover { color: var(--tim); }
.philosophy-nav a:focus-visible { outline: 2px solid var(--tim); outline-offset: 4px; }
</style>
