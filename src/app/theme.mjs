import DefaultTheme from 'vitepress/theme-without-fonts'
import { defineAsyncComponent } from 'vue'
import Layout from './StudyLayout.vue'
import './styles/index.css'
import './styles/philosophy.css'
// Components used inside Markdown pages are split into their own chunks.
// Wiki components read the full concept dictionary, so loading them only on
// the pages that use them keeps that data out of every other page.
const pageComponents = {
  CourseOverview: () => import('../features/course/components/CourseOverview.vue'),
  OldCourseLink: () => import('../features/legacy/components/OldCourseLink.vue'),
  CodeIllustration: () => import('../features/illustrations/components/CodeIllustration.vue'),
  WikiIndex: () => import('../features/wiki/components/WikiIndex.vue'),
  LegacyCourseRoute: () => import('../features/legacy/components/LegacyCourseRoute.vue'),
  WikiUsage: () => import('../features/wiki/components/WikiUsage.vue'),
  TopicMap: () => import('../features/lecture/components/TopicMap.vue'),
  ChapterExercises: () => import('../features/lecture/components/ChapterExercises.vue'),
  PhilosophyTopic: () => import('../features/philosophy/components/PhilosophyTopic.vue'),
  DataDiagram: () => import('../features/illustrations/components/DataDiagram.vue'),
  NotebookExecution: () => import('../features/illustrations/components/NotebookExecution.vue')
}

// Mọi mô phỏng tương tác đặt tên dạng <Tên>Lab.vue được đăng ký toàn cục theo đúng tên file,
// nên Notes có thể viết <AffineLab type="line" /> mà không cần import.
const labs = import.meta.glob('../features/labs/components/*Lab.vue')

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app, router }) {
    for (const [name, load] of Object.entries(pageComponents)) app.component(name, defineAsyncComponent(load))
    for (const [file, load] of Object.entries(labs)) app.component(file.split('/').at(-1).replace(/\.vue$/, ''), defineAsyncComponent(load))

    if (typeof window !== 'undefined' && router) {
      const normalizePath = (path) => path.replace(/(?:^|\/)index(?:\.html)?$/, '/').replace(/\.html$/, '').replace(/\/+$/, '') || '/'
      const shouldNavigateNatively = (to) => {
        try {
          const target = new URL(to, window.location.href)
          return normalizePath(target.pathname) !== normalizePath(window.location.pathname)
        } catch {
          return false
        }
      }
      router.onBeforeRouteChange = (to) => {
        if (shouldNavigateNatively(to)) {
          const target = new URL(to, window.location.href)
          window.location.href = target.href
          return false
        }
      }
      router.onBeforePageLoad = (to) => {
        if (shouldNavigateNatively(to)) {
          const target = new URL(to, window.location.href)
          window.location.href = target.href
          return false
        }
      }
    }
  }
}
