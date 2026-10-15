import { ref, onMounted, onUnmounted } from 'vue'
import {
  DEFAULT_WORKSPACE_TABS,
  parseTabFromHash,
  formatTabHash
} from '../services/workspaceService.mjs'

export function useWorkspaceTabs(initialTabs = DEFAULT_WORKSPACE_TABS) {
  const tabs = initialTabs
  const active = ref(tabs[0]?.id || 'flashcards')

  function changeTab(id) {
    active.value = id
    if (typeof window !== 'undefined' && window.history?.replaceState) {
      window.history.replaceState(null, '', formatTabHash(id))
    }
  }

  function syncHash() {
    if (typeof window === 'undefined') return
    const id = parseTabFromHash(window.location.hash, tabs, active.value)
    active.value = id
  }

  onMounted(() => {
    syncHash()
    if (typeof window !== 'undefined') {
      window.addEventListener('hashchange', syncHash)
    }
  })

  onUnmounted(() => {
    if (typeof window !== 'undefined') {
      window.removeEventListener('hashchange', syncHash)
    }
  })

  return {
    tabs,
    active,
    changeTab,
    syncHash
  }
}
