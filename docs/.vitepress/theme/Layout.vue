<script setup>
import DefaultTheme from 'vitepress/theme-without-fonts'
import DiagramLightbox from './DiagramLightbox.vue'
import LessonActions from './LessonActions.vue'
import CourseNav from './CourseNav.vue'
import TermPreview from './TermPreview.vue'
import LectureHeader from './LectureHeader.vue'
import LecturePanels from './LecturePanels.vue'
import WikiFooter from './WikiFooter.vue'
import BuyMeCoffee from './BuyMeCoffee.vue'
import WelcomeScreen from './WelcomeScreen.vue'
import SiteIntroduction from './SiteIntroduction.vue'
import { useData, useRoute, withBase } from 'vitepress'
import { onMounted, onUnmounted, watch, ref } from 'vue'
import { lecturePart, syncLecturePart } from './lecture-state'

const { Layout } = DefaultTheme
const welcomeScreen = ref(null)
const { frontmatter }=useData(), route=useRoute()
function openSearch() { document.querySelector('.DocSearch-Button')?.click() }
function syncLink(event) {
  if(event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return
  const anchor=event.target.closest?.('a[href]');if(!anchor)return
  const url=new URL(anchor.href,window.location.href)
  if(url.origin===window.location.origin && url.pathname===window.location.pathname && ['#slides','#notes','#kien-thuc-can-co','#bai-tap'].includes(url.hash))lecturePart.value=url.hash==='#bai-tap'?'notes':url.hash.slice(1)
}
onMounted(()=>{syncLecturePart();window.addEventListener('hashchange',syncLecturePart);window.addEventListener('popstate',syncLecturePart);document.addEventListener('click',syncLink,true)})
onUnmounted(()=>{window.removeEventListener('hashchange',syncLecturePart);window.removeEventListener('popstate',syncLecturePart);document.removeEventListener('click',syncLink,true)})
watch(()=>route.path,()=>syncLecturePart())
</script>

<template>
  <Layout :class="{ 'lecture-layout': frontmatter.section==='lecture', 'lecture-slides-layout': frontmatter.section==='lecture' && lecturePart==='slides', 'lecture-alt': frontmatter.section==='lecture' && lecturePart!=='notes' }">
    <template #not-found><main class="course-shell"><h1>Trang này không tồn tại</h1><p>Tìm bài giảng hoặc thuật ngữ để tiếp tục học.</p><div class="button-row"><button class="study-button primary" @click="openSearch">Tìm bài, thuật ngữ</button><a class="text-link" :href="withBase('/')">Danh sách học phần</a></div></main></template>
    <template #doc-before>
      <LectureHeader v-if="frontmatter.section==='lecture'" />
      <CourseNav v-else />
      <LecturePanels v-if="frontmatter.section==='lecture'" />
    </template>
    <template #doc-after><LessonActions v-if="frontmatter.section==='lecture'" /><WikiFooter v-if="frontmatter.wikiTerm" /></template>
    <template #layout-bottom>
      <DiagramLightbox />
      <TermPreview />
      <SiteIntroduction @show-introduction="welcomeScreen?.show()" />
      <WelcomeScreen ref="welcomeScreen" />
      <BuyMeCoffee />
    </template>
  </Layout>
</template>
