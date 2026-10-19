// Pure build-time navigation model. The VitePress adapter supplies content.
export function buildThemeConfig({ courseCatalog, wikiGroups, concepts }) {
  return {
    sidebarMenuLabel:'Bài giảng',returnToTopLabel:'Về đầu bài',outlineTitle:'Mục lục',
    siteTitle:'UETệ', darkModeSwitchLabel:'Giao diện', lightModeSwitchTitle:'Chuyển sang giao diện sáng', darkModeSwitchTitle:'Chuyển sang giao diện tối',
    nav:[
      {text:'Học phần',items:courseCatalog.map(c=>({text:`${c.name} (${c.lessons.length} bài)`,link:`/${c.id}/`}))},
      {text:'Wiki',link:'/wiki/'}, {text:'Góc học tập',link:'/goc-hoc-tap'}, {text:'Hướng dẫn học',link:'/guide/'}
    ],
    sidebar:{
      ...Object.fromEntries(courseCatalog.map(course=>[`/${course.id}/`,[
        {text: course.name, items:[
          {text:'Tổng quan môn học',link:`/${course.id}/`},
          ...(!course.review ? [{
            text:course.problemSets ? 'Problem Set' : 'Bài tập ôn luyện',
            link:`/${course.id}/bai-tap`,
            ...(course.problemSets ? {items:course.problemSets.map(set=>({text:set.title,link:`/${course.id}/problem-set/${set.slug}`}))} : {})
          }] : []),
          ...(course.id === 'xu-ly-du-lieu' ? [{text:'Ôn thi',link:`/${course.id}/on-thi/`}] : [])
        ]},
        ...(course.review ? [
          {text:'Ôn luyện',collapsed:false,items:[
            {text:'Tổng quan ôn luyện',link:`/${course.id}/on-luyen`},
            ...course.review.topicGroups.map(group=>({text:group.title,collapsed:true,items:group.topics.map(topic=>({text:topic.title,link:`/${course.id}/on-luyen/${topic.slug}`}))}))
          ]},
          {text:'Bài tập ôn luyện',items:[{text:'Bài tập',link:`/${course.id}/bai-tap`}]}
        ] : []),
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
              // Chương có trang chủ đề: Liệt kê các chủ đề theo thứ tự đọc, thu gọn khi không ở trong chương.
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
}
