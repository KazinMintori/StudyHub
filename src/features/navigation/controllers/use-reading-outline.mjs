import { nextTick, onMounted, onUnmounted, provide, ref, watch } from 'vue'
import { getScrollOffset, onContentUpdated } from 'vitepress'
import { lecturePart } from './use-lecture-navigation.mjs'

export const readingOutlineKey = Symbol('reading-outline')

export function provideReadingOutline(page) {
  const headings = ref([])
  const active = ref('')
  let observer, frame = 0, scrollFrame = 0, disposed = false
  let positions = []
  let resizeObserver

  function updateActive() {
    scrollFrame = 0
    const top = window.scrollY + getScrollOffset() + 8
    let low = 0, high = positions.length
    while (low < high) {
      const mid = (low + high) >>> 1
      if (positions[mid].top <= top) low = mid + 1
      else high = mid
    }
    active.value = positions[low - 1]?.id || ''
  }

  function onScroll() {
    if (!scrollFrame) scrollFrame = requestAnimationFrame(updateActive)
  }

  function refresh() {
    frame = 0
    const root = document.querySelector('.VPDoc .content-container')
    const next = [...(root?.querySelectorAll('.main > .vp-doc :is(h2,h3), .lecture-panels :is(h2,h3)') || [])]
      .filter(element => element.getClientRects().length && !element.closest('.ignore-header'))
      .map((element, index) => {
        if (!element.id && element.closest('.lecture-panels')) element.id = `${lecturePart.value}--${index + 1}`
        return {
          id: element.id,
          title: element.textContent.replace(/[\u200b#]/g, '').trim(),
          level: Number(element.tagName[1])
        }
      }).filter(heading => heading.id)
    // The observer also sees the outline render. Avoid feeding it another update.
    if (JSON.stringify(next) !== JSON.stringify(headings.value)) headings.value = next
    positions = next.map(heading => ({ id: heading.id, top: window.scrollY + document.getElementById(heading.id).getBoundingClientRect().top }))
      .sort((a, b) => a.top - b.top)
    updateActive()
  }

  function schedule() {
    if (!disposed && !frame) frame = requestAnimationFrame(refresh)
  }

  async function observe() {
    await nextTick()
    if (disposed) return
    observer?.disconnect()
    resizeObserver?.disconnect()
    const root = document.querySelector('.VPDoc .content-container')
    if (root) {
      observer.observe(root, { childList: true, subtree: true })
      resizeObserver.observe(root)
    }
    schedule()
  }

  async function navigate(id) {
    const hash = `#${encodeURIComponent(id)}`
    if (window.location.hash !== hash) {
      window.history.replaceState({ ...window.history.state, scrollPosition: window.scrollY }, '')
      window.history.pushState({}, '', hash)
      window.dispatchEvent(new HashChangeEvent('hashchange'))
    }
    await nextTick()
    const target = document.getElementById(id)
    if (!target) return
    target.setAttribute('tabindex', '-1')
    target.focus({ preventScroll: true })
    window.scrollTo({ top: Math.max(0, window.scrollY + target.getBoundingClientRect().top - getScrollOffset()), behavior: 'instant' })
    active.value = id
  }

  onMounted(() => {
    observer = new MutationObserver(schedule)
    resizeObserver = new ResizeObserver(schedule)
    observe()
    window.addEventListener('scroll', onScroll, { passive: true })
    window.addEventListener('resize', schedule)
  })
  onContentUpdated(() => { if (observer) observe() })
  watch([lecturePart, () => page.value.relativePath], () => { if (observer) observe() }, { flush: 'post' })
  onUnmounted(() => {
    disposed = true
    observer?.disconnect()
    resizeObserver?.disconnect()
    cancelAnimationFrame(frame)
    cancelAnimationFrame(scrollFrame)
    window.removeEventListener('scroll', onScroll)
    window.removeEventListener('resize', schedule)
  })
  provide(readingOutlineKey, { headings, active, navigate })
}
