// Pure build-time navigation model. The VitePress adapter supplies content.
import { getUetCourses, getExtendedCourses, isExtendedCourse } from '../../../content/collections.mjs'

export function buildThemeConfig({ courseCatalog = [], wikiGroups = [], concepts = {} } = {}) {
  const uetCourses = getUetCourses(courseCatalog)
  const extendedCourses = getExtendedCourses(courseCatalog)

  const nav = [
    { text: 'Trang chủ', link: '/' },
    {
      text: 'Học phần UET',
      items: uetCourses.map(c => ({
        text: `${c.name} (${(c.lessons || []).length} ${c.presentation === 'philosophy' ? 'chương' : 'bài'})`,
        link: `/${c.id}/`
      }))
    },
    ...(extendedCourses.length ? [{
      text: 'Học liệu mở rộng',
      link: '/hoc-lieu-mo-rong/',
      items: [
        { text: 'Thư viện học liệu mở rộng', link: '/hoc-lieu-mo-rong/' },
        ...extendedCourses.map(c => ({
          text: `${c.name} (${(c.lessons || []).length} chương)`,
          link: `/${c.id}/`
        }))
      ]
    }] : [
      { text: 'Học liệu mở rộng', link: '/hoc-lieu-mo-rong/' }
    ]),
    { text: 'Wiki', link: '/wiki/' },
    { text: 'Góc học tập', link: '/goc-hoc-tap' },
    { text: 'Hướng dẫn học', link: '/guide/' }
  ]

  const courseSidebars = Object.fromEntries(courseCatalog.map(course => {
    const isExt = isExtendedCourse(course)
    return [
      `/${course.id}/`,
      course.presentation === 'philosophy' ? [
        {
          text: course.name,
          items: [
            { text: 'Học tập', link: `/${course.id}/` },
            {
              text: 'Ôn thi',
              link: `/${course.id}/on-thi/`,
              items: [
                ...course.lessons.map(chapter => ({
                  text: `Chương ${['I', 'II', 'III'][chapter.number - 1] || chapter.number}`,
                  link: `/${course.id}/on-thi/chuong-${chapter.number}`,
                  items: [{ text: 'Điền từ', link: `/${course.id}/on-thi/chuong-${chapter.number}/dien-tu` }]
                })),
                { text: 'Đề thi trắc nghiệm', link: `/${course.id}/on-thi/de-thi/` }
              ]
            }
          ]
        },
        ...course.lessons.map(chapter => ({
          text: `Chương ${chapter.number}. ${chapter.title}`,
          link: `/${course.id}/bai-giang/${chapter.slug}`,
          collapsed: true,
          items: (chapter.topics || []).map(topic => ({ text: topic.title, link: `/${course.id}/bai-giang/${chapter.slug}/${topic.slug}` }))
        }))
      ] : [
        {
          text: course.name,
          items: [
            { text: isExt ? 'Tổng quan sách & Mục lục' : 'Tổng quan môn học', link: `/${course.id}/` },
            ...(!course.review ? [{
              text: course.problemSets ? 'Problem Set' : 'Bài tập ôn luyện',
              link: `/${course.id}/bai-tap`,
              ...(course.problemSets ? { items: course.problemSets.map(set => ({ text: set.title, link: `/${course.id}/problem-set/${set.slug}` })) } : {})
            }] : []),
            ...(course.id === 'xu-ly-du-lieu' ? [
              { text: 'Ôn thi', link: `/${course.id}/on-thi/` },
              { text: 'Đề thi', link: `/${course.id}/de-thi/`, items: [1, 2, 3, 4, 5].map(number => ({ text: `Đề ${number}`, link: `/${course.id}/de-thi/de-${number}` })) },
            ] : []),
            ...(isExt ? [{ text: 'Lộ trình và tài liệu', link: `/${course.id}/notes/lo-trinh` }] : [])
          ]
        },
        ...(course.review ? [
          {
            text: 'Ôn luyện',
            collapsed: false,
            items: [
              { text: 'Tổng quan ôn luyện', link: `/${course.id}/on-luyen` },
              ...course.review.topicGroups.map(group => ({
                text: group.title,
                collapsed: true,
                items: group.topics.map(topic => ({ text: topic.title, link: `/${course.id}/on-luyen/${topic.slug}` }))
              }))
            ]
          },
          { text: course.problemSets ? 'Homework' : 'Bài tập ôn luyện', items: [
            { text: 'Bài tập', link: `/${course.id}/bai-tap` },
            ...(course.problemSets || []).map(set => ({ text: set.title, link: `/${course.id}/problem-set/${set.slug}` }))
          ] }
        ] : []),
        ...(course.parts ? course.parts.map(part => ({
          text: part.title,
          ...(part.link ? { link: part.link } : {}),
          collapsed: part.collapsed ?? false,
          items: part.lessons.map(slug => {
            const lesson = (course.lessons || []).find(l => l.slug === slug)
            if (!lesson) return null
            const topics = (lesson.topicGroups || []).flatMap(group => group.topics)
            return {
              text: (course.id === 'toan-cho-ai' ? `Lecture ${String(lesson.number).padStart(2, '0')}. ` : '') + lesson.title + (lesson.status === 'draft' ? ' (đang biên soạn)' : ''),
              link: `/${course.id}/bai-giang/${lesson.slug}`,
              ...(topics.length ? { collapsed: true, items: topics.map((topic, i) => ({ text: isExt ? topic.title : `${i + 1}. ${topic.title}`, link: `/${course.id}/bai-giang/${lesson.slug}/${topic.slug}` })) } : {})
            }
          }).filter(Boolean)
        })) : [
          { text: isExt ? 'Các chương sách' : 'Bài giảng', items: (course.lessons || []).map(lesson => ({ text: lesson.title + (lesson.status === 'draft' ? ' (đang biên soạn)' : ''), link: `/${course.id}/bai-giang/${lesson.slug}` })) }
        ]),
        {
          text: 'Tra cứu',
          items: [
            ...(isExt ? [{ text: 'Thư viện mở rộng', link: '/hoc-lieu-mo-rong/' }] : []),
            { text: 'Wiki thuật ngữ', link: '/wiki/' },
            { text: 'Góc học tập', link: '/goc-hoc-tap' }
          ]
        }
      ]
    ]
  }))

  const sidebar = {
    ...courseSidebars,
    '/hoc-lieu-mo-rong/': [
      {
        text: 'Thư viện học liệu mở rộng',
        items: [
          { text: 'Tất cả học liệu mở rộng', link: '/hoc-lieu-mo-rong/' },
          ...extendedCourses.map(c => ({ text: c.name, link: `/${c.id}/` }))
        ]
      },
      {
        text: 'Tra cứu & Điều hướng',
        items: [
          { text: 'Trang chủ UET', link: '/' },
          { text: 'Wiki thuật ngữ', link: '/wiki/' },
          { text: 'Góc học tập', link: '/goc-hoc-tap' }
        ]
      }
    ],
    '/wiki/': [
      { text: 'Wiki học tập', items: [{ text: 'Tất cả thuật ngữ', link: '/wiki/' }] },
      ...wikiGroups.map(group => ({ text: group.name, collapsed: true, items: (group.ids || []).map(id => ({ text: concepts[id]?.name || id, link: `/wiki/${id}` })) }))
    ],
    '/guide/': [{ text: 'Hướng dẫn', items: [{ text: 'Phương pháp học', link: '/guide/' }] }]
  }

  return {
    sidebarMenuLabel: 'Bài giảng',
    returnToTopLabel: 'Về đầu bài',
    outlineTitle: 'Mục lục',
    siteTitle: 'UETệ',
    darkModeSwitchLabel: 'Giao diện',
    lightModeSwitchTitle: 'Chuyển sang giao diện sáng',
    darkModeSwitchTitle: 'Chuyển sang giao diện tối',
    nav,
    sidebar,
    outline: { level: [2, 3], label: 'Mục lục' },
    docFooter: { prev: 'Bài trước', next: 'Bài tiếp theo' },
    lastUpdated: { text: 'Cập nhật lần cuối' }
  }
}
