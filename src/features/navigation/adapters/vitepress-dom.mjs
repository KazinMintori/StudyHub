import { NAVIGATION_SELECTORS } from '../../../config/navigation.mjs'

/**
 * Finds a DOM element by hash/id with safety against malformed URI.
 *
 * @param {string} hash
 * @returns {HTMLElement|null}
 */
export function findAnchorElement(hash) {
  if (typeof document === 'undefined' || !hash) return null
  try {
    return document.getElementById(decodeURIComponent(hash))
  } catch {
    return null
  }
}

/**
 * Checks whether an element is inside the exercises content container.
 *
 * @param {Element|null} element
 * @returns {boolean}
 */
export function isExerciseElement(element) {
  return Boolean(element?.closest?.(NAVIGATION_SELECTORS.exerciseContent))
}

/**
 * Triggers the VitePress doc search modal.
 */
export function openSearch() {
  if (typeof document === 'undefined') return
  document.querySelector(NAVIGATION_SELECTORS.docSearchButton)?.click()
}
