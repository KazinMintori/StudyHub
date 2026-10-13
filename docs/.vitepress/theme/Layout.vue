<script setup>
import DefaultTheme, { useSidebar } from 'vitepress/theme-without-fonts'
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
import ReadingScrollOffset from './ReadingScrollOffset.vue'
import { useData, useRoute, withBase } from 'vitepress'
import { computed, onMounted, onUnmounted, watch, ref, nextTick } from 'vue'
import { courseCatalog } from '../course-catalog.mjs'
import { lecturePart, syncLecturePart } from './lecture-state'

const { Layout } = DefaultTheme
const welcomeScreen = ref(null)
const { hasSidebar } = useSidebar()
// Keep the desktop preference across courses, independently of the mobile drawer.
const desktopSidebarCollapsed = ref(false)
const { frontmatter, page } = useData(), route = useRoute()
const hasCourseSidebar = computed(() => hasSidebar.value && courseCatalog.some(course => page.value.relativePath.startsWith(`${course.id}/`)))
let sidebarBreakpoint
let navigationBreakpoint
function syncResponsiveNavigation() {
  if (sidebarBreakpoint?.matches && document.querySelector('.VPSidebar.open')) {
    const restoreFocus = desktopSidebarCollapsed.value && document.querySelector('.VPSidebar')?.contains(document.activeElement)
    // Close the actual DefaultTheme drawer so its modal state and scroll lock
    // are cleared. useSidebar() instances do not share their isOpen ref.
    document.querySelector('.Layout > .VPBackdrop.backdrop')?.click()
    if (restoreFocus) nextTick(() => document.querySelector('.course-sidebar-toggle')?.focus({ preventScroll: true }))
  }
  if (navigationBreakpoint?.matches) document.querySelector('.VPNavBarHamburger[aria-expanded="true"]')?.click()
}
function openSearch() { document.querySelector('.DocSearch-Button')?.click() }
function syncLink(event) {
  if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return
  const anchor = event.target.closest?.('a[href]'); if (!anchor) return
  const url = new URL(anchor.href, window.location.href)
  if (url.origin === window.location.origin && url.pathname === window.location.pathname && ['#slides', '#notes', '#cheatsheet', '#kien-thuc-can-co', '#bai-tap'].includes(url.hash)) {
    lecturePart.value = url.hash.slice(1)
  }
}
onMounted(() => {
  syncLecturePart()
  sidebarBreakpoint = window.matchMedia('(min-width: 960px)')
  navigationBreakpoint = window.matchMedia('(min-width: 1200px)')
  sidebarBreakpoint.addEventListener('change', syncResponsiveNavigation)
  navigationBreakpoint.addEventListener('change', syncResponsiveNavigation)
  window.addEventListener('hashchange', syncLecturePart)
  window.addEventListener('popstate', syncLecturePart)
  document.addEventListener('click', syncLink, true)
})
onUnmounted(() => {
  sidebarBreakpoint?.removeEventListener('change', syncResponsiveNavigation)
  navigationBreakpoint?.removeEventListener('change', syncResponsiveNavigation)
  window.removeEventListener('hashchange', syncLecturePart)
  window.removeEventListener('popstate', syncLecturePart)
  document.removeEventListener('click', syncLink, true)
})
watch(() => route.path, syncLecturePart)
</script>

<template>
  <Layout :class="{ 'sidebar-collapsed': hasCourseSidebar && desktopSidebarCollapsed, 'lecture-layout': frontmatter.section === 'lecture' || frontmatter.section === 'topic', 'topic-layout': frontmatter.section === 'topic', 'physics-layout': ['vat-ly-1', 'vat-ly-2'].includes(frontmatter.course), 'lecture-reading-plain': frontmatter.section === 'lecture' && frontmatter.readingStyle === 'plain', 'lecture-slides-layout': frontmatter.section === 'lecture' && lecturePart === 'slides', 'lecture-alt': frontmatter.section === 'lecture' && lecturePart !== 'notes', 'has-chapter-exercises': frontmatter.hasChapterExercises, 'lecture-exercises-layout': frontmatter.hasChapterExercises && lecturePart === 'bai-tap' }">
    <template #layout-top><ReadingScrollOffset /></template>
    <template #nav-bar-content-before>
      <button
        v-if="hasCourseSidebar"
        class="course-sidebar-toggle"
        type="button"
        aria-controls="VPSidebarNav"
        :aria-expanded="!desktopSidebarCollapsed"
        :aria-label="desktopSidebarCollapsed ? 'Mở danh sách bài giảng' : 'Thu danh sách bài giảng'"
        :title="desktopSidebarCollapsed ? 'Mở danh sách bài giảng' : 'Thu danh sách bài giảng'"
        @click="desktopSidebarCollapsed = !desktopSidebarCollapsed"
      >
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" /></svg>
      </button>
    </template>
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
