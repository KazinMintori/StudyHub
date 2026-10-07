import DefaultTheme from 'vitepress/theme-without-fonts'
import Layout from './Layout.vue'
import './custom.css'
import CourseOverview from './CourseOverview.vue'
import OldCourseLink from './OldCourseLink.vue'
import CodeIllustration from './CodeIllustration.vue'
import WikiIndex from './WikiIndex.vue'
import LegacyCourseRoute from './LegacyCourseRoute.vue'
import MathLab from './MathLab.vue'
import WikiUsage from './WikiUsage.vue'

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app }) {
    for (const [name, component] of Object.entries({ CourseOverview, OldCourseLink, CodeIllustration, WikiIndex, LegacyCourseRoute, MathLab, WikiUsage })) app.component(name, component)
  }
}
