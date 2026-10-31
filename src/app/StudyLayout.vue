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
import BuyMeCoffee from '../features/site/components/BuyMeCoffee.vue'
import FeedbackWidget from '../features/site/components/FeedbackWidget.vue'
import WelcomeScreen from '../features/site/components/WelcomeScreen.vue'
import SiteIntroduction from '../features/site/components/SiteIntroduction.vue'
import SpotArt from '../features/illustrations/components/SpotArt.vue'
import ReadingScrollOffset from '../features/navigation/components/ReadingScrollOffset.vue'
import ReadingOutline from '../features/navigation/components/ReadingOutline.vue'
import ReadingPageControls from '../features/navigation/components/ReadingPageControls.vue'
import SiteSearch from '../features/navigation/components/SiteSearch.vue'
import { provideReadingOutline } from '../features/navigation/controllers/use-reading-outline.mjs'
import ZenModeToggle from '../features/navigation/components/ZenModeToggle.vue'
import StudyUtilityWidget from '../features/study-tools/components/StudyUtilityWidget.vue'
import { useData, withBase } from 'vitepress'
import { computed, defineAsyncComponent, ref } from 'vue'
import { courseCatalog } from '../content/catalog.mjs'
import {
  useResponsiveSidebar,
  useLectureNavigation,
  resolveHasCourseSidebar,
  resolveLayoutClasses
} from '../features/navigation/index.mjs'

const { Layout } = DefaultTheme
// Wiki footers read the concept dictionary; load them only on Wiki pages.
const WikiFooter = defineAsyncComponent(() => import('../features/wiki/components/WikiFooter.vue'))
const welcomeScreen = ref(null)
const { hasSidebar } = useSidebar()
const { frontmatter, page } = useData()
provideReadingOutline(page)
const currentCourse = computed(() => courseCatalog.find(course =>
  course.id === frontmatter.value.course || page.value?.relativePath?.startsWith(`${course.id}/`)
))
const isPhilosophy = computed(() => frontmatter.value.course === 'triet-hoc-mac-lenin')
// XSTK stores the exercise-panel flag in the lesson catalog. Older Notes may
// omit its frontmatter copy, so both the layout and panels use the same value.
const chapterExercises = computed(() => frontmatter.value.course === 'xac-suat-thong-ke'
  ? courseCatalog.find(course => course.id === frontmatter.value.course)?.lessons.find(lesson => lesson.slug === frontmatter.value.lecture)?.hasChapterExercises ?? frontmatter.value.hasChapterExercises
  : frontmatter.value.hasChapterExercises)

const {
  desktopSidebarCollapsed,
  toggleDesktopSidebar
} = useResponsiveSidebar()

const { lecturePart } = useLectureNavigation()

const hasCourseSidebar = computed(() =>
  resolveHasCourseSidebar(hasSidebar.value, page.value?.relativePath, courseCatalog)
)

const layoutClasses = computed(() => ({
  'course-context': Boolean(currentCourse.value),
  'shared-reading-outline': frontmatter.value.section === 'lecture' && !isPhilosophy.value,
  ...resolveLayoutClasses({
    frontmatter: { ...frontmatter.value, hasChapterExercises: chapterExercises.value },
    hasCourseSidebar: hasCourseSidebar.value,
    desktopSidebarCollapsed: desktopSidebarCollapsed.value,
    lecturePart: isPhilosophy.value ? 'notes' : lecturePart.value
  }),
  'xstk-layout': frontmatter.value.course === 'xac-suat-thong-ke',
  'philosophy-layout': isPhilosophy.value && !frontmatter.value.quizTest,
  'philosophy-exercise-view': isPhilosophy.value && frontmatter.value.section === 'topic' && lecturePart.value === 'bai-tap'
}))
</script>

<template>
  <Layout :class="layoutClasses">
    <template #layout-top><ReadingScrollOffset /></template>
    <template #aside-outline-before><ReadingOutline v-if="frontmatter.section === 'lecture' && !isPhilosophy" /></template>
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
      <SiteSearch />
    </template>
    <template #nav-bar-content-after>
      <div v-if="currentCourse" class="nav-extra-tools">
        <StudyUtilityWidget :course-name="currentCourse.name" :course-id="currentCourse.id" />
        <ZenModeToggle />
      </div>
    </template>
    <template #not-found><main class="course-shell not-found-page"><SpotArt name="notfound" tone="tim" /><h1>Trang này không tồn tại</h1><p>Có thể đường dẫn đã đổi hoặc bài chưa được xuất bản. Tra cứu thuật ngữ trong Wiki hoặc chọn học phần để tiếp tục học.</p><div class="button-row"><a class="study-button primary" :href="withBase('/wiki/')">Tra cứu Wiki</a><a class="text-link" :href="withBase('/')">Danh sách học phần</a></div></main></template>
    <template #doc-before>
      <PhilosophyHeader v-if="isPhilosophy" />
      <LectureHeader v-else-if="frontmatter.section === 'lecture'" />
      <TopicHeader v-else-if="frontmatter.section === 'topic'" />
      <CourseNav v-else />
      <LecturePanels v-if="frontmatter.section === 'lecture' && !isPhilosophy" />
    </template>
    <template #doc-after><LessonActions v-if="frontmatter.section === 'lecture'" /><PhilosophyTopicNav v-if="frontmatter.section === 'topic' && isPhilosophy" /><TopicNav v-else-if="frontmatter.section === 'topic'" /><WikiFooter v-if="frontmatter.wikiTerm" /></template>
    <template #layout-bottom>
      <ReadingPageControls v-if="['lecture', 'topic'].includes(frontmatter.section)" />
      <DiagramLightbox />
      <TermPreview />
      <SiteIntroduction @show-introduction="welcomeScreen?.show()" />
      <WelcomeScreen ref="welcomeScreen" />
      <BuyMeCoffee />
      <FeedbackWidget :page-title="frontmatter.title || page.title" :course-name="currentCourse?.name || ''" />
    </template>
  </Layout>
</template>
