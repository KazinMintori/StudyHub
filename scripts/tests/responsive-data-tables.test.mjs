import test from 'node:test'
import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'
import { responsiveTablesPlugin } from '../build/responsive-tables.mjs'

const render = text => new MarkdownIt().use(responsiveTablesPlugin).render(text)

test('lab table cells retain plain and code header labels for mobile cards', () => {
  const html = render('| Chỉ số | `price` |\n| --- | --- |\n| Trung vị | 45000 |\n| Số dòng | 6 |')
  assert.match(html, /<th scope="col">Chỉ số<\/th>/)
  assert.equal((html.match(/data-label="Chỉ số"/g) || []).length, 2)
  assert.equal((html.match(/data-label="price"/g) || []).length, 2)
  assert.match(html, /class="study-data-table"/)
})

test('labels reset between tables and attributes remain escaped', () => {
  const html = render('| **Giá** | A & B |\n| --- | --- |\n| 1 | 2 |\n\n| Mới |\n| --- |\n| 3 |')
  assert.match(html, /data-label="Giá"/)
  assert.match(html, /data-label="A &amp; B"/)
  assert.match(html, /data-label="Mới"/)
  assert.equal((html.match(/data-label="Giá"/g) || []).length, 1)
})

test('ordinary paragraphs and code blocks are untouched', () => {
  const html = render('Một đoạn văn.\n\n```text\n| A | B |\n```')
  assert.doesNotMatch(html, /data-label|study-data-table/)
})

test('preserves responsive attributes with the VitePress fixed table renderer', () => {
  const md = new MarkdownIt()
  md.renderer.rules.table_open = () => '<table tabindex="0">\n'
  md.use(responsiveTablesPlugin)
  const html = md.render('| Cột |\n| --- |\n| Giá trị |')
  assert.match(html, /<table[^>]*class="study-data-table"[^>]*tabindex="0"/)
  assert.match(html, /data-label="Cột"/)
})
