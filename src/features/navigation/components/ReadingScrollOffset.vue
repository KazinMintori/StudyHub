<script setup>
import { nextTick, onMounted, onUnmounted, ref } from 'vue'
import { onContentUpdated, useData } from 'vitepress'

const { frontmatter } = useData()
const height = ref(134)
let observer
let disposed = false

function measure() {
  if (!['lecture', 'topic'].includes(frontmatter.value.section)) {
    height.value = 134 // Preserve VitePress's default offset on other pages.
    return
  }
  let bottom = 0
  for (const element of document.querySelectorAll('.VPNav, .VPLocalNav, .lecture-tabs')) {
    const style = getComputedStyle(element)
    if (style.display === 'none' || !['fixed', 'sticky'].includes(style.position)) continue
    // Use the sticky inset, not the element's current position in the article.
    bottom = Math.max(bottom, (parseFloat(style.top) || 0) + element.getBoundingClientRect().height)
  }
  height.value = bottom + 16
}

function observe() {
  if (disposed) return
  observer?.disconnect()
  observer = new ResizeObserver(measure)
  for (const element of document.querySelectorAll('.VPNav, .VPLocalNav, .lecture-tabs')) observer.observe(element)
  measure()
}

onMounted(() => {
  observe()
  window.addEventListener('resize', measure)
  // On a statically rendered deep link, VitePress can calculate the initial
  // offset before hydration. Correct a covered heading once the chrome exists.
  const initialHash = window.location.hash
  nextTick(async () => {
    await document.fonts.ready
    requestAnimationFrame(() => requestAnimationFrame(() => {
    if (disposed || window.location.hash !== initialHash || !initialHash) return
    let target
    try { target = document.getElementById(decodeURIComponent(initialHash.slice(1))) } catch { return }
    if (!target?.matches('h2, h3, h4')) return
    measure()
    const top = target.getBoundingClientRect().top
    if (top >= 0 && top < height.value) window.scrollTo({ top: window.scrollY + top - height.value, behavior: 'instant' })
    }))
  })
})
onContentUpdated(async () => {
  await nextTick()
  observe()
})
onUnmounted(() => {
  disposed = true
  observer?.disconnect()
  window.removeEventListener('resize', measure)
})
</script>

<template>
  <span class="reading-scroll-offset" aria-hidden="true" :style="{ height: `${height}px` }" />
</template>

<style scoped>
/* VitePress measures this noninteractive marker for anchor navigation. */
.reading-scroll-offset { position: fixed; top: 0; left: 0; width: 0; visibility: hidden; pointer-events: none; }
</style>
