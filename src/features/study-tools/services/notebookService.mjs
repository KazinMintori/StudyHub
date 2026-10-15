/**
 * Pure domain service for notebook notes operations.
 */

export const DEFAULT_NOTE_TEMPLATE = '# Ghi chú học tập\n\n## Điều mình đã hiểu\n\n- \n\n## Câu hỏi cần làm rõ\n\n- \n'

export function getNoteStorageKey(subject = 'general') {
  const safeSubject = subject || 'general'
  return `studyhub_note_${safeSubject}`
}

export function resolveInitialNote(storedText, legacyRawNotes, subject = 'general') {
  if (typeof storedText === 'string') {
    return storedText
  }

  if (storedText === null && subject === 'general' && typeof legacyRawNotes === 'string') {
    return legacyRawNotes
  }

  return DEFAULT_NOTE_TEMPLATE
}

export function getNoteDownloadFilename(subject = 'general') {
  const safeSubject = subject || 'general'
  return `StudyHub-${safeSubject}.md`
}

export function createMarkdownOptions() {
  return {
    html: false,
    linkify: true,
    breaks: true
  }
}
