import { nextTick, onMounted, onUnmounted, ref, watch } from 'vue'

/** Keep the selected tab visible without moving the document's reading position. */
export function useActiveTabVisibility(active) {
  const tabList = ref(null)
  let observer
  let disposed = false

  async function reveal() {
    await nextTick()
    if (disposed) return
    const list = tabList.value
    const selected = list?.querySelector('[aria-current="page"]')
    if (!selected) return
    const bounds = list.getBoundingClientRect()
    const item = selected.getBoundingClientRect()
    const gutter = 12
    if (item.left < bounds.left + gutter) list.scrollLeft += item.left - bounds.left - gutter
    else if (item.right > bounds.right - gutter) list.scrollLeft += item.right - bounds.right + gutter
  }

  watch(active, reveal, { flush: 'post' })
  onMounted(() => {
    reveal()
    observer = new ResizeObserver(reveal)
    if (tabList.value) observer.observe(tabList.value)
    document.fonts.ready.then(reveal)
  })
  onUnmounted(() => { disposed = true; observer?.disconnect() })
  return tabList
}
