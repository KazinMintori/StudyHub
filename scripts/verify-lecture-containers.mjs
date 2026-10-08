import assert from 'node:assert/strict'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import config from '../docs/.vitepress/config.mjs'

const md = await createMarkdownRenderer(fileURLToPath(new URL('../docs/', import.meta.url)), config.markdown)
const containers = [
  ['example', 'Ví dụ', 'info'],
  ['exercise', 'Bài tập', 'warning'],
  ['hint', 'Gợi ý', 'tip'],
  ['solution', 'Lời giải', 'details'],
  ['proof', 'Chứng minh', 'details'],
  ['derivation', 'Khai triển chi tiết', 'details']
]

let checks = 0
for (const [type, label, target] of containers) {
  for (const newline of ['\n', '\r\n']) {
    for (const title of ['', 'Tiêu đề riêng']) {
      const marker = 'Nội dung đầu tiên phải nằm trong phần thân.'
      const source = [`::: ${type}${title ? ` ${title}` : ''}`, marker, ':::', ''].join(newline)
      const html = md.render(source)
      const expected = `${label}${title ? `: ${title}` : ''}`
      assert(html.includes(target === 'details' ? `<summary>${expected}</summary>` : `<p class="custom-block-title">${expected}</p>`), `${type}: title`)
      assert(html.includes(`<p>${marker}</p>`), `${type}: first paragraph`)
      checks++
    }
  }
}

const solution = md.render('::: solution\n1. Đáp án đầu tiên.\n2. Đáp án thứ hai.\n:::\n')
assert(solution.includes('<summary>Lời giải</summary>'))
assert(solution.includes('<li>Đáp án đầu tiên.</li>'))
assert(solution.includes('<li>Đáp án thứ hai.</li>'))
assert(!solution.includes('<details open'))
console.log(`PASS ${checks} container cases; numbered answers stay inside the collapsed solution.`)
