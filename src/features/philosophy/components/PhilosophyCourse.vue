<script setup>
import { course } from '../../../content/courses/triet-hoc-mac-lenin/course.mjs'
import { studyLink } from '../../../core/routing/links.js'
</script>

<template>
  <main class="philosophy-course course-shell">
    <nav class="book-breadcrumbs" aria-label="Đường dẫn"><a :href="studyLink('/')">Trang chủ</a><span>/</span><span>Học phần</span></nav>
    <p class="philosophy-eyebrow">TRIẾT HỌC · 3 CHƯƠNG</p>
    <h1>Triết học Mác – Lênin</h1>
    <p class="philosophy-lead">Từ những câu hỏi về thế giới và con người đến cách nhìn biện chứng về tự nhiên, nhận thức và đời sống xã hội.</p>
    <section v-for="chapter in course.lessons" :key="chapter.slug" class="philosophy-chapter">
      <div class="philosophy-chapter-number" aria-hidden="true">0{{ chapter.number }}</div>
      <div class="philosophy-chapter-body">
        <p class="philosophy-eyebrow">Chương {{ chapter.number }}</p>
        <h2><a :href="studyLink(`/triet-hoc-mac-lenin/bai-giang/${chapter.slug}`)">{{ chapter.title }}</a></h2>
        <p>{{ chapter.summary }}</p>
        <ol class="philosophy-topics">
          <li v-for="topic in chapter.topics" :key="topic.id"><a :href="studyLink(`/triet-hoc-mac-lenin/bai-giang/${chapter.slug}/${topic.slug}`)">{{ topic.title }}</a></li>
        </ol>
        <a class="philosophy-read" :href="studyLink(`/triet-hoc-mac-lenin/bai-giang/${chapter.slug}`)">Đọc chương {{ chapter.number }} <span aria-hidden="true">→</span></a>
      </div>
    </section>
  </main>
</template>

<style scoped>
.philosophy-course { max-width: 960px; }
.philosophy-course h1 { font-family: var(--font-read); font-size: clamp(30px, 4vw, 46px); line-height: 1.25; margin: var(--space-3) 0 var(--space-5); text-wrap: balance; }
.philosophy-eyebrow { color: var(--ink-3); font: 500 var(--fs-meta)/1.7 var(--font-ui); letter-spacing: .08em; margin: var(--space-4) 0 var(--space-2); }
.philosophy-lead { max-width: 680px; font: var(--fs-h3)/1.75 var(--font-read); color: var(--ink-2); }
.philosophy-chapter { display: grid; grid-template-columns: 72px minmax(0, 1fr); gap: var(--space-5); padding: var(--space-6) 0 var(--space-7); border-bottom: 1px solid var(--rule); }
.philosophy-chapter-number { font: 48px/1.3 var(--font-read); color: var(--tim); padding-top: var(--space-4); }
.philosophy-chapter h2 { font: 600 var(--fs-h2)/1.4 var(--font-read); margin: 0 0 var(--space-4); text-wrap: balance; }
.philosophy-chapter-body > p:not(.philosophy-eyebrow) { color: var(--ink-2); line-height: 1.8; }
.philosophy-topics { list-style: decimal; padding-left: 22px; margin: var(--space-5) 0; color: var(--ink-3); }
.philosophy-topics a { display: inline-flex; align-items: center; min-height: 44px; color: var(--ink); font-size: var(--fs-ui); line-height: 1.6; padding: var(--space-2) 0; }
.philosophy-course a:hover { color: var(--tim); text-decoration: underline; text-underline-offset: 4px; }
.philosophy-course a:focus-visible { outline: 2px solid var(--tim); outline-offset: 4px; }
.philosophy-read { display: inline-flex; align-items: center; min-height: 44px; gap: var(--space-3); color: var(--tim); font-size: var(--fs-ui); font-weight: 600; }
@media (max-width: 600px) { .philosophy-chapter { grid-template-columns: minmax(0, 1fr); gap: 0; padding: var(--space-5) 0; } .philosophy-chapter-number { display: none; } }
</style>
