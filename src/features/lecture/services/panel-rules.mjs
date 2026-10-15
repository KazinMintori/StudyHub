export function foundationGroupsFor(lesson, concepts) {
  const required = (lesson?.prerequisites || []).filter(id => concepts[id])
  const supporting = (lesson?.supportingConcepts || []).filter(id => concepts[id] && !required.includes(id))
  return [
    { id: 'required', title: 'Cần ôn trước', description: 'Bài giảng dùng trực tiếp các khái niệm này mà không trình bày lại từ đầu.', ids: required },
    { id: 'supporting', title: 'Tra cứu trong khi đọc', description: 'Các thuật ngữ xuất hiện trong Notes hoặc Slides. Bạn không cần học thuộc trước; hãy mở mục tương ứng khi gặp chỗ chưa rõ.', ids: supporting }
  ].filter(group => group.ids.length)
}
export function panelHasContent(course, lesson, part) {
  if (!course || !lesson) return false
  if (['slides', 'cheatsheet', 'kien-thuc-can-co'].includes(part)) return true
  return part === 'bai-tap' && !lesson.hasChapterExercises
}
