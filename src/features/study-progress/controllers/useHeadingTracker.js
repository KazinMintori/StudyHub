import { onMounted, onBeforeUnmount, onUnmounted, watch, nextTick } from 'vue'
import { readStored, writeStored } from '../../../core/storage/index.js'
import { calculateProgressKey } from '../services/progress-key.js'
import {
  cleanHeadingTitle,
  findActiveHeading,
  buildLastLessonPayload
} from '../services/heading-bookmark.js'
import { studyLink as defaultStudyLink } from '../../../core/routing/links.js'

export function useHeadingTracker({
  course,
  lesson,
  part,
  route,
  readable,
  studyLink = defaultStudyLink,
  read = readStored,
  write = writeStored,
  progressKeyFn = calculateProgressKey
}) {
  let frame = null
  let trackedPath = ''
  let trackedTitle = ''

  async function load() {
    await nextTick()
    const isReadable = typeof readable?.value === 'boolean' ? readable.value : lesson?.value?.status === 'ready'
    if (!isReadable) {
      trackedPath = ''
      trackedTitle = ''
      return
    }
    trackedPath = progressKeyFn(course?.value, lesson?.value)
    trackedTitle = lesson?.value?.title || ''
    const previous = read('studyhub_last_lesson', null)
    const retained = previous?.path === trackedPath ? previous : {}
    write('studyhub_last_lesson', {
      ...retained,
      path: trackedPath,
      title: lesson?.value?.title || trackedTitle
    })
  }

  function recordHeading() {
    if (part?.value !== 'notes' || !trackedPath) return
    if (typeof window === 'undefined' || typeof document === 'undefined') return
    // Navigation can reset scroll before this component finishes unmounting.
    if (window.location.pathname !== studyLink(trackedPath)) return

    const headings = [...document.querySelectorAll('.main > .vp-doc h2[id]')]
    if (!headings.length) return

    const heading = findActiveHeading(headings, 160)
    const previous = read('studyhub_last_lesson', {}) || {}
    const headingId = heading?.id || ''
    const headingTitle = cleanHeadingTitle(heading?.textContent || '')

    write(
      'studyhub_last_lesson',
      buildLastLessonPayload({
        previous,
        trackedPath,
        trackedTitle,
        headingId,
        headingTitle
      })
    )
  }

  function scroll() {
    if (typeof window === 'undefined') return
    if (frame) cancelAnimationFrame(frame)
    frame = requestAnimationFrame(recordHeading)
  }

  onMounted(() => {
    load()
    if (typeof window !== 'undefined') {
      window.addEventListener('scroll', scroll, { passive: true })
      window.addEventListener('pagehide', recordHeading)
    }
  })

  onBeforeUnmount(recordHeading)

  onUnmounted(() => {
    if (typeof window !== 'undefined') {
      if (frame) cancelAnimationFrame(frame)
      window.removeEventListener('scroll', scroll)
      window.removeEventListener('pagehide', recordHeading)
    }
  })

  if (route) {
    watch(() => route.path, load)
  }

  return {
    load,
    recordHeading,
    getTrackedPath: () => trackedPath,
    getTrackedTitle: () => trackedTitle
  }
}
