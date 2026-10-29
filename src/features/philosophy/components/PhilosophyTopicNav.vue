<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../../../content/catalog.mjs'
import { studyLink } from '../../../core/routing/links.js'
import { lecturePart, selectLecturePart } from '../../navigation/controllers/use-lecture-navigation.mjs'
import { shouldIgnoreNavigationClick } from '../../navigation/services/tab-service.mjs'
const { frontmatter } = useData()
const course = computed(() => findCourse(frontmatter.value.course))
const chapter = computed(() => course.value?.lessons.find(item => item.slug === frontmatter.value.lecture))
const topics = computed(() => chapter.value?.topics || [])
const index = computed(() => topics.value.findIndex(item => item.slug === frontmatter.value.topic))
const previous = computed(() => topics.value[index.value - 1])
const next = computed(() => topics.value[index.value + 1])
const nextChapter = computed(() => course.value?.lessons[course.value.lessons.indexOf(chapter.value) + 1])
const path = topic => studyLink(`/triet-hoc-mac-lenin/bai-giang/${chapter.value.slug}/${topic.slug}`)
function practice(event) {
  if (shouldIgnoreNavigationClick(event)) return
  event.preventDefault()
  return selectLecturePart('bai-tap')
}
</script>

<template>
  <div v-if="chapter && index >= 0" class="philosophy-topic-footer">
  <a v-if="lecturePart !== 'bai-tap'" class="philosophy-topic-practice vp-raw" href="#bai-tap" @click="practice">Làm bài tập của chủ đề <span aria-hidden="true">→</span></a>
  <nav class="philosophy-topic-nav" aria-label="Chuyển chủ đề">
    <a v-if="previous" :href="path(previous)"><span>← Chủ đề trước</span><strong>{{ previous.title }}</strong></a>
    <a v-else :href="studyLink(`/triet-hoc-mac-lenin/bai-giang/${chapter.slug}`)"><span>← Mục lục chương</span><strong>{{ chapter.title }}</strong></a>
    <a v-if="next" :href="path(next)"><span>Chủ đề tiếp theo →</span><strong>{{ next.title }}</strong></a>
    <a v-else-if="nextChapter" :href="studyLink(`/triet-hoc-mac-lenin/bai-giang/${nextChapter.slug}`)"><span>Chương tiếp theo →</span><strong>{{ nextChapter.title }}</strong></a>
    <a v-else :href="studyLink('/triet-hoc-mac-lenin/on-thi/')"><span>Ôn thi →</span><strong>Kiểm tra kiến thức theo chương</strong></a>
  </nav>
  </div>
</template>

<style scoped>
.philosophy-topic-nav { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-5); margin-top: var(--space-7); padding-top: var(--space-5); border-top: 1px solid var(--rule); font-family: var(--font-ui); }
.philosophy-topic-practice { display: inline-flex; align-items: center; flex-direction: row; gap: var(--space-4); margin-top: var(--space-6); color: var(--tim); font-family: var(--font-ui); min-height: 48px; padding: var(--space-3) var(--space-4); }
a { display: flex; flex-direction: column; gap: var(--space-2); min-height: 60px; padding: var(--space-3); border: 1px solid var(--rule); border-radius: var(--radius); }
a:last-child { text-align: right; }
span { color: var(--ink-3); font-size: var(--fs-small); }
strong { color: var(--tim); font-size: var(--fs-ui); line-height: 1.6; }
a:hover { background: var(--canvas); border-color: var(--tim); }
a:focus-visible { outline: 2px solid var(--tim); outline-offset: 3px; }
@media (max-width: 600px) { .philosophy-topic-nav { grid-template-columns: 1fr; } a:last-child { text-align: left; } }
</style>
