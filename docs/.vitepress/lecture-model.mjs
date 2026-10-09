import { findCourse } from './course-catalog.mjs'
import { readingMetadata } from './reading-metadata.mjs'
export const lectureParts = [{ id: 'notes', name: 'Notes' }, { id: 'slides', name: 'Slides' }, { id: 'cheatsheet', name: 'Cheatsheet' }, { id: 'kien-thuc-can-co', name: 'Kiến thức nền' }]
export const readingMinutes = (courseId, slug) => readingMetadata[`${courseId}/${slug}`]?.minutes || 5

export const lecturePath = (courseId, slug, part = '') => `/${courseId}/bai-giang/${slug}${part ? `#${part}` : ''}`
export const lectureConceptIds = lesson => [...new Set([...(lesson?.prerequisites || []), ...(lesson?.supportingConcepts || [])])]
export function findLecture(courseId, slug) { return findCourse(courseId)?.lessons.find(lesson => lesson.slug === slug) }

// A long lecture can be split into topic pages. The lecture page stays the chapter hub (Notes, Slides,
// Kiến thức nền); each topic lives at /<course>/bai-giang/<lecture>/<topic> and is read in catalog order.
export const lessonTopics = lesson => (lesson?.topicGroups || []).flatMap((group, groupIndex) =>
  group.topics.map(topic => ({ ...topic, group: group.title, groupIndex })))
export const topicPath = (courseId, lessonSlug, topicSlug) => `/${courseId}/bai-giang/${lessonSlug}/${topicSlug}`
export const topicMinutes = (courseId, lessonSlug, topicSlug) => readingMetadata[`${courseId}/${lessonSlug}/${topicSlug}`]?.minutes || 5
export function findTopic(courseId, lessonSlug, topicSlug) {
  const lesson = findLecture(courseId, lessonSlug)
  const topics = lessonTopics(lesson)
  const index = topics.findIndex(topic => topic.slug === topicSlug)
  return index < 0 ? null : { lesson, topics, index, topic: topics[index] }
}
export function lectureSlides(course, lesson) {
  if (!course || !lesson) return []
  const slides = course.slides.filter(slide => slide.note === lesson.slug)
  if (slides.length || lesson.status !== 'ready') return slides
  if (course.id === 'dsa' && lesson.slug === 'trees') return [{ title: 'Cây & cây nhị phân', note: 'trees', bullets: ['Cây gốc biểu diễn quan hệ cha–con; lá không có con.', 'Cây nhị phân có tối đa hai con. Cây tìm kiếm nhị phân còn yêu cầu quy tắc thứ tự.', 'Duyệt trước, giữa và sau khác nhau ở thời điểm xử lý nút gốc.', 'Chi phí tìm kiếm trên BST phụ thuộc chiều cao; cây lệch có thể tốn O(n).'], formula: 'Cây cân bằng: chiều cao O(log n)', example: 'Duyệt giữa một BST với khóa phân biệt cho dãy khóa tăng dần.' }]
  return []
}

export { getLectureCheatsheet as lectureCheatsheet } from './cheatsheets.mjs'
