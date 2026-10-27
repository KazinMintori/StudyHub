import { nextTick, onMounted, onUnmounted, provide, ref, watch } from 'vue'
import { getScrollOffset, onContentUpdated } from 'vitepress'
import { lecturePart } from './use-lecture-navigation.mjs'

export const readingOutlineKey = Symbol('reading-outline')

export function provideReadingOutline(page) {
  const headings = ref([])
  const active = ref('')
  let observer, frame = 0, scrollFrame = 0, disposed = false

  function updateActive() {
    scrollFrame = 0
    let current = ''
    for (const heading of headings.value) {
      const element = document.getElementById(heading.id)
      if (element?.getBoundingClientRect().top <= getScrollOffset() + 8) current = heading.id
    }
    active.value = current
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
    updateActive()
  }

  function schedule() {
    if (!disposed && !frame) frame = requestAnimationFrame(refresh)
  }

  async function observe() {
    await nextTick()
    if (disposed) return
    observer?.disconnect()
    const root = document.querySelector('.VPDoc .content-container')
    if (root) observer.observe(root, { childList: true, subtree: true })
    schedule()
  }

  async function navigate(id) {
    const hash = `#${encodeURIComponent(id)}`
    if (window.location.hash !== hash) {
      window.history.pushState(window.history.state, '', hash)
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
    observe()
    window.addEventListener('scroll', onScroll, { passive: true })
    window.addEventListener('resize', schedule)
  })
  onContentUpdated(() => { if (observer) observe() })
  watch([lecturePart, () => page.value.relativePath], () => { if (observer) observe() }, { flush: 'post' })
  onUnmounted(() => {
    disposed = true
    observer?.disconnect()
    cancelAnimationFrame(frame)
    cancelAnimationFrame(scrollFrame)
    window.removeEventListener('scroll', onScroll)
    window.removeEventListener('resize', schedule)
  })
  provide(readingOutlineKey, { headings, active, navigate })
}
