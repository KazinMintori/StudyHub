<script setup>
import { nextTick, onMounted, onUnmounted, ref, watch } from 'vue'
import { useRoute, withBase } from 'vitepress'
import { concepts } from '../concepts.mjs'
import { conceptField } from '../wiki-content.mjs'
import MathText from './MathText.vue'

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

  const gutter = window.innerWidth < 640 ? 12 : 16
  const width = Math.min(360, window.innerWidth - gutter * 2)

  if (window.innerWidth < 640) {
    position.value = {
      left: `${gutter}px`,
      right: `${gutter}px`,
      bottom: `calc(${gutter}px + env(safe-area-inset-bottom, 0px))`
    }
    return
  }

  const rect = anchor.getBoundingClientRect()
  const height = popover.value?.getBoundingClientRect().height || 280
  const top = Math.max(gutter, Math.min(rect.top, window.innerHeight - height - gutter))

  if (window.innerWidth - rect.right >= width + gutter * 2) {
    position.value = { width: `${width}px`, left: `${rect.right + gutter}px`, top: `${top}px` }
  } else if (rect.left >= width + gutter * 2) {
    position.value = { width: `${width}px`, left: `${rect.left - width - gutter}px`, top: `${top}px` }
  } else {
    const left = Math.max(gutter, Math.min(rect.left, window.innerWidth - width - gutter))
    if (rect.bottom + height + gutter <= window.innerHeight) {
      position.value = { width: `${width}px`, left: `${left}px`, top: `${rect.bottom + gutter}px` }
    } else {
      position.value = { width: `${width}px`, left: `${left}px`, bottom: `${window.innerHeight - rect.top + gutter}px` }
    }
  }
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
  if (pinned.value || event.pointerType === 'touch') return
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
  if (link) show(link)
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
</script>

<template>
  <Teleport to="body">
    <button v-if="term && pinned" type="button" class="term-preview-scrim" aria-label="Đóng ghi chú nhanh" @click="close({ restoreFocus: true })"></button>
    <aside
      v-if="term"
      id="study-term-preview"
      ref="popover"
      class="term-preview"
      :class="{ 'is-pinned': pinned }"
      :style="position"
      :role="pinned ? 'dialog' : 'tooltip'"
      :aria-labelledby="pinned ? 'study-term-preview-title' : undefined"
      @pointerenter="keepOpen"
      @pointerleave="leavePopover"
    >
      <div class="term-preview-heading">
        <div>
          <span class="term-preview-kicker">Ghi chú nhanh</span>
          <strong id="study-term-preview-title">{{ term.name }}</strong>
          <span v-if="field" class="term-preview-field">Lĩnh vực: {{ field.name }}</span>
        </div>
        <button
          v-if="pinned"
          ref="closeButton"
          type="button"
          class="term-preview-close"
          aria-label="Đóng ghi chú nhanh"
          @click="close({ restoreFocus: true })"
        >Đóng</button>
      </div>
      <MathText as="p" :text="term.definition" />
      <div class="term-preview-example">
        <span>Ví dụ:</span>
        <MathText as="p" :text="term.example" />
        <MathText v-if="term.notation" as="div" class="term-preview-notation" :text="term.notation" />
      </div>
      <a v-if="pinned" class="term-preview-wiki" :href="wikiHref">Đọc bài Wiki đầy đủ <span aria-hidden="true">→</span></a>
      <span v-else class="term-preview-hint">Nhấp để giữ ghi chú và mở đường dẫn tới Wiki.</span>
    </aside>
  </Teleport>
</template>
