import test from 'node:test'
import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'
import { examProsePlugin } from '../build/exam-prose.mjs'

const md = new MarkdownIt().use(examProsePlugin)
test('Capitalizes Vietnamese prose after colons, including bold labels and quotes', () => {
  const html = md.render('**A sai:** nhầm phép nhân. Ví dụ: “giá hợp lệ”.\n\n- Kết luận: đúng.')
  assert(html.includes('</strong> Nhầm'))
  assert(html.includes('Ví dụ: “Giá hợp lệ”'))
  assert(html.includes('Kết luận: Đúng.'))
})
test('Preserves exact code, URLs and case-sensitive Python identifiers', () => {
  const html = md.render('Output: nan. Giá trị: np.nan. Mã: `print("a: nhỏ")`\n\n```python\nx = {"a": "nhỏ"}\n```\n\nhttps://example.com/a:b')
  assert(html.includes('Output: <code>nan</code>.'))
  assert(html.includes('<code>np.nan</code>.'))
  assert(html.includes('print(&quot;a: nhỏ&quot;)'))
  assert(html.includes('x = {&quot;a&quot;: &quot;nhỏ&quot;}'))
  assert(html.includes('https://example.com/a:b'))
})
test('Treats quoted program data after a colon as literal code, preserving its case', () => {
  assert(md.render("Dữ liệu: 'wifi'.").includes("<code>'wifi'</code>"))
})
