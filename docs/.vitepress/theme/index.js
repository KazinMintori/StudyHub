import DefaultTheme from 'vitepress/theme-without-fonts'
import Layout from './Layout.vue'
import './custom.css'
import CourseOverview from './CourseOverview.vue'
import OldCourseLink from './OldCourseLink.vue'
import CodeIllustration from './CodeIllustration.vue'
import WikiIndex from './WikiIndex.vue'
import LegacyCourseRoute from './LegacyCourseRoute.vue'
import WikiUsage from './WikiUsage.vue'
import TopicMap from './TopicMap.vue'
import DataDiagram from './DataDiagram.vue'
import NotebookExecution from './NotebookExecution.vue'

// Mọi mô phỏng tương tác đặt tên dạng <Tên>Lab.vue được đăng ký toàn cục theo đúng tên file,
// nên Notes có thể viết <AffineLab type="line" /> mà không cần import.
const labs = import.meta.glob('./*Lab.vue', { eager: true })

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app }) {
    for (const [name, component] of Object.entries({ CourseOverview, OldCourseLink, CodeIllustration, WikiIndex, LegacyCourseRoute, WikiUsage, TopicMap, DataDiagram, NotebookExecution })) app.component(name, component)
    for (const [file, module] of Object.entries(labs)) app.component(file.replace(/^\.\/|\.vue$/g, ''), module.default)
  }
}
