import test from 'node:test'
import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'
import {assertCodePreserved, htmlCodeText} from '../build/exam-code-integrity.mjs'

const md = new MarkdownIt()
test('Source comparison rejects commas inserted into strings, operators and outputs', () => {
  for (const [source, corrupt] of [
    ['`[("A",8),("C",6)]`', '`[(",A",,8),(",C",,6)]`'],
    ['`[g / 1000 for g in gam if g is not None and g >= 0]`', '`[g / 1000 for g in gam if g is not None and g >,= 0]`'],
    ['```text\n[(\'A\', 8), (\'C\', 6)]\n```', '```text\n[(\'A\', 8), (\'C\', 6)]^M\n```']
  ]) {
    assert.doesNotThrow(() => assertCodePreserved(source, md.render(source), 'valid'))
    assert.throws(() => assertCodePreserved(source, md.render(corrupt), 'corrupt'))
  }
})
test('Entity decoding preserves regex escapes and source comparison permits additional prose identifiers', () => {
  assert.equal(htmlCodeText('r&quot;\\.\\s+&lt;=&amp;&quot;'), 'r"\\.\\s+<=&"')
  assertCodePreserved('Dùng `r"\\d+"`.', md.render('Gọi `re` với `r"\\d+"`.'), 'regex')
})
test('Rejects damaged HTML entities even in prose without code delimiters', () => {
  assert.throws(() => assertCodePreserved('So sánh.', '<p>Giá &gt,= 0</p>', 'entity'))
  assert.throws(() => assertCodePreserved('Chuỗi.', '<p>&quot,A&quot,</p>', 'quote'))
  assertCodePreserved('HTML.', '<p>Ký tự &lt; và &gt;.</p>', 'valid entities')
})
