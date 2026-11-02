import test from 'node:test'
import assert from 'node:assert/strict'
import { mergeStylesheets, linkedStylesheets, replaceStylesheetLinks } from '../build/shared-styles.mjs'

test('batch CSS union retains every page style and includes common rules once', () => {
  const common = '@font-face{font-family:Study;src:url(./study.woff2)}.theme{color:purple}'
  const a = '.practice-test-list[data-v-a]{display:grid;border:1px solid purple}'
  const b = '.exam-practice[data-v-b]{max-width:860px}'
  const media = '@media(max-width:600px){.practice-test-list[data-v-a]{grid-template-columns:1fr}}'
  const keyframes = '@keyframes spin{to{transform:rotate(360deg)}}'
  const css = mergeStylesheets([common + a + media + keyframes, common + b + keyframes])
  assert.equal(css, common + a + media + keyframes + b)
  assert.equal(css.match(/font-family:Study/g).length, 1)
})

test('CSS parsing preserves quoted braces, data URLs and the original within-sheet cascade', () => {
  const sheet = '.a{color:red}.a{color:blue}.a{color:red}.icon::after{content:"}";background:url("data:image/svg+xml,%3Csvg%3E%7B%3C/svg%3E")}'
  assert.equal(mergeStylesheets([sheet, sheet]), sheet)
  assert.throws(() => mergeStylesheets(['.broken{']), /Unclosed/)
})

test('stylesheet discovery and replacement preserve deployment base, attributes and unrelated links', () => {
  const html = '<link rel="preload stylesheet" href="/StudyHub/assets/style.a.css" as="style"><link rel="modulepreload" href="/StudyHub/assets/app.js"><link href="/StudyHub/vp-icons.css" rel="stylesheet">'
  assert.deepEqual(linkedStylesheets(html, ['assets/style.a.css', 'assets/style.b.css']), ['assets/style.a.css'])
  assert.equal(replaceStylesheetLinks(html, ['assets/style.a.css'], 'assets/style-shared.hash.css'), html.replace('style.a.css', 'style-shared.hash.css'))
})
