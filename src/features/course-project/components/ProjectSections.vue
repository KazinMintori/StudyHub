<script setup>
import { withBase } from 'vitepress'
defineProps({ active: { type: String, default: 'brief' } })
</script>

<template>
  <nav class="project-sections" aria-label="Các phần của bài tập lớn">
    <a :href="withBase('/xu-ly-du-lieu/bai-tap-lon/')" :aria-current="active === 'brief' ? 'page' : undefined">
      <span class="project-section-number">1</span>
      <span>Đề bài tập lớn</span>
    </a>
    <a :href="withBase('/xu-ly-du-lieu/bai-tap-lon/thuc-hanh.html')" :aria-current="active === 'practice' ? 'page' : undefined">
      <span class="project-section-number">2</span>
      <span>Ví dụ thực hành <small>Sẽ cập nhật</small></span>
    </a>
  </nav>
</template>

<style scoped>
.project-sections { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; margin: 16px 0 28px; }
.project-sections a { display: flex; align-items: center; gap: 10px; min-height: 58px; padding: 12px 14px; border: 1px solid var(--rule); border-radius: 10px; text-decoration: none; color: var(--ink-2); background: var(--paper); line-height: 1.45; }
.project-sections a[aria-current] { border-color: var(--tim); background: var(--tim-soft); color: var(--ink); }
.project-sections a:hover { border-color: var(--tim); }
.project-sections a:focus-visible { outline: 2px solid var(--tim); outline-offset: 3px; }
.project-section-number { flex: 0 0 auto; font-size: 14px; color: var(--tim); }
.project-sections small { display: block; font-size: 12px; color: var(--ink-3); font-weight: 400; }
@media (max-width: 480px) { .project-sections { grid-template-columns: 1fr; } }
</style>
