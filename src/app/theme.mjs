import DefaultTheme from 'vitepress/theme-without-fonts'
import { defineAsyncComponent } from 'vue'
import Layout from './StudyLayout.vue'
import './styles/index.css'
import './styles/philosophy.css'
import CourseOverview from '../features/course/components/CourseOverview.vue'
import OldCourseLink from '../features/legacy/components/OldCourseLink.vue'
import CodeIllustration from '../features/illustrations/components/CodeIllustration.vue'
import WikiIndex from '../features/wiki/components/WikiIndex.vue'
import LegacyCourseRoute from '../features/legacy/components/LegacyCourseRoute.vue'
import WikiUsage from '../features/wiki/components/WikiUsage.vue'
import TopicMap from '../features/lecture/components/TopicMap.vue'
import PhilosophyTopic from '../features/philosophy/components/PhilosophyTopic.vue'
import DataDiagram from '../features/illustrations/components/DataDiagram.vue'
import NotebookExecution from '../features/illustrations/components/NotebookExecution.vue'

// Mọi mô phỏng tương tác đặt tên dạng <Tên>Lab.vue được đăng ký toàn cục theo đúng tên file,
// nên Notes có thể viết <AffineLab type="line" /> mà không cần import.
const labs = import.meta.glob('../features/labs/components/*Lab.vue')

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app, router }) {
    for (const [name, component] of Object.entries({ CourseOverview, OldCourseLink, CodeIllustration, WikiIndex, LegacyCourseRoute, WikiUsage, TopicMap, PhilosophyTopic, DataDiagram, NotebookExecution })) app.component(name, component)
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
