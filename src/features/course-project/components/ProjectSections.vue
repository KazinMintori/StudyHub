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
      <span>Ví dụ thực hành <small>Kế hoạch và dự án Porto</small></span>
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
:global(.project-result-gallery) { display: grid; grid-template-columns: repeat(2,minmax(0,1fr)); gap: var(--space-5); align-items: start; margin: var(--space-5) 0; }
:global(.project-result-gallery .lecture-figure) { margin: 0; min-width: 0; }
:global(.project-result-gallery img) { width: 100%; height: auto; border: 1px solid var(--rule); border-radius: var(--radius-lg); }
@media (max-width: 767px) { :global(.project-result-gallery) { grid-template-columns: 1fr; } }
@media (max-width: 480px) { .project-sections { grid-template-columns: 1fr; } }
@media (max-width: 600px) {
  :global(.data-project-brief .vp-doc .study-data-table) {
    display: block;
    width: 100%;
    max-width: 100%;
    overflow: visible;
    border: 0;
  }
  :global(.data-project-brief .vp-doc .study-data-table thead) {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip-path: inset(50%);
    white-space: nowrap;
  }
  :global(.data-project-brief .vp-doc .study-data-table tbody) { display: block; }
  :global(.data-project-brief .vp-doc .study-data-table tbody tr) {
    display: block;
    margin: var(--space-3) 0;
    border: 1px solid var(--rule);
    border-radius: var(--radius-md, 8px);
  }
  :global(.data-project-brief .vp-doc .study-data-table td) {
    display: block;
    width: auto;
    min-width: 0;
    padding: var(--space-3);
    border: 0;
    white-space: normal;
    overflow-wrap: anywhere;
  }
  :global(.data-project-brief .vp-doc .study-data-table td + td) { border-top: 1px solid var(--rule); }
  :global(.data-project-brief .vp-doc .study-data-table td::before) {
    content: attr(data-label);
    display: block;
    margin-bottom: var(--space-1);
    color: var(--ink-3);
    font-weight: 600;
  }
  :global(.data-project-brief .vp-doc .study-data-table td code) {
    white-space: normal;
    overflow-wrap: anywhere;
  }
}
</style>
