<script setup>
import { nextTick, onMounted, onUnmounted, ref } from 'vue'

const props = defineProps({ topicId: { type: String, required: true } })
const active = ref('notes')
const tablist = ref(null)
const tabs = [{ id: 'notes', label: 'Notes' }, { id: 'bai-tap', label: 'Bài tập' }]
const tabId = id => `${props.topicId}-${id}`
const panelId = id => `${props.topicId}-panel-${id}`

async function syncHash() {
  let hash
  try { hash = decodeURIComponent(window.location.hash.slice(1)) } catch { return }
  const exercise = hash === 'bai-tap' || hash === `${props.topicId}-bai-tap`
  const changed = active.value !== (exercise ? 'bai-tap' : 'notes')
  active.value = exercise ? 'bai-tap' : 'notes'
  if (exercise && changed) {
    await nextTick()
    // Wait for Notes to leave the layout before positioning the shorter exercise panel.
    requestAnimationFrame(() => requestAnimationFrame(() => tablist.value?.scrollIntoView({ block: 'start', behavior: 'instant' })))
  }
}

function select(id) {
  if (active.value === id) return
  active.value = id
  const hash = id
  window.history.pushState(window.history.state, '', `#${hash}`)
  window.dispatchEvent(new Event('hashchange'))
}

function keyboard(event, index) {
  const next = { ArrowRight: (index + 1) % 2, ArrowLeft: (index + 1) % 2, Home: 0, End: 1 }[event.key]
  if (next === undefined) return
  event.preventDefault()
  select(tabs[next].id)
  tablist.value?.querySelectorAll('[role="tab"]')[next]?.focus()
}

onMounted(() => {
  syncHash()
  window.addEventListener('hashchange', syncHash)
  window.addEventListener('popstate', syncHash)
})
onUnmounted(() => {
  window.removeEventListener('hashchange', syncHash)
  window.removeEventListener('popstate', syncHash)
})
</script>

<template>
  <section class="philosophy-topic" :data-topic="topicId" :aria-labelledby="topicId">
    <div id="bai-tap" ref="tablist" class="philosophy-topic-tabs" role="tablist" :aria-labelledby="topicId">
      <button v-for="(tab, index) in tabs" :id="tabId(tab.id)" :key="tab.id" type="button" role="tab"
        :aria-selected="active === tab.id" :aria-controls="panelId(tab.id)" :tabindex="active === tab.id ? 0 : -1"
        @click="select(tab.id)" @keydown="keyboard($event, index)">{{ tab.label }}</button>
    </div>
    <section v-show="active === 'notes'" :id="panelId('notes')" class="philosophy-topic-panel" role="tabpanel" :aria-labelledby="tabId('notes')" tabindex="0">
      <slot v-if="active === 'notes'" name="notes" />
    </section>
    <section v-show="active === 'bai-tap'" :id="panelId('bai-tap')" class="philosophy-topic-panel philosophy-topic-exercises" role="tabpanel" :aria-labelledby="tabId('bai-tap')" tabindex="0">
      <slot v-if="active === 'bai-tap'" name="exercises" />
    </section>
  </section>
</template>

<style scoped>
.philosophy-topic { min-width: 0; }
.philosophy-topic-tabs { display: flex; gap: var(--space-5); border-bottom: 1px solid var(--rule); margin-bottom: var(--space-5); font-family: var(--font-ui); scroll-margin-top: 120px; }
.philosophy-topic-tabs button { min-height: 48px; padding: var(--space-2) var(--space-3); border-bottom: 2px solid transparent; color: var(--ink-2); font-size: var(--fs-ui); cursor: pointer; }
.philosophy-topic-tabs button[aria-selected="true"] { color: var(--tim); border-color: var(--tim); font-weight: 600; }
.philosophy-topic-tabs button:hover { color: var(--tim); background: var(--tim-soft); }
.philosophy-topic-tabs button:focus-visible, .philosophy-topic-panel:focus-visible { outline: 2px solid var(--tim); outline-offset: 3px; }
.philosophy-topic-panel { min-width: 0; }
.philosophy-topic-panel :deep(.philosophy-figure) { margin: var(--space-6) 0; }
.philosophy-topic-panel :deep(.philosophy-figure img) { display: block; max-width: 100%; max-height: 560px; width: auto; height: auto; margin-inline: auto; object-fit: contain; border-radius: var(--radius-sm); }
.philosophy-topic-panel :deep(.philosophy-figure figcaption) { margin-top: var(--space-3); color: var(--ink-2); font: var(--fs-small)/1.8 var(--font-ui); text-align: center; }
</style>
