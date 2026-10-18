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
      if (type === 'exercise') {
        assert(html.includes('<div class="warning custom-block exercise">'), 'exercise: semantic class')
      }
      checks++
    }
  }
}

// Focused exercise title normalization tests
const normalizationCases = [
  ['Bài tập1: Đọc bảng giá', 'Bài tập 1: Đọc bảng giá'],
  ['Bài tập 1: Đọc bảng giá', 'Bài tập 1: Đọc bảng giá'],
  ['Bài 1: Đọc bảng giá', 'Bài 1: Đọc bảng giá' ? 'Bài tập 1: Đọc bảng giá' : ''],
  ['Bài 1.2.1: Thay đổi quy mô', 'Bài tập 1.2.1: Thay đổi quy mô'],
  ['1. Nhận diện bốn thành phần', 'Bài tập 1: Nhận diện bốn thành phần'],
  ['1: Nhận diện bốn thành phần', 'Bài tập 1: Nhận diện bốn thành phần'],
  ['1', 'Bài tập 1'],
  ['Bài 1', 'Bài tập 1'],
  ['Bài tập 1', 'Bài tập 1']
]

for (const [inputTitle, expectedTitle] of normalizationCases) {
  for (const newline of ['\n', '\r\n']) {
    const source = [`::: exercise ${inputTitle}`, 'Nội dung bài tập.', ':::', ''].join(newline)
    const html = md.render(source)
    assert(html.includes('<div class="warning custom-block exercise">'), `exercise class for "${inputTitle}"`)
    assert(html.includes(`<p class="custom-block-title">${expectedTitle}</p>`), `normalized title for "${inputTitle}" -> "${expectedTitle}"`)
    assert(!html.includes('Bài tập: Bài tập'), `no duplicate "Bài tập: Bài tập" for "${inputTitle}"`)
    assert(!html.includes('Bài tập: Bài 1'), `no duplicate "Bài tập: Bài 1" for "${inputTitle}"`)
    assert(!html.includes('::'), `no double colons for "${inputTitle}"`)
    checks++
  }
}

// External exercise heading and span anchor preservation (avoid repeated title)
for (const newline of ['\n', '\r\n']) {
  const labSource = [
    '## Bài 1: Đọc tệp bảng lớn có chọn lọc với tham số cột và ngày giờ',
    '',
    '<span id="data-lab-06-01"></span>',
    '',
    '::: exercise',
    'Nội dung phòng lab cần thực hiện.',
    ':::',
    ''
  ].join(newline)
  const labHtml = md.render(labSource)
  assert(labHtml.includes('<h2 id=') && labHtml.includes('Bài 1: Đọc tệp bảng lớn có chọn lọc với tham số cột và ngày giờ'), 'external heading rendered')
  assert(labHtml.includes('<span id="data-lab-06-01"></span>'), 'span anchor preserved')
  assert(labHtml.includes('<div class="warning custom-block exercise">'), 'exercise semantic class in lab')
  assert(!labHtml.includes('<p class="custom-block-title">'), 'avoid repeated title when external heading names it')
  assert(labHtml.includes('<p>Nội dung phòng lab cần thực hiện.</p>'), 'lab exercise content preserved')
  checks++
}

// Subject-only exercise under numbered heading
for (const newline of ['\n', '\r\n']) {
  const subSource = [
    '## 1. Bài tập mục tiêu bậc ba',
    '',
    '::: exercise Lập hệ KKT và tìm nghiệm toàn cục',
    'Nội dung tìm nghiệm.',
    ':::',
    ''
  ].join(newline)
  const subHtml = md.render(subSource)
  assert(subHtml.includes('<p class="custom-block-title">Bài tập 1: Lập hệ KKT và tìm nghiệm toàn cục</p>'), 'subject-only under numbered heading')
  assert(subHtml.includes('<div class="warning custom-block exercise">'), 'exercise class')
  checks++
}

// Subject-only exercise under non-exercise heading (keeps descriptive title)
for (const newline of ['\n', '\r\n']) {
  const nonExSource = [
    '### Thuật toán xét mọi cặp và tính đúng',
    '',
    '::: exercise Tự kiểm đặc tả',
    'Nếu vòng trong bắt đầu từ j=1...',
    ':::',
    ''
  ].join(newline)
  const nonExHtml = md.render(nonExSource)
  assert(nonExHtml.includes('<p class="custom-block-title">Bài tập: Tự kiểm đặc tả</p>'), 'subject-only under non-exercise heading')
  assert(nonExHtml.includes('<div class="warning custom-block exercise">'), 'exercise class')
  checks++
}

// Unaffected ordinary warnings: must retain warning custom-block WITHOUT exercise class
for (const newline of ['\n', '\r\n']) {
  const warnSource = ['::: warning Cảnh báo quan trọng', 'Nội dung cảnh báo không bị ảnh hưởng.', ':::', ''].join(newline)
  const warnHtml = md.render(warnSource)
  assert(warnHtml.includes('<div class="warning custom-block">'), 'ordinary warning retains custom-block')
  assert(!warnHtml.includes('exercise'), 'ordinary warning must not have exercise class')
  assert(warnHtml.includes('<p class="custom-block-title">Cảnh báo quan trọng</p>'), 'ordinary warning title intact')
  checks++
}

const solution = md.render('::: solution\n1. Đáp án đầu tiên.\n2. Đáp án thứ hai.\n:::\n')
assert(solution.includes('<summary>Lời giải</summary>'))
assert(solution.includes('<li>Đáp án đầu tiên.</li>'))
assert(solution.includes('<li>Đáp án thứ hai.</li>'))
assert(!solution.includes('<details open'))
console.log(`PASS ${checks} container cases; numbered answers stay inside the collapsed solution.`)
