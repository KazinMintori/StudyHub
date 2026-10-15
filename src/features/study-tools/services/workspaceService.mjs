/**
 * Pure domain service for workspace tabs navigation and hash routing.
 */

export const DEFAULT_WORKSPACE_TABS = [
  { id: 'flashcards', name: 'Flashcard' },
  { id: 'notes', name: 'Ghi chú' },
  { id: 'focus', name: 'Hẹn giờ' },
  { id: 'simulation', name: 'Mô phỏng' }
]

export function isValidTab(id, tabs = DEFAULT_WORKSPACE_TABS) {
  if (!id || !Array.isArray(tabs)) return false
  return tabs.some(tab => tab.id === id)
}

export function parseTabFromHash(hash, tabs = DEFAULT_WORKSPACE_TABS, fallback = 'flashcards') {
  if (!hash || typeof hash !== 'string') return fallback
  const id = hash.replace(/^#/, '').trim()
  return isValidTab(id, tabs) ? id : fallback
}

export function formatTabHash(tabId) {
  return `#${tabId}`
}
