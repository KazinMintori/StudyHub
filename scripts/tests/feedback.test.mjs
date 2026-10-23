import test from 'node:test'
import assert from 'node:assert/strict'
import { captureFeedbackContext, buildFeedbackIssueUrl } from '../../src/features/site/services/feedback.mjs'

const context = captureFeedbackContext({
  pageTitle: 'Đạo hàm & gradient',
  courseName: 'Cơ sở toán học cho AI',
  href: 'https://KazinMintori.github.io/StudyHub/toan-cho-ai/bai-giang/dao-ham.html?token=private#slides'
})

test('feedback automatically includes the lesson, course, base path and current tab without query data', () => {
  const url = new URL(buildFeedbackIssueUrl({ category: 'content', description: 'Thiếu dấu trừ & ký hiệu # ở mục 2.', context }))
  assert.equal(url.origin + url.pathname, 'https://github.com/KazinMintori/StudyHub/issues/new')
  assert.equal(url.searchParams.get('title'), '[Lỗi nội dung bài học] Đạo hàm & gradient')
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
