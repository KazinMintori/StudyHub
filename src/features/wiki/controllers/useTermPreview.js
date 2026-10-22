import { popoverPosition, pinnedPreviewPosition } from '../services/popover-position.mjs'
import { nextTick, onMounted, onUnmounted, ref, watch } from 'vue'
import { useRoute, withBase } from 'vitepress'
import { loadConceptData } from '../services/concept-loader.mjs'

export function useTermPreview() {
  const route = useRoute()
  const term = ref(null)
  const wikiHref = ref('')
  const position = ref({})
  const popover = ref(null)
  const closeButton = ref(null)
  const pinned = ref(false)
  const modal = ref(false)
  const field = ref(null)

  let anchor
  let timer
  let suppressFocus = false
  let loadToken = 0
  let pendingLink = null
  let modalLock = null

  function setModal(value) {
    modal.value = value
    if (value && !modalLock) {
      const app = document.querySelector('#app')
      modalLock = { app, inert: app?.inert, overflow: document.documentElement.style.overflow }
      if (app) app.inert = true
      document.documentElement.style.overflow = 'hidden'
    } else if (!value && modalLock) {
      if (modalLock.app) modalLock.app.inert = modalLock.inert
      document.documentElement.style.overflow = modalLock.overflow
      modalLock = null
    }
  }

  function clearAnchor(link = anchor) {
    link?.removeAttribute('aria-describedby')
    link?.setAttribute('aria-expanded', 'false')
  }

  function close({ restoreFocus = false } = {}) {
    clearTimeout(timer)
    loadToken++
    pendingLink = null
    setModal(false)
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
    if (pinned.value) {
      const article = document.querySelector('.main > .vp-doc')
      const layout = pinnedPreviewPosition({ viewportWidth: window.innerWidth, viewportHeight: window.innerHeight, readingRect: article?.getBoundingClientRect() })
      position.value = layout.position
      setModal(layout.modal)
      return
    }
    setModal(false)
    position.value = popoverPosition({
      viewportWidth: window.innerWidth,
      viewportHeight: window.innerHeight,
      anchor: anchor.getBoundingClientRect(),
      height: popover.value?.getBoundingClientRect().height || 280
    })
  }

  // The concept dictionary is a separate chunk. It is fetched on the first
  // hover/focus/tap of a term (or when the browser is idle on hover devices).
  let conceptData = null
  async function ensureConceptData() {
    if (!conceptData) conceptData = await loadConceptData()
    return conceptData
  }

  async function show(link, { persist = false } = {}) {
    clearTimeout(timer)
    const id = link?.dataset.term
    if (!link || !id) return
    const token = ++loadToken
    pendingLink = link
    if (!conceptData) {
      try { await ensureConceptData() } catch { if (token === loadToken) pendingLink = null; return }
      // Ignore a hover that ended while the data was downloading.
      if (token !== loadToken || !link.isConnected) return
      if (!persist && !link.matches(':hover') && !link.matches(':focus-visible')) { pendingLink = null; return }
    }
    if (token !== loadToken || !link.isConnected) return
    pendingLink = null
    const nextTerm = conceptData.concepts[id]
    if (!nextTerm) return

    if (anchor !== link) clearAnchor()
    anchor = link
    term.value = nextTerm
    field.value = conceptData.conceptField(id)
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
      if ((pinned.value || pendingLink) && !popover.value?.contains(event.target)) close({ restoreFocus: !!event.target.closest?.('.term-preview-scrim') })
      return
    }
    if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return
    event.preventDefault()
    event.stopPropagation()
    show(link, { persist: true })
  }

  function key(event) {
    if (event.key === 'Escape' && (term.value || pendingLink)) {
      event.preventDefault()
      event.stopPropagation()
      close({ restoreFocus: pinned.value })
    }
    if (event.key === 'Tab' && pinned.value && modal.value) {
      const controls = [...(popover.value?.querySelectorAll('button:not([disabled]), a[href], [tabindex="0"]') || [])].filter(el => el.getClientRects().length)
      const first = controls[0], last = controls.at(-1)
      if (!first) { event.preventDefault(); popover.value?.focus(); return }
      if (!popover.value.contains(document.activeElement) || (!event.shiftKey && document.activeElement === last)) {
        event.preventDefault(); first.focus()
      } else if (event.shiftKey && document.activeElement === first) {
        event.preventDefault(); last.focus()
      }
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
    if (window.matchMedia?.('(hover: hover)').matches && !navigator.connection?.saveData) {
      const warm = () => { if (document.querySelector('button.study-term')) ensureConceptData().catch(() => {}) }
      if ('requestIdleCallback' in window) window.requestIdleCallback(warm, { timeout: 4000 })
      else setTimeout(warm, 2500)
    }
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

  return { route, term, wikiHref, position, popover, closeButton, pinned, modal, field, anchor, timer, suppressFocus, clearAnchor, close, updatePosition, show, over, out, focusIn, focusOut, click, key, keepOpen, leavePopover, scroll }
}
