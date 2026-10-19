<script setup>
import { computed, onMounted } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../../../content/catalog.mjs'
import { studyLink } from '../../../core/routing/links.js'
import PhilosophyNav from './PhilosophyNav.vue'
const { frontmatter } = useData()
const course = computed(() => findCourse(frontmatter.value.course))
const lesson = computed(() => course.value?.lessons.find(item => item.slug === frontmatter.value.lecture))
const topic = computed(() => lesson.value?.topics.find(item => item.slug === frontmatter.value.topic))
const exam = computed(() => frontmatter.value.section === 'exam')
onMounted(() => {
  if (!lesson.value || topic.value || !window.location.hash) return
  let hash
  try { hash = decodeURIComponent(window.location.hash.slice(1)) } catch { return }
  const exercise = hash.endsWith('-bai-tap')
  const oldTopic = lesson.value.topics.find(item => item.id === hash || `${item.id}-bai-tap` === hash)
  if (oldTopic) window.location.replace(studyLink(`/triet-hoc-mac-lenin/bai-giang/${lesson.value.slug}/${oldTopic.slug}`) + (exercise ? '#bai-tap' : ''))
})
</script>

<template>
  <header class="philosophy-header">
    <nav class="book-breadcrumbs" aria-label="Đường dẫn bài đọc"><a :href="studyLink('/triet-hoc-mac-lenin/')">Triết học Mác – Lênin</a><template v-if="topic"><span>/</span><a :href="studyLink(`/triet-hoc-mac-lenin/bai-giang/${lesson.slug}`)">Chương {{ lesson.number }}</a></template><template v-else-if="exam && frontmatter.quiz"><span>/</span><a :href="studyLink('/triet-hoc-mac-lenin/on-thi/')">Ôn thi</a><template v-if="frontmatter.quizTest"><span>/</span><a :href="studyLink(`/triet-hoc-mac-lenin/on-thi/${frontmatter.quiz}`)">Chương {{ frontmatter.quizChapter === 1 ? 'I' : 'II' }}</a></template></template></nav>
    <PhilosophyNav :exam="exam" />
    <p v-if="lesson" class="philosophy-kicker">Chương {{ lesson.number }}<template v-if="topic"> · Chủ đề {{ lesson.topics.indexOf(topic) + 1 }}</template></p>
    <h1 :id="topic?.id">{{ topic?.title || lesson?.title || frontmatter.title || 'Ôn thi' }}</h1>
  </header>
</template>

<style scoped>
.philosophy-header { margin-bottom: var(--space-6); }
.philosophy-kicker { color: var(--tim); font-size: var(--fs-ui); margin-bottom: var(--space-3); }
h1 { font: 600 clamp(28px, 3vw, 38px)/1.35 var(--font-read); letter-spacing: -.02em; text-wrap: balance; }
</style>
