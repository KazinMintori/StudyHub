<script setup>
import { computed } from 'vue'
import { studyLink } from '../../../core/routing/links.js'
import { chapterPracticeTests } from '../services/practice-tests.mjs'
import catalog from '../../../content/courses/triet-hoc-mac-lenin/exam/catalog.json'
const props = defineProps({ chapterId: { type: String, required: true } })
const chapter = computed(() => catalog.banks.find(bank => bank.id === props.chapterId))
const tests = computed(() => chapterPracticeTests(chapter.value))
</script>

<template>
  <section v-if="chapter" class="practice-chapter" aria-label="Chọn bài kiểm tra">
    <p class="practice-description">{{ chapter.count }} câu hỏi được chia thành {{ tests.length }} bài. Chọn một bài để bắt đầu hoặc tiếp tục phần đang làm.</p>
    <ol class="practice-test-list">
      <li v-for="test in tests" :key="test.id">
        <a :href="studyLink(test.path)"><span class="practice-test-number" aria-hidden="true">{{ test.testNumber }}</span><span class="practice-test-copy"><strong>{{ test.title }}</strong><span>{{ test.count }} câu hỏi</span></span><span class="practice-test-arrow" aria-hidden="true">→</span></a>
      </li>
    </ol>
  </section>
</template>

<style scoped>
.practice-description { color: var(--ink-2); line-height: 1.8; margin: 0 0 var(--space-6); }
.practice-test-list { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-4); margin: 0 !important; padding: 0 !important; list-style: none !important; }
.practice-test-list li { margin: 0; min-width: 0; }
.practice-test-list a { display: flex; gap: var(--space-4); align-items: center; min-height: 96px; height: 100%; padding: var(--space-4); border: 1px solid var(--rule); border-radius: var(--radius-lg); text-decoration: none; font-family: var(--font-ui); }
.practice-test-number { display: grid; place-items: center; min-width: 36px; min-height: 36px; border-radius: 50%; background: var(--tim-soft); color: var(--tim); }
.practice-test-copy { display: flex; flex-direction: column; gap: var(--space-2); min-width: 0; font-size: var(--fs-ui); }
.practice-test-copy strong { color: var(--ink); line-height: 1.6; }
.practice-test-copy > span { color: var(--ink-3); font-size: var(--fs-small); }
.practice-test-arrow { margin-left: auto; color: var(--tim); }
.practice-test-list a:hover { border-color: var(--tim); background: var(--canvas); }
.practice-test-list a:focus-visible { outline: 2px solid var(--tim); outline-offset: 4px; }
@media (max-width: 600px) { .practice-test-list { grid-template-columns: 1fr; } }
</style>
