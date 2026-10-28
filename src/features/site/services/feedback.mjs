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

export function validateFeedback({ category, description, contact = '' }) {
  const selectedCategory = feedbackConfig.categories.find(item => item.id === category)
  const message = String(description || '').trim()
  const reply = String(contact || '').trim()
  if (!selectedCategory) throw new Error('Chọn loại góp ý hợp lệ.')
  if (!message) throw new Error('Bạn hãy viết vài dòng mô tả trước khi gửi.')
  if (message.length > feedbackConfig.maxDescriptionLength) throw new Error(`Mô tả tối đa ${feedbackConfig.maxDescriptionLength} ký tự.`)
  if (reply.length > feedbackConfig.maxContactLength) throw new Error('Thông tin liên hệ quá dài.')
  return { selectedCategory, message, reply }
}

export function formatFeedbackText({ category, description, contact, context, includePage = true }) {
  const { selectedCategory, message, reply } = validateFeedback({ category, description, contact })
  return [
    `Loại góp ý: ${selectedCategory.label}`,
    '',
    message,
    ...(includePage && context ? ['', `Trang: ${context.pageTitle}`, ...(context.courseName ? [`Môn học: ${context.courseName}`] : []), `Đường dẫn: ${context.url}`] : []),
    ...(reply ? ['', `Liên hệ: ${reply}`] : [])
  ].join('\n')
}

export function hasFeedbackEndpoint() {
  return Boolean(feedbackConfig.endpoint)
}

export async function sendFeedback({ category, description, contact, context, includePage = true, endpoint = feedbackConfig.endpoint, accessKey = feedbackConfig.accessKey, fetchImpl = globalThis.fetch }) {
  const { selectedCategory, message, reply } = validateFeedback({ category, description, contact })
  if (!endpoint) throw new Error('Kênh gửi trực tiếp chưa được cấu hình.')
  const payload = {
    subject: `[StudyHub · ${selectedCategory.short}] ${includePage && context ? context.pageTitle : 'Góp ý chung'}`.slice(0, 160),
    category: selectedCategory.label,
    message,
    ...(includePage && context ? { page_title: context.pageTitle, course: context.courseName, page_url: context.url } : {}),
    ...(reply ? { contact: reply } : {}),
    ...(accessKey ? { access_key: accessKey, from_name: 'StudyHub' } : {})
  }
  const controller = typeof AbortController === 'function' ? new AbortController() : null
  const timer = controller ? setTimeout(() => controller.abort(), feedbackConfig.requestTimeoutMs) : null
  try {
    const response = await fetchImpl(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(payload),
      signal: controller?.signal
    })
    let body = null
    try { body = await response.json() } catch { /* some services answer with an empty body */ }
    if (!response.ok || body?.success === false) throw new Error('Máy chủ góp ý từ chối yêu cầu.')
    return true
  } catch (cause) {
    if (cause?.name === 'AbortError') throw new Error('Gửi quá lâu, có thể mạng đang chậm.')
    if (cause instanceof TypeError) throw new Error('Không kết nối được tới máy chủ góp ý.')
    throw cause
  } finally {
    if (timer) clearTimeout(timer)
  }
}

export function buildFeedbackIssueUrl({ category, description, contact, context, includePage = true }) {
  const { selectedCategory } = validateFeedback({ category, description, contact })
  const body = formatFeedbackText({ category, description, contact, context, includePage })
  const url = new URL(`https://github.com/${feedbackConfig.repository}/issues/new`)
  url.searchParams.set('title', `[${selectedCategory.label}] ${includePage && context ? context.pageTitle : 'Góp ý chung'}`.slice(0, 160))
  url.searchParams.set('body', body)
  if (url.href.length > feedbackConfig.maxIssueUrlLength) {
    throw new Error('Nội dung quá dài để mở trên GitHub. Bạn hãy rút gọn mô tả.')
  }
  return url.href
}
