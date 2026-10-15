import { popoverPosition } from '../services/popover-position.mjs'
import { nextTick, onMounted, onUnmounted, ref, watch } from 'vue'
import { useRoute, withBase } from 'vitepress'
import { concepts } from '../../../../docs/.vitepress/concepts.mjs'
import { conceptField } from '../../../../docs/.vitepress/wiki-content.mjs'

export function useTermPreview() {
  const route = useRoute()
  const term = ref(null)
  const wikiHref = ref('')
  const position = ref({})
  const popover = ref(null)
  const closeButton = ref(null)
  const pinned = ref(false)
  const field = ref(null)

  let anchor
  let timer
  let suppressFocus = false

  function clearAnchor(link = anchor) {
    link?.removeAttribute('aria-describedby')
    link?.setAttribute('aria-expanded', 'false')
  }

  function close({ restoreFocus = false } = {}) {
    clearTimeout(timer)
    const previousAnchor = anchor
    clearAnchor(previousAnchor)
    term.value = null
    wikiHref.value = ''
    pinned.value = false
    field.value = null
    anchor = null
    if (restoreFocus && previousAnchor?.isConnected) {
      suppressFocus = true
      previousAnchor.focus()
      queueMicrotask(() => { suppressFocus = false })
    }
  }

  function updatePosition() {
    if (!anchor || !term.value) return
    position.value = popoverPosition({
      viewportWidth: window.innerWidth,
      viewportHeight: window.innerHeight,
      anchor: anchor.getBoundingClientRect(),
      height: popover.value?.getBoundingClientRect().height || 280
    })
  }

  async function show(link, { persist = false } = {}) {
    clearTimeout(timer)
    const nextTerm = concepts[link?.dataset.term]
    if (!link || !nextTerm) return

    if (anchor !== link) clearAnchor()
    anchor = link
    term.value = nextTerm
    field.value = conceptField(link.dataset.term)
    wikiHref.value = withBase(link.dataset.wiki)
    pinned.value = persist
    link.setAttribute('aria-expanded', persist ? 'true' : 'false')
    if (persist) link.removeAttribute('aria-describedby')
    else link.setAttribute('aria-describedby', 'study-term-preview')

    await nextTick()
    updatePosition()
    if (persist) closeButton.value?.focus()
  }

  function over(event) {
    if (pinned.value || event.pointerType === 'touch' || window.innerWidth < 640) return
    const link = event.target.closest?.('button.study-term')
    if (link) show(link)
  }

  function out(event) {
    if (pinned.value) return
    if (anchor?.contains(event.target) && !popover.value?.contains(event.relatedTarget)) {
      timer = setTimeout(close, 140)
    }
  }

  function focusIn(event) {
    if (pinned.value || suppressFocus) return
    const link = event.target.closest?.('button.study-term')
    // Touch focus fires before click. A bottom-sheet tooltip at that point can
    // cover the tapped button and prevent the click from pinning the note.
    if (link?.matches(':focus-visible')) show(link)
  }

  function focusOut(event) {
    if (pinned.value) return
    if (anchor?.contains(event.target) && !popover.value?.contains(event.relatedTarget)) {
      timer = setTimeout(close, 140)
    }
  }

  function click(event) {
    const link = event.target.closest?.('button.study-term')
    if (!link) {
      if (pinned.value && !popover.value?.contains(event.target)) close()
      return
    }
    if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return
    event.preventDefault()
    event.stopPropagation()
    show(link, { persist: true })
  }

  function key(event) {
    if (event.key === 'Escape' && term.value) {
      event.preventDefault()
      event.stopPropagation()
      close({ restoreFocus: pinned.value })
    }
  }

  function keepOpen() {
    clearTimeout(timer)
  }

  function leavePopover(event) {
    if (!pinned.value && !anchor?.contains(event.relatedTarget)) timer = setTimeout(close, 140)
  }

  function scroll(event) {
    if (popover.value?.contains(event.target)) return
    if (!anchor) return
    const rect = anchor.getBoundingClientRect()
    if (rect.bottom <= 0 || rect.top >= window.innerHeight) close()
    else updatePosition()
  }

  onMounted(() => {
    document.addEventListener('pointerover', over)
    document.addEventListener('pointerout', out)
    document.addEventListener('focusin', focusIn)
    document.addEventListener('focusout', focusOut)
    window.addEventListener('click', click, true)
    window.addEventListener('keydown', key, true)
    window.addEventListener('scroll', scroll, true)
    window.addEventListener('resize', updatePosition)
  })

  onUnmounted(() => {
    close()
    document.removeEventListener('pointerover', over)
    document.removeEventListener('pointerout', out)
    document.removeEventListener('focusin', focusIn)
    document.removeEventListener('focusout', focusOut)
    window.removeEventListener('click', click, true)
    window.removeEventListener('keydown', key, true)
    window.removeEventListener('scroll', scroll, true)
    window.removeEventListener('resize', updatePosition)
  })

  watch(() => route.path, () => close())

  return { route, term, wikiHref, position, popover, closeButton, pinned, field, anchor, timer, suppressFocus, clearAnchor, close, updatePosition, show, over, out, focusIn, focusOut, click, key, keepOpen, leavePopover, scroll }
}
