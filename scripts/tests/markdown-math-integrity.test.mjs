import assert from 'node:assert/strict'
import { readdir, readFile } from 'node:fs/promises'
import { relative } from 'node:path'
import { fileURLToPath } from 'node:url'
import test from 'node:test'
import { createMarkdownRenderer } from 'vitepress'
import config from '../../docs/.vitepress/config.mjs'

const docs = fileURLToPath(new URL('../../docs/', import.meta.url))
const md = await createMarkdownRenderer(docs, config.markdown)
const affectedPages = [
  'discrete-math/bai-tap.md',
  'toan-cho-ai/bai-giang/bai-00-on-tap-nen-tang.md',
  'toan-cho-ai/bai-giang/bai-03-doi-ngau-lagrange.md',
  'toan-cho-ai/bai-giang/bai-04-gradient-newton/phuong-phap-primal-dual.md',
  'giai-thuat-du-lieu/bai-tap.md',
  'toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.md',
  'toan-cho-ai/bai-giang/bai-02-tap-loi.md',
  'toan-cho-ai/bai-giang/bai-04-gradient-newton.md',
  'toan-cho-ai/bai-giang/bai-05-toi-uu-huan-luyen.md',
  'toan-cho-ai/bai-giang/bai-06-phuong-phap-thich-nghi.md',
  'toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/hai-lop-bai-toan-kinh-dien.md',
  'toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/non-loi.md',
  'toan-cho-ai/bai-giang/bai-02-tap-loi/bai-toan-dinh-vi-va-mang-luoi.md',
  'toan-cho-ai/bai-giang/bai-02-tap-loi/can-chebyshev-va-chernoff.md',
  'toan-cho-ai/bai-giang/bai-02-tap-loi/ellipsoid-cuc-tri-va-tam-hinh-hoc.md',
  'toan-cho-ai/bai-giang/bai-02-tap-loi/khop-ham-va-noi-suy.md',
  'toan-cho-ai/bai-giang/bai-02-tap-loi/quy-hoach-mat-bang.md',
  'toan-cho-ai/bai-giang/bai-02-tap-loi/uoc-luong-phi-tham-so-va-kiem-dinh.md',
  'toan-cho-ai/bai-giang/bai-04-gradient-newton/do-phuc-tap-va-bat-dang-thuc-tong-quat.md'
]
const mathError = /data-mjx-error|data-mml-node=(?:&quot;|["'])merror|<merror\b/

function* mathTokens(tokens) {
  for (const token of tokens) {
    if (token.type === 'math_block' || token.type === 'math_inline') yield token
    if (token.children) yield* mathTokens(token.children)
  }
}

function swallowedMarkdown(token) {
  // Inspect the real parser output. Counting source delimiters alone misses a
  // list whose opening delimiter is indented but whose body escapes the list.
  const content = token.content
  return (token.type === 'math_block' && !content.trim())
    || /(?:^|\n)\s*#{1,6}\s+\S/.test(content)
    || /(?:^|\n)\s*:::(?:\s|$)/.test(content)
    || /(?:^|\n)\s*\$\$\s*(?:\n|$)/.test(content)
    // A bare prose line cannot be TeX. Text inside \text{...}, commands,
    // variables with operators and escaped \# remain valid math here.
    || content.split('\n').some(line => {
      const text = line.trim()
      return /^\p{L}[\p{L}\t ,.!?():;\-]{18,}$/u.test(text)
        && /\p{Ll}/u.test(text)
        && /(?:\p{L}{2,}[ \t]+){2,}\p{L}{2,}/u.test(text)
    })
}

async function* markdownFiles(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if (['.vitepress', 'public', 'agy-plans'].includes(entry.name)) continue
    const path = `${directory}/${entry.name}`
    if (entry.isDirectory()) yield* markdownFiles(path)
    else if (entry.name.endsWith('.md')) yield path
  }
}

test('the integrity check detects list math swallowing headings and prose', () => {
  const broken = [
    '1. Tính giá trị:',
    '   $$',
    'x = 1',
    '$$',
    '',
    '## Phần tiếp theo',
    '',
    'Đây là đoạn văn phải nằm ngoài công thức.',
    '',
    '$$',
    'y = 2',
    '$$'
  ].join('\n')
  const tokens = md.parse(broken, {})
  const invalid = [...mathTokens(tokens)].filter(swallowedMarkdown)
  assert(invalid.some(token => token.content.includes('## Phần tiếp theo')))
  assert(invalid.some(token => token.content.includes('Đây là đoạn văn')))
  assert.match(md.render(broken, {}), mathError)
  assert(swallowedMarkdown({ content: 'Đây là đoạn văn phải nằm ngoài công thức.' }))
})

test('consistent list indentation preserves math, the next heading and prose', () => {
  for (const indentation of ['   ', '     ']) {
    const source = [
      '1. Tính giá trị:',
      ...(indentation.length === 5 ? ['   - Xét biểu thức:'] : []),
      `${indentation}$$`,
      `${indentation}x = 1`,
      `${indentation}$$`,
      '',
      '## Phần tiếp theo',
      '',
      'Đây là đoạn văn phải nằm ngoài công thức.',
      '',
      '$$',
      'y = 2',
      '$$'
    ].join('\n')
    const tokens = md.parse(source, {})
    assert.equal([...mathTokens(tokens)].length, 2)
    assert(![...mathTokens(tokens)].some(swallowedMarkdown))
    const html = md.render(source, {})
    assert.doesNotMatch(html, mathError)
    assert.match(html, /<h2\b[^>]*>Phần tiếp theo/)
    assert.match(html, /<p>Đây là đoạn văn phải nằm ngoài công thức\.<\/p>/)
  }
})

test('literal Markdown in code and legitimate TeX text are not flagged', () => {
  const source = [
    '```markdown',
    '1. Tính giá trị:',
    '   $$',
    'x = 1',
    '$$',
    '## Phần tiếp theo',
    '```',
    '',
    '$$',
    '\\text{Đây là chú thích ngắn.} \\quad x = 1',
    '$$',
    '',
    '$CRA, CAR, ARC, ACR, RAC, RCA$'
  ].join('\n')
  const tokens = md.parse(source, {})
  assert.equal([...mathTokens(tokens)].length, 2)
  assert(![...mathTokens(tokens)].some(swallowedMarkdown))
  assert.doesNotMatch(md.render(source, {}), mathError)
})

test('no published Markdown page swallows headings or prose into math', async t => {
  const issues = []
  let pageCount = 0
  for await (const file of markdownFiles(docs)) {
    pageCount++
    const relativePath = relative(docs, file).replaceAll('\\', '/')
    const env = { path: file, relativePath }
    const tokens = md.parse(await readFile(file, 'utf8'), env)
    for (const token of mathTokens(tokens)) {
      if (!swallowedMarkdown(token)) continue
      const html = md.renderer.render([token], md.options, env)
      issues.push(`${relativePath}:${(token.map?.[0] ?? 0) + 1}: ${mathError.test(html) ? 'MathJax error and ' : ''}Markdown inside ${token.type}`)
    }
  }
  assert(pageCount > 1000, 'The regression check must cover the full published Markdown tree')
  t.diagnostic(`Parsed ${pageCount} published Markdown pages with the VitePress configuration`)
  assert.deepEqual(issues, [])
})

for (const page of affectedPages) {
  test(`the repaired page renders without MathJax errors: ${page}`, async () => {
    const source = await readFile(`${docs}/${page}`, 'utf8')
    const html = md.render(source, { path: `${docs}/${page}`, relativePath: page })
    assert.doesNotMatch(html, mathError)
  })
}
