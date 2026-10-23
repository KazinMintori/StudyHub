import { courseCatalog } from '../../../content/catalog.mjs'
import { cards } from './flashcards.mjs'

export const courses = courseCatalog.map(course => ({
  ...course,
  tags: course.presentation === 'philosophy' ? 'Notes, Bài tập theo chủ đề và Ôn thi' : 'Notes, Cheatsheet và Kiến thức nền theo từng bài',
  first: course.lessons.find(lesson => lesson.status === 'ready')?.slug || '',
  count: course.lessons.filter(lesson => lesson.status === 'ready').length
}))

export { cards }
