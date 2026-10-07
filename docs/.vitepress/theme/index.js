import DefaultTheme from 'vitepress/theme'
import Layout from './Layout.vue'
import './custom.css'
import CourseOverview from './CourseOverview.vue'
import OldCourseLink from './OldCourseLink.vue'
import CodeIllustration from './CodeIllustration.vue'
import WikiIndex from './WikiIndex.vue'
import LegacyCourseRoute from './LegacyCourseRoute.vue'

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app }) {
    for (const [name, component] of Object.entries({ CourseOverview, OldCourseLink, CodeIllustration, WikiIndex, LegacyCourseRoute })) app.component(name, component)
  }
}
