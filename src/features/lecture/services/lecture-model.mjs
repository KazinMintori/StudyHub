import { findCourse } from '../../../content/catalog.mjs'
import { readingMetadata } from '../../../../docs/.vitepress/reading-metadata.mjs'
export const lectureParts = [
  { id: 'kien-thuc-can-co', name: 'Kiến thức nền' },
  { id: 'notes', name: 'Notes' },
  { id: 'bai-tap', name: 'Bài tập' },
  { id: 'cheatsheet', name: 'Cheatsheet' }
]
export const readingMinutes = (courseId, slug) => readingMetadata[`${courseId}/${slug}`]?.minutes || 5

export const lecturePath = (courseId, slug, part = '') => `/${courseId}/${slug === 'on-luyen' ? 'on-luyen/tong-hop' : `bai-giang/${slug}`}${part ? `#${part}` : ''}`
export const lectureConceptIds = lesson => [...new Set([...(lesson?.prerequisites || []), ...(lesson?.supportingConcepts || [])])]
export function findLecture(courseId, slug) {
  const course = findCourse(courseId)
  if (!course || !slug) return undefined
  return course?.lessons.find(lesson => lesson.slug === slug) || (course?.review?.slug === slug ? course.review : undefined)
}

// A long lecture can be split into topic pages. The lecture page stays the chapter hub (Notes, Cheatsheet,
// Kiến thức nền); each topic lives at /<course>/bai-giang/<lecture>/<topic> and is read in catalog order.
export const lessonTopics = lesson => (lesson?.topicGroups || []).flatMap((group, groupIndex) =>
  group.topics.map(topic => ({ ...topic, group: group.title, groupIndex })))
export const topicPath = (courseId, lessonSlug, topicSlug) => `/${courseId}/${lessonSlug === 'on-luyen' ? 'on-luyen' : `bai-giang/${lessonSlug}`}/${topicSlug}`
export const topicMinutes = (courseId, lessonSlug, topicSlug) => readingMetadata[`${courseId}/${lessonSlug}/${topicSlug}`]?.minutes || 5
export function findTopic(courseId, lessonSlug, topicSlug) {
  const lesson = findLecture(courseId, lessonSlug)
  const topics = lessonTopics(lesson)
  const index = topics.findIndex(topic => topic.slug === topicSlug)
  return index < 0 ? null : { lesson, topics, index, topic: topics[index] }
}
export function lectureSlides(course, lesson) {
  if (!course || !lesson) return []
  return (course.slides || []).filter(slide => slide.note === lesson.slug)
}
