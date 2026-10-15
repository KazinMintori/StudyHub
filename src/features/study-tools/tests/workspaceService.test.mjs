import test from 'node:test'
import assert from 'node:assert/strict'
import {
  DEFAULT_WORKSPACE_TABS,
  isValidTab,
  parseTabFromHash,
  formatTabHash
} from '../services/workspaceService.mjs'

test('workspaceService: isValidTab verifies recognized study tabs', () => {
  assert.equal(isValidTab('flashcards'), true)
  assert.equal(isValidTab('notes'), true)
  assert.equal(isValidTab('focus'), true)
  assert.equal(isValidTab('simulation'), true)
  assert.equal(isValidTab('other'), false)
  assert.equal(isValidTab(''), false)
  assert.equal(isValidTab(null), false)
})

test('workspaceService: parseTabFromHash extracts valid tab id from location hash', () => {
  assert.equal(parseTabFromHash('#flashcards'), 'flashcards')
  assert.equal(parseTabFromHash('#notes'), 'notes')
  assert.equal(parseTabFromHash('#focus'), 'focus')
  assert.equal(parseTabFromHash('#simulation'), 'simulation')
  assert.equal(parseTabFromHash('notes'), 'notes') // tolerance for hash without prefix
})

test('workspaceService: parseTabFromHash defaults to fallback for unknown or empty hash', () => {
  assert.equal(parseTabFromHash('#unknown'), 'flashcards')
  assert.equal(parseTabFromHash('#'), 'flashcards')
  assert.equal(parseTabFromHash(''), 'flashcards')
  assert.equal(parseTabFromHash(null), 'flashcards')
  assert.equal(parseTabFromHash(undefined), 'flashcards')
  assert.equal(parseTabFromHash('#invalid', DEFAULT_WORKSPACE_TABS, 'notes'), 'notes')
})

test('workspaceService: formatTabHash formats URL hash anchor', () => {
  assert.equal(formatTabHash('flashcards'), '#flashcards')
  assert.equal(formatTabHash('focus'), '#focus')
})
