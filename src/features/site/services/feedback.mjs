import { feedbackConfig } from '../../../config/feedback.mjs'

export function captureFeedbackContext({ pageTitle, courseName, href }) {
  const url = new URL(href)
  if (!['https:', 'http:'].includes(url.protocol)) throw new Error('Đường dẫn trang không hợp lệ.')
  // Keep the lesson/tab anchor, but exclude query strings and credentials.
  url.search = ''
  url.username = ''
  url.password = ''
  return {
    pageTitle: String(pageTitle || 'Trang StudyHub').trim(),
    courseName: String(courseName || '').trim(),
    url: url.href
  }
}

export function buildFeedbackIssueUrl({ category, description, context }) {
  const selectedCategory = feedbackConfig.categories.find(item => item.id === category)
  const message = String(description || '').trim()
  if (!selectedCategory) throw new Error('Chọn loại góp ý hợp lệ.')
  if (!message) throw new Error('Bạn hãy mô tả lỗi hoặc góp ý trước khi tiếp tục.')
  if (message.length > feedbackConfig.maxDescriptionLength) throw new Error('Mô tả tối đa 1000 ký tự.')

  const body = [
    '## Góp ý',
    message,
    '',
    '## Bài học đang mở',
    `Tên trang: ${context.pageTitle}`,
    ...(context.courseName ? [`Môn học: ${context.courseName}`] : []),
    `Đường dẫn: ${context.url}`,
    `Loại góp ý: ${selectedCategory.label}`
  ].join('\n')
  const url = new URL(`https://github.com/${feedbackConfig.repository}/issues/new`)
  url.searchParams.set('title', `[${selectedCategory.label}] ${context.pageTitle}`.slice(0, 160))
  url.searchParams.set('body', body)
  if (url.href.length > feedbackConfig.maxIssueUrlLength) {
    throw new Error('Nội dung quá dài để mở trên GitHub. Bạn hãy rút gọn mô tả và bổ sung chi tiết trên GitHub.')
  }
  return url.href
}
