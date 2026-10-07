import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import { courseCatalog } from './course-catalog.mjs'
import { wikiGroups } from './wiki-content.mjs'
import { concepts } from './concepts.mjs'
import { termLinks } from './term-links.mjs'

const base=process.env.BASE_PATH || (process.env.GITHUB_ACTIONS ? `/${process.env.GITHUB_REPOSITORY?.split('/')[1] || 'StudyHub'}/` : '/')
export default withMermaid(defineConfig({
  base, title:'UETệ', description:'Bài giảng UET và Wiki thuật ngữ', lang:'vi-VN',
  ignoreDeadLinks: true,
  head:[
    ['link',{rel:'icon',href:`${base}favicon.svg`}],
    ['link',{rel:'icon',type:'image/png',href:`${base}favicon.png`}],
    ['meta',{name:'theme-color',content:'#244bd6'}],
    ['link',{rel:'preconnect',href:'https://fonts.googleapis.com'}],
    ['link',{rel:'preconnect',href:'https://fonts.gstatic.com',crossorigin:''}],
    ['link',{rel:'stylesheet',href:'https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&family=JetBrains+Mono:wght@600;700&family=Lora:ital,wght@0,600;0,700;1,600&family=Playfair+Display:ital,wght@0,700;1,700&family=Plus+Jakarta+Sans:wght@700;800&family=Space+Grotesk:wght@600;700&display=swap'}]
  ],
  markdown:{
    math:true,
    lineNumbers:true,
    config:md=>{
      md.core.ruler.before('block', 'normalize_custom_containers', state => {
        state.src = state.src
          .replace(/^::: example(?:\s+(.*))?$/gm, (_, title) => `::: info Ví dụ${title ? `: ${title}` : ''}`)
          .replace(/^::: proof(?:\s+(.*))?$/gm, (_, title) => `::: details Chứng minh${title ? `: ${title}` : ''}`)
          .replace(/^::: exercise(?:\s+(.*))?$/gm, (_, title) => `::: warning Bài tập${title ? `: ${title}` : ''}`)
          .replace(/^::: solution(?:\s+(.*))?$/gm, (_, title) => `::: details Lời giải${title ? `: ${title}` : ''}`)
          .replace(/^::: derivation(?:\s+(.*))?$/gm, (_, title) => `::: details Khai triển chi tiết${title ? `: ${title}` : ''}`)
          .replace(/^::: hint(?:\s+(.*))?$/gm, (_, title) => `::: tip Gợi ý${title ? `: ${title}` : ''}`);
      });
      md.use(termLinks,base)
    }
  },
  mermaid:{theme:'default',themeVariables:{fontSize:'14px',fontFamily:'Inter, system-ui, sans-serif'},flowchart:{htmlLabels:true,padding:18,curve:'basis'}},
  appearance:true,
  vite:{optimizeDeps:{include:['mermaid','fastdom','fastdom/extensions/fastdom-promised.js']}},
  themeConfig:{
    logo:{light:'/logo.png',dark:'/logo-dark.png',alt:'UET Polytechnic'},
    siteTitle:'UETệ', darkModeSwitchLabel:'Giao diện', lightModeSwitchTitle:'Chuyển sang giao diện sáng', darkModeSwitchTitle:'Chuyển sang giao diện tối',
    nav:[
      {text:'Trang chủ',link:'/'},
      {text:'Học phần',items:courseCatalog.map(c=>({text:c.name,link:`/${c.id}/`}))},
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
            return {
              text: lesson.title + (lesson.status==='draft'?' (đang biên soạn)':''),
              link: `/${course.id}/bai-giang/${lesson.slug}`
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
    outline:{level:[2,3],label:'Mục lục bài viết'},
    docFooter:{prev:'Bài trước',next:'Bài tiếp theo'},lastUpdated:{text:'Cập nhật lần cuối'},
    footer:{message:'Tài liệu học tập dành cho sinh viên UET',copyright:'Bản quyền nội dung © 2026 UETệ'}
  }
}))
