<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vitepress'
import { concepts } from '../concepts.mjs'
const route = useRoute(), term = ref(null), position = ref({}), tooltip = ref(null)
let anchor, timer
function close() { clearTimeout(timer); anchor?.removeAttribute('aria-describedby'); term.value = null; anchor = null }
function show(link) {
  clearTimeout(timer)
  if (!link || !concepts[link.dataset.term]) return
  if (anchor !== link) anchor?.removeAttribute('aria-describedby')
  anchor = link; term.value = concepts[link.dataset.term]; link.setAttribute('aria-describedby','study-term-preview')
  const rect = link.getBoundingClientRect(), width = Math.min(360, window.innerWidth - 32)
  position.value = { width: `${width}px`, left: `${Math.max(16,Math.min(rect.left, window.innerWidth-width-16))}px`, ...(rect.bottom + 235 < window.innerHeight ? { top: `${rect.bottom+9}px` } : { bottom: `${Math.max(16, window.innerHeight-rect.top+9)}px` }) }
}
function over(event) { const link = event.target.closest?.('a.study-term'); if (link) show(link) }
function out(event) { if (anchor?.contains(event.target) && !tooltip.value?.contains(event.relatedTarget)) timer = setTimeout(close, 120) }
function key(event) { if (event.key === 'Escape') close() }
function keepOpen() { clearTimeout(timer) }
function scroll(event) {
  if (tooltip.value?.contains(event.target)) return
  if (anchor && (document.activeElement === anchor || anchor.matches(':hover'))) {
    const rect = anchor.getBoundingClientRect()
    if (rect.bottom > 0 && rect.top < window.innerHeight) show(anchor)
    else close()
  } else close()
}
onMounted(() => { document.addEventListener('pointerover',over); document.addEventListener('pointerout',out); document.addEventListener('focusin',over); document.addEventListener('focusout',out); document.addEventListener('keydown',key); window.addEventListener('scroll',scroll,true) })
onUnmounted(() => { close(); document.removeEventListener('pointerover',over); document.removeEventListener('pointerout',out); document.removeEventListener('focusin',over); document.removeEventListener('focusout',out); document.removeEventListener('keydown',key); window.removeEventListener('scroll',scroll,true) }); watch(() => route.path,close)
</script>
<template><Teleport to="body"><aside v-if="term" ref="tooltip" id="study-term-preview" role="tooltip" class="term-preview" :style="position" @pointerenter="keepOpen" @pointerleave="close"><strong>{{ term.name }}</strong><p>{{ term.definition }}</p><span>Nhấn thuật ngữ để mở bài viết Wiki và các khái niệm liên quan.</span></aside></Teleport></template>
