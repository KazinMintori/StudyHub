import assert from 'node:assert/strict'
import test from 'node:test'
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import { TeXFont } from 'mathjax-full/js/output/svg/fonts/tex.js'
import { createVietnameseMathFont, vietnameseMathOptions } from '../math-fonts/vietnamese.mjs'
import { renderMathInStrings, mathTextPlugin } from '../math-text-plugin.mjs'

const vietnamese = 'àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ'
const md = new MarkdownIt().use(mathjax, vietnameseMathOptions)
const expression = String.raw`$P(\text{một chuỗi})=p^k(1-p)^{n-k}$`

test('Vietnamese text uses measured SVG paths, not per-letter browser fallbacks', () => {
  for (const command of ['text', 'mathrm', 'mathbf', 'mathit']) {
    const html = md.renderInline(`$\\${command}{${vietnamese + vietnamese.toUpperCase()}}$`)
    assert.doesNotMatch(html, /<text\b|data-mjx-error|merror/)
    assert.match(html, /data-c="1ED9"/)
    assert.match(html, /data-c="1ED7"/)
  }
})

test('the reported probability formula retains its superscripts and readable label', () => {
  const html = md.renderInline(expression)
  assert.doesNotMatch(html, /<text\b/)
  assert.match(html, /data-mml-node="msup"/)
  assert.match(html, /<mtext>một chuỗi<\/mtext>/)
})

test('missing glyphs keep real widths and distinct normal, italic and bold outlines', () => {
  const font = createVietnameseMathFont()
  const variants = ['normal', 'italic', 'bold', 'bold-italic']
  const chars = variants.map(variant => font.getChar(variant, 'ộ'.codePointAt(0)))
  for (const char of chars) {
    assert(char[0] > 0 && char[1] >= 0 && char[2] > 0)
    assert(char[3].p && !char[3].unknown)
  }
  assert.equal(new Set(chars.map(char => char[3].p)).size, 4)
  const original = new TeXFont()
  for (const variant of variants) for (const char of 'APxyz0123+-=') {
    assert.deepEqual(font.getChar(variant, char.codePointAt(0)), original.getChar(variant, char.codePointAt(0)))
  }
})

test('slide, cheatsheet and generated catalog renderers use the same Vietnamese glyphs', () => {
  const html = renderMathInStrings([expression])[expression]
  assert.doesNotMatch(html, /<text\b/)
  assert.match(html, /<mtext>một chuỗi<\/mtext>/)
  const result = mathTextPlugin().transform(`export const value=${JSON.stringify(expression)}`, '/course-catalog.mjs')
  assert(result?.code.includes('studyRenderedMath'))
  assert.doesNotMatch(result.code, /<text\b/)
})
