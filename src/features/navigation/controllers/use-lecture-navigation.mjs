import { ref, nextTick, onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vitepress'
import {
  LECTURE_PART_HASHES,
  NAVIGATION_SELECTORS
} from '../../../config/navigation.mjs'
import { lectureParts } from '../../lecture/services/lecture-model.mjs'
import {
  classifyLectureHash,
  isSamePageLectureLink,
  shouldIgnoreNavigationClick
} from '../services/tab-service.mjs'

/**
 * Shared reactive state for current lecture part across layout and components.
 */
export const lecturePart = ref('notes')

// Tab hashes are state, not article anchors (the exercise content also has an
// element named bai-tap). Bypass the router's automatic anchor scrolling.
export async function selectLecturePart(part) {
  lecturePart.value = part
  const hash = `#${part}`
  if (window.location.hash !== hash) {
    window.history.pushState(window.history.state, '', hash)
    window.dispatchEvent(new HashChangeEvent('hashchange'))
  }
  await nextTick()
  window.scrollTo({ top: 0, behavior: 'instant' })
}

/**
 * Synchronizes the reactive lecturePart with current window.location.hash.
 */
export function syncLecturePart() {
  if (typeof window === 'undefined') return
  let rawHash = window.location.hash
  if (rawHash === '#slides') {
    rawHash = '#notes'
    window.history.replaceState(window.history.state, '', window.location.pathname + window.location.search + rawHash)
  }
  lecturePart.value = classifyLectureHash(rawHash, {
    allowedParts: lectureParts,
    isExerciseAnchor: (anchorId) => {
      if (typeof document === 'undefined') return false
      let anchor
      try {
        anchor = document.getElementById(anchorId)
      } catch {
        return false
      }
      return Boolean(anchor?.closest(NAVIGATION_SELECTORS.exerciseContent))
    }
  })
  if (LECTURE_PART_HASHES.includes(rawHash) && document.querySelector('.shared-reading-outline')) {
    nextTick(() => requestAnimationFrame(() => window.scrollTo({ top: 0, behavior: 'instant' })))
  }
}

/**
 * Intercepts in-page lecture link clicks to switch tabs without full navigation.
 *
 * @param {MouseEvent} event
 */
export function syncLink(event) {
  if (typeof window === 'undefined') return
  if (shouldIgnoreNavigationClick(event)) return
  const anchor = event.target?.closest?.('a[href]')
  if (!anchor?.closest('.shared-reading-outline')) return

  const result = isSamePageLectureLink(anchor.href, window.location.href, LECTURE_PART_HASHES)
  if (result.isMatch && result.part) {
    event.preventDefault()
    selectLecturePart(result.part)
  }
}

/**
 * Composable setting up lecture hash and link click listeners.
 */
export function useLectureNavigation() {
  let route
  try {
    route = useRoute()
  } catch {
    // In SSR or test contexts where useRoute is unavailable
  }

  onMounted(() => {
    if (typeof window === 'undefined') return
    syncLecturePart()
    window.addEventListener('hashchange', syncLecturePart)
    window.addEventListener('popstate', syncLecturePart)
    document.addEventListener('click', syncLink, true)
  })

  onUnmounted(() => {
    if (typeof window === 'undefined') return
    window.removeEventListener('hashchange', syncLecturePart)
    window.removeEventListener('popstate', syncLecturePart)
    document.removeEventListener('click', syncLink, true)
  })

  if (route) {
    watch(() => route.path, syncLecturePart)
  }

  return {
    lecturePart,
    syncLecturePart,
    syncLink
  }
}
