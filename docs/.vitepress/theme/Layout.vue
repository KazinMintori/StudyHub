<script setup>
import DefaultTheme from 'vitepress/theme'
import DiagramLightbox from './DiagramLightbox.vue'
import LessonActions from './LessonActions.vue'
import CourseNav from './CourseNav.vue'
import TermPreview from './TermPreview.vue'
import LectureHeader from './LectureHeader.vue'
import LecturePanels from './LecturePanels.vue'
import WikiFooter from './WikiFooter.vue'
import { useData, useRoute } from 'vitepress'
import { onMounted, onUnmounted, watch } from 'vue'
import { lecturePart, syncLecturePart } from './lecture-state'

const { Layout } = DefaultTheme
const { frontmatter }=useData(), route=useRoute()
function syncLink(event) {
  if(event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return
  const anchor=event.target.closest?.('a[href]');if(!anchor)return
  const url=new URL(anchor.href,window.location.href)
  if(url.origin===window.location.origin && url.pathname===window.location.pathname && ['#slides','#notes','#kien-thuc-can-co'].includes(url.hash))lecturePart.value=url.hash.slice(1)
}
onMounted(()=>{syncLecturePart();window.addEventListener('hashchange',syncLecturePart);window.addEventListener('popstate',syncLecturePart);document.addEventListener('click',syncLink,true)})
onUnmounted(()=>{window.removeEventListener('hashchange',syncLecturePart);window.removeEventListener('popstate',syncLecturePart);document.removeEventListener('click',syncLink,true)})
watch(()=>route.path,()=>syncLecturePart())
</script>

<template>
  <Layout :class="{ 'lecture-layout': frontmatter.section==='lecture', 'lecture-alt': frontmatter.section==='lecture' && lecturePart!=='notes' }">
    <template #doc-before>
      <LectureHeader v-if="frontmatter.section==='lecture'" />
      <CourseNav v-else />
      <LessonActions />
      <LecturePanels v-if="frontmatter.section==='lecture'" />
    </template>
    <template #doc-after><WikiFooter v-if="frontmatter.wikiTerm" /></template>
    <template #layout-bottom>
      <DiagramLightbox />
      <TermPreview />
    </template>
  </Layout>
</template>
