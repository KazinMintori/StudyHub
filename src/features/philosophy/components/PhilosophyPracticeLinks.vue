<script setup>
import { computed } from 'vue'
import { studyLink } from '../../../core/routing/links.js'
import { chapterPracticeTests } from '../services/practice-tests.mjs'
import catalog from '../../../content/courses/triet-hoc-mac-lenin/exam/catalog.json'
const props = defineProps({ chapterId: { type: String, required: true }, testNumber: { type: Number, required: true } })
const tests = computed(() => chapterPracticeTests(catalog.banks.find(bank => bank.id === props.chapterId)))
const next = computed(() => tests.value.find(test => test.testNumber === props.testNumber + 1))
</script>

<template>
  <nav class="practice-test-links" aria-label="Chuyển bài kiểm tra">
    <a :href="studyLink(`/triet-hoc-mac-lenin/on-thi/${chapterId}`)">← Danh sách bài</a>
    <a v-if="next" :href="studyLink(next.path)">{{ next.title }} →</a>
    <a v-else :href="studyLink('/triet-hoc-mac-lenin/on-thi/')">Chọn chương →</a>
  </nav>
</template>

<style scoped>
.practice-test-links { display: flex; justify-content: space-between; flex-wrap: wrap; gap: var(--space-3); margin-top: var(--space-7); padding-top: var(--space-5); border-top: 1px solid var(--rule); font: var(--fs-ui)/1.7 var(--font-ui); }
a { display: inline-flex; align-items: center; min-height: 44px; color: var(--tim); }
a:hover { text-decoration: underline; text-underline-offset: 4px; }
a:focus-visible { outline: 2px solid var(--tim); outline-offset: 4px; }
</style>
