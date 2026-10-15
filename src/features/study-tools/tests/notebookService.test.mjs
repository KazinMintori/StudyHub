import test from 'node:test'
import assert from 'node:assert/strict'
import {
  DEFAULT_NOTE_TEMPLATE,
  getNoteStorageKey,
  resolveInitialNote,
  getNoteDownloadFilename,
  createMarkdownOptions
} from '../services/notebookService.mjs'

test('notebookService: getNoteStorageKey namespaces by subject', () => {
  assert.equal(getNoteStorageKey('general'), 'studyhub_note_general')
  assert.equal(getNoteStorageKey('toan-cho-ai'), 'studyhub_note_toan-cho-ai')
  assert.equal(getNoteStorageKey(''), 'studyhub_note_general')
  assert.equal(getNoteStorageKey(null), 'studyhub_note_general')
})

test('notebookService: resolveInitialNote returns stored text when present', () => {
  const customNote = '# Ghi chú của tôi\nNội dung'
  assert.equal(resolveInitialNote(customNote, null, 'general'), customNote)
  assert.equal(resolveInitialNote(customNote, 'legacy', 'toan-cho-ai'), customNote)
  assert.equal(resolveInitialNote('', null, 'general'), '')
})

test('notebookService: resolveInitialNote preserves legacy raw studyhub_notes fallback for general subject', () => {
  const legacyNotes = '# Ghi chú cũ từ phiên bản 1\nĐiều đã học'
  // When no key studyhub_note_general exists (storedText is null), fall back to raw studyhub_notes
  const resolved = resolveInitialNote(null, legacyNotes, 'general')
  assert.equal(resolved, legacyNotes)
})

test('notebookService: resolveInitialNote ignores legacy raw notes for specific course subjects', () => {
  const legacyNotes = '# Ghi chú cũ từ phiên bản 1'
  // Subject is specific course, not 'general'
  const resolved = resolveInitialNote(null, legacyNotes, 'toan-cho-ai')
  assert.equal(resolved, DEFAULT_NOTE_TEMPLATE)
})

test('notebookService: resolveInitialNote provides default markdown template when no storage exists', () => {
  assert.equal(resolveInitialNote(null, null, 'general'), DEFAULT_NOTE_TEMPLATE)
  assert.equal(resolveInitialNote(null, null, 'toan-cho-ai'), DEFAULT_NOTE_TEMPLATE)
  assert.equal(resolveInitialNote(undefined, undefined, 'general'), DEFAULT_NOTE_TEMPLATE)
})

test('notebookService: getNoteDownloadFilename formats export name', () => {
  assert.equal(getNoteDownloadFilename('general'), 'StudyHub-general.md')
  assert.equal(getNoteDownloadFilename('vat-ly-2'), 'StudyHub-vat-ly-2.md')
  assert.equal(getNoteDownloadFilename(null), 'StudyHub-general.md')
})

test('notebookService: createMarkdownOptions enforces strict rendering safety', () => {
  const opts = createMarkdownOptions()
  assert.equal(opts.html, false)
  assert.equal(opts.linkify, true)
  assert.equal(opts.breaks, true)
})
