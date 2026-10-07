import { findCourse } from './course-catalog.mjs'

export const lecturePath = (courseId, slug, part = '') => `/${courseId}/bai-giang/${slug}${part ? `#${part}` : ''}`
export function findLecture(courseId, slug) { return findCourse(courseId)?.lessons.find(lesson => lesson.slug === slug) }
export function lectureSlides(course, lesson) {
  if (!course || !lesson) return []
  const slides = course.slides.filter(slide => slide.note === lesson.slug)
  if (slides.length || lesson.status !== 'ready') return slides
  if (course.id === 'dsa' && lesson.slug === 'trees') return [{ title: 'Cây & cây nhị phân', note: 'trees', bullets: ['Cây gốc biểu diễn quan hệ cha–con; lá không có con.', 'Cây nhị phân có tối đa hai con. Cây tìm kiếm nhị phân còn yêu cầu quy tắc thứ tự.', 'Duyệt trước, giữa và sau khác nhau ở thời điểm xử lý nút gốc.', 'Chi phí tìm kiếm trên BST phụ thuộc chiều cao; cây lệch có thể tốn O(n).'], formula: 'Cây cân bằng: chiều cao O(log n)', example: 'Duyệt giữa một BST với khóa phân biệt cho dãy khóa tăng dần.' }]
  return []
}
