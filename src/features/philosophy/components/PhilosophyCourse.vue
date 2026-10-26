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
    <a class="text-link" :href="studyLink('/goc-hoc-tap?mon=triet-hoc-mac-lenin')">Góc học tập của môn <span aria-hidden="true">→</span></a>
    <section v-for="chapter in course.lessons" :key="chapter.slug" class="philosophy-chapter" :aria-labelledby="`philosophy-chapter-${chapter.number}`">
      <div class="philosophy-chapter-number" aria-hidden="true">0{{ chapter.number }}</div>
      <div class="philosophy-chapter-body">
        <p class="philosophy-eyebrow">Chương {{ chapter.number }}</p>
        <h2 :id="`philosophy-chapter-${chapter.number}`"><a :href="studyLink(`/triet-hoc-mac-lenin/bai-giang/${chapter.slug}`)">{{ chapter.title }}</a></h2>
        <p>{{ chapter.summary }}</p>
        <ol class="philosophy-topics" role="list">
          <li v-for="(topic, index) in chapter.topics" :key="topic.id">
            <a class="philosophy-topic-link" :href="studyLink(`/triet-hoc-mac-lenin/bai-giang/${chapter.slug}/${topic.slug}`)">
              <span class="philosophy-topic-number" aria-hidden="true">{{ index + 1 }}</span>
              <span class="philosophy-topic-title">{{ topic.title }}</span>
              <svg class="philosophy-topic-arrow" viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M4 10h12m-5-5 5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /></svg>
            </a>
          </li>
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
.philosophy-chapter { display: grid; grid-template-columns: 56px minmax(0, 1fr); gap: var(--space-5); margin-top: var(--space-5); padding: var(--space-6); border: 1px solid var(--rule); border-radius: var(--radius-xl); background: var(--paper); }
.philosophy-chapter-number { font: 48px/1.3 var(--font-read); color: var(--tim); }
.philosophy-chapter-body { min-width: 0; }
.philosophy-chapter-body > .philosophy-eyebrow { margin-top: 0; }
.philosophy-chapter h2 { font: 600 var(--fs-h2)/1.4 var(--font-read); margin: 0 0 var(--space-4); text-wrap: balance; }
.philosophy-chapter-body > p:not(.philosophy-eyebrow) { color: var(--ink-2); line-height: 1.8; }
.philosophy-topics { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: var(--space-3); list-style: none; padding: 0; margin: var(--space-5) 0; }
.philosophy-topics li { display: flex; min-width: 0; }
.philosophy-topic-link { display: grid; grid-template-columns: 32px minmax(0, 1fr) 18px; align-items: center; gap: var(--space-3); width: 100%; min-height: 88px; padding: var(--space-4); border: 1px solid var(--rule); border-radius: var(--radius-lg); background: var(--canvas); color: var(--ink); text-decoration: none; transition: border-color var(--motion-fast) var(--ease), background var(--motion-fast) var(--ease); }
.philosophy-topic-number { display: grid; place-items: center; width: 32px; height: 32px; border-radius: var(--radius); background: var(--tim-soft); color: var(--tim); font-size: var(--fs-small); font-weight: 600; font-variant-numeric: tabular-nums; }
.philosophy-topic-title { font-size: var(--fs-ui); font-weight: 500; line-height: 1.65; overflow-wrap: anywhere; }
.philosophy-topic-arrow { color: var(--tim); }
.philosophy-course a:hover { color: var(--tim); text-decoration: underline; text-underline-offset: 4px; }
.philosophy-course .philosophy-topic-link:hover { border-color: var(--tim); background: var(--tim-soft); text-decoration: none; }
.philosophy-course a:focus-visible { outline: 2px solid var(--tim); outline-offset: 4px; }
.philosophy-read { display: inline-flex; align-items: center; min-height: 44px; gap: var(--space-3); color: var(--tim); font-size: var(--fs-ui); font-weight: 600; }
@media (max-width: 600px) {
  .philosophy-chapter { grid-template-columns: minmax(0, 1fr); gap: 0; padding: var(--space-4); }
  .philosophy-chapter-number { display: none; }
  .philosophy-topic-link { min-height: 76px; padding: var(--space-3); gap: var(--space-2); }
}
</style>
