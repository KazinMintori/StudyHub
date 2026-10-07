import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import { courseCatalog } from './course-catalog.mjs'
import { wikiGroups } from './wiki-content.mjs'
import { concepts } from './concepts.mjs'
import { termLinks } from './term-links.mjs'
import { renderStudySearch } from './search-render.mjs'

const base=process.env.BASE_PATH || (process.env.GITHUB_ACTIONS ? `/${process.env.GITHUB_REPOSITORY?.split('/')[1] || 'StudyHub'}/` : '/')
export default withMermaid(defineConfig({
  base, title:'UETệ', description:'Bài giảng UET và Wiki thuật ngữ', lang:'vi-VN',
  head:[['link',{rel:'icon',href:`${base}favicon.svg`}],['meta',{name:'theme-color',content:'#244bd6'}]],
  markdown:{math:true,lineNumbers:true,config:md=>md.use(termLinks,base)},
  mermaid:{theme:'default',themeVariables:{fontSize:'14px',fontFamily:'Inter, system-ui, sans-serif'},flowchart:{htmlLabels:true,padding:18,curve:'basis'}},
  appearance:true,
  vite:{optimizeDeps:{include:['mermaid','fastdom','fastdom/extensions/fastdom-promised.js']}},
  themeConfig:{
    siteTitle:'UETệ', darkModeSwitchLabel:'Giao diện', lightModeSwitchTitle:'Chuyển sang giao diện sáng', darkModeSwitchTitle:'Chuyển sang giao diện tối',
    nav:[
      {text:'Trang chủ',link:'/'},
      {text:'Học phần',items:courseCatalog.filter(c=>c.current).map(c=>({text:c.name,link:`/${c.id}/`}))},
      {text:'Môn học khác',items:courseCatalog.filter(c=>!c.current).map(c=>({text:c.name,link:`/${c.id}/`}))},
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
    search:{provider:'local',options:{_render:renderStudySearch,locales:{root:{translations:{button:{buttonText:'Tìm kiếm bài học & Wiki…',buttonAriaLabel:'Tìm kiếm tài liệu'},modal:{noResultsText:'Không tìm thấy kết quả cho',resetButtonTitle:'Xóa tìm kiếm',footer:{selectText:'để chọn',navigateText:'để điều hướng',closeText:'để đóng'}}}}}}},
    outline:{level:[2,3],label:'Mục lục bài viết'},
    docFooter:{prev:'Bài trước',next:'Bài tiếp theo'},lastUpdated:{text:'Cập nhật lần cuối'},
    footer:{message:'Tài liệu học tập dành cho sinh viên UET',copyright:'Bản quyền nội dung © 2026 UETệ'}
  }
}))
