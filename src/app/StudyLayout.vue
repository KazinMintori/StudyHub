<script setup>
import DefaultTheme, { useSidebar } from 'vitepress/theme-without-fonts'
import DiagramLightbox from '../core/diagrams/components/DiagramLightbox.vue'
import LessonActions from '../features/study-progress/components/LessonActions.vue'
import CourseNav from '../features/course/components/CourseNav.vue'
import TermPreview from '../features/wiki/components/TermPreview.vue'
import LectureHeader from '../features/lecture/components/LectureHeader.vue'
import LecturePanels from '../features/lecture/components/LecturePanels.vue'
import PhilosophyHeader from '../features/philosophy/components/PhilosophyHeader.vue'
import PhilosophyTopicNav from '../features/philosophy/components/PhilosophyTopicNav.vue'
import TopicHeader from '../features/lecture/components/TopicHeader.vue'
import TopicNav from '../features/lecture/components/TopicNav.vue'
import WikiFooter from '../features/wiki/components/WikiFooter.vue'
import BuyMeCoffee from '../features/site/components/BuyMeCoffee.vue'
import WelcomeScreen from '../features/site/components/WelcomeScreen.vue'
import SiteIntroduction from '../features/site/components/SiteIntroduction.vue'
import ReadingScrollOffset from '../features/navigation/components/ReadingScrollOffset.vue'
import { useData, withBase } from 'vitepress'
import { computed, ref } from 'vue'
import { courseCatalog } from '../content/catalog.mjs'
import {
  useResponsiveSidebar,
  useLectureNavigation,
  resolveHasCourseSidebar,
  resolveLayoutClasses,
  openSearch
} from '../features/navigation/index.mjs'

const { Layout } = DefaultTheme
const welcomeScreen = ref(null)
const { hasSidebar } = useSidebar()
const { frontmatter, page } = useData()
const isPhilosophy = computed(() => frontmatter.value.course === 'triet-hoc-mac-lenin')

const {
  desktopSidebarCollapsed,
  toggleDesktopSidebar
} = useResponsiveSidebar()

const { lecturePart } = useLectureNavigation()

const hasCourseSidebar = computed(() =>
  resolveHasCourseSidebar(hasSidebar.value, page.value?.relativePath, courseCatalog)
)

const layoutClasses = computed(() => ({
  ...resolveLayoutClasses({
    frontmatter: frontmatter.value,
    hasCourseSidebar: hasCourseSidebar.value,
    desktopSidebarCollapsed: desktopSidebarCollapsed.value,
    lecturePart: isPhilosophy.value ? 'notes' : lecturePart.value
  }),
  'philosophy-layout': isPhilosophy.value,
  'philosophy-exercise-view': isPhilosophy.value && frontmatter.value.section === 'topic' && lecturePart.value === 'bai-tap'
}))
</script>

<template>
  <Layout :class="layoutClasses">
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
        @click="toggleDesktopSidebar"
      >
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" /></svg>
      </button>
    </template>
    <template #not-found><main class="course-shell"><h1>Trang này không tồn tại</h1><p>Tìm bài giảng hoặc thuật ngữ để tiếp tục học.</p><div class="button-row"><button class="study-button primary" @click="openSearch">Tìm bài, thuật ngữ</button><a class="text-link" :href="withBase('/')">Danh sách học phần</a></div></main></template>
    <template #doc-before>
      <PhilosophyHeader v-if="isPhilosophy" />
      <LectureHeader v-else-if="frontmatter.section === 'lecture'" />
      <TopicHeader v-else-if="frontmatter.section === 'topic'" />
      <CourseNav v-else />
      <LecturePanels v-if="frontmatter.section === 'lecture' && !isPhilosophy" />
    </template>
    <template #doc-after><LessonActions v-if="frontmatter.section === 'lecture' && !isPhilosophy" /><PhilosophyTopicNav v-if="frontmatter.section === 'topic' && isPhilosophy" /><TopicNav v-else-if="frontmatter.section === 'topic'" /><WikiFooter v-if="frontmatter.wikiTerm" /></template>
    <template #layout-bottom>
      <DiagramLightbox />
      <TermPreview />
      <SiteIntroduction @show-introduction="welcomeScreen?.show()" />
      <WelcomeScreen ref="welcomeScreen" />
      <BuyMeCoffee />
    </template>
  </Layout>
</template>
