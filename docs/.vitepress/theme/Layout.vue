<script setup>
import DefaultTheme from 'vitepress/theme-without-fonts'
import DiagramLightbox from './DiagramLightbox.vue'
import LessonActions from './LessonActions.vue'
import CourseNav from './CourseNav.vue'
import TermPreview from './TermPreview.vue'
import LectureHeader from './LectureHeader.vue'
import LecturePanels from './LecturePanels.vue'
import TopicHeader from './TopicHeader.vue'
import TopicNav from './TopicNav.vue'
import WikiFooter from './WikiFooter.vue'
import BuyMeCoffee from './BuyMeCoffee.vue'
import WelcomeScreen from './WelcomeScreen.vue'
import SiteIntroduction from './SiteIntroduction.vue'
import { useData, useRoute, withBase } from 'vitepress'
import { onMounted, onUnmounted, watch, ref, nextTick } from 'vue'
import { lecturePart, syncLecturePart } from './lecture-state'

const { Layout } = DefaultTheme
const welcomeScreen = ref(null)
const { frontmatter } = useData(), route = useRoute()
function openSearch() { document.querySelector('.DocSearch-Button')?.click() }
function syncLink(event) {
  if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return
  const anchor = event.target.closest?.('a[href]'); if (!anchor) return
  const url = new URL(anchor.href, window.location.href)
  if (url.origin === window.location.origin && url.pathname === window.location.pathname && ['#slides', '#notes', '#cheatsheet', '#kien-thuc-can-co', '#bai-tap'].includes(url.hash)) {
    lecturePart.value = url.hash.slice(1)
  }
}
function scrollToExerciseIfActive() {
  if (lecturePart.value === 'bai-tap') {
    nextTick(() => {
      const el = document.getElementById('bai-tap') || document.querySelector('.main > .vp-doc h2:last-of-type')
      if (el) el.scrollIntoView({ behavior: 'smooth' })
    })
  }
}
onMounted(() => {
  syncLecturePart()
  window.addEventListener('hashchange', () => { syncLecturePart(); scrollToExerciseIfActive() })
  window.addEventListener('popstate', syncLecturePart)
  document.addEventListener('click', syncLink, true)
  scrollToExerciseIfActive()
})
onUnmounted(() => {
  window.removeEventListener('hashchange', syncLecturePart)
  window.removeEventListener('popstate', syncLecturePart)
  document.removeEventListener('click', syncLink, true)
})
watch(() => route.path, () => { syncLecturePart(); scrollToExerciseIfActive() })
watch(() => lecturePart.value, (newVal) => { if (newVal === 'bai-tap') scrollToExerciseIfActive() })
</script>

<template>
  <Layout :class="{ 'lecture-layout': frontmatter.section === 'lecture' || frontmatter.section === 'topic', 'topic-layout': frontmatter.section === 'topic', 'lecture-reading-plain': frontmatter.section === 'lecture' && frontmatter.readingStyle === 'plain', 'lecture-slides-layout': frontmatter.section === 'lecture' && lecturePart === 'slides', 'lecture-alt': frontmatter.section === 'lecture' && !['notes', 'bai-tap'].includes(lecturePart) }">
    <template #not-found><main class="course-shell"><h1>Trang này không tồn tại</h1><p>Tìm bài giảng hoặc thuật ngữ để tiếp tục học.</p><div class="button-row"><button class="study-button primary" @click="openSearch">Tìm bài, thuật ngữ</button><a class="text-link" :href="withBase('/')">Danh sách học phần</a></div></main></template>
    <template #doc-before>
      <LectureHeader v-if="frontmatter.section === 'lecture'" />
      <TopicHeader v-else-if="frontmatter.section === 'topic'" />
      <CourseNav v-else />
      <LecturePanels v-if="frontmatter.section === 'lecture'" />
    </template>
    <template #doc-after><LessonActions v-if="frontmatter.section === 'lecture'" /><TopicNav v-if="frontmatter.section === 'topic'" /><WikiFooter v-if="frontmatter.wikiTerm" /></template>
    <template #layout-bottom>
      <DiagramLightbox />
      <TermPreview />
      <SiteIntroduction @show-introduction="welcomeScreen?.show()" />
      <WelcomeScreen ref="welcomeScreen" />
      <BuyMeCoffee />
    </template>
  </Layout>
</template>
