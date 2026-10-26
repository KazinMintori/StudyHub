import test from 'node:test'
import assert from 'node:assert/strict'
import { pagePath } from '../../src/core/routing/page-path.mjs'

test('course workspace links add the extension before the query and keep their tab', () => {
  assert.equal(pagePath('/goc-hoc-tap?mon=toan-cho-ai#notes'), '/goc-hoc-tap.html?mon=toan-cho-ai#notes')
  assert.equal(pagePath('/goc-hoc-tap.html?mon=dsa#plan'), '/goc-hoc-tap.html?mon=dsa#plan')
  assert.equal(pagePath('/goc-hoc-tap?mon=vat-ly-2&from=lesson#simulation'), '/goc-hoc-tap.html?mon=vat-ly-2&from=lesson#simulation')
})
test('existing directory, page, fragment and asset destinations keep their shape', () => {
  for (const [source, expected] of [
    ['/', '/'], ['/wiki/', '/wiki/'], ['/wiki/gradient#definition', '/wiki/gradient.html#definition'],
    ['/lecture.html#notes', '/lecture.html#notes'], ['/diagram.svg?cache=1', '/diagram.svg?cache=1'],
    ['/materials/example.pdf#page=2', '/materials/example.pdf#page=2']
  ]) assert.equal(pagePath(source), expected)
})
