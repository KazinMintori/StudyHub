import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import { courseCatalog } from './course-catalog.mjs'
import { wikiGroups } from './wiki-content.mjs'
import { concepts } from './concepts.mjs'
import { termLinks } from './term-links.mjs'
import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { mathTextPlugin } from '../../scripts/math-text-plugin.mjs'

const tokenSource = readFileSync(new URL('./theme/tokens.css', import.meta.url), 'utf8')
const colorToken = name => tokenSource.match(new RegExp(`--${name}:\\s*([^;]+)`))[1].trim()

const base=process.env.BASE_PATH || (process.env.GITHUB_ACTIONS ? `/${process.env.GITHUB_REPOSITORY?.split('/')[1] || 'StudyHub'}/` : '/')
export default withMermaid(defineConfig({
  buildConcurrency: 2,
  base, title:'UETệ', description:'Bài giảng UET và Wiki thuật ngữ', lang:'vi-VN',
  ignoreDeadLinks: true, lastUpdated: true,
  head:[
    ['link',{rel:'icon',href:`${base}favicon.svg`}],
    ['link',{rel:'icon',type:'image/png',href:`${base}favicon.png`}],
    ['meta',{name:'theme-color',content:colorToken('paper')}]
  ],
  markdown:{
    math:true,
    lineNumbers:false,
    config:md=>{
      md.core.ruler.before('block', 'normalize_custom_containers', state => {
        state.src = state.src
          .replace(/^## Tự kiểm tra$/gm, '## Câu hỏi ôn lại')
          // A container title ends on the same line; never consume the next paragraph.
          .replace(/^::: example(?:[\t ]+(.*))?$/gm, (_, title) => `::: info Ví dụ${title ? `: ${title}` : ''}`)
          .replace(/^::: proof(?:[\t ]+(.*))?$/gm, (_, title) => `::: details Chứng minh${title ? `: ${title}` : ''}`)
          .replace(/^::: exercise(?:[\t ]+(.*))?$/gm, (_, title) => `::: warning Bài tập${title ? `: ${title}` : ''}`)
          .replace(/^::: solution(?:[\t ]+(.*))?$/gm, (_, title) => `::: details Lời giải${title ? `: ${title}` : ''}`)
          .replace(/^::: derivation(?:[\t ]+(.*))?$/gm, (_, title) => `::: details Khai triển chi tiết${title ? `: ${title}` : ''}`)
          .replace(/^::: hint(?:[\t ]+(.*))?$/gm, (_, title) => `::: tip Gợi ý${title ? `: ${title}` : ''}`);
      });
      md.use(termLinks,base)
      // Only standalone images become figures; escape alt text before inserting captions.
      md.core.ruler.after('inline', 'study_image_captions', state => {
        for (let i = 1; i < state.tokens.length - 1; i++) {
          const token = state.tokens[i]
          if (token.type !== 'inline' || state.tokens[i-1].type !== 'paragraph_open') continue
          const children = token.children?.filter(child => child.type !== 'text' || child.content.trim()) || []
          if (children.length !== 1 || children[0].type !== 'image') continue
          const image = children[0]
          const caption = image.content
          state.tokens[i-1].tag = 'figure'
          state.tokens[i-1].attrSet('class', 'lecture-figure')
          state.tokens[i+1].tag = 'figure'
          if (caption) {
            const token = new state.Token('html_inline', '', 0)
            token.content = `<figcaption>${md.utils.escapeHtml(caption)}</figcaption>`
            state.tokens[i].children.push(token)
          }
        }
      })
    }
  },
  mermaid:{theme:'base',themeVariables:{fontSize:'15px',fontFamily:'Be Vietnam Pro, sans-serif',primaryColor:colorToken('tim-soft'),primaryBorderColor:colorToken('tim'),primaryTextColor:colorToken('ink')},flowchart:{htmlLabels:true,padding:18,curve:'basis'}},
  appearance:true,
  vite:{plugins:[mathTextPlugin()],resolve:{alias:{'vitepress-plugin-mermaid/Mermaid.vue':fileURLToPath(new URL('./theme/StudyMermaid.vue',import.meta.url))}},optimizeDeps:{include:['mermaid','fastdom','fastdom/extensions/fastdom-promised.js']}},
  themeConfig:{
    sidebarMenuLabel:'Bài giảng',returnToTopLabel:'Về đầu bài',outlineTitle:'Mục lục',
    siteTitle:'UETệ', darkModeSwitchLabel:'Giao diện', lightModeSwitchTitle:'Chuyển sang giao diện sáng', darkModeSwitchTitle:'Chuyển sang giao diện tối',
    nav:[
      {text:'Vật lý 1',link:'/vat-ly-1/',activeMatch:'^/vat-ly-1/'},
      {text:'Vật lý 2',link:'/vat-ly-2/',activeMatch:'^/vat-ly-2/'},
      {text:'Học phần',items:courseCatalog.map(c=>({text:`${c.name} (${c.lessons.length} bài)`,link:`/${c.id}/`}))},
      {text:'Vật lý 1',link:'/vat-ly-1/',activeMatch:'^/vat-ly-1/'},
      {text:'Vật lý 2',link:'/vat-ly-2/',activeMatch:'^/vat-ly-2/'},
      {text:'Wiki',link:'/wiki/'}, {text:'Góc học tập',link:'/goc-hoc-tap'}, {text:'Hướng dẫn học',link:'/guide/'}
    ],
    sidebar:{
      ...Object.fromEntries(courseCatalog.map(course=>[`/${course.id}/`,[
        {text: course.name, items:[
          {text:'Tổng quan môn học',link:`/${course.id}/`},
          {text:'Bài tập ôn luyện',link:`/${course.id}/bai-tap`}
        ]},
        ...(course.parts ? course.parts.map(part=>({
          text: part.title,
          collapsed: false,
          items: part.lessons.map(slug => {
            const lesson = course.lessons.find(l => l.slug === slug)
            if (!lesson) return null
            const topics = (lesson.topicGroups || []).flatMap(group => group.topics)
            return {
              text: (course.id==='toan-cho-ai'?`Lecture ${String(lesson.number).padStart(2,'0')}. `:'') + lesson.title + (lesson.status==='draft'?' (đang biên soạn)':''),
              link: `/${course.id}/bai-giang/${lesson.slug}`,
              // Chương có trang chủ đề: liệt kê các chủ đề theo thứ tự đọc, thu gọn khi không ở trong chương.
              ...(topics.length ? { collapsed: true, items: topics.map((topic, i) => ({ text: `${i + 1}. ${topic.title}`, link: `/${course.id}/bai-giang/${lesson.slug}/${topic.slug}` })) } : {})
            }
          }).filter(Boolean)
        })) : [
          {text:'Bài giảng',items:course.lessons.map(lesson=>({text:lesson.title+(lesson.status==='draft'?' (đang biên soạn)':''),link:`/${course.id}/bai-giang/${lesson.slug}`}))}
        ]),
        {text:'Tra cứu',items:[{text:'Wiki thuật ngữ',link:'/wiki/'},{text:'Góc học tập',link:'/goc-hoc-tap'}]}
      ]])),
      '/wiki/':[
        {text:'Wiki học tập',items:[{text:'Tất cả thuật ngữ',link:'/wiki/'}]},
        ...wikiGroups.map(group=>({text:group.name,collapsed:true,items:group.ids.map(id=>({text:concepts[id].name,link:`/wiki/${id}`}))}))
      ],
      '/guide/':[{text:'Hướng dẫn',items:[{text:'Phương pháp học',link:'/guide/'},{text:'Đóng góp nội dung',link:'/guide/contribute'}]}]
    },
    outline:{level:2,label:'Mục lục'},
    docFooter:{prev:'Bài trước',next:'Bài tiếp theo'},lastUpdated:{text:'Cập nhật lần cuối'},
  }
}))
