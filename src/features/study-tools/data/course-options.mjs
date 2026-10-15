import { courseCatalog } from '../../../content/catalog.mjs'
import { cards } from './flashcards.mjs'

export const courses = courseCatalog.map(course => ({
  ...course,
  tags: 'Slides · Notes · Nền tảng theo từng bài',
  first: course.lessons.find(lesson => lesson.status === 'ready')?.slug || '',
  count: course.lessons.filter(lesson => lesson.status === 'ready').length
}))

export { cards }
