import {
  LECTURE_PART_IDS,
  LECTURE_PART_HASHES,
  DEFAULT_LECTURE_PART,
  EXERCISE_LECTURE_PART
} from '../../../config/navigation.mjs'

/**
 * Normalizes a raw URL hash by stripping the leading `#`
 * and safely decoding URI components.
 *
 * @param {string|null|undefined} rawHash
 * @returns {string}
 */
export function normalizeHash(rawHash) {
  if (rawHash == null) return ''
  const str = typeof rawHash === 'string' ? rawHash.trim() : String(rawHash)
  const stripped = str.startsWith('#') ? str.slice(1) : str
  if (!stripped) return ''
  try {
    return decodeURIComponent(stripped)
  } catch {
    return stripped
  }
}

/**
 * Checks whether an ID is a valid lecture tab/part ID.
 *
 * @param {string} id
 * @param {Array<string|{id: string}>} [allowedParts]
 * @returns {boolean}
 */
export function isValidLecturePartId(id, allowedParts = LECTURE_PART_IDS) {
  if (!id || !Array.isArray(allowedParts)) return false
  return allowedParts.some(part => (typeof part === 'string' ? part === id : part?.id === id))
}

/**
 * Classifies a lecture hash into a lecture tab ID ('notes', 'slides', 'bai-tap', etc.).
 *
 * Domain rules:
 * 1. If hash matches a known lecture part, return that part.
 * 2. If hash is an anchor that belongs to an exercise container, return 'bai-tap'.
 * 3. Otherwise (notes anchor, unknown hash, or empty hash), return 'notes'.
 *
 * @param {string|null|undefined} rawHash
 * @param {object} [options]
 * @param {Array<string|{id: string}>} [options.allowedParts]
 * @param {(anchorId: string) => boolean} [options.isExerciseAnchor]
 * @param {string} [options.defaultPart]
 * @param {string} [options.exercisePart]
 * @returns {string}
 */
export function classifyLectureHash(rawHash, options = {}) {
  const allowedParts = options.allowedParts || LECTURE_PART_IDS
  const defaultPart = options.defaultPart || DEFAULT_LECTURE_PART
  const exercisePart = options.exercisePart || EXERCISE_LECTURE_PART
  const isExerciseAnchor = options.isExerciseAnchor

  if (rawHash == null) return defaultPart

  const rawStr = typeof rawHash === 'string' ? rawHash.trim() : String(rawHash)
  if (!rawStr) return defaultPart

  const stripped = rawStr.startsWith('#') ? rawStr.slice(1) : rawStr
  if (!stripped) return defaultPart

  // 1. Direct match with allowed tab IDs (e.g. 'slides', 'notes', 'cheatsheet', etc.)
  if (isValidLecturePartId(stripped, allowedParts)) {
    return stripped
  }

  // 2. Decode hash and check if it targets an exercise anchor
  let decodedId = stripped
  try {
    decodedId = decodeURIComponent(stripped)
  } catch {
    // Malformed URI keeps the raw stripped string
  }

  if (typeof isExerciseAnchor === 'function') {
    try {
      if (isExerciseAnchor(decodedId)) {
        return exercisePart
      }
    } catch {
      // In case element lookup throws
    }
  }

  // 3. Fallback to default notes part
  return defaultPart
}

/**
 * Determines whether a click on an anchor link is an in-page lecture tab transition.
 *
 * @param {string} targetHref
 * @param {string} currentHref
 * @param {string[]} [allowedHashes]
 * @returns {{ isMatch: boolean, part: string | null }}
 */
export function isSamePageLectureLink(targetHref, currentHref, allowedHashes = LECTURE_PART_HASHES) {
  if (!targetHref || !currentHref) {
    return { isMatch: false, part: null }
  }

  try {
    const url = new URL(targetHref, currentHref)
    const current = new URL(currentHref)

    const isSameOrigin = url.origin === current.origin
    const isSamePath = url.pathname === current.pathname
    const isAllowedHash = allowedHashes.includes(url.hash)

    if (isSameOrigin && isSamePath && isAllowedHash) {
      return {
        isMatch: true,
        part: url.hash.slice(1)
      }
    }
  } catch {
    // Malformed URL string
  }

  return { isMatch: false, part: null }
}

/**
 * Determines if a mouse/keyboard navigation click should be ignored
 * (e.g. middle click, ctrl/cmd/shift/alt clicks).
 *
 * @param {MouseEvent|object} event
 * @returns {boolean}
 */
export function shouldIgnoreNavigationClick(event) {
  if (!event) return false
  if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return true
  if (event.button !== undefined && event.button !== 0) return true
  return false
}
