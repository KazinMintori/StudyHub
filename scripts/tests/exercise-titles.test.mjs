import assert from 'node:assert/strict'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import config from '../../docs/.vitepress/config.mjs'
import {
  isSectionHeading,
  parseExerciseHeading,
  normalizeExerciseTitle,
  normalizeExerciseContainers
} from '../build/exercise-containers.mjs'

// 1. Unit Tests: isSectionHeading
assert.equal(isSectionHeading('Bài tập rèn luyện'), true)
assert.equal(isSectionHeading('Hệ thống bài tập rèn luyện'), true)
assert.equal(isSectionHeading('5. Bài tập rèn luyện'), true) // section heading containing multiple exercises
assert.equal(isSectionHeading('Bài tập tự luyện'), true)
assert.equal(isSectionHeading('Bài 1: Đọc tệp bảng lớn'), false)
assert.equal(isSectionHeading('Phần 1: Giới thiệu'), true)

// 2. Unit Tests: parseExerciseHeading
assert.deepEqual(parseExerciseHeading('Bài 1: Đọc tệp bảng lớn'), { number: '1', subject: 'Đọc tệp bảng lớn' })
assert.deepEqual(parseExerciseHeading('### Bài 1.2.1: Thay đổi quy mô dữ liệu'), { number: '1.2.1', subject: 'Thay đổi quy mô dữ liệu' })
assert.deepEqual(parseExerciseHeading('## Bài tập 2: Chuẩn hóa vector'), { number: '2', subject: 'Chuẩn hóa vector' })
assert.deepEqual(parseExerciseHeading('## 1. Bài tập mục tiêu bậc ba'), { number: '1', subject: 'mục tiêu bậc ba' })
assert.equal(parseExerciseHeading('## Bài tập rèn luyện'), null)

// 3. Unit Tests: normalizeExerciseTitle
// Explicit numbering
assert.equal(normalizeExerciseTitle('Bài tập1: Đọc bảng giá'), 'Bài tập 1: Đọc bảng giá')
assert.equal(normalizeExerciseTitle('Bài tập 1: Đọc bảng giá'), 'Bài tập 1: Đọc bảng giá')
assert.equal(normalizeExerciseTitle('Bài tập: Bài tập 1: Đọc bảng giá'), 'Bài tập 1: Đọc bảng giá')
assert.equal(normalizeExerciseTitle('Bài 1: Đọc bảng giá'), 'Bài tập 1: Đọc bảng giá')
assert.equal(normalizeExerciseTitle('Bài 1.2.1: Thay đổi quy mô'), 'Bài tập 1.2.1: Thay đổi quy mô')
assert.equal(normalizeExerciseTitle('1. Nhận diện bốn thành phần'), 'Bài tập 1: Nhận diện bốn thành phần')
assert.equal(normalizeExerciseTitle('1: Nhận diện bốn thành phần'), 'Bài tập 1: Nhận diện bốn thành phần')
assert.equal(normalizeExerciseTitle('1'), 'Bài tập 1')
assert.equal(normalizeExerciseTitle('Bài 1'), 'Bài tập 1')
assert.equal(normalizeExerciseTitle('Bài tập 1'), 'Bài tập 1')
for (const fence of ['```', '~~~~']) {
  const example = `${fence}markdown\n::: exercise Bài tập 1: Mã minh họa\n:::\n${fence}`
  assert.equal(normalizeExerciseContainers(example), example, 'exercise syntax inside code stays literal')
}
const headingWithCode = '## Bài 1: Đọc bảng\n```python\n# Bài 99: Chỉ là chú thích\n```\n::: exercise\nĐề bài\n:::'
assert(normalizeExerciseContainers(headingWithCode).includes('::: warning exercise-notitle'), 'code comments do not replace the exercise heading')

// Bare container: with and without active external exercise heading
assert.equal(normalizeExerciseTitle('', { number: '1', subject: 'Đọc bảng' }), null) // avoids repeating title
assert.equal(normalizeExerciseTitle('', null), 'Bài tập')

// Subject-only container: with and without active heading
assert.equal(
  normalizeExerciseTitle('Lập hệ KKT và tìm nghiệm toàn cục', { number: '1', subject: 'Mục tiêu bậc ba' }),
  'Bài tập 1: Lập hệ KKT và tìm nghiệm toàn cục'
)
assert.equal(
  normalizeExerciseTitle('Tự kiểm đặc tả', null),
  'Bài tập: Tự kiểm đặc tả'
)
// Important edge case: "Bài toán" must NOT have "Bài" stripped
assert.equal(
  normalizeExerciseTitle('Bài toán phân bổ cảm biến định vị', null),
  'Bài tập: Bài toán phân bổ cảm biến định vị'
)

// 4. Integration Tests with VitePress Markdown Renderer
const md = await createMarkdownRenderer(fileURLToPath(new URL('../../docs/', import.meta.url)), config.markdown)

const testCases = [
  {
    name: 'Explicit "Bài tập1: ..."',
    input: '::: exercise Bài tập1: Đọc bảng giá\nNội dung bài tập 1.\n:::',
    expectClass: 'warning custom-block exercise',
    expectTitle: 'Bài tập 1: Đọc bảng giá',
    forbidTitle: 'Bài tập: Bài tập',
  },
  {
    name: 'Explicit "Bài tập 1: ..."',
    input: '::: exercise Bài tập 1: Đọc bảng giá\nNội dung bài tập 1.\n:::',
    expectClass: 'warning custom-block exercise',
    expectTitle: 'Bài tập 1: Đọc bảng giá',
    forbidTitle: 'Bài tập: Bài tập',
  },
  {
    name: 'Explicit "Bài 1: ..."',
    input: '::: exercise Bài 1: Đọc bảng giá\nNội dung bài 1.\n:::',
    expectClass: 'warning custom-block exercise',
    expectTitle: 'Bài tập 1: Đọc bảng giá',
    forbidTitle: 'Bài tập: Bài 1',
  },
  {
    name: 'Explicit "1. ..."',
    input: '::: exercise 1. Nhận diện bốn thành phần\nNội dung bài 1.\n:::',
    expectClass: 'warning custom-block exercise',
    expectTitle: 'Bài tập 1: Nhận diện bốn thành phần',
    forbidTitle: 'Bài tập: 1.',
  },
  {
    name: 'Bare container without heading',
    input: '::: exercise\nNội dung bài tập độc lập.\n:::',
    expectClass: 'warning custom-block exercise',
    expectTitle: 'Bài tập',
  },
  {
    name: 'Subject-only container without heading',
    input: '::: exercise Tự kiểm đặc tả\nNội dung tự kiểm.\n:::',
    expectClass: 'warning custom-block exercise',
    expectTitle: 'Bài tập: Tự kiểm đặc tả',
  },
  {
    name: 'Subject-only preserving "Bài toán"',
    input: '::: exercise Bài toán phân bổ cảm biến định vị\nNội dung bài toán.\n:::',
    expectClass: 'warning custom-block exercise',
    expectTitle: 'Bài tập: Bài toán phân bổ cảm biến định vị',
  }
]

for (const tc of testCases) {
  for (const newline of ['\n', '\r\n']) {
    const src = tc.input.replace(/\n/g, newline)
    const html = md.render(src)
    assert(html.includes(`<div class="${tc.expectClass}">`), `${tc.name} (${newline === '\n' ? 'LF' : 'CRLF'}): class match`)
    assert(html.includes(`<p class="custom-block-title">${tc.expectTitle}</p>`), `${tc.name} (${newline === '\n' ? 'LF' : 'CRLF'}): title match`)
    if (tc.forbidTitle) {
      assert(!html.includes(tc.forbidTitle), `${tc.name}: forbidden title check`)
    }
  }
}

// 5. External Exercise Heading + Span Anchor Preservation
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
  assert(labHtml.includes('<h2 id=') && labHtml.includes('Bài 1: Đọc tệp bảng lớn có chọn lọc với tham số cột và ngày giờ'), 'external heading preserved')
  assert(labHtml.includes('<span id="data-lab-06-01"></span>'), 'span anchor preserved')
  assert(labHtml.includes('<div class="warning custom-block exercise">'), 'exercise semantic class in lab')
  assert(!labHtml.includes('<p class="custom-block-title">'), 'no repeated title inside container when external heading names it')
  assert(labHtml.includes('<p>Nội dung phòng lab cần thực hiện.</p>'), 'content preserved')
}

// 6. Subject-only exercise under numbered heading
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
}

// 7. Ordinary Warning Isolation (MUST NOT have exercise class)
for (const newline of ['\n', '\r\n']) {
  const warnSource = [
    '::: warning Cảnh báo quan trọng',
    'Nội dung cảnh báo không bị ảnh hưởng.',
    ':::',
    ''
  ].join(newline)
  const warnHtml = md.render(warnSource)
  assert(warnHtml.includes('<div class="warning custom-block">'), 'ordinary warning retains standard custom-block')
  assert(!warnHtml.includes('exercise'), 'ordinary warning must not have exercise class')
  assert(warnHtml.includes('<p class="custom-block-title">Cảnh báo quan trọng</p>'), 'ordinary warning title intact')
}

// 8. Other Custom Blocks (tip, details, proof, solution)
const mixedSource = [
  '::: tip Mẹo tính toán',
  'Gợi ý nhanh.',
  ':::',
  '',
  '::: proof',
  'Chứng minh định lý.',
  ':::',
  '',
  '::: solution',
  '1. Bước một.',
  '2. Bước hai.',
  ':::'
].join('\n')
const mixedHtml = md.render(mixedSource)
assert(mixedHtml.includes('<div class="tip custom-block">'), 'tip block intact')
assert(mixedHtml.includes('<summary>Chứng minh</summary>'), 'proof block intact')
assert(mixedHtml.includes('<summary>Lời giải</summary>'), 'solution block intact')
assert(mixedHtml.includes('<li>Bước một.</li>'), 'solution list intact')

console.log('ALL EXERCISE TITLE & CONTAINER TESTS PASSED SUCCESSFULLY!')
