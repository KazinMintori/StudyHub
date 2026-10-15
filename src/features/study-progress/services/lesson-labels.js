export const mathAiChapters = {
  'bai-00-on-tap-nen-tang': 'Phần 0. Nền tảng giải tích & ma trận',
  'bai-01-nhap-mon-toi-uu': 'Phần 1. Tối ưu lồi: Tập lồi, hàm lồi & bài toán tối ưu',
  'bai-02-tap-loi': 'Phần 2. Các lớp bài toán tối ưu lồi',
  'bai-03-doi-ngau-lagrange': 'Phần 3. Đối ngẫu Lagrange & điều kiện KKT',
  'bai-04-gradient-newton': 'Phần 4. Phương pháp Gradient, Newton & điểm trong',
  'bai-05-toi-uu-huan-luyen': 'Phần 5. Tối ưu trong huấn luyện mô hình sâu',
  'bai-06-phuong-phap-thich-nghi': 'Phần 6. Phương pháp thích nghi & mở rộng',
  'bai-07-quy-hoach-tuyen-tinh-va-dong': 'Phần 7. Quy hoạch tuyến tính & quy hoạch động'
}

export function getLessonChapter(course, lesson) {
  if (!course || !lesson) return ''
  if (course.id === 'toan-cho-ai' && mathAiChapters[lesson.slug]) {
    return mathAiChapters[lesson.slug]
  }
  const part = course.parts?.find(p => p.lessons?.includes(lesson.slug))
  if (part && part.title && part.title !== 'Bài giảng') {
    return part.title
  }
  return part?.title || ''
}

export function getLessonDetailTitle(course, lesson) {
  if (!course || !lesson) return ''
  const num = lesson.number ?? (course.lessons ? course.lessons.indexOf(lesson) + 1 : 1)
  if (/^bài\s*\d+/i.test(lesson.title)) {
    return lesson.title
  }
  return `Bài ${num}: ${lesson.title}`
}
