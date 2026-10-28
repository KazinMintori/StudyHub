import test from 'node:test'
import assert from 'node:assert/strict'
import { captureFeedbackContext, buildFeedbackIssueUrl, formatFeedbackText, sendFeedback } from '../../src/features/site/services/feedback.mjs'

const context = captureFeedbackContext({
  pageTitle: 'Đạo hàm & gradient',
  courseName: 'Cơ sở toán học cho AI',
  href: 'https://KazinMintori.github.io/StudyHub/toan-cho-ai/bai-giang/dao-ham.html?token=private#slides'
})

test('feedback automatically includes the lesson, course, base path and current tab without query data', () => {
  const url = new URL(buildFeedbackIssueUrl({ category: 'content', description: 'Thiếu dấu trừ & ký hiệu # ở mục 2.', context }))
  assert.equal(url.origin + url.pathname, 'https://github.com/KazinMintori/StudyHub/issues/new')
  assert.equal(url.searchParams.get('title'), '[Nội dung sai hoặc khó hiểu] Đạo hàm & gradient')
  const body = url.searchParams.get('body')
  for (const expected of ['Đạo hàm & gradient', 'Cơ sở toán học cho AI', '/StudyHub/toan-cho-ai/bai-giang/dao-ham.html#slides', 'Thiếu dấu trừ & ký hiệu # ở mục 2.']) assert.ok(body.includes(expected))
  assert.ok(!body.includes('token=private'))
})

test('non-course pages work and feedback remains plain Markdown, including Unicode and newlines', () => {
  const wiki = captureFeedbackContext({ pageTitle: 'Wiki', href: 'https://example.org/StudyHub/wiki/#khai-niem' })
  const url = new URL(buildFeedbackIssueUrl({ category: 'suggestion', description: 'Dòng 1\nDòng 2: <script>alert(1)</script>', context: wiki }))
  assert.ok(url.searchParams.get('body').includes('Dòng 1\nDòng 2: <script>alert(1)</script>'))
  assert.ok(!url.searchParams.get('body').includes('Môn học:'))
})

test('invalid or excessively long reports never produce a broken GitHub URL', () => {
  const report = { category: 'display', description: 'Lỗi hiển thị', context }
  assert.throws(() => buildFeedbackIssueUrl({ ...report, description: '   ' }))
  assert.throws(() => buildFeedbackIssueUrl({ ...report, category: 'unknown' }))
  assert.throws(() => buildFeedbackIssueUrl({ ...report, description: 'a'.repeat(1001) }))
  assert.throws(() => buildFeedbackIssueUrl({ ...report, description: 'ắ'.repeat(1000) }), /quá dài/)
  assert.throws(() => captureFeedbackContext({ href: 'javascript:alert(1)' }))
})

test('feedback is posted as JSON with page context, optional contact and service key', async () => {
  const calls = []
  const fetchImpl = async (url, init) => { calls.push({ url, init }); return { ok: true, json: async () => ({ success: true }) } }
  await sendFeedback({ category: 'display', description: '  Nút bị lệch  ', contact: 'sv@uet.vn', context, endpoint: 'https://forms.example/submit', accessKey: 'k1', fetchImpl })
  assert.equal(calls.length, 1)
  assert.equal(calls[0].url, 'https://forms.example/submit')
  const payload = JSON.parse(calls[0].init.body)
  assert.equal(payload.message, 'Nút bị lệch')
  assert.equal(payload.contact, 'sv@uet.vn')
  assert.equal(payload.access_key, 'k1')
  assert.equal(payload.page_title, 'Đạo hàm & gradient')
  assert.ok(!payload.page_url.includes('token=private'))
})

test('readers may leave out the page; failed or rejected requests surface a readable error', async () => {
  const ok = []
  await sendFeedback({ category: 'suggestion', description: 'Ý chung', context, includePage: false, endpoint: 'https://f', fetchImpl: async (u, i) => { ok.push(JSON.parse(i.body)); return { ok: true, json: async () => { throw new Error('empty') } } } })
  assert.equal(ok[0].page_url, undefined)
  assert.match(ok[0].subject, /Góp ý chung/)
  await assert.rejects(sendFeedback({ category: 'content', description: 'x', context, endpoint: 'https://f', fetchImpl: async () => ({ ok: false, json: async () => ({}) }) }), /từ chối/)
  await assert.rejects(sendFeedback({ category: 'content', description: 'x', context, endpoint: 'https://f', fetchImpl: async () => ({ ok: true, json: async () => ({ success: false }) }) }), /từ chối/)
  await assert.rejects(sendFeedback({ category: 'content', description: 'x', context, endpoint: 'https://f', fetchImpl: async () => { throw new TypeError('Failed to fetch') } }), /Không kết nối/)
  await assert.rejects(sendFeedback({ category: 'content', description: 'x', context, endpoint: '' }), /chưa được cấu hình/)
})

test('the copyable text keeps the message, page and contact', () => {
  const text = formatFeedbackText({ category: 'content', description: 'Sai dấu', contact: 'Zalo 09', context })
  for (const expected of ['Nội dung sai hoặc khó hiểu', 'Sai dấu', 'Đạo hàm & gradient', 'Liên hệ: Zalo 09']) assert.ok(text.includes(expected))
  assert.ok(!formatFeedbackText({ category: 'content', description: 'Sai dấu', context, includePage: false }).includes('Đường dẫn'))
})
